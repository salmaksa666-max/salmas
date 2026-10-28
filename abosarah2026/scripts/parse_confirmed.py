# -*- coding: utf-8 -*-
"""Parse "SMLE Confirmed Infographics" PDF -> data/confirmed12.json + one infographic JPEG per disease.

usage: python3 parse_confirmed.py SRC.pdf OUT_JSON IMG_DIR
Run with /usr/bin/python3 (pdfplumber, pypdfium2, pillow).
"""
import json
import os
import re
import sys

import pdfplumber
import pypdfium2 as pdfium
from PIL import Image

SRC, OUT_JSON, IMG_DIR = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(IMG_DIR, exist_ok=True)

pdf = pdfplumber.open(SRC)
lines = []
for pn, pg in enumerate(pdf.pages):
    for l in pg.extract_text_lines():
        c = l["chars"][0]
        lines.append(dict(p=pn, top=l["top"], bot=l["bottom"], x0=l["x0"], size=round(c["size"], 1),
                          bold="Bold" in c["fontname"], text=l["text"].strip()))

specialty, disease = None, None
diseases, questions = [], []
cur = None
section = None
i = 0
OPT = re.compile(r"^([A-E])\.\s+(.*?)(\s*✓\s*correct)?$")


def new_disease(title, p, top):
    d = dict(id=len(diseases) + 1, specialty=specialty, title=title, page=p, top=top, first_q=None)
    diseases.append(d)
    return d


while i < len(lines):
    l = lines[i]
    t = l["text"]
    if l["size"] == 24 and l["bold"] and l["p"] > 2:
        specialty = t
    elif l["size"] == 15.0 and l["bold"] and l["p"] > 2:
        title = t
        while i + 1 < len(lines) and lines[i + 1]["size"] == 15.0 and lines[i + 1]["p"] == l["p"] and lines[i + 1]["top"] - lines[i]["top"] < 25:
            i += 1
            title += " " + lines[i]["text"]
        if diseases and diseases[-1]["first_q"] is None and l["p"] == diseases[-1]["page"] + 1:
            title = diseases.pop()["title"] + " " + title  # heading split across a page break
        disease = new_disease(title, l["p"], l["top"])
        cur = None
    elif re.match(r"^CSEP-\d+", t) and l["size"] == 8.5:
        m = re.match(r"^(CSEP-\d+)\s*(.*)$", t)
        cur = dict(qid=m.group(1), unconfirmed="not fully confirmed" in m.group(2), specialty=specialty,
                   disease=disease["id"], stem="", opts={}, why={}, correct="", right="", kc="", ep="",
                   _last=None, p=l["p"], top=l["top"])
        if disease["first_q"] is None:
            disease["first_q"] = (l["p"], l["top"])
        questions.append(cur)
        section = "stem"
    elif cur is not None and l["size"] >= 8:
        om = OPT.match(t) if (l["bold"] and l["size"] == 10.5) else None
        if t.startswith("Why this is right."):
            section = "right"
            cur["right"] = t[len("Why this is right."):].strip()
        elif t.startswith("Key concept."):
            section = "kc"
            cur["kc"] = t[len("Key concept."):].strip()
        elif t.startswith("Exam pearl."):
            section = "ep"
            cur["ep"] = t[len("Exam pearl."):].strip()
        elif section in ("stem", "opt") and om:
            section = "opt"
            k = om.group(1)
            cur["opts"][k] = om.group(2).strip()
            cur["_last"] = k
            if om.group(3):
                cur["correct"] = k
        elif section == "opt" and l["bold"] and l["size"] == 10.5 and cur["_last"] and not cur["why"].get(cur["_last"]):
            cur["opts"][cur["_last"]] += " " + t
        elif section == "opt":
            k = cur["_last"]
            cur["why"][k] = (cur["why"].get(k, "") + " " + re.sub(r"^Why wrong:\s*", "", t)).strip()
        elif section == "stem":
            cur["stem"] = (cur["stem"] + " " + t).strip()
        elif section in ("right", "kc", "ep"):
            cur[section] = (cur[section] + " " + t).strip()
    i += 1

for q in questions:
    q.pop("_last", None)

# ---- infographic crops
doc = pdfium.PdfDocument(SRC)
SCALE = 1.5
cache = {}


def page_img(p):
    if p not in cache:
        cache[p] = doc[p].render(scale=SCALE).to_pil().convert("RGB")
    return cache[p]


def trim_blank(im, top=True):
    """cut white rows at the bottom (and top) ignoring the outer frame lines"""
    px = im.load()
    w, h = im.size

    def blank(y):
        return all(sum(px[x, y]) >= 735 for x in range(70, w - 70, 3))

    y1 = h
    while y1 > 1 and blank(y1 - 1):
        y1 -= 1
    y0 = 0
    if top:
        while y0 < y1 - 1 and blank(y0):
            y0 += 1
    return im.crop((0, max(0, y0 - 4), w, min(h, y1 + 8)))


for d in diseases:
    if not d["first_q"]:
        continue
    p0, y0 = d["page"], max(0, d["top"] - 12)
    pq, yq = d["first_q"]
    parts = []
    for p in range(p0, pq + 1):
        im = page_img(p)
        top = int(y0 * SCALE) if p == p0 else 0
        bot = int((yq - 18) * SCALE) if p == pq else im.size[1]
        if bot - top < 20:
            continue
        seg = trim_blank(im.crop((0, top, im.size[0], bot)), top=(p != p0))
        if seg.size[1] > 30:
            parts.append(seg)
    w = max(s.size[0] for s in parts)
    H = sum(s.size[1] for s in parts)
    canvas = Image.new("RGB", (w, H), "white")
    y = 0
    for s in parts:
        canvas.paste(s, (0, y))
        y += s.size[1]
    # crop horizontal margins
    canvas = canvas.crop((int(30 * SCALE), 0, w - int(30 * SCALE), H))
    d["img"] = f"cf12_{d['id']:03d}.jpg"
    canvas.save(os.path.join(IMG_DIR, d["img"]), quality=72, optimize=True)
    d["first_q"] = list(d["first_q"])

json.dump(dict(diseases=diseases, questions=questions), open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("diseases", len(diseases), "questions", len(questions))
bad = [q["qid"] for q in questions if q["correct"] == "" or len(q["opts"]) < 2 or not q["stem"]]
print("problem questions:", len(bad), bad[:20])
