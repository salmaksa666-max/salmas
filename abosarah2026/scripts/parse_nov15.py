"""Alhomrani '15 November' PDF (one recall per page) -> n15.json  [{n, stem, opts, ans, note, sec}]"""
import re, json, sys
txt = open(sys.argv[1], encoding="utf-8").read().split("\f")
HDR = re.compile(r"https?://t\.me/\S+|^\s*15 November\s*$|^\s*10[–-]14 November\s*$")
norm = lambda t: re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()
out, sec = [], ""
for pi, pg in enumerate(txt, 1):
    L = [HDR.sub("", l).strip() for l in pg.splitlines()]
    L = [l for l in L if l]
    for l in L:
        if re.match(r"^(New Questions|Repeated|Modified|Old|Repeated Questions|Modified Questions)\b", l, re.I): sec = l
    st = next((i for i, l in enumerate(L) if re.match(r"^\d{1,4}\.\s", l)), None)
    if st is None: continue
    oi = [i for i, l in enumerate(L) if i > st and re.match(r"^[A-F][\.\)\-]\s*\S", l)]
    if len(oi) < 2: out.append(dict(page=pi, n=int(L[st].split(".")[0]), stem=" ".join(L[st:st + 8]), opts=[], ans=None, note="", sec=sec, raw=L)); continue
    # options = first run of consecutive lettered lines (A, B, C...)
    run = [oi[0]]
    for i in oi[1:]:
        if ord(L[i][0]) == ord(L[run[-1]][0]) + 1: run.append(i)
        else: break
    stem = re.sub(r"^\d{1,4}\.\s*", "", " ".join(L[st:run[0]]))
    opts = [re.sub(r"^[A-F][\.\)\-]\s*", "", L[i]) for i in run]
    rest = L[run[-1] + 1:]
    ans = None
    for l in rest:
        m = re.match(r"^([A-F])[\.\)\-]\s*(.+)", l)
        if m and m.group(1) in "ABCDEF"[:len(opts)] and norm(m.group(2))[:12] == norm(opts["ABCDEF".index(m.group(1))])[:12]:
            ans = "ABCDEF".index(m.group(1)); break
        nl = norm(l)
        for j, o in enumerate(opts):
            if nl and norm(o) and nl == norm(o): ans = j; break
        if ans is not None: break
    out.append(dict(page=pi, n=int(L[st].split(".")[0]), stem=stem, opts=opts, ans=ans, note=" ".join(rest)[:900], sec=sec))
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(out), "with opts", sum(bool(o["opts"]) for o in out), "with answer", sum(o["ans"] is not None for o in out))
from collections import Counter; print(Counter(o["sec"] for o in out))
