"""Alhomrani '16 November' file -> site/alh16.json (Silent bank section + Alhomrani Nov copies spread by specialty)
and packed page sheets in site/pg16/. Usage: alh16_build.py <scratchpad n16 dir> <pdf>"""
import json, os, re, subprocess, sys
from PIL import Image
sys.path.insert(0, "data")
from alh16_spec import NEW, REP, OVR
SP, PDF = sys.argv[1], sys.argv[2]
SEC = {"M": "Medicine", "S": "Surgery", "O": "OBGYN", "P": "Pediatrics", "Y": "Psychiatry", "X": "Other / Mixed"}
plain = open(os.path.join(SP, "plain.txt"), encoding="utf-8").read().split("\f")
JUNK = re.compile(r"https?://|t\.me/|salla\.sa|^\s*\d{1,3}\.\s*$|Seen in (September|October|November|Aug)|Key source|Other answer|Lookalike|SMLE First Aid|SMLE-Alliance|^\s*16 November|see next slide|Examiner|Athar|Alhomrani:|Wafa:|^Answer|^Ans:|athar1881", re.I)
OPT = re.compile(r"^\s*[\(\[]?([A-Ea-e])\s*[\)\]\.\-–:]\s*(.+)$")

def text(p):
    t = plain[p - 1] if p - 1 < len(plain) else ""
    body = re.sub(r"https://t\.me/\S+.*", "", t).strip()
    if len(body) <= 40: t = open(os.path.join(SP, "ocr", "p-%03d.txt" % p), encoding="utf-8").read()
    return t

def parse(p):
    lines = [l.strip() for l in text(p).split("\n") if l.strip()]
    stem, opts, after, started = [], [], [], False
    for l in lines:
        m = OPT.match(l)
        if m and not (started and len(opts) >= 2 and m.group(1).upper() <= opts[-1][0]):
            started = True; opts.append([m.group(1).upper(), m.group(2).strip()]); continue
        if not started:
            if JUNK.search(l): continue
            stem.append(l)
        else: after.append(l)
    s = " ".join(stem)
    s = re.sub(r"^\d{1,4}\.\s*", "", s); s = re.sub(r"^\d{3,4}\.\s*", "", s)
    s = re.sub(r"[\[\(\{][qQ]?\d{4,6}[^\]\)\}]*[\]\)\}]", "", s).strip()
    # cut the options at the answer line (repeat of an option)
    seen, clean = set(), []
    for k, o in opts:
        if k in seen: break
        seen.add(k); clean.append([k, re.sub(r"\s*\[Complete\].*$", "", o).strip()])
    return s, clean, after

out, pages_used, bad = [], set(), []
order = 0
for grp, rows in (("1) الأسئلة الجديدة", NEW), ("2) الأسئلة المكررة", REP)):
    for (p, a, sec, nums, extra, note) in rows:
        if p in OVR:
            s, o = OVR[p]; o = [[chr(65 + i), x] for i, x in enumerate(o)]; after = []
        else:
            s, o, after = parse(p)
        if a not in dict(o) or len(o) < 2 or len(s) < 15: bad.append((p, a, s[:80], o))
        nid = (nums.split(",")[0].strip() if nums else "p%d" % p)
        expl = " ".join(l for l in after if not JUNK.search(l) and not OPT.match(l))[:600]
        pg = [p] + [x for x in extra if x != p]
        pages_used.update(pg)
        lab = ("سؤال #" + nums.replace(", ", " و#") + " · " if nums else "") + "ملف الحمراني 16 نوفمبر (صفحة %d)" % p
        if "," in nums: lab += " · تكرر في الاختبار %d مرات" % len(nums.split(","))
        order += 1
        out.append(dict(i="AH16-" + nid, q=s, o=o, a=a, b="Silent", s="ملف الحمراني 16 نوفمبر", t=grp, h="", k=note.split("⚠")[0].strip() if note and not note.startswith("⚠") else "",
                        r=("شرح الحمراني: " + expl) if expl else "", n=((note + " ") if note.startswith("⚠") else "") + lab, f="", im=[], kw=[], _pg=pg, _sec=SEC[sec], _ord=order))
ids = [q["i"] for q in out]
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]
# pack used pages into sheets
os.makedirs("site/pg16", exist_ok=True)
for f in os.listdir("site/pg16"): os.remove(os.path.join("site/pg16", f))
used = sorted(pages_used); tiles = {}
W, PER = 900, 8
for s0 in range(0, len(used), PER):
    grp = used[s0:s0 + PER]; ims = []
    for p in grp:
        im = Image.open(os.path.join(SP, "png", "p-%03d.png" % p)).convert("RGB")
        ims.append(im.resize((W, round(im.height * W / im.width))))
    H = sum(i.height for i in ims); sheet = Image.new("RGB", (W, H), "white"); y = 0
    name = "pg16/s%d.webp" % (s0 // PER)
    for p, im in zip(grp, ims):
        sheet.paste(im, (0, y)); h = im.height
        tiles[p] = "%s|%s|%s|%s" % (name, 0 if H == h else round(100 * y / (H - h), 3), round(100 * H / h, 3), round(W / h, 4)); y += h
    sheet.save(os.path.join("site", name), "WEBP", quality=55)
for q in out: q["sp"] = [tiles[p] for p in q.pop("_pg")]
json.dump(out, open("site/alh16.json", "w", encoding="utf-8"), ensure_ascii=False)
print("questions", len(out), "pages", len(used), "sheets", len(os.listdir("site/pg16")))
for b in bad: print("CHECK", b)
