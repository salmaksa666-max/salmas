# -*- coding: utf-8 -*-
"""Mistake-review sheets: per topic, the similar questions (condensed) on the left with their answers underneath,
and the basic idea on the right (points / small tree / table).  Black & white, A4 landscape, packed.

usage: build_review.py SRC.txt OUT.pdf [SPECIALTY] [ONLY_SECTION]
SRC format:  "# Section"  "== Topic"  "q: text | answer"  "idea:" then lines: "## sub", "- point", "> a → b", "| a | b |"
"""
import glob
import html
import os
import re
import subprocess
import sys
import tempfile

SRC, OUT = sys.argv[1], sys.argv[2]
SPEC = sys.argv[3] if len(sys.argv) > 3 else "Medicine"
ONLY = sys.argv[4] if len(sys.argv) > 4 else None
CHROME = sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))[-1]

LAT = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’\-/.+%±↑↓:]*(?: (?:[A-Za-z0-9±][A-Za-z0-9'’\-/.+%±:]*|\+|/|=|–))*")
AR = re.compile(r"[؀-ۿ]")

CSS = """
@page { size: A4 landscape; margin: 7mm; }
* { box-sizing: border-box; }
html, body { width: 283mm; margin: 0; }
body { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 8.6pt; line-height: 1.32; color: #000; background: #fff; }
.sec { break-before: page; }
.sec:first-child { break-before: auto; }
.hdr { display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1.6pt solid #000; padding-bottom: 1mm; margin-bottom: 2mm; }
.hdr .spec { font-size: 13pt; font-weight: bold; }
.hdr .sys { font-size: 13pt; font-weight: bold; border: 1.4pt solid #000; border-radius: 4mm; padding: 0 4mm; }
.blk { display: grid; grid-template-columns: 56% 44%; border: 0.8pt solid #000; margin-bottom: 2.5mm; break-inside: avoid; }
.blk .ttl { grid-column: 1 / 3; background: #000; color: #fff; font-weight: bold; padding: .6mm 2mm; font-size: 9.2pt; }
.qs { padding: 1.5mm 2mm; border-right: 0.8pt solid #000; }
.qs ol { margin: 0; padding-left: 5mm; }
.qs li { margin-bottom: .7mm; }
.ans { margin-top: 1.5mm; border-top: 1pt solid #000; padding-top: 1mm; font-size: .95em; }
.ans b.h { display: block; font-size: .85em; letter-spacing: .5px; }
.ans span { display: inline-block; margin-right: 3.5mm; }
.idea { padding: 1.5mm 2mm; direction: rtl; text-align: right; }
.idea .h { font-weight: bold; text-decoration: underline; margin: 1mm 0 .5mm; }
.idea .lbl { font-size: .85em; font-weight: bold; letter-spacing: .5px; direction: ltr; text-align: right; }
.idea ul { margin: 0; padding-right: 4mm; padding-left: 0; }
.idea li { margin-bottom: .4mm; }
.idea table { border-collapse: collapse; width: 100%; margin: .6mm 0 1mm; font-size: .95em; }
.idea td { border: 0.5pt solid #000; padding: .4mm 1.2mm; vertical-align: top; }
.idea tr:first-child td { font-weight: bold; background: #e6e6e6; }
.tree { display: flex; flex-wrap: wrap; align-items: center; gap: 1mm; margin: .6mm 0; }
.tree .n { border: 0.7pt solid #000; border-radius: 1.5mm; padding: .2mm 1.5mm; }
.tree .a { font-weight: bold; }
b { font-weight: bold; }
.warn { font-size: .9em; }
"""


def bidi(t):
    """escape and keep Latin runs left-to-right inside Arabic text"""
    t = html.escape(t, quote=False)
    if not AR.search(t):
        return t
    return LAT.sub(lambda m: f'<bdi dir="ltr">{m.group(0)}</bdi>', t)


def bold(t):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(t, quote=False))


def idea_html(lines):
    out, table = [], []

    def flush():
        if table:
            out.append("<table>" + "".join("<tr>" + "".join(f"<td>{bidi(c.strip())}</td>" for c in r) + "</tr>" for r in table) + "</table>")
            table.clear()
    for ln in lines:
        s = ln.strip()
        if s.startswith("|"):
            table.append(s.strip("|").split("|"))
            continue
        flush()
        if s.startswith("## "):
            out.append(f'<div class="h">{bidi(s[3:])}</div>')
        elif s.startswith("> "):
            parts = [p.strip() for p in s[2:].split("→")]
            out.append('<div class="tree" dir="rtl">' + '<span class="a">←</span>'.join(f'<span class="n">{bidi(p)}</span>' for p in parts) + "</div>")
        elif s.startswith("- "):
            out.append(f"<ul><li>{bidi(s[2:])}</li></ul>")
        elif s:
            out.append(f"<div>{bidi(s)}</div>")
    flush()
    return "".join(out).replace("</ul><ul>", "")


def parse(path):
    secs, sec, blk, mode = [], None, None, None
    for ln in open(path, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if ln.startswith("# "):
            sec = dict(name=ln[2:].strip(), blocks=[])
            secs.append(sec)
        elif ln.startswith("== "):
            blk = dict(title=ln[3:].strip(), qs=[], idea=[])
            sec["blocks"].append(blk)
            mode = "q"
        elif ln.startswith("q: "):
            q, _, a = ln[3:].rpartition("|")
            blk["qs"].append((q.strip(), a.strip()))
        elif ln.strip() == "idea:":
            mode = "idea"
        elif mode == "idea" and blk is not None:
            blk["idea"].append(ln)
    return secs


def main():
    secs = parse(SRC)
    if ONLY:
        secs = [s for s in secs if s["name"].lower() == ONLY.lower()]
    body = ""
    for s in secs:
        body += f'<div class="sec"><div class="hdr"><span class="spec">{html.escape(SPEC)}</span><span class="sys">{html.escape(s["name"])}</span><span>Basic idea</span></div>'
        n = 0
        for b in s["blocks"]:
            first = n + 1
            qs = "".join(f"<li>{bold(q)}</li>" for q, _ in b["qs"])
            ans = "".join(f"<span><b>{first + i}.</b> {bold(a)}</span>" for i, (_, a) in enumerate(b["qs"]))
            n += len(b["qs"])
            body += (f'<div class="blk"><div class="ttl">{html.escape(b["title"])}</div>'
                     f'<div class="qs"><ol start="{first}">{qs}</ol><div class="ans"><b class="h">ANSWERS</b>{ans}</div></div>'
                     f'<div class="idea"><div class="lbl">BASIC IDEA</div>{idea_html(b["idea"])}</div></div>')
        body += "</div>"
    doc = f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'
    src = os.path.join(tempfile.mkdtemp(), "r.html")
    open(src, "w", encoding="utf-8").write(doc)
    subprocess.run([CHROME, "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={OUT}", "file://" + src], check=True, capture_output=True)
    print(sum(len(b["qs"]) for s in secs for b in s["blocks"]), "questions ->", OUT)


main()
