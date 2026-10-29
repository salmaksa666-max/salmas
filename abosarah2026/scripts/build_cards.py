# -*- coding: utf-8 -*-
"""Phone-width explanatory map cards (dark, Arabic RTL) -> PNG per map -> one PDF with page size = image size.

usage: build_cards.py MAPS_DIR OUT.pdf [PNG_DIR]
"""
import glob
import html
import os
import re
import subprocess
import sys
import tempfile

from PIL import Image

MAPS, OUT = sys.argv[1], sys.argv[2]
PNG_DIR = sys.argv[3] if len(sys.argv) > 3 else tempfile.mkdtemp()
os.makedirs(PNG_DIR, exist_ok=True)
CHROME = sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))[-1]
FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
W = 430

CSS = f"""
@font-face {{ font-family: 'Taj'; font-weight: 400; src: url(file://{os.path.abspath(FONT)}/tajawal_1.ttf); }}
@font-face {{ font-family: 'Taj'; font-weight: 700; src: url(file://{os.path.abspath(FONT)}/tajawal_2.ttf); }}
* {{ box-sizing: border-box; }}
html {{ background: #0e0e10; }}
body {{ width: {W}px; margin: 0; padding: 16px 14px 20px; background: #0e0e10; color: #ececec; font-family: 'Taj', 'DejaVu Sans', sans-serif;
       font-size: 17px; line-height: 1.65; direction: rtl; text-align: right; }}
h1 {{ font-size: 23px; line-height: 1.4; margin: 0 0 10px; }}
h2 {{ font-size: 19px; margin: 22px 0 8px; color: #fff; }}
p {{ margin: 6px 0 10px; }}
.tag {{ display: inline-block; font-size: 13px; color: #aaa; margin-bottom: 4px; }}
.box {{ border: 1px solid #3a3a3f; border-radius: 14px; padding: 10px 12px; text-align: center; margin: 0; background: #17171a; }}
.box b {{ display: block; font-size: 18px; color: #fff; }}
.box > span {{ display: block; font-size: 15.5px; color: #b9b9c0; line-height: 1.55; margin-top: 2px; }}
.arrow {{ text-align: center; color: #888; font-size: 20px; line-height: 1.2; margin: 3px 0; }}
.two {{ display: flex; gap: 8px; margin: 10px 0; align-items: stretch; }}
.two .box {{ flex: 1; background: #1d1d21; }}
.two .box b {{ font-size: 16.5px; }}
.two .box > span {{ font-size: 14.5px; }}
ul {{ margin: 6px 0 10px; padding: 0 22px 0 0; }}
li {{ margin: 4px 0; }}
.note {{ border-right: 4px solid #e0a100; background: #221d0e; padding: 8px 12px; border-radius: 10px; margin: 12px 0; }}
.sum {{ border: 1px solid #2f6f55; background: #10231b; padding: 9px 12px; border-radius: 12px; margin: 14px 0 4px; font-weight: 700; }}
.st {{ color: #f2b800; }}
.ex {{ color: #9a9aa2; }}
"""

LAT = re.compile(r"[A-Za-z][A-Za-z0-9'’\-/.+%±↑↓]*(?: (?:[A-Za-z0-9±][A-Za-z0-9'’\-/.+%±]*|\+|/))*")


def e(t):
    t = t.strip()
    out, last = [], 0
    for m in LAT.finditer(t):
        out.append(html.escape(t[last:m.start()], quote=False))
        out.append(f'<bdi dir="ltr">{html.escape(m.group(0), quote=False)}</bdi>')
        last = m.end()
    out.append(html.escape(t[last:], quote=False))
    return "".join(out).replace("★", '<span class="st">★</span>').replace("○", '<span class="ex">○</span>')


def box(t):
    a, _, b = t.partition("::")
    return f'<div class="box"><b>{e(a)}</b>' + (f"<span>{e(b)}</span>" if b.strip() else "") + "</div>"


def render(block):
    head, *rest = block.strip().splitlines()
    _, title = head[1:].split("|", 1)
    out = [f"<h1>{e(title)}</h1>"]
    for ln in rest:
        ln = ln.strip()
        if not ln.startswith(">"):
            continue
        kind, _, body = ln[1:].strip().partition(":")
        body = body.strip()
        if kind == "p":
            out.append(f"<p>{e(body)}</p>")
        elif kind == "h":
            out.append(f"<h2>{e(body)}</h2>")
        elif kind == "box":
            items = [x for x in body.split(";;") if x.strip()]
            out.append('<div class="arrow">↓</div>'.join(box(x) for x in items))
        elif kind == "two":
            items = [x for x in body.split(";;") if x.strip()]
            out.append('<div class="two">' + "".join(box(x) for x in items) + "</div>")
        elif kind == "list":
            out.append("<ul>" + "".join(f"<li>{e(x)}</li>" for x in body.split(";;") if x.strip()) + "</ul>")
        elif kind == "note":
            out.append(f'<div class="note">{e(body)}</div>')
        elif kind == "sum":
            out.append(f'<div class="sum">{e(body)}</div>')
    return "".join(out)


def shot(html_doc, png):
    src = os.path.join(tempfile.mkdtemp(), "m.html")
    open(src, "w", encoding="utf-8").write(html_doc)
    meas = html_doc.replace("</body>", "<script>document.title=document.documentElement.scrollHeight</script></body>")
    open(src + ".m.html", "w", encoding="utf-8").write(meas)
    out = subprocess.run([CHROME, "--no-sandbox", "--hide-scrollbars", "--virtual-time-budget=2000", "--dump-dom", "file://" + src + ".m.html"],
                         capture_output=True, text=True).stdout
    h = int(re.search(r"<title>(\d+)</title>", out).group(1))
    subprocess.run([CHROME, "--no-sandbox", "--hide-scrollbars", "--force-device-scale-factor=2", f"--window-size={W},{h + 4}",
                    "--virtual-time-budget=2000", f"--screenshot={png}", "file://" + src], check=True, capture_output=True)


def main():
    blocks = []
    for f in sorted(glob.glob(os.path.join(MAPS, "*.txt"))):
        blocks += [b for b in re.split(r"(?m)^(?=@ )", open(f, encoding="utf-8").read()) if b.strip().startswith("@")]
    pngs = []
    for i, b in enumerate(blocks, 1):
        png = os.path.join(PNG_DIR, f"map_{i:03d}.png")
        shot(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{render(b)}</body></html>', png)
        pngs.append(png)
    imgs = [Image.open(p).convert("RGB") for p in pngs]
    imgs[0].save(OUT, save_all=True, append_images=imgs[1:], resolution=192.0)
    print(len(imgs), "maps ->", OUT)


main()
