# -*- coding: utf-8 -*-
"""Tree-style concept maps: topic at the top, a trunk down the middle, branches left/right with their details.
Same text format as build_cards.py.  usage: build_tree.py MAPS_DIR OUT.pdf [PNG_DIR]"""
import glob
import html
import os
import re
import subprocess
import sys
import tempfile

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import annot

MAPS, OUT = sys.argv[1], sys.argv[2]
PNG_DIR = sys.argv[3] if len(sys.argv) > 3 else tempfile.mkdtemp()
os.makedirs(PNG_DIR, exist_ok=True)
CHROME = sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))[-1]
FONT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets"))
W = 900
COLORS = ["#4f9cf9", "#f2b800", "#43c59e", "#f07167", "#b388ff", "#56cfe1", "#ff9f1c", "#9ccc65"]

CSS = f"""
@font-face {{ font-family: 'Taj'; font-weight: 400; src: url(file://{FONT}/tajawal_1.ttf); }}
@font-face {{ font-family: 'Taj'; font-weight: 700; src: url(file://{FONT}/tajawal_2.ttf); }}
* {{ box-sizing: border-box; }}
html, body {{ background: #0e0e10; }}
body {{ width: {W}px; margin: 0; padding: 18px 16px 22px; color: #ececec; font-family: 'Taj', 'DejaVu Sans', sans-serif;
       font-size: 16px; line-height: 1.55; direction: rtl; }}
.root {{ margin: 0 auto 0; width: 70%; text-align: center; background: #1f2a44; border: 2px solid #4f9cf9; border-radius: 18px;
        padding: 12px 16px; font-size: 24px; font-weight: 700; color: #fff; position: relative; }}
.intro {{ width: 80%; margin: 10px auto 0; text-align: center; color: #c9c9cf; font-size: 15.5px; }}
.tree {{ position: relative; display: grid; grid-template-columns: 1fr 1fr; column-gap: 46px; margin-top: 14px; padding-top: 10px; }}
.tree:before {{ content: ""; position: absolute; top: -14px; bottom: 30px; left: 50%; border-left: 3px solid #555; transform: translateX(-1.5px); }}
.br {{ position: relative; margin: 12px 0; }}
.br:nth-child(odd) {{ grid-column: 1; }}
.br:nth-child(even) {{ grid-column: 2; }}
.br .bh {{ position: relative; border-radius: 14px; padding: 8px 12px; font-weight: 700; font-size: 18px; color: #111; text-align: center; }}
.br:nth-child(odd) .bh:after {{ content: ""; position: absolute; top: 50%; left: -26px; width: 26px; border-top: 3px solid #555; }}
.br:nth-child(even) .bh:after {{ content: ""; position: absolute; top: 50%; right: -26px; width: 26px; border-top: 3px solid #555; }}
.kids {{ margin: 6px 14px 0 0; padding-right: 14px; border-right: 2px solid #3a3a3f; }}
.k {{ position: relative; background: #17171a; border: 1px solid #34343a; border-radius: 12px; padding: 7px 10px; margin: 8px 0; font-size: 15px; }}
.k:before {{ content: ""; position: absolute; top: 16px; right: -16px; width: 14px; border-top: 2px solid #3a3a3f; }}
.k b {{ color: #fff; }}
.k .s {{ display: block; color: #b9b9c0; font-size: 14px; }}
.k.note {{ background: #221d0e; border-color: #e0a100; }}
.arrow {{ text-align: center; color: #888; font-size: 15px; line-height: 1; margin: -4px 0; }}
.sum {{ grid-column: 1 / 3; margin-top: 14px; border: 1px solid #2f6f55; background: #10231b; padding: 10px 14px; border-radius: 14px; font-weight: 700; font-size: 17px; text-align: center; position: relative; z-index: 1; }}
.st {{ color: #f2b800; }}
.ex {{ color: #9a9aa2; }}
.ref {{ color: #8fb8ff; font-size: .85em; font-weight: 400; }}
"""

LAT = re.compile(r"[A-Za-z][A-Za-z0-9'’\-/.+%±↑↓]*(?: (?:[A-Za-z0-9±][A-Za-z0-9'’\-/.+%±]*|\+|/))*")


def e(t):
    t = t.strip()
    out, last = [], 0
    for m in LAT.finditer(t):
        out.append(html.escape(t[last:m.start()], quote=False))
        out.append(f'<bdi dir="ltr">{annot.annotate_text(html.escape(m.group(0), quote=False), labs=False)}</bdi>')
        last = m.end()
    out.append(html.escape(t[last:], quote=False))
    return "".join(out).replace("★", '<span class="st">★</span>').replace("○", '<span class="ex">○</span>')


def node(t, cls="k"):
    a, _, b = t.partition("::")
    if b.strip():
        return f'<div class="{cls}"><b>{e(a)}</b><span class="s">{e(b)}</span></div>'
    return f'<div class="{cls}">{e(a)}</div>'


def render(block):
    head, *rest = block.strip().splitlines()
    _, title = head[1:].split("|", 1)
    intro, branches, summary = "", [], ""
    cur = None
    for ln in rest:
        ln = ln.strip()
        if not ln.startswith(">"):
            continue
        kind, _, body = ln[1:].strip().partition(":")
        body = body.strip()
        if kind == "h":
            cur = [body, []]
            branches.append(cur)
        elif kind == "sum":
            summary = body
        elif cur is None and kind == "p":
            intro += " " + body
        else:
            if cur is None:
                cur = ["", []]
                branches.append(cur)
            items = [x for x in body.split(";;") if x.strip()]
            if kind == "p":
                cur[1].append(node(body))
            elif kind == "box":
                cur[1].append('<div class="arrow">↓</div>'.join(node(x) for x in items))
            elif kind in ("two", "list"):
                cur[1] += [node(x) for x in items]
            elif kind == "note":
                cur[1].append(node(body, "k note"))
    out = f'<div class="root">{e(title)}</div>'
    if intro.strip():
        out += f'<div class="intro">{e(intro)}</div>'
    out += '<div class="tree">'
    for i, (h, kids) in enumerate(branches):
        col = COLORS[i % len(COLORS)]
        out += f'<div class="br"><div class="bh" style="background:{col}">{e(h)}</div><div class="kids">{"".join(kids)}</div></div>'
    if summary:
        lines = [x for x in re.split(r"(?<=[.:])\s+", summary) if x.strip()]
        out += '<div class="sum">' + "".join(f'<div dir="rtl">{e(x.strip(" ."))}</div>' for x in lines) + '</div>'
    return out + "</div>"


def shot(doc, png):
    src = os.path.join(tempfile.mkdtemp(), "m.html")
    open(src, "w", encoding="utf-8").write(doc)
    open(src + ".m.html", "w", encoding="utf-8").write(doc.replace("</body>", "<script>document.title=document.documentElement.scrollHeight</script></body>"))
    out = subprocess.run([CHROME, "--no-sandbox", "--hide-scrollbars", "--virtual-time-budget=2000", "--dump-dom", "file://" + src + ".m.html"], capture_output=True, text=True).stdout
    h = int(re.search(r"<title>(\d+)</title>", out).group(1))
    subprocess.run([CHROME, "--no-sandbox", "--hide-scrollbars", "--force-device-scale-factor=2", f"--window-size={W},{h + 4}",
                    "--virtual-time-budget=2000", f"--screenshot={png}", "file://" + src], check=True, capture_output=True)


PRINT = """
@page { size: A4; margin: 0; }
html, body { width: 210mm; background: #0e0e10; margin: 0; padding: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { width: 210mm; padding: 0; }
.stage { position: absolute; left: 0; top: 0; visibility: hidden; }
.mp { width: %dpx; padding: 14px 12px 18px; zoom: var(--z); }
.page { width: 210mm; height: 297mm; box-sizing: border-box; padding: 5mm; display: flex; flex-direction: row-reverse; gap: 4mm; break-after: page; overflow: hidden; background: #0e0e10; }
.page:last-child { break-after: auto; }
.col { flex: 1 1 0; min-width: 0; display: flex; flex-direction: column; gap: 3mm; }
.mp + .mp { border-top: 1px dashed #333; }
""" % W

PACK = """<script>
document.fonts.ready.then(function () {
  var page = document.createElement('div'); page.className = 'page';
  var probe = document.createElement('div'); probe.className = 'col'; page.appendChild(probe);
  var probe2 = document.createElement('div'); probe2.className = 'col'; page.appendChild(probe2);
  document.body.appendChild(page);
  var cw = probe.getBoundingClientRect().width, ch = probe.getBoundingClientRect().height;
  page.remove();
  var z = cw / %d; document.documentElement.style.setProperty('--z', z);
  var maps = [...document.querySelectorAll('.stage .mp')], cur = null, col = 2, used = 0;
  var gap = parseFloat(getComputedStyle(probe).gap) || 11;
  maps.forEach(function (m) {
    var h = m.getBoundingClientRect().height;
    if (h > ch) { m.style.zoom = z * ch / h; h = ch; }
    if (!cur || used + h > ch + 0.5) {
      if (col >= 2) { var pg = document.createElement('div'); pg.className = 'page'; document.body.appendChild(pg); cur = pg; col = 0; }
      var c = document.createElement('div'); c.className = 'col'; cur.appendChild(c); cur.lastCol = c; col += 1; used = 0;
    }
    cur.lastCol.appendChild(m); used += h + gap;
  });
  document.querySelector('.stage').remove();
  document.title = 'pages:' + document.querySelectorAll('.page').length;
});
</script>""" % W


def main():
    blocks = []
    for f in sorted(glob.glob(os.path.join(MAPS, "*.txt"))):
        blocks += [b for b in re.split(r"(?m)^(?=@ )", open(f, encoding="utf-8").read()) if b.strip().startswith("@")]
    if os.environ.get("PNG"):
        for i, b in enumerate(blocks, 1):
            shot(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{render(b)}</body></html>',
                 os.path.join(PNG_DIR, f"tree_{i:03d}.png"))
    # vector PDF (sharp at any zoom), ~4 maps per A4 page in two columns
    css = CSS.replace("html, body { background: #0e0e10; }", "").replace("body {", ".mp {", 1)
    doc = (f'<html><head><meta charset="utf-8"><style>{css}{PRINT}</style></head><body><div class="stage">'
           + "".join(f'<div class="mp">{render(b)}</div>' for b in blocks) + f"</div>{PACK}</body></html>")
    src = os.path.join(tempfile.mkdtemp(), "all.html")
    open(src, "w", encoding="utf-8").write(doc)
    out = subprocess.run([CHROME, "--no-sandbox", "--virtual-time-budget=8000", "--dump-dom", "file://" + src], capture_output=True, text=True).stdout
    pages = re.search(r"<title>(.*?)</title>", out)
    packed = src.replace("all.html", "packed.html")
    open(packed, "w", encoding="utf-8").write(re.sub(r"<script>.*?</script>", "", out, flags=re.S))  # print the laid-out DOM
    subprocess.run([CHROME, "--no-sandbox", "--no-pdf-header-footer", "--virtual-time-budget=4000", f"--print-to-pdf={OUT}", "file://" + packed],
                   check=True, capture_output=True)
    print(len(blocks), "maps,", pages.group(1) if pages else "?", "->", OUT)


main()
