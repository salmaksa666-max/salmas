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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import annot

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
.ref { font-size: .82em; font-style: italic; color: #444; }
html, body { width: 194mm; }
.page.map { display: flex; align-items: center; justify-content: center; }
.page.map img { width: 194mm; max-height: 280mm; object-fit: contain; filter: grayscale(1) contrast(1.15); }
.page.qs, .page.sol { grid-template-rows: auto repeat(5, minmax(0, 1fr)); }
.ph { grid-column: 1 / 3; font-weight: bold; font-size: 10pt; border-bottom: 1.2pt solid #000; padding-bottom: 1mm; margin-bottom: 1mm; }
.dz { font-size: .85em; font-style: italic; }
.page.tr { display: block; column-count: 2; column-gap: 6mm; column-fill: auto; padding-top: 1mm; }
.page.tr h1 { column-span: all; font-size: 11pt; margin: 0 0 2mm; border-bottom: 1.2pt solid #000; }
.page.tr h3 { font-size: 1.05em; margin: 2.5mm 0 .8mm; border-bottom: 0.5pt solid #000; break-after: avoid; }
.page.tr ol { margin: 0; padding-left: 5mm; }
.page.tr li { margin-bottom: 1mm; break-inside: avoid; }
.sol .q { border-bottom: 0.4pt dashed #000; }
.ans { font-weight: bold; border: 0.6pt solid #000; border-radius: 1mm; padding: 0 1.5mm; display: inline-block; margin-bottom: .6mm; }
.why, .pearl { margin-top: .6mm; }
"""

FIT = """<script>
document.querySelectorAll('.page.tr').forEach(function(pg){
  var fs = 8.8; pg.style.fontSize = fs + 'pt';
  while (fs > 5 && pg.scrollWidth > pg.clientWidth + 2) { fs -= 0.2; pg.style.fontSize = fs + 'pt'; }
});
document.querySelectorAll('.page.qs, .page.sol').forEach(function(pg){
  var fs = 8.8;
  pg.style.fontSize = fs + 'pt';
  while (fs > 4.6 && [...pg.querySelectorAll('.q')].some(function(q){ return q.scrollHeight > q.clientHeight + 1; })) {
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


def plain(h):
    return html.unescape(re.sub(r"<[^>]+>", "", h or "")).strip()


def question_cell(i, f, dtitle):
    stem = re.search(r'<div dir="ltr" style="text-align:left">(.*)</div>\s*$', f["Question"], re.S).group(1)
    stem = annot.annotate_html(stem)
    opts = "".join(f'<div class="o"><bdi dir="ltr">{k}. {annot.annotate_text(html.escape(plain(f["Opt" + k])), labs=False)}</bdi></div>'
                   for k in "ABCD" if f["Opt" + k].strip())
    return (f'<div class="q"><div class="hd">{i}) <span>{f["QID"]}</span></div>'
            f'<div class="dz" dir="ltr">{html.escape(dtitle)}</div>'
            f'<div class="stem" dir="ltr">{stem}</div>{opts}</div>')


def solution_cell(i, f):
    ans = f["Correct"]
    ex = f["Explain"]
    if ans and f["Opt" + ans].strip():
        a_txt = f"{ans}. {plain(f['Opt' + ans])}"
    else:
        m = re.search(r"<p><b>الجواب:</b> <bdi[^>]*>(.*?)</bdi>", ex, re.S)
        a_txt = plain(m.group(1)) if m else "— بدون جواب مؤكد من المصدر"
    memo = re.search(r'<div id="memo"[^>]*>(.*?)</div>', ex, re.S)
    right = re.search(r"<p><b>ليش الجواب صح:</b></p><div[^>]*>(.*?)</div>", ex, re.S)
    pearl = re.search(r'<p class="pearl"><b>Exam pearl:</b> (.*?)</p>', ex, re.S)
    flag = " ⚠ المصدر مو متأكد" if f["_doubt"] else ""
    out = f'<div class="q"><div class="hd">{i}) <span>{f["QID"]}{flag}</span></div>'
    out += f'<div class="ans" dir="ltr">✔ {html.escape(a_txt)}</div>'
    if memo:
        out += f'<div class="memo">{memo.group(1)}</div>'
    if right:
        out += f'<div class="why" dir="ltr"><b>Why:</b> {html.escape(plain(right.group(1)))}</div>'
    if pearl:
        out += f'<div class="pearl" dir="ltr"><b>Pearl:</b> {html.escape(plain(pearl.group(1)))}</div>'
    return out + "</div>"


def load_trapq():
    out = {}
    for f in sorted(glob.glob(os.path.join(os.path.dirname(DATA), "cf12_trapq", "*.txt"))):
        for ln in open(f, encoding="utf-8"):
            if "|" in ln:
                k, v = ln.split("|", 1)
                out[k.strip()] = v.strip()
    return out


TRAPQ = load_trapq()


def traps_page(batch, ep_of):
    import difflib
    out = '<div class="page tr"><h1>⚠ Traps — answer each one in your head, the answer is right below</h1>'
    for d, part, _ in batch:
        seen, items = [], []
        for f in part:
            t = ep_of.get(f["QID"], "")
            if t and not any(difflib.SequenceMatcher(None, t.lower(), x.lower()).ratio() > 0.8 for x in seen):
                seen.append(t)
                q = TRAPQ.get(f["QID"][5:], "")
                items.append(f'<li><b>{html.escape(q)}</b><br>{html.escape(t)}</li>' if q else f"<li>{html.escape(t)}</li>")
        if items:
            out += f'<h3 dir="ltr">{html.escape(d["title"])}</h3><ol dir="ltr">' + "".join(items) + "</ol>"
    return out + "</div>"



CSS += """
.page.qs { display: block; column-count: 2; column-gap: 6mm; column-fill: auto; }
.page.qs .ph { column-span: all; }
.page.qs .q { break-inside: avoid; overflow: visible; }
.page.ak { display: block; column-count: 3; column-gap: 6mm; column-fill: auto; }
.ak h1 { column-span: all; font-size: 10pt; margin: 0 0 2mm; border-bottom: 1.2pt solid #000; }
.ak .it { break-inside: avoid; margin-bottom: 1.2mm; border-bottom: 0.3pt dashed #000; padding-bottom: .8mm; }
.ak .memo { margin-top: .3mm; }
"""
FIT = FIT.replace("querySelectorAll('.page.qs, .page.sol')", "querySelectorAll('.nomatch')")
FIT = FIT.replace("querySelectorAll('.page.tr')", "querySelectorAll('.page.ak, .page.qs')")
FIT = FIT.replace("var fs = 8.8; pg.style.fontSize = fs + 'pt';\n  while (fs > 5 && pg.scrollWidth", "var fs = 8.4; pg.style.fontSize = fs + 'pt';\n  while (fs > 4.6 && pg.scrollWidth")


def ak_item(i, f):
    ans = f["Correct"]
    ex = f["Explain"]
    if ans and f["Opt" + ans].strip():
        a_txt = f"{ans}. {plain(f['Opt' + ans])}"
    else:
        m = re.search(r"<p><b>الجواب:</b> <bdi[^>]*>(.*?)</bdi>", ex, re.S)
        a_txt = plain(m.group(1)) if m else "— no firm answer in the source"
    memo = re.search(r'<div id="memo"[^>]*>(.*?)</div>', ex, re.S)
    flag = " ⚠" if f["_doubt"] else ""
    return (f'<div class="it"><b dir="ltr">{i}) \u2714 {html.escape(a_txt)}{flag}</b>'
            + "</div>")


CAP = int(os.environ.get("CAP", "6500"))


def main():
    os.makedirs(OUT, exist_ok=True)
    data = json.load(open(DATA, encoding="utf-8"))
    by = {}
    for f in load():
        by.setdefault(f["_dis"], []).append(f)
    dis = {d["id"]: d for d in data["diseases"]}
    for spec, fname in FILES.items():
        items = []
        for d in [d for d in data["diseases"] if d["specialty"] == spec]:
            for f in sorted(by.get(d["id"], []), key=lambda f: f["QID"]):
                items.append((d, f))
        def weight(f):
            return len(plain(f["Question"])) + sum(len(plain(f["Opt" + k])) + 6 for k in "ABCD")

        chunks, cur, w = [], [], 0
        for it in items:
            wt = weight(it[1])
            if cur and (len(cur) >= 16 or w + wt > CAP):
                chunks.append(cur)
                cur, w = [], 0
            cur.append(it)
            w += wt
        if cur:
            chunks.append(cur)
        pages, num = [], 0
        for g in range(0, len(chunks), 3):
            ak, first = "", num + 1
            for chunk in chunks[g:g + 3]:
                start = num + 1
                body = ""
                for d, f in chunk:
                    num += 1
                    body += question_cell(num, f, d["title"])
                    ak += ak_item(num, f)
                pages.append(f'<div class="page qs"><div class="ph">Questions {start}\u2013{num}</div>{body}</div>')
            pages.append(f'<div class="page ak"><h1>Answers {first}\u2013{num}</h1>{ak}</div>')
        doc = f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}{FIT}</body></html>'
        srcf = os.path.join(tempfile.mkdtemp(), "x.html")
        open(srcf, "w", encoding="utf-8").write(doc)
        chk = doc.replace("</body>", "<script>document.title=[...document.querySelectorAll('.q')].filter(q=>q.scrollHeight>q.clientHeight+1).length+'/'+Math.min(...[...document.querySelectorAll('.page.qs')].map(p=>parseFloat(p.style.fontSize)))+'/'+Math.min(...[...document.querySelectorAll('.page.ak')].map(p=>parseFloat(p.style.fontSize)))</script></body>")
        open(srcf + ".chk.html", "w", encoding="utf-8").write(chk)
        out = subprocess.run([CHROME, "--no-sandbox", "--dump-dom", "file://" + srcf + ".chk.html"], capture_output=True, text=True).stdout
        print("  clipped cells / min font(pt):", re.search(r"<title>(.*?)</title>", out).group(1))
        pdf = os.path.join(OUT, f"Confirmed_dense_{fname}.pdf")
        subprocess.run([CHROME, "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", "file://" + srcf], check=True, capture_output=True)
        print(fname, num, "questions,", len(pages), "pages ->", pdf)


main()
