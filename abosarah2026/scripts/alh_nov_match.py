"""1-9 November: match every page of Alhomrani's PDFs to the MKJ card made from it, read HIS answer off the page,
and report agreement. Output: SD/nov19_pages.json"""
import json, re, os, sys
import numpy as np
from collections import Counter
SD = sys.argv[1]
def pages(key):
    P = open(os.path.join(SD, key + ".raw.txt"), encoding="utf-8", errors="ignore").read().split("\f")
    for i in range(len(P)):
        o = os.path.join(SD, "ocr", f"{key}_{i + 1}.txt")
        if os.path.exists(o) and len(re.sub(r"\s", "", P[i])) < 120: P[i] = open(o, encoding="utf-8", errors="ignore").read()
    return P
PG = [(k, i + 1, t) for k in ("N15f", "N68", "N9") for i, t in enumerate(pages(k))]
PG = [x for x in PG if len(re.findall(r"[a-z]{3,}", x[2].lower())) > 15 and not re.search(r"WARNING|Corrected By|End Of The File|If You Have Any New Recall", x[2][:300])]
MK = json.load(open("site/mkj.json", encoding="utf-8"))
tok = lambda s: re.findall(r"[a-z]{3,}", s.lower())
docs = [tok(t) for _, _, t in PG] + [tok(q["q"] + " " + " ".join(o[1] for o in q["o"])) for q in MK]
df = Counter(w for d in docs for w in set(d)); W = {w: i for i, w in enumerate(df)}
M = np.zeros((len(docs), len(W)), np.float32)
for r, d in enumerate(docs):
    for w, c in Counter(d).items(): M[r, W[w]] = (1 + np.log(c)) * np.log(len(docs) / df[w])
M /= np.maximum(np.linalg.norm(M, axis=1, keepdims=True), 1e-9)
S = M[:len(PG)] @ M[len(PG):].T
norm = lambda t: re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()
res = []
for i, (k, p, t) in enumerate(PG):
    j = int(S[i].argmax()); s = float(S[i, j]); q = MK[j]; nt = norm(t)
    his = None
    m = re.findall(r"(?:final\s+)?answer\s*(?:is|:)?\s*[\"“”']?\s*([a-f])\b", nt)
    hits = [(len(norm(o)), L) for L, o in q["o"] if len(norm(o)) > 1 and nt.count(norm(o)) >= 2]
    if hits:
        mx = max(hits)[0]; top = [L for n, L in hits if n == mx]
        if len(top) == 1: his = top[0]
    if his is None and m: his = m[-1].upper()
    res.append(dict(src=k, page=p, id=q["i"], sim=round(s, 2), mk=q["a"], his=his, st=q["st"]))
json.dump(res, open(os.path.join(SD, "nov19_pages.json"), "w"))
good = [r for r in res if r["sim"] >= 0.5]
print("pages", len(PG), "matched>=0.5", len(good), "distinct cards", len({r["id"] for r in good}), "of", len(MK))
print("answer read", sum(r["his"] is not None for r in good), "agree", sum(r["his"] == r["mk"] for r in good), "disagree", sum(r["his"] not in (None, r["mk"]) for r in good))
print(Counter(r["src"] for r in good))
