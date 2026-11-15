"""Alhomrani 10-14 November (Part 1 + 2) -> site bank. usage: nov1014.py p1.txt p2.txt out.json"""
import re, json, sys
import numpy as np
from collections import Counter
HDR = re.compile(r"^\s*(https?://t\.me/\S+.*|10[–-]14 November.*)$")
AR = re.compile(r"[؀-ۿ]")
norm = lambda t: re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()
raw = []
for part, fn in (("P1", sys.argv[1]), ("P2", sys.argv[2])):
    for pi, pg in enumerate(open(fn, encoding="utf-8").read().split("\f"), 1):
        lines = [l.rstrip() for l in pg.splitlines() if not HDR.match(l)]
        blocks, cur = [], []
        for l in lines:
            if l.strip(): cur.append(l.strip())
            elif cur: blocks.append(cur); cur = []
        if cur: blocks.append(cur)
        if not blocks or not re.match(r"^\d+\.\s", blocks[0][0]): continue
        k = next((i for i, b in enumerate(blocks[:4]) if b[-1].rstrip().endswith("?")), None)
        if k is None or k + 1 >= len(blocks): continue
        stem = re.sub(r"^\d+\.\s*", "", " ".join(" ".join(b) for b in blocks[:k + 1]))
        opts = []
        for l in blocks[k + 1]:
            if re.match(r"^(Q|A)\s*:", l) or AR.search(l) and not re.search(r"[A-Za-z]{3}", l): break
            opts.append(re.sub(r"^[A-F][.)]\s*", "", l))
        if len(opts) < 2 or len(opts) > 7: continue
        ans = None
        for b in blocks[k + 2:k + 6]:
            nb = norm(re.sub(r"^[A-F][.)]\s*", "", " ".join(b)))
            for j, o in enumerate(opts):
                no = norm(o)
                if no and (nb == no or (nb.startswith(no + " ") and len(b) == 1)): ans = j; break
            if ans is not None: break
        if ans is None: continue
        note = " ".join(" ".join(b) for b in blocks[k + 3:])[:240]
        raw.append(dict(i=f"N14-{part}-{pi:03d}", stem=stem, opts=[[chr(65 + j), o] for j, o in enumerate(opts)], a=chr(65 + ans), n=note))
print("parsed with answer:", len(raw))
# system + duplicate check against the other banks
site = json.load(open("site/data.json", encoding="utf-8"))
def label(q):
    b, s = q["b"], q["s"]
    if b == "Pediatrics": return "Pediatrics"
    if b == "OB/GYN": return "OB/GYN"
    if b == "Surgery": return "Surgery"
    if b == "Medicine": return "Medicine"
    if b == "GameBoy": return "Medicine" if s == "Medicine" else "OB/GYN"
    return {"OBGYN": "OB/GYN", "Medicine": "Medicine", "Pediatrics": "Pediatrics", "Surgery": "Surgery"}.get(s, "Other")
ref = [q for q in site if q["b"] != "Alhomrani 10-14"]
T = re.compile(r"[a-z][a-z0-9\-]{2,}")
tk = lambda q, o: T.findall((q + " " + " ".join(t for _, t in o)).lower())
docs = [tk(q["q"], q["o"]) for q in ref] + [tk(r["stem"], r["opts"]) for r in raw]
df = Counter(w for d in docs for w in set(d)); N = len(docs)
keep = [w for w, c in df.most_common() if 2 <= c <= 600][:9000]; voc = {w: i for i, w in enumerate(keep)}
M = np.zeros((N, len(voc)), dtype=np.float32)
for r, d in enumerate(docs):
    for w, c in Counter(d).items():
        if w in voc: M[r, voc[w]] = (1 + np.log(c)) * np.log(N / df[w])
M /= np.maximum(np.linalg.norm(M, axis=1, keepdims=True), 1e-9)
S = M[len(ref):] @ M[:len(ref)].T
out = []; dup = diff = 0
for r, it in enumerate(raw):
    top = np.argsort(-S[r])[:5]; votes = Counter(label(ref[j]) for j in top)
    sysn = votes.most_common(1)[0][0]
    j = int(S[r].argmax()); s = float(S[r, j]); note = it["n"]
    if s >= 0.85:
        o = ref[j]; ta = dict(o["o"]).get(o["a"], "").lower().strip(); tb = dict(it["opts"])[it["a"]].lower().strip()
        if ta and (ta in tb or tb in ta): dup += 1; note = ("مكرر من القديم (" + o["i"] + "). " + note)[:260]
        else: diff += 1; note = ("⚠ يشبه " + o["i"] + " لكن جوابه: " + dict(o["o"]).get(o["a"], "")[:40] + ". " + note)[:260]
    out.append(dict(i=it["i"], b="Alhomrani 10-14", s=sysn, t="كل أسئلة النظام", h="", q=it["stem"], o=it["opts"], a=it["a"], k="", r="", n=note, f=""))
print("duplicates:", dup, "similar-but-different:", diff, Counter(o["s"] for o in out))
json.dump(out, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False)
