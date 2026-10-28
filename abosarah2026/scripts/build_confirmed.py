# -*- coding: utf-8 -*-
"""Anki deck from SMLE Confirmed Infographics (Sept 2026 Part 12).

usage: python3 build_confirmed.py DATA_JSON IMG_DIR OUT.apkg
Each card keeps its disease infographic (collapsed on the front: read it before solving).
"""
import collections
import glob
import html
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import genanki
import json

import build_apkg as B

DATA, IMG_DIR, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
SOURCE = "SMLE Confirmed Sept 2026 Part 12"
ROOT = "Months::9 September::Confirmed Part 12"
SPEC = {"Surgery": "01- Surgery", "Medicine": "02- Medicine", "Pediatrics": "03- Pediatrics",
        "Other, Psychiatry and OB/GYN": "04- Other, Psych & OBGYN"}
DOUBT = ROOT + "::⚠ المشكوك فيهم"

STOP = set("""a an the and or of to in on at for with without by from as is are was were be been being has have had
her his she he they them their it its this that these those which what who whom when where why how
patient patients presents presented presenting came comes come complains complaining complained known
following most likely next step steps best appropriate management manage diagnosis diagnose what's
year years old yo man woman male female boy girl child baby history examination exam found also
there than then after before during while since about into over under up down not no yes any all
one two three four five due given give gives taking took take most more less very mild severe
case cases""".split())

JUNK_ANS = re.compile(r"not recalled", re.I)


def norm(s):
    return re.sub(r"[^a-z0-9% ]+", " ", s.lower())


def tokens(stem):
    return [(m.start(), m.end(), m.group(0)) for m in re.finditer(r"[A-Za-z0-9][A-Za-z0-9'\-./%]*", stem)]


def load_clues():
    out = {}
    for f in sorted(glob.glob(os.path.join(os.path.dirname(DATA), "cf12_clues", "*.txt"))):
        for ln in open(f, encoding="utf-8"):
            if not ln.strip():
                continue
            parts = [x.strip() for x in ln.split("|")]
            parts += [""] * (3 - len(parts))
            split = lambda t: [p.strip() for p in t.split(" ;; ") if p.strip()]
            out["CSEP-" + parts[0]] = (split(parts[1]), split(parts[2]))
    return out


CLUES = load_clues()


def clue_terms(qid):
    return CLUES[qid]


def short(t):
    w = t.split()[:5]
    while w and w[-1].lower().strip(",.;:") in STOP:
        w.pop()
    return " ".join(w).strip(" ,.;:")


def esc(t):
    return html.escape(t, quote=False)


data = json.load(open(DATA, encoding="utf-8"))
dis = {d["id"]: d for d in data["diseases"]}
decks, media, stats = {}, set(), collections.Counter()
order = {n: i for i, n in enumerate(SPEC)}

for q in sorted(data["questions"], key=lambda q: (order.get(q["specialty"], 9), q["disease"], q["qid"])):
    d = dis[q["disease"]]
    opts = {k: v for k, v in q["opts"].items() if v.strip()}
    letter = q["correct"]
    stem_raw = re.sub(r"\s+A\. Why wrong:.*$", "", q["stem"])
    if "A" not in opts and "A. Why wrong" in q["stem"]:
        opts = {"A": "(option not recalled)", **opts}
    in_stem = len(opts) < 2 or len(opts) > 4
    q["ep"] = re.sub(r"\s*\d+ topics?, \d+ questions?\s*$", "", q["ep"])
    lvl2, lvl1 = clue_terms(q["qid"])
    stem = B.highlight_memorize(esc(stem_raw), [esc(t) for t in lvl2], [esc(t) for t in lvl1])
    if in_stem:
        stem += "".join(f"<br>{k}. {esc(v)}" for k, v in opts.items())
        opts = {}
        stats["options_in_stem"] += 1

    img = d.get("img")
    front_top = f'<div class="dz" dir="ltr" style="text-align:left;font-weight:bold;margin-bottom:6px">📌 {esc(d["title"])}</div>'
    if img and os.path.exists(os.path.join(IMG_DIR, img)):
        media.add(img)
        front_top += (f'<details class="map" style="margin:4px 0 10px;border:1px solid #3e5a4f;border-radius:8px;padding:4px 8px">'
                      f'<summary style="cursor:pointer;color:#9fd1b8">🗺 الخريطة — اقرئيها قبل ما تحلين ▾</summary>'
                      f'<img src="{img}" style="max-width:100%;background:#fff;border-radius:6px;margin-top:6px"></details>')
    question = front_top + f'<div dir="ltr" style="text-align:left">{stem}</div>'

    ans_txt = opts.get(letter, "") if letter else ""
    if not ans_txt and letter:
        ans_txt = q["opts"].get(letter, "")
    memo = ""
    if letter and ans_txt and not JUNK_ANS.search(ans_txt):
        LEAD = ("next step", "most appropriate", "what to do", "appropriate next", "most likely", "management plan",
                "next best", "what will you", "appropriate management", "most important", "cause of this")
        clues = [c.strip(" ,.;:") for c in lvl2 + lvl1
                 if c.strip(" ,.;:") and not any(w in c.lower() for w in LEAD)]
        clues = (clues or [c.strip(" ,.;:") for c in lvl2 + lvl1])[:5]
        ans_clean = ans_txt.strip(" .")
        line, used = "", []
        for c in clues:
            cand = " + ".join(used + [c]) + " \u2192 " + ans_clean
            if len(cand) > 150 and used:
                break
            used.append(c)
        if used:
            line = " + ".join(used) + " \u2192 " + ans_clean
        if line:
            memo = f'<div id="memo" dir="rtl"><b>احفظي:</b> <bdi dir="ltr">{esc(line)}</bdi></div>'
            stats["memo"] += 1

    parts = []
    if not letter:
        parts.append('<div class="star-badge">⭐ المصدر ما حط جواب مؤكد لهذا السؤال</div>')
    elif q["unconfirmed"]:
        parts.append('<div class="star-badge">⚠ حتى المصدر نفسه مو متأكد 100% من هذا الجواب</div>')
    if letter and in_stem:
        parts.append(f'<p><b>الجواب:</b> <bdi dir="ltr">{letter}. {esc(q["opts"].get(letter, ""))}</bdi></p>')
    if q["right"]:
        parts.append(f'<p><b>ليش الجواب صح:</b></p><div dir="ltr" style="text-align:left">{esc(q["right"])}</div>')
    body = (f'<div class="kc">{esc(q["kc"])}</div>' if q["kc"] else "") + (
        f'<p class="pearl"><b>Exam pearl:</b> {esc(q["ep"])}</p>' if q["ep"] else "")
    if body:
        parts.append(f'<details class="topic"><summary>ملخص الموضوع ▾</summary><div class="topic-body" dir="ltr">{body}</div></details>')
    parts.append(f'<p class="src">المصدر: {SOURCE}، السؤال رقم {q["qid"]} — {esc(d["title"])}</p>')
    explain = memo + "".join(parts)

    why = {k: ("" if (k == letter or not q["why"].get(k)) else
               f'<span dir="ltr" style="display:block;text-align:left">{esc(q["why"][k])}</span>') for k in "ABCD"}
    deck_name = ROOT + "::" + SPEC.get(q["specialty"], q["specialty"])
    if not letter or q["unconfirmed"]:
        deck_name = DOUBT
        stats["doubtful"] += 1
    if deck_name not in decks:
        decks[deck_name] = genanki.Deck(B.deck_id_for("cf12::" + deck_name), deck_name)
    tags = ["مشكوك_الجواب"] if deck_name == DOUBT else []
    tags.append("خريطة_" + str(d["id"]))
    fields = [question] + [opts.get(k, "") for k in "ABCD"] + [why[k] for k in "ABCD"] + [letter, explain, q["qid"]]
    decks[deck_name].add_note(genanki.Note(model=B.MODEL, fields=fields, guid=genanki.guid_for("cf12", q["qid"]), tags=tags))
    stats["notes"] += 1

pkg = genanki.Package(list(decks.values()))
pkg.media_files = [os.path.join(IMG_DIR, m) for m in sorted(media)]
pkg.write_to_file(OUT)
print(dict(stats), "media", len(media), "size MB", round(os.path.getsize(OUT) / 1e6, 1))
for k, v in sorted(decks.items()):
    print(len(v.notes), k)
