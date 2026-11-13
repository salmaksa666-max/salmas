"""Collect every structured question bank into one compact JSON for the solve-site."""
import json, re, ast, sys
S = "/tmp/claude-0/-home-user-salmas/a5458d62-c397-540f-8afd-07d9eb2a5edf/scratchpad/"
L = lambda f: json.load(open(f if f.startswith("/") else S + f, encoding="utf-8"))
out, seen = [], set()
norm = lambda t: re.sub(r"\W+", "", t.lower())[:160]


def add(bank, it, sysn, topic, howto="", ex=None):
    ex = ex or {}
    ans = (it.get("ans") or "").strip()
    m = re.match(r"([A-F])[.)]", ans)
    opts = it["opts"]
    if isinstance(opts, str):
        opts = ast.literal_eval(opts)
    opts = [[k, t] for k, t in opts if (t or "").strip()]
    if not opts:
        return
    letter = m.group(1) if m else ""
    if not letter:
        return  # no firm answer: nothing to grade
    key = (bank, norm(it["stem"]), letter)
    if key in seen:
        return
    seen.add(key)
    note = (ex.get("author") or "")
    note = re.sub(r"\s+", " ", note)[:260]
    out.append(dict(i=it["qid"], b=bank, s=sysn, t=topic, h=howto, q=it["stem"].strip(), o=opts, a=letter,
                    k=(ex.get("key") or "")[:300], r=(ex.get("rule") or "")[:300], n=note, f=(it.get("flag") or "").strip()[:80]))


# Pediatrics
pm = L("peds_map.json")
ex = {**L("pedsS_expl.json"), **L("pedsO_expl.json")}
for f in ("fill/pedsS_items.json", "fill/pedsO_items.json"):
    for it in L(f):
        s, t = pm.get(it["qid"], ["Other", "Other"])
        add("Pediatrics", it, s, t, "", ex.get(it["qid"]))
# OB/GYN (grouped)
ex = {**L("obS_expl.json"), **L("obO_expl.json")}
for it in L("ob_grp.json"):
    add("OB/GYN", it, it["sys"], it["topic"], it.get("howto", ""), ex.get(it["qid"]))
# Surgery
sm = L("surgery_map.json")
ex = {**L("surS_expl.json"), **L("surO_expl.json")}
for f in ("fill/surS_items.json", "fill/surO_items.json"):
    for it in L(f):
        s, t = sm.get(it["qid"], ["Other", "Other"])
        add("Surgery", it, s, t, "", ex.get(it["qid"]))
# Medicine
mm = L("merged_map.json")
ex = {**L("sepm_expl.json"), **L("oct_expl.json")}
for f in ("fill/sepm_items.json", "fill/oct_items.json"):
    for it in L(f):
        if it["qid"] in mm:
            s, t = mm[it["qid"]]
            add("Medicine", it, s, t, "", ex.get(it["qid"]))
# GameBoy
for it in L("gb_items.json"):
    add("GameBoy", it, it.get("part") or "GameBoy", it.get("dn") or it.get("sec") or "", it.get("flip") or "",
        {"key": it.get("keyc"), "rule": it.get("pearl")})
# Alhomrani November (MKJ apkg): sourced answers only; replaces the Yasir bank
for it in json.load(open("site/mkj.json", encoding="utf-8")):
    if it["st"] != "sourced" or not it["a"] or len(it["o"]) < 2:
        continue
    if "BRCA1" in it["q"] and "surveillance" in it["q"]:  # Alhomrani post: MRI immediately (not mammogram)
        for k, t in it["o"]:
            if "mri" in t.lower():
                it["a"] = k
    out.append(dict(i=it["i"], b="Alhomrani Nov", s=it["s"], t="كل أسئلة النظام", h="", q=it["q"], o=it["o"], a=it["a"],
                    k="", r="", n=it["n"], f=""))
# Yasir November: only the questions that are NOT in the Alhomrani November deck
import numpy as np
from collections import Counter as _C
_mk = json.load(open("site/mkj.json", encoding="utf-8"))
_ex = L("yasir/expl.json")
_yi = L("yasir/items_fixed.json")
_T = re.compile(r"[a-z][a-z0-9\-]{2,}")
_tk = lambda q, o: _T.findall((q + " " + " ".join(t for _, t in o)).lower())
_docs = [_tk(i["q"], i["o"]) for i in _mk] + [_tk(i["stem"], i["opts"]) for i in _yi]
_df = _C(w for d in _docs for w in set(d)); _N = len(_docs)
_voc = {w: k for k, w in enumerate(_df)}
_M = np.zeros((_N, len(_voc)), dtype=np.float32)
for r, d in enumerate(_docs):
    for w, c in _C(d).items():
        _M[r, _voc[w]] = (1 + np.log(c)) * np.log(_N / _df[w])
_M /= np.maximum(np.linalg.norm(_M, axis=1, keepdims=True), 1e-9)
_S = _M[len(_mk):] @ _M[:len(_mk)].T
_before = len(out)
for r, it in enumerate(_yi):
    if _S[r].max() < 0.75:
        add("Yasir Nov", it, it.get("spec") or "", "", "", _ex.get(it["qid"]))
print("yasir extra:", len(out) - _before)

# --- post-processing -------------------------------------------------
CH = L("fill/alhomrani_changes.json")
gbraw = {i["qid"]: i for i in L("gb_items.json")}
DIFF = re.compile(r"different answer|gives a different|answer (differs|changes)|MODIFIED|conflict", re.I)
dropped = 0
keep = []
for q in out:
    if q["b"] == "Pediatrics" and q["i"] not in CH and "⚠" in q["f"]:
        dropped += 1  # doubtful / conflicting answer: removed unless Alhomrani confirmed it
        continue
    if q["b"] in ("Medicine", "Pediatrics", "Surgery", "Yasir Nov", "Alhomrani Nov"):
        q["t"], q["h"] = "كل أسئلة النظام", ""
    if q["b"] == "GameBoy" and q["s"] == "Medicine":
        q["s"], q["t"], q["h"] = gbraw[q["i"]]["sec"], "كل أسئلة النظام", ""
    keep.append(q)
out = keep
order = []
for q in out:
    if (q["b"], q["s"]) not in order:
        order.append((q["b"], q["s"]))
out.sort(key=lambda q: order.index((q["b"], q["s"])))
print("dropped unsure peds:", dropped)
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
from collections import Counter
print(len(out), Counter(x["b"] for x in out))
