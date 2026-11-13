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
# Yasir November
ex = L("yasir/expl.json")
for it in L("yasir/items_fixed.json"):
    add("Yasir Nov", it, it.get("spec") or "", it.get("exam") or "", "", ex.get(it["qid"]))
json.dump(out, open(sys.argv[1], "w", ensure_ascii=False and None) if False else open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
from collections import Counter
print(len(out), Counter(x["b"] for x in out))
