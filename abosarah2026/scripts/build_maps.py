# -*- coding: utf-8 -*-
"""Concept maps (flow boxes + exam tricks) -> PDF.  usage: build_maps.py MAPS_DIR OUT.pdf [N_PER_PAGE]"""
import glob
import html
import os
import re
import subprocess
import sys
import tempfile

MAPS, OUT = sys.argv[1], sys.argv[2]
PER = int(sys.argv[3]) if len(sys.argv) > 3 else 2
CHROME = sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))[-1]

CSS = """
@page { size: A4; margin: 9mm; }
* { box-sizing: border-box; }
html, body { width: 192mm; }
body { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 9pt; line-height: 1.35; color: #000; margin: 0; }
.page { height: 279mm; display: grid; grid-template-rows: repeat(PER, minmax(0,1fr)); gap: 3mm; break-after: page; overflow: hidden; }
.map { border: 1.2pt solid #000; border-radius: 3mm; padding: 2.5mm 3.5mm; overflow: hidden; }
.map h2 { font-size: 11pt; margin: 0 0 1.5mm; padding-bottom: 1mm; border-bottom: 0.8pt solid #000; }
.idea { margin: 0 0 2mm; font-weight: bold; }
.cols { display: flex; gap: 3mm; align-items: flex-start; }
.flow { flex: 1; }
.ft { font-weight: bold; font-size: .95em; margin-bottom: 1mm; text-decoration: underline; }
.box { border: 0.8pt solid #000; border-radius: 2mm; padding: 1mm 2mm; text-align: center; background: #f0f0f0; }
.box b { display: block; font-size: 1.02em; }
.vs .box, .tr li, .idea, .ft, .lab { text-align: right; }
.box small { display: block; font-size: .88em; }
.arrow { text-align: center; line-height: 1; font-size: 11pt; margin: .3mm 0; }
.vs { display: flex; gap: 2mm; margin: 2mm 0; }
.vs .box { flex: 1; text-align: left; background: #fff; border-width: 1.1pt; }
.vs .box b { border-bottom: 0.5pt solid #000; margin-bottom: .6mm; }
.tr { margin: 0; padding-left: 4mm; }
.tr li { margin-bottom: .8mm; }
.lab { font-weight: bold; margin-top: 1.5mm; }
"""

FIT = """<script>
document.querySelectorAll('.map').forEach(function(m){
  var fs = START; m.style.fontSize = fs + 'pt';
  while (fs > 5.2 && m.scrollHeight > m.clientHeight + 1) { fs -= 0.2; m.style.fontSize = fs + 'pt'; }
});
</script>"""


LAT = re.compile(r"[A-Za-z][A-Za-z0-9'’\-/.+%()±↑↓→←]*(?: (?:[A-Za-z0-9±][A-Za-z0-9'’\-/.+%()±]*|→|←|\+|/))*")


def e(t):
    t = html.escape(t.strip(), quote=False)
    return LAT.sub(lambda m: f'<bdi dir="ltr">{m.group(0)}</bdi>', t)


def box(t):
    t = t.strip().replace("● ", "● ", 1)
    if "::" in t:
        a, b = t.split("::", 1)
        return f'<div class="box"><b dir="rtl">{e(a)}</b><small dir="rtl">{e(b)}</small></div>'
    return f'<div class="box"><b dir="rtl">{e(t)}</b></div>'


def render(block):
    head, *rest = block.strip().splitlines()
    ids, title = head[1:].split("|", 1)
    idea, flows, vs, tricks = "", [], [], []
    for ln in rest:
        ln = ln.strip()
        if not ln.startswith(">"):
            continue
        ln = ln[1:].strip()
        if ln.startswith("idea:"):
            idea = ln[5:]
        elif ln.startswith("flow"):
            t, body = ln[4:].split(":", 1) if ":" in ln[4:] else ("", ln[4:])
            flows.append((t.strip(), [x for x in body.split(";;") if x.strip()]))
        elif ln.startswith("vs"):
            vs.append([x for x in ln[2:].split(";;") if x.strip()])
        elif ln.startswith("trick:"):
            tricks.append(ln[6:])
    out = f'<div class="map"><h2 dir="ltr">{html.escape(title.strip())}</h2>'
    if idea:
        out += f'<div class="idea" dir="rtl">{e(idea)}</div>'
    out += '<div class="cols">'
    for t, items in flows:
        out += f'<div class="flow"><div class="ft" dir="rtl">{e(t)}</div>' + '<div class="arrow">↓</div>'.join(box(x) for x in items) + "</div>"
    out += "</div>"
    for pair in vs:
        out += '<div class="vs">' + "".join(box(x) for x in pair) + "</div>"
    if tricks:
        out += '<div class="lab">⚠ فخاخ الاختبار</div><ul class="tr">' + "".join(f'<li dir="rtl">{e(t)}</li>' for t in tricks) + "</ul>"
    return out + "</div>"


def main():
    blocks = []
    for f in sorted(glob.glob(os.path.join(MAPS, "*.txt"))):
        blocks += [b for b in re.split(r"(?m)^(?=@ )", open(f, encoding="utf-8").read()) if b.strip().startswith("@")]
    maps = [render(b) for b in blocks]
    pages = ['<div class="page">' + "".join(maps[i:i + PER]) + "</div>" for i in range(0, len(maps), PER)]
    css = CSS.replace("repeat(PER,", f"repeat({PER},")
    doc = f'<html><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(pages)}{FIT.replace("START", "12.5" if PER == 1 else "9.4")}</body></html>'
    src = os.path.join(tempfile.mkdtemp(), "x.html")
    open(src, "w", encoding="utf-8").write(doc)
    subprocess.run([CHROME, "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={OUT}", "file://" + src], check=True, capture_output=True)
    print(len(maps), "maps,", len(pages), "pages ->", OUT)


main()
