# -*- coding: utf-8 -*-
"""Topic tables that solve a whole group of similar questions: per topic a table (last column = the questions it answers),
notes, then the questions themselves with the answer ticked.  Black & white, A4, packed.
usage: build_tables.py TABLES.txt ITEMS.json DECK.apkg OUT.pdf TITLE"""
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

SRC, ITEMS, DECK, OUT, TITLE = sys.argv[1:6]
CHROME = sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))[-1]
AR = re.compile(r"[؀-ۿ]")
LAT = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’\-/.+%±:&]*(?: (?:[A-Za-z0-9±][A-Za-z0-9'’\-/.+%±:&]*|\+|/|=|–))*")
QID = re.compile(r"\b\d{4}\b")
PREFIX = os.environ.get("PREFIX", "GB-")

items = {it["qid"]: it for it in json.load(open(ITEMS, encoding="utf-8"))}
d = tempfile.mkdtemp()
zipfile.ZipFile(DECK).extract("collection.anki21", d)
c = sqlite3.connect(os.path.join(d, "collection.anki21"))
names = [f["name"] for f in list(json.loads(c.execute("select models from col").fetchone()[0]).values())[0]["flds"]]
OPTS = {}
for (flds,) in c.execute("select flds from notes"):
    f = dict(zip(names, flds.split("\x1f")))
    OPTS[f["QNo"].split("-")[-1]] = [(k, re.sub(r"^[A-Z]\.\s*", "", html.unescape(html.unescape(re.sub(r"<[^>]+>", "", t)))).strip())
                          for k, t in re.findall(r'data-letter="([A-Z])">(.*?)</div>', f.get("OriginalQuestionHTML", ""), re.S)]


def bidi(t):
    if not AR.search(t):
        return html.escape(t, quote=False)
    out, last = "", 0
    for m in LAT.finditer(t):
        out += html.escape(t[last:m.start()], quote=False) + f'<bdi dir="ltr">{html.escape(m.group(0), quote=False)}</bdi>'
        last = m.end()
    return out + html.escape(t[last:], quote=False)


# parse
secs, cur = [], None
for ln in open(SRC, encoding="utf-8").read().splitlines():
    if ln.startswith("# "):
        secs.append([ln[2:].strip(), []])
    elif ln.startswith("== "):
        cur = dict(title=ln[3:].strip(), rows=[], notes=[], tree=[])
        secs[-1][1].append(cur)
    elif ln.startswith("|"):
        cur["rows"].append([x.strip() for x in ln.strip().strip("|").split("|")])
    elif ln.startswith("- "):
        cur["notes"].append(ln[2:].strip())
    elif ln.startswith("> "):
        cur["tree"].append([x.strip() for x in ln[2:].split("→")])

num, seen = {}, set()
n = 0
for _, topics in secs:
    for tp in topics:
        tp["qs"] = []
        for q in QID.findall(" ".join(r[-1] for r in tp["rows"][1:]) + " " + " ".join(" ".join(re.findall(r"\[([0-9 ]+)\]", x)) for x in tp["notes"])):
            if q not in num:
                n += 1
                num[q] = n
                tp["qs"].append(q)


def refs(ids):
    return "، ".join(str(num[q]) for q in ids)


CSS = """
@page { size: A4; margin: 6mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 7.3pt; line-height: 1.25; color: #000; margin: 0; }
.top { display: flex; justify-content: space-between; border-bottom: 1.6pt solid #000; padding-bottom: .8mm; margin-bottom: 1.5mm; font-weight: bold; font-size: 11pt; }
.sec { font-size: 10pt; font-weight: bold; border: 1.2pt solid #000; border-radius: 3mm; padding: 0 3mm; display: inline-block; margin: 1.5mm 0 1mm; }
.tp { border: .8pt solid #000; margin-bottom: 2mm; }
.tt { background: #000; color: #fff; font-weight: bold; padding: .5mm 2mm; font-size: 8.4pt; direction: rtl; text-align: right; }
table { border-collapse: collapse; width: 100%; direction: rtl; }
td { border: .5pt solid #000; padding: .4mm 1.2mm; vertical-align: top; text-align: right; }
tr:first-child td { background: #e6e6e6; font-weight: bold; }
td.q { white-space: nowrap; font-weight: bold; direction: ltr; text-align: left; width: 1%; }
.notes { direction: rtl; text-align: right; padding: .6mm 2mm; border-top: .5pt solid #000; }
.notes div { margin: .2mm 0; }
.notes b { direction: ltr; unicode-bidi: isolate; }
.qs { column-count: 2; column-gap: 4mm; column-rule: .4pt solid #999; padding: 1mm 2mm; border-top: .8pt solid #000; }
.q { break-inside: avoid; margin-bottom: .9mm; }
.q .o { padding-left: 3mm; color: #222; }
.q .o span { margin-right: 2.5mm; }
.rp { border: .8pt solid #000; border-radius: 1mm; padding: 0 1mm; font-weight: bold; }
.tree { direction: rtl; display: flex; flex-wrap: wrap; align-items: center; gap: 1mm; padding: .8mm 2mm; font-size: 8pt; }
.tree .n { border: .8pt solid #000; border-radius: 1.5mm; padding: .3mm 1.5mm; }
.tree .a { font-weight: bold; }
.tree:first-of-type { padding-top: 1.5mm; }
.ok { font-weight: bold; text-decoration: underline; color: #000; }
"""
body = f'<div class="top"><span>{html.escape(TITLE)}</span><span>جداول الحل</span></div>'
for sname, topics in secs:
    body += f'<div class="sec">{html.escape(sname)}</div>'
    for tp in topics:
        rows = ""
        for i, r in enumerate(tp["rows"]):
            cells = r[:-1]
            last = "Q" if i == 0 else refs([q for q in QID.findall(r[-1])])
            rows += "<tr>" + "".join(f"<td>{bidi(x)}</td>" for x in cells) + f'<td class="q">{last}</td></tr>'
        notes = "".join("<div>• " + bidi(re.sub(r"\[([0-9 ]+)\]", lambda m: f"(Q {refs(QID.findall(m.group(1)))})", x)) + "</div>" for x in tp["notes"])
        qs = ""
        for q in tp["qs"]:
            it = items[PREFIX + q]
            ans = it["ans"]
            o = ""
            for k, t in OPTS.get(q, []):
                ok = re.match(rf"{k}[.)]", ans.strip())
                o += f'<span class="{"ok" if ok else ""}">{"✔ " if ok else ""}{k}. {html.escape(t)}</span> '
            if not o or not re.match(r"[A-E][.)]", ans.strip()):
                o += f' <span class="ok">✔ {html.escape(ans)}</span>'
            badge = f'<span class="rp">مكرر {html.escape(it["rep"])}</span> ' if it.get("rep") else ""
            qs += f'<div class="q"><b>{num[q]})</b> {badge}{html.escape(it["stem"])}{it["flag"]}<div class="o">{o}</div></div>'
        tree = "".join('<div class="tree">' + '<span class="a">←</span>'.join(f'<span class="n">{bidi(x)}</span>' for x in br) + "</div>" for br in tp["tree"])
        body += (f'<div class="tp"><div class="tt">{bidi(tp["title"])}</div>{tree}' + (f"<table>{rows}</table>" if rows else "")
                 + (f'<div class="notes">{notes}</div>' if notes else "") + (f'<div class="qs">{qs}</div>' if qs else "") + "</div>")
doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'
src = os.path.join(tempfile.mkdtemp(), "t.html")
open(src, "w", encoding="utf-8").write(doc)
subprocess.run([CHROME, "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={OUT}", "file://" + src], check=True, capture_output=True)
print(n, "questions ->", OUT)
