# -*- coding: utf-8 -*-
"""One-off sweep: replace a curated list of Arabic clinical exam-sign terms
with their English equivalent wrapped in <bdi>, across all data_batch*.py
source files. Run once, then re-merge and rebuild.
"""
import glob
import re

FILES = sorted(glob.glob("data_batch*.py"))

MURMUR_RE = re.compile(r'(ال)?(نفخات|نفخة)')
def murmur_repl(m):
    prefix = "الـ" if m.group(1) else ""
    word = "murmurs" if m.group(2) == "نفخات" else "murmur"
    return f'{prefix}<bdi>{word}</bdi>'

CREPITATIONS_RE = re.compile(r'(ال)?كركرة')
def crep_repl(m):
    prefix = "الـ" if m.group(1) else ""
    return f'{prefix}<bdi>crepitations</bdi>'

NYSTAGMUS_RE = re.compile(r'(ال)?رأرأة')
def nystagmus_repl(m):
    prefix = "الـ" if m.group(1) else ""
    return f'{prefix}<bdi>nystagmus</bdi>'

PERICARDIAL_RUB_RE = re.compile(r'(ال)?احتكاك\s+(ال)?تامور[يى]?')
def pericardial_repl(m):
    prefix = "الـ" if m.group(1) else ""
    return f'{prefix}<bdi>pericardial friction rub</bdi>'

RUB_RE = re.compile(r'(ال)?احتكاك')
def rub_repl(m):
    prefix = "الـ" if m.group(1) else ""
    return f'{prefix}<bdi>friction rub</bdi>'


def fix_line(line):
    if "مناطق الاحتكاك" in line:
        # skin/dermatology sense (e.g. extensor "friction areas" like elbows),
        # not a cardiac/pericardial sign — leave untouched.
        pass
    else:
        line = PERICARDIAL_RUB_RE.sub(pericardial_repl, line)
        line = RUB_RE.sub(rub_repl, line)
    line = MURMUR_RE.sub(murmur_repl, line)
    line = CREPITATIONS_RE.sub(crep_repl, line)
    line = NYSTAGMUS_RE.sub(nystagmus_repl, line)
    return line


total_changes = 0
for path in FILES:
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    new_lines = []
    file_changes = 0
    for line in lines:
        new_line = fix_line(line)
        if new_line != line:
            file_changes += 1
        new_lines.append(new_line)
    if file_changes:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"{path}: {file_changes} lines changed")
        total_changes += file_changes

print("TOTAL lines changed:", total_changes)
