"""Questions from the MKJ 'Alhomrani 1-16 November' deck that our 1-14 November bank was missing -> site/mkj_add.json
(+ their source-page images packed into site/pgk). Usage: mkj_add.py <scratchpad>"""
import json, os, re, sys
from PIL import Image
SP = sys.argv[1]
A = [k for k in json.load(open(os.path.join(SP, "mkj_add2.json"))) if k["al"] and k["al"] in dict(k["opts"]) and len(k["opts"]) >= 2]
media = json.load(open(os.path.join(SP, "mkj16", "media"))); inv = {v: k for k, v in media.items()}
P1 = open(os.path.join(SP, "src", "P1.raw.txt"), encoding="utf-8").read().split("\f")
P2 = open(os.path.join(SP, "src", "P2.raw.txt"), encoding="utf-8").read().split("\f")
N15 = open(os.path.join(SP, "src", "N15f.raw.txt"), encoding="utf-8").read().split("\f")
SEC = {"01": "Medicine", "02": "Pediatrics", "03": "OBGYN", "04": "Surgery", "05": "Psychiatry", "06": "Other / Mixed"}
FLAG = re.compile(r"No Idea|Don.?t Know|Donno|\(Question\)|Not Sure|Athar:|Dr\.S|Wafa:|Gut", re.I)
os.makedirs("site/pgk", exist_ok=True)
for f in os.listdir("site/pgk"): os.remove(os.path.join("site/pgk", f))
need = sorted({i for k in A for i in k["imgs"]}); tiles = {}
W, PER = 900, 8
for s0 in range(0, len(need), PER):
    grp = need[s0:s0 + PER]; ims = []
    for n in grp:
        im = Image.open(os.path.join(SP, "mkj16", inv[n])).convert("RGB"); ims.append(im.resize((W, round(im.height * W / im.width))))
    H = sum(i.height for i in ims); sh = Image.new("RGB", (W, H), "white"); y = 0; name = "pgk/s%d.webp" % (s0 // PER)
    for n, im in zip(grp, ims):
        sh.paste(im, (0, y)); h = im.height
        tiles[n] = "%s|%s|%s|%s" % (name, 0 if H == h else round(100 * y / (H - h), 3), round(100 * H / h, 3), round(W / h, 4)); y += h
    sh.save(os.path.join("site", name), "WEBP", quality=55)
out = []
for k in A:
    m = re.search(r"pp\.\s*(\d+)", k["page"]); pg = int(m.group(1)) if m else 0
    src = P2 if "Part_2" in k["tags"] else P1 if k["src"].startswith("10-14") else N15 if k["src"].startswith("1-5") else None
    ptxt = src[pg - 1] if src and 0 < pg <= len(src) else ""
    warn = k["state"] != "sourced" or bool(FLAG.search(ptxt.split("\n", 3)[-1][-700:]))
    ex = re.sub(r"\.[a-z-]+\{[^}]*\}", "", k["expl"]); ex = re.sub(r"\s+", " ", ex).strip()
    note = ("⚠ الحمراني مو متأكد منه أو الجواب من غيره (شوفي صفحته). " if warn else "") + "مضاف من دكة MKJ (الحمراني 1-16) · " + k["page"]
    out.append(dict(i="MK-" + k["qno"], q=re.sub(r"\s+", " ", k["stem"]), o=[[l, t] for l, t in k["opts"]], a=k["al"], b="Alhomrani Nov",
                    s=SEC[k["sec"][:2]], t="كل أسئلة النظام", h="", k="", r=ex[:700], n=note, f="", im=[], kw=[], sp=[tiles[i] for i in k["imgs"] if i in tiles]))
json.dump(out, open("site/mkj_add.json", "w", encoding="utf-8"), ensure_ascii=False)
from collections import Counter
print(len(out), Counter(q["s"] for q in out), "warn", sum("⚠" in q["n"] for q in out), "sheets", len(os.listdir("site/pgk")))
