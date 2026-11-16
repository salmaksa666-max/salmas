"""Render the source page of every mapped question and pack pictures into sheets (artifact file limit).
Produces site/pg/*.webp and data/src_tiles.json: qid -> ["sheet|pos%|size%|aspect"], plus packs site/simg into site/sg."""
import json, os, re, subprocess, sys, tempfile, glob
from PIL import Image
SD = sys.argv[1]
src = {k: v for k, v in json.load(open(os.path.join(SD, "src_map.json"))).items() if v[2] >= 0.6}
os.makedirs("site/pg", exist_ok=True)
for f in glob.glob("site/pg/*.webp"): os.remove(f)
tmp = tempfile.mkdtemp()
need = sorted({(v[0], v[1]) for v in src.values()})
imgs = {}
for pdf, pg in need:
    out = os.path.join(tmp, f"{pdf}_{pg}")
    w = 1000 if pdf in ("P1", "P2", "UP", "N68", "N9", "N15f") else 820
    subprocess.run(["pdftoppm", "-f", str(pg), "-l", str(pg), "-scale-to-x", str(w), "-scale-to-y", "-1", "-png", "-singlefile", os.path.join(SD, pdf + ".pdf"), out], check=True)
    imgs[(pdf, pg)] = Image.open(out + ".png").convert("RGB")
def pack(items, prefix, per=8, width=1000, q=50):
    """items: list of (key, PIL image) -> {key: 'file|pos|size|aspect'}"""
    res, k = {}, 0
    for s in range(0, len(items), per):
        grp = [(key, im.resize((width, max(1, round(im.height * width / im.width))))) for key, im in items[s:s + per]]
        H = sum(im.height for _, im in grp); sheet = Image.new("RGB", (width, H), "white"); y = 0
        name = f"{prefix}{k}.webp"
        for key, im in grp:
            sheet.paste(im, (0, y)); h = im.height
            pos = 0 if H == h else round(100 * y / (H - h), 3)
            res[key] = f"{name}|{pos}|{round(100 * H / h, 3)}|{round(width / h, 4)}"; y += h
        sheet.save(os.path.join("site", name), "WEBP", quality=q); k += 1
    return res
# pages grouped by pdf so sheets have similar widths
order = sorted(imgs.items(), key=lambda kv: (kv[0][0], kv[0][1]))
tiles = pack([(f"{p}_{g}", im) for (p, g), im in order], "pg/s", per=8, width=900)
qt = {qid: [tiles[f"{v[0]}_{v[1]}"]] for qid, v in src.items()}
json.dump(qt, open("data/src_tiles.json", "w"))
# channel screenshots
os.makedirs("site/sg", exist_ok=True)
sh = sorted(glob.glob("site/simg/*.webp"))
if not sh: print("pages", len(imgs), "page sheets", len(glob.glob("site/pg/*.webp"))); sys.exit(0)
st = pack([(os.path.basename(f), Image.open(f).convert("RGB")) for f in sh], "sg/s", per=6, width=800, q=55)
json.dump(st, open("data/simg_tiles.json", "w"))
print("pages", len(imgs), "page sheets", len(glob.glob("site/pg/*.webp")), "shot sheets", len(glob.glob("site/sg/*.webp")))
