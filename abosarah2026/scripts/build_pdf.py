# -*- coding: utf-8 -*-
"""Print-friendly PDFs: one file per specialty, 10 questions per page, black & white.

usage: build_pdf.py SRC.apkg OUT_DIR [PER_PAGE]
Needs the headless chromium that ships in /opt/pw-browsers.
"""
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
PER_PAGE = int(sys.argv[3]) if len(sys.argv) > 3 else 10
CHROME = sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))[-1]

CSS = """
@page { size: A4; margin: 8mm; }
* { box-sizing: border-box; }
html, body { width: 194mm; }
body { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 8.8pt; line-height: 1.3; color: #000; background: #fff; margin: 0; }
.page { height: 281mm; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: repeat(5, minmax(0, 1fr)); gap: 0 5mm; break-after: page; overflow: hidden; }
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


FIT = """<script>
document.querySelectorAll('.page').forEach(function(pg){
  var fs = 8.8;
  pg.style.fontSize = fs + 'pt';
  while (fs > 4.6 && [...pg.querySelectorAll('.q')].some(function(q){ return q.scrollHeight > q.clientHeight + 1; })) {
    fs -= 0.2; pg.style.fontSize = fs + 'pt';
  }
});
</script>"""


def load(src):
    d = tempfile.mkdtemp()
    zipfile.ZipFile(src).extract("collection.anki2", d)
    c = sqlite3.connect(os.path.join(d, "collection.anki2"))
    decks = {k: v["name"] for k, v in json.loads(c.execute("select decks from col").fetchone()[0]).items()}
    model = list(json.loads(c.execute("select models from col").fetchone()[0]).values())[0]
    names = [f["name"] for f in model["flds"]]
    rows = c.execute("select n.flds, c.did from notes n join cards c on c.nid = n.id").fetchall()
    return [(dict(zip(names, f.split("\x1f"))), decks[str(did)]) for f, did in rows]


def memo_of(explain):
    m = re.search(r'<div id="memo"[^>]*>(.*?)</div>', explain or "", re.S)
    return m.group(1) if m else ""


def card(i, f):
    ans = f["Correct"]
    opts = "".join(
        f'<div class="o{" ok" if k == ans else ""}"><bdi dir="ltr">{k}. {html.escape(re.sub(r"<[^>]+>", "", f["Opt" + k]))}</bdi></div>'
        for k in "ABCD" if f["Opt" + k].strip()
    )
    memo = memo_of(f["Explain"])
    memo_html = f'<div class="memo">{memo}</div>' if memo else ""
    return (
        f'<div class="q"><div class="hd">{i}) <span>{f["QID"]}</span></div>'
        f'<div class="stem" dir="ltr">{f["Question"]}</div>{opts}{memo_html}</div>'
    )


def main():
    os.makedirs(OUT, exist_ok=True)
    by = {}
    for f, deck in load(SRC):
        if "المشكوك" in deck or f["Correct"] not in list("ABCD"):
            continue
        by.setdefault(deck.split("::")[-1], []).append(f)
    for name, cards in sorted(by.items()):
        cards.sort(key=lambda f: f["QID"])
        pages = []
        for p in range(0, len(cards), PER_PAGE):
            chunk = cards[p:p + PER_PAGE]
            pages.append('<div class="page">' + "".join(card(p + j + 1, f) for j, f in enumerate(chunk)) + "</div>")
        doc = f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}{FIT}</body></html>'
        safe = re.sub(r"[^\w\-]+", "_", name)
        src = os.path.join(tempfile.mkdtemp(), "x.html")
        open(src, "w", encoding="utf-8").write(doc)
        if os.environ.get("CHECK"):
            chk = doc.replace("</body>", "<script>document.title=[...document.querySelectorAll('.q')].filter(q=>q.scrollHeight>q.clientHeight+1).length</script></body>")
            open(src + ".chk.html", "w", encoding="utf-8").write(chk)
            out = subprocess.run([CHROME, "--no-sandbox", "--dump-dom", "file://" + src + ".chk.html"], capture_output=True, text=True).stdout
            print("  overflowing cards:", re.search(r"<title>(.*?)</title>", out).group(1))
        pdf = os.path.join(OUT, f"{safe}.pdf")
        subprocess.run([CHROME, "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", "file://" + src],
                       check=True, capture_output=True)
        print(name, len(cards), "questions ->", pdf)


main()
