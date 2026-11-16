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
# pages whose recall differs from every stored version: write them as on Alhomrani's page
NEWP = {
 58: dict(q="45-year-old woman with severe vaginal bleeding, hypotensive; β-hCG negative. What is the most appropriate next step?", o=["D&C", "Hysterectomy", "Ultrasound", "Blood transfusion"], a="D",
          k="Unstable bleeding → resuscitate / transfuse first", n="ملف الحمراني 15 نوفمبر (صفحة 58): الجواب Blood transfusion (نفس فكرة 21 أكتوبر)."),
 132: dict(q="A 30-year-old woman G2 P1 L1, LMP 7 weeks ago, has lower abdominal pain and spotting; tender abdomen, closed cervix. Bedside US: no intrauterine pregnancy and moderate intra-abdominal fluid. Most appropriate next step?", o=["Liver enzymes", "BhCG qualitative", "BhCG quantitative", "Complete blood count"], a="C",
          k="Suspected ectopic → quantitative β-hCG", n="ملف الحمراني 15 نوفمبر (صفحة 132)، GameBoy 0415."),
}
out = [q for q in out if int(re.search(r"صفحة (\d+)", q["n"]).group(1)) not in NEWP]
for pg, v in NEWP.items():
    out.append(dict(i=f"AH15-P{pg}", q=v["q"], o=[["ABCD"[i], t] for i, t in enumerate(v["o"])], a=v["a"], b="Silent", s="ملف الحمراني 15 نوفمبر", t="كل أسئلة النظام", h="", k=v["k"], r="", n=v["n"], f="", im=[], kw=[]))
UNSURE = {7: "الحمراني: Fluid (infusion مو bolus) – I Don't Know", 32: "الحمراني رفض يجاوب (ما عاد له دخل بالسؤال)", 33: "الحمراني: كل الخيارات غلط، MG = D",
          43: "الحمراني ما حط جواب", 66: "الحمراني: A أو C، مو مؤكد", 67: "الحمراني: I Don't Know – للنقاش", 102: "الحمراني: A vs C، يميل لـ Suction evacuation",
          107: "الخيارات ناقصة (azathioprine …)، الحمراني ما جاوب", 29: "الحمراني: مو متأكد، يمكن C", 65: "الحمراني: بين C و D، الحين C", 81: "الحمراني ما جاوب"}
for q in out:
    pg = int(re.search(r"صفحة (\d+)", q["n"]).group(1))
    if pg in UNSURE: q["n"] = "⚠ " + UNSURE[pg] + ". " + q["n"]
# Alhomrani's own explanation: his notes from the text pages + the picture of his page (shown after answering)
TXT = {}
for line in open(os.path.join(SP, "compact.txt"), encoding="utf-8"):
    m = re.match(r"@@(\d+): (.*)", line.strip())
    if m: TXT[int(m.group(1))] = [x.strip() for x in m.group(2).split("¦")]
nrm = lambda t: re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()
for q in out:
    pg = int(re.search(r"صفحة (\d+)", q["n"]).group(1))
    if os.path.exists(f"site/a15/p{pg}.webp"): q["ap"] = [f"p{pg}.webp"]
    seg = TXT.get(pg)
    if not seg: continue
    last = max([i for i, x in enumerate(seg) if re.match(r"^[A-F][\.\)]\s", x) or any(nrm(o)[:20] and nrm(o)[:20] == nrm(x)[:20] for _, o in q["o"])] or [-1])
    notes = [x for x in seg[last + 1:] if x and not re.match(r"^(15 November|https?:)", x)]
    notes = [x for x in notes if not re.fullmatch(r"[\d\.\s]+", x)]
    if notes and re.match(r"^\d+\.", notes[0]): notes = []          # page had no lettered options: the 'notes' are the recall itself
    notes = [x for x in notes if "\u202b" not in x]                 # drop Arabic recall fragments
    if len(" ".join(notes)) > 15: q["r"] = "شرح الحمراني: " + " · ".join(notes) + ((" ‖ " + q["r"]) if q.get("r") else "")
out.sort(key=lambda q: int(re.search(r"صفحة (\d+)", q["n"]).group(1)))
json.dump(out, open("site/alh15.json", "w", encoding="utf-8"), ensure_ascii=False)
print("pages", len(pages), "section", len(out), "unmatched", len(miss))
for m in miss: print("  miss", m)

# pack page pictures 4 per sheet (artifact file limit); q["ap"] = ["s<sheet>|<row>"]
from PIL import Image
_pg = sorted({int(x[1:-5]) for q in out for x in q.get("ap", []) if x.startswith("p")}); _pos = {}
os.makedirs("site/a15s", exist_ok=True)
for k in range(0, len(_pg), 4):
    sh = Image.new("RGB", (1267, 713 * 4), "white")
    for i, pg in enumerate(_pg[k:k + 4]): sh.paste(Image.open(f"site/a15/p{pg}.webp"), (0, 713 * i)); _pos[pg] = (k // 4, i)
    sh.save(f"site/a15s/s{k // 4}.webp", "WEBP", quality=55)
for q in out: q["ap"] = [f"s{_pos[int(x[1:-5])][0]}|{_pos[int(x[1:-5])][1]}" for x in q.get("ap", []) if x.startswith("p")]
json.dump(out, open("site/alh15.json", "w", encoding="utf-8"), ensure_ascii=False)

for q in out:  # his file: 'New Questions' (pages 5-40) then 'Repeated Questions' (42-203)
    q["t"] = "1) الأسئلة الجديدة (صفحة 5–40)" if int(re.search(r"صفحة (\d+)", q["n"]).group(1)) <= 40 else "2) الأسئلة المكررة (صفحة 42–203)"
json.dump(out, open("site/alh15.json", "w", encoding="utf-8"), ensure_ascii=False)
