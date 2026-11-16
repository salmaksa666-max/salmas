"""Silent channel 15 Nov: recalls (data/silent_recalls.py) + screenshot questions matched to existing banks -> site/silent.json"""
import json, sys, os
sys.path.insert(0, "data"); from silent_recalls import R; from ninja_recalls import N
SP = sys.argv[1]  # scratchpad silent dir with match.json
D = {q["i"]: q for q in json.load(open("site/data_all.json", encoding="utf-8"))}
AR = {"Alhomrani Nov": "الحمراني", "Alhomrani 10-14": "الحمراني 10-14", "GameBoy": "GameBoy", "Yasir Nov": "ياسر"}
over = {"ph/88491_4.txt": "OCT-6654", "ph/88532_5.txt": "N14-P1-211"}
skip = {"ph/88429_0.txt", "ph/88491_9.txt"}
out, seen = [], set()
def sec(pid): return "كل الأسئلة"
for j, (pid, q, opts, a, k, r, n) in enumerate(R):
    L = "ABCDE"
    import random, re as _re
    good = opts[L.index(a)]
    if not any(_re.match(r"^[\d<>≥]", o) or "months" in o or "weeks" in o or "hours" in o for o in opts):
        opts = opts[:]; random.Random(f"{pid}-{j}").shuffle(opts)  # don't leave the answer on A
    a = L[opts.index(good)]
    out.append(dict(i=f"SL-{pid}-{j:02d}", q=q, o=[[L[i], o] for i, o in enumerate(opts)], a=a, b="Silent", s=sec(pid), t="كل أسئلة النظام", h="", k=k, r=r, n=("سايلنت %s #%d. " % ("الاثنين 16" if pid > 88562 else "الأحد 15", pid)) + n, f="", im=[], kw=[]))
for pid, q, opts, a, k, n in N:
    L = "ABCDE"
    out.append(dict(i=f"NJ-{pid}", q=q, o=[[L[i], o] for i, o in enumerate(opts)], a=a, b="Silent", s="كل الأسئلة", t="كل أسئلة النظام", h="", k=k, r="", n=f"نينجا #{pid} (استفتاء). " + n, f="", im=[], kw=[]))
for x in json.load(open(os.path.join(SP, "match.json"))):
    f = x["f"]
    if f in skip: continue
    i = over.get(f, x["id"])
    if f not in over and x["sim"] < (0.55 if f.startswith("ph") else 0.85): continue
    if i in seen: continue
    seen.add(i); q = dict(D[i])
    src = q["b"]; where = AR.get(src, "سبتمبر/أكتوبر (" + src + ")")
    if f.startswith("ph/"): q["si"] = [os.path.basename(f)[:-4] + ".webp"]
    q.update(i="SL-" + i, b="Silent", s="كل الأسئلة", t="كل أسئلة النظام", h="", n=(f"صورة من نينجا" if os.path.basename(f).startswith("n") else f"صورة من سايلنت {'الاثنين 16' if f[3:8].isdigit() and int(f[3:8]) > 88562 else 'الأحد 15'}") + f" – موجود في {where} ({i}). " + (q.get("n") or ""))
    out.append(q)
import re as _re, numpy as _np
from collections import Counter as _C
_tk = lambda q: _re.findall(r"[a-z]{3,}", (q["q"] + " " + " ".join(o[1] for o in q["o"])).lower())
_T = [_tk(q) for q in out]; _df = _C(w for t in _T for w in set(t)); _w = {w: i for i, w in enumerate(_df)}
_M = _np.zeros((len(out), len(_w)), dtype=_np.float32)
for r, t in enumerate(_T):
    for w, c in _C(t).items(): _M[r, _w[w]] = (1 + _np.log(c)) * _np.log(len(out) / _df[w])
_M /= _np.maximum(_np.linalg.norm(_M, axis=1, keepdims=True), 1e-9)
_S = _M @ _M.T; _drop = set()
for r in range(len(out)):
    if r in _drop: continue
    for c in range(r + 1, len(out)):
        if c not in _drop and _S[r, c] >= 0.8 and dict(out[r]["o"]).get(out[r]["a"], "").lower()[:15] == dict(out[c]["o"]).get(out[c]["a"], "").lower()[:15]: _drop.add(c)
print("dedup dropped", len(_drop))
out = [q for r, q in enumerate(out) if r not in _drop]
json.dump(out, open("site/silent.json", "w", encoding="utf-8"), ensure_ascii=False)
print(len(R), len(out))
