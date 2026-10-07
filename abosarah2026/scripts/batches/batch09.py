# -*- coding: utf-8 -*-
# Batch 09 — AS-1308 .. AS-1897 (Medicine), 145 questions.

EXPLANATIONS = {
"AS-1308": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "هذا <bdi>screening</bdi> روتيني لقى عنده كوم من <bdi>modifiable cardiovascular risk factors</bdi> (<bdi>glucose</bdi>، <bdi>blood pressure</bdi>، <bdi>obesity</bdi>، <bdi>smoking</bdi>)، والسؤال يبي الخطوة الأولى الصح، مو علاج واحد بس.",
    "clues": [
        ("abnormal fasting glucose", "<bdi>impaired fasting glucose</bdi> — عامل خطر قابل للتعديل"),
        ("high blood preesure readings", "<bdi>BP</bdi> مرتفع بس لسا ما تأكد بقراءات متكررة"),
        ("BMI is 31", "<bdi>obesity</bdi>"),
        ("significant smoking", "أهم عامل خطر <bdi>cardiovascular</bdi> قابل للتعديل"),
    ],
    "why_correct": [
        "عنده مجموعة <bdi>modifiable risk factors</bdi> مع بعض: <bdi>impaired fasting glucose</bdi>، <bdi>high BP</bdi> (غير مؤكد لسا)، <bdi>BMI 31</bdi>، <bdi>smoking</bdi>، أكل سريع وقلة حركة، مع <bdi>cholesterol</bdi> مرتفع.",
        "السؤال يسأل عن الخطوة <bdi>initial</bdi>، وهي تغيير نمط الحياة الشامل: ترك <bdi>smoking</bdi>، <bdi>exercise</bdi>، <bdi>diet</bdi> وتخفيف الوزن، مع <bdi>follow up</bdi> لإعادة قياس <bdi>BP</bdi> و<bdi>glucose</bdi> و<bdi>lipids</bdi> قبل أي قرار دوائي.",
        "الخيار B (مراجعة الملف... لا، هذا السؤال مختلف) — الخيار A (تخفيف الوزن فقط) كشف جزء من المشكلة بس ما يغطي كل العوامل.",
    ],
    "when_changes": [
        "لو تأكد <bdi>BP</bdi> بقراءات متكررة وطلع <bdi>stage 2 HTN</bdi> أو عنده <bdi>target organ damage</bdi>، يصير الجواب البدء بدواء مباشرة مع تغيير نمط الحياة.",
        "لو <bdi>LDL</bdi> كان 4.9 <bdi>mmol/L</bdi> أو أعلى (190 <bdi>mg/dL</bdi>)، يصير <bdi>statin</bdi> لازم بغض النظر عن باقي الخطر.",
    ],
    "rule": "«<bdi>initial step</bdi>» مع عدة عوامل خطر = الجواب اللي يجمع كل تغييرات نمط الحياة سوا، مو عامل واحد لحاله.",
    "comparison": None,
    "labs": [
        ["LDL", "4.03 mmol/L", "أقل من 4.9 mmol/L (190 mg/dL) حد الـ statin الإلزامي"],
        ["Total cholesterol", "7.04 mmol/L", "أقل من 5.2 mmol/L (200 mg/dL) مرغوب"],
        ["BMI", "31", "18.5-24.9 طبيعي، 30 فأعلى obese"],
    ],
    "guideline_note": None,
},
"AS-1314": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "<bdi>hypertensive smoker</bdi> كبير بالعمر عنده <bdi>exertional dyspnea</bdi> و<bdi>basal crackles</bdi>، والسؤال يبي التحليل الأكثر فايدة لتشخيص <bdi>ventricular dysfunction</bdi>.",
    "clues": [
        ("dyspnoea on exertion", "عرض <bdi>heart failure</bdi> الكلاسيكي"),
        ("long standing hypertension", "عامل خطر لـ<bdi>LV dysfunction</bdi>"),
        ("rare crackles at the bases of the lungs", "احتقان رئوي خفيف"),
    ],
    "why_correct": [
        "المريض <bdi>hypertensive smoker</bdi> من فترة طويلة، عنده <bdi>exertional dyspnea</bdi> و<bdi>basal crackles</bdi>، فالشك قوي بـ<bdi>left ventricular dysfunction</bdi> (<bdi>heart failure</bdi>).",
        "<bdi>BNP</bdi> (أو <bdi>NT-proBNP</bdi>) يطلع من عضلة البطين وهو ممطوط، فهو أكثر تحليل دم يساعد يكشف <bdi>ventricular dysfunction</bdi>؛ وإذا كان طبيعي فده يبعد <bdi>heart failure</bdi>.",
        "نفس الفكرة تنطبق على مريض <bdi>COPD</bdi> بعرض <bdi>SOB</bdi> و<bdi>crackles</bdi> و<bdi>leg edema</bdi> — يطلب <bdi>pro-BNP</bdi>.",
    ],
    "when_changes": [
        "لو السؤال يبي تحليل لتشخيص <bdi>acute coronary syndrome</bdi> (ألم صدر، تغيرات <bdi>ischemic ECG</bdi>)، الجواب يصير <bdi>troponin</bdi>.",
        "لو السؤال يبي علامة <bdi>inflammation</bdi> عامة، الجواب يصير <bdi>CRP</bdi>.",
    ],
    "rule": "<bdi>dyspnea</bdi> + <bdi>crackles</bdi> + «كشف <bdi>LV dysfunction</bdi>» = <bdi>BNP</bdi>؛ أما ألم الصدر الإقفاري فجوابه <bdi>troponin</bdi>.",
    "comparison": {
        "headers": ["التحليل", "يكشف"],
        "rows": [
            ["BNP / NT-proBNP", "Ventricular dysfunction / heart failure"],
            ["Troponin T", "Myocardial necrosis / ACS"],
            ["CK (CK-MB)", "Myocardial injury / infarction"],
            ["CRP", "Non-specific inflammation"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},
}

WHY_WRONG = {
"AS-1308": {
    "A": "<bdi>weight loss</bdi> جزء من الخطة بس عنصر واحد بس، يتجاهل <bdi>smoking</bdi> اللي من أهم عوامل الخطر <bdi>cardiovascular</bdi> عنده.",
    "B": "الدواء يجي لاحقًا: <bdi>BP</bdi> ما تأكد بقراءات متكررة، و<bdi>LDL</bdi> 4.03 <bdi>mmol/L</bdi> أقل من حد الـ<bdi>statin</bdi> الإلزامي (4.9 <bdi>mmol/L</bdi>) بدون <bdi>diabetes</bdi> أو <bdi>established cardiovascular disease</bdi>.",
    "D": "الطمأنة خطأ لأن عنده عدة عوامل خطر <bdi>cardiovascular</bdi> و<bdi>prediabetes</bdi> تحتاج تدخل فعلي الحين، مو فحص طبيعي تمامًا.",
},
"AS-1314": {
    "B": "<bdi>CRP</bdi> علامة <bdi>inflammation</bdi> غير نوعية، تدعم <bdi>pneumonia</bdi> أو التهاب ثاني، مو <bdi>ventricular dysfunction</bdi>.",
    "C": "<bdi>CK (CK-MB)</bdi> علامة إصابة عضلة القلب و<bdi>ischemia</bdi>، تستخدم لـ<bdi>infarction</bdi> مو لـ<bdi>heart failure</bdi>.",
    "D": "<bdi>Troponin T</bdi> يدل على <bdi>myocardial necrosis</bdi> وهو تحليل <bdi>acute coronary syndrome</bdi> (ألم صدر، <bdi>ischemic ECG</bdi>)، مو تحليل <bdi>ventricular dysfunction</bdi>.",
},
}

HIGHLIGHT_TERMS = {
"AS-1308": ["abnormal fasting glucose", "high blood preesure readings", "BMI is 31", "significant smoking"],
"AS-1314": ["dyspnoea on exertion", "long standing hypertension", "rare crackles at the bases of the lungs"],
}
