"""Where a Yasir-only question matches (>=0.8) a question from the Alhomrani deck / our other banks and the reference answer
text is one of Yasir's options, switch Yasir's answer to the reference one."""
import json, re, sys
import numpy as np
from collections import Counter
P = "site/data.json"
d = json.load(open(P, encoding="utf-8"))
ys = [q for q in d if q["b"] == "Yasir Nov"]
ref = [q for q in d if q["b"] == "Alhomrani Nov"]
T = re.compile(r"[a-z][a-z0-9\-]{2,}")
tk = lambda q: T.findall((q["q"] + " " + " ".join(t for _, t in q["o"])).lower())
docs = [tk(q) for q in ys + ref]
df = Counter(w for x in docs for w in set(x)); N = len(docs)
keep = [w for w, c in df.most_common() if 2 <= c <= 500][:9000]; voc = {w: i for i, w in enumerate(keep)}
M = np.zeros((N, len(voc)), dtype=np.float32)
for r, x in enumerate(docs):
    for w, c in Counter(x).items():
        if w in voc: M[r, voc[w]] = (1 + np.log(c)) * np.log(N / df[w])
M /= np.maximum(np.linalg.norm(M, axis=1, keepdims=True), 1e-9)
S = M[:len(ys)] @ M[len(ys):].T
norm = lambda t: set(re.findall(r"[a-z0-9]+", t.lower()))
changed = []
for r, q in enumerate(ys):
    j = int(S[r].argmax()); s = float(S[r, j])
    if s < 0.7: continue
    o = ref[j]; ra = dict(o["o"]).get(o["a"], "")
    ya = dict(q["o"]).get(q["a"], "")
    A, B = norm(ra), norm(ya)
    if not A or (A & B) and len(A & B) / len(A | B) >= 0.6: continue  # same answer
    best, bs = None, 0
    for k, t in q["o"]:
        X = norm(t)
        if X and A:
            sc = len(A & X) / len(A | X)
            if sc > bs: best, bs = k, sc
    if best and bs >= 0.7 and best != q["a"]:
        changed.append((q["i"], q["a"], best, round(s, 2), ya[:35], dict(q["o"])[best][:35], o["i"]))
        q["a"] = best
        q["n"] = ("الحمراني: " + ra[:80] + " · " + q["n"])[:260]
print(len(changed))
for c in changed: print(c)
json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
