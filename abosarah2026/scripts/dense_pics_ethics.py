"""Dense 3-column PDFs (like the OBGYN files) for the Pictures and Ethics banks + Salma's remaining plan."""
import json, html, os, re, subprocess, sys
D = json.load(open("site/data.json", encoding="utf-8"))
OUT = "build/final"; SP = sys.argv[1]
E = html.escape
CSS = """@page{size:A4;margin:7mm}body{font-family:'Noto Sans',Arial,sans-serif;font-size:%(fs)spt;line-height:1.25;color:#111}
.cols{column-count:%(cols)s;column-gap:4mm;column-rule:0.3pt solid #bbb}h1{font-size:12pt;margin:0 0 2mm}
h2{column-span:all;font-size:9.5pt;background:#1f3b63;color:#fff;padding:1mm 2mm;margin:2mm 0 1mm;border-radius:1mm}
.q{break-inside:avoid;margin:0 0 1.2mm;padding:0 0 1mm;border-bottom:0.3pt dotted #999}.n{font-weight:700;color:#1f3b63}
.o{display:inline;margin-right:1.5mm;color:#444}.ok{color:#0a7a2a;font-weight:700;background:#e3f6e8;padding:0 .6mm;border-radius:.6mm}
.x{color:#7a4b00;font-size:.92em;display:block;margin-top:.4mm}.x b{color:#7a4b00}
img{max-width:100%%;max-height:42mm;display:block;margin:.6mm auto;border:0.3pt solid #ccc}"""
def strip(s, n=230):
    s = re.sub(r"<[^>]+>", " ", s or ""); s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + "…"
JUNK = re.compile(r"bold|source|marked|recaller|stem|option[s]? (kept|removed)|printed|cleaned|chatter|auto-detect|on the page|appeared|repeats:|stray|collapsed|mistake \\d", re.I)
def clean(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return " ".join(x for x in re.split(r"(?<=[.;])\s+", s) if x.strip() and not JUNK.search(x))
def item(i, q, imgs):
    o = " ".join(f'<span class="o{" ok" if L == q["a"] else ""}">{L}. {E(t)}{" ✔" if L == q["a"] else ""}</span>' for L, t in q["o"])
    ex = strip(clean(q.get("k")), 160); r = strip(clean(q.get("r")), 230)
    note = " · ".join(x for x in (ex, r) if x)
    im = "".join(f'<img src="file://{os.path.join(os.environ.get("PIMG", os.path.abspath("site/pimg")), p)}">' for p in (q.get("pi") or [])) + "".join(f'<img src="file://{os.path.join(os.environ.get("IMG", os.path.abspath("site/img")), p)}">' for p in (q.get("im") or [])) if imgs else ""
    return f'<div class="q"><span class="n">{i}.</span> {E(q["q"])}{im}<br>{o}' + (f'<span class="x"><b>💡</b> {E(note)}</span>' if note else "") + "</div>"
def build(bank, title, fname, order, imgs, fs, cols, pre=None):
    qs = [q for q in D if q["b"] == bank and (pre is None or q["i"].startswith(pre))]
    secs = sorted({q["s"] for q in qs}, key=lambda s: (order.index(s) if s in order else 99, s))
    body, n = [], 0
    for s in secs:
        body.append(f"<h2>{E(s)} ({sum(q['s']==s for q in qs)})</h2>")
        for q in [q for q in qs if q["s"] == s]:
            n += 1; body.append(item(n, q, imgs))
    h = f'<html><head><meta charset="utf-8"><style>{CSS % dict(fs=fs, cols=cols)}</style></head><body><h1>{E(title)} — {n} Q</h1><div class="cols">{"".join(body)}</div></body></html>'
    p = os.path.join(SP, fname + ".html"); open(p, "w").write(h)
    subprocess.run(["node", os.path.join(SP, "pdf.js"), p, os.path.join(OUT, fname + ".pdf")], check=True, env=dict(os.environ, NODE_PATH=subprocess.check_output(["npm", "root", "-g"], text=True).strip()))
WHICH = sys.argv[2:] or ["pics", "ethics"]
if "pics" in WHICH: build("Pictures", "Pictures — Joe + Almakrami", "الصور_Joe_المكرمي_محشور", ["Medicine", "Surgery", "Pediatrics", "OBGYN", "Dermatology & STI", "Ophthalmology"], True, 6.6, 3)
if "ethics" in WHICH: build("Ethics", "Ethics — Athar + SMLE Brain", "Ethics_محشور", ["Medical Ethics", "Patient Safety", "Public Health", "Clinical Research", "Biostatistics"], False, 6.3, 3)
if "alh" in WHICH: build("Alhomrani Nov", "Alhomrani November (1-14)", "الحمراني_نوفمبر_محشور", ["OBGYN", "Pediatrics", "Medicine", "Surgery", "Psychiatry", "Other / Mixed"], True, 6.2, 3)
if "yasir" in WHICH: build("Yasir Nov", "Yasir November", "ياسر_نوفمبر_محشور", ["OB/GYN", "Pediatrics", "Medicine", "Surgery", "Psychiatry, ENT, eye & skin", "Ethics & public health"], False, 6.2, 3)
if "joe" in WHICH: build("Pictures", "Pictures — Joe", "الصور_Joe_محشور", ["Medicine", "Surgery", "Pediatrics", "OBGYN", "Dermatology & STI", "Ophthalmology"], True, 6.6, 3, "JOE")
if "amk" in WHICH: build("Pictures", "Pictures — Almakrami", "الصور_المكرمي_محشور", ["Medicine", "Surgery", "Pediatrics", "OBGYN", "Dermatology & STI", "Ophthalmology"], True, 6.6, 3, "AMK")
if "silent" in WHICH: build("Silent", "Silent — Sunday 15 + Monday 16 Nov", "سايلنت_15_16_نوفمبر_محشور", [], True, 6.3, 3)
