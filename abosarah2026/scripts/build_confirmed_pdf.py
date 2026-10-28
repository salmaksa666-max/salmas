# -*- coding: utf-8 -*-
"""Print PDFs (B&W) for SMLE Confirmed Part 12: one file per specialty, each disease = its map page(s) then
its questions, 10 per page.

usage: build_confirmed_pdf.py APKG DATA_JSON IMG_DIR OUT_DIR
"""
import base64
import glob
import html
import json
import os
import re
import sqlite3
import subprocess
import sys
import tempfile
import zipfile

APKG, DATA, IMG_DIR, OUT = sys.argv[1:5]
CHROME = sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))[-1]
FILES = {"Surgery": "01_Surgery", "Medicine": "02_Medicine", "Pediatrics": "03_Pediatrics",
         "Other, Psychiatry and OB/GYN": "04_Other_Psych_OBGYN"}

CSS = """
@page { size: A4; margin: 8mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 8.8pt; line-height: 1.3; color: #000; background: #fff; margin: 0; }
.page { height: 281mm; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: repeat(5, 1fr); gap: 0 5mm; break-after: page; overflow: hidden; }
.page:last-child { break-after: auto; }
.q { border-bottom: 0.4pt solid #000; padding: 1.2mm 0 1.4mm; overflow: hidden; }
.hd { font-weight: bold; font-size: .9em; margin-bottom: .6mm; }
.hd span { float: right; font-weight: normal; }
.stem { margin-bottom: .8mm; }
mark { background: #fff; color: #000; }
mark.l1 { background: #dcdcdc; }
mark.l2 { background: #b4b4b4; font-weight: bold; text-decoration: underline; }
.o { padding-left: 3.2mm; text-indent: -3.2mm; }
.o.ok { font-weight: bold; border: 0.6pt solid #000; padding-left: 3.6mm; border-radius: 1mm; }
.memo { margin-top: .8mm; font-size: .92em; border-left: 1.2pt solid #000; padding-left: 1.5mm; }
.memo b { font-weight: bold; }
"""
CSS += """
.page.map { display: flex; flex-direction: column; align-items: center; justify-content: flex-start; }
.page.map h2 { font-size: 13pt; margin: 0 0 2mm; align-self: flex-start; }
.page.map img { max-width: 194mm; max-height: 268mm; filter: grayscale(1) contrast(1.15); }
.page.qs { grid-template-rows: auto repeat(5, 1fr); }
.ph { grid-column: 1 / 3; font-weight: bold; font-size: 10pt; border-bottom: 1.2pt solid #000; padding-bottom: 1mm; margin-bottom: 1mm; }
"""

FIT = """<script>
document.querySelectorAll('.page.qs').forEach(function(pg){
  var fs = 8.8;
  pg.style.fontSize = fs + 'pt';
  while (fs > 5.5 && [...pg.querySelectorAll('.q')].some(function(q){ return q.scrollHeight > q.clientHeight + 1; })) {
    fs -= 0.2; pg.style.fontSize = fs + 'pt';
  }
});
</script>"""


def load():
    d = tempfile.mkdtemp()
    zipfile.ZipFile(APKG).extract("collection.anki2", d)
    c = sqlite3.connect(os.path.join(d, "collection.anki2"))
    decks = {k: v["name"] for k, v in json.loads(c.execute("select decks from col").fetchone()[0]).items()}
    model = list(json.loads(c.execute("select models from col").fetchone()[0]).values())[0]
    names = [f["name"] for f in model["flds"]]
    out = []
    for flds, tags, did in c.execute("select n.flds, n.tags, c.did from notes n join cards c on c.nid = n.id"):
        f = dict(zip(names, flds.split("\x1f")))
        f["_dis"] = int(re.search(r"خريطة_(\d+)", tags).group(1))
        f["_doubt"] = "المشكوك" in decks[str(did)]
        out.append(f)
    return out


def card(i, f):
    ans = f["Correct"]
    stem = re.search(r'<div dir="ltr" style="text-align:left">(.*)</div>\s*$', f["Question"], re.S).group(1)
    opts = "".join(
        f'<div class="o{" ok" if k == ans else ""}"><bdi dir="ltr">{k}. {html.escape(re.sub(r"<[^>]+>", "", f["Opt" + k]))}</bdi></div>'
        for k in "ABCD" if f["Opt" + k].strip()
    )
    m = re.search(r'<div id="memo"[^>]*>(.*?)</div>', f["Explain"], re.S)
    memo = f'<div class="memo">{m.group(1)}</div>' if m else ""
    flag = " ⚠ المصدر مو متأكد" if f["_doubt"] else ""
    return (f'<div class="q"><div class="hd">{i}) <span>{f["QID"]}{flag}</span></div>'
            f'<div class="stem" dir="ltr">{stem}</div>{opts}{memo}</div>')


def main():
    os.makedirs(OUT, exist_ok=True)
    data = json.load(open(DATA, encoding="utf-8"))
    dis = {d["id"]: d for d in data["diseases"]}
    cards = load()
    by = {}
    for f in cards:
        by.setdefault(f["_dis"], []).append(f)
    for spec, fname in FILES.items():
        pages = []
        for d in [d for d in data["diseases"] if d["specialty"] == spec]:
            fs = sorted(by.get(d["id"], []), key=lambda f: f["QID"])
            if not fs:
                continue
            title = html.escape(d["title"])
            img = os.path.join(IMG_DIR, d.get("img") or "")
            if d.get("img") and os.path.exists(img):
                b64 = base64.b64encode(open(img, "rb").read()).decode()
                pages.append(f'<div class="page map"><h2>🗺 {title}</h2><img src="data:image/jpeg;base64,{b64}"></div>')
            for p in range(0, len(fs), 10):
                body = "".join(card(p + j + 1, f) for j, f in enumerate(fs[p:p + 10]))
                pages.append(f'<div class="page qs"><div class="ph">{title}</div>{body}</div>')
        doc = f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}{FIT}</body></html>'
        src = os.path.join(tempfile.mkdtemp(), "x.html")
        open(src, "w", encoding="utf-8").write(doc)
        pdf = os.path.join(OUT, f"Confirmed_{fname}.pdf")
        subprocess.run([CHROME, "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", "file://" + src],
                       check=True, capture_output=True)
        print(fname, len(pages), "pages ->", pdf)


main()
