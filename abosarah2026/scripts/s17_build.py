"""Silent + Ninja 17 Nov -> site/s17.json + packed page sheets site/pg17/.
Usage: s17_build.py <scratchpad dir>  (needs src/SO.pdf, src/SO.txt, so17/*.png, soout/, s17/img, t17/nimg)"""
import json, os, re, subprocess, sys, glob
from PIL import Image, ImageDraw
sys.path.insert(0, "data")
from s17_spec import R, S, EXTRA, G3
SP = sys.argv[1]
SO = open(os.path.join(SP, "src/SO.txt"), encoding="utf-8").read()
pages = SO.split("\f")

def so_q(n):
    m = re.search(r"(?m)^ %d\. (.*?)(?=^ \d{1,4}\. |\Z)" % n, SO, re.S)
    body = m.group(1)
    body = re.sub(r"(?m)^SMLE First Aid.*$|^ [A-Z][A-Z/ -]+ {5,}.*$", "", body)
    lines = [l.strip() for l in body.split("\n") if l.strip()]
    stem, opts, ans = [], [], None
    for l in lines:
        mo = re.match(r"^([A-E])\) (.*)", l)
        if l.startswith("Answer:"):
            ans = re.match(r"Answer: ([A-E])\)", l).group(1); break
        if mo: opts.append([mo.group(1), mo.group(2)])
        elif opts: opts[-1][1] += " " + l
        else: stem.append(l)
    s = " ".join(stem); s = re.sub(r"\s*\[q\d+ ·[^\]]*\]", "", s).strip()
    return s, opts, ans

def crop(n, name):
    out = os.path.join(SP, "so17", name + ".png")
    if os.path.exists(out): return out
    p = next(i + 1 for i, t in enumerate(pages) if re.search(r"(?m)^\s*%d\.\s" % n, t))
    pdf = os.path.join(SP, "src/SO.pdf")
    x = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-bbox", pdf, "-"], capture_output=True, text=True).stdout
    pw, ph = map(float, re.search(r'<page width="([\d.]+)" height="([\d.]+)"', x).groups())
    words = [(float(a), float(b), w) for a, b, c, d, w in re.findall(r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)<', x)]
    y0 = min(w[1] for w in words if w[2] == "%d." % n and w[0] < pw * 0.3)
    starts = sorted(w[1] for w in words if re.fullmatch(r"\d{2,4}\.", w[2]) and w[0] < pw * 0.3)
    nxt = [s for s in starts if s > y0 + 5]; y1 = nxt[0] if nxt else ph - 30
    tmp = os.path.join(SP, "tmp17")
    subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", "110", "-png", "-singlefile", pdf, tmp], check=True)
    im = Image.open(tmp + ".png").convert("RGB"); sy = im.height / ph
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    d.rectangle([10, y0 * sy - 6, im.width - 10, y1 * sy - 4], fill=(255, 230, 0, 70), outline=(230, 160, 0, 255), width=4)
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    im = im.crop((0, max(0, int(y0 * sy) - 60), im.width, min(im.height, int(y1 * sy) + 30)))
    g = im.convert("L").point(lambda v: 255 if v < 150 else 0); bb = g.crop((0, 0, im.width, im.height - 40)).getbbox()
    if bb: im = im.crop((0, 0, im.width, bb[3] + 25))
    im.save(out); return out

def path(c):
    if c.startswith("@"):
        g = glob.glob(os.path.join(SP, c[1:] + "*")); return [x for x in g if x.endswith((".png", ".jpg"))][0]
    return glob.glob(os.path.join(SP, "so17", c + "_p*.png"))[0]

out = []
def add(grp, nid, stem, opts, a, ok, k, imgs, lab):
    o = [[chr(65 + i), t] for i, t in enumerate(opts)] if opts and isinstance(opts[0], str) else opts
    assert a in dict(o), (nid, a)
    out.append(dict(i="S17-" + nid, q=stem, o=o, a=a, b="Silent", s="سايلنت + نينجا 17 نوفمبر", t=grp, h="", k=k if not k.startswith("⚠") else "",
                    r="", n=((k + " ") if k.startswith("⚠") else "") + lab + (" · ✅ موجود في ملف التجميعات" if ok else ""), f="", im=[], kw=[], _img=imgs))
for grp, nid, stem, opts, a, ok, k, cr in R:
    add(grp, nid, stem, opts, a, ok, k, [path(c) for c in cr], "سايلنت/نينجا 17 نوفمبر")
for n in S:
    s, o, a = so_q(n)
    add(G3, "SO%d" % n, s, o, a, 1, "", [crop(n, "SO%d" % n)], "صورة نزلت اليوم · سؤال #%d من ملف التجميعات" % n)
for grp, nid, stem, opts, a, ok, k, cr in EXTRA:
    add(grp, nid, stem, opts, a, ok, k, [path(c) for c in cr], "صورة نزلت اليوم")
# pack images into sheets
os.makedirs("site/pg17", exist_ok=True)
for f in os.listdir("site/pg17"): os.remove(os.path.join("site/pg17", f))
used = []
for q in out:
    for p in q["_img"]:
        if p not in used: used.append(p)
tiles, W, PER = {}, 900, 8
for s0 in range(0, len(used), PER):
    grp = used[s0:s0 + PER]; ims = []
    for p in grp:
        im = Image.open(p).convert("RGB"); ims.append(im.resize((W, round(im.height * W / im.width))))
    H = sum(i.height for i in ims); sheet = Image.new("RGB", (W, H), "white"); y = 0
    name = "pg17/s%d.webp" % (s0 // PER)
    for p, im in zip(grp, ims):
        sheet.paste(im, (0, y)); h = im.height
        tiles[p] = "%s|%s|%s|%s" % (name, 0 if H == h else round(100 * y / (H - h), 3), round(100 * H / h, 3), round(W / h, 4)); y += h
    sheet.save(os.path.join("site", name), "WEBP", quality=60)
for q in out: q["sp"] = [tiles[p] for p in q.pop("_img")]
ids = [q["i"] for q in out]; assert len(ids) == len(set(ids))
json.dump(out, open("site/s17.json", "w", encoding="utf-8"), ensure_ascii=False)
print("questions", len(out), "images", len(used), "sheets", len(os.listdir("site/pg17")))
for q in out[-26:-20]: print(q["i"], q["a"], q["q"][:70], [x[1][:25] for x in q["o"]])
