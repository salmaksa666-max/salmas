# -*- coding: utf-8 -*-
"""Inline helpers for printed questions/maps: normal ranges after lab values and a short class after drug names.
annotate_html() only touches text outside tags; it never changes the original wording, it only appends (…)."""
import re

# name pattern -> (range, unit-picker)  unit-picker gets the number and returns the range string
def _by(cut, lo, hi):
    return lambda v: lo if v < cut else hi


LABS = [
    (r"urine (?:Na|sodium)", lambda v: "prerenal <20 · ATN >40"),
    (r"CSF glucose", lambda v: "N ~2/3 of serum"),
    (r"Hb|Hgb|ha?emoglobin", _by(25, "N 12–16 g/dL", "N 120–160 g/L")),
    (r"WBCs?|white cells?", _by(100, "N 4–11 ×10⁹/L", "N 4000–11000")),
    (r"platelets?|PLTs?", _by(1000, "N 150–400 ×10⁹/L", "N 150,000–400,000")),
    (r"INR", lambda v: "N 0.8–1.2 · warfarin target 2–3"),
    (r"aPTT|PTT", lambda v: "N 25–35 s"),
    (r"PT", lambda v: "N 11–13.5 s"),
    (r"Na|sodium", lambda v: "N 135–145"),
    (r"K|potassium", lambda v: "N 3.5–5.0"),
    (r"Cl|chloride", lambda v: "N 98–106"),
    (r"HCO3|bicarbonate|bicarb", lambda v: "N 22–28"),
    (r"creatinine|Cr", _by(20, "N 0.6–1.2 mg/dL", "N 60–110 µmol/L")),
    (r"urea|BUN", _by(25, "N 2.5–7.5 mmol/L", "BUN N 7–20 mg/dL")),
    (r"glucose|FBS|RBS", _by(30, "N fasting 4–5.6 mmol/L", "N fasting 70–100 mg/dL")),
    (r"HbA1c|A1c", lambda v: "N <5.7% · DM ≥6.5%"),
    (r"ALT|AST", lambda v: "N <40"),
    (r"ALP|alkaline phosphatase", lambda v: "N 40–130"),
    (r"bilirubin", _by(5, "N <1.2 mg/dL", "N <21 µmol/L")),
    (r"albumin", _by(10, "N 3.5–5 g/dL", "N 35–50 g/L")),
    (r"calcium|Ca", _by(5, "N 2.2–2.6 mmol/L", "N 8.5–10.5 mg/dL")),
    (r"Mg|magnesium", lambda v: "N 0.7–1.0 mmol/L"),
    (r"phosphate", lambda v: "N 0.8–1.5 mmol/L"),
    (r"TSH", lambda v: "N 0.4–4"),
    (r"free T4|FT4|T4", lambda v: "N 10–22 pmol/L"),
    (r"ESR", lambda v: "N <20"),
    (r"CRP", lambda v: "N <5–10"),
    (r"pH", lambda v: "N 7.35–7.45"),
    (r"PaCO2|pCO2|PCO2|CO2", lambda v: "N 35–45"),
    (r"PaO2|pO2|PO2", lambda v: "N 80–100"),
    (r"lactate", lambda v: "N <2"),
    (r"lipase|amylase", lambda v: "dx if >3× upper limit"),
    (r"ferritin", lambda v: "N 30–300"),
    (r"MCV", lambda v: "N 80–100"),
    (r"RDW", lambda v: "N 11.5–14.5%"),
    (r"retics?|reticulocytes?(?: count)?", lambda v: "N 0.5–2.5%"),
    (r"serum osm\w*|osmolality|osm", lambda v: "N 275–295"),
    (r"urine osm\w*", lambda v: "dilute <100 · concentrated >300"),
    (r"uric acid", _by(20, "N 3.5–7 mg/dL", "N 200–420 µmol/L")),
    (r"LDH", lambda v: "N 140–280"),
    (r"CK|CPK", lambda v: "N <200"),
    (r"troponin", lambda v: "N below the lab cut-off"),
    (r"PSA", lambda v: "N <4"),
    (r"(?:e)?GFR", lambda v: "N >90 · CKD4 15–29"),
    (r"SpO2|O2 sat\w*|oxygen sat\w*|saturation|sat|O2|oxygen", lambda v: "N 95–100%"),
    (r"RR|resp\w* rate", lambda v: "N 12–20"),
    (r"HR|pulse|heart rate", lambda v: "N 60–100"),
    (r"CVP", lambda v: "N 2–8 cmH2O"),
    (r"ASO", lambda v: "N <200"),
]
LAB_RE = re.compile(
    r"\b(" + "|".join(f"(?:{p})" for p, _ in LABS) + r")\b(\s*(?:level|count|of|is|was|:|=)?\s*[<>≥≤~]?\s*)(\d+(?:[.,]\d+)?)(?![\d.,])(\s*(?:%|mmol/L|µmol/L|umol/L|mg/dL|g/dL|g/L|mEq/L|x\s*10\^?9/L|×10⁹/L|/µL|sec|s\b)?)",
    re.I)
LAB_FN = [(re.compile(rf"^(?:{p})$", re.I), fn) for p, fn in LABS]

DRUGS = {
    # cardio
    "sacubitril": "ARNI", "sacubatril": "ARNI", "valsartan": "ARB", "losartan": "ARB", "candesartan": "ARB",
    "lisinopril": "ACE inhibitor", "enalapril": "ACE inhibitor", "ramipril": "ACE inhibitor", "captopril": "ACE inhibitor",
    "spironolactone": "K-sparing diuretic", "spirono": "K-sparing diuretic", "eplerenone": "K-sparing diuretic",
    "furosemide": "loop diuretic", "lasix": "loop diuretic", "hydrochlorothiazide": "thiazide", "indapamide": "thiazide-like",
    "metoprolol": "beta blocker", "bisoprolol": "beta blocker", "carvedilol": "beta blocker", "atenolol": "beta blocker",
    "propranolol": "beta blocker", "labetalol": "beta blocker", "esmolol": "beta blocker",
    "amlodipine": "CCB", "nifedipine": "CCB", "diltiazem": "CCB", "verapamil": "CCB",
    "digoxin": "rate control, inotrope", "amiodarone": "antiarrhythmic", "clonidine": "central antihypertensive", "adenosine": "for SVT",
    "warfarin": "anticoagulant", "heparin": "anticoagulant", "enoxaparin": "LMWH", "apixaban": "DOAC", "rivaroxaban": "DOAC",
    "dabigatran": "DOAC", "aspirin": "antiplatelet", "clopidogrel": "antiplatelet", "ticagrelor": "antiplatelet",
    "atorvastatin": "statin", "atrovstatin": "statin", "rosuvastatin": "statin", "simvastatin": "statin",
    "dobutamine": "inotrope", "norepinephrine": "vasopressor", "noradrenaline": "vasopressor", "vasopressin": "vasopressor",
    "dopamine": "vasopressor", "epinephrine": "adrenaline", "hydralazine": "vasodilator", "nitroglycerin": "nitrate",
    "alteplase": "thrombolytic", "tenecteplase": "thrombolytic", "streptokinase": "thrombolytic",
    "protamine": "reverses heparin", "idarucizumab": "reverses dabigatran",
    # diabetes / endo
    "metformin": "biguanide", "dapagliflozin": "SGLT2 inhibitor", "empagliflozin": "SGLT2 inhibitor",
    "liraglutide": "GLP-1 agonist", "semaglutide": "GLP-1 agonist", "sitagliptin": "DPP-4 inhibitor",
    "gliclazide": "sulfonylurea", "glibenclamide": "sulfonylurea", "pioglitazone": "TZD",
    "levothyroxine": "thyroid hormone", "carbimazole": "antithyroid", "methimazole": "antithyroid",
    "propylthiouracil": "antithyroid", "PTU": "antithyroid", "hydrocortisone": "steroid", "fludrocortisone": "mineralocorticoid",
    "dexamethasone": "steroid", "prednisolone": "steroid", "prednisone": "steroid", "methylprednisolone": "steroid",
    "budesonide": "steroid", "cabergoline": "dopamine agonist", "bromocriptine": "dopamine agonist",
    "octreotide": "somatostatin analogue", "desmopressin": "ADH analogue", "tolvaptan": "ADH blocker",
    # GI
    "omeprazole": "PPI", "pantoprazole": "PPI", "esomeprazole": "PPI", "ranitidine": "H2 blocker",
    "ondansetron": "antiemetic", "metoclopramide": "antiemetic", "loperamide": "antidiarrheal", "bismuth": "salicylate",
    "lactulose": "laxative", "rifaximin": "gut antibiotic", "mesalamine": "5-ASA", "mesalazine": "5-ASA",
    "sulfasalazine": "5-ASA", "infliximab": "anti-TNF", "adalimumab": "anti-TNF", "azathioprine": "immunosuppressant",
    "ursodeoxycholic": "bile acid", "terlipressin": "for varices",
    # anti-infective
    "ceftriaxone": "3rd-gen cephalosporin", "cefuroxime": "2nd-gen cephalosporin", "cefazolin": "1st-gen cephalosporin",
    "cephalexin": "1st-gen cephalosporin", "cefixime": "3rd-gen cephalosporin", "ceftazidime": "anti-pseudomonal",
    "azithromycin": "macrolide", "clarithromycin": "macrolide", "erythromycin": "macrolide",
    "amoxicillin": "penicillin", "ampicillin": "penicillin", "penicillin": "antibiotic", "augmentin": "amox-clav",
    "piperacillin": "anti-pseudomonal", "tazobactam": "beta-lactamase inhibitor", "meropenem": "carbapenem",
    "vancomycin": "for MRSA", "linezolid": "for MRSA", "clindamycin": "anaerobes + gram+", "metronidazole": "anaerobes",
    "doxycycline": "tetracycline", "ciprofloxacin": "quinolone", "levofloxacin": "quinolone", "moxifloxacin": "quinolone",
    "gentamicin": "aminoglycoside", "amikacin": "aminoglycoside", "streptomycin": "aminoglycoside",
    "nitrofurantoin": "UTI antibiotic", "trimethoprim": "antibiotic", "TMP-SMX": "antibiotic", "co-trimoxazole": "antibiotic",
    "rifampicin": "anti-TB", "rifampin": "anti-TB", "isoniazid": "anti-TB", "INH": "anti-TB", "pyrazinamide": "anti-TB",
    "ethambutol": "anti-TB", "acyclovir": "antiviral (HSV/VZV)", "valacyclovir": "antiviral", "oseltamivir": "anti-flu",
    "fluconazole": "antifungal", "amphotericin": "antifungal", "albendazole": "antiparasitic", "mebendazole": "antiparasitic",
    "primaquine": "antimalarial", "chloroquine": "antimalarial", "artemether": "antimalarial",
    # neuro / psych
    "risperidone": "antipsychotic", "olanzapine": "antipsychotic", "quetiapine": "antipsychotic", "haloperidol": "antipsychotic",
    "clozapine": "antipsychotic", "aripiprazole": "antipsychotic", "lithium": "mood stabilizer", "valproate": "antiepileptic",
    "valproic": "antiepileptic", "carbamazepine": "antiepileptic", "lamotrigine": "antiepileptic", "levetiracetam": "antiepileptic",
    "phenytoin": "antiepileptic", "ethosuximide": "for absence", "fluoxetine": "SSRI", "sertraline": "SSRI",
    "escitalopram": "SSRI", "citalopram": "SSRI", "paroxetine": "SSRI", "venlafaxine": "SNRI", "amitriptyline": "TCA",
    "bupropion": "antidepressant, smoking", "varenicline": "smoking cessation", "methylphenidate": "stimulant, ADHD",
    "lorazepam": "benzodiazepine", "diazepam": "benzodiazepine", "midazolam": "benzodiazepine", "chlordiazepoxide": "benzodiazepine",
    "thiamine": "vitamin B1", "naloxone": "opioid antidote", "flumazenil": "benzo antidote", "donepezil": "for Alzheimer",
    "levodopa": "for Parkinson", "sumatriptan": "for migraine", "mannitol": "lowers ICP", "nimodipine": "for SAH",
    "neostigmine": "anticholinesterase", "pyridostigmine": "anticholinesterase", "baclofen": "muscle relaxant",
    # rheum / heme / misc
    "allopurinol": "lowers uric acid", "febuxostat": "lowers uric acid", "colchicine": "for gout", "rasburicase": "lowers uric acid",
    "methotrexate": "DMARD", "MTX": "DMARD", "hydroxychloroquine": "DMARD", "hydroxyurea": "raises HbF",
    "ibuprofen": "NSAID", "naproxen": "NSAID", "diclofenac": "NSAID", "indomethacin": "NSAID", "ketorolac": "NSAID",
    "paracetamol": "analgesic", "acetaminophen": "analgesic", "morphine": "opioid", "tramadol": "opioid", "fentanyl": "opioid",
    "IVIG": "immunoglobulin", "PCC": "clotting factors", "deferoxamine": "iron chelator", "desferrioxamine": "iron chelator",
    "N-acetylcysteine": "paracetamol antidote", "tamsulosin": "alpha blocker", "finasteride": "5-ARI",
    "oxybutynin": "anticholinergic", "salbutamol": "SABA", "albuterol": "SABA", "ipratropium": "SAMA",
    "tiotropium": "LAMA", "salmeterol": "LABA", "formoterol": "LABA", "fluticasone": "inhaled steroid",
    "montelukast": "leukotriene blocker", "magnesium sulfate": "MgSO4", "oxytocin": "uterotonic",
    "misoprostol": "prostaglandin", "methylergonovine": "uterotonic", "carboprost": "uterotonic",
    "tranexamic": "antifibrinolytic", "nifedipine ": "tocolytic", "clomiphene": "ovulation inducer", "letrozole": "aromatase inhibitor",
    "tamoxifen": "SERM", "isotretinoin": "retinoid", "permethrin": "scabicide", "ivermectin": "antiparasitic",
    # added from the GB / Confirmed text
    "insulin": "hormone, lowers sugar", "lidocaine": "local anesthetic", "bupivacaine": "local anesthetic",
    "levobupivacaine": "local anesthetic", "ropivacaine": "local anesthetic", "mycophenolate": "immunosuppressant",
    "cyclophosphamide": "chemo / immunosuppressant", "rituximab": "anti-CD20", "eculizumab": "complement blocker",
    "cyclosporine": "immunosuppressant", "tacrolimus": "immunosuppressant", "etanercept": "anti-TNF",
    "tocilizumab": "anti-IL-6", "phentolamine": "alpha blocker", "methacholine": "bronchial challenge test",
    "beclometasone": "inhaled steroid", "beclomethasone": "inhaled steroid", "betamethasone": "steroid",
    "pyridoxine": "vitamin B6", "aminophylline": "bronchodilator", "theophylline": "bronchodilator",
    "ventolin": "salbutamol", "irbesartan": "ARB", "perindopril": "ACE inhibitor", "acetylcysteine": "paracetamol antidote",
    "voriconazole": "antifungal", "methergine": "uterotonic", "ergometrine": "uterotonic", "syntometrine": "uterotonic",
    "sorafenib": "targeted chemo", "isosorbide": "nitrate", "loratadine": "antihistamine", "promethazine": "antihistamine",
    "pethidine": "opioid", "ritodrine": "tocolytic", "terbutaline": "beta-2 agonist", "atosiban": "tocolytic",
    "indometacin": "NSAID", "flucloxacillin": "anti-staph penicillin", "dicloxacillin": "anti-staph penicillin",
    "nortriptyline": "TCA", "apoxaban": "DOAC", "tafenoquine": "antimalarial", "quinacrine": "antiparasitic",
    "gentamycin": "aminoglycoside", "valaciclovir": "antiviral", "tigecycline": "antibiotic", "tetracycline": "antibiotic",
    "mifepristone": "anti-progesterone", "medroxyprogesterone": "progestin", "diazoxide": "raises sugar",
    "nitroprusside": "IV vasodilator", "methyldopa": "antihypertensive in pregnancy", "cryoprecipitate": "fibrinogen",
    "calcium gluconate": "IV calcium", "vilanterol": "LABA", "glucagon": "raises sugar", "dinoprostone": "prostaglandin",
    "anti-D": "Rh immunoglobulin", "folic acid": "vitamin B9", "ferrous sulfate": "oral iron",
}
DRUG_RE = re.compile(r"\b(" + "|".join(sorted((re.escape(k.strip()) for k in DRUGS), key=len, reverse=True)) + r")\b(?!\s*\()", re.I)
DRUG_LOOK = {k.strip().lower(): v for k, v in DRUGS.items()}


def _lab(m):
    if re.match(r"\s*(?:[^\s\[(;]{1,12}\s*)?[\[(]", m.string[m.end():m.end() + 25]):
        return m.group(0)  # the source already gives a range / comment
    if m.string[m.end():m.end() + 1].isalpha():
        return m.group(0)  # e.g. "oxygen 15L", "Hb 9x"
    name, num = m.group(1), m.group(3).replace(",", ".")
    try:
        v = float(num)
    except ValueError:
        return m.group(0)
    for rx, fn in LAB_FN:
        if rx.match(name.strip()):
            return f'{m.group(0)} <span class="ref">({fn(v)})</span>'
    return m.group(0)


def _drug(m):
    cls = DRUG_LOOK[m.group(1).lower()]
    if cls.lower() in m.string.lower():
        return m.group(0)  # the text already says what it is
    return f'{m.group(0)} <span class="ref">({DRUG_LOOK[m.group(1).lower()]})</span>'


def annotate_text(t, labs=True, drugs=True):
    if labs:
        t = LAB_RE.sub(_lab, t)
    if drugs:
        seen = set()

        def once(m):
            k = m.group(1).lower()
            if k in seen:
                return m.group(0)
            seen.add(k)
            return _drug(m)
        t = DRUG_RE.sub(once, t)
    return t


def annotate_html(h, labs=True, drugs=True):
    """apply annotate_text to the text between tags (inside one HTML fragment)"""
    parts = re.split(r"(<[^>]+>)", h)
    seen = set()
    out = []
    for p in parts:
        if p.startswith("<"):
            out.append(p)
            continue
        if labs:
            p = LAB_RE.sub(_lab, p)
        if drugs:
            def once(m):
                k = m.group(1).lower()
                if k in seen:
                    return m.group(0)
                seen.add(k)
                return _drug(m)
            p = DRUG_RE.sub(once, p)
        out.append(p)
    return "".join(out)
