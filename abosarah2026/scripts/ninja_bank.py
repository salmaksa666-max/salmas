"""Ninja SMLE Recall polls (today) -> site bank; only polls whose correct option is marked."""
import json, re, sys
import numpy as np
from collections import Counter
today = json.load(open(sys.argv[1], encoding="utf-8"))
full = {re.sub(r"\W+", "", v["text"].lower())[:50]: v["text"] for v in today if not v["poll"] and v["text"]}
raw = []
for v in today:
    p = v["poll"]
    if not p: continue
    blank = [i for i, (t, pc) in enumerate(p["opts"]) if pc == ""]
    if len(blank) != 1: continue
    stem = full.get(re.sub(r"\W+", "", p["q"].lower())[:50], p["q"])
    opts = [[chr(65 + i), t] for i, (t, pc) in enumerate(p["opts"]) if t and not t.startswith("(no ")]
    raw.append(dict(i=f"NJ-{v['id']}", q=" ".join(stem.split()), o=opts, a=chr(65 + blank[0])))
site = json.load(open("site/data_all.json", encoding="utf-8"))
def label(q):
    b, s = q["b"], q["s"]
    if b in ("Pediatrics", "OB/GYN", "Surgery", "Medicine"): return b
    if b == "GameBoy": return "Medicine" if s == "Medicine" else "OB/GYN"
    return {"OBGYN": "OB/GYN"}.get(s, s if s in ("Medicine", "Pediatrics", "Surgery") else "Other")
T = re.compile(r"[a-z][a-z0-9\-]{2,}")
tk = lambda q, o: T.findall((q + " " + " ".join(t for _, t in o)).lower())
docs = [tk(q["q"], q["o"]) for q in site] + [tk(r["q"], r["o"]) for r in raw]
df = Counter(w for d in docs for w in set(d)); N = len(docs)
keep = [w for w, c in df.most_common() if 2 <= c <= 600][:9000]; voc = {w: i for i, w in enumerate(keep)}
M = np.zeros((N, len(voc)), dtype=np.float32)
for r, d in enumerate(docs):
    for w, c in Counter(d).items():
        if w in voc: M[r, voc[w]] = (1 + np.log(c)) * np.log(N / df[w])
M /= np.maximum(np.linalg.norm(M, axis=1, keepdims=True), 1e-9)
S = M[len(site):] @ M[:len(site)].T
out = []
for r, it in enumerate(raw):
    top = np.argsort(-S[r])[:5]
    sysn = Counter(label(site[j]) for j in top).most_common(1)[0][0]
    j = int(S[r].argmax()); s = float(S[r, j]); o = site[j]
    note = "جواب القناة (علامة الاستفتاء)، غير مؤكد."
    k = r_ = ""; kw = []
    if s >= 0.8:
        oa = dict(o["o"]).get(o["a"], "")
        note = ("مكرر (" + o["i"] + ") وجوابه هناك: " + oa[:50] + ". " + note)[:260]
        k, r_, kw = o.get("k", ""), o.get("r", ""), o.get("kw", [])
    out.append(dict(it, b="Ninja", s=sysn, t="كل أسئلة النظام", h="", k=k, r=r_, n=note, f="", im=[], kw=kw))
print(len(raw), Counter(x["s"] for x in out))
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False)
