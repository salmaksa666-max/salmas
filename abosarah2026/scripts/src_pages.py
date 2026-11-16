"""Find, for every question, the page of its source PDF (Alhomrani Nov files, 10-14 parts, Yasir, GB 14 NOV, Sep/Oct bank)."""
import json, re, sys, os
import numpy as np
from collections import Counter
SD = sys.argv[1]
PDFS = {k: open(os.path.join(SD, k + ".txt"), encoding="utf-8", errors="ignore").read().split("\f") for k in ["P1", "P2", "UP", "N68", "N9", "YA", "GB14", "SO"]}
# UP covers Sep-Nov: keep only its November pages
PDFS["UP"] = [p if re.search(r"November", p[:400]) else "" for p in PDFS["UP"]]
D = json.load(open("site/data.json", encoding="utf-8"))
WANT = {"Alhomrani Nov": ["P1", "P2", "UP", "N68", "N9"], "Yasir Nov": ["YA"], "GameBoy Nov": ["GB14"],
        "Silent": ["P1", "P2", "UP", "N68", "N9", "SO", "YA"]}
tok = lambda s: re.findall(r"[a-z]{3,}", s.lower())
pages = [(k, i, t) for k in PDFS for i, t in enumerate(PDFS[k]) if len(tok(t)) > 8]
qs = [q for q in D if q["b"] in WANT and not q.get("ap")]
docs = [tok(t) for _, _, t in pages] + [tok(q["q"] + " " + " ".join(o[1] for o in q["o"])) for q in qs]
df = Counter(w for d in docs for w in set(d)); W = {w: i for i, (w, c) in enumerate([x for x in df.most_common() if 2 <= x[1] <= 3000][:12000])}
N = len(docs)
def vec(d):
    v = {}
    for w, c in Counter(d).items():
        if w in W: v[W[w]] = (1 + np.log(c)) * np.log(N / df[w])
    return v
def mat(ds):
    m = np.zeros((len(ds), len(W)), np.float32)
    for i, d in enumerate(ds):
        for j, val in vec(d).items(): m[i, j] = val
    m /= np.maximum(np.linalg.norm(m, axis=1, keepdims=True), 1e-9); return m
PM = mat(docs[:len(pages)]); QM = mat(docs[len(pages):])
S = QM @ PM.T
src = {}; low = 0
for i, q in enumerate(qs):
    allowed = set(WANT[q["b"]])
    mask = np.array([k in allowed for k, _, _ in pages])
    s = np.where(mask, S[i], -1); j = int(s.argmax())
    if s[j] >= 0.45: src[q["i"]] = [pages[j][0], pages[j][1] + 1, round(float(s[j]), 2)]
    else: low += 1
json.dump(src, open(os.path.join(SD, "src_map.json"), "w"))
print(len(qs), "mapped", len(src), "low", low, Counter(v[0] for v in src.values()))
