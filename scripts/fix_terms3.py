# -*- coding: utf-8 -*-
"""Third, comprehensive sweep: disease/condition names in Arabic -> English,
per explicit request (student wants ALL medical terminology in English,
even common disease names like diabetes/depression). Longest-phrase-first
so e.g. "rheumatoid arthritis" is matched before generic "arthritis".
"""
import glob
import re

FILES = sorted(glob.glob("data_batch*.py"))

# Arabic phrase (as it appears WITHOUT a leading "ال") -> English.
# Ordered here by category for readability; sorted by length before use.
GLOSSARY = {
    # Cardiology
    "قصور القلب الاحتقاني": "congestive heart failure",
    "قصور القلب": "heart failure",
    "احتشاء عضلة القلب": "myocardial infarction",
    "الذبحة الصدرية": "angina",
    "ذبحة صدرية": "angina",
    "تصلب الشرايين": "atherosclerosis",
    "الرجفان الأذيني": "atrial fibrillation",
    "رجفان أذيني": "atrial fibrillation",
    "تضيق الصمام الأبهري": "aortic stenosis",
    "تضيق الأبهري": "aortic stenosis",
    "تضيق أبهري": "aortic stenosis",
    "قصور الصمام الأبهري": "aortic regurgitation",
    "قصور الأبهري": "aortic regurgitation",
    "قصور أبهري": "aortic regurgitation",
    "تضيق الصمام التاجي": "mitral stenosis",
    "تضيق تاجي": "mitral stenosis",
    "قصور الصمام التاجي": "mitral regurgitation",
    "قصور تاجي": "mitral regurgitation",
    "التهاب الشغاف الجرثومي": "infective endocarditis",
    "التهاب الشغاف المعدي": "infective endocarditis",
    "التهاب الشغاف": "endocarditis",
    "التهاب التامور": "pericarditis",
    "اعتلال عضلة القلب": "cardiomyopathy",
    "الصمة الرئوية": "pulmonary embolism",
    "تجلط الأوردة العميقة": "deep vein thrombosis",
    "الدوالي": "varicose veins",
    "الصدمة القلبية": "cardiogenic shock",
    "اعتلال الشريان المحيطي": "peripheral arterial disease",

    # Respiratory
    "الربو": "asthma",
    "الانسداد الرئوي المزمن": "COPD",
    "الالتهاب الرئوي": "pneumonia",
    "التهاب رئوي": "pneumonia",
    "استرواح الصدر": "pneumothorax",
    "الانصباب الجنبي": "pleural effusion",
    "انصباب جنبي": "pleural effusion",
    "توقف التنفس أثناء النوم": "sleep apnea",
    "انقطاع التنفس النومي": "sleep apnea",
    "التليف الرئوي": "pulmonary fibrosis",

    # GI
    "القرحة الهضمية": "peptic ulcer",
    "قرحة هضمية": "peptic ulcer",
    "ارتجاع المريء": "GERD",
    "التهاب البنكرياس": "pancreatitis",
    "تليف الكبد": "liver cirrhosis",
    "التهاب الكبد": "hepatitis",
    "حصى المرارة": "gallstones",
    "التهاب الزائدة الدودية": "appendicitis",
    "التهاب الزائدة": "appendicitis",
    "مرض كرون": "Crohn's disease",
    "التهاب القولون التقرحي": "ulcerative colitis",
    "القولون العصبي": "IBS",
    "الداء البطني": "celiac disease",

    # Renal / urology
    "الفشل الكلوي": "renal failure",
    "القصور الكلوي": "renal failure",
    "حصى الكلى": "kidney stones",
    "التهاب كبيبات الكلى": "glomerulonephritis",
    "التهاب المسالك البولية": "UTI",
    "التهاب الحويضة والكلية": "pyelonephritis",

    # Endocrine
    "السكري": "diabetes",
    "فرط نشاط الغدة الدرقية": "hyperthyroidism",
    "فرط الدرقية": "hyperthyroidism",
    "قصور الغدة الدرقية": "hypothyroidism",
    "قصور الدرقية": "hypothyroidism",
    "قصور الغدة الكظرية": "adrenal insufficiency",
    "هشاشة العظام": "osteoporosis",

    # Neuro
    "السكتة الدماغية": "stroke",
    "الصرع": "epilepsy",
    "الشلل الرعاش": "Parkinson's disease",
    "الزهايمر": "Alzheimer's disease",
    "التصلب المتعدد": "multiple sclerosis",
    "الصداع النصفي": "migraine",
    "التهاب السحايا": "meningitis",
    "التهاب الدماغ": "encephalitis",

    # Heme/onc
    "فقر الدم": "anemia",
    "سرطان الدم": "leukemia",
    "نقص الصفائح": "thrombocytopenia",

    # Rheum
    "التهاب المفاصل الروماتويدي": "rheumatoid arthritis",
    "الذئبة الحمامية": "lupus",
    "النقرس": "gout",
    "خشونة المفاصل": "osteoarthritis",

    # Psych
    "الاكتئاب": "depression",
    "القلق": "anxiety",
    "الفصام": "schizophrenia",
    "الوسواس القهري": "OCD",
    "ثنائي القطب": "bipolar disorder",

    # ID
    "حمى الضنك": "dengue fever",
    "السل": "tuberculosis",
}


def make_pattern(phrase):
    return re.compile(
        r'(?<![؀-ۿ])([وفبكل]{0,2})(ال)?'
        + re.escape(phrase) + r'\b'
    )


def make_repl(english):
    def _repl(m):
        prefix = m.group(1) or ""
        article = "الـ" if m.group(2) else ""  # "الـ"
        return f'{prefix}{article}<bdi>{english}</bdi>'
    return _repl


# longest phrase first so multi-word entries win over their sub-phrases
ordered = sorted(GLOSSARY.items(), key=lambda kv: -len(kv[0]))

total_changes = 0
for path in FILES:
    with open(path, encoding="utf-8") as f:
        content = f.read()
    original = content
    for phrase, english in ordered:
        pattern = make_pattern(phrase)
        content = pattern.sub(make_repl(english), content)
    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"{path}: changed")
        total_changes += 1

print("Files changed:", total_changes)
