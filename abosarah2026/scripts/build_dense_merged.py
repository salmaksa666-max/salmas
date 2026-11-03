# -*- coding: utf-8 -*-
"""Merge several dump_mkj.py item sets into one very dense PDF grouped by system -> topic, similar questions side by side.
Each question: number, stem, options inline (answer ticked), Alhomrani / card notes.
usage: build_dense_merged.py OUT.pdf TITLE ITEMS1.json:EXPL1.json[:TAG] ITEMS2.json:EXPL2.json[:TAG] ...
env: FS (font pt, default 6.3), COLS (default 3), MAP=out.json (writes qid -> [system, topic])"""
import glob
import html
import json
import os
import re
import subprocess
import sys
import tempfile

OUT, TITLE = sys.argv[1], sys.argv[2]
CHROME = sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))[-1]
FS = float(os.environ.get("FS", "6.3"))
COLS = int(os.environ.get("COLS", "3"))

# system -> [(topic, regex)] ; order matters (first match wins inside the chosen system)
SYS = [
 ("Cardiology", r"heart|cardi|chest pain|myocard|coronary|angina|\becg\b|murmur|valv|aort|atrial|arrhythm|syncope|hypertens|blood pressure|stemi|troponin|statin|ldl|cholesterol|lipid|endocarditis|pericard|tachycard|bradycard|warfarin.*valve", [
   ("Hypertension", r"hypertens|blood pressure|\bbp\b|amlodipine|lisinopril|ace inhibitor|losartan|thiazide|resistant"),
   ("Lipids", r"ldl|cholesterol|lipid|statin|triglycer|ezetimibe|pcsk9"),
   ("IHD / ACS", r"chest pain|myocard|coronary|angina|stemi|troponin|st elevation|st depression|thromboly|pci\b"),
   ("Arrhythmia", r"atrial|fibrillation|flutter|arrhythm|tachycard|bradycard|block|qt\b|wpw|palpitat|syncope|cardioversion|amiodarone|digoxin"),
   ("Heart failure", r"heart failure|\bhf\b|ejection fraction|edema|furosemide|cardiomyopathy|bnp"),
   ("Valves / endocarditis", r"murmur|valv|stenosis|regurgit|endocarditis|prophylaxis|rheumatic"),
   ("Other cardiology", r".")]),
 ("Pulmonology", r"asthma|copd|lung|pulmonary|pneumon|pleural|dyspnea|shortness of breath|cough|wheez|spirometr|inhaler|sarcoid|bronch|oxygen|intubat|ventilat|ards|tuberc|\btb\b|embolism|\bpe\b|smok", [
   ("Asthma", r"asthma|inhaler|salbutamol|ics\b|wheez"),
   ("COPD", r"copd|emphysema|chronic bronchitis|fev1/fvc"),
   ("Pneumonia / TB", r"pneumon|tuberc|\btb\b|consolidation|ppd|igra|isoniazid|sputum"),
   ("PE / pleural", r"embolism|\bpe\b|pleural|effusion|pneumothorax|d-dimer|ctpa"),
   ("Respiratory failure / ICU", r"intubat|ventilat|ards|abg|respiratory failure|niv|bipap"),
   ("Other pulmonology", r".")]),
 ("GI & Hepatology", r"liver|hepat|cirrho|ascites|jaundice|pancrea|bowel|colitis|crohn|celiac|diarrh|constipat|dysphagia|esophag|gastr|stomach|ulcer|reflux|gerd|dyspepsia|h\.? ?pylori|colon|rectal|melena|hematemesis|varice|bilirubin|gallstone|biliary|abdominal pain", [
   ("Liver", r"liver|hepat|cirrho|ascites|varice|bilirubin|alt\b|ast\b|encephalopathy|hbv|hcv|hbsag|paracetamol"),
   ("Pancreas / biliary", r"pancrea|gallstone|biliary|cholangit|cholecyst|lipase|amylase"),
   ("Upper GI", r"dysphagia|esophag|gastr|stomach|peptic|ulcer|reflux|gerd|dyspepsia|pylori|hematemesis|ppi|omeprazole"),
   ("IBD / celiac / IBS", r"colitis|crohn|celiac|ibs\b|irritable|inflammatory bowel|gluten|ttg"),
   ("Colon / screening", r"colon|colorectal|polyp|rectal|colonoscopy|screening|melena|bleeding per rectum"),
   ("Other GI", r".")]),
 ("Nephrology & Electrolytes", r"kidney|renal|creatinine|nephr|proteinuria|hematuria|dialysis|egfr|\baki\b|\bckd\b|sodium|potassium|hyponat|hypernat|hyperkal|hypokal|calcium|acidosis|alkalosis|urin|stone", [
   ("Potassium / acid-base", r"potassium|hyperkal|hypokal|\bk\b|acidosis|alkalosis|bicarbonate|anion gap|abg"),
   ("Sodium / water", r"sodium|hyponat|hypernat|siadh|\bna\b|insipidus"),
   ("Calcium", r"calcium|hypercalc|hypocalc|parathyroid|pth"),
   ("AKI / CKD", r"aki\b|ckd\b|creatinine|dialysis|egfr|acute kidney|chronic kidney"),
   ("Glomerular / stones / UTI", r"nephrotic|nephritic|proteinuria|hematuria|glomerul|stone|calculi|uti\b|pyelo|urinary"),
   ("Other nephrology", r".")]),
 ("Endocrinology", r"diabet|insulin|glucose|hba1c|metformin|thyroid|tsh|graves|adrenal|cortisol|cushing|addison|pituitar|prolactin|acromegal|osteopor|vitamin d|testosteron|obes|bmi|hypoglyc|dka", [
   ("Diabetes", r"diabet|insulin|glucose|hba1c|metformin|hypoglyc|dka|sglt|glp|sulfonylurea"),
   ("Thyroid", r"thyroid|tsh|graves|t4\b|levothyrox|goiter|nodule|methimazole"),
   ("Adrenal / pituitary", r"adrenal|cortisol|cushing|addison|pituitar|prolactin|acromegal|pheochrom|aldosteron"),
   ("Bone / obesity", r"osteopor|vitamin d|dexa|bisphosph|obes|bmi|weight"),
   ("Other endocrinology", r".")]),
 ("Hematology & Oncology", r"anemia|hemoglobin|\bhb\b|ferritin|iron|b12|folate|platelet|thrombocyt|bleeding|coagul|warfarin|heparin|dvt|thrombo|leukemia|lymphoma|myeloma|sickle|thalass|g6pd|transfusion|cancer|tumou?r|malignan|chemo|neutropeni|polycyth|hemophilia|willebrand|inr", [
   ("Anemia", r"anemia|iron|ferritin|b12|folate|mcv|thalass|sickle|g6pd|hemoly|pernicious"),
   ("Bleeding / clotting / VTE", r"bleeding|coagul|warfarin|heparin|dvt|thrombo|platelet|itp|ttp|hemophilia|willebrand|inr|anticoag|doac|apixaban|rivaroxaban"),
   ("Leukemia / lymphoma / myeloma", r"leukemia|lymphoma|myeloma|polycyth|myeloprolif|lymph node|neutropeni"),
   ("Cancer / screening / TLS", r"cancer|tumou?r|malignan|chemo|tumor lysis|screening|metasta|palliat"),
   ("Other hematology", r".")]),
 ("Neurology", r"stroke|seizure|epilep|headache|migraine|dementia|alzheimer|parkinson|tremor|multiple sclerosis|myasthenia|guillain|neuropath|weakness|numbness|vertigo|meningitis|encephal|bell|cranial|consciousness|gcs|spinal|nerve", [
   ("Stroke / TIA", r"stroke|tia\b|hemipar|thrombolys|tpa|carotid|infarct|hemorrhage"),
   ("Seizures", r"seizure|epilep|convuls|status|valpro|levetir|phenytoin"),
   ("Headache", r"headache|migraine|cluster|tension"),
   ("Dementia / movement", r"dementia|alzheimer|parkinson|tremor|lewy|huntington|confusion|delirium"),
   ("Neuromuscular / MS", r"multiple sclerosis|myasthenia|guillain|neuropath|als\b|motor neuron|weakness|bell|optic neuritis"),
   ("Other neurology", r".")]),
 ("Infectious disease", r"fever|infection|antibiotic|hiv|hepatitis b vaccine|malaria|brucell|sepsis|meningit|syphilis|herpes|zoster|influenza|vaccin|cellulitis|abscess|osteomyel|travel|typhoid|dengue|covid|fungal|candid", [
   ("Vaccines / travel / exposure", r"vaccin|travel|hajj|prophylaxis|exposure|rabies|tetanus|needle"),
   ("HIV / STI", r"hiv|syphilis|gonorr|chlamydia|herpes|sexual"),
   ("Fever / sepsis / zoonoses", r"fever|sepsis|brucell|malaria|typhoid|dengue|q fever"),
   ("Skin / bone / soft tissue", r"cellulitis|abscess|osteomyel|zoster|wound|diabetic foot"),
   ("Other infections", r".")]),
 ("Rheumatology", r"arthritis|joint|gout|lupus|\bsle\b|vasculit|spondyl|scleroderma|myositis|polymyalgia|sjogren|raynaud|behcet|fibromyalg|back pain|osteoarth|knee|shoulder|hip", [
   ("Gout / crystal / septic", r"gout|uric|pseudogout|crystal|septic|aspirat|monoarthritis"),
   ("RA / SLE / connective tissue", r"rheumatoid|lupus|\bsle\b|scleroderma|sjogren|myositis|raynaud|methotrexate|anti-?ccp|ana\b"),
   ("Spondyloarthritis / back", r"spondyl|back pain|sacroil|reactive|psoria|ankylos"),
   ("Vasculitis / PMR", r"vasculit|giant cell|temporal|polymyalgia|behcet|kawasaki|wegener|granulomatosis"),
   ("OA / soft tissue", r"osteoarth|knee|shoulder|hip|fibromyalg|tendon|carpal"),
   ("Other rheumatology", r".")]),
]
SYSORDER = ["Hematology & Oncology", "Neurology", "Cardiology", "Pulmonology", "GI & Hepatology", "Infectious disease",
            "Rheumatology", "Endocrinology", "Nephrology & Electrolytes"]
_by = {s: tps for s, _, tps in SYS}
ALL_TOPICS = [(s, t) for s in SYSORDER for t, _ in _by[s]] + [("Other", "Other")]
BOXES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "review", "merged_topic_boxes.json"), encoding="utf-8"))
AR = re.compile(r"[\u0600-\u06ff]")
LAT = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’\-/.+%±:&]*(?: (?:[A-Za-z0-9±][A-Za-z0-9'’\-/.+%±:&]*|\+|/|=|–))*")


def bidi(t):
    out, last = "", 0
    for m in LAT.finditer(t):
        out += html.escape(t[last:m.start()], quote=False) + f'<bdi dir="ltr">{html.escape(m.group(0), quote=False)}</bdi>'
        last = m.end()
    return out + html.escape(t[last:], quote=False)


HIST = re.compile(r"(known (case )?(of|with)|k/c|history of|hx of|with|has|on)\s+(type ?[12] )?(hypertension|htn|diabetes( mellitus)?|dm|dyslipidemia|hyperlipidemia|smok\w*)(\s*(and|,|&)\s*(type ?[12] )?(hypertension|htn|diabetes( mellitus)?|dm|dyslipidemia|hyperlipidemia))*", re.I)


def classify(stem, opts, ans):
    stem_l = HIST.sub(" ", stem.lower())
    sents = re.split(r"(?<=[.?!])\s+", stem_l)
    lead = sents[-1] if sents else ""
    parts = ((ans.lower(), 3.0), (lead, 2.0), (" ".join(opts).lower(), 1.2), (stem_l, 1.0))
    best = None
    for s, rx, tps in SYS:
        sc = sum(w * len(re.findall(rx, t)) for t, w in parts)
        if sc and (best is None or sc > best[0]):
            best = (sc, s, tps)
    if not best:
        return "Other", "Other"
    tbest = None
    for i, (tname, trx) in enumerate(best[2][:-1]):
        sc = sum(w * len(re.findall(trx, t)) for t, w in parts)
        if sc and (tbest is None or sc > tbest[0]):
            tbest = (sc, tname)
    return best[1], (tbest[1] if tbest else best[2][-1][0])


SKIP = re.compile(r"^(Other versions? of this recall|↻|Same question as|The same question reappears|Same-version)", re.I)
items = []
for spec in sys.argv[3:]:
    parts = spec.split(":")
    its, ex = json.load(open(parts[0], encoding="utf-8")), json.load(open(parts[1], encoding="utf-8"))
    tag = parts[2] if len(parts) > 2 else ""
    for it in its:
        s, tp = classify(it["stem"], [o for _, o in it["opts"]], it["ans"])
        note = ex.get(it["qid"], {}).get("author", "")
        note = " ".join(x for x in re.split(r"(?<=[.)])\s+(?=[A-Z↑↻O])", note) if not SKIP.match(x))
        items.append(dict(it, sys=s, topic=tp, note=note, tag=tag))

order = {k: i for i, k in enumerate(ALL_TOPICS)}
import numpy as np
from collections import Counter, defaultdict
TOK = re.compile(r"[a-z][a-z0-9\-]{2,}")
STOP = set("the and with for was has his her are this that which following most appropriate next step what patient presents presented year old years woman man male female history examination management diagnosis likely best initial".split())
docs = [[w for w in TOK.findall((it["ans"] + " ") * 3 + it["stem"].lower() + " " + " ".join(o for _, o in it["opts"]).lower()) if w not in STOP] for it in items]
df = Counter(w for d in docs for w in set(d))
N = len(docs)
vecs = []
vocab = {w: i for i, w in enumerate(df)}
for d in docs:
    c = Counter(d)
    v = {vocab[w]: (1 + np.log(n)) * np.log(N / df[w]) for w, n in c.items()}
    nrm = np.sqrt(sum(x * x for x in v.values())) or 1
    vecs.append({k: x / nrm for k, x in v.items()})
cos = lambda a, b: sum(x * b.get(k, 0) for k, x in a.items()) if len(a) < len(b) else sum(x * a.get(k, 0) for k, x in b.items())
groups = defaultdict(list)
for i, it in enumerate(items):
    groups[(it["sys"], it["topic"])].append(i)
ordered = []
for g in sorted(groups, key=lambda k: order.get(k, 999)):
    rest = groups[g][:]
    cur = rest.pop(0)
    chain = [cur]
    while rest:  # greedy nearest neighbour -> similar questions side by side
        j = max(range(len(rest)), key=lambda r: cos(vecs[cur], vecs[rest[r]]))
        cur = rest.pop(j)
        chain.append(cur)
    ordered += chain
# October questions that match a September one (same recall): badge, and flag when the answer differs
V = len(vocab)
Mx = np.zeros((N, V), dtype=np.float32)
for i, v in enumerate(vecs):
    for k, x in v.items():
        Mx[i, k] = x
tags_ = np.array([it["tag"] for it in items])
sep_i, oct_i = np.where(tags_ == "Sep")[0], np.where(tags_ == "Oct")[0]
if len(sep_i) and len(oct_i):
    sim = Mx[oct_i] @ Mx[sep_i].T
    na = lambda t: re.sub(r"[^a-z0-9]", "", re.sub(r"^[a-e][.)\-]\s*", "", t.lower()))[:14]
    for r, i in enumerate(oct_i):
        j = int(sim[r].argmax())
        if sim[r, j] >= 0.75:
            items[i]["same"] = "same" if na(items[i]["ans"]) == na(items[sep_i[j]]["ans"]) else "diff"
items = [items[i] for i in ordered]
if os.environ.get("MAP"):
    json.dump({it["qid"]: [it["sys"], it["topic"]] for it in items}, open(os.environ["MAP"], "w"), ensure_ascii=False)

e = lambda t: html.escape(t, quote=False)
body, cur_s, cur_t, n = "", None, None, 0
for it in items:
    if it["sys"] != cur_s:
        body += f'<div class="sh">{e(it["sys"])}</div>'
        cur_s, cur_t = it["sys"], None
    if it["topic"] != cur_t:
        body += f'<div class="th">{e(it["topic"])}</div>'
        if BOXES.get(it["topic"]):
            body += '<div class="bx">' + "".join(f"<div>• {bidi(x.replace('→', '←'))}</div>" for x in BOXES[it["topic"]]) + "</div>"
        cur_t = it["topic"]
    n += 1
    ans = it["ans"].strip()
    o = ""
    hit = False
    for k, t in it["opts"]:
        ok = bool(re.match(rf"{k}[.)\-]", ans))
        hit = hit or ok
        o += f' <span class="{"ok" if ok else "op"}">{"✔" if ok else ""}{k}. {e(t)}</span>'
    if not hit:
        o += f' <span class="ok">✔ {e(ans)}</span>'
    rp = f'<span class="rp">مكرر {e(it["rep"])}</span> ' if it.get("rep") else ""
    tg = f'<span class="tg">{e(it["tag"])}</span>' if it["tag"] else ""
    if it.get("same") == "same":
        tg += '<span class="sm">= Sep</span>'
    elif it.get("same") == "diff":
        tg += '<span class="sm df">≈ Sep: جواب مختلف ⚠</span>'
    nt = f'<div class="nt">✍ {e(it["note"])}</div>' if it["note"] else ""
    body += f'<div class="q"><b>{n}.</b>{tg} {rp}{e(it["stem"])}{it["flag"]}{o}{nt}</div>'

CSS = f"""
@page {{ size: A4; margin: 4mm 4mm 5mm; }}
* {{ box-sizing: border-box; }}
body {{ font-family: "DejaVu Sans", Arial, sans-serif; font-size: {FS}pt; line-height: 1.13; margin: 0; color: #000; }}
.top {{ display: flex; justify-content: space-between; font-weight: bold; font-size: 9pt; border-bottom: 1.2pt solid #000; margin-bottom: .8mm; }}
.cols {{ column-count: {COLS}; column-gap: 2.6mm; column-rule: .3pt solid #888; }}
.sh {{ background: #000; color: #fff; font-weight: bold; font-size: 1.25em; padding: .3mm 1.2mm; margin: .8mm 0 .3mm; break-after: avoid; }}
.th {{ border-bottom: .8pt solid #000; font-weight: bold; margin: .6mm 0 .2mm; break-after: avoid; }}
.q {{ border-bottom: .25pt solid #999; padding: .25mm 0 .35mm; break-inside: avoid; }}
.op {{ color: #222; }}
.ok {{ font-weight: bold; text-decoration: underline; }}
.rp {{ border: .6pt solid #000; border-radius: .8mm; padding: 0 .6mm; font-weight: bold; direction: rtl; unicode-bidi: isolate; }}
.tg {{ font-size: .85em; border: .4pt solid #000; padding: 0 .4mm; margin-left: .6mm; }}
.bx {{ direction: rtl; text-align: right; border: .9pt solid #000; border-radius: 1mm; padding: .4mm 1mm; margin: .3mm 0 .6mm; font-size: 1.02em; line-height: 1.22; break-inside: avoid; background: #f2f2f2; }}
.bx div {{ margin: .15mm 0; }}
.sm {{ font-size: .82em; border: .4pt dashed #000; padding: 0 .4mm; margin-left: .5mm; }}
.sm.df {{ font-weight: bold; border-style: solid; }}
.nt {{ font-size: .92em; font-style: italic; color: #111; border-left: .9pt solid #000; padding-left: .8mm; margin-top: .15mm; }}
"""
doc = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
       f'<div class="top"><span>{e(TITLE)}</span><span>{n} سؤال</span></div><div class="cols">{body}</div></body></html>')
src = os.path.join(tempfile.mkdtemp(), "d.html")
open(src, "w", encoding="utf-8").write(doc)
subprocess.run([CHROME, "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={OUT}", "file://" + src], check=True, capture_output=True)
print(n, "questions ->", OUT)
