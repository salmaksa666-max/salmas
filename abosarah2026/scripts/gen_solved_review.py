# -*- coding: utf-8 -*-
"""Items JSON (build_mkj_dense.py with DUMP=) -> review-sheet source for build_review.py:
one block per disease (split into chunks), questions on the left, each card's exam pearl on the right.
usage: gen_solved_review.py ITEMS.json OUT.txt [CHUNK]"""
import json
import sys

items = json.load(open(sys.argv[1], encoding="utf-8"))
CH = int(sys.argv[3]) if len(sys.argv) > 3 else 7
out, sec, groups = [], None, []
for it in items:
    if groups and groups[-1][0] == (it["sec"], it["dn"]):
        groups[-1][1].append(it)
    else:
        groups.append(((it["sec"], it["dn"]), [it]))
for (s, dn), its in groups:
    if s != sec:
        sec = s
        out.append(f"# {s}")
    parts = [its[i:i + CH] for i in range(0, len(its), CH)]
    for k, part in enumerate(parts, 1):
        out.append(f"== {dn}" + (f"  ({k}/{len(parts)})" if len(parts) > 1 else ""))
        for it in part:
            badge = f"{{{{rep:{it['rep']}}}}} " if it["rep"] else ""
            stem = " ".join(it["stem"].replace("|", "/").split())
            out.append(f"q: {badge}{stem} | {it['ans'].replace('|', '/')}{it['flag']} @{it['qid']}")
        out.append("idea:")
        for i, it in enumerate(part):
            out.append(f"- [[{i}]] {it['pearl']}")
            if it["check"]:
                out.append(f"- [[{i}]] ⚠ {it['check']}")
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(out) + "\n")
print(len(groups), "diseases,", sum(len(g[1]) for g in groups), "questions")
