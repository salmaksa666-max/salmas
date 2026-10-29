# -*- coding: utf-8 -*-
"""Dense print PDF for an MKJ-style apkg (old-format collection.anki21): questions packed in columns,
answer key after every 3 pages.  usage: build_mkj_dense.py SRC.apkg OUT.pdf"""
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

SRC, OUT = sys.argv[1], sys.argv[2]
CHROME = sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))[-1]
CAP = int(os.environ.get("CAP", "6500"))

CSS = """
@page { size: A4; margin: 8mm; }
* { box-sizing: border-box; }
html, body { width: 194mm; }
body { font-family: "DejaVu Sans", Arial, sans-serif; line-height: 1.3; color: #000; margin: 0; }
.page { height: 281mm; display: block; column-count: 2; column-gap: 6mm; column-fill: auto; break-after: page; overflow: hidden; }
.ph { column-span: all; font-weight: bold; font-size: 10pt; border-bottom: 1.2pt solid #000; margin-bottom: 1mm; }
.q { break-inside: avoid; border-bottom: 0.4pt solid #000; padding: 1.2mm 0 1.4mm; }
.hd { font-weight: bold; font-size: .9em; margin-bottom: .6mm; }
.hd span { float: right; font-weight: normal; }
.o { padding-left: 3.2mm; text-indent: -3.2mm; }
.page.ak { column-count: 3; }
.it { break-inside: avoid; margin-bottom: 1.2mm; border-bottom: 0.3pt dashed #000; padding-bottom: .8mm; font-weight: bold; }
"""
FIT = """<script>
document.querySelectorAll('.page').forEach(function(pg){
  var fs = 8.4; pg.style.fontSize = fs + 'pt';
  while (fs > 4.6 && pg.scrollWidth > pg.clientWidth + 2) { fs -= 0.2; pg.style.fontSize = fs + 'pt'; }
});
</script>"""


def plain(h):
    return html.unescape(re.sub(r"<[^>]+>", "", h or "")).strip()


d = tempfile.mkdtemp()
zipfile.ZipFile(SRC).extract("collection.anki21", d)
c = sqlite3.connect(os.path.join(d, "collection.anki21"))
model = list(json.loads(c.execute("select models from col").fetchone()[0]).values())[0]
names = [f["name"] for f in model["flds"]]
rows = [dict(zip(names, r[0].split("\x1f"))) for r in c.execute("select flds from notes order by id")]

items = []
for r in rows:
    qh = r["OriginalQuestionHTML"]
    m = re.search(r'<div class="question-stem-text">(.*?)</div>', qh, re.S)
    stem = re.sub(r"^\s*\d+\.\s*", "", plain(m.group(1) if m else qh.split('<div class="question-options">')[0]))
    opts = re.findall(r'<div class="source-option" data-letter="([A-Z])">(.*?)</div>', qh, re.S)
    opts = [(k, re.sub(r"^[A-E]\.\s*", "", plain(t))) for k, t in opts]
    sa = r["SourceAnswer"].strip()
    flag = " ⚠" if r["AnswerState"] != "confirmed" or not sa else ""
    items.append(dict(qid=r["QNo"], stem=stem, opts=opts, ans=sa or "— no firm answer in the source", flag=flag))

w = lambda it: len(it["stem"]) + sum(len(t) + 6 for _, t in it["opts"])
chunks, cur, tot = [], [], 0
for it in items:
    if cur and (len(cur) >= 16 or tot + w(it) > CAP):
        chunks.append(cur); cur, tot = [], 0
    cur.append(it); tot += w(it)
if cur:
    chunks.append(cur)

pages, num = [], 0
for g in range(0, len(chunks), 3):
    ak, first = "", num + 1
    for ch in chunks[g:g + 3]:
        start, body = num + 1, ""
        for it in ch:
            num += 1
            o = "".join(f'<div class="o"><bdi dir="ltr">{k}. {html.escape(t)}</bdi></div>' for k, t in it["opts"])
            if not it["opts"]:
                o = ""
            body += (f'<div class="q"><div class="hd">{num}) <span>{it["qid"]}</span></div>'
                     f'<div dir="ltr">{html.escape(it["stem"])}</div>{o}</div>')
            ak += f'<div class="it" dir="ltr">{num}) ✔ {html.escape(it["ans"])}{it["flag"]}</div>'
        pages.append(f'<div class="page"><div class="ph">Questions {start}–{num}</div>{body}</div>')
    pages.append(f'<div class="page ak"><div class="ph">Answers {first}–{num}</div>{ak}</div>')

doc = f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}{FIT}</body></html>'
src = os.path.join(tempfile.mkdtemp(), "x.html")
open(src, "w", encoding="utf-8").write(doc)
subprocess.run([CHROME, "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={OUT}", "file://" + src], check=True, capture_output=True)
print(len(items), "questions,", len(pages), "pages ->", OUT)
