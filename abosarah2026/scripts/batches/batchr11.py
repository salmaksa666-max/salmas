# -*- coding: utf-8 -*-
# Batch r11: AS-0083 ... (141 questions). Translated/restructured from source
# why_right / why_wrong_block / key_concept / exam_pearl per AGENT_INSTRUCTIONS.md.

EXPLANATIONS = {}
WHY_WRONG = {}
HIGHLIGHT_TERMS = {}

EXPLANATIONS.update({
"AS-0083": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "السؤال عن <bdi>pyogenic liver abscess</bdi> بعد <bdi>bacteremia</bdi> من مصدر سني، ومتى الحجم يفرض <bdi>drainage</bdi> مو <bdi>antibiotics</bdi> لوحدها.",
    "clues": [
        ("dental procedure", "مصدر <bdi>bacteremia</bdi> يودي لـ<bdi>pyogenic liver abscess</bdi> (مو <bdi>amoebic</bdi>)"),
        ("jaundice and chills", "<bdi>sepsis</bdi> من <bdi>hepatic abscess</bdi>"),
        ("6 cm hypoechoic lesion in the liver", "<bdi>abscess</bdi> كبير (أكبر من 3 سم) ما يستجيب لـ<bdi>antibiotics</bdi> لوحده"),
    ],
    "why_correct": [
        "<bdi>dental procedure</bdi> يعطي <bdi>bacteremia</bdi> تنزرع بالـ<bdi>liver</bdi> وتسوي <bdi>pyogenic abscess</bdi>، والـ<bdi>jaundice</bdi> مع <bdi>chills</bdi> يدعمون <bdi>sepsis</bdi> من مصدر كبدي.",
        "<bdi>abscess</bdi> بحجم 6 سم كبير، فما يروح لوحده بـ<bdi>antibiotics</bdi> فقط، إذن <bdi>management</bdi> المبدئي هو <bdi>image-guided percutaneous drainage</bdi> مع <bdi>IV broad-spectrum antibiotics</bdi>، وهذا كمان يعطي عينة <bdi>pus</bdi> للـ<bdi>culture</bdi>.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>abscess</bdi> صغير (أقل من 3 سم تقريبًا)، الجواب يصير <bdi>IV antibiotics</bdi> لوحدها بدون <bdi>drainage</bdi>.",
        "لو السيناريو فيه سفر وتاريخ يرجح <bdi>Entamoeba</bdi>، الجواب يتحول لـ<bdi>metronidazole</bdi> أول حتى لو الـ<bdi>abscess</bdi> كبير.",
    ],
    "rule": "<bdi>pyogenic liver abscess</bdi> كبير (أكبر من 3 سم) = <bdi>percutaneous drainage</bdi> + <bdi>IV antibiotics</bdi>؛ <bdi>amoebic abscess</bdi> = <bdi>metronidazole</bdi> أول دايمًا بغض النظر عن الحجم.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0087": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "السؤال عن أول خطوة بـ<bdi>primary survey</bdi> لـ<bdi>unstable pelvic fracture</bdi> مع <bdi>hypotension</bdi> رغم الـ<bdi>fluids</bdi>.",
    "clues": [
        ("hypotensive despite receiving IV fluids", "<bdi>ongoing hemorrhage</bdi> يحتاج تدخل فوري بالـ<bdi>circulation</bdi>"),
        ("openbook pelvic fracture", "<bdi>pelvic ring</bdi> متوسع يحتاج تضييق لتقليل النزف"),
    ],
    "why_correct": [
        "<bdi>open-book pelvic fracture</bdi> مع <bdi>hypotension</bdi> رغم الـ<bdi>IV fluids</bdi> يعني نزف مستمر من <bdi>pelvic ring</bdi> المتوسع.",
        "أول خطوة بـ<bdi>primary survey</bdi> (الـ<bdi>circulation</bdi>) هي <bdi>pelvic binder</bdi> فوق الـ<bdi>greater trochanters</bdi>: يقفل الـ<bdi>ring</bdi>، يقلل حجم الحوض، ويضغط على النزف <bdi>venous</bdi> والعظمي، وبنفس الوقت يبدأ نقل الدم.",
    ],
    "when_changes": [
        "لو المريض ثبت بعد الـ<bdi>binder</bdi> والـ<bdi>transfusion</bdi> وبعدين رجع يصير <bdi>unstable</bdi>، الجواب يصير <bdi>angioembolization</bdi> أو <bdi>pre-peritoneal packing</bdi>.",
        "لو السؤال يبي <bdi>definitive management</bdi> بعد ما المريض استقر تمامًا، الجواب يصير <bdi>internal fixation</bdi>.",
    ],
    "rule": "بـ<bdi>unstable pelvic fracture</bdi> مع <bdi>hypotension</bdi>، أبسط أداة بالسرير (<bdi>pelvic binder</bdi>) تسبق أي خيار جراحي كخطوة أولى.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0088": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "السؤال عن <bdi>management</bdi> الصحيح لـ<bdi>symptomatic reducible inguinal hernia</bdi> بمريض <bdi>fit</bdi> كبير بالسن.",
    "clues": [
        ("inguinal hernia incidentally", "اكتُشف بالـ<bdi>examination</bdi>، لكن السؤال عن علاجه مو التشخيص"),
        ("reducible", "ما فيه <bdi>incarceration</bdi> أو <bdi>strangulation</bdi> حاليًا"),
        ("slight discomfort", "هذا يجعلها <bdi>symptomatic</bdi> حتى لو خفيفة"),
    ],
    "why_correct": [
        "<bdi>reducible inguinal hernia</bdi> تسبب <bdi>discomfort</bdi> ولو خفيف تعتبر <bdi>symptomatic</bdi>، والقاعدة بالامتحان إن <bdi>symptomatic inguinal hernia</bdi> بمريض <bdi>fit</bdi> تُحوَّل لـ<bdi>elective surgical repair</bdi> (<bdi>open mesh repair</bdi> للحالة الأولية الأحادية).",
        "الـ<bdi>repair</bdi> يخفف <bdi>symptoms</bdi> ويشيل خطر <bdi>incarceration</bdi> و<bdi>strangulation</bdi> بالمستقبل.",
    ],
    "when_changes": [
        "لو الـ<bdi>hernia</bdi> بدون أي <bdi>symptoms</bdi> ومريض مسن ضعيف أو يرفض الجراحة، الجواب يصير <bdi>observation</bdi>.",
        "لو كانت <bdi>femoral hernia</bdi> حتى بدون <bdi>symptoms</bdi>، الجواب يصير <bdi>repair</bdi> لخطر <bdi>strangulation</bdi> العالي.",
    ],
    "rule": "أي <bdi>discomfort</bdi> ولو خفيف يجعل <bdi>inguinal hernia</bdi> حالة <bdi>symptomatic</bdi>؛ <bdi>observation</bdi> فقط للحالة بدون أعراض أو المريض اللي يرفض/غير مؤهل للجراحة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0089": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "السؤال يفرّق بين عدوى طرف الإصبع حسب الموضع: <bdi>pulp</bdi> مقابل <bdi>nail fold</bdi>.",
    "clues": [
        ("tip of her right thumb", "منطقة الـ<bdi>pulp</bdi> بطرف الإصبع"),
        ("tense tender swelling in pulp", "<bdi>abscess</bdi> داخل حيز <bdi>pulp</bdi> المقسّم"),
        ("Nail FOLD Is Intact", "يستبعد عدوى الـ<bdi>nail fold</bdi> (<bdi>paronychia</bdi>)"),
    ],
    "why_correct": [
        "<bdi>tense, tender swelling</bdi> بالـ<bdi>pulp</bdi> مع <bdi>nail fold</bdi> سليم بعد <bdi>minor trauma</bdi> (حفّ الجلد الزائد) يدل على <bdi>felon</bdi>: <bdi>abscess</bdi> داخل حيوز <bdi>pulp</bdi> المقسّمة المغلقة بطرف الإصبع.",
        "المحدد الأساسي هو الموضع: إصابة الـ<bdi>pulp</bdi> = <bdi>felon</bdi>، وإصابة الـ<bdi>nail fold</bdi> = <bdi>paronychia</bdi>.",
    ],
    "when_changes": [
        "لو كان التورم والألم حول الـ<bdi>nail fold</bdi> نفسه (بعد قص الزوائد الجلدية) مع <bdi>pulp</bdi> سليم، الجواب يصير <bdi>paronychia</bdi>.",
        "لو فيه <bdi>vesicles</bdi> بدل التورم المتوتر، الجواب يصير <bdi>herpetic whitlow</bdi> ولا يُفتح جراحيًا.",
    ],
    "rule": "كلمة <bdi>pulp</bdi> + <bdi>nail fold intact</bdi> = <bdi>felon</bdi>، وعلاجه <bdi>incision and drainage</bdi>؛ لا تنخدع بتاريخ قص الزوائد الجلدية اللي يذكّر بـ<bdi>paronychia</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0090": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "السؤال عن أول خطوة بـ<bdi>severe hypercalcemia</bdi> من <bdi>primary hyperparathyroidism</bdi> قبل الحل الجراحي.",
    "clues": [
        ("Recurrent ureteric stones", "عرض من <bdi>hypercalcemia</bdi> المزمن"),
        ("bone pain", "عرض من <bdi>PTH</bdi> الزايد على العظم"),
        ("Ca: 3.50 mmol", "<bdi>severe hypercalcemia</bdi> تحتاج تحكم فوري"),
        ("2cm parathyroid adenoma", "سبب <bdi>primary hyperparathyroidism</bdi> المؤكد"),
    ],
    "why_correct": [
        "الـ<bdi>calcium</bdi> عند 3.50 <bdi>mmol/L</bdi> مرتفع بشدة وقريب من حد <bdi>severe hypercalcemia</bdi>، والخطوة الفورية هي تخفيض الـ<bdi>calcium</bdi> بـ<bdi>IV normal saline</bdi> المكثف ثم <bdi>IV bisphosphonate</bdi> قبل أي شيء آخر.",
        "الـ<bdi>parathyroidectomy</bdi> هي العلاج النهائي، لكن بهذا السؤال تُحسب كخطوة بعد ضبط الـ<bdi>calcium</bdi> الحاد.",
    ],
    "when_changes": [
        "لو السؤال يبي <bdi>definitive management</bdi> أو ما فيه أزمة <bdi>calcium</bdi> حادة، الجواب ينقلب لـ<bdi>parathyroidectomy</bdi>.",
        "لو المريض غير مؤهل للجراحة، الجواب يصير <bdi>cinacalcet</bdi> (<bdi>calcimimetic</bdi>).",
    ],
    "rule": "بـ<bdi>severe hypercalcemia</bdi> الحادة، رتّب العلاج: <bdi>IV fluids</bdi> ثم <bdi>bisphosphonate</bdi> قبل <bdi>parathyroidectomy</bdi> النهائي.",
    "comparison": None,
    "labs": [["Calcium", "3.50 mmol/L", "2.1-2.6 mmol/L"]],
    "guideline_note": "الجواب هنا مو مؤكد 100% بالمصدر (معلّم بعلامة استفهام بين <bdi>bisphosphonate</bdi> و<bdi>parathyroidectomy</bdi>)، لكن نلتزم بإجابة المصدر <bdi>bisphosphonate</bdi> لأن السؤال يركّز على التحكم الحاد بالـ<bdi>calcium</bdi> أولًا.",
},
"AS-0091": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "السؤال عن أفضل مؤشر لتأكيد <bdi>adequate resuscitation</bdi> بعد <bdi>IV fluids</bdi>، يعني <bdi>tissue perfusion</bdi> مو الحجم أو الضغط فقط.",
    "clues": [
        ("IV fluid", "السؤال عن مؤشر نجاح الإنعاش بعدها"),
        ("well resuscitated", "يبي مؤشر <bdi>perfusion</bdi> لا <bdi>volume</bdi> فقط"),
    ],
    "why_correct": [
        "الإنعاش الكافي يظهر باستعادة <bdi>tissue perfusion</bdi>، و<bdi>serum lactate</bdi> أدق مؤشر مباشر له: <bdi>lactate</bdi> حوالي 2 <bdi>mmol/L</bdi> (طبيعي أو يتحسن) يعني الأكسجين الواصل للأنسجة كافي الآن.",
        "من بين الخيارات هو الوحيد اللي يؤكد نجاح الإنعاش فعليًا، لأن الباقي يقيس <bdi>volume</bdi> أو ضغط لحظي بدون تأكيد <bdi>perfusion</bdi>.",
    ],
    "when_changes": [
        "لو السيناريو عن <bdi>burn</bdi> وفيه خيار <bdi>urine output</bdi> كافي (0.5-1 <bdi>ml/kg/h</bdi>)، الجواب يصير <bdi>urine output</bdi> لأنه أفضل مؤشر بالـ<bdi>burns</bdi>.",
        "لو السيناريو <bdi>sepsis</bdi> وما فيه <bdi>lactate</bdi> ضمن الخيارات، ممكن يختارون <bdi>CVP</bdi> كخيار تاريخي أقل دقة.",
    ],
    "rule": "<bdi>perfusion markers</bdi> (<bdi>lactate clearance</bdi>) تتغلب على <bdi>pressure</bdi> و<bdi>volume markers</bdi> كدليل على نجاح الإنعاش، إلا بسيناريو <bdi>burns</bdi> اللي يفضَّل فيه <bdi>urine output</bdi>.",
    "comparison": {
        "headers": ["الخيار", "ماذا يقيس", "كفايته كمؤشر إنعاش"],
        "rows": [
            ["CVP 8", "<bdi>volume</bdi> تقريبي", "ضعيف، لا يؤكد <bdi>perfusion</bdi>"],
            ["MAP 45", "ضغط", "<bdi>shock</bdi> مستمر"],
            ["urine output 0.1", "<bdi>renal perfusion</bdi>", "<bdi>oliguria</bdi> شديد، إنعاش غير كافٍ"],
            ["lactate = 2", "<bdi>tissue perfusion</bdi>", "كافٍ / طبيعي"],
        ],
    },
    "labs": [["MAP", "45 mmHg", "≥65 mmHg"], ["Urine output", "0.1 ml/kg/h", "≥0.5 ml/kg/h"], ["Lactate", "2 mmol/L", "≤2 mmol/L"]],
    "guideline_note": None,
},
})

WHY_WRONG.update({
"AS-0083": {
    "A": "<bdi>oral antibiotics</bdi> غير كافية لمريض <bdi>septic</bdi> عنده <bdi>abscess</bdi> كبير؛ العلاج يبدأ <bdi>IV</bdi> مع <bdi>drainage</bdi>، والـ<bdi>antibiotics</bdi> لوحدها تناسب فقط <bdi>abscess</bdi> صغير أو <bdi>amoebic abscess</bdi> بـ<bdi>metronidazole</bdi>.",
},
"AS-0087": {
    "B": "<bdi>external fixation</bdi> يثبّت الحوض بشكل أدق لكن يحتاج وقت وموارد غرفة العمليات؛ يجي بعد الـ<bdi>binder</bdi> بمريض <bdi>unstable</bdi>، مو قبله.",
    "C": "<bdi>surgery</bdi> (مثل <bdi>laparotomy</bdi> أو <bdi>pre-peritoneal packing</bdi>) تجي لو استمر عدم الاستقرار بعد الـ<bdi>binder</bdi> والـ<bdi>transfusion</bdi>، مو كخطوة أولى للنزف الحوضي.",
    "D": "<bdi>internal fixation</bdi> علاج نهائي مؤجل يصير بعد استقرار المريض تمامًا؛ ما له مكان بالإنعاش الحاد لمريض <bdi>hypotensive</bdi>.",
},
"AS-0088": {
    "B": "<bdi>observation</bdi> تناسب <bdi>hernia</bdi> بدون أعراض أو مريض غير مؤهل/يرفض الجراحة؛ أغلب الحالات المتابَعة بالمسنين تنتهي بحاجة <bdi>repair</bdi>، وهذه الحالة فيها <bdi>discomfort</bdi> من الأساس.",
    "C": "زيادة النشاط <bdi>physical activity</bdi> لا تعالج الـ<bdi>hernia</bdi> وممكن تزيد ضغط البطن؛ لا يوجد علاج تمارين لـ<bdi>inguinal hernia</bdi>.",
},
"AS-0089": {
    "B": "<bdi>paronychia</bdi> عدوى الـ<bdi>nail fold</bdi> حول الظفر، كلاسيكيًا بعد قص الزوائد الجلدية أو العناية بالأظافر؛ هنا النص يوضح إن الـ<bdi>nail fold</bdi> سليم والتورم بالـ<bdi>pulp</bdi>.",
    "C": "<bdi>onychomycosis</bdi> عدوى فطرية مزمنة بصفيحة الظفر تسبب تثخّن وتغيّر لون، مو تورم حاد متوتر ومؤلم بالـ<bdi>pulp</bdi> خلال يومين.",
    "D": "<bdi>cellulitis</bdi> احمرار منتشر غير محدد بالجلد والنسيج تحته؛ التورم المحدد المتوتر هنا هو <bdi>abscess</bdi> بحيز مغلق، يعني <bdi>felon</bdi>.",
},
"AS-0090": {
    "B": "<bdi>calcimimetic</bdi> (<bdi>cinacalcet</bdi>) يخفّض <bdi>PTH</bdi> والـ<bdi>calcium</bdi> بمرضى غير مرشّحين للجراحة أو بـ<bdi>parathyroid carcinoma</bdi>؛ ليس الخيار الأول بمرشّح جراحي وتأثيره بطيء جدًا لارتفاع حاد شديد.",
    "C": "زيادة <bdi>dietary calcium</bdi> تزيد <bdi>hypercalcemia</bdi> وتكوّن الحصوات؛ لا دور له هنا إطلاقًا.",
    "D": "<bdi>parathyroidectomy</bdi> هو العلاج النهائي ومؤشر بوضوح (مرض <bdi>symptomatic</bdi> مع حصوات وألم عظمي وارتفاع <bdi>calcium</bdi> شديد مع <bdi>adenoma</bdi> محدد)، لكن بهذا السؤال يُحسب كخطوة بعد ضبط الـ<bdi>calcium</bdi> الحاد.",
},
"AS-0091": {
    "A": "<bdi>CVP</bdi> يقيس فقط تقدير حجم الامتلاء الوريدي؛ كان هدف قديم بالـ<bdi>early goal-directed therapy</bdi> لكن ضعيف الارتباط بالاستجابة للسوائل وما يثبت <bdi>perfusion</bdi> الأنسجة.",
    "B": "<bdi>MAP</bdi> عند 45 <bdi>mmHg</bdi> يعني <bdi>hypotension</bdi> و<bdi>shock</bdi> مستمر؛ الهدف ≥65 <bdi>mmHg</bdi>.",
    "C": "<bdi>urine output</bdi> مؤشر ممتاز للإنعاش (الأفضل كلاسيكيًا بالـ<bdi>burns</bdi>، الهدف ≥0.5 <bdi>ml/kg/h</bdi> بالبالغين)، لكن 0.1 <bdi>ml/kg/h</bdi> يعني <bdi>oliguria</bdi> شديد وإنعاش غير كافٍ.",
},
})

HIGHLIGHT_TERMS.update({
"AS-0083": ["dental procedure", "jaundice and chills", "6 cm hypoechoic lesion in the liver"],
"AS-0087": ["hypotensive despite receiving IV fluids", "openbook pelvic fracture"],
"AS-0088": ["inguinal hernia incidentally", "reducible", "slight discomfort"],
"AS-0089": ["tip of her right thumb", "tense tender swelling in pulp", "Nail FOLD Is Intact"],
"AS-0090": ["Recurrent ureteric stones", "bone pain", "Ca: 3.50 mmol", "2cm parathyroid adenoma"],
"AS-0091": ["IV fluid", "well resuscitated"],
})

EXPLANATIONS.update({
"AS-0110": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "لازم تقرأ فعل السؤال بدقة: فيه فرق بين <bdi>initial imaging</bdi> و<bdi>most appropriate imaging</bdi> لـ<bdi>biliary obstruction</bdi>.",
    "clues": [
        ("jaundice", "يرجّح انسداد بالـ<bdi>biliary tree</bdi>"),
        ("RUQ tenderness", "مصدر الألم كبدي صفراوي"),
        ("LFT and bilirubin are elevated", "يدعم <bdi>obstructive jaundice</bdi>"),
    ],
    "why_correct": [
        "السؤال يسأل عن <bdi>most appropriate</bdi> مب <bdi>initial</bdi>، وبمريض عنده <bdi>jaundice</bdi> و<bdi>RUQ tenderness</bdi> وارتفاع <bdi>bilirubin</bdi> و<bdi>LFTs</bdi>، أدق فحص غير جراحي يبيّن كامل الـ<bdi>biliary tree</bdi> ويكشف حصوات أو تضيّقات بـ<bdi>CBD</bdi> هو <bdi>MRCP</bdi>.",
        "الفرق مهم: <bdi>initial</bdi> = <bdi>ultrasound</bdi>، بينما <bdi>most appropriate</bdi> لتوضيح تشريح الـ<bdi>biliary tree</bdi> بدقة = <bdi>MRCP</bdi>.",
    ],
    "when_changes": [
        "لو السؤال قال \"initial\" أو \"first\"، الجواب يرجع لـ<bdi>abdominal ultrasound</bdi>.",
        "لو السؤال فيه <bdi>cholangitis</bdi> وحصوة مؤكدة وحاجة للعلاج بنفس الوقت، الجواب يصير <bdi>ERCP</bdi>.",
    ],
    "rule": "بأي سؤال صفراوي: \"initial\" = <bdi>ultrasound</bdi>، \"most appropriate / confirm CBD stone\" = <bdi>MRCP</bdi>، \"therapeutic\" = <bdi>ERCP</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0123": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "مريض خارج الطوارئ بعد حادث قبل أسبوع عنده ألم جديد بالـ<bdi>RUQ</bdi>؛ السؤال عن مكان التقييم الصحيح مو الفحص نفسه.",
    "clues": [
        ("Vitally stable", "لا يستبعد إصابة متأخرة محتواة بالكبد"),
        ("right upper quadrant", "موضع إصابة <bdi>liver</bdi> المحتملة"),
    ],
    "why_correct": [
        "ألم متأخر بالـ<bdi>RUQ</bdi> بعد حادث (أسبوع) قد يعكس إصابة كبدية محتواة أو <bdi>subcapsular hematoma</bdi> أو نزف متأخر، حتى لو المريض <bdi>vitally stable</bdi>.",
        "هذا يحتاج بيئة فيها إمكانية <bdi>CT with contrast</bdi> ومراقبة متسلسلة وتدخل فوري لو تدهور، فالخطوة الأولى الصحيحة هي <bdi>referral</bdi> للطوارئ لتقييم كامل.",
    ],
    "when_changes": [
        "لو كان الخيار يذكر \"CT abdomen with contrast\" مباشرة بمريض <bdi>stable</bdi> بعد <bdi>trauma</bdi>، هذا يتغلب على <bdi>referral</bdi> و<bdi>ultrasound</bdi> كخطوة تشخيصية.",
        "لو المريض <bdi>unstable</bdi> مع <bdi>positive FAST</bdi>، الجواب يصير <bdi>laparotomy</bdi> فورًا.",
    ],
    "rule": "ألم بطني متأخر بعد <bdi>trauma</bdi> يُقيَّم بالطوارئ حتى لو العلامات الحيوية مستقرة؛ <bdi>CT with contrast</bdi> هو فحص <bdi>stable trauma</bdi> المعياري، لكنه يتم ضمن تقييم الطوارئ لا كفحص خارجي منفصل.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0156": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "تورم وتدهور عصبي بعد <bdi>revascularisation</bdi> مباشرة = <bdi>acute compartment syndrome</bdi> من إصابة <bdi>reperfusion</bdi>، والعلاج تحرير الضغط فورًا.",
    "clues": [
        ("6hours post femoral artery surgery", "توقيت نموذجي لإصابة <bdi>reperfusion</bdi>"),
        ("swelling and worsening neurological signs", "علامات <bdi>compartment syndrome</bdi> المتقدمة"),
    ],
    "why_correct": [
        "بعد <bdi>revascularisation</bdi>، تسرّب الشعيرات (<bdi>capillary leak</bdi>) يرفع ضغط الحيز العضلي، فيصير <bdi>ischemia</bdi> للعضلة والعصب، والضرر يصبح دائم خلال ساعات لو ما عُولج.",
        "العلاج هو تحرير حيوز الـ<bdi>fascia</bdi> فورًا (<bdi>fasciotomy</bdi>) لإنقاذ الطرف واستعادة التروية.",
    ],
    "when_changes": [
        "لو السبب كسر بالعظم بدون تورم حيّز، الجواب يصير تثبيت الكسر لا فتح الحيوز.",
        "لو العصب مقطوع فعليًا (<bdi>laceration</bdi>) بدون علامات ضغط حيّز، الجواب يصير <bdi>nerve repair</bdi>.",
    ],
    "rule": "تورم + ألم + تدهور عصبي بعد جراحة وعائية = <bdi>compartment syndrome</bdi> لحد ما يُستبعد؛ وجود نبض محيطي لا يستبعده، والعلاج <bdi>emergency fasciotomy</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0161": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "السؤال عن أول خطوة بـ<bdi>open fracture</bdi>؛ ترتيب الخطوات مهم جدًا: <bdi>antibiotics</bdi> قبل غرفة العمليات.",
    "clues": [
        ("open femur fracture", "جرح ملوّث من لحظة الإصابة"),
        ("5-cm wound", "يؤكد كونه <bdi>open fracture</bdi> واضح"),
    ],
    "why_correct": [
        "<bdi>open femur fracture</bdi> مع جرح 5 سم ملوّث من البداية، وأكثر خطوة فعالة لمنع العدوى العميقة و<bdi>osteomyelitis</bdi> هي <bdi>IV antibiotics</bdi> مبكرًا.",
        "لأن السؤال يقول \"first step\"، تبدأ الـ<bdi>antibiotics</bdi> خلال الساعة الأولى (مع <bdi>tetanus prophylaxis</bdi>، تصوير الجرح، تغطيته بـ<bdi>saline dressing</bdi>، وتجبيس) قبل الذهاب لغرفة العمليات.",
    ],
    "when_changes": [
        "لو السؤال يقول الـ<bdi>antibiotics</bdi> أُعطيت مسبقًا ويسأل عن الخطوة التالية، الجواب يصير <bdi>surgical debridement</bdi>.",
        "لو فيه تلوث شديد جدًا أو تهديد للطرف، يصير <bdi>debridement</bdi> الطارئ أقرب زمنيًا للـ<bdi>antibiotics</bdi>.",
    ],
    "rule": "بترتيب <bdi>open fracture</bdi>: <bdi>IV antibiotics</bdi> أولًا، ثم <bdi>debridement</bdi> بغرفة العمليات، ثم التثبيت النهائي.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0163": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نفس سيناريو <bdi>pyogenic liver abscess</bdi> بعد <bdi>dental procedure</bdi> (تكرار لـ AS-0083) — الحجم الكبير يفرض <bdi>drainage</bdi>.",
    "clues": [
        ("dental procedure", "مصدر <bdi>bacteremia</bdi> يودي لـ<bdi>pyogenic liver abscess</bdi>"),
        ("jaundice and chills", "<bdi>sepsis</bdi> من مصدر كبدي"),
        ("6-cm hypoechoic lesion in the liver", "<bdi>abscess</bdi> كبير يحتاج <bdi>drainage</bdi>"),
    ],
    "why_correct": [
        "<bdi>dental procedure</bdi> يعطي <bdi>bacteremia</bdi> تنزرع بالكبد وتسوي <bdi>pyogenic abscess</bdi>، والـ<bdi>jaundice</bdi> مع <bdi>chills</bdi> يدعمون <bdi>sepsis</bdi> كبدي المصدر.",
        "بحجم 6 سم، العلاج المبدئي <bdi>image-guided percutaneous drainage</bdi> مع <bdi>IV broad-spectrum antibiotics</bdi>، وهذا يعطي عينة <bdi>pus</bdi> للـ<bdi>culture</bdi> أيضًا.",
    ],
    "when_changes": [
        "لو كان الحجم أصغر من 3 سم تقريبًا، يكفي <bdi>IV antibiotics</bdi> لوحدها.",
        "لو السيناريو فيه سفر وتاريخ يرجّح <bdi>Entamoeba</bdi>، الجواب يصير <bdi>metronidazole</bdi> أول رغم الحجم.",
    ],
    "rule": "<bdi>pyogenic liver abscess</bdi> كبير = <bdi>percutaneous drainage</bdi> + <bdi>IV antibiotics</bdi>؛ <bdi>amoebic</bdi> = <bdi>metronidazole</bdi> أول بغض النظر عن الحجم.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0226": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "السؤال عن الفحص اللي يأكد نوع <bdi>diabetic foot ulcer</bdi> (<bdi>neuropathic</bdi> مقابل <bdi>arterial</bdi>) حسب الموضع والنبض.",
    "clues": [
        ("plantar foot ulcer", "موضع تحمّل الوزن النموذجي لـ<bdi>neuropathic ulcer</bdi>"),
        ("diminished sensation", "فقدان الحس الوقائي"),
        ("intact peripheral pulses", "يستبعد السبب <bdi>arterial</bdi>"),
    ],
    "why_correct": [
        "<bdi>plantar ulcer</bdi> بمريض سكري عنده <bdi>diminished sensation</bdi> مع <bdi>intact peripheral pulses</bdi> يرجّح <bdi>neuropathic ulcer</bdi>: موضع تحمّل الوزن، تروية كافية، فقدان الحس الوقائي.",
        "الفحص اللي يثبت هذا التشخيص هو <bdi>10-g monofilament test</bdi>، يأكد فقدان الحس الوقائي ومنه السبب <bdi>neuropathic</bdi>.",
    ],
    "when_changes": [
        "لو كان القرح على <bdi>malleolus</bdi> أو ظهر القدم وغير ملتئم مع ضعف النبض، الجواب يتحول لـ<bdi>ABI</bdi> لتقييم السبب <bdi>arterial</bdi>.",
        "لو فيه شك بـ<bdi>osteomyelitis</bdi> (قرحة عميقة مزمنة)، الفحص المناسب يصير <bdi>MRI</bdi> لا <bdi>CT</bdi>.",
    ],
    "rule": "<bdi>plantar</bdi> + نبض سليم + فقدان حس = <bdi>neuropathic ulcer</bdi> يُؤكَّد بـ<bdi>monofilament test</bdi>؛ موضع <bdi>dorsal/malleolar</bdi> وغير ملتئم مع ضعف نبض = فكّر <bdi>arterial</bdi> ويُقيَّم بـ<bdi>ABI</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0233": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>trauma</bdi> مع نبض ضعيف وتقرّح بالذراع يرجّح إصابة <bdi>arterial</bdi> تحتاج استكشاف جراحي فوري.",
    "clues": [
        ("trauma", "سبب الإصابة الوعائية المحتملة"),
        ("decreased pulses", "علامة قوية (<bdi>hard sign</bdi>) على إصابة <bdi>arterial</bdi>"),
    ],
    "why_correct": [
        "نقص النبض بعد <bdi>trauma</bdi> مع تقرّح (علامة نقص تروية مزمن) هو من <bdi>hard signs</bdi> لإصابة الشريان، والتعامل الصحيح هو <bdi>surgical exploration/repair</bdi> عاجل لإنقاذ الطرف.",
        "ما فيه هنا علامات <bdi>compartment syndrome</bdi> الكلاسيكية (ألم شديد خارج عن التناسب، تيبّس الحيّز)، فالأولوية لتصحيح مشكلة الشريان نفسه.",
    ],
    "when_changes": [
        "لو الوصف يذكر ألم شديد خارج التناسب وتيبّس حيّز العضلة مع نبض متذبذب، الجواب يصير <bdi>fasciotomy</bdi> لـ<bdi>compartment syndrome</bdi>.",
        "لو الطرف نفسه فيه نقص تروية إقفاري شديد، لا ترفعه فوق مستوى القلب؛ يبقى بمستوى القلب.",
    ],
    "rule": "نبض ضعيف وشاحب وبرد بعد <bdi>trauma</bdi> = فكّر بالشريان أولًا (استكشاف/تصحيح جراحي)؛ ألم شديد مع حيّز متيبّس = فكّر <bdi>compartment syndrome</bdi> (<bdi>fasciotomy</bdi>).",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر نفسه غير متأكد من هذا الجواب (معلّم بعلامات استفهام)، لكن نلتزم بـ<bdi>answer_letter</bdi> المعطى B لأنه الإجابة المؤكدة من المصدر.",
},
"AS-0265": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "<bdi>intermittent biliary colic</bdi> مع <bdi>jaundice</bdi> يرجّح <bdi>choledocholithiasis</bdi>، والسؤال عن أدق فحص تصويري لتأكيد حصوة الـ<bdi>CBD</bdi>.",
    "clues": [
        ("intermittent RUQ pain", "نمط <bdi>biliary colic</bdi> المتكرر"),
        ("jaundice", "يدعم انسداد بالـ<bdi>CBD</bdi>"),
        ("high bilirubin and LFTs", "يؤكد صورة الانسداد الصفراوي"),
    ],
    "why_correct": [
        "الألم المتكرر بالـ<bdi>RUQ</bdi> مع <bdi>nausea</bdi> و<bdi>vomiting</bdi> و<bdi>jaundice</bdi> وارتفاع <bdi>bilirubin</bdi> و<bdi>LFTs</bdi> يرجّح <bdi>choledocholithiasis</bdi>، والسؤال يسأل عن \"most appropriate\" (بعد مرحلة الفحص الأولي) فيكون <bdi>MRCP</bdi>: دقيق وغير جراحي لرؤية الـ<bdi>CBD</bdi> بالكامل.",
        "<bdi>MRCP</bdi> يفرّق بدقة بين وجود حصوة بالـ<bdi>CBD</bdi> أو تضيّق، وهذا أهم من الفحص الأولي السريع.",
    ],
    "when_changes": [
        "لو السؤال قال \"initial\"، الجواب يرجع لـ<bdi>abdominal US</bdi>.",
        "لو فيه حمى مع <bdi>Charcot triad</bdi> كاملة (حمى + ألم + يرقان) وحصوة مؤكدة، الجواب يصير <bdi>ERCP</bdi> لأنه علاجي وتشخيصي.",
    ],
    "rule": "\"most appropriate\" لتأكيد حصوة <bdi>CBD</bdi> بعد الشك = <bdi>MRCP</bdi>؛ \"initial\" = <bdi>ultrasound</bdi>؛ <bdi>cholangitis</bdi> مؤكد = <bdi>ERCP</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": "إجابة المصدر نفسه مش مؤكدة 100% (معلّمة بعلامات استفهام بين <bdi>MRCP</bdi> و<bdi>US</bdi>)، لكن نلتزم بـ<bdi>answer_letter</bdi> المعطى A كإجابة المصدر الرسمية.",
},
"AS-0273": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "قرحة سكري بموضع يرجّح <bdi>osteomyelitis</bdi> محتمل، والسؤال عن أدق فحص لتأكيد إصابة العظم رغم وجود تورم بالـ<bdi>calf</bdi> يشتت الانتباه.",
    "clues": [
        ("diabetes", "عامل خطر لـ<bdi>infection</bdi> وضعف التئام"),
        ("warmth and tenderness of the (calf)", "يثير الشك بـ<bdi>DVT</bdi> لكنه مشتت هنا"),
        ("2 cm ulcer over the first metatarsal area", "موضع قريب من العظم، يرجّح <bdi>osteomyelitis</bdi> محتمل"),
        ("Distal pulses are intact", "يستبعد السبب <bdi>arterial</bdi> الرئيسي"),
    ],
    "why_correct": [
        "قرحة 2 سم فوق <bdi>first metatarsal</bdi> بمريض سكري مع نبض سليم ترفع الشك بإصابة العظم تحتها (<bdi>osteomyelitis</bdi>)، والفحص الأدق لتأكيد ذلك هو <bdi>MRI</bdi>.",
        "تورم وحرارة الـ<bdi>calf</bdi> يثير احتمال <bdi>DVT</bdi>، لكن السؤال يركّز على القرحة والعظم تحتها، فالـ<bdi>MRI</bdi> هو الأنسب لتوضيح عمق الإصابة.",
    ],
    "when_changes": [
        "لو السؤال ركّز بالكامل على ألم وتورم الـ<bdi>calf</bdi> كاحتمال <bdi>DVT</bdi> بدون تفصيل عن القرحة، الجواب يتحول لـ<bdi>duplex ultrasound</bdi>.",
        "لو النبض غائب وفيه قرحة غير ملتئمة، الجواب يصير تقييم <bdi>arterial</bdi> (<bdi>angiography</bdi> أو <bdi>duplex</bdi> شرياني).",
    ],
    "rule": "قرحة سكري قريبة من عظم مع نبض سليم = فكّر <bdi>osteomyelitis</bdi> ويؤكَّد بـ<bdi>MRI</bdi>؛ تورم وحرارة الـ<bdi>calf</bdi> وحده يوجّه نحو <bdi>duplex</bdi> لاستبعاد <bdi>DVT</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر نفسه مختلف بين <bdi>MRI</bdi> و<bdi>Duplex</bdi> (معلّم «C or A not sure»)، لكن نلتزم بـ<bdi>answer_letter</bdi> المعطى C.",
},
})

WHY_WRONG.update({
"AS-0110": {
    "B": "<bdi>abdominal ultrasound</bdi> هو فحص الـ<bdi>INITIAL</bdi> لليرقان مع ألم <bdi>RUQ</bdi> (سريع، رخيص، يبيّن الحصوات وتوسع الـ<bdi>CBD</bdi>)؛ يُختار لو السؤال قال \"initial\" أو \"first\"، ونقطة ضعفه رؤية ضعيفة للـ<bdi>distal CBD</bdi>.",
    "C": "<bdi>CT abdomen</bdi> أفضل بالشك بورم خبيث (كتلة رأس البنكرياس) أو المضاعفات أو التدريج؛ يفوّت كثير من حصوات الـ<bdi>CBD</bdi> غير المتكلّسة.",
},
"AS-0123": {
    "A": "<bdi>ultrasound (FAST)</bdi> فحص سريع عند السرير للسوائل الحرة، غالبًا بالمرضى <bdi>unstable</bdi>؛ يعتمد على مهارة الفاحص وضعيف بتقييم درجة إصابة الأعضاء الصلبة، وبالمريض المستقر الفحص الحاسم هو <bdi>CT</bdi> ضمن تقييم الطوارئ.",
    "C": "فحوصات الدم (<bdi>Hb</bdi>، <bdi>LFTs</bdi>) تدعم التقييم لكنها لا تستبعد أو تحدد الإصابة لوحدها؛ <bdi>Hb</bdi> طبيعي مبكرًا لا يستبعد النزف، وتُطلب ضمن تقييم الطوارئ لا بدلاً عنه.",
},
"AS-0156": {
    "A": "<bdi>backslab</bdi> (جبيرة جبسية) تُستخدم لتثبيت كسر؛ وضع أي جبس أو ضمادة ضيقة على طرف يرتفع فيه ضغط الحيّز يزيد الوضع سوءًا؛ بالاشتباه بـ<bdi>compartment syndrome</bdi> تُزال كل الجبائر والضمادات لا تُضاف.",
    "B": "<bdi>traction</bdi> تُستخدم لمحاذاة أو تثبيت الكسور (مثل كسر عظم الفخذ)؛ لا تؤثر على ضغط الحيّز وممكن ترفعه.",
    "D": "<bdi>nerve repair</bdi> يناسب العصب المقطوع فعليًا؛ هنا العجز العصبي سببه نقص تروية بالضغط، ويتحسن فقط بتحرير الحيّز بسرعة.",
},
"AS-0161": {
    "A": "<bdi>surgical debridement</bdi> والغسل ضروريان لكنهما الخطوة التالية، تتمّان بشكل عاجل (خلال حوالي 12 ساعة للإصابات عالية الطاقة مثل كسر الفخذ المفتوح) بعد بدء <bdi>antibiotics</bdi>؛ يكون الجواب لو السؤال قال الـ<bdi>antibiotics</bdi> أُعطيت مسبقًا ويسأل عن الخطوة التالية.",
},
"AS-0163": {
    "A": "<bdi>oral antibiotics</bdi> غير كافية لمريض <bdi>septic</bdi> مع <bdi>abscess</bdi> كبير؛ العلاج يبدأ <bdi>IV</bdi> مع <bdi>drainage</bdi>، وتُترك الـ<bdi>antibiotics</bdi> لوحدها للحالات الصغيرة أو <bdi>amoebic abscess</bdi>.",
},
"AS-0226": {
    "A": "<bdi>ABI</bdi> يقيّم القصور <bdi>arterial</bdi>؛ هو الفحص الأهم عند غياب أو ضعف النبض أو قرحة غير ملتئمة بموضع ظهري/كعب؛ هنا النبض سليم والقرحة بالالتئام (وممكن يرتفع كاذبًا بالسكري بسبب تكلّس الأوعية).",
    "C": "<bdi>CT</bdi> لا يشخّص نوع القرحة؛ الشك بالعدوى العميقة أو <bdi>osteomyelitis</bdi> يُقيَّم بـ<bdi>X-ray</bdi> أولًا ثم <bdi>MRI</bdi>، لا <bdi>CT</bdi>.",
    "D": "تحديد نقاط الضغط يوجّه الوقاية وتخفيف الحمل بعد تأكيد وجود الاعتلال العصبي؛ هذا <bdi>management</bdi> لا فحص تشخيصي.",
},
"AS-0233": {
    "A": "<bdi>fasciotomy</bdi> علاج <bdi>compartment syndrome</bdi> (ألم خارج التناسب، حيّز متيبّس، ألم بالتمدد السلبي)؛ نقص النبض وحده بعد <bdi>trauma</bdi> يرجّح إصابة الشريان أولًا.",
    "C": "رفع الطرف فوق مستوى القلب يزيد سوء التروية بحالة نقص التروية الإقفاري؛ خطأ هنا.",
},
"AS-0265": {
    "B": "<bdi>abdominal ultrasound</bdi> هو الفحص الـ<bdi>INITIAL</bdi> (سريع، يكشف حصوات وتوسع <bdi>CBD</bdi>)؛ يُختار لو السؤال قال \"initial\"، لكن هذا السؤال يسأل عن الأنسب لتأكيد حصوة الـ<bdi>CBD</bdi>.",
    "C": "<bdi>CT abdomen</bdi> أفضل بالشك بورم خبيث أو مضاعفات؛ يفوّت كثير من حصوات الـ<bdi>CBD</bdi> غير المتكلّسة ولا يناسب هذا العرض.",
},
"AS-0273": {
    "A": "<bdi>duplex ultrasound</bdi> الأفضل لتقييم <bdi>DVT</bdi>؛ مفيد لو تركيز السؤال على تورم الـ<bdi>calf</bdi> فقط، لكن هنا القرحة فوق العظم تطرح شك أقوى بـ<bdi>osteomyelitis</bdi> يحتاج <bdi>MRI</bdi>.",
    "B": "<bdi>conventional angiography</bdi> فحص جراحي باضع لتقييم الشريان قبل التدخل؛ لا يناسب هذا العرض لأن النبض سليم وما فيه دليل قوي على مرض شرياني.",
    "D": "<bdi>CT with contrast</bdi> ليس الأدق للعظم أو الأنسجة الرخوة هنا؛ <bdi>MRI</bdi> أدق لتقييم <bdi>osteomyelitis</bdi> المحتمل.",
},
})

HIGHLIGHT_TERMS.update({
"AS-0110": ["jaundice", "RUQ tenderness", "LFT and bilirubin are elevated"],
"AS-0123": ["Vitally stable", "right upper quadrant"],
"AS-0156": ["6hours post femoral artery surgery", "swelling and worsening neurological signs"],
"AS-0161": ["open femur fracture", "5-cm wound"],
"AS-0163": ["dental procedure", "jaundice and chills", "6-cm hypoechoic lesion in the liver"],
"AS-0226": ["plantar foot ulcer", "diminished sensation", "intact peripheral pulses"],
"AS-0233": ["trauma", "decreased pulses"],
"AS-0265": ["intermittent RUQ pain", "jaundice", "high bilirubin and LFTs"],
"AS-0273": ["diabetes", "warmth and tenderness of the (calf)", "2 cm ulcer over the first metatarsal area", "Distal pulses are intact"],
})

EXPLANATIONS.update({
"AS-0312": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "<bdi>reducible inguinal hernia</bdi> بأعراض خفيفة جدًا بس عند كبير بالسن = <bdi>watchful waiting</bdi> خيار مقبول، مو <bdi>repair</bdi> مباشرة.",
    "clues": [
        ("reducible inguinal hernia", "لا فيه <bdi>incarceration</bdi> أو <bdi>strangulation</bdi>"),
        ("mild discomfort without significant pain", "أعراض بسيطة جدًا تجعل <bdi>watchful waiting</bdi> آمن"),
    ],
    "why_correct": [
        "الـ<bdi>hernia</bdi> هنا <bdi>reducible</bdi> مع <bdi>discomfort</bdi> خفيف بدون ألم مهم، يعني <bdi>minimally symptomatic</bdi>.",
        "بمريض كبير بالسن مع <bdi>hernia</bdi> بهذا المستوى من الأعراض، <bdi>watchful waiting</bdi> مع مراجعة دورية خيار مقبول لأن خطر <bdi>acute incarceration</bdi> منخفض؛ الجراحة تُعرض لو زادت الأعراض أو صارت <bdi>irreducible</bdi>.",
    ],
    "when_changes": [
        "لو الألم أصبح يحدّ من النشاط اليومي أو الـ<bdi>hernia</bdi> كبرت أو صارت <bdi>irreducible</bdi>، الجواب يتحول لـ<bdi>surgical repair</bdi>.",
        "لو كانت <bdi>femoral hernia</bdi>، الجواب يصير <bdi>repair</bdi> حتى بدون أعراض لخطر <bdi>strangulation</bdi> العالي.",
    ],
    "rule": "\"mild discomfort without significant pain\" = <bdi>watchful waiting</bdi>؛ \"pain limiting activity\" أو <bdi>irreducible</bdi> أو <bdi>femoral</bdi> = <bdi>repair</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0332": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>lucid interval</bdi> ثم فقدان وعي مع آفة <bdi>convex</bdi> بالـ<bdi>CT</bdi> = <bdi>epidural hematoma</bdi>، وعلاجها الجراحي الفوري.",
    "clues": [
        ("lucid interval", "علامة كلاسيكية لـ<bdi>epidural hematoma</bdi>"),
        ("convex lesion", "شكل <bdi>biconvex/lens-shaped</bdi> نموذجي لـ<bdi>epidural</bdi>"),
    ],
    "why_correct": [
        "إصابة رأس مع <bdi>lucid interval</bdi> ثم فقدان وعي وآفة <bdi>convex</bdi> (عدسية الشكل) بالـ<bdi>CT</bdi> هي <bdi>epidural hematoma</bdi>، غالبًا من تمزق <bdi>middle meningeal artery</bdi>.",
        "هذا نزف شرياني متوسع يسبب تأثير كتلي، فالعلاج الأنسب الفوري هو <bdi>craniotomy</bdi> عاجل وإخراج الـ<bdi>hematoma</bdi>.",
    ],
    "when_changes": [
        "لو الآفة <bdi>concave/crescent-shaped</bdi> بمريض مسن أو مدمن كحول وتطور تدريجي، الجواب يصير <bdi>subdural hematoma</bdi> (نفس علاج الإخراج الجراحي لو كبيرة).",
        "لو المريض بانتظار نقله للجراحة وفيه ارتفاع ضغط داخل الجمجمة، <bdi>mannitol</bdi> يُستخدم كجسر مؤقت لا كعلاج نهائي.",
    ],
    "rule": "آفة <bdi>convex</bdi> + <bdi>lucid interval</bdi> = <bdi>epidural hematoma</bdi>؛ العلاج <bdi>craniotomy</bdi> عاجل، و<bdi>airway</bdi> و<bdi>mannitol</bdi> فقط كجسور مؤقتة.",
    "comparison": {
        "headers": ["النوع", "الشكل بالـCT", "المصدر", "النمط الزمني"],
        "rows": [
            ["Epidural", "<bdi>convex / lens-shaped</bdi>", "<bdi>middle meningeal artery</bdi>", "<bdi>lucid interval</bdi> ثم تدهور"],
            ["Subdural", "<bdi>concave / crescent-shaped</bdi>", "<bdi>bridging veins</bdi>", "تدريجي، بالمسنين"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},
"AS-0334": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "حركة جدار صدر <bdi>paradoxical</bdi> بعد <bdi>blunt trauma</bdi> = <bdi>flail chest</bdi> من كسور أضلاع متعددة متجاورة.",
    "clues": [
        ("Paradoxical chest wall movement", "علامة مباشرة لفقدان الاستمرارية العظمية بجدار الصدر"),
    ],
    "why_correct": [
        "<bdi>paradoxical chest wall movement</bdi> بعد <bdi>blunt trauma</bdi> يعني جزء من جدار الصدر فقد استمراريته العظمية: <bdi>flail chest</bdi>، من كسور عدة أضلاع متجاورة كل واحد مكسور بأكثر من موضع.",
        "الجزء الحر ينسحب للداخل أثناء الشهيق وينبرز للخارج أثناء الزفير، عكس حركة باقي جدار الصدر.",
    ],
    "when_changes": [
        "لو السيناريو فيه اضطراب نظم قلبي أو تغيّرات <bdi>ECG</bdi> جديدة بعد ضربة على عظم القص، الجواب يتحول لـ<bdi>cardiac contusion</bdi>.",
        "لو فيه هبوط ضغط وانتفاخ أوردة رقبية مع انحراف القصبة، الجواب يصير <bdi>tension pneumothorax</bdi>.",
    ],
    "rule": "<bdi>paradoxical chest wall movement</bdi> = <bdi>flail chest</bdi>؛ العلاج دعم تنفسي وتسكين ألم، والسبب الأساسي لنقص الأكسجين هو <bdi>pulmonary contusion</bdi> تحت القطعة المكسورة لا الحركة نفسها.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0344": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "تورم متوتر بـ<bdi>pulp</bdi> الإصبع بعد وخز مع <bdi>nail bed</bdi> سليم = <bdi>felon</bdi>.",
    "clues": [
        ("hairdresser", "مهنة تتعامل بأدوات حادة"),
        ("swollen bulb of the thumb finger", "تورم <bdi>pulp</bdi> طرف الإصبع"),
        ("stick from the tools", "إصابة اختراقية (<bdi>puncture</bdi>) تسبب <bdi>felon</bdi>"),
        ("Nail bed is intact", "يستبعد عدوى الـ<bdi>nail</bdi>"),
    ],
    "why_correct": [
        "تورم متوتر بـ<bdi>bulb</bdi> (<bdi>pulp</bdi>) الإصبع بعد وخز (\"a stick from the tools\") مع <bdi>nail bed</bdi> سليم هو <bdi>felon</bdi>: عدوى بحيّز <bdi>pulp</bdi> المقسّم المغلق بالسلامية البعيدة، غالبًا <bdi>Staphylococcus aureus</bdi> من إصابة اختراقية.",
        "الحواجز الداخلية (<bdi>septa</bdi>) تجعلها تجمّع متوتر مؤلم جدًا يحتاج <bdi>incision and drainage</bdi> لو تكوّن <bdi>pus</bdi>.",
    ],
    "when_changes": [
        "لو العدوى حول حافة الظفر بعد قص الزوائد الجلدية، الجواب يتحول لـ<bdi>paronychia</bdi>.",
        "لو فيه <bdi>vesicles</bdi> على الإصبع، الجواب يصير <bdi>herpetic whitlow</bdi> ولا يُفتح جراحيًا.",
    ],
    "rule": "<bdi>pulp</bdi> = <bdi>felon</bdi>، <bdi>nail fold</bdi> = <bdi>paronychia</bdi>، <bdi>vesicles</bdi> = <bdi>herpetic whitlow</bdi> اللي ممنوع فتحه.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0353": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "تورم وألم و<bdi>paresthesia</bdi> بعد كسر الساعد مع نبض سليم = <bdi>compartment syndrome</bdi> لازم <bdi>fasciotomy</bdi>، والنبض السليم لا يستبعدها.",
    "clues": [
        ("distal radius fracture", "سبب <bdi>compartment syndrome</bdi> المحتمل"),
        ("paresthesia of the hand", "علامة مبكرة لنقص تروية العصب"),
    ],
    "why_correct": [
        "بعد كسر الساعد، التورم والألم و<bdi>paresthesia</bdi> باليد تشير لارتفاع ضغط الحيّز مع <bdi>nerve ischemia</bdi>: <bdi>compartment syndrome</bdi>. الألم والـ<bdi>paresthesia</bdi> علامات مبكرة، وفقدان النبض علامة متأخرة جدًا، فـ\"النبض سليم\" لا يستبعد الحالة.",
        "علاج <bdi>compartment syndrome</bdi> هو <bdi>fasciotomy</bdi> عاجل، ويمكن اتخاذ القرار بناء على الشك السريري فقط.",
    ],
    "when_changes": [
        "لو كان التورم بسيط بدون أي علامة عصبية أو حسية، الجواب يصير فقط رفع الطرف ومراقبة.",
        "لو كان هناك جبس ضيق مطبّق، أول خطوة تصير إزالته قبل التفكير بـ<bdi>fasciotomy</bdi> مباشرة.",
    ],
    "rule": "النبض السليم لا يستبعد <bdi>compartment syndrome</bdi>؛ ألم + <bdi>paresthesia</bdi> بعد كسر يكفي لاتخاذ قرار <bdi>fasciotomy</bdi> العاجل.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0354": {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "مريض <bdi>vitally stable</bdi> بألم بطني خفيف متأخر بعد <bdi>trauma</bdi> من غير علامات تحذيرية؛ الخطوة المنطقية هي تصوير غير باضع أولًا قبل التحويل.",
    "clues": [
        ("RTA 1 week ago", "تاريخ <bdi>trauma</bdi> يرفع شك إصابة كبدية متأخرة"),
        ("Vitally stable", "لا توجد علامة طارئة تفرض تحويل فوري"),
    ],
    "why_correct": [
        "بما إن العلامات الحيوية <bdi>مستقرة تمامًا</bdi> وما فيه نتائج أخرى غير طبيعية بالفحص، الخطوة الأولى المنطقية هي عمل <bdi>abdominal ultrasound</bdi> لتقييم الكبد ومنطقة الـ<bdi>RUQ</bdi> واستبعاد تجمع دم أو إصابة محتواة قبل تحويله.",
        "لو ظهر شيء غير طبيعي بالـ<bdi>ultrasound</bdi> أو تغيّرت الحالة، يصير التحويل للطوارئ للتقييم الكامل بالـ<bdi>CT</bdi>.",
    ],
    "when_changes": [
        "لو كانت أي علامة حيوية غير طبيعية (كما بنسخة AS-0354B)، الجواب يتحول مباشرة لـ<bdi>refer to ED</bdi>.",
        "لو ظهر ألم متزايد أو علامات <bdi>peritonism</bdi>، يصير التحويل الفوري هو الأنسب بدل الانتظار لنتيجة <bdi>ultrasound</bdi>.",
    ],
    "rule": "الاستقرار الكامل بالعلامات الحيوية يسمح بتصوير أولي (<bdi>ultrasound</bdi>) بدل تحويل فوري؛ أي شذوذ بالعلامات الحيوية يحوّل القرار مباشرة لـ<bdi>ED referral</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر نفسه غير محدد لهذا السؤال (لا توجد إجابة مؤكدة)، فاخترنا A بالاعتماد على إن النسخة هنا تذكر استقرار العلامات الحيوية صراحة، بعكس نسخة AS-0354B اللي فيها شذوذ بالعلامات الحيوية وإجابتها B.",
},
"AS-0354B": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نفس سيناريو الألم البطني المتأخر بعد <bdi>trauma</bdi>، لكن هنا فيه شذوذ بالعلامات الحيوية، فيتغيّر القرار لتحويل فوري للطوارئ.",
    "clues": [
        ("RTA 1 week ago", "تاريخ <bdi>trauma</bdi> يرفع شك إصابة كبدية متأخرة"),
        ("some vitals were abnormal", "يفرض تحويل فوري بدل تصوير بالعيادة"),
    ],
    "why_correct": [
        "مريض بألم <bdi>RUQ</bdi> بعد <bdi>trauma</bdi> بعيادة خارجية وعلاماته الحيوية <bdi>شاذة</bdi> يرجّح نزف متأخر من إصابة كبدية أو عضو صلب آخر.",
        "يحتاج قدرة على الإنعاش ومراقبة متسلسلة وتقييم شامل (<bdi>CT</bdi> لو استقر)، وهذا متوفر فقط بالطوارئ، فالخطوة الأنسب <bdi>referral to ED</bdi>.",
    ],
    "when_changes": [
        "لو العلامات الحيوية طبيعية تمامًا، الجواب يرجع لتصوير أولي بالعيادة (<bdi>ultrasound</bdi>).",
        "لو المريض بالطوارئ فعلًا و<bdi>unstable</bdi> مع <bdi>FAST</bdi> موجب، الجواب يصير <bdi>laparotomy</bdi>.",
    ],
    "rule": "كلمة \"abnormal\" بالعلامات الحيوية تنقل القرار من تصوير بالعيادة إلى تحويل فوري للطوارئ.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0355": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "مريض <bdi>toxic</bdi> بآفة كيسية جدارها سميك بالكبد = <bdi>pyogenic liver abscess</bdi>، والخطوة الأنسب <bdi>percutaneous drainage</bdi>.",
    "clues": [
        ("febrile, toxic", "صورة <bdi>sepsis</bdi> من مصدر كبدي"),
        ("cystic lesion with thick wall in the liver", "صورة <bdi>abscess</bdi> لا كيس بسيط"),
    ],
    "why_correct": [
        "مريض <bdi>febrile, toxic</bdi> بألم <bdi>RUQ</bdi>، ارتفاع <bdi>WBC</bdi> و<bdi>bilirubin</bdi>، وآفة كيسية جدارها سميك بالكبد يدل على <bdi>liver abscess</bdi>، وبدون تاريخ سفر أو إسهال دموي أو فحص <bdi>amoebic serology</bdi> فالصورة <bdi>pyogenic</bdi>.",
        "علاج <bdi>pyogenic abscess</bdi> هو تصريف الـ<bdi>pus</bdi> مع <bdi>antibiotics</bdi>، والأقل تداخلًا والفعّال هو <bdi>image-guided percutaneous drainage</bdi>.",
    ],
    "when_changes": [
        "لو فيه تاريخ سفر وإسهال دموي وفحص <bdi>Entamoeba</bdi> موجب، الجواب يتحول لـ<bdi>metronidazole</bdi> كعلاج أولي.",
        "لو فشل <bdi>percutaneous drainage</bdi> أو حصل تمزق بالـ<bdi>abscess</bdi>، الجواب يصير <bdi>surgical drainage</bdi>.",
    ],
    "rule": "علامات <bdi>amoebic</bdi> (سفر، إسهال دموي، <bdi>serology</bdi> موجب) = <bdi>metronidazole</bdi> أول حتى لو كبير؛ غياب هذه العلامات مع آفة كبيرة = <bdi>percutaneous drainage</bdi>.",
    "comparison": None,
    "labs": [["Temperature", "~37.9°C", "36.5-37.5°C"]],
    "guideline_note": None,
},
"AS-0369": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>hematemesis</bdi> بعد 24 ساعة من <bdi>PTC</bdi> بمريض <bdi>مستقر</bdi> = <bdi>hemobilia</bdi>، والخطوة التالية <bdi>upper GI endoscopy</bdi> لأنها أول فحص لأي <bdi>hematemesis</bdi>.",
    "clues": [
        ("PTC (percutaneous transhepatic cholangiography)", "إجراء يسبب إصابة وعائية كبدية"),
        ("After 24 hours", "توقيت نموذجي لظهور <bdi>hemobilia</bdi>"),
        ("hematemesis", "عرض النزف من الشجرة الصفراوية"),
        ("vitals are stable", "يسمح بخطوة تشخيصية غير باضعة أولًا"),
    ],
    "why_correct": [
        "<bdi>hematemesis</bdi> بعد 24 ساعة من <bdi>PTC</bdi> يعني <bdi>hemobilia</bdi> لحد ما يُستبعد: الإبرة عبر الكبد تصيب وعاء كبدي والدم ينزل بالقناة الصفراوية للعفج.",
        "بما إن المريض <bdi>مستقر</bdi>، الخطوة التالية هي <bdi>upper GI endoscopy</bdi>: أول فحص لأي <bdi>hematemesis</bdi>، يستبعد أسباب أخرى (قرحة، دوالي) وممكن يُظهر دم من <bdi>ampulla of Vater</bdi> يؤكد المصدر الصفراوي.",
    ],
    "when_changes": [
        "لو المريض <bdi>unstable</bdi> أو النزف مستمر أو الـ<bdi>endoscopy</bdi> أكّدت مصدر صفراوي، الجواب يتحول لـ<bdi>angiography</bdi> مع <bdi>embolization</bdi>.",
        "لو <bdi>Hb</bdi> منخفض بشكل واضح والعلامات الحيوية حدّية، الجواب المباشر يصير <bdi>angiography</bdi> (كما بـ AS-0370).",
    ],
    "rule": "نزف بعد إجراء كبدي صفراوي (<bdi>PTC</bdi>، <bdi>biopsy</bdi>، <bdi>TIPS</bdi>) = فكّر <bdi>hemobilia</bdi>؛ مستقر = <bdi>endoscopy</bdi> أول؛ <bdi>gold standard</bdi> للتشخيص والعلاج = <bdi>angiography with embolization</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر نفسه فيه تردد (علّم الإجابة تحتاج تصحيح وذكر إجابة مرجع آخر D)، لكن نلتزم بـ<bdi>answer_letter</bdi> المعطى B لأن المريض هنا مستقر، بعكس AS-0370 اللي فيه Hb منخفض وعلامات حيوية حدّية وإجابته D.",
},
"AS-0370": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "<bdi>upper GI bleeding</bdi> بعد <bdi>PTC</bdi> مع <bdi>Hb</bdi> منخفض وعلامات حيوية حدّية = <bdi>hemobilia</bdi> يحتاج التشخيص والعلاج النهائي مباشرة بـ<bdi>angiography</bdi>.",
    "clues": [
        ("percutaneous trans-hepatic cholangiography", "إجراء يسبب إصابة وعائية كبدية"),
        ("24 hours after the procedure", "توقيت نموذجي لـ<bdi>hemobilia</bdi>"),
        ("upper gastrointestinal bleeding", "عرض النزف الصفراوي"),
    ],
    "why_correct": [
        "نزف هضمي علوي بعد 24 ساعة من <bdi>PTC</bdi> هو <bdi>hemobilia</bdi>: الإجراء يصيب شريان داخل الكبد (غالبًا <bdi>pseudoaneurysm</bdi>) ينزف داخل الشجرة الصفراوية.",
        "<bdi>angiography</bdi> هو <bdi>gold standard</bdi> لتحديد موقع النزف ويسمح بـ<bdi>transarterial embolization</bdi> بنفس الجلسة؛ انخفاض <bdi>Hb</bdi> وارتفاع <bdi>RR</bdi> وضغط حدّي يدعمون التوجه المباشر للفحص التشخيصي والعلاجي النهائي.",
    ],
    "when_changes": [
        "لو المريض مستقر تمامًا بدون انخفاض واضح بالـ<bdi>Hb</bdi>، الخطوة الأولى تصير <bdi>upper GI endoscopy</bdi> (كما بـ AS-0369).",
        "لو الـ<bdi>CT angiography</bdi> أظهرت <bdi>pseudoaneurysm</bdi> بوضوح وفيه تأخير بالوصول للـ<bdi>angiography</bdi> التداخلية، ممكن تُستخدم كخطوة توضيحية وسيطة فقط لا علاجية.",
    ],
    "rule": "نزف هضمي علوي بعد إجراء كبدي صفراوي مع <bdi>Hb</bdi> منخفض وعلامات حيوية حدّية = اذهب مباشرة لـ<bdi>angiography</bdi> (تشخيص وعلاج بجلسة واحدة).",
    "comparison": None,
    "labs": [["Hemoglobin", "103 g/L", "120-160 g/L (female) / 130-170 g/L (male)"], ["BP", "105/62 mmHg", "90-120/60-80 mmHg"], ["HR", "89/min", "60-100/min"], ["RR", "22/min", "12-20/min"], ["O2 sat", "94%", "≥95%"]],
    "guideline_note": None,
},
"AS-0371": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "مريض سكري بعدوى سنّية ثم يرقان وقشعريرة مع آفة كبدية 6 سم = <bdi>pyogenic liver abscess</bdi> كبير يحتاج <bdi>drainage</bdi>.",
    "clues": [
        ("DM", "عامل خطر للعدوى والـ<bdi>abscess</bdi>"),
        ("dental infection", "مصدر <bdi>bacteremia</bdi>"),
        ("6 cm hypoechoic lesion in the liver", "<bdi>abscess</bdi> كبير يحتاج <bdi>drainage</bdi>"),
    ],
    "why_correct": [
        "مريض <bdi>diabetic</bdi> بعدوى سنّية ثم قشعريرة ويرقان مع آفة كبدية 6 سم <bdi>hypoechoic</bdi> هو <bdi>pyogenic liver abscess</bdi> من انتشار دموي لفلورا الفم.",
        "الـ<bdi>abscess</bdi> الكبير يحتاج ضبط المصدر: <bdi>image-guided percutaneous drainage</bdi> مع <bdi>IV broad-spectrum antibiotics</bdi>، وهذا الـ<bdi>management</bdi> المبدئي الأنسب.",
    ],
    "when_changes": [
        "لو الآفة صغيرة (أقل من 3 سم تقريبًا)، تكفي <bdi>IV antibiotics</bdi> لوحدها.",
        "لو السيناريو فيه نيوتروبينيا وآفات متعددة صغيرة، الجواب يتحول لـ<bdi>antifungal therapy</bdi> لاحتمال <bdi>hepatosplenic candidiasis</bdi>.",
    ],
    "rule": "مصدر بكتيري (أسنان، صفراوي) + <bdi>abscess</bdi> كبير = <bdi>drainage</bdi>؛ سفر وإسهال = <bdi>metronidazole</bdi> لوحده.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0372": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "ضيق تنفس متأخر بعد <bdi>MVA</bdi> مع أصوات تنفس منخفضة و<bdi>dullness</bdi> بالقرع وهبوط ضغط = <bdi>hemothorax</bdi> متأخر.",
    "clues": [
        ("decreased breath sounds and dullness on percussion", "دليل على سائل (دم) بالجوف الجنبي"),
        ("hypotensive", "فقدان دم مستمر"),
    ],
    "why_correct": [
        "بعد <bdi>MVA</bdi>، ضيق تنفس مع أصوات تنفس منخفضة و<bdi>dullness</bdi> بالقرع على جهة واحدة مع هبوط ضغط يعني سائل (دم) بالجوف الجنبي مع فقدان دم: <bdi>hemothorax</bdi>.",
        "الظهور المتأخر بعد استقرار مبدئي معروف لأن النزف البطيء من أضلاع مكسورة أو أوعية بين الأضلاع يتراكم تدريجيًا بالصدر.",
    ],
    "when_changes": [
        "لو كان القرع <bdi>hyperresonant</bdi> مع انحراف القصبة وانتفاخ أوردة رقبية، الجواب يتحول لـ<bdi>tension pneumothorax</bdi>.",
        "لو الأصوات متساوية الجانبين مع انتفاخ أوردة رقبية وأصوات قلب مكتومة، الجواب يصير <bdi>cardiac tamponade</bdi>.",
    ],
    "rule": "<bdi>dull</bdi> = دم (<bdi>hemothorax</bdi>)، <bdi>hyperresonant</bdi> = هواء (<bdi>tension pneumothorax</bdi>)؛ كلمة القرع هي الفيصل بينهم.",
    "comparison": {
        "headers": ["الحالة", "القرع", "أصوات التنفس", "أوردة الرقبة"],
        "rows": [
            ["Hemothorax", "<bdi>dull</bdi>", "منخفضة جهة واحدة", "طبيعية/منخفضة"],
            ["Tension pneumothorax", "<bdi>hyperresonant</bdi>", "منخفضة جهة واحدة", "منتفخة + انحراف قصبة"],
            ["Cardiac tamponade", "طبيعي", "متساوية الجانبين", "منتفخة + أصوات قلب مكتومة"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},
"AS-0373": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "نفس سيناريو <bdi>severe hypercalcemia</bdi> من <bdi>PHPT</bdi>، والسؤال يحدد \"NEXT step\" فيكون ضبط الـ<bdi>calcium</bdi> الحاد أول.",
    "clues": [
        ("recurrent ureteric stones and bone pain", "أعراض <bdi>PHPT</bdi> المزمنة"),
        ("Ca: 3.50 mmol", "<bdi>severe hypercalcemia</bdi> تحتاج ضبط فوري"),
        ("2 cm parathyroid adenoma", "سبب <bdi>PHPT</bdi> المؤكد"),
    ],
    "why_correct": [
        "كلمة \"NEXT step\" بالسؤال توجّه للخطوة الفورية: <bdi>calcium</bdi> عند 3.50 <bdi>mmol/L</bdi> مرتفع بشدة ويحتاج تخفيض سريع.",
        "ترتيب الخطوات بـ<bdi>severe hypercalcemia</bdi>: <bdi>IV normal saline</bdi> أولًا، ثم <bdi>calcitonin</bdi> (أسرع)، ثم <bdi>IV bisphosphonate</bdi> (أبطأ وأطول مفعولًا)؛ إذا <bdi>bisphosphonate</bdi> هو الخيار المطروح يُعتبر الخطوة التالية المناسبة بعد الترطيب.",
    ],
    "when_changes": [
        "لو السؤال قال \"most appropriate management\" بدون التركيز على خطوة فورية، الجواب يتحول لـ<bdi>parathyroidectomy</bdi>.",
        "لو كان خيار <bdi>IV fluids</bdi> أو <bdi>calcitonin</bdi> مطروح، يسبق <bdi>bisphosphonate</bdi> بالترتيب الزمني.",
    ],
    "rule": "\"most appropriate\" = <bdi>parathyroidectomy</bdi>؛ \"NEXT step\" مع <bdi>calcium</bdi> شديد الارتفاع = خفضه أولًا (<bdi>fluids</bdi> ثم <bdi>bisphosphonate</bdi> أو <bdi>calcitonin</bdi>).",
    "comparison": None,
    "labs": [["Calcium", "3.50 mmol/L", "2.1-2.6 mmol/L"]],
    "guideline_note": None,
},
"AS-0375": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "<bdi>diverticulosis</bdi> بألم خفيف متقطع بدون أي علامة التهاب = <bdi>uncomplicated disease</bdi> يُدار بالغذاء مو بالتصوير أو المضادات.",
    "clues": [
        ("diverticulosis", "حالة معروفة مسبقًا، مو حدث جديد"),
        ("mild and intermittent pain", "لا يوجد التهاب حاد (<bdi>diverticulitis</bdi>)"),
    ],
    "why_correct": [
        "<bdi>diverticulosis</bdi> معروفة مع ألم <bdi>mild</bdi> و<bdi>intermittent</bdi> بالـ<bdi>LLQ</bdi> وبدون أي علامة التهاب هي <bdi>symptomatic uncomplicated diverticular disease</bdi>، مو <bdi>diverticulitis</bdi>.",
        "الـ<bdi>management</bdi> سرّي خارج المستشفى: <bdi>high-fiber diet</bdi> مع سوائل كافية تلين البراز وتخفف الضغط داخل القولون، وهذا يقلل الأعراض ونوبات المستقبل.",
    ],
    "when_changes": [
        "لو ظهرت حمى أو ارتفاع <bdi>WBC</bdi> أو ألم ثابت مستمر، الجواب يتحول لـ<bdi>CT abdomen</bdi> للشك بـ<bdi>diverticulitis</bdi>.",
        "لو تأكد <bdi>complicated diverticulitis</bdi> (خراج، تسمم جهازي)، الجواب يصير <bdi>IV antibiotics</bdi>.",
    ],
    "rule": "حمى أو ارتفاع <bdi>WBC</bdi> أو ألم ثابت موضعي يحوّل <bdi>diverticulosis</bdi> إلى <bdi>diverticulitis</bdi> وينقل الجواب لـ<bdi>CT</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0376": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "نفس مبدأ <bdi>uncomplicated diverticular disease</bdi>، هنا السؤال يصرّح بغياب كل علامات <bdi>diverticulitis</bdi> بوضوح.",
    "clues": [
        ("diverticulosis", "حالة معروفة مسبقًا"),
        ("no fever, normal WBCs and no signs of peritonitis", "يستبعد <bdi>diverticulitis</bdi> بشكل مباشر"),
    ],
    "why_correct": [
        "السؤال يشيل كل علامات <bdi>diverticulitis</bdi>: لا حمى، <bdi>WBC</bdi> طبيعي، لا علامات <bdi>peritonitis</bdi>، والألم <bdi>mild</bdi> ومتقطع.",
        "هذا <bdi>uncomplicated diverticular disease</bdi>، والـ<bdi>management</bdi> المبدئي الأنسب هو زيادة الألياف والسوائل لتلطيف البراز وخفض ضغط القولون.",
    ],
    "when_changes": [
        "لو ظهرت حمى أو ارتفاع <bdi>WBC</bdi> أو ألم موضعي ثابت، الجواب يتحول لـ<bdi>CT abdomen</bdi>.",
        "لو تأكد خراج أو تسمم جهازي، الجواب يصير <bdi>IV antibiotics</bdi> وراحة الأمعاء.",
    ],
    "rule": "غياب الحمى وطبيعية <bdi>WBC</bdi> وغياب <bdi>peritonism</bdi> تؤكد <bdi>diverticulosis</bdi> لا <bdi>diverticulitis</bdi>؛ العلاج غذائي فقط، لا تصوير ولا مضادات.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
"AS-0312": {
    "A": "<bdi>surgical repair</bdi> يصير صحيح لو زادت الأعراض (ألم يحدّ النشاط) أو كبرت الـ<bdi>hernia</bdi> أو صارت <bdi>irreducible</bdi>؛ مجرد <bdi>discomfort</bdi> خفيف لا يفرضها.",
    "B": "<bdi>lifestyle modification</bdi> نصيحة عامة (تخفيف وزن، تجنب الشد) ممكن تصاحب المتابعة، لكنها ليست خطة علاج للـ<bdi>hernia</bdi> نفسها.",
    "C": "<bdi>activity modification</bdi> لا تعالج أو تراقب الـ<bdi>hernia</bdi>؛ تقييد النشاط غير مطلوب وتناسب فقط كنصيحة مساعدة لا كخطة مختارة.",
},
"AS-0332": {
    "A": "<bdi>shunt</bdi> (<bdi>ventriculoperitoneal</bdi>) يعالج <bdi>hydrocephalus</bdi>؛ لا يزيل تجمع دم خارج الجافية يضغط على الدماغ.",
    "C": "<bdi>mannitol</bdi> إجراء مؤقت لتخفيض الضغط داخل الجمجمة بانتظار ترتيب الجراحة؛ لا يوقف النزف الشرياني ولا يزيل الـ<bdi>hematoma</bdi>.",
    "D": "<bdi>intubation</bdi> يحمي مجرى الهواء لو <bdi>GCS</bdi> ≤8 ويكون جزء من إنعاش <bdi>ABC</bdi>، لكنه إجراء داعم؛ السؤال يسأل عن علاج الآفة نفسها وهو الإخراج الجراحي.",
},
"AS-0334": {
    "B": "<bdi>cardiac contusion</bdi> تظهر باضطراب نظم أو تغيّرات <bdi>ECG</bdi> جديدة أو هبوط ضغط بعد ضربة على عظم القص؛ لا تسبب حركة جدار صدر <bdi>paradoxical</bdi>.",
},
"AS-0344": {
    "B": "<bdi>paronychia</bdi> عدوى الـ<bdi>nail fold</bdi> عند حافة أو قاعدة الظفر، نموذجيًا بعد قضم الأظافر أو المانيكير؛ هنا منطقة الظفر سليمة والـ<bdi>pulp</bdi> هو المصاب.",
    "C": "<bdi>onychomycosis</bdi> عدوى فطرية مزمنة تسبب ظفر سميك متغيّر اللون ومتفتت، مو تورم حاد مؤلم بالـ<bdi>pulp</bdi> بعد وخز.",
    "D": "<bdi>cellulitis</bdi> احمرار منتشر غير محدد بالجلد والنسيج تحته بدون تجمع متوتر محدد؛ التورم الموضعي المتوتر هنا يدل على <bdi>felon</bdi>.",
},
"AS-0353": {
    "B": "<bdi>elevation of the hand</bdi> تناسب كسر متورم بدون علامات عصبية وعائية؛ بالاشتباه بـ<bdi>compartment syndrome</bdi> الرفع يخفض ضغط التروية الشريانية، فيبقى الطرف بمستوى القلب مع التحرير الجراحي.",
},
"AS-0354": {
    "B": "<bdi>referral to ED</bdi> يناسب وجود شذوذ بالعلامات الحيوية أو تدهور الحالة؛ هنا المريض <bdi>vitally stable</bdi> تمامًا فلا حاجة ملحّة للتحويل الفوري قبل تصوير أولي.",
    "C": "فحوصات الدم لا تستبعد النزف الداخلي لأن <bdi>Hb</bdi> قد يكون طبيعي مبكرًا، وهي خطوة مساعدة لا بديل عن تصوير أو تحويل عند الحاجة.",
},
"AS-0354B": {
    "A": "<bdi>abdominal ultrasound</bdi> خيار مقبول فقط بمريض مستقر تمامًا بعلامات حيوية طبيعية؛ هنا وجود علامات حيوية شاذة يجعل تأخير التحويل خطر.",
    "C": "فحوصات الدم لا تستبعد النزف الحاد لأن <bdi>Hb</bdi> يبقى طبيعي مبكرًا؛ هي إجراء مساعد يتم بالطوارئ لا بديل عن التحويل.",
},
"AS-0355": {
    "A": "<bdi>ceftriaxone</bdi> (مضاد حيوي) يُعطى مع التصريف لكن لوحده نادرًا يشفي <bdi>pyogenic abscess</bdi> متكوّن بمريض <bdi>toxic</bdi>؛ لوحده يناسب فقط آفات صغيرة جدًا.",
    "B": "<bdi>metronidazole</bdi> علاج أولي لو كانت الصورة <bdi>amoebic</bdi> (سفر، إسهال دموي، <bdi>serology</bdi> موجب)؛ هذه القرائن غير موجودة هنا.",
    "C": "<bdi>surgical drainage</bdi> يُحجز لفشل أو استحالة <bdi>percutaneous drainage</bdi>، أو تمزق مع التهاب بريتوني؛ أكثر تداخلًا من اللازم كخطوة أولى.",
},
"AS-0369": {
    "A": "<bdi>CT abdomen</bdi> (<bdi>CT angiography</bdi>) ممكن يرجّح <bdi>pseudoaneurysm</bdi> لكنه ليس أول فحص للـ<bdi>hematemesis</bdi> ولا يعالج النزف.",
    "C": "<bdi>US</bdi> ممكن يُظهر تجلط بالقنوات الصفراوية لكن حساسيته ضعيفة لتحديد الوعاء الناز ولا يوقف النزف؛ ليس طريقة تقييم <bdi>hematemesis</bdi> المعيارية.",
    "D": "<bdi>angiography</bdi> هي <bdi>gold standard</bdi> لتشخيص وعلاج <bdi>hemobilia</bdi> بآن واحد، لكنها تصير الجواب عند عدم استقرار المريض أو استمرار النزف أو تأكيد المصدر الصفراوي بالـ<bdi>endoscopy</bdi> أولًا؛ هنا المريض مستقر فتبدأ بالـ<bdi>endoscopy</bdi>.",
},
"AS-0370": {
    "A": "<bdi>CT scan</bdi> ممكن يرجّح <bdi>pseudoaneurysm</bdi> لكنه ليس <bdi>gold standard</bdi> ولا يعالج؛ <bdi>angiography</bdi> التقليدية تجمع الاثنين.",
    "B": "<bdi>endoscopy</bdi> ممكن تُظهر دم من <bdi>ampulla</bdi> لكنها لا تحدد أو تعالج مصدر شرياني داخل الكبد؛ تناسب النزف الهضمي العلوي العادي بدون إجراء كبدي سابق.",
    "C": "<bdi>ultrasound</bdi> ممكن يُظهر تجلط بالقنوات الصفراوية لكنه لا يحدد أو يعالج الوعاء الناز.",
},
"AS-0371": {
    "A": "<bdi>oral antibiotics</bdi> لا تخترق تجمعًا كبيرًا محاطًا بجدار وغير كافية لمريض <bdi>septic</bdi>؛ <bdi>antibiotics</bdi> لوحدها (<bdi>IV</bdi>) تناسب آفات صغيرة، والـ<bdi>amoebic abscess</bdi> يُعالج بـ<bdi>metronidazole</bdi> بدون تصريف.",
    "C": "<bdi>antifungals</bdi> تناسب <bdi>hepatosplenic candidiasis</bdi> بمرضى <bdi>neutropenic</bdi> (آفات متعددة صغيرة)، مو آفة واحدة كبيرة بعد مصدر سنّي.",
},
"AS-0372": {
    "B": "<bdi>tension pneumothorax</bdi> يعطي أيضًا غياب أصوات تنفس وهبوط ضغط، لكنه <bdi>hyperresonant</bdi> بالقرع مع انحراف القصبة وانتفاخ أوردة رقبية، ويتطور بسرعة لا تدريجيًا.",
    "C": "<bdi>pulmonary contusion</bdi> يسبب نقص أكسجين مع ارتشاحات متقطعة بدون <bdi>dullness</bdi> أو تجمع سائل موضعي؛ <bdi>cardiac contusion</bdi> يسبب اضطراب نظم لا علامات صدرية جانبية.",
    "D": "<bdi>cardiac tamponade</bdi> يعطي هبوط ضغط وانتفاخ أوردة رقبية وأصوات قلب مكتومة مع أصوات تنفس متساوية الجانبين (<bdi>Beck triad</bdi>)، لا <bdi>dullness</bdi> جهة واحدة.",
},
"AS-0373": {
    "B": "<bdi>calcimimetics</bdi> (<bdi>cinacalcet</bdi>) تناسب مريض غير مؤهل أو يرفض الجراحة، أو <bdi>parathyroid carcinoma</bdi>؛ ليست الخطوة التالية بمريض مرشّح جراحي وبارتفاع حاد بالـ<bdi>calcium</bdi>.",
    "C": "زيادة <bdi>calcium</bdi> بالغذاء تزيد سوء <bdi>hypercalcemia</bdi> وتكوّن الحصوات؛ خطأ تمامًا هنا.",
    "D": "<bdi>parathyroidectomy</bdi> هي العلاج النهائي المناسب لو السؤال سأل \"most appropriate\"، لكن مع \"NEXT step\" وارتفاع حاد بالـ<bdi>calcium</bdi> تسبقها خطوة ضبط الـ<bdi>calcium</bdi>.",
},
"AS-0375": {
    "A": "<bdi>CT abdomen</bdi> مناسب عند الشك بـ<bdi>diverticulitis</bdi> (ألم ثابت، حمى، ارتفاع <bdi>WBC</bdi>، حساسية موضعية) للتدريج والبحث عن خراج أو ثقب؛ الألم الخفيف المتقطع هنا لا يحتاجه.",
    "B": "<bdi>IV antibiotics</bdi> تناسب <bdi>diverticulitis</bdi> المعقدة أو الشديدة (خراج، مرض جهازي، عدم تحمل الفم عن طريق الفم)؛ لا عدوى هنا.",
},
"AS-0376": {
    "A": "<bdi>CT abdomen</bdi> هو فحص الاشتباه بـ<bdi>acute diverticulitis</bdi> (حمى، ارتفاع <bdi>WBC</bdi>، حساسية موضعية)؛ لا شيء من هذا موجود هنا.",
    "B": "<bdi>IV antibiotics and bowel rest</bdi> تناسب <bdi>diverticulitis</bdi> المعقدة أو الشديدة (خراج، تسمم جهازي، عدم تحمل الفم)، لا <bdi>diverticulosis</bdi> غير ملتهبة.",
    "D": "<bdi>laparotomy</bdi> تُحجز لثقب مع التهاب بريتوني منتشر أو فشل العلاج المحافظ؛ البطن هنا رخو بلا علامات التهاب.",
},
})

HIGHLIGHT_TERMS.update({
"AS-0312": ["reducible inguinal hernia", "mild discomfort without significant pain"],
"AS-0332": ["lucid interval", "convex lesion"],
"AS-0334": ["Paradoxical chest wall movement"],
"AS-0344": ["hairdresser", "swollen bulb of the thumb finger", "stick from the tools", "Nail bed is intact"],
"AS-0353": ["distal radius fracture", "paresthesia of the hand"],
"AS-0354": ["RTA 1 week ago", "Vitally stable"],
"AS-0354B": ["RTA 1 week ago", "some vitals were abnormal"],
"AS-0355": ["febrile, toxic", "cystic lesion with thick wall in the liver"],
"AS-0369": ["PTC (percutaneous transhepatic cholangiography)", "After 24 hours", "hematemesis", "vitals are stable"],
"AS-0370": ["percutaneous trans-hepatic cholangiography", "24 hours after the procedure", "upper gastrointestinal bleeding"],
"AS-0371": ["DM", "dental infection", "6 cm hypoechoic lesion in the liver"],
"AS-0372": ["decreased breath sounds and dullness on percussion", "hypotensive"],
"AS-0373": ["recurrent ureteric stones and bone pain", "Ca: 3.50 mmol", "2 cm parathyroid adenoma"],
"AS-0375": ["diverticulosis", "mild and intermittent pain"],
"AS-0376": ["diverticulosis", "no fever, normal WBCs and no signs of peritonitis"],
})
