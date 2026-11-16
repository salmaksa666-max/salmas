"""Silent channel 15 Nov: recalls (data/silent_recalls.py) + screenshot questions matched to existing banks -> site/silent.json"""
import json, sys, os, re
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
    out.append(dict(i=f"SL-{pid}-{j:02d}", q=q, o=[[L[i], o] for i, o in enumerate(opts)], a=a, b="Silent", s=sec(pid), t="كل أسئلة النظام", h="", k=k, r=r, n=(("الحمراني 15 نوفمبر. " if pid >= 91000 else "سايلنت %s #%d. " % ("الاثنين 16" if pid > 88562 else "الأحد 15", pid))) + n, f="", im=[], kw=[]))
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
ANS = {"SL-SWR-1877": ("B", "✔ جواب الصورة في القناة: B (Varicella vaccine خلال 3–5 أيام من التعرض). إذا كان مطعم → Reassure.")}
for q in out:
    if q["i"] in ANS:
        q["a"], _nn = ANS[q["i"]]; q["n"] = _nn + " " + (q.get("n") or "")
ALH = {88435, 88438, 88442, 88447, 88453, 88491}   # same answer in Alhomrani's 15 November file
COMM = {88549, 88550, 88560, 88610}                 # answer given in the channel comments
RECALLER = {88450, 88551, 88552, 88553, 88555, 88557, 88558, 88444, 88454, 88455, 88456, 88546, 88613, 88614, 88729, 88457, 88507}   # the person who sat the exam wrote the answer
SHOTS = {88564, 88574, 88584, 88591, 88601, 88637, 88646, 88656, 88681, 88691, 88701, 88712, 88719}  # answer printed on the channel screenshot
for q in out:  # say where each answer comes from; flag the ones that are only Claude's
    m = re.match(r"(SL|NJ)-(\d+)", q["i"]); n = q.get("n") or ""
    if not m or re.search(r"✔|التعليقات|التصويت|الحمراني|التجميع|مفتاح|GameBoy|الملف", n): continue
    pid = int(m.group(2))
    if m.group(1) == "NJ": q["n"] = "✔ نفس تصويت نينجا. " + n
    elif pid in ALH: q["n"] = "✔ الحمراني 15 نوفمبر. " + n
    elif pid in COMM: q["n"] = "✔ التعليقات. " + n
    elif pid in RECALLER: q["n"] = "✔ الجواب كتبه اللي اختبر. " + n
    elif pid in SHOTS: q["n"] = "✔ جواب الصورة في القناة. " + n
    else: q["n"] = "⚠ جواب Claude، مو مؤكد. " + n
PIC = {"SL-88549": ["joefig_p03_b3.webp"]}  # recall says "picture of endometrial polyp" -> hysteroscopy image from Joe
for q in out:
    for k, v in PIC.items():
        if q["i"].startswith(k + "-"): q["pi"] = v
json.dump(out, open("site/silent.json", "w", encoding="utf-8"), ensure_ascii=False)
print(len(R), len(out))
