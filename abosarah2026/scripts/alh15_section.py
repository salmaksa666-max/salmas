"""Alhomrani '15 November' file as its own section inside the Silent bank: every page of his file -> best-matching
question (exam-recalls bank first, then all banks); copies carry id AH15-<orig>. Pages that match nothing are listed."""
import json, re, glob, sys, os
import numpy as np
from collections import Counter
SP = sys.argv[1]  # scratchpad n15 dir
pages = {}
for line in open(os.path.join(SP, "compact.txt"), encoding="utf-8"):
    m = re.match(r"@@(\d+): (.*)", line.strip())
    if m and len(m.group(2)) > 60 and not re.search(r"If You Have Any New Recall|^WARNING|End Of The File|Corrected By|WARNING", m.group(2)): pages[int(m.group(1))] = m.group(2)
for f in glob.glob(os.path.join(SP, "pg", "*.txt")):
    n = int(re.findall(r"p(\d+)", f)[-1]); t = re.sub(r"\s+", " ", open(f).read())
    if len(t) > 60: pages[n] = t
SIL = json.load(open("site/silent.json", encoding="utf-8"))
ALL = [q for q in json.load(open("site/data_all.json", encoding="utf-8"))]
pages = dict(sorted(pages.items()))
cands = SIL + ALL
tok = lambda s: re.findall(r"[a-z]{3,}", s.lower())
docs = [tok(q["q"] + " " + " ".join(o[1] for o in q["o"])) for q in cands] + [tok(t) for t in pages.values()]
df = Counter(w for d in docs for w in set(d)); W = {w: i for i, w in enumerate(df)}
M = np.zeros((len(docs), len(W)), np.float32)
for r, d in enumerate(docs):
    for w, c in Counter(d).items(): M[r, W[w]] = (1 + np.log(c)) * np.log(len(docs) / df[w])
M /= np.maximum(np.linalg.norm(M, axis=1, keepdims=True), 1e-9)
X = M[len(cands):] @ M[:len(cands)].T
out, seen, miss = [], set(), []
BAD = {23, 44, 49, 100}  # pages whose best match is a different question
MAN = {78: "itching (urticaria) during a blood transfusion", 95: "sandpaper skin rash", 99: "after thyroidectomy, a patient develops neck swelling",
       100: "written IM instead of IV", 23: "epiglottitis", 22: "lower GI bleeding"}
_find = lambda frag: next((i for i, q in enumerate(SIL) if frag.lower() in q["q"].lower()), None)
for k, (pg, t) in enumerate(pages.items()):
    sims = X[k]; j = int(np.argmax(sims[:len(SIL)])); s = float(sims[j])
    if pg in MAN and _find(MAN[pg]) is not None: j, s = _find(MAN[pg]), 1.0
    elif pg in BAD: miss.append((pg, "bad", t[:90])); continue
    if s < 0.45:
        j2 = int(np.argmax(sims)); 
        if float(sims[j2]) > s: j, s = j2, float(sims[j2])
    if s < 0.24: miss.append((pg, round(s, 2), t[:90])); continue
    q = dict(cands[j]); base = q["i"][3:] if q["i"].startswith("SL-") else q["i"]
    if base in seen: continue
    seen.add(base)
    q.update(i="AH15-" + base, b="Silent", s="ملف الحمراني 15 نوفمبر", t="كل أسئلة النظام", h="", n=f"ملف الحمراني 15 نوفمبر (صفحة {pg}). " + (q.get("n") or ""))
    q.pop("si", None); out.append(q)
    if s < 0.5: print("  low", pg, round(s, 2), "|", t[:70], "||", cands[j]["q"][:70])
json.dump(out, open("site/alh15.json", "w", encoding="utf-8"), ensure_ascii=False)
print("pages", len(pages), "section", len(out), "unmatched", len(miss))
for m in miss: print("  miss", m)
