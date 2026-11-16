"""Yasir Nov questions that already exist in Alhomrani's files (Nov 1-14, 15, 16) -> data/yasir_dupes.json"""
import json, re, sys, collections, numpy as np
Q = json.load(open("site/data.json")); Q = Q["questions"] if isinstance(Q, dict) else Q
Y = [q for q in Q if q["b"] == "Yasir Nov"]
A = [q for q in Q if q["b"] == "Alhomrani Nov" or q["i"].startswith(("AH15-", "AH16-"))]
tok = lambda s: re.findall(r"[a-z]{3,}", s.lower())
txt = lambda q: q["q"] + " " + " ".join(o for _, o in q["o"])
docs = [tok(txt(q)) for q in Y + A]; df = collections.Counter(w for d in docs for w in set(d)); W = {w: i for i, w in enumerate(df)}; N = len(docs)
M = np.zeros((N, len(W)), np.float32)
for i, d in enumerate(docs):
    for w, c in collections.Counter(d).items(): M[i, W[w]] = (1 + np.log(c)) * np.log(N / df[w])
M /= np.linalg.norm(M, axis=1, keepdims=True) + 1e-9
S = M[:len(Y)] @ M[len(Y):].T
best, j = S.max(1), S.argmax(1)
TH = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
ans = lambda q: set(tok(dict(q["o"]).get(q["a"], "")))
def jac(a, b): return len(a & b) / max(1, len(a | b))
out = {}
for k in range(len(Y)):
    # best Alhomrani match among the top 5 whose key answer agrees
    for jj in np.argsort(-S[k])[:5]:
        s_ = float(S[k, jj]); aj = jac(ans(Y[k]), ans(A[jj]))
        if s_ >= 0.62 or (s_ >= TH and aj >= 0.5):
            out[Y[k]["i"]] = [A[jj]["i"], round(s_, 3), round(aj, 2)]; break
json.dump(out, open("data/yasir_dupes.json", "w"), indent=0)
print("Yasir", len(Y), "dupes", len(out), "kept", len(Y) - len(out))
if len(sys.argv) > 2:
    import random; random.seed(int(sys.argv[2]))
    D = {q["i"]: q for q in A}; YY = {q["i"]: q for q in Y}
    band = [k for k, v in out.items() if v[1] < 0.62]
    for k in random.sample(band, min(10, len(band))):
        a = D[out[k][0]]; y = YY[k]; print(out[k][1:], "\n Y:", y["q"][:120], "=>", dict(y["o"])[y["a"]][:40], "\n A:", a["q"][:120], "=>", dict(a["o"])[a["a"]][:40])
    miss = [q for q in Y if q["i"] not in out and 0.5 <= float(best[Y.index(q)]) ]
    print("high-sim but different answer:", len(miss))
    for y in random.sample(miss, min(6, len(miss))):
        a = A[j[Y.index(y)]]; print(" Y:", y["q"][:110], "=>", dict(y["o"])[y["a"]][:35], "\n A:", a["q"][:110], "=>", dict(a["o"])[a["a"]][:35])
