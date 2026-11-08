# -*- coding: utf-8 -*-
"""Parse 'SMLE Recalls · 1–7 November · by Yasir' (pdftotext -layout output) into items + expl JSON
in the dump_mkj.py shape, plus specialty / look-alike set info.
usage: parse_yasir.py Y.txt ITEMS.json EXPL.json"""
import json
import re
import sys

TXT, ITEMS, EXPL = sys.argv[1:4]
SPECS = {"MEDICINE": "Medicine", "SURGERY": "Surgery", "PEDIATRICS": "Pediatrics", "OB / GYN": "OB/GYN",
         "ETHICS & PUBLIC HEALTH": "Ethics & public health", "PSYCHIATRY, ENT, EYE & SKIN": "Psychiatry, ENT, eye & skin"}
lines = open(TXT, encoding="utf-8").read().replace("\f", "\n").split("\n")
start = next(i for i, l in enumerate(lines) if re.match(r"^\s*MEDICINE \d+ questions\s*$", l))
lines = [l for l in lines[start:] if not re.match(r"^\s*SMLE Recalls · 1–7 November 2026 · by Yasir\s+\d+\s*$", l)]


def para(ls):
    return re.sub(r"\s+", " ", " ".join(x.strip() for x in ls)).strip()


items, spec, cur_set, i = [], None, None, 0
while i < len(lines):
    l = lines[i]
    m = re.match(r"^\s*([A-Z ,/&]+) \d+ questions\s*$", l)
    if m and m.group(1).strip() in SPECS:
        spec = SPECS[m.group(1).strip()]
        cur_set = None
        i += 1
        continue
    m = re.match(r"^\s*LOOK-ALIKE SET (\d+) · (.*?) \((\d+) questions\)\s*$", l)
    if m:
        j, how = i + 1, []
        while j < len(lines) and lines[j].strip():
            how.append(lines[j])
            j += 1
        cur_set = dict(n=int(m.group(1)), title=m.group(2).strip(), how=para(how).replace("How to tell them apart:", "").strip(), first=True, left=int(m.group(3)))
        i = j
        continue
    if re.match(r"^\s*Exam: ", l):
        exam = l.strip()
        j = i + 1
        before = False
        while not re.match(r"^\s*\d{1,3}\. ", lines[j]):
            if "LOOK-ALIKE FROM BEFORE" in lines[j]:
                before = True
            elif lines[j].strip() and not lines[j].strip().startswith("Exam"):
                exam += " " + lines[j].strip()
            j += 1
        m = re.match(r"^\s*(\d{1,3})\. (.*)$", lines[j])
        num, stem = int(m.group(1)), [m.group(2)]
        j += 1
        while not re.match(r"^\s{2,}[A-E]\. ", lines[j]):
            stem.append(lines[j])
            j += 1
        opts = []
        while not re.match(r"^\s*The answer is ", lines[j]):
            mo = re.match(r"^\s{2,}([A-E])\. (.*)$", lines[j])
            if mo:
                opts.append([mo.group(1), mo.group(2).strip()])
            elif lines[j].strip() and opts:
                opts[-1][1] += " " + lines[j].strip()
            j += 1
        ma = re.match(r"^\s*The answer is ([A-E])\s+(.*)$", lines[j])
        letter, src = ma.group(1), re.sub(r"\s{2,}", " | ", ma.group(2).strip())
        j += 1
        body = []
        while j < len(lines) and not re.match(r"^\s*(Exam: |LOOK-ALIKE SET \d+ · |[A-Z ,/&]+ \d+ questions\s*$)", lines[j]):
            body.append(lines[j])
            j += 1
        # body: explanation paragraph(s), "Why not X? ...", "Claude's note: ..."
        blocks, curb = [], []
        for x in body:
            if not x.strip():
                if curb:
                    blocks.append(para(curb))
                    curb = []
            else:
                curb.append(x)
        if curb:
            blocks.append(para(curb))
        expl, whynot, cnote = [], [], []
        for b in blocks:
            parts = re.split(r"(?=Why not [A-E](?: or [A-E])?\?)", b)
            for p in parts:
                p = p.strip()
                if not p:
                    continue
                if p.startswith("Why not"):
                    whynot.append(p)
                elif p.startswith("Claude's note:"):
                    cnote.append(re.sub(r"^Claude's note:\s*(Claude:\s*)?", "", p))
                else:
                    expl.append(p)
        ans_txt = dict((k, t) for k, t in opts).get(letter, "")
        items.append(dict(num=num, spec=spec, exam=exam, before=before, stem=para(stem), opts=opts, letter=letter,
                          ans=f"{letter}. {ans_txt}", src=src, claude=src.strip() == "Claude",
                          expl=" ".join(expl), whynot=" ".join(whynot), cnote=" ".join(cnote),
                          set=(dict(n=cur_set["n"], title=cur_set["title"], how=cur_set["how"]) if cur_set else None),
                          set_first=bool(cur_set and cur_set.pop("first", False))))
        if cur_set:
            cur_set["left"] -= 1
            if cur_set["left"] <= 0:
                cur_set = None
        i = j
        continue
    i += 1

assert len(items) == 764, len(items)
assert [x["num"] for x in items] == list(range(1, 765))
bad = [x["num"] for x in items if x["letter"] not in [k for k, _ in x["opts"]]]
print(len(items), "items; answer letter missing from options:", bad)
out, ex = [], {}
for x in items:
    q = f"NOV-{x['num']:03d}"
    exam_date = re.search(r"Exam: ([^●]+)●", x["exam"])
    out.append(dict(qid=q, stem=x["stem"], opts=[tuple(o) for o in x["opts"]], ans=x["ans"],
                    flag=" ⚠" if x["claude"] else "", rep=("قبل نوفمبر" if x["before"] else ""),
                    spec=x["spec"], set=x["set"], set_first=x["set_first"], src=x["src"], claude=x["claude"],
                    exam=(exam_date.group(1).strip() if exam_date else ""), num=x["num"]))
    # rule = the explanation without the trailing source parenthesis; author = why-not + Claude's note
    e = re.sub(r"\s*\((?:[^()]*(?:answer|key|extract|post|file|slide|Gameboy|Medgard|review)[^()]*)\)\s*$", "", x["expl"]).strip()
    ex[q] = dict(rule=e, author=" ".join(t for t in (x["whynot"], ("Claude: " + x["cnote"]) if x["cnote"] else "") if t),
                 key="", decide=[], whynot=x["whynot"], cnote=x["cnote"], expl_full=x["expl"])
json.dump(out, open(ITEMS, "w", encoding="utf-8"), ensure_ascii=False)
json.dump(ex, open(EXPL, "w", encoding="utf-8"), ensure_ascii=False)
from collections import Counter
print(Counter(x["spec"] for x in out), sum(x["claude"] for x in out), "answered by Claude;", sum(bool(x["rep"]) for x in out), "look-alikes from before Nov")
