# -*- coding: utf-8 -*-
# Explanations for questions 014-110 (topic: mostly Infectious Diseases / Respiratory Medicine)

TOPICS = {
14: "Infectious Diseases",
15: "Infectious Diseases",
16: "Infectious Diseases",
17: "Infectious Diseases",
18: "Infectious Diseases",
19: "Infectious Diseases",
20: "Infectious Diseases",
21: "Infectious Diseases",
22: "Infectious Diseases",
23: "Infectious Diseases",
24: "Infectious Diseases",
25: "Infectious Diseases",
26: "Infectious Diseases",
27: "Infectious Diseases",
28: "Infectious Diseases",
29: "Infectious Diseases",
30: "Infectious Diseases",
31: "Infectious Diseases",
32: "Infectious Diseases",
33: "Infectious Diseases",
34: "Infectious Diseases",
35: "Infectious Diseases",
36: "Infectious Diseases",
37: "Infectious Diseases",
38: "Infectious Diseases",
39: "Infectious Diseases",
40: "Infectious Diseases",
41: "Infectious Diseases",
42: "Infectious Diseases",
43: "Infectious Diseases",
44: "Infectious Diseases",
45: "Infectious Diseases",
46: "Infectious Diseases",
47: "Infectious Diseases",
48: "Infectious Diseases",
49: "Infectious Diseases",
50: "Infectious Diseases",
51: "Infectious Diseases",
52: "Infectious Diseases",
53: "Infectious Diseases",
54: "Infectious Diseases",
55: "Infectious Diseases",
56: "Infectious Diseases",
57: "Respiratory Medicine",
58: "Infectious Diseases",
59: "Infectious Diseases",
60: "Infectious Diseases",
61: "Respiratory Medicine",
62: "Respiratory Medicine",
63: "Respiratory Medicine",
64: "Infectious Diseases",
65: "Infectious Diseases",
66: "Infectious Diseases",
67: "Infectious Diseases",
68: "Infectious Diseases",
69: "Infectious Diseases",
70: "Infectious Diseases",
71: "Dermatology",
72: "Dermatology",
73: "Infectious Diseases",
74: "Musculoskeletal & Orthopedics",
75: "Infectious Diseases",
76: "Infectious Diseases",
77: "Infectious Diseases",
78: "Infectious Diseases",
79: "Infectious Diseases",
80: "Infectious Diseases",
81: "Infectious Diseases",
82: "Infectious Diseases",
83: "Infectious Diseases",
84: "Infectious Diseases",
85: "Infectious Diseases",
86: "Urology",
87: "Obstetrics & Gynecology",
88: "Urology",
89: "Urology",
90: "Urology",
91: "Infectious Diseases",
92: "Infectious Diseases",
93: "Obstetrics & Gynecology",
94: "Nephrology",
95: "Respiratory Medicine",
96: "Respiratory Medicine",
97: "Respiratory Medicine",
98: "Respiratory Medicine",
99: "Respiratory Medicine",
100: "Respiratory Medicine",
101: "Respiratory Medicine",
102: "Infectious Diseases",
103: "Respiratory Medicine",
104: "Respiratory Medicine",
105: "Respiratory Medicine",
106: "Respiratory Medicine",
107: "Respiratory Medicine",
108: "Respiratory Medicine",
109: "Respiratory Medicine",
110: "Respiratory Medicine",
}

EXPLANATIONS = {}
WHY_WRONG = {}
HIGHLIGHT_TERMS = {}

EXPLANATIONS[14] = {
    "idea": "السؤال يبي تحديد <bdi>cause</bdi> <bdi>meningitis</bdi> بالاعتماد على صورة تحليل السائل الشوكي (<bdi>CSF</bdi>) الكلاسيكية.",
    "clues": [
        ("Appearance cloudy", "عكارة السائل الشوكي توحي بالتهاب صديدي بكتيري"),
        ("Glucose low", "البكتيريا تستهلك الجلوكوز فينخفض بالسائل الشوكي"),
        ("Protein high", "بروتين <bdi>elevated</bdi> يدل على التهاب <bdi>severe</bdi>"),
        ("White cells 100 /mm3 (70% polymorphs)", "غلبة العدلات (polymorphs) نموذجية للالتهاب البكتيري الـ<bdi>acute</bdi>"),
    ],
    "why_correct": [
        "صورة السائل الشوكي هنا (عكر، جلوكوز <bdi>low</bdi>، بروتين <bdi>elevated</bdi>، وغلبة عدلات) كلاسيكية تمامًا لالتهاب سحايا بكتيري <bdi>acute</bdi>.",
        "الالتهاب السلي أو الفطري (<bdi>Cryptococcal</bdi>) يعطي غلبة لمفاويات مع مسار أبطأ، مو غلبة عدلات بهالشكل الـ<bdi>acute</bdi>.",
        "الالتهاب الفيروسي يعطي سائل صافٍ أو <bdi>mild</bdi> العكارة مع جلوكوز <bdi>normal</bdi> غالبًا، وهذا يخالف الصورة هنا تمامًا.",
    ],
    "when_changes": [
        "لو كانت الغلبة لمفاوية مع بروتين <bdi>elevated</bdi> جدًا ومسار <bdi>chronic</bdi> (أسابيع)، يتغيّر الـ<bdi>diagnosis</bdi> إلى التهاب سحايا سلي.",
        "لو الجلوكوز <bdi>normal</bdi> والخلايا لمفاوية بعدد أقل مع مسار أخف، يتجه الـ<bdi>diagnosis</bdi> للفيروسي.",
    ],
    "rule": "عكارة السائل الشوكي مع جلوكوز <bdi>low</bdi> وبروتين <bdi>elevated</bdi> وغلبة عدلات يعني التهاب سحايا بكتيري حتى يثبت العكس.",
    "comparison": {
        "headers": ["الـ<bdi>cause</bdi>", "الخلايا الغالبة", "الجلوكوز"],
        "rows": [
            ["<bdi>Bacterial</bdi>", "عدلات (polymorphs)", "<bdi>low</bdi> جدًا"],
            ["<bdi>Tuberculous</bdi>", "لمفاويات", "<bdi>low</bdi> تدريجيًا"],
            ["<bdi>Viral</bdi>", "لمفاويات", "<bdi>normal</bdi> غالبًا"],
            ["<bdi>Cryptococcal</bdi>", "لمفاويات", "<bdi>low</bdi>"],
        ],
    },
    "guideline_note": None,
}
WHY_WRONG[14] = {
    "A": "الكريبتوكوكال يعطي غلبة لمفاويات ومسار أبطأ عادة عند ضعف المناعة، مو غلبة عدلات <bdi>acute</bdi>.",
    "B": "السلي يعطي مسار <bdi>chronic</bdi> وغلبة لمفاويات، وهذا مختلف عن غلبة العدلات الـ<bdi>acute</bdi> هنا.",
    "D": "الفيروسي يعطي سائل أوضح وجلوكوز <bdi>normal</bdi> غالبًا، وهذا يخالف الجلوكوز الـ<bdi>low</bdi> هنا.",
}
HIGHLIGHT_TERMS[14] = ["cloudy", "Glucose low", "Protein high", "100 /mm3 (70% polymorphs)"]

EXPLANATIONS[15] = {
    "idea": "السؤال يبي <bdi>diagnosis</bdi> <bdi>meningitis</bdi> اعتمادًا على مسار <bdi>chronic</bdi> (شهر كامل من الحمى) وصورة سائل شوكي فيها غلبة لمفاويات مع بروتين <bdi>elevated</bdi> جدًا، وهذي صورة توحي ب<bdi>tuberculosis</bdi>.",
    "clues": [
        ("history of fever for the preceding month", "مسار <bdi>chronic</bdi> يميل لل<bdi>tuberculosis</bdi> مو للالتهاب البكتيري الـ<bdi>acute</bdi>"),
        ("Cells 240", "زيادة خلايا واضحة بالسائل الشوكي"),
        ("Total protein 3.6", "ارتفاع <bdi>severe</bdi> جدًا بالبروتين يدعم <bdi>tuberculosis</bdi>"),
        ("Lymphocytes 73", "غلبة لمفاويات، نموذجية لل<bdi>tuberculosis</bdi>"),
    ],
    "why_correct": [
        "شهر كامل من الحمى قبل ظهور <bdi>symptoms</bdi> السحايا مسار <bdi>chronic</bdi> يميل بقوة لالتهاب سحايا سلي مو بكتيري <bdi>acute</bdi>.",
        "غلبة اللمفاويات (73%) مع بروتين <bdi>elevated</bdi> جدًا (3.6 مقابل الـ<bdi>normal</bdi> 0.22-0.33 g/L) صورة كلاسيكية لل<bdi>tuberculosis</bdi>، والإنتان (<bdi>Septicemia</bdi>) ما يفسر هالتغيرات النوعية بالسائل الشوكي.",
        "الالتهاب الفيروسي عادة مسار أقصر وبروتين أقل ارتفاعًا من المذكور هنا بكثير.",
    ],
    "when_changes": [
        "لو المسار كان أيام قليلة بس مع غلبة عدلات بالسائل الشوكي، يتجه الـ<bdi>diagnosis</bdi> للبكتيري الـ<bdi>acute</bdi>.",
        "لو الجلوكوز <bdi>normal</bdi> تمامًا والبروتين <bdi>elevated</bdi> بشكل <bdi>mild</bdi> فقط، يميل الـ<bdi>diagnosis</bdi> للفيروسي.",
    ],
    "rule": "حمى <bdi>chronic</bdi> تمتد لأسابيع مع غلبة لمفاويات وبروتين <bdi>severe</bdi> الارتفاع بالسائل الشوكي توجّه لالتهاب سحايا سلي.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[15] = {
    "A": "الإنتان (<bdi>Septicemia</bdi>) وحده ما يفسر التغيرات النوعية المذكورة بالسائل الشوكي.",
    "C": "هذا الخيار مو كيان مرضي معروف يطابق صورة السائل الشوكي هنا.",
    "D": "الفيروسي عادة مسار أقصر وبروتين أقل ارتفاعًا من المستوى المذكور بكثير.",
}
HIGHLIGHT_TERMS[15] = ["history of fever for the", "Cells 240", "Total protein 3.6", "Lymphocytes 73"]

EXPLANATIONS[16] = {
    "idea": "السؤال يبي تحديد <bdi>cause</bdi> تسمم غذائي بدأ بسرعة <bdi>severe</bdi> (خلال 4 ساعات) بعد أكل لحم، وهذا يوجه لسم جاهز الصنع مو عدوى تحتاج فترة حضانة أطول.",
    "clues": [
        ("vomiting, profuse<br>watery diarrhea", "<bdi>symptoms</bdi> تسمم غذائي <bdi>acute</bdi>"),
        ("within 4 hours of eating", "فترة حضانة قصيرة جدًا توحي بسم جاهز مو بكتيريا تتكاثر بالأمعاء"),
    ],
    "why_correct": [
        "<bdi>Staphylococcus aureus</bdi> يفرز سم معوي جاهز بالطعام قبل الأكل، فتظهر الـ<bdi>symptoms</bdi> بسرعة <bdi>severe</bdi> (2-6 ساعات) وهذا يطابق الوصف تمامًا.",
        "<bdi>Salmonella</bdi> و<bdi>Campylobacter</bdi> و<bdi>E. coli</bdi> يحتاجون فترة حضانة أطول (12 ساعة إلى عدة أيام) لأن الـ<bdi>disease</bdi> يحتاج تكاثر الجرثومة بالأمعاء أول.",
        "التقيؤ الـ<bdi>severe</bdi> المصاحب من أبرز <bdi>signs</bdi> التسمم بسم <bdi>Staph aureus</bdi> الجاهز.",
    ],
    "when_changes": [
        "لو الـ<bdi>symptoms</bdi> بدأت بعد 12-24 ساعة مع إسهال دموي، يميل الـ<bdi>cause</bdi> لـ <bdi>Salmonella</bdi> أو <bdi>Campylobacter</bdi>.",
        "لو الحضانة كانت أيام مع إسهال مائي غزير بدون دم، يفكر بـ <bdi>E. coli</bdi>.",
    ],
    "rule": "فترة حضانة قصيرة جدًا (ساعات قليلة) بعد الأكل مع تقيؤ <bdi>severe</bdi> توجّه لسم <bdi>Staphylococcus aureus</bdi> الجاهز.",
    "comparison": {
        "headers": ["الجرثومة", "فترة الحضانة", "الآلية"],
        "rows": [
            ["<bdi>Staph aureus</bdi>", "2-6 ساعات", "سم جاهز بالطعام"],
            ["<bdi>Salmonella</bdi>", "12-72 ساعة", "غزو بكتيري"],
            ["<bdi>Campylobacter</bdi>", "2-5 أيام", "غزو بكتيري"],
            ["<bdi>E. coli</bdi>", "1-3 أيام", "سموم بعد التكاثر"],
        ],
    },
    "guideline_note": None,
}
WHY_WRONG[16] = {
    "A": "الإي كولاي يحتاج فترة حضانة أطول من 4 ساعات لأنه يحتاج تكاثر بالأمعاء أول.",
    "B": "السالمونيلا فترة حضانتها أطول بكثير (12 ساعة فأكثر)، ما تناسب هالسرعة.",
    "C": "الكامبيلوباكتر فترة حضانته أيام، بعيد جدًا عن 4 ساعات.",
}
HIGHLIGHT_TERMS[16] = ["profuse", "watery diarrhea", "within 4 hours of eating"]

EXPLANATIONS[17] = {
    "idea": "السؤال يبي أول <bdi>procedure</bdi> فوري ل<bdi>patient</bdi> عنده <bdi>symptoms</bdi> توحي ب<bdi>tuberculosis</bdi> رئوي نشط (حمى وتعرق ليلي وكحة لأسبوعين) قبل تأكيد الـ<bdi>diagnosis</bdi>.",
    "clues": [
        ("fever, night sweating, and<br>cough for 2 weeks", "صورة كلاسيكية توحي ب<bdi>tuberculosis</bdi> الرئوي النشط"),
    ],
    "why_correct": [
        "أي <bdi>patient</bdi> يشتبه فيه ب<bdi>tuberculosis</bdi> رئوي نشط لازم يُعزل فورًا بغرفة ضغط سلبي لمنع انتشار العدوى قبل أي فحص آخر.",
        "العزل <bdi>step</bdi> إدارية فورية تسبق حتى تأكيد الـ<bdi>diagnosis</bdi>، لأن <bdi>tuberculosis</bdi> ينتقل بالهواء (<bdi>airborne</bdi>).",
        "إرسال عينة القشع أو عمل منظار قصبات فحوصات مهمة بس تجي بعد ضمان عدم انتشار العدوى، مو ك<bdi>step</bdi> أولى.",
    ],
    "when_changes": [
        "لو الـ<bdi>symptoms</bdi> كانت <bdi>acute</bdi> قصيرة (أيام) بدون تعرق ليلي أو فقدان وزن، يقل الاشتباه ب<bdi>tuberculosis</bdi> ويختلف الـ<bdi>procedure</bdi> الأولي.",
        "بعد العزل، الـ<bdi>step</bdi> التالية المنطقية تكون إرسال القشع لفحص العصيات الصامدة للحمض (<bdi>AFB</bdi>).",
    ],
    "rule": "أي اشتباه ب<bdi>tuberculosis</bdi> رئوي نشط يستوجب العزل بغرفة ضغط سلبي فورًا قبل أي <bdi>procedure</bdi> تشخيصي ثاني.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[17] = {
    "A": "منظار القصبات <bdi>procedure</bdi> تشخيصي يأتي لاحقًا، مو الـ<bdi>procedure</bdi> الفوري الأول.",
    "B": "إرسال القشع فحص مهم بس يأتي بعد ضمان عزل الـ<bdi>patient</bdi> أول.",
    "D": "تأجيل الـ<bdi>patient</bdi> لعيادة خارجية <bdi>risk</bdi> لأنه يترك عدوى محتملة تنتشر بدون عزل.",
}
HIGHLIGHT_TERMS[17] = ["fever, night sweating, and", "cough for 2 weeks"]

EXPLANATIONS[18] = {
    "idea": "رجل جاي من الهند للحج معه حمى متقطعة وضيق نفس ودوخة وتشنجات ولخبطة ذهنية، وهذي صورة تتوافق مع الملاريا الدماغية الـ<bdi>severe</bdi>.",
    "clues": [
        ("Indian man came to Saudi Arabia for Hajj", "منطقة موبوءة بالملاريا وموسم يزيد الازدحام والعدوى"),
        ("intermittent fever", "نمط حمى متقطع كلاسيكي للملاريا"),
        ("drowsiness, convulsion and confusion", "<bdi>signs</bdi> إصابة دماغية <bdi>severe</bdi> توحي بملاريا دماغية"),
    ],
    "why_correct": [
        "الحمى المتقطعة مع قدوم من منطقة موبوءة بالملاريا (الهند) واللخبطة الذهنية والتشنجات تطابق صورة الملاريا الدماغية الـ<bdi>severe</bdi> (<bdi>P. falciparum</bdi>).",
        "الإنفلونزا ما تسبب تشنجات ولخبطة ذهنية <bdi>severe</bdi> بهالشكل عادة.",
        "الحمى الصفراء و<bdi>tuberculosis</bdi> ما تعطي هالصورة العصبية الـ<bdi>acute</bdi> المصاحبة للحمى المتقطعة.",
    ],
    "when_changes": [
        "لو ما فيه <bdi>symptoms</bdi> عصبية وبس حمى دورية بسيطة، يبقى الـ<bdi>diagnosis</bdi> ملاريا بس بدون تعقيد دماغي.",
        "لو كان الوصول من منطقة موبوءة بالحمى الصفراء مع <bdi>jaundice</bdi> ونزيف، يتجه الـ<bdi>diagnosis</bdi> لحمى صفراء بدالها.",
    ],
    "rule": "حمى متقطعة مع <bdi>symptoms</bdi> عصبية <bdi>acute</bdi> (تشنج، لخبطة) بعد قدوم من منطقة موبوءة بالملاريا تعني ملاريا دماغية حتى يثبت العكس.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[18] = {
    "B": "الإنفلونزا ما تسبب تشنجات ولخبطة ذهنية بهالشدة عادة.",
    "C": "الحمى الصفراء نادرة بالهند وتعطي <bdi>jaundice</bdi> ونزيف مو الصورة العصبية هذي.",
    "D": "<bdi>tuberculosis</bdi> <bdi>disease</bdi> <bdi>chronic</bdi> ما يسبب تشنجات ولخبطة <bdi>acute</bdi> خلال 4 أيام.",
}
HIGHLIGHT_TERMS[18] = ["Indian man came to Saudi Arabia for Hajj", "intermittent fever", "drowsiness, convulsion and confusion"]

EXPLANATIONS[19] = {
    "idea": "رجل معه حمى <bdi>elevated</bdi> وألم خلف العين وآلام عضلية ومفصلية <bdi>severe</bdi>، وهذي الصورة الكلاسيكية ل<bdi>dengue fever</bdi>.",
    "clues": [
        ("retro-orbital pain", "ألم خلف العين، <bdi>sign</bdi> مميزة ل<bdi>dengue fever</bdi>"),
        ("severe muscle and joint<br>pains", "آلام <bdi>severe</bdi> بالعضلات والمفاصل، <bdi>cause</bdi> تسميتها Break-bone fever"),
        ("fever to 39", "حمى <bdi>elevated</bdi> مصاحبة"),
    ],
    "why_correct": [
        "ألم خلف العين مع آلام عضلية ومفصلية <bdi>severe</bdi> وحمى <bdi>elevated</bdi> توليفة كلاسيكية جدًا ل<bdi>dengue fever</bdi> (<bdi>Dengue fever</bdi>).",
        "الإيبولا يعطي نزيف وصدمة سريعة مو هالصورة، والشيكونغونيا تشبه الضنك بس الألم المفصلي فيها أشد وأطول من الألم العضلي.",
        "فيروس كورونا (<bdi>MERS</bdi>) يعطي <bdi>symptoms</bdi> تنفسية بشكل أساسي مو هالصورة العضلية المفصلية.",
    ],
    "when_changes": [
        "لو الألم المفصلي كان هو السائد جدًا مع تورم مفصلي واضح ومستمر لأسابيع، يميل الـ<bdi>diagnosis</bdi> للشيكونغونيا.",
        "لو ظهر نزيف و<bdi>jaundice</bdi> وصدمة سريعة، يتجه الـ<bdi>diagnosis</bdi> للإيبولا بدالها.",
    ],
    "rule": "ألم خلف العين مع آلام عضلية ومفصلية <bdi>severe</bdi> وحمى يوجّه بقوة ل<bdi>dengue fever</bdi>.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[19] = {
    "A": "الإيبولا يعطي نزيف وصدمة سريعة، مو الصورة العضلية المفصلية هذي.",
    "B": "الشيكونغونيا تشبه الضنك بس الألم المفصلي فيها أشد وأطول أمدًا من الألم العضلي.",
    "D": "فيروس كورونا (MERS) يعطي <bdi>symptoms</bdi> تنفسية بشكل أساسي مو آلام عضلية مفصلية <bdi>severe</bdi>.",
}
HIGHLIGHT_TERMS[19] = ["retro-orbital pain", "severe muscle and joint", "fever to 39"]

EXPLANATIONS[20] = {
    "idea": "السؤال يبي أفضل <bdi>procedure</bdi> وقائي للملاريا عند السفر لمنطقة موبوءة، وما فيه لقاح روتيني معتمد وواسع الانتشار للملاريا.",
    "clues": [
        ("traveling to an<br>endemic country", "السفر لمنطقة موبوءة يستوجب وقاية دوائية"),
    ],
    "why_correct": [
        "الـ<bdi>treatment</bdi> الوقائي بالأدوية (<bdi>chemoprophylaxis</bdi>) هو الـ<bdi>procedure</bdi> المعتمد والموصى به لمنع الملاريا عند السفر لمنطقة موبوءة.",
        "ما فيه لقاح روتيني واسع الاستخدام للملاريا بنفس فعالية لقاحات ثانية، فخيار التطعيم غير دقيق هنا.",
        "تجنب المناطق الموبوءة كليًا مو عملي دايمًا للمسافرين، والمناعة (<bdi>immunoglobulin</bdi>) ما تستخدم للوقاية من الملاريا.",
    ],
    "when_changes": [
        "لو السؤال يذكر منطقة قليلة الخطورة بدون إقامة طويلة، ممكن يكتفى ب<bdi>procedures</bdi> وقائية غير دوائية (ناموسية، طارد حشرات) بجانب الأدوية.",
    ],
    "rule": "الوقاية الدوائية (<bdi>chemoprophylaxis</bdi>) هي الـ<bdi>procedure</bdi> المعتمد لمنع الملاريا عند السفر لمنطقة موبوءة.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[20] = {
    "A": "ما فيه لقاح روتيني معتمد وواسع الانتشار للملاريا بنفس فعالية التطعيمات الثانية.",
    "B": "المناعة (immunoglobulin) ما تستخدم للوقاية من الملاريا.",
    "D": "تجنب المناطق الموبوءة كليًا مو عملي دايمًا، والوقاية الدوائية أساسية بغض النظر.",
}
HIGHLIGHT_TERMS[20] = ["traveling to an", "endemic country"]

EXPLANATIONS[21] = {
    "idea": "السؤال يبي أكثر دواء ملاريا تطور طفيلي الملاريا مقاومة ضده، وهذا معروف جدًا مع الكلوروكين.",
    "clues": [
        ("parasites develop resistance to", "يبي تحديد الدواء اللي فقد فعاليته ب<bdi>cause</bdi> مقاومة الطفيلي الواسعة"),
    ],
    "why_correct": [
        "<bdi>Chloroquine</bdi> هو الدواء اللي تطورت ضده مقاومة واسعة جدًا من طفيلي <bdi>P. falciparum</bdi> بمعظم مناطق العالم الموبوءة.",
        "ب<bdi>cause</bdi> هالمقاومة الواسعة، صار الكلوروكين غير فعال كخط أول بمعظم المناطق الموبوءة حاليًا.",
        "الأدوية الثانية زي <bdi>Malarone</bdi> و<bdi>Mefloquine</bdi> و<bdi>Atovaquone/proguanil</bdi> أحدث ومقاومتها أقل انتشارًا بكثير.",
    ],
    "when_changes": [
        "لو المنطقة معروفة بحساسية الطفيلي للكلوروكين (مناطق قليلة متبقية)، يصير الكلوروكين خيار فعال هناك تحديدًا.",
    ],
    "rule": "الكلوروكين هو الدواء الأشهر اللي طور طفيلي الملاريا مقاومة واسعة ضده عالميًا.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[21] = {
    "A": "الـ Malarone مقاومته أقل انتشارًا مقارنة بالكلوروكين.",
    "B": "الـ Mefloquine فيه مقاومة بمناطق محددة بس أقل بكثير من الكلوروكين.",
    "D": "الـ Atovaquone/proguanil من الأدوية الأحدث ومقاومته محدودة جدًا حتى الآن.",
}
HIGHLIGHT_TERMS[21] = ["parasites develop resistance to"]

EXPLANATIONS[22] = {
    "idea": "السؤال يبي أشيع <bdi>cause</bdi> حمى عند المسافرين الراجعين من أفريقيا جنوب الصحراء، وهي منطقة موبوءة جدًا بالملاريا.",
    "clues": [
        ("sub-Saharan Africa", "منطقة معروفة بانتشار الملاريا الـ<bdi>severe</bdi>"),
    ],
    "why_correct": [
        "الملاريا هي أشيع <bdi>cause</bdi> حمى عند المسافرين الراجعين من أفريقيا جنوب الصحراء ب<bdi>cause</bdi> انتشارها الواسع هناك.",
        "<bdi>dengue fever</bdi> وزيكا أكثر شيوعًا بمناطق ثانية زي جنوب شرق آسيا مو أفريقيا جنوب الصحراء.",
        "إسهال المسافرين يسبب <bdi>symptoms</bdi> هضمية بشكل أساسي مو حمى معزولة بدون <bdi>symptoms</bdi> هضمية واضحة.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> راجع من جنوب شرق آسيا بدل أفريقيا، يصير <bdi>dengue fever</bdi> هو الـ<bdi>cause</bdi> الأشيع بدالها.",
    ],
    "rule": "الملاريا أشيع <bdi>cause</bdi> حمى عند المسافرين الراجعين من أفريقيا جنوب الصحراء.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[22] = {
    "B": "زيكا أقل شيوعًا ك<bdi>cause</bdi> حمى من أفريقيا جنوب الصحراء مقارنة بالملاريا.",
    "C": "<bdi>dengue fever</bdi> أشيع بمناطق زي جنوب شرق آسيا مو أفريقيا جنوب الصحراء تحديدًا.",
    "D": "إسهال المسافرين يعطي <bdi>symptoms</bdi> هضمية بارزة، مو حمى معزولة بالدرجة الأولى.",
}
HIGHLIGHT_TERMS[22] = ["sub-Saharan Africa"]

EXPLANATIONS[23] = {
    "idea": "السؤال يبي أشيع <bdi>cause</bdi> حمى عند المسافرين الراجعين من جنوب شرق آسيا، وهذي المنطقة معروفة بانتشار <bdi>dengue fever</bdi>.",
    "clues": [
        ("Southeast<br>Asia", "منطقة معروفة بانتشار <bdi>dengue fever</bdi>"),
    ],
    "why_correct": [
        "<bdi>dengue fever</bdi> هي أشيع <bdi>disease</bdi> يُشخّص عند المسافرين الراجعين من جنوب شرق آسيا ب<bdi>cause</bdi> انتشار بعوضة الزاعجة هناك.",
        "الملاريا موجودة بجنوب شرق آسيا بس أقل شيوعًا ك<bdi>cause</bdi> حمى مقارنة ب<bdi>dengue fever</bdi> بهالمنطقة تحديدًا.",
        "زيكا وإسهال المسافرين <bdi>causes</bdi> أقل شيوعًا للحمى المعزولة مقارنة ب<bdi>dengue fever</bdi> هناك.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> راجع من أفريقيا جنوب الصحراء بدل جنوب شرق آسيا، تصير الملاريا هي الـ<bdi>cause</bdi> الأشيع بدالها.",
    ],
    "rule": "<bdi>dengue fever</bdi> أشيع <bdi>cause</bdi> حمى عند المسافرين الراجعين من جنوب شرق آسيا.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[23] = {
    "A": "الملاريا موجودة بس أقل شيوعًا ك<bdi>cause</bdi> حمى من جنوب شرق آسيا مقارنة ب<bdi>dengue fever</bdi>.",
    "B": "زيكا أقل شيوعًا ك<bdi>cause</bdi> حمى مقارنة ب<bdi>dengue fever</bdi> بهالمنطقة.",
    "D": "إسهال المسافرين يعطي <bdi>symptoms</bdi> هضمية بارزة، مو حمى معزولة بالدرجة الأولى.",
}
HIGHLIGHT_TERMS[23] = ["Southeast"]

EXPLANATIONS[24] = {
    "idea": "السؤال يبي وقت ذروة لسع بعوضة الزاعجة المصرية (<bdi>Aedes aegypti</bdi>) الناقلة ل<bdi>dengue fever</bdi>.",
    "clues": [
        ("Aedes aegypti", "بعوضة نهارية النشاط تختلف عن بعوض الملاريا الليلي"),
    ],
    "why_correct": [
        "بعوضة <bdi>Aedes aegypti</bdi> نشطة نهارًا بعكس أغلب البعوض، وذروة لسعها تكون بالصباح الباكر.",
        "معرفة وقت النشاط مهمة للوقاية (لبس ملابس واقية واستخدام طارد حشرات بهالفترة تحديدًا).",
        "باقي الخيارات (منتصف اليوم، أول الليل، آخر الليل) أقل تطابقًا مع نمط نشاط هالبعوضة النهاري المبكر.",
    ],
    "when_changes": [
        "لو السؤال عن بعوض الملاريا (<bdi>Anopheles</bdi>) بدل الزاعجة، الذروة تكون ليلًا مو صباحًا.",
    ],
    "rule": "بعوضة الزاعجة المصرية الناقلة ل<bdi>dengue fever</bdi> نشطة نهارًا وذروتها بالصباح الباكر.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[24] = {
    "B": "منتصف اليوم مو ذروة النشاط الرئيسية لهالبعوضة.",
    "C": "أول الليل يناسب أكثر بعوض الملاريا (Anopheles) مو الزاعجة.",
    "D": "آخر الليل أيضًا يناسب بعوض الملاريا مو الزاعجة النهارية.",
}
HIGHLIGHT_TERMS[24] = ["Aedes aegypti"]

EXPLANATIONS[25] = {
    "idea": "<bdi>patient</bdi> مشتبه فيه بالإيبولا (<bdi>disease</bdi> معدي خطير جدًا وقاتل) يبي يترك المستشفى رغمًا، والسؤال يبي أنسب <bdi>procedure</bdi> يحمي المجتمع من انتشار العدوى.",
    "clues": [
        ("suspected Ebola case", "<bdi>disease</bdi> <bdi>severe</bdi> العدوى يستوجب <bdi>procedures</bdi> حماية عامة صارمة"),
        ("leave the hospital", "<bdi>risk</bdi> انتشار عدوى قاتلة بالمجتمع لو غادر"),
    ],
    "why_correct": [
        "الإيبولا <bdi>disease</bdi> <bdi>severe</bdi> العدوى ومهدد للحياة وللمجتمع، فمنع الـ<bdi>patient</bdi> من المغادرة عبر أمن المستشفى <bdi>procedure</bdi> ضروري لحماية الصحة العامة.",
        "هذا يختلف عن حالات الخروج بالإرادة (<bdi>AMA</bdi>) العادية، لأن <bdi>risk</bdi> انتشار <bdi>disease</bdi> معدٍ قاتل بيبرر تقييد الحرية الفردية مؤقتًا لحماية الآخرين.",
        "استشارة لجنة الأخلاقيات أو فريق الـ<bdi>diseases</bdi> المعدية <bdi>procedures</bdi> مهمة بس تأخذ وقت، والخطورة هنا تستدعي منع فوري.",
    ],
    "when_changes": [
        "لو الـ<bdi>disease</bdi> غير معدٍ أو خطره محدود على الآخرين، يصير توقيع التخريج بالإرادة (<bdi>AMA</bdi>) هو الـ<bdi>procedure</bdi> المناسب واحترام حق الـ<bdi>patient</bdi>.",
    ],
    "rule": "بالـ<bdi>diseases</bdi> <bdi>severe</bdi> العدوى والخطورة على المجتمع مثل الإيبولا، منع الـ<bdi>patient</bdi> من المغادرة <bdi>procedure</bdi> ضروري لحماية الصحة العامة.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[25] = {
    "B": "استشارة لجنة الأخلاقيات مهمة بس تأخذ وقت، والـ<bdi>risk</bdi> الفوري يستدعي <bdi>procedure</bdi> أسرع.",
    "C": "إحالة لفريق الـ<bdi>diseases</bdi> المعدية <bdi>step</bdi> لاحقة، مو الـ<bdi>procedure</bdi> الفوري لمنع مغادرته الآن.",
    "D": "توقيع التخريج بالإرادة يسمح له بالمغادرة وينشر عدوى قاتلة بالمجتمع، وهذا غير مقبول.",
}
HIGHLIGHT_TERMS[25] = ["suspected Ebola case", "leave the hospital"]

EXPLANATIONS[26] = {
    "idea": "نفس فكرة أشيع <bdi>cause</bdi> حمى عند العائدين من أفريقيا جنوب الصحراء، وهي منطقة موبوءة جدًا بالملاريا.",
    "clues": [
        ("sub-Saharan Africa", "منطقة معروفة بانتشار الملاريا الـ<bdi>severe</bdi>"),
    ],
    "why_correct": [
        "الملاريا أشيع <bdi>cause</bdi> حمى عند العائدين من رحلة لمنطقة جنوب الصحراء الأفريقية ب<bdi>cause</bdi> انتشارها الواسع هناك.",
        "<bdi>dengue fever</bdi> وزيكا أشيع بمناطق ثانية (جنوب شرق آسيا) مو أفريقيا جنوب الصحراء تحديدًا.",
        "إسهال المسافرين يعطي <bdi>symptoms</bdi> هضمية بارزة، مو حمى معزولة بالدرجة الأولى كما بالسؤال.",
    ],
    "when_changes": [
        "لو الرحلة كانت لجنوب شرق آسيا بدل أفريقيا، يصير <bdi>dengue fever</bdi> هو الـ<bdi>cause</bdi> الأشيع بدالها.",
    ],
    "rule": "الملاريا أشيع <bdi>cause</bdi> حمى عند المسافرين الراجعين من أفريقيا جنوب الصحراء.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[26] = {
    "B": "زيكا أقل شيوعًا ك<bdi>cause</bdi> حمى من أفريقيا جنوب الصحراء مقارنة بالملاريا.",
    "C": "<bdi>dengue fever</bdi> أشيع بمناطق زي جنوب شرق آسيا مو أفريقيا جنوب الصحراء.",
    "D": "إسهال المسافرين يعطي <bdi>symptoms</bdi> هضمية بارزة، مو حمى معزولة فقط.",
}
HIGHLIGHT_TERMS[26] = ["sub-Saharan Africa"]

EXPLANATIONS[27] = {
    "idea": "السؤال يبي أفضل <bdi>procedure</bdi> وقائي بسيط لإسهال المسافرين، وهو تجنب مصادر تلوث الماء الشائعة زي الثلج.",
    "clues": [
        ("preventive measures is recommended for travel diarrhea", "يبي تحديد أبسط وأفعل <bdi>procedure</bdi> وقائي من إسهال المسافرين"),
    ],
    "why_correct": [
        "الثلج غالبًا يُصنع من ماء غير مأمون بمناطق كثيرة ويعتبر مصدر شائع لتلوث المشروبات وإسهال المسافرين.",
        "تجنب المشروبات مع الثلج <bdi>procedure</bdi> وقائي بسيط وفعال وموصى به بشكل موثق.",
        "الأكل بمطاعم نظيفة الظاهر ما يضمن سلامة الماء أو الأكل فعليًا، والاعتماد على مصدر ماء حكومي أو تجنب كل الخضار مو عملي ولا دقيق كقاعدة عامة.",
    ],
    "when_changes": [
        "لو المصدر الموثق للتلوث كان الخضار النيئة غير المغسولة بدل الثلج، يصير تجنبها هو الـ<bdi>procedure</bdi> الأنسب بذاك السياق.",
    ],
    "rule": "تجنب المشروبات المضاف لها ثلج من أبسط وأهم <bdi>procedures</bdi> الوقاية من إسهال المسافرين.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[27] = {
    "B": "الأكل بمطاعم نظيفة الظاهر ما يضمن سلامة الماء أو مصادر التلوث الفعلية.",
    "C": "الاعتماد على ماء حكومي فقط مو عملي دايمًا للمسافر ولا يغطي كل مصادر التلوث.",
    "D": "تجنب كل الخضار والاكتفاء بالفواكه قاعدة غير دقيقة ولا عملية بالكامل.",
}
HIGHLIGHT_TERMS[27] = ["preventive measures is recommended for travel diarrhea"]

EXPLANATIONS[28] = {
    "idea": "رجل مسافر للسودان يحتاج وقاية دوائية من الملاريا، والسودان منطقة معروفة بمقاومة الكلوروكين فيها.",
    "clues": [
        ("travel to Sudan", "منطقة موبوءة بالملاريا ومعروفة بمقاومة الكلوروكين"),
    ],
    "why_correct": [
        "السودان منطقة فيها مقاومة واسعة للكلوروكين من طفيلي <bdi>P. falciparum</bdi>، فيُفضّل <bdi>Atovaquone/proguanil</bdi> كوقاية دوائية.",
        "ما فيه لقاح روتيني معتمد وواسع للملاريا، فخيار التطعيم غير صحيح.",
        "مع أي سفر لمنطقة موبوءة زي السودان، لازم وقاية دوائية بغض النظر عن مدة الرحلة، حتى لو كانت قصيرة.",
    ],
    "when_changes": [
        "لو المنطقة معروفة بحساسية الطفيلي للكلوروكين، يصير الكلوروكين خيار مناسب هناك تحديدًا.",
    ],
    "rule": "بالمناطق ذات المقاومة للكلوروكين (زي السودان)، يُفضّل <bdi>Atovaquone/proguanil</bdi> كوقاية دوائية من الملاريا.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[28] = {
    "A": "الكلوروكين غير فعال بالسودان ب<bdi>cause</bdi> انتشار مقاومة الطفيلي ضده.",
    "B": "ما فيه لقاح روتيني معتمد وفعال للملاريا حتى الآن.",
    "D": "حتى برحلة قصيرة لمنطقة موبوءة، الوقاية الدوائية ضرورية لتجنب <bdi>risk</bdi> الإصابة.",
}
HIGHLIGHT_TERMS[28] = ["travel to Sudan"]

EXPLANATIONS[29] = {
    "idea": "السؤال يبي <bdi>procedure</bdi> وقائي إضافي لحجاج قادمين من حزام <bdi>meningitis</bdi> الأفريقي، بجانب تطعيم المكورات السحائية الرباعي.",
    "clues": [
        ("African meningitis<br>belt countries", "منطقة عالية الخطورة لانتقال المكورات السحائية"),
        ("quadrivalent (ACYW 135) vaccine", "تطعيم موصى به أصلًا، والسؤال عن إضافة له"),
    ],
    "why_correct": [
        "جرعة واحدة من <bdi>ciprofloxacin</bdi> (500 مجم) كيموبروفيلاكسي إضافي موصى بها لحجاج قادمين من مناطق عالية الخطورة بجانب التطعيم.",
        "المراقبة لفترة طويلة (6 أو 10 أيام) مو الـ<bdi>procedure</bdi> الوقائي المباشر الموصى به هنا، والهدف هو منع الـ<bdi>disease</bdi> مو رصده بعد حدوثه فقط.",
        "إعطاء جرعة تنشيطية من نفس التطعيم بمجرد الوصول مو الـ<bdi>procedure</bdi> الإضافي المعتمد بهالسياق.",
    ],
    "when_changes": [
        "لو الحاج من منطقة <bdi>low</bdi> الخطورة بدون تاريخ تفشي حديث، يكتفى بالتطعيم الروتيني بدون كيموبروفيلاكسي إضافي.",
    ],
    "rule": "للحجاج القادمين من حزام <bdi>meningitis</bdi> الأفريقي، يضاف كيموبروفيلاكسي بجرعة سيبروفلوكساسين بجانب التطعيم الرباعي.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[29] = {
    "A": "المراقبة لـ 6 أيام وحدها مو <bdi>procedure</bdi> وقائي فعّال إضافي معتمد بهالسياق.",
    "B": "نفس الفكرة بمدة أطول (10 أيام)، مو الـ<bdi>procedure</bdi> الوقائي الدوائي المطلوب.",
    "D": "إعطاء جرعة تنشيطية فورية عند الوصول مو الـ<bdi>procedure</bdi> الإضافي المعتمد هنا.",
}
HIGHLIGHT_TERMS[29] = ["African meningitis", "quadrivalent (ACYW 135) vaccine"]

EXPLANATIONS[30] = {
    "idea": "السؤال يبي التطعيم الإلزامي على كل الحجاج القادمين لأداء الحج بغض النظر عن بلدهم، وهو تطعيم <bdi>meningitis</bdi>.",
    "clues": [
        ("arriving from any country", "تطعيم مطلوب من الجميع بلا استثناء"),
    ],
    "why_correct": [
        "تطعيم <bdi>meningitis</bdi> الرباعي (<bdi>ACYW135</bdi>) مطلوب إلزاميًا من جميع الحجاج بغض النظر عن بلد قدومهم ب<bdi>cause</bdi> ازدحام الحج الـ<bdi>severe</bdi> و<bdi>risk</bdi> انتقال المكورات السحائية.",
        "الحمى الصفراء مطلوبة فقط من القادمين من بلدان موبوءة محددة، مو من الجميع.",
        "<bdi>dengue fever</bdi> ما فيها تطعيم روتيني إلزامي، وشلل الأطفال مطلوب من بلدان معينة موبوءة فقط مو من الجميع.",
    ],
    "when_changes": [
        "لو السؤال يخص القادمين من بلد موبوء بالحمى الصفراء تحديدًا، يصير تطعيم الحمى الصفراء هو المطلوب إضافيًا لهم.",
    ],
    "rule": "تطعيم <bdi>meningitis</bdi> الرباعي إلزامي على جميع حجاج بيت الله الحرام بغض النظر عن بلد القدوم.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[30] = {
    "B": "الحمى الصفراء مطلوبة فقط من القادمين من بلدان موبوءة محددة، مو من الجميع.",
    "C": "<bdi>dengue fever</bdi> ما فيها تطعيم روتيني إلزامي معتمد للحجاج.",
    "D": "شلل الأطفال مطلوب من بلدان معينة موبوءة فقط، مو شرط عام على كل الحجاج.",
}
HIGHLIGHT_TERMS[30] = ["arriving from any country"]

EXPLANATIONS[31] = {
    "idea": "نفس فكرة أشيع <bdi>cause</bdi> حمى عند العائدين من جنوب شرق آسيا، وهو <bdi>dengue fever</bdi>.",
    "clues": [
        ("Southeast Asia", "منطقة معروفة بانتشار <bdi>dengue fever</bdi>"),
    ],
    "why_correct": [
        "<bdi>dengue fever</bdi> أشيع <bdi>cause</bdi> حمى عند المسافرين العائدين من رحلة قصيرة لجنوب شرق آسيا ب<bdi>cause</bdi> انتشار بعوضة الزاعجة هناك.",
        "الملاريا موجودة بالمنطقة بس أقل شيوعًا ك<bdi>cause</bdi> حمى مقارنة ب<bdi>dengue fever</bdi> بهالمنطقة تحديدًا.",
        "زيكا وإسهال المسافرين <bdi>causes</bdi> أقل شيوعًا للحمى المعزولة مقارنة ب<bdi>dengue fever</bdi> هناك.",
    ],
    "when_changes": [
        "لو الرحلة كانت لأفريقيا جنوب الصحراء بدل جنوب شرق آسيا، تصير الملاريا هي الـ<bdi>cause</bdi> الأشيع.",
    ],
    "rule": "<bdi>dengue fever</bdi> أشيع <bdi>cause</bdi> حمى عند المسافرين الراجعين من جنوب شرق آسيا.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[31] = {
    "A": "الملاريا موجودة بس أقل شيوعًا ك<bdi>cause</bdi> حمى من جنوب شرق آسيا مقارنة ب<bdi>dengue fever</bdi>.",
    "B": "زيكا أقل شيوعًا ك<bdi>cause</bdi> حمى مقارنة ب<bdi>dengue fever</bdi> بهالمنطقة.",
    "D": "إسهال المسافرين يعطي <bdi>symptoms</bdi> هضمية بارزة، مو حمى معزولة فقط.",
}
HIGHLIGHT_TERMS[31] = ["Southeast Asia"]

EXPLANATIONS[32] = {
    "idea": "السؤال يبي دواء يزيد <bdi>risk</bdi> تكرار عدوى <bdi>Clostridium difficile</bdi>، والمثبطات المضخة البروتونية من أشهر <bdi>factors</bdi> الـ<bdi>risk</bdi> الدوائية المعروفة.",
    "clues": [
        ("clostriduim difficile infection", "عدوى معوية مرتبطة بخلل ميكروبيوم الأمعاء و<bdi>factors</bdi> <bdi>risk</bdi> دوائية معروفة"),
    ],
    "why_correct": [
        "<bdi>Omeprazole</bdi> (مثبط مضخة البروتون) يقلل حموضة المعدة ويغيّر بيئة الأمعاء، وهذا مرتبط بزيادة <bdi>risk</bdi> عدوى <bdi>C. difficile</bdi> وتكرارها.",
        "كبريتات الحديد وكربونات الكالسيوم والفيتامينات المتعددة ما لها علاقة موثقة بزيادة <bdi>risk</bdi> <bdi>C. difficile</bdi>.",
        "تقليل الحموضة المعدية يسمح لأبواغ الجرثومة بالبقاء والانتقال للأمعاء بسهولة أكبر.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> يستخدم مضادات حيوية واسعة الطيف مؤخرًا، يصير هذا <bdi>factor</bdi> الـ<bdi>risk</bdi> الأبرز بدل مثبط المضخة.",
    ],
    "rule": "مثبطات مضخة البروتون (<bdi>PPIs</bdi>) من <bdi>factors</bdi> الـ<bdi>risk</bdi> الدوائية المعروفة لعدوى <bdi>C. difficile</bdi> وتكرارها.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[32] = {
    "B": "كبريتات الحديد ما لها علاقة موثقة بزيادة <bdi>risk</bdi> C. difficile.",
    "C": "كربونات الكالسيوم مثلها، ما ترتبط بزيادة <bdi>risk</bdi> هالعدوى.",
    "D": "الفيتامينات المتعددة ما لها تأثير معروف على <bdi>risk</bdi> C. difficile.",
}
HIGHLIGHT_TERMS[32] = ["clostriduim difficile infection", "recurrent infection"]

EXPLANATIONS[33] = {
    "idea": "شاب معه إسهال مائي <bdi>chronic</bdi> (3 أشهر) وفقدان وزن بعد سفر لمكة، وسحب من الاثني عشر طلع فيه أشكال متحركة (تروفوزويت)، وهذي صورة كلاسيكية لداء الجيارديا.",
    "clues": [
        ("watery diarrhea", "إسهال مائي <bdi>chronic</bdi> مو دموي، يميل ل<bdi>cause</bdi> طفيلي مو غزوي"),
        ("travel to Mecca few months back", "احتمال التقاط عدوى معوية من ازدحام أو مصدر ماء ملوث"),
        ("many trophozoites", "أشكال متحركة للطفيلي بسحب الاثني عشر، مميزة لـ Giardia"),
    ],
    "why_correct": [
        "وجود تروفوزويت بسحب الاثني عشر مع إسهال مائي <bdi>chronic</bdi> وفقدان وزن صورة كلاسيكية جدًا لداء الجيارديا (<bdi>Giardia lamblia</bdi>).",
        "السالمونيلا والكامبيلوباكتر يعطون إسهال <bdi>acute</bdi> غالبًا دموي مو <bdi>chronic</bdi> ممتد لأشهر، والـ <bdi>C. difficile</bdi> مرتبط باستخدام مضادات حيوية مؤخرًا وهذا غير مذكور هنا.",
        "منظار المعدة الـ<bdi>normal</bdi> يبعد <bdi>causes</bdi> هضمية علوية ثانية، ويوجه التركيز للاثني عشر واختبار البراز النوعي.",
    ],
    "when_changes": [
        "لو الإسهال كان دمويًا <bdi>acute</bdi> مع حمى <bdi>severe</bdi>، يميل الـ<bdi>diagnosis</bdi> لسالمونيلا أو كامبيلوباكتر بدل الجيارديا.",
        "لو الـ<bdi>patient</bdi> استخدم مضادات حيوية مؤخرًا، يصير <bdi>C. difficile</bdi> احتمال أقوى.",
    ],
    "rule": "إسهال مائي <bdi>chronic</bdi> مع فقدان وزن بعد سفر ووجود تروفوزويت بسحب الاثني عشر يعني داء الجيارديا حتى يثبت العكس.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[33] = {
    "A": "السالمونيلا تعطي إسهال <bdi>acute</bdi> غالبًا مو <bdi>chronic</bdi> ممتد لأشهر بهالشكل.",
    "C": "C. difficile مرتبط باستخدام مضادات حيوية مؤخرًا، وهذا غير مذكور بالسؤال.",
    "D": "الكامبيلوباكتر يعطي إسهال <bdi>acute</bdi> أحيانًا دموي، مو مسار <bdi>chronic</bdi> ممتد 3 أشهر.",
}
HIGHLIGHT_TERMS[33] = ["watery diarrhea", "travel to Mecca few months back", "many trophozoites"]

EXPLANATIONS[34] = {
    "idea": "نفس صورة داء الجيارديا (إسهال <bdi>chronic</bdi> بعد سفر وتروفوزويت بسحب الاثني عشر)، والسؤال هذي المرة عن الـ<bdi>treatment</bdi> المناسب.",
    "clues": [
        ("watery diarrhea", "إسهال مائي <bdi>chronic</bdi> نموذجي للجيارديا"),
        ("many trophozities", "تأكيد الـ<bdi>diagnosis</bdi> بوجود التروفوزويت"),
    ],
    "why_correct": [
        "<bdi>Metronidazole</bdi> هو الـ<bdi>treatment</bdi> القياسي الأول لداء الجيارديا المؤكد.",
        "<bdi>Doxycycline</bdi> يستخدم لعدوى ثانية (زي الكوليرا أو الـ<bdi>Brucella</bdi>) مو الجيارديا كخط أول.",
        "<bdi>Rifampicin</bdi> و<bdi>Chloramphenicol</bdi> ما لهم دور علاجي معتمد بداء الجيارديا.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> حامل، يُفضّل بدائل زي <bdi>paromomycin</bdi> بدل الميترونيدازول بحسب مرحلة الحمل.",
    ],
    "rule": "الميترونيدازول هو الـ<bdi>treatment</bdi> القياسي الأول لداء الجيارديا المؤكد.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[34] = {
    "A": "الدوكسيسايكلين ما له دور علاجي معتمد لداء الجيارديا.",
    "B": "الريفامبيسين ما له دور علاجي بهالعدوى الطفيلية.",
    "D": "الكلورامفينيكول أيضًا ما له استطباب معتمد ل<bdi>treatment</bdi> الجيارديا.",
}
HIGHLIGHT_TERMS[34] = ["watery diarrhea", "many trophozities"]

EXPLANATIONS[35] = {
    "idea": "السؤال يبي أبسط وأفضل <bdi>procedure</bdi> وقائي من عدوى الجيارديا، وهي عدوى تنتقل عبر التلوث البرازي-الفموي.",
    "clues": [
        ("prevent giardiasis infection", "يبي تحديد أبسط <bdi>procedure</bdi> وقائي يقطع طريق انتقال الطفيلي"),
    ],
    "why_correct": [
        "غسل اليدين <bdi>procedure</bdi> بسيط وفعال جدًا لقطع طريق انتقال الجيارديا (برازي-فموي)، وهو الأساس بكل برامج الوقاية.",
        "تجنب الفواكه أو الخضار كليًا مو ضروري ولا عملي، والعدوى تنتقل غالبًا عبر الماء الملوث واليدين مو الطعام النباتي تحديدًا.",
        "المضادات الوقائية ما تستخدم للوقاية من الجيارديا بشكل روتيني أصلًا.",
    ],
    "when_changes": [
        "لو مصدر الـ<bdi>risk</bdi> كان ماء غير معالج تحديدًا، يضاف غلي أو تعقيم الماء ك<bdi>procedure</bdi> وقائي إضافي مع غسل اليدين.",
    ],
    "rule": "غسل اليدين هو أبسط وأهم <bdi>procedure</bdi> وقائي من عدوى الجيارديا.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[35] = {
    "B": "تجنب الفواكه كليًا مو ضروري ولا يستهدف طريقة انتقال العدوى الفعلية.",
    "C": "تجنب الخضار كليًا نفس الفكرة، غير عملي وغير مستهدف لل<bdi>cause</bdi> الحقيقي.",
    "D": "المضادات الوقائية ما تستخدم روتينيًا للوقاية من الجيارديا.",
}
HIGHLIGHT_TERMS[35] = ["prevent giardiasis infection"]

EXPLANATIONS[36] = {
    "idea": "<bdi>patient</bdi> <bdi>diabetes</bdi> بالعناية المركزة عنده إنتان دم من <bdi>MRSA</bdi> (مقاوم للميثيسيلين)، والسؤال يبي المضاد الحيوي المناسب لهالمقاومة.",
    "clues": [
        ("methicillin-resistant staphylococcus aureus", "مقاومة للميثيسيلين تحدد اختيار المضاد الحيوي المناسب"),
    ],
    "why_correct": [
        "<bdi>Vancomycin</bdi> هو خط الـ<bdi>treatment</bdi> الأول المعتمد لعدوى <bdi>MRSA</bdi> الغازية زي إنتان الدم.",
        "<bdi>Cefuroxime</bdi> و<bdi>Flucloxacillin</bdi> من مجموعة البيتالاكتام اللي MRSA مقاوم لها أصلًا، فما تفيد.",
        "<bdi>Gentamycin</bdi> ممكن يضاف كمساعد بحالات معينة بس ما يعتبر <bdi>treatment</bdi> أساسي وحيد لـ MRSA.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عنده حساسية أو فشل استجابة للفانكومايسين، تصير بدائل زي <bdi>linezolid</bdi> أو <bdi>daptomycin</bdi> هي الخيار.",
    ],
    "rule": "الفانكومايسين هو خط الـ<bdi>treatment</bdi> الأول لعدوى MRSA الغازية مثل إنتان الدم.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[36] = {
    "A": "السيفوروكسيم من البيتالاكتام اللي MRSA مقاوم له أصلًا.",
    "C": "الجنتامايسين ممكن يضاف كمساعد بس مو <bdi>treatment</bdi> وحيد معتمد لـ MRSA.",
    "D": "الفلوكلوكساسيلين من البيتالاكتام أيضًا، وMRSA مقاوم له بحكم التعريف.",
}
HIGHLIGHT_TERMS[36] = ["methicillin-resistant staphylococcus aureus"]

EXPLANATIONS[37] = {
    "idea": "السؤال يبي أبسط وأفعل <bdi>procedure</bdi> لمنع انتشار عدوى <bdi>MRSA</bdi>، وهو نظافة اليدين.",
    "clues": [
        ("prevent spread of MRSA infection", "يبي تحديد أبسط وأفعل <bdi>procedure</bdi> لمنع انتقال الجرثومة"),
    ],
    "why_correct": [
        "نظافة اليدين (<bdi>hand hygiene</bdi>) هي الـ<bdi>procedure</bdi> الأبسط والأكثر فعالية المثبت لمنع انتقال MRSA بين المرضى والعاملين الصحيين.",
        "لبس الأثواب والكمامات <bdi>procedures</bdi> إضافية بحالات تماس مباشر معين، بس مو الـ<bdi>procedure</bdi> الأساسي الأشمل والأبسط.",
        "التعقيم اليومي للأسرة مهم بس أقل تأثيرًا من نظافة اليدين المتكررة بكل تماس مع الـ<bdi>patient</bdi>.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> بعزل تماسي مؤكد بـ MRSA، تضاف الأثواب والقفازات ك<bdi>procedures</bdi> إضافية بجانب نظافة اليدين.",
    ],
    "rule": "نظافة اليدين هي أبسط وأهم <bdi>procedure</bdi> لمنع انتشار عدوى MRSA.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[37] = {
    "B": "لبس الأثواب <bdi>procedure</bdi> إضافي بحالات تماس مباشر، مو الـ<bdi>procedure</bdi> الأبسط والأشمل.",
    "C": "الكمامات تستخدم بحالات محددة، مو الـ<bdi>procedure</bdi> الأساسي لمنع انتشار MRSA.",
    "D": "تعقيم الأسرة يوميًا مهم بس أقل تأثيرًا من نظافة اليدين المتكررة.",
}
HIGHLIGHT_TERMS[37] = ["prevent spread of MRSA infection"]

EXPLANATIONS[38] = {
    "idea": "رجل معه حمى وطفح على الكفين والأخمصين وتاريخ قرحة غير مؤلمة بالعضو التناسلي قبل 6 أسابيع، وهذي صورة كلاسيكية للزهري الثانوي.",
    "clues": [
        ("rash on his palm and soles", "طفح بالراحتين والأخمصين، <bdi>sign</bdi> مميزة جدًا للزهري الثانوي"),
        ("painless ulcer on his penis 6 weeks earlier", "القرحة الأولية غير المؤلمة (chancre) بالزهري الأولي"),
        ("generalised<br>lymphadenopathy", "تضخم غدد لمفاوية معمم، متوافق مع الزهري الثانوي"),
    ],
    "why_correct": [
        "القرحة التناسلية غير المؤلمة قبل أسابيع تتبعها طفح بالراحتين والأخمصين مع تضخم غدد لمفاوية معمم صورة كلاسيكية للانتقال من الزهري الأولي للثانوي.",
        "الكلاميديا وستافيلوكوكس أوريوس ما يعطون هالتسلسل الزمني ولا هالتوزيع المميز للطفح بالراحتين والأخمصين.",
        "الطفح بالراحتين والأخمصين تحديدًا <bdi>sign</bdi> تكاد تكون حصرية للزهري بين الـ<bdi>diseases</bdi> المنقولة جنسيًا.",
    ],
    "when_changes": [
        "لو القرحة كانت مؤلمة مع تضخم غدد مؤلم موضعي، يميل الـ<bdi>diagnosis</bdi> للهربس التناسلي أو القرحة اللينة بدل الزهري.",
    ],
    "rule": "طفح بالراحتين والأخمصين بعد قرحة تناسلية غير مؤلمة يعني زهري ثانوي حتى يثبت العكس.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[38] = {
    "A": "Coxiella burnetii يسبب حمى كيو (Q fever)، ما يعطي هالتسلسل التناسلي والجلدي المميز.",
    "C": "Staphylococcus aureus يسبب عدوى موضعية أو جهازية، ما يفسر التسلسل الزمني والطفح المميز هنا.",
    "D": "الكلاميديا تسبب <bdi>symptoms</bdi> تناسلية بس ما تعطي طفح بالراحتين والأخمصين بهالشكل.",
}
HIGHLIGHT_TERMS[38] = ["rash on his palm and soles", "painless ulcer on his penis 6 weeks earlier", "generalised"]

EXPLANATIONS[39] = {
    "idea": "رجل معه لخمول <bdi>chronic</bdi> وحمى وتضخم غدد وسعال وسفر متكرر مع مبيضات فموية، والتحاليل تظهر نقص لمفاويات نسبي، وهذي صورة توحي بفيروس نقص المناعة.",
    "clues": [
        ("lethargy, fever, generalised lymphadenopathy and<br>cough", "<bdi>symptoms</bdi> <bdi>chronic</bdi> معممة توحي ب<bdi>disease</bdi> جهازي مثل HIV"),
        ("oral candidiasis", "عدوى انتهازية توحي بضعف مناعي"),
    ],
    "why_correct": [
        "المبيضات الفموية مع <bdi>symptoms</bdi> جهازية <bdi>chronic</bdi> (تعب، حمى، تضخم غدد، سعال) عند شخص بالغ سليم سابقًا توحي بضعف مناعي مكتسب ب<bdi>cause</bdi> <bdi>HIV</bdi>.",
        "المبيضات الفموية عدوى انتهازية كلاسيكية تظهر عند ضعف المناعة الخلوية، وهذا يميز HIV عن الزهري والتوكسوبلازما والـ<bdi>Brucella</bdi>.",
        "الـ<bdi>Brucella</bdi> والتوكسوبلازما والزهري ما يسببون مبيضات فموية ك<bdi>symptom</bdi> مميز مصاحب لصورتهم المعتادة.",
    ],
    "when_changes": [
        "لو ما فيه مبيضات فموية بس فيه تاريخ لدغة حيوان وحمى موجية مع ألم مفصلي، يميل الـ<bdi>diagnosis</bdi> لل<bdi>Brucella</bdi> بدل HIV.",
    ],
    "rule": "المبيضات الفموية مع <bdi>symptoms</bdi> جهازية <bdi>chronic</bdi> عند بالغ سليم سابقًا توجّه بقوة لفحص HIV.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[39] = {
    "B": "الزهري ما يسبب مبيضات فموية ولا يعطي هالصورة الجهازية الـ<bdi>chronic</bdi> بهالشكل.",
    "C": "الـ<bdi>Brucella</bdi> تعطي حمى موجية وألم مفصلي غالبًا، مو مبيضات فموية ك<bdi>sign</bdi> مميزة.",
    "D": "التوكسوبلازما عند سليم المناعة غالبًا بدون <bdi>symptoms</bdi>، وما تسبب مبيضات فموية.",
}
HIGHLIGHT_TERMS[39] = ["lethargy, fever, generalised lymphadenopathy and", "oral candidiasis"]

EXPLANATIONS[40] = {
    "idea": "رجل <bdi>diabetes</bdi> معه كحة وحمى وتجويف (cavity) بالفص العلوي من الرئة اليسرى، وهذي صورة مشتبه فيها ب<bdi>tuberculosis</bdi> الرئوي النشط، والسؤال يبي نوع الاحتياطات المناسب.",
    "clues": [
        ("cavity at upper lobe of<br>the left lung", "تجويف بالفص العلوي، صورة كلاسيكية لل<bdi>tuberculosis</bdi> الرئوي النشط"),
    ],
    "why_correct": [
        "<bdi>tuberculosis</bdi> الرئوي ينتقل عبر الهواء (<bdi>airborne</bdi>) بجزيئات دقيقة جدًا تبقى معلقة بالهواء، فيحتاج احتياطات هوائية وغرفة ضغط سلبي.",
        "الاحتياطات القطروية (<bdi>droplet</bdi>) أو التماسية (<bdi>contact</bdi>) غير كافية لمنع انتقال <bdi>tuberculosis</bdi> لأن جزيئاته أصغر وتبقى بالهواء أطول.",
        "الاحتياطات القياسية وحدها (<bdi>standard</bdi>) غير كافية أبدًا مع اشتباه ب<bdi>disease</bdi> ينتقل بالهواء زي <bdi>tuberculosis</bdi>.",
    ],
    "when_changes": [
        "لو الصورة الإشعاعية كانت <bdi>pneumonia</bdi> نموذجي بدون تجويف ولا <bdi>factors</bdi> <bdi>risk</bdi> لل<bdi>tuberculosis</bdi>، تكفي الاحتياطات القياسية أو القطروية حسب الـ<bdi>cause</bdi>.",
    ],
    "rule": "أي اشتباه ب<bdi>tuberculosis</bdi> رئوي نشط (تجويف، <bdi>symptoms</bdi> <bdi>chronic</bdi>) يستوجب احتياطات هوائية (airborne) بغرفة ضغط سلبي.",
    "comparison": {
        "headers": ["نوع الاحتياط", "أمثلة <bdi>diseases</bdi>", "طريقة الانتقال"],
        "rows": [
            ["<bdi>Airborne</bdi>", "<bdi>tuberculosis</bdi>، الحصبة، الجدري المائي", "جزيئات دقيقة معلقة بالهواء"],
            ["<bdi>Droplet</bdi>", "الإنفلونزا، السحائية", "رذاذ كبير قريب المدى"],
            ["<bdi>Contact</bdi>", "MRSA، C. difficile", "لمس مباشر أو أسطح ملوثة"],
        ],
    },
    "guideline_note": None,
}
WHY_WRONG[40] = {
    "A": "الاحتياطات القطروية غير كافية لل<bdi>tuberculosis</bdi> لأن جزيئاته أصغر وتبقى معلقة بالهواء لفترة أطول.",
    "B": "الاحتياطات التماسية تناسب عدوى تنتقل باللمس، مو <bdi>tuberculosis</bdi> اللي ينتقل بالهواء.",
    "D": "الاحتياطات القياسية وحدها غير كافية أبدًا مع اشتباه قوي ب<bdi>tuberculosis</bdi> الرئوي النشط.",
}
HIGHLIGHT_TERMS[40] = ["cavity at upper lobe of", "the left lung"]

EXPLANATIONS[41] = {
    "idea": "شاب عنده كحة نوبية <bdi>severe</bdi> بعد نزلة برد <bdi>mild</bdi> رغم تطعيمه ضد السعال الديكي بالطفولة، والسؤال يبي مدة استمرار المناعة بعد التطعيم.",
    "clues": [
        ("paroxysms of coughing", "كحة نوبية <bdi>severe</bdi>، نموذجية للسعال الديكي"),
        ("immunised for pertussis as a child", "تطعيم بالطفولة بس مناعته تضعف مع الوقت"),
    ],
    "why_correct": [
        "مناعة تطعيم السعال الديكي غير دائمة وتضعف خلال سنوات قليلة بعد الجرعات الأساسية بالطفولة، ما يفسر إصابة الـ<bdi>patient</bdi> رغم التطعيم.",
        "هذا يفسر ليش يصاب البالغين بالسعال الديكي رغم أخذهم التطعيم كاملًا وهم أطفال، فتحتاج جرعات تنشيطية لاحقًا.",
        "لو كانت المناعة تدوم مدى الحياة، ما كان يصير عنده كل هالأعراض النوبية الـ<bdi>severe</bdi> بعد سنوات من التطعيم.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> أخذ جرعة تنشيطية حديثة (خلال آخر سنة أو سنتين)، يقل احتمال السعال الديكي ك<bdi>diagnosis</bdi>.",
    ],
    "rule": "مناعة تطعيم السعال الديكي تضعف خلال سنوات قليلة بعد التطعيم الأساسي، فيحتاج جرعات تنشيطية دورية.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[41] = {
    "A": "المناعة ما تكون مدى الحياة، وهذا يخالف حقيقة إصابة الـ<bdi>patient</bdi> رغم التطعيم.",
    "C": "المدة أطول من الفعلية المتوقعة لضعف المناعة بعد التطعيم الأساسي.",
    "D": "المدة أطول بكثير من المتوقع فعليًا لضعف مناعة السعال الديكي.",
}
HIGHLIGHT_TERMS[41] = ["paroxysms of coughing", "immunised for pertussis as a child"]

EXPLANATIONS[42] = {
    "idea": "امرأة معها تقيؤ <bdi>severe</bdi> بعد 4 ساعات من الأكل بمطعم، وهذي فترة حضانة قصيرة جدًا توحي بسم جاهز الصنع من <bdi>Staph aureus</bdi>.",
    "clues": [
        ("severe vomiting 4 hours after having lunch", "فترة حضانة قصيرة جدًا توحي بسم جاهز مو عدوى تحتاج تكاثر"),
    ],
    "why_correct": [
        "<bdi>Staphylococcus aureus</bdi> يفرز سم معوي جاهز بالطعام، فتظهر أعراضه بسرعة <bdi>severe</bdi> (2-6 ساعات) مع تقيؤ <bdi>severe</bdi> وهذا يطابق الوصف.",
        "شيغيلا وكامبيلوباكتر وإي كولاي يحتاجون فترة حضانة أطول بكثير (تحتاج تكاثر بالأمعاء أول)، فما يناسبون هالتوقيت السريع.",
        "غلبة التقيؤ الـ<bdi>severe</bdi> على الإسهال من أبرز <bdi>signs</bdi> التسمم بسم Staph aureus الجاهز.",
    ],
    "when_changes": [
        "لو الـ<bdi>symptoms</bdi> ظهرت بعد 24-72 ساعة مع إسهال دموي، يميل الـ<bdi>cause</bdi> لشيغيلا أو كامبيلوباكتر بدلًا من ستاف.",
    ],
    "rule": "فترة حضانة قصيرة جدًا (ساعات قليلة) بعد الأكل مع تقيؤ <bdi>severe</bdi> توجه لسم Staphylococcus aureus الجاهز.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[42] = {
    "A": "الشيغيلا فترة حضانتها أطول من 4 ساعات وتعطي إسهال دموي بشكل أساسي.",
    "B": "الكامبيلوباكتر فترة حضانته أيام، بعيد جدًا عن 4 ساعات.",
    "C": "الإي كولاي يحتاج فترة حضانة أطول لأنه يحتاج تكاثر بالأمعاء أول.",
}
HIGHLIGHT_TERMS[42] = ["severe vomiting 4 hours after having lunch"]

EXPLANATIONS[43] = {
    "idea": "السؤال يبي تحديد صورة تحليل إلكتروليتات البراز اللي تطابق كوليرا، وهي إسهال إفرازي (سموم) بفجوة أسموزية <bdi>low</bdi>.",
    "clues": [
        ("Vibrio cholerae", "جرثومة تسبب إسهال إفرازي بفجوة أسموزية <bdi>low</bdi> بالبراز"),
    ],
    "why_correct": [
        "الكوليرا إسهال إفرازي ناتج عن سم بكتيري يحفز إفراز الأملاح والماء، وهذا يعطي فجوة أسموزية <bdi>low</bdi> بالبراز (أقل من 50 mOsm/kg).",
        "الفجوة الأسموزية الـ<bdi>low</bdi> (30 mOsm/kg) تدل إن معظم أسمولية البراز مشروحة بالإلكتروليتات المفروزة نفسها، وهذا نموذج الإسهال الإفرازي.",
        "الفجوة الأسموزية الـ<bdi>elevated</bdi> (110) تناسب أكثر إسهال أسموزي (زي سوء امتصاص السكريات)، مو الكوليرا.",
    ],
    "when_changes": [
        "لو الفجوة الأسموزية كانت <bdi>elevated</bdi> جدًا، يميل الـ<bdi>cause</bdi> لإسهال أسموزي (مثل نقص اللاكتيز) مو إفرازي زي الكوليرا.",
    ],
    "rule": "إسهال الكوليرا إفرازي بفجوة أسموزية <bdi>low</bdi> بالبراز، بعكس الإسهال الأسموزي اللي فجوته <bdi>elevated</bdi>.",
    "comparison": {
        "headers": ["نوع الإسهال", "الفجوة الأسموزية", "مثال"],
        "rows": [
            ["إفرازي (Secretory)", "<bdi>low</bdi> (&lt;50)", "الكوليرا"],
            ["أسموزي (Osmotic)", "<bdi>elevated</bdi> (>100)", "نقص اللاكتيز"],
        ],
    },
    "guideline_note": None,
}
WHY_WRONG[43] = {
    "A": "أسمولية البراز وحدها بدون فجوة محسوبة لا تميز نوع الإسهال بدقة.",
    "B": "نفس الفكرة، أسمولية عالية وحدها ما تحدد كون الإسهال إفرازي أو أسموزي.",
    "D": "فجوة أسموزية <bdi>elevated</bdi> (110) تناسب إسهال أسموزي مو إفرازي زي الكوليرا.",
}
HIGHLIGHT_TERMS[43] = ["Vibrio cholerae"]

EXPLANATIONS[44] = {
    "idea": "رجل استبدل صمام قلبي صناعي قبل شهر ومعه حمى وقشعريرة وفقدان وزن مع نبيتة بالـ<bdi>echo</bdi>، وهذي صورة التهاب شغاف صمام صناعي مبكر (خلال أول شهرين بعد الجراحة).",
    "clues": [
        ("Mitral<br>valve replacement by prosthetic valve a month ago", "صمام صناعي حديث خلال أول شهرين، فترة <bdi>risk</bdi> التهاب شغاف مبكر"),
        ("small vegetation", "نبيتة بالـ<bdi>echo</bdi> تؤكد <bdi>endocarditis</bdi>"),
    ],
    "why_correct": [
        "<bdi>endocarditis</bdi> المبكر بعد زراعة صمام صناعي (خلال أول شهرين تقريبًا) سببه الأشيع <bdi>Staphylococcus epidermidis</bdi> (المكورات العنقودية سلبية الكواغيولاز) من تلوث أثناء الجراحة.",
        "العقديات الفموية (<bdi>viridans</bdi>) أشيع ب<bdi>endocarditis</bdi> المتأخر على صمام صناعي أو الصمامات الـ<bdi>normal</bdi>، مو المبكر.",
        "الستافيلوكوكس أوريوس <bdi>cause</bdi> مهم بس أكثر ارتباطًا ب<bdi>endocarditis</bdi> الـ<bdi>acute</bdi> على صمام <bdi>normal</bdi> أو مستخدمي المخدرات الوريدية.",
    ],
    "when_changes": [
        "لو الالتهاب صار بعد أكثر من سنة من زراعة الصمام، تصير العقديات الفموية أو الـ<bdi>causes</bdi> المشابهة للصمام الـ<bdi>normal</bdi> أشيع.",
    ],
    "rule": "<bdi>endocarditis</bdi> المبكر (خلال أول شهرين) بعد زراعة صمام صناعي سببه الأشيع Staphylococcus epidermidis.",
    "comparison": {
        "headers": ["التوقيت", "الـ<bdi>cause</bdi> الأشيع"],
        "rows": [
            ["مبكر (&lt;2 شهر)", "<bdi>Staph epidermidis</bdi>"],
            ["متأخر (>1 سنة)", "<bdi>Streptococcus viridans</bdi>"],
        ],
    },
    "guideline_note": None,
}
WHY_WRONG[44] = {
    "A": "Coxiella burnetii <bdi>cause</bdi> نادر مرتبط بحمى كيو، ما يناسب هالتوقيت المبكر بعد الجراحة.",
    "B": "الستاف أوريوس أشيع ب<bdi>endocarditis</bdi> الـ<bdi>acute</bdi> على صمام <bdi>normal</bdi> مو المبكر على صمام صناعي بهالتوقيت.",
    "C": "العقديات الفموية أشيع ب<bdi>endocarditis</bdi> المتأخر، مو خلال شهر من الجراحة.",
}
HIGHLIGHT_TERMS[44] = ["Mitral", "valve replacement by prosthetic valve a month ago", "small vegetation"]

EXPLANATIONS[45] = {
    "idea": "نفس صورة الزهري الثانوي (طفح بالراحتين والأخمصين بعد قرحة تناسلية غير مؤلمة)، مع تاريخ سفر وعلاقة غير محمية يدعم احتمال <bdi>disease</bdi> منقول جنسيًا.",
    "clues": [
        ("painless ulcer on his penis", "قرحة تناسلية غير مؤلمة (chancre)، <bdi>sign</bdi> الزهري الأولي"),
        ("extramarital unprotected sex", "سلوك جنسي عالي الخطورة يدعم احتمال <bdi>disease</bdi> منقول جنسيًا"),
        ("generalized lymphadenopathy", "تضخم غدد لمفاوية معمم، متوافق مع الزهري الثانوي"),
    ],
    "why_correct": [
        "قرحة تناسلية غير مؤلمة قبل 6 أسابيع تتبعها طفح بالراحتين والأخمصين وتضخم غدد معمم صورة كلاسيكية للزهري الثانوي.",
        "الهربس النطاقي يعطي طفح حويصلي بتوزيع عصبي محدد مو منتشر بالراحتين والأخمصين، فلا يناسب.",
        "الكلاميديا وHIV ما يسببون هالتسلسل المميز من قرحة غير مؤلمة ثم طفح كفي أخمصي.",
    ],
    "when_changes": [
        "لو القرحة كانت مؤلمة مع تضخم غدد موضعي مؤلم، يميل الـ<bdi>diagnosis</bdi> للهربس التناسلي بدل الزهري.",
    ],
    "rule": "طفح بالراحتين والأخمصين بعد قرحة تناسلية غير مؤلمة يعني زهري ثانوي حتى يثبت العكس.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[45] = {
    "A": "HIV لا يعطي هالتسلسل المميز من قرحة غير مؤلمة ثم طفح كفي أخمصي بهالشكل.",
    "C": "الهربس النطاقي يعطي توزيع عصبي محدد للطفح، مو منتشر بالراحتين والأخمصين.",
    "D": "الكلاميديا تسبب <bdi>symptoms</bdi> تناسلية موضعية، ما تعطي هالطفح المميز.",
}
HIGHLIGHT_TERMS[45] = ["painless ulcer on his penis", "extramarital unprotected sex", "generalized lymphadenopathy"]

EXPLANATIONS[46] = {
    "idea": "طبيب بيطري معه تعب <bdi>chronic</bdi> وألم ظهر وحمى مع <bdi>symptoms</bdi> عصبية نفسية وتضخم كبد وطحال وألم بمفصل العجزي الحرقفي، وهذي صورة كلاسيكية لل<bdi>Brucella</bdi> (مهنة تعرّض للحيوانات).",
    "clues": [
        ("veterinarian", "مهنة معرضة للتماس مع حيوانات، <bdi>factor</bdi> <bdi>risk</bdi> رئيسي لل<bdi>Brucella</bdi>"),
        ("mood /behaviour changes and paraesthesia", "<bdi>symptoms</bdi> عصبية نفسية، <bdi>complication</bdi> معروفة لل<bdi>Brucella</bdi>"),
        ("tender right sacroiliac joint", "التهاب المفصل العجزي الحرقفي، <bdi>complication</bdi> عظمية مفصلية شائعة بالـ<bdi>Brucella</bdi>"),
        ("mild hepatosplenomegaly", "تضخم كبد وطحال <bdi>mild</bdi>، متوافق مع الـ<bdi>Brucella</bdi>"),
    ],
    "why_correct": [
        "مهنة الطبيب البيطري (تماس مع حيوانات) مع تعب <bdi>chronic</bdi> وحمى وألم عجزي حرقفي وتغيرات نفسية عصبية وتضخم كبد وطحال صورة كلاسيكية جدًا لل<bdi>Brucella</bdi>.",
        "<bdi>tuberculosis</bdi> يعطي <bdi>symptoms</bdi> تنفسية بارزة أكثر عادة، والزهري والتوكسوبلازما ما يفسران المهنة وألم المفصل العجزي الحرقفي المميز.",
        "التغيرات العصبية النفسية من <bdi>complications</bdi> الـ<bdi>Brucella</bdi> المعروفة (neurobrucellosis) وتدعم الـ<bdi>diagnosis</bdi> أكثر.",
    ],
    "when_changes": [
        "لو الزراعة الدموية طلعت مكورات عصوية سالبة الغرام، يتأكد الـ<bdi>diagnosis</bdi> أكثر وتصير الـ<bdi>step</bdi> التالية اختبار التراص (agglutination test).",
    ],
    "rule": "تعب <bdi>chronic</bdi> وحمى وألم عجزي حرقفي عند شخص متعرض للحيوانات (زي الطبيب البيطري) يوجّه بقوة لل<bdi>Brucella</bdi>.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[46] = {
    "A": "الزهري ما يفسر ألم المفصل العجزي الحرقفي ولا المهنة المعرضة للحيوانات.",
    "C": "<bdi>tuberculosis</bdi> يعطي <bdi>symptoms</bdi> تنفسية بارزة أكثر عادة، وهذا غير مذكور بالسؤال.",
    "D": "التوكسوبلازما عند سليم المناعة غالبًا بدون <bdi>symptoms</bdi> بهالشدة، وما تفسر المهنة المذكورة.",
}
HIGHLIGHT_TERMS[46] = ["veterinarian", "mood /behaviour changes and paraesthesia", "tender right sacroiliac joint"]

EXPLANATIONS[47] = {
    "idea": "نفس صورة الـ<bdi>Brucella</bdi> عند الطبيب البيطري، والسؤال هذي المرة عن أفضل <bdi>step</bdi> تشخيصية تالية لتأكيد الـ<bdi>diagnosis</bdi>.",
    "clues": [
        ("veterinarian", "مهنة معرضة للتماس مع حيوانات، <bdi>factor</bdi> <bdi>risk</bdi> لل<bdi>Brucella</bdi>"),
        ("tender right sacroiliac joint", "التهاب المفصل العجزي الحرقفي، <bdi>complication</bdi> شائعة بالـ<bdi>Brucella</bdi>"),
    ],
    "why_correct": [
        "اختبار التراص الأنبوبي (<bdi>Tube agglutination test</bdi>) هو الفحص المصلي القياسي لتأكيد <bdi>diagnosis</bdi> الـ<bdi>Brucella</bdi>.",
        "وظائف الكبد وأشعة المفصل العجزي الحرقفي فحوصات داعمة بس ما تأكد الـ<bdi>diagnosis</bdi> النوعي لل<bdi>Brucella</bdi>.",
        "اختبار السلين (<bdi>tuberculin skin test</bdi>) يخص <bdi>tuberculosis</bdi>، والصورة هنا لا توحي ب<bdi>tuberculosis</bdi> بشكل أساسي.",
    ],
    "when_changes": [
        "لو الزراعة الدموية طلعت سلبية والشك قوي مستمر، يُعاد التراص بعد أسابيع لرصد ارتفاع العيار (titer).",
    ],
    "rule": "اختبار التراص الأنبوبي هو الفحص التأكيدي المصلي القياسي ل<bdi>diagnosis</bdi> الـ<bdi>Brucella</bdi>.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[47] = {
    "A": "وظائف الكبد فحص داعم عام، ما يؤكد <bdi>diagnosis</bdi> الـ<bdi>Brucella</bdi> تحديدًا.",
    "B": "أشعة المفصل العجزي الحرقفي <bdi>assessment</bdi> لل<bdi>complication</bdi>، مو تأكيد لل<bdi>diagnosis</bdi> النوعي.",
    "C": "اختبار السلين يخص <bdi>diagnosis</bdi> <bdi>tuberculosis</bdi>، وصورة الـ<bdi>patient</bdi> هنا لا توحي ب<bdi>tuberculosis</bdi>.",
}
HIGHLIGHT_TERMS[47] = ["veterinarian", "tender right sacroiliac joint"]

EXPLANATIONS[48] = {
    "idea": "رجل عنده التهاب سحايا بروسيلي (neurobrucellosis) بدأ على ريفامبيسين ودوكسيسايكلين، والسؤال يبي مدة الـ<bdi>treatment</bdi> المناسبة لهالشكل الـ<bdi>severe</bdi> من الـ<bdi>Brucella</bdi>.",
    "clues": [
        ("neurobrucellosis", "شكل <bdi>severe</bdi> من الـ<bdi>Brucella</bdi> يصيب الجهاز العصبي المركزي"),
        ("rifampicin", "أحد أدوية الـ<bdi>treatment</bdi> المركب لل<bdi>Brucella</bdi>"),
    ],
    "why_correct": [
        "التهاب سحايا/جهاز عصبي بالـ<bdi>Brucella</bdi> (<bdi>neurobrucellosis</bdi>) يحتاج <bdi>treatment</bdi> مطوّل يصل حتى 6 أشهر بعكس الـ<bdi>Brucella</bdi> غير المعقدة.",
        "المدد الأقصر (6 أو 8 أسابيع) كافية لل<bdi>Brucella</bdi> غير المعقدة بس غير كافية للشكل العصبي الـ<bdi>severe</bdi>.",
        "4 أشهر أيضًا أقل من المطلوب لضمان القضاء الكامل على الجرثومة من الجهاز العصبي المركزي.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>Brucella</bdi> غير معقدة بدون إصابة عصبية أو عظمية، تكفي مدة أقصر (6 أسابيع تقريبًا).",
    ],
    "rule": "التهاب الجهاز العصبي المركزي بالـ<bdi>Brucella</bdi> (neurobrucellosis) يحتاج <bdi>treatment</bdi> مطوّل حتى 6 أشهر.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[48] = {
    "A": "6 أسابيع مدة كافية لل<bdi>Brucella</bdi> غير المعقدة بس قصيرة جدًا للشكل العصبي.",
    "B": "8 أسابيع أيضًا أقصر من المطلوب ل<bdi>treatment</bdi> neurobrucellosis بشكل كافٍ.",
    "C": "4 أشهر أقل من المدة الموصى بها لضمان القضاء الكامل على العدوى العصبية.",
}
HIGHLIGHT_TERMS[48] = ["neurobrucellosis", "rifampicin"]

EXPLANATIONS[49] = {
    "idea": "<bdi>patient</bdi> إيدز على <bdi>treatment</bdi> مضاد للفيروسات معه <bdi>symptoms</bdi> عصبية بؤرية مع ارتفاع أضداد التوكسوبلازما وآفات متعددة بالرنين، وهذي صورة كلاسيكية لالتهاب دماغ التوكسوبلازما عند ضعف المناعة.",
    "clues": [
        ("known case with AIDS", "ضعف مناعة <bdi>severe</bdi> يهيئ لعدوى انتهازية بالدماغ"),
        ("rising titers of anti- toxoplasma immunoglobulin G (IgG) antibodies and positive immunoglobulin M (IgM)", "دليل مصلي على عدوى توكسوبلازما نشطة"),
        ("multiple hypodense lesions in white matter and basal ganglia", "آفات متعددة بالرنين، صورة كلاسيكية لالتهاب دماغ التوكسوبلازما"),
    ],
    "why_correct": [
        "الآفات المتعددة بالمادة البيضاء والعقد القاعدية مع دليل مصلي على توكسوبلازما نشطة عند <bdi>patient</bdi> إيدز صورة كلاسيكية لالتهاب دماغ التوكسوبلازما.",
        "<bdi>Sulfadiazine</bdi> مع <bdi>pyrimethamine</bdi> هو الـ<bdi>treatment</bdi> القياسي الأول المعتمد لالتهاب دماغ التوكسوبلازما.",
        "باقي التوليفات (ريفامبيسين وسيفوروكسيم، دوكسيسايكلين وكليندامايسين، كلورامفينيكول ولوكوفورين) ما تعتبر <bdi>treatment</bdi> قياسي أول لهالحالة.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عنده حساسية للسلفا، يصير بديل معتمد هو <bdi>pyrimethamine</bdi> مع <bdi>clindamycin</bdi> بدل السلفاديازين.",
    ],
    "rule": "التهاب دماغ التوكسوبلازما عند <bdi>patient</bdi> الإيدز يُعالج بـ Sulfadiazine مع Pyrimethamine كخط أول.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[49] = {
    "A": "ريفامبيسين وسيفوروكسيم ما يغطيان التوكسوبلازما ولا يعتبران <bdi>treatment</bdi> معتمد لهالعدوى.",
    "B": "دوكسيسايكلين وكليندامايسين ليست التوليفة القياسية الأولى لالتهاب دماغ التوكسوبلازما.",
    "C": "كلورامفينيكول ما له دور علاجي معتمد بهالعدوى، واللوكوفورين مساعد فقط لتقليل سمية الـ<bdi>treatment</bdi> الأساسي.",
}
HIGHLIGHT_TERMS[49] = ["known case with AIDS", "multiple hypodense lesions in white matter and basal ganglia"]

EXPLANATIONS[50] = {
    "idea": "امرأة معها لخبطة ذهنية وخمول وحمى وتيبس <bdi>mild</bdi> بالرقبة مع منطقة <bdi>low</bdi> الكثافة بالفص الصدغي الجداري اليميني، وهذي صورة كلاسيكية لالتهاب دماغ الهربس البسيط.",
    "clues": [
        ("confusion, lethargy and fever", "<bdi>symptoms</bdi> التهاب دماغي <bdi>acute</bdi>"),
        ("mild neck stiffness", "تيبس رقبة <bdi>mild</bdi> يدعم تهيج سحائي مصاحب"),
        ("low attenuation at right tempo-parietal region", "موقع كلاسيكي جدًا لالتهاب دماغ الهربس البسيط"),
    ],
    "why_correct": [
        "التوضع الصدغي الجداري للآفة بالأشعة المقطعية <bdi>sign</bdi> كلاسيكية جدًا ومميزة لالتهاب دماغ الهربس البسيط (<bdi>HSV encephalitis</bdi>).",
        "خراج الدماغ عادة يعطي كتلة محددة بحلقة تعزيز واضحة أكثر مو مجرد انخفاض كثافة منتشر بالفص الصدغي.",
        "التهاب سحايا المكورات الرئوية والليستيريا يعطون صورة سحائية بدون تخصص بالفص الصدغي بهالشكل المميز.",
    ],
    "when_changes": [
        "لو الأشعة أظهرت خراج بحلقة تعزيز واضحة مع كتلة محددة، يميل الـ<bdi>diagnosis</bdi> لخراج دماغي بدل الهربس.",
    ],
    "rule": "آفة <bdi>low</bdi> الكثافة بالفص الصدغي مع لخبطة وحمى تعني التهاب دماغ الهربس البسيط حتى يثبت العكس.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[50] = {
    "A": "خراج الدماغ يعطي كتلة محددة بحلقة تعزيز واضحة أكثر من مجرد انخفاض كثافة منتشر.",
    "B": "التهاب سحايا المكورات الرئوية يعطي صورة سحائية عامة بدون تخصص بالفص الصدغي.",
    "D": "التهاب سحايا الليستيريا لا يرتبط بهالتوضع الصدغي المميز بالأشعة.",
}
HIGHLIGHT_TERMS[50] = ["confusion, lethargy and fever", "mild neck stiffness", "low attenuation at right tempo-parietal region"]

EXPLANATIONS[51] = {
    "idea": "امرأة شابة معها حمى وألم عضلي والتهاب حلق مع طفح بعد أخذ أموكسيسيلين وتضخم غدد معمم، وهذي صورة كلاسيكية للعدوى بكثرة الوحيدات العدوائية (EBV) مع طفح دوائي مميز.",
    "clues": [
        ("fever, myalgia and<br>pharyngitis", "التهاب حلق مع حمى وألم عضلي، صورة توحي بعدوى فيروسية جهازية"),
        ("macular rash over the trunk after she received amoxicillin", "طفح مميز جدًا يظهر بعد الأموكسيسيلين عند مرضى كثرة الوحيدات العدوائية"),
        ("generalised lymphadenopathy", "تضخم غدد معمم متوافق مع كثرة الوحيدات العدوائية"),
    ],
    "why_correct": [
        "ظهور طفح جلدي بعد أخذ أموكسيسيلين عند <bdi>patient</bdi> بالتهاب حلق وحمى وتضخم غدد معمم <bdi>sign</bdi> كلاسيكية ومميزة جدًا لكثرة الوحيدات العدوائية (<bdi>Infectious mononucleosis</bdi>).",
        "هالطفح يحصل ب<bdi>cause</bdi> تفاعل مناعي مؤقت مع الأموكسيسيلين عند وجود عدوى EBV نشطة، وليس حساسية دوائية حقيقية دائمة.",
        "الدفتيريا وسايتوميغالوفيروس ما يعطون هالطفح المميز المرتبط تحديدًا بالأموكسيسيلين، و<bdi>disease</bdi> هودجكن <bdi>chronic</bdi> ولا يفسر الـ<bdi>symptoms</bdi> الـ<bdi>acute</bdi> الحالية.",
    ],
    "when_changes": [
        "لو الطفح ظهر بدون علاقة بأخذ أموكسيسيلين ومع حمى <bdi>chronic</bdi> وتضخم غدد ثابت لأسابيع، يفكر ب<bdi>disease</bdi> هودجكن بدلًا من ذلك.",
    ],
    "rule": "طفح جلدي بعد أموكسيسيلين عند <bdi>patient</bdi> بالتهاب حلق وحمى وتضخم غدد معمم يعني كثرة الوحيدات العدوائية حتى يثبت العكس.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[51] = {
    "A": "الدفتيريا تعطي غشاء بلعومي مميز، مو طفح مرتبط بالأموكسيسيلين.",
    "B": "<bdi>disease</bdi> هودجكن <bdi>chronic</bdi> التطور ولا يفسر الحمى والالتهاب الحلقي الـ<bdi>acute</bdi> المصاحب للطفح الدوائي.",
    "D": "سايتوميغالوفيروس يعطي صورة مشابهة بس أقل ارتباطًا بهالطفح المميز بعد الأموكسيسيلين تحديدًا.",
}
HIGHLIGHT_TERMS[51] = ["fever, myalgia and", "macular rash over the trunk after she received amoxicillin", "generalised lymphadenopathy"]

EXPLANATIONS[52] = {
    "idea": "امرأة كبيرة معها التهاب سحايا وصبغة غرام تظهر مكورات عصوية سالبة الغرام (توحي بالمستدمية النزلية)، والسؤال يبي الوقاية الدوائية المناسبة لمخالطيها.",
    "clues": [
        ("Gram negative cocco-bacilli", "شكل الجرثومة يوحي بالمستدمية النزلية (Haemophilus influenzae)"),
    ],
    "why_correct": [
        "المكورات العصوية سالبة الغرام بصبغة السائل الشوكي توحي بالمستدمية النزلية (<bdi>Haemophilus influenzae</bdi>)، والوقاية القياسية لمخالطيها هي <bdi>Rifampicin</bdi>.",
        "السيفترياكسون <bdi>treatment</bdi> لل<bdi>patient</bdi> نفسها مو وقاية للمخالطين، والأزيثرومايسين والسيبروفلوكساسين ليسا الخيار القياسي لوقاية مخالطي المستدمية النزلية.",
        "الوقاية الدوائية للمخالطين تهدف لمنع نقل الجرثومة قبل ظهور <bdi>symptoms</bdi> عندهم.",
    ],
    "when_changes": [
        "لو الصبغة أظهرت مكورات <bdi>bilateral</bdi> سالبة الغرام (ديبلوكوكاي) بدل عصويات، يتجه الـ<bdi>diagnosis</bdi> للمكورات السحائية والوقاية تبقى ريفامبيسين أو سيبروفلوكساسين حسب البروتوكول.",
    ],
    "rule": "الريفامبيسين هو الوقاية الدوائية القياسية لمخالطي <bdi>patient</bdi> التهاب سحايا بالمستدمية النزلية.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[52] = {
    "B": "السيفترياكسون <bdi>treatment</bdi> لل<bdi>patient</bdi> المصابة نفسها، مو وقاية للمخالطين.",
    "C": "السيبروفلوكساسين يستخدم أكثر لوقاية مخالطي المكورات السحائية مو المستدمية النزلية تحديدًا.",
    "D": "الأزيثرومايسين ليس الخيار القياسي المعتمد لوقاية مخالطي هالجرثومة.",
}
HIGHLIGHT_TERMS[52] = ["Gram negative cocco-bacilli"]

EXPLANATIONS[53] = {
    "idea": "رجل معه حمى متقطعة كل يومين بنمط كلاسيكي (قشعريرة ثم حمى ثم تعرق) بعد سفر للسودان، بس اللطاخة الدموية طلعت سلبية، والسؤال يبي الـ<bdi>step</bdi> التشخيصية التالية.",
    "clues": [
        ("recurrent attacks of high-grade fever with<br>chills", "نمط حمى نوبي متكرر، كلاسيكي للملاريا"),
        ("The attacks comes<br>every other day", "نمط زمني محدد (يوم بيني) يوحي بنوع معين من الملاريا"),
        ("Blood smear at Emergency Room<br>was negative for parasites", "لطاخة سلبية واحدة لا تنفي الملاريا ب<bdi>cause</bdi> تذبذب مستوى الطفيلي بالدم"),
    ],
    "why_correct": [
        "مستوى الطفيليات بالدم يتذبذب مع دورة الحمى، فلطاخة واحدة سلبية ما تنفي الملاريا، ولازم تكرار اللطاخة كل 8 ساعات لمدة يومين لزيادة حساسية الكشف.",
        "تكرار لطاخة واحدة بس (سميكة أو رفيعة) أو أثناء نوبة حمى واحدة فقط غير كافٍ، لأن الطفيلي ممكن يكون بمستوى <bdi>low</bdi> جدًا وقتها بالذات.",
        "الصورة السريرية (سفر لمنطقة موبوءة، حمى نوبية، تضخم طحال) تدعم استمرار الاشتباه بالملاريا رغم اللطاخة الأولى السلبية.",
    ],
    "when_changes": [
        "لو تكررت اللطاخات وبقيت سلبية مع استمرار الاشتباه القوي، يُلجأ لاختبارات أحدث زي اختبار الأنتيجين السريع (RDT) أو PCR.",
    ],
    "rule": "اللطاخة الدموية السلبية الواحدة لا تنفي الملاريا، ويلزم تكرارها كل 8 ساعات لمدة يومين لتأكيد النفي.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[53] = {
    "A": "لطاخة رفيعة واحدة إضافية غير كافية لأن مستوى الطفيلي يتذبذب مع الوقت.",
    "B": "تكرار لطاخة سميكة واحدة فقط غير كافٍ لضمان اكتشاف مستوى طفيلي <bdi>low</bdi> مؤقت.",
    "C": "الانتظار لنوبة حمى واحدة بس فرصة ضائعة، والأدق تكرار منتظم كل 8 ساعات لعدة أيام.",
}
HIGHLIGHT_TERMS[53] = ["recurrent attacks of high-grade fever with", "The attacks comes", "Blood smear at Emergency Room"]

EXPLANATIONS[54] = {
    "idea": "امرأة معها صداع <bdi>severe</bdi> وتيبس رقبة وحمى و<bdi>sign</bdi> كيرنيغ إيجابية مع سائل شوكي عكر وجلوكوز <bdi>low</bdi> جدًا وبروتين <bdi>elevated</bdi>، وهذي صورة التهاب سحايا بكتيري <bdi>acute</bdi>، وأشيع <bdi>cause</bdi> عند البالغين السليمين هو المكورات الرئوية.",
    "clues": [
        ("positive Kernig's sign", "<bdi>sign</bdi> تهيج سحائي إيجابية"),
        ("Colour Turbid", "عكارة السائل الشوكي توحي بالتهاب بكتيري"),
        ("Glucose 1.6", "جلوكوز <bdi>low</bdi> جدًا مقارنة بالـ<bdi>normal</bdi>، يدعم البكتيري"),
    ],
    "why_correct": [
        "<bdi>Streptococcus pneumoniae</bdi> هو أشيع <bdi>cause</bdi> التهاب سحايا بكتيري عند البالغين السليمين سابقًا خارج فترة الوليد أو الحمل.",
        "الليستيريا مونوسايتوجينز أشيع بكبار السن أو ضعاف المناعة أو الحوامل، وهذا غير مذكور هنا.",
        "الإي كولاي أشيع بالمواليد الجدد، والستافيلوكوكس بايوجينس <bdi>cause</bdi> نادر ل<bdi>meningitis</bdi> مقارنة بالمكورات الرئوية.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> حامل أو كبيرة بالسن أو ضعيفة المناعة، يصير احتمال الليستيريا أقوى ويضاف الأمبيسيلين للتغطية التجريبية.",
    ],
    "rule": "المكورات الرئوية هي أشيع <bdi>cause</bdi> التهاب سحايا بكتيري عند البالغين السليمين سابقًا.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[54] = {
    "A": "الإي كولاي أشيع <bdi>cause</bdi> بالمواليد الجدد، مو بالبالغة السليمة هنا.",
    "B": "الليستيريا أشيع بكبار السن أو الحوامل أو ضعاف المناعة، وهذا غير مذكور بالسؤال.",
    "D": "الستافيلوكوكس بايوجينس <bdi>cause</bdi> نادر جدًا ل<bdi>meningitis</bdi> مقارنة بالمكورات الرئوية.",
}
HIGHLIGHT_TERMS[54] = ["positive Kernig's sign", "Colour Turbid", "Glucose 1.6"]

EXPLANATIONS[55] = {
    "idea": "رجل معه إسهال دموي <bdi>acute</bdi> وألم بطن وحمى بعد سفر لإندونيسيا، والزراعة أكدت الكامبيلوباكتر، والسؤال يبي أفضل <bdi>treatment</bdi>.",
    "clues": [
        ("stool culture is positive for Campylobacter", "تأكيد الـ<bdi>diagnosis</bdi> بالزراعة يحدد اختيار المضاد الحيوي المناسب"),
    ],
    "why_correct": [
        "<bdi>Azithromycin</bdi> هو الـ<bdi>treatment</bdi> المفضل حاليًا لعدوى الكامبيلوباكتر المؤكدة، خصوصًا مع تزايد مقاومة الكامبيلوباكتر للسيبروفلوكساسين عالميًا.",
        "<bdi>Ciprofloxacin</bdi> كان يستخدم سابقًا بس صارت مقاومة الكامبيلوباكتر له واسعة الانتشار، فما يُفضّل كخط أول.",
        "<bdi>Metronidazole</bdi> و<bdi>Amoxicillin</bdi> ما يعتبران <bdi>treatment</bdi> قياسي فعال معتمد لعدوى الكامبيلوباكتر.",
    ],
    "when_changes": [
        "لو الـ<bdi>case</bdi> <bdi>mild</bdi> ومحدودة لنفسها بدون حمى <bdi>severe</bdi> أو دم بالبراز، يكتفى بالـ<bdi>treatment</bdi> الداعم بدون مضاد حيوي.",
    ],
    "rule": "الأزيثرومايسين هو الـ<bdi>treatment</bdi> المفضل حاليًا لعدوى الكامبيلوباكتر المؤكدة ب<bdi>cause</bdi> انتشار مقاومة الكينولونات.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[55] = {
    "A": "الميترونيدازول ما له فعالية معتمدة ضد الكامبيلوباكتر.",
    "B": "السيبروفلوكساسين صارت مقاومة الكامبيلوباكتر له واسعة، فما يُفضّل كخط أول.",
    "D": "الأموكسيسيلين ما يعتبر <bdi>treatment</bdi> قياسي فعال لعدوى الكامبيلوباكتر.",
}
HIGHLIGHT_TERMS[55] = ["stool culture is positive for Campylobacter"]

EXPLANATIONS[56] = {
    "idea": "رجل معه إسهال مائي مستمر وفقدان وزن بعد سفر لمصر، والزراعة العادية طلعت سلبية، وهذي صورة كلاسيكية لداء الجيارديا اللي ما يظهر دايمًا بالزراعة أو الفحص العادي للبراز.",
    "clues": [
        ("persistent watery diarrhea", "إسهال مائي مستمر، نموذجي لداء الجيارديا"),
        ("stool sample that came back negative", "الفحص العادي للبراز قد يكون سلبيًا كاذبًا بالجيارديا لأنه يحتاج فحص نوعي متكرر"),
    ],
    "why_correct": [
        "داء الجيارديا يعطي إسهال مائي <bdi>chronic</bdi> مع فقدان وزن، والطفيلي يُطرح بشكل متقطع فممكن تطلع عينة براز واحدة سلبية رغم وجود العدوى فعلًا.",
        "الشيغيلا والأميبا يعطون غالبًا إسهال دموي أو زحاري أكثر من إسهال مائي <bdi>chronic</bdi> بحت.",
        "<bdi>ulcerative colitis</bdi> <bdi>disease</bdi> <bdi>chronic</bdi> بس ما يرتبط بالضرورة بسفر حديث، والسياق هنا يوجه أكثر لعدوى طفيلية مكتسبة بالسفر.",
    ],
    "when_changes": [
        "لو الفحص المتكرر للبراز أو اختبار الأنتيجين النوعي طلع إيجابي للجيارديا، يتأكد الـ<bdi>diagnosis</bdi> ويبدأ <bdi>treatment</bdi> الميترونيدازول.",
    ],
    "rule": "إسهال مائي <bdi>chronic</bdi> بعد سفر مع فحص براز أولي سلبي لا ينفي الجيارديا، لأن الطفيلي يُطرح بشكل متقطع.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[56] = {
    "B": "الشيغيلا تعطي غالبًا إسهال دموي زحاري <bdi>acute</bdi> أكثر من إسهال مائي <bdi>chronic</bdi>.",
    "C": "الأميبا تعطي غالبًا إسهال دموي مخاطي، مو إسهال مائي بحت بهالشكل الـ<bdi>chronic</bdi>.",
    "D": "<bdi>ulcerative colitis</bdi> <bdi>disease</bdi> مناعي <bdi>chronic</bdi> ولا يرتبط بشكل مباشر بسفر حديث لمنطقة موبوءة.",
}
HIGHLIGHT_TERMS[56] = ["persistent watery diarrhea", "stool sample that came back negative"]

EXPLANATIONS[57] = {
    "idea": "رجل معه حمى وسعال منتج وتسلل بالفص الأوسط الأيمن بالأشعة، وهذي صورة <bdi>pneumonia</bdi> مكتسب من المجتمع (<bdi>CAP</bdi>)، والسؤال يبي <bdi>treatment</bdi> تجريبي فوري مناسب ل<bdi>patient</bdi> من دون <bdi>factors</bdi> <bdi>risk</bdi> واضحة تستدعي تغطية أوسع.",
    "clues": [
        ("productive<br>cough", "<bdi>symptoms</bdi> تنفسية سفلية توحي ب<bdi>pneumonia</bdi>"),
        ("Right middle lobe infiltrate", "تسلل رئوي مؤكد بالأشعة"),
    ],
    "why_correct": [
        "<bdi>Moxifloxacin</bdi> (كينولون تنفسي) خط <bdi>treatment</bdi> تجريبي معتمد وفعال وحيد ل<bdi>pneumonia</bdi> مكتسب من المجتمع يحتاج دخول مستشفى، يغطي الجراثيم النموذجية وغير النموذجية معًا.",
        "<bdi>Ceftazidime</bdi> و<bdi>Meropenem</bdi> و<bdi>Piperacillin/Tazobactam</bdi> تغطية أوسع مخصصة لعدوى مستشفوية أو زائفة، وهذا غير مناسب ل<bdi>pneumonia</bdi> مجتمعي بسيط نسبيًا.",
        "الإفراط بمضادات واسعة الطيف بدون داعٍ يزيد <bdi>risk</bdi> المقاومة والآثار الجانبية دون فائدة إضافية بهالحالة.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عنده <bdi>diseases</bdi> مصاحبة (<bdi>diabetes</bdi>، قصور كلوي، <bdi>diseases</bdi> قلب <bdi>chronic</bdi>)، يُفضّل توليفة بيتالاكتام مع ماكروليد بدل الكينولون المفرد.",
    ],
    "rule": "الكينولون التنفسي (Moxifloxacin) خيار تجريبي فعال ل<bdi>pneumonia</bdi> مكتسب من المجتمع بدون <bdi>factors</bdi> <bdi>risk</bdi> لجراثيم مقاومة.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[57] = {
    "B": "Ceftazidime تغطية موسعة تستخدم أكثر لعدوى مستشفوية أو زائفة، مو خط أول ل<bdi>pneumonia</bdi> مجتمعي بسيط.",
    "C": "Meropenem مضاد واسع الطيف جدًا محجوز لعدوى <bdi>severe</bdi> مقاومة، مبالغ فيه هنا.",
    "D": "Piperacillin/Tazobactam أيضًا تغطية أوسع من اللازم ل<bdi>pneumonia</bdi> مجتمعي بدون <bdi>factors</bdi> <bdi>risk</bdi> واضحة.",
}
HIGHLIGHT_TERMS[57] = ["productive", "Right middle lobe infiltrate"]

EXPLANATIONS[58] = {
    "idea": "رجل شاب معه لخبطة وتشنجات مع تاريخ علاقات جنسية غير محمية متعددة، والمستضد الكريبتوكوكي إيجابي، وهذي صورة قوية توحي بضعف مناعة كامن ب<bdi>cause</bdi> HIV يستدعي فحصه.",
    "clues": [
        ("multiple unprotected sexual contact for the last 6 years", "سلوك جنسي عالي الخطورة يزيد احتمال HIV"),
        ("Serum Cryptococcal Antigen: Positive", "عدوى انتهازية فطرية توحي بضعف مناعي كامن"),
        ("WBC 1.3", "نقص <bdi>severe</bdi> بكريات الدم البيضاء، يدعم ضعف مناعي <bdi>severe</bdi>"),
    ],
    "why_correct": [
        "التهاب سحايا كريبتوكوكي عند شاب بسلوك جنسي عالي الخطورة ونقص <bdi>severe</bdi> بكريات الدم البيضاء يوجّه بقوة لضعف مناعي كامن ب<bdi>cause</bdi> HIV، ولازم يُفحص فورًا.",
        "الكريبتوكوكوس عدوى انتهازية كلاسيكية تظهر بشكل أساسي عند ضعف المناعة الخلوية الـ<bdi>severe</bdi> زي مرضى HIV المتقدم.",
        "فحص PCR للتوكسوبلازما أو الهربس أو زراعة الزهري فحوصات ثانوية بس لا تفسر <bdi>cause</bdi> ضعف المناعة الأساسي المؤدي لهالعدوى الانتهازية.",
    ],
    "when_changes": [
        "لو ثبت HIV إيجابي، تصير الـ<bdi>step</bdi> التالية قياس عدد CD4 وبدء <bdi>treatment</bdi> الكريبتوكوكوس المناسب مع <bdi>treatment</bdi> مضاد للفيروسات لاحقًا.",
    ],
    "rule": "أي عدوى انتهازية فطرية زي الكريبتوكوكوس ب<bdi>patient</bdi> ب<bdi>factors</bdi> <bdi>risk</bdi> جنسية يستوجب فحص HIV فورًا.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[58] = {
    "B": "PCR للتوكسوبلازما فحص ثانوي، ما يفسر <bdi>cause</bdi> ضعف المناعة الأساسي هنا.",
    "C": "زراعة السائل الشوكي للزهري لا ترتبط مباشرة بصورة الكريبتوكوكوس ونقص المناعة الـ<bdi>severe</bdi>.",
    "D": "PCR للهربس البسيط يخص <bdi>diagnosis</bdi> ثاني مختلف، ما يفسر وجود عدوى انتهازية فطرية أصلًا.",
}
HIGHLIGHT_TERMS[58] = ["multiple unprotected sexual contact for the last 6 years", "Serum Cryptococcal Antigen: Positive", "WBC 1.3"]

EXPLANATIONS[59] = {
    "idea": "رجل شخص حديثًا بـ HIV جاي للاستشارة، والسؤال يبي لمن يجب إخباره بحالته من ناحية أخلاقية وقانونية.",
    "clues": [
        ("counselling", "استشارة تتضمن مناقشة الإفصاح عن الـ<bdi>case</bdi> للمخالطين المعرضين لل<bdi>risk</bdi>"),
    ],
    "why_correct": [
        "الزوجة تعتبر شريك جنسي حالي معرض مباشر ل<bdi>risk</bdi> انتقال العدوى، فمن واجب الـ<bdi>patient</bdi> الأخلاقي (وأحيانًا القانوني) إبلاغها لحمايتها واختبارها.",
        "الوالدين والأخ ليسوا بمعرض <bdi>risk</bdi> مباشر لانتقال HIV منه بالحياة اليومية العادية، فلا يوجد <bdi>cause</bdi> طبي يوجب إخبارهم.",
        "صاحب العمل ليس له علاقة بخصوصية الـ<bdi>case</bdi> الصحية ولا يشكل <bdi>risk</bdi> انتقال، فإفصاح له ينتهك خصوصية الـ<bdi>patient</bdi> بدون مبرر طبي.",
    ],
    "when_changes": [
        "لو رفض الـ<bdi>patient</bdi> إخبار زوجته رغم الاستشارة المتكررة، يحق للطبيب أحيانًا (حسب الأنظمة المحلية) إبلاغها مباشرة لحماية صحتها العامة.",
    ],
    "rule": "الشريك الجنسي الحالي (كالزوجة) يجب إبلاغه ب<bdi>case</bdi> HIV لأنه معرض مباشر ل<bdi>risk</bdi> انتقال العدوى.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[59] = {
    "B": "الوالدين ليسوا معرضين ل<bdi>risk</bdi> انتقال مباشر بالحياة اليومية العادية.",
    "C": "الأخ أيضًا ما فيه <bdi>cause</bdi> طبي لإخباره ما لم يكن معرض <bdi>risk</bdi> مباشر.",
    "D": "صاحب العمل ليس له علاقة بالـ<bdi>case</bdi> الصحية الخاصة، وإفصاح له ينتهك الخصوصية بدون مبرر.",
}
HIGHLIGHT_TERMS[59] = ["counselling"]

EXPLANATIONS[60] = {
    "idea": "رجل شخص بـ HIV، والسؤال يبي من يجب <bdi>symptom</bdi> فحص HIV عليه من مخالطيه، والمبدأ هو تحديد من كان بمعرض <bdi>risk</bdi> انتقال حقيقي (شريك جنسي سابق أو حالي).",
    "clues": [
        ("who should be offered HIV testing", "يبي تحديد المخالط المعرض ل<bdi>risk</bdi> انتقال حقيقي"),
    ],
    "why_correct": [
        "الزوجة السابقة كانت شريكة جنسية معرضة ل<bdi>risk</bdi> انتقال العدوى بالماضي، فمن الأنسب <bdi>symptom</bdi> الفحص عليها لأنها بمعرض <bdi>risk</bdi> حقيقي.",
        "الوالدين وزملاء العمل ليسوا بمعرض <bdi>risk</bdi> انتقال HIV بالحياة اليومية العادية، فما يستدعي <bdi>symptom</bdi> الفحص عليهم.",
        "الابن البالغ (28 سنة) ليس بمعرض <bdi>risk</bdi> انتقال إلا لو كان عبر طريق انتقال معروف زي نقل دم أو ولادة من أم مصابة، وهذا غير مذكور هنا.",
    ],
    "when_changes": [
        "لو الابن وُلد من أم مصابة بـ HIV، يصير فحصه ضروريًا ب<bdi>cause</bdi> احتمال انتقال عمودي وقت الولادة.",
    ],
    "rule": "يُعرض فحص HIV على من كان بمعرض <bdi>risk</bdi> انتقال حقيقي فقط، مثل شريك جنسي سابق أو حالي.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[60] = {
    "A": "الوالدين ليسوا معرضين ل<bdi>risk</bdi> انتقال حقيقي بالحياة اليومية العادية.",
    "C": "الابن البالغ ليس بمعرض <bdi>risk</bdi> إلا لو فيه طريق انتقال معروف زي الولادة أو نقل دم، وهذا غير مذكور.",
    "D": "زملاء العمل ليسوا معرضين ل<bdi>risk</bdi> انتقال HIV بالتعامل اليومي العادي.",
}
HIGHLIGHT_TERMS[60] = ["offered HIV testing"]

EXPLANATIONS[61] = {
    "idea": "رجل <bdi>diabetes</bdi> معه <bdi>pneumonia</bdi> (كحة منتجة، تسرع تنفس، تسلل رئوي) بمؤشرات شدة متوسطة (تسرع تنفس 23، يوريا <bdi>normal</bdi>)، والسؤال يبي مستوى الرعاية المناسب.",
    "clues": [
        ("Respiratory rate 23 /min", "تسرع تنفس <bdi>mild</bdi> إلى متوسط، يرفع درجة الشدة قليلًا"),
        ("Urea 5", "يوريا ضمن الـ<bdi>normal</bdi>، <bdi>factor</bdi> مطمئن بمقياس شدة <bdi>pneumonia</bdi>"),
        ("Right lower lobe infiltrate", "تأكيد الـ<bdi>diagnosis</bdi> بالأشعة"),
    ],
    "why_correct": [
        "مؤشرات الشدة هنا (تسرع تنفس بسيط، يوريا <bdi>normal</bdi>، توجه ذهني سليم) تدل على <bdi>pneumonia</bdi> متوسط الشدة يحتاج دخول مستشفى عادي مو عناية مركزة.",
        "الدخول للعناية المركزة يُحجز لحالات الشدة العالية (هبوط ضغط <bdi>severe</bdi>، فشل تنفسي، تسرع تنفس <bdi>severe</bdi> جدًا)، وهذا غير موجود هنا.",
        "الـ<bdi>patient</bdi> <bdi>diabetes</bdi> و<bdi>factors</bdi> الـ<bdi>risk</bdi> المصاحبة تجعل الـ<bdi>treatment</bdi> بالمضادات الوريدية بالمستشفى أضمن من الـ<bdi>treatment</bdi> بالعيادة الخارجية أو الملاحظة القصيرة بالطوارئ.",
    ],
    "when_changes": [
        "لو تدهورت الـ<bdi>signs</bdi> الحيوية (هبوط ضغط <bdi>severe</bdi> أو فشل تنفسي)، يصير النقل للعناية المركزة ضروريًا.",
        "لو كانت مؤشرات الشدة كلها <bdi>mild</bdi> جدًا بدون <bdi>factors</bdi> <bdi>risk</bdi> (<bdi>diabetes</bdi>)، يمكن التفكير ب<bdi>treatment</bdi> خارجي بمضاد فموي.",
    ],
    "rule": "<bdi>pneumonia</bdi> بمؤشرات شدة متوسطة عند <bdi>patient</bdi> <bdi>diabetes</bdi> يستدعي دخول مستشفى عادي مع مضادات وريدية، مو عناية مركزة ولا <bdi>treatment</bdi> خارجي.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[61] = {
    "B": "العناية المركزة تُحجز لحالات الشدة العالية، وهذا غير موجود هنا (تسرع تنفس بسيط ويوريا <bdi>normal</bdi>).",
    "C": "الملاحظة بالطوارئ فقط غير كافية ل<bdi>patient</bdi> <bdi>diabetes</bdi> بحاجة مضادات وريدية و<bdi>follow-up</bdi> أطول.",
    "D": "الـ<bdi>treatment</bdi> الخارجي غير مناسب مع وجود <bdi>diabetes</bdi> وتسرع تنفس وتسلل رئوي مؤكد.",
}
HIGHLIGHT_TERMS[61] = ["Respiratory rate 23 /min", "Urea 5", "Right lower lobe infiltrate"]

EXPLANATIONS[62] = {
    "idea": "امرأة معها كحة منتجة وضيق نفس وتسرع تنفس و<bdi>crepitations</bdi> بالرئة، والسؤال يبي أفضل فحص تشخيصي فوري لتأكيد <bdi>pneumonia</bdi>.",
    "clues": [
        ("productive cough, shortness of breath and tachypnea", "<bdi>symptoms</bdi> تنفسية سفلية توحي ب<bdi>pneumonia</bdi>"),
        ("right lobe zone crepitation", "<bdi>sign</bdi> فحص سريري تدعم <bdi>pneumonia</bdi>"),
    ],
    "why_correct": [
        "أشعة الصدر (<bdi>Chest X-ray</bdi>) هي الفحص التشخيصي الأساسي والفوري لتأكيد وجود تسلل رئوي يدعم <bdi>diagnosis</bdi> <bdi>pneumonia</bdi>.",
        "ارتفاع كريات الدم البيضاء <bdi>sign</bdi> داعمة غير نوعية، وزراعة القشع تأخذ وقت ولا تؤكد الـ<bdi>diagnosis</bdi> فورًا بالطوارئ.",
        "تخطيط صدى القلب يفيد ب<bdi>assessment</bdi> القلب مو تأكيد <bdi>pneumonia</bdi>، فما يناسب هالسياق.",
    ],
    "when_changes": [
        "لو الصورة السريرية توحي أكثر بقصور قلب (تورم أطراف، JVP <bdi>elevated</bdi>)، يصير تخطيط صدى القلب هو الفحص الأنسب بدالها.",
    ],
    "rule": "أشعة الصدر هي الفحص التشخيصي الفوري الأساسي لتأكيد <bdi>pneumonia</bdi> مشتبه به سريريًا.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[62] = {
    "B": "ارتفاع كريات الدم البيضاء <bdi>sign</bdi> داعمة غير نوعية، ما يؤكد الـ<bdi>diagnosis</bdi> بمفرده.",
    "C": "زراعة القشع تأخذ وقت طويل نسبيًا ولا تعطي تأكيد فوري بالطوارئ.",
    "D": "تخطيط صدى القلب يقيّم القلب، ما يؤكد وجود <bdi>pneumonia</bdi>.",
}
HIGHLIGHT_TERMS[62] = ["productive cough, shortness of breath and tachypnea", "right lobe zone crepitation"]

EXPLANATIONS[63] = {
    "idea": "رجل <bdi>diabetes</bdi> وضغط معه كحة و<bdi>wheeze</bdi> وحمى <bdi>mild</bdi> مع تسلل <bdi>bilateral</bdi> بالأشعة وعيار الراصات الباردة <bdi>elevated</bdi> (1:256)، وهذي صورة كلاسيكية ل<bdi>pneumonia</bdi> لانمطي (غالبًا بالمايكوبلازما).",
    "clues": [
        ("wheezing, and<br>right side<br>crepitation", "<bdi>symptoms</bdi> صدرية مختلطة توحي بعدوى لانمطية"),
        ("Cold agglutinin titre: 1:256", "ارتفاع الراصات الباردة، <bdi>sign</bdi> مميزة لعدوى المايكوبلازما"),
        ("Bilateral shadowing both lungs", "تسلل <bdi>bilateral</bdi> منتشر، نموذج شائع بالالتهاب اللانمطي"),
    ],
    "why_correct": [
        "ارتفاع عيار الراصات الباردة (Cold agglutinins) <bdi>sign</bdi> مميزة جدًا لعدوى المايكوبلازما الرئوية، وهذا أحد أشكال <bdi>pneumonia</bdi> اللانمطي (<bdi>Atypical pneumonia</bdi>).",
        "التسلل الـ<bdi>bilateral</bdi> المنتشر مع <bdi>wheeze</bdi> وحمى <bdi>mild</bdi> نسبيًا (38°م) يناسب الالتهاب اللانمطي أكثر من الالتهاب النموذجي الـ<bdi>severe</bdi> المفاجئ.",
        "<bdi>asthma</bdi> و<bdi>heart failure</bdi> ما يفسران الحمى وارتفاع الراصات الباردة، و<bdi>pneumonia</bdi> العقدي (النموذجي) عادة أحادي الجانب مع حمى <bdi>severe</bdi> مفاجئة.",
    ],
    "when_changes": [
        "لو الحمى كانت <bdi>elevated</bdi> جدًا فجأة مع تسلل أحادي الجانب محدد الفص وقشع صدئ، يميل الـ<bdi>diagnosis</bdi> ل<bdi>pneumonia</bdi> عقدي نموذجي بدلًا من اللانمطي.",
    ],
    "rule": "ارتفاع عيار الراصات الباردة مع تسلل <bdi>bilateral</bdi> منتشر يوجّه بقوة ل<bdi>pneumonia</bdi> لانمطي بالمايكوبلازما.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[63] = {
    "A": "تفاقم <bdi>asthma</bdi> ما يفسر الحمى وارتفاع الراصات الباردة والتسلل الرئوي.",
    "B": "<bdi>pneumonia</bdi> العقدي النموذجي عادة أحادي الجانب مع حمى <bdi>elevated</bdi> مفاجئة، بعكس الصورة هنا.",
    "D": "تفاقم <bdi>heart failure</bdi> لا يفسر ارتفاع الراصات الباردة ولا الحمى المصاحبة.",
}
HIGHLIGHT_TERMS[63] = ["Cold agglutinin titre: 1:256", "Bilateral shadowing both lungs"]

EXPLANATIONS[64] = {
    "idea": "امرأة معها تعب وألم مفصلي وظهري وحمى بعد شرب حليب نيء مع تضخم كبد وطحال <bdi>mild</bdi>، والزراعة أظهرت مكورات عصوية سالبة الغرام، وهذي صورة كلاسيكية لل<bdi>Brucella</bdi>، والسؤال يبي <bdi>treatment</bdi> الخط الأول.",
    "clues": [
        ("raw milk ingestion", "مصدر عدوى كلاسيكي لل<bdi>Brucella</bdi>"),
        ("Gram negative cocco-bacilli", "شكل الجرثومة يوحي بالـ<bdi>Brucella</bdi>"),
    ],
    "why_correct": [
        "توليفة <bdi>Doxycycline</bdi> مع <bdi>Streptomycin</bdi> من أنظمة الـ<bdi>treatment</bdi> القياسية الأولى لل<bdi>Brucella</bdi> غير المعقدة الموصى بها بالإرشادات.",
        "توليفة الدوكسيسايكلين مع الكليندامايسين ليست نظام معتمد ل<bdi>treatment</bdi> الـ<bdi>Brucella</bdi>.",
        "السيبروفلوكساسين مع التريميثوبريم سلفاميثوكسازول والريفامبين مع التريميثوبريم سلفاميثوكسازول بدائل أقل فعالية أو أقل استخدامًا كخط أول مقارنة بالدوكسيسايكلين والستربتومايسين.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> حامل أو الستربتومايسين غير متاح، يُستبدل بريفامبين مع الدوكسيسايكلين كبديل معتمد.",
    ],
    "rule": "الخط الأول ل<bdi>treatment</bdi> الـ<bdi>Brucella</bdi> غير المعقدة هو توليفة Doxycycline مع Streptomycin.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[64] = {
    "A": "الدوكسيسايكلين مع الكليندامايسين ليست توليفة معتمدة ل<bdi>treatment</bdi> الـ<bdi>Brucella</bdi>.",
    "C": "السيبروفلوكساسين مع التريميثوبريم سلفاميثوكسازول أقل فعالية من الخط الأول القياسي.",
    "D": "الريفامبين مع التريميثوبريم سلفاميثوكسازول بديل أقل استخدامًا كخط أول مقارنة بالدوكسيسايكلين والستربتومايسين.",
}
HIGHLIGHT_TERMS[64] = ["raw milk ingestion", "Gram negative cocco-bacilli"]

EXPLANATIONS[65] = {
    "idea": "نفس صورة الـ<bdi>Brucella</bdi>، بس هذي المرة مع التهاب مفصل عجزي حرقفي مؤكد بالرنين (شكل معقد من الـ<bdi>Brucella</bdi>)، والسؤال يبي مدة الـ<bdi>treatment</bdi> المناسبة.",
    "clues": [
        ("Sacroiliac joint spondylits", "إصابة عظمية مفصلية مؤكدة، شكل معقد من الـ<bdi>Brucella</bdi> يحتاج مدة <bdi>treatment</bdi> أطول"),
    ],
    "why_correct": [
        "الـ<bdi>Brucella</bdi> المصحوبة بإصابة عظمية مفصلية (سبونديليت أو التهاب مفصل عجزي حرقفي) تعتبر شكل معقد يحتاج مدة <bdi>treatment</bdi> أطول تصل لـ 12 أسبوع.",
        "المدد الأقصر (3 أو 6 أسابيع) تكفي لل<bdi>Brucella</bdi> غير المعقدة بس غير كافية مع إصابة عظمية مفصلية مؤكدة.",
        "24 أسبوع مدة أطول من اللازم لهالشكل من الـ<bdi>Brucella</bdi>، وتزيد <bdi>risk</bdi> الآثار الجانبية بدون فائدة إضافية مثبتة.",
    ],
    "when_changes": [
        "لو ما فيه إصابة عظمية مفصلية والـ<bdi>Brucella</bdi> غير معقدة، تكفي مدة 6 أسابيع فقط.",
    ],
    "rule": "الـ<bdi>Brucella</bdi> المصحوبة بإصابة عظمية مفصلية تحتاج مدة <bdi>treatment</bdi> أطول تصل لـ 12 أسبوعًا.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[65] = {
    "A": "3 أسابيع قصيرة جدًا حتى لل<bdi>Brucella</bdi> غير المعقدة.",
    "B": "6 أسابيع تكفي لل<bdi>Brucella</bdi> غير المعقدة بس غير كافية مع إصابة عظمية مفصلية.",
    "D": "24 أسبوع مدة مبالغ فيها وأطول من الموصى به لهالشكل من الـ<bdi>Brucella</bdi>.",
}
HIGHLIGHT_TERMS[65] = ["Sacroiliac joint spondylits"]

EXPLANATIONS[66] = {
    "idea": "عاملة منزلية من جنوب شرق آسيا معها كحة منتجة ونفث دم وتجويف بالفص العلوي مع ارتفاع سرعة الترسيب، وهذي صورة قوية توحي ب<bdi>tuberculosis</bdi> رئوي نشط، والسؤال يبي الـ<bdi>step</bdi> التشخيصية التالية.",
    "clues": [
        ("Southeast Asia", "منطقة عالية انتشار <bdi>tuberculosis</bdi>"),
        ("hemoptysis", "نفث دم، <bdi>symptom</bdi> شائع ب<bdi>tuberculosis</bdi> الرئوي الكهفي"),
        ("Right upper lobe infiltrate and cavitation", "تجويف بالفص العلوي، صورة كلاسيكية لل<bdi>tuberculosis</bdi> الرئوي النشط"),
    ],
    "why_correct": [
        "قبل أي <bdi>treatment</bdi>، لازم تأكيد <bdi>diagnosis</bdi> <bdi>tuberculosis</bdi> عبر فحص القشع للعصيات الصامدة للحمض (<bdi>AFB</bdi>) ك<bdi>step</bdi> تشخيصية أساسية وسريعة نسبيًا.",
        "بدء الـ<bdi>treatment</bdi> الرباعي مباشرة بدون تأكيد نسيجي أو مخبري غير مناسب ك<bdi>step</bdi> أولى قبل الفحص التشخيصي الأساسي.",
        "منظار القصبات <bdi>procedure</bdi> تدخلي يُحجز لو فشل فحص القشع العادي بالـ<bdi>diagnosis</bdi>، مو ك<bdi>step</bdi> أولى مباشرة.",
    ],
    "when_changes": [
        "لو فحص القشع للعصيات الصامدة تكرر وطلع سلبي مع استمرار الاشتباه القوي، يصير منظار القصبات هو الـ<bdi>step</bdi> التالية.",
    ],
    "rule": "أي اشتباه ب<bdi>tuberculosis</bdi> رئوي نشط يستوجب فحص القشع للعصيات الصامدة للحمض ك<bdi>step</bdi> تشخيصية أولى قبل بدء الـ<bdi>treatment</bdi>.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[66] = {
    "A": "سيفترياكسون وريدي يعالج <bdi>pneumonia</bdi> بكتيري عادي، مو <bdi>step</bdi> مناسبة قبل تأكيد أو نفي <bdi>tuberculosis</bdi>.",
    "B": "منظار القصبات <bdi>procedure</bdi> تدخلي لاحق، يُحجز لو فشل فحص القشع العادي.",
    "D": "بدء الـ<bdi>treatment</bdi> الرباعي مباشرة بدون تأكيد تشخيصي أولي غير مناسب ك<bdi>step</bdi> أولى.",
}
HIGHLIGHT_TERMS[66] = ["Southeast Asia", "hemoptysis", "Right upper lobe infiltrate and cavitation"]

EXPLANATIONS[67] = {
    "idea": "رجل بدأ على 4 أدوية مضادة لل<bdi>tuberculosis</bdi> ولاحظ تغير لون البول لأحمر، والسؤال يبي الـ<bdi>cause</bdi> الأرجح، وهو أثر جانبي معروف وحميد لأحد أدوية <bdi>tuberculosis</bdi>.",
    "clues": [
        ("started on 4 anti- TB drugs", "بداية <bdi>treatment</bdi> رباعي لل<bdi>tuberculosis</bdi> يشمل دواء يغيّر لون سوائل الجسم"),
        ("urine color is red", "تغير لون البول، أثر جانبي معروف لدواء الريفامبين"),
    ],
    "why_correct": [
        "<bdi>Rifampin</bdi> (أحد الأدوية الرباعية لل<bdi>tuberculosis</bdi>) يسبب تلوّن البول والدموع والعرق باللون الأحمر البرتقالي، وهذا أثر جانبي حميد معروف وشائع جدًا وليس <bdi>sign</bdi> <bdi>risk</bdi>.",
        "التاريخ العائلي لحصى المسالك موجود بس لا يفسر ظهور اللون الأحمر بالتوقيت المباشر بعد بدء الـ<bdi>treatment</bdi>.",
        "<bdi>tuberculosis</bdi> الكلوي واضطرابات الدم المرتبطة ب<bdi>tuberculosis</bdi> <bdi>causes</bdi> أندر بكثير من الأثر الجانبي المباشر والشائع للريفامبين.",
    ],
    "when_changes": [
        "لو ظهرت <bdi>symptoms</bdi> ألم كلوي <bdi>severe</bdi> مع دم حقيقي بالبول مؤكد مخبريًا (لا مجرد تلوّن)، يفكر بحصوة كلوية أو <bdi>cause</bdi> آخر فعلي.",
    ],
    "rule": "تلوّن البول الأحمر البرتقالي بعد بدء الريفامبين أثر جانبي حميد ومتوقع، وليس <bdi>sign</bdi> <bdi>risk</bdi>.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[67] = {
    "A": "حصى المسالك تسبب دم حقيقي وألم كلوي، مو مجرد تغير لون فوري بعد بدء الـ<bdi>treatment</bdi>.",
    "B": "<bdi>tuberculosis</bdi> الكلوي <bdi>cause</bdi> نادر ولا يظهر بهالسرعة المباشرة بعد بدء الـ<bdi>treatment</bdi>.",
    "D": "اضطرابات الدم المرتبطة ب<bdi>tuberculosis</bdi> <bdi>cause</bdi> أندر بكثير من الأثر الجانبي المباشر المعروف للريفامبين.",
}
HIGHLIGHT_TERMS[67] = ["started on 4 anti- TB", "urine color is red"]

EXPLANATIONS[68] = {
    "idea": "رجل على <bdi>treatment</bdi> <bdi>tuberculosis</bdi> الرباعي معه تحسن سريري وارتفاع <bdi>mild</bdi> بإنزيمات الكبد (أقل من 3 أضعاف الـ<bdi>normal</bdi>) بعد 3 أسابيع، والسؤال يبي أفضل تصرف مع هالارتفاع البسيط.",
    "clues": [
        ("Cough was better and no other symptoms", "تحسن سريري واضح يدعم الاستمرار بالـ<bdi>treatment</bdi>"),
        ("Sputum AB Negative", "استجابة جيدة لل<bdi>treatment</bdi> المضاد لل<bdi>tuberculosis</bdi>"),
    ],
    "why_correct": [
        "الارتفاع الـ<bdi>mild</bdi> بإنزيمات الكبد (أقل من 3 أضعاف الـ<bdi>normal</bdi>) بدون <bdi>symptoms</bdi> كبدية يُعتبر مقبولًا، فيُستمر بالـ<bdi>treatment</bdi> مع مراقبة وظائف الكبد أسبوعيًا.",
        "إيقاف كل الأدوية فورًا غير ضروري ويعرّض الـ<bdi>patient</bdi> ل<bdi>risk</bdi> فشل الـ<bdi>treatment</bdi> وانتشار العدوى، خصوصًا مع تحسن سريري واضح.",
        "إيقاف دواء واحد بعينه (بيرازيناميد أو إيزونيازيد وريفامبين) غير مبرر مع ارتفاع <bdi>mild</bdi> كهذا، ويُحجز للارتفاع الـ<bdi>severe</bdi> أو الـ<bdi>symptoms</bdi> الكبدية.",
    ],
    "when_changes": [
        "لو ارتفعت الإنزيمات أكثر من 5 أضعاف الـ<bdi>normal</bdi> أو ظهرت <bdi>symptoms</bdi> كبدية (<bdi>jaundice</bdi>، غثيان <bdi>severe</bdi>)، يجب إيقاف الأدوية المسببة للسمية الكبدية فورًا.",
    ],
    "rule": "ارتفاع إنزيمات الكبد أقل من 3 أضعاف الـ<bdi>normal</bdi> بدون <bdi>symptoms</bdi> أثناء <bdi>treatment</bdi> <bdi>tuberculosis</bdi> لا يستدعي إيقاف الـ<bdi>treatment</bdi>، بل استمرار مع مراقبة.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[68] = {
    "B": "إيقاف كل الأدوية غير ضروري مع ارتفاع <bdi>mild</bdi> بدون <bdi>symptoms</bdi> ومع تحسن سريري واضح.",
    "C": "إيقاف البيرازيناميد وحده غير مبرر مع ارتفاع أقل من 3 أضعاف الـ<bdi>normal</bdi>.",
    "D": "إيقاف الإيزونيازيد والريفامبين غير مبرر أيضًا بهالمستوى الـ<bdi>mild</bdi> من الارتفاع.",
}
HIGHLIGHT_TERMS[68] = ["Cough was better and no other symptoms", "Sputum AB Negative"]

EXPLANATIONS[69] = {
    "idea": "رجل على <bdi>warfarin</bdi> بدأ <bdi>treatment</bdi> <bdi>tuberculosis</bdi> الرباعي الذي يشمل الريفامبين، والريفامبين محفّز إنزيمي قوي يسرّع تكسير الـ<bdi>warfarin</bdi>، فيحتاج تعديل الجرعة.",
    "clues": [
        ("warfarin 3 mg once daily", "دواء حساس جدًا للتفاعلات الدوائية مع محفزات الإنزيمات"),
        ("First line four anti-TB drugs were started", "يشمل الريفامبين المعروف بتحفيزه الإنزيمي القوي"),
    ],
    "why_correct": [
        "الريفامبين محفّز قوي لإنزيمات الكبد (<bdi>CYP450</bdi>) اللي تكسّر الـ<bdi>warfarin</bdi>، فيقلل فعاليته ويحتاج زيادة جرعة الـ<bdi>warfarin</bdi> للحفاظ على مستوى تخثر مناسب.",
        "الليزينوبريل والـ<bdi>amlodipine</bdi> ما لهما تفاعل مباشر مهم مع أدوية <bdi>tuberculosis</bdi> الرباعية يستدعي تعديل جرعتهما بهالسياق.",
        "إيقاف الريفامبين غير مناسب لأنه دواء أساسي ب<bdi>treatment</bdi> <bdi>tuberculosis</bdi>، والحل الصحيح تعديل جرعة الـ<bdi>warfarin</bdi> مع <bdi>follow-up</bdi> INR عن كثب.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> على دواء آخر يزيد تأثير الـ<bdi>warfarin</bdi> (زي بعض المضادات الحيوية الأخرى)، يحتاج تقليل الجرعة بدل زيادتها.",
    ],
    "rule": "الريفامبين يقلل فعالية الـ<bdi>warfarin</bdi> ب<bdi>cause</bdi> تحفيزه الإنزيمي، فيحتاج زيادة جرعة الـ<bdi>warfarin</bdi> مع <bdi>follow-up</bdi> دقيقة لـ INR.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[69] = {
    "A": "الليزينوبريل ما له تفاعل مباشر مهم مع أدوية <bdi>tuberculosis</bdi> يستدعي تقليل جرعته.",
    "B": "الـ<bdi>amlodipine</bdi> ما يحتاج إيقاف ب<bdi>cause</bdi> أدوية <bdi>tuberculosis</bdi> الرباعية.",
    "D": "إيقاف الريفامبين غير مناسب لأنه دواء أساسي ب<bdi>treatment</bdi> <bdi>tuberculosis</bdi>، والحل تعديل جرعة الـ<bdi>warfarin</bdi> بدلًا من ذلك.",
}
HIGHLIGHT_TERMS[69] = ["warfarin 3 mg once daily", "First line four anti-TB drugs were started"]

EXPLANATIONS[70] = {
    "idea": "رجل من الهند معه صداع وحمى <bdi>mild</bdi> لأسابيع تفاقمت مع تشنجات، والسائل الشوكي فيه ضغط <bdi>elevated</bdi> وغلبة لمفاويات مع بروتين <bdi>elevated</bdi> وجلوكوز <bdi>low</bdi>، وهذي صورة كلاسيكية لالتهاب سحايا سلي.",
    "clues": [
        ("headache and low-<br>grade fever for 3-weeks", "مسار <bdi>chronic</bdi> يميل لل<bdi>tuberculosis</bdi> مو البكتيري الـ<bdi>acute</bdi>"),
        ("Pressure 280", "ضغط سائل شوكي <bdi>elevated</bdi>، يدعم التهاب سحايا <bdi>chronic</bdi> <bdi>severe</bdi>"),
        ("73% lymphocytes", "غلبة لمفاويات، نموذجية لل<bdi>tuberculosis</bdi>"),
        ("Glucose 1.2", "جلوكوز <bdi>low</bdi> جدًا يدعم عدوى نشطة <bdi>chronic</bdi> ك<bdi>tuberculosis</bdi>"),
    ],
    "why_correct": [
        "مسار <bdi>chronic</bdi> (3 أسابيع) من الهند (منطقة عالية انتشار <bdi>tuberculosis</bdi>) مع غلبة لمفاويات وبروتين <bdi>elevated</bdi> وجلوكوز <bdi>low</bdi> جدًا يطابق التهاب سحايا سلي تمامًا.",
        "الالتهاب البكتيري الـ<bdi>acute</bdi> عادة أسرع بالمسار (أيام) مع غلبة عدلات مو لمفاويات بهالنسبة العالية.",
        "الفيروسي عادة يعطي جلوكوز <bdi>normal</bdi> وبروتين أقل ارتفاعًا من المستوى المذكور هنا، والتكيسات الدماغية الطفيلية (نيوروسيستيسركوسيس) ما تعطي هالصورة الالتهابية الـ<bdi>acute</bdi> بالسائل الشوكي.",
    ],
    "when_changes": [
        "لو المسار كان أيام قليلة بس مع غلبة عدلات، يتجه الـ<bdi>diagnosis</bdi> للبكتيري الـ<bdi>acute</bdi> بدل السلي.",
    ],
    "rule": "صداع وحمى <bdi>chronic</bdi> من منطقة عالية انتشار <bdi>tuberculosis</bdi> مع غلبة لمفاويات وجلوكوز <bdi>low</bdi> جدًا بالسائل الشوكي توجّه لالتهاب سحايا سلي.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[70] = {
    "A": "النيوروسيستيسركوسيس عادة يعطي كيسات محددة بالتصوير مو صورة التهابية <bdi>acute</bdi> بالسائل الشوكي بهالشكل.",
    "C": "البكتيري الـ<bdi>acute</bdi> عادة أسرع بالمسار مع غلبة عدلات، مو لمفاويات بهالنسبة العالية.",
    "D": "الفيروسي عادة جلوكوز <bdi>normal</bdi> وبروتين أقل ارتفاعًا من المستوى المذكور هنا بكثير.",
}
HIGHLIGHT_TERMS[70] = ["headache and low-", "Pressure 280", "73% lymphocytes", "Glucose 1.2"]

EXPLANATIONS[71] = {
    "idea": "امرأة سكرية معها احمرار وألم بالساق مع حد واضح جدًا للاحمرار وبدون قرحة، وهذي صورة كلاسيكية لالتهاب جلدي سطحي محدد الحدود (إريزيبيلاس).",
    "clues": [
        ("sharply demarcated red lesion", "حد واضح و<bdi>acute</bdi> للاحمرار، <bdi>sign</bdi> مميزة للإريزيبيلاس"),
        ("no ulcer", "غياب القرحة يبعد <bdi>causes</bdi> ثانية"),
    ],
    "why_correct": [
        "الحد الواضح والـ<bdi>acute</bdi> جدًا للاحمرار (sharply demarcated) <bdi>sign</bdi> مميزة تفرّق الإريزيبيلاس عن التهاب النسيج الخلوي العادي اللي حدوده غير واضحة.",
        "الإريزيبيلاس التهاب سطحي بالجلد يعطي احمرار مؤلم محدد الحدود بشكل واضح، وهذا يطابق الوصف تمامًا.",
        "الحمامي العقدية عادة تظهر كعقد مؤلمة بالساقين <bdi>bilateral</bdi> الجانب مو احمرار منتشر أحادي الجانب، والنخر الشحمي <bdi>diabetes</bdi> له مظهر مختلف تمامًا (بقع بنية صفراء غير مؤلمة).",
    ],
    "when_changes": [
        "لو الحد كان غير واضح ومنتشر تدريجيًا بدون حد <bdi>acute</bdi>، يميل الـ<bdi>diagnosis</bdi> لالتهاب النسيج الخلوي العادي بدل الإريزيبيلاس.",
    ],
    "rule": "احمرار جلدي بحد واضح و<bdi>acute</bdi> (sharply demarcated) يعني إريزيبيلاس، بعكس التهاب النسيج الخلوي اللي حدوده غير واضحة.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[71] = {
    "B": "الحمامي العقدية تعطي عقد مؤلمة <bdi>bilateral</bdi> الجانب، مو احمرار منتشر أحادي <bdi>acute</bdi> الحدود.",
    "C": "الـ<bdi>amiodarone</bdi> يسبب تغيرات جلدية مختلفة (<bdi>cyanosis</bdi> رمادية) مو احمرار <bdi>acute</bdi> الحدود مؤلم.",
    "D": "النخر الشحمي <bdi>diabetes</bdi> له مظهر بقع بنية صفراء غير مؤلمة، مختلف تمامًا عن الوصف هنا.",
}
HIGHLIGHT_TERMS[71] = ["sharply demarcated red lesion", "no ulcer"]

EXPLANATIONS[72] = {
    "idea": "امرأة سكرية معها احمرار وألم بالفخذ مع خراج عميق مؤكد بالسونار، والسؤال يبي أفضل <bdi>management</bdi> تجمع بين المضادات الوريدية والتصريف الجراحي.",
    "clues": [
        ("15 cm red<br>lesion, which was tender", "التهاب جلدي واسع ومؤلم"),
        ("10 x 8 cm deep abscess collection", "خراج عميق كبير يحتاج تصريف جراحي بجانب المضادات"),
    ],
    "why_correct": [
        "وجود خراج عميق كبير مؤكد بالسونار يستوجب استشارة جراحية للتصريف بجانب المضادات الحيوية الوريدية، لأن المضادات وحدها لا تخترق الخراج بفعالية كافية.",
        "الدخول للمستشفى ضروري نظرًا لحجم الخراج وشدة الالتهاب، والـ<bdi>treatment</bdi> المنزلي بمضاد فموي غير كافٍ لهالحجم من الخراج.",
        "الدخول للعناية المركزة غير مبرر بدون <bdi>signs</bdi> صدمة إنتانية أو فشل أعضاء، فالدخول للقسم العادي مع المضادات والتصريف كافٍ.",
    ],
    "when_changes": [
        "لو ما فيه خراج مؤكد بالتصوير وبس التهاب جلدي سطحي، تكفي المضادات الوريدية بدون تدخل جراحي.",
    ],
    "rule": "أي خراج عميق مؤكد بالتصوير يحتاج تصريف جراحي بجانب المضادات الحيوية، لأن المضادات وحدها غير كافية.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[72] = {
    "A": "المضادات الوريدية وحدها غير كافية بدون تصريف الخراج العميق المؤكد.",
    "B": "الدخول للعناية المركزة غير مبرر بدون <bdi>signs</bdi> صدمة أو فشل أعضاء.",
    "C": "الـ<bdi>treatment</bdi> المنزلي بمضاد فموي غير كافٍ لخراج بهالحجم يحتاج تصريف جراحي ومضادات وريدية.",
}
HIGHLIGHT_TERMS[72] = ["15 cm red", "10 x 8 cm deep abscess collection"]

EXPLANATIONS[73] = {
    "idea": "امرأة سكرية بدأت على مضاد حيوي فموي ل<bdi>treatment</bdi> التهاب جلدي (بديل عن البنسلين ب<bdi>cause</bdi> الحساسية)، وبعد يوم صار عندها ألم بطن وإسهال مائي وحمى، وهذي صورة كلاسيكية لعدوى معوية مرتبطة بالمضادات الحيوية.",
    "clues": [
        ("allergy to penicillin", "استخدام مضاد حيوي بديل عن البنسلين، غالبًا من فئة ترتبط ب<bdi>risk</bdi> C. difficile"),
        ("abdominal pain, watery diarrhoea and<br>fever", "<bdi>symptoms</bdi> إسهال معوي <bdi>acute</bdi> بعد استخدام مضاد حيوي حديث"),
    ],
    "why_correct": [
        "ظهور إسهال مائي وألم بطن وحمى بعد يوم واحد فقط من بدء مضاد حيوي حديث صورة كلاسيكية لعدوى <bdi>Clostridium difficile</bdi> المرتبطة بالمضادات الحيوية.",
        "تفاقم <bdi>gastropathy</bdi> <bdi>diabetes</bdi> لا يفسر ظهور حمى وإسهال <bdi>acute</bdi> مرتبط زمنيًا ببدء مضاد حيوي جديد بهالوضوح.",
        "الحساسية الدوائية عادة تعطي طفح جلدي أو حكة أو تورم مو إسهال معوي <bdi>acute</bdi> وحمى بهالشكل، والسالمونيلا أقل احتمالًا بدون تاريخ أكل مشبوه واضح.",
    ],
    "when_changes": [
        "لو ظهر طفح جلدي أو حكة بدل الـ<bdi>symptoms</bdi> الهضمية بعد المضاد الحيوي، يصير الـ<bdi>diagnosis</bdi> حساسية دوائية بدل C. difficile.",
    ],
    "rule": "إسهال مائي وحمى بعد بدء مضاد حيوي حديث يعني عدوى C. difficile حتى يثبت العكس.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[73] = {
    "A": "تفاقم <bdi>gastropathy</bdi> <bdi>diabetes</bdi> لا يفسر الحمى وظهور الإسهال المرتبط زمنيًا بالمضاد الحيوي.",
    "B": "الحساسية الدوائية عادة تعطي طفح أو حكة، مو إسهال معوي <bdi>acute</bdi> وحمى بهالشكل.",
    "D": "السالمونيلا أقل احتمالًا بدون تاريخ أكل مشبوه واضح، والتوقيت المباشر بعد المضاد الحيوي يوجه أكثر لـ C. difficile.",
}
HIGHLIGHT_TERMS[73] = ["allergy to penicillin", "abdominal pain, watery diarrhoea and"]

EXPLANATIONS[74] = {
    "idea": "امرأة سكرية معها ألم وتورم <bdi>acute</bdi> بالركبة مع عدد خلايا بيضاء عالٍ جدًا بالسائل الزلالي (55000)، وهذي صورة قوية جدًا توحي بالتهاب مفصل إنتاني رغم الزراعة السلبية.",
    "clues": [
        ("red, swollen and tender with severely limited range of movement", "التهاب مفصلي <bdi>acute</bdi> <bdi>severe</bdi> بمفصل واحد"),
        ("Synovial fluid: WBC: 55.000", "عدد خلايا بيضاء <bdi>elevated</bdi> جدًا بالسائل الزلالي، يوحي بقوة بعدوى مفصلية"),
        ("Culture: Negative", "زراعة سلبية لا تنفي العدوى المفصلية"),
    ],
    "why_correct": [
        "عدد خلايا بيضاء بالسائل الزلالي فوق 50 ألف يوحي بقوة جدًا بالتهاب مفصل إنتاني حتى لو كانت الزراعة سلبية (يحصل بنسبة معينة من الحالات خصوصًا بعد أخذ مضاد حيوي سابق أو جراثيم صعبة النمو).",
        "<bdi>gout</bdi> و<bdi>gout</bdi> الكاذب يحتاجون رؤية بلورات مميزة بالسائل الزلالي لتأكيدهم، وهذا لم يُذكر (الـ<bdi>result</bdi> معلقة/pending).",
        "مفصل شاركو مرتبط باعتلال عصبي محيطي <bdi>chronic</bdi> مع تشوه تدريجي غير مؤلم عادة، مو التهاب <bdi>acute</bdi> <bdi>severe</bdi> الألم بهالشكل.",
    ],
    "when_changes": [
        "لو ظهرت بلورات نموذجية بالفحص المجهري (إبرية سالبة الانكسار المزدوج لل<bdi>gout</bdi>)، يتأكد <bdi>diagnosis</bdi> <bdi>gout</bdi> بدل الإنتاني.",
    ],
    "rule": "عدد خلايا بيضاء فوق 50 ألف بالسائل الزلالي يعني التهاب مفصل إنتاني حتى لو الزراعة سلبية.",
    "comparison": {
        "headers": ["الـ<bdi>diagnosis</bdi>", "عدد خلايا بيضاء بالسائل الزلالي", "البلورات"],
        "rows": [
            ["<bdi>Septic arthritis</bdi>", "أكثر من 50,000 غالبًا", "لا يوجد"],
            ["<bdi>Gout</bdi>", "متفاوت", "إبرية سالبة الانكسار"],
            ["<bdi>Pseudogout</bdi>", "متفاوت", "معينية موجبة الانكسار"],
        ],
    },
    "guideline_note": None,
}
WHY_WRONG[74] = {
    "A": "مفصل شاركو اعتلال <bdi>chronic</bdi> غير مؤلم غالبًا، مو التهاب <bdi>acute</bdi> <bdi>severe</bdi> الألم مع خلايا بيضاء <bdi>elevated</bdi> جدًا.",
    "C": "<bdi>gout</bdi> يحتاج تأكيد ببلورات إبرية مميزة، وهذا غير مؤكد بعد (الـ<bdi>result</bdi> معلقة).",
    "D": "<bdi>gout</bdi> الكاذب أيضًا يحتاج بلورات مميزة للتأكيد، والصورة هنا أقوى توحي بالإنتاني.",
}
HIGHLIGHT_TERMS[74] = ["red, swollen and tender with severely limited range of movement", "Synovial fluid: WBC: 55.000"]

EXPLANATIONS[75] = {
    "idea": "رجل معه <bdi>symptoms</bdi> إنفلونزا مؤكدة بمسحة الحلق وبدأ على <bdi>treatment</bdi> مضاد للإنفلونزا، والسؤال يبي نوع احتياطات العزل المناسب لهالفيروس.",
    "clues": [
        ("started on oseltamivir", "<bdi>treatment</bdi> مضاد فيروسي يؤكد الـ<bdi>diagnosis</bdi> بالإنفلونزا"),
    ],
    "why_correct": [
        "الإنفلونزا تنتقل عبر الرذاذ التنفسي (<bdi>droplet</bdi>) بشكل أساسي، فتحتاج احتياطات قطروية مو هوائية أو تماسية.",
        "الاحتياطات الهوائية تُحجز ل<bdi>diseases</bdi> تنتقل بجزيئات دقيقة معلقة بالهواء زي <bdi>tuberculosis</bdi>، وهذا يختلف عن آلية انتقال الإنفلونزا.",
        "الاحتياطات القياسية وحدها غير كافية مع <bdi>disease</bdi> تنفسي معدٍ ينتقل بالرذاذ زي الإنفلونزا.",
    ],
    "when_changes": [
        "لو تم <bdi>procedure</bdi> <bdi>procedures</bdi> مولّدة للرذاذ (زي التنبيب)، تُضاف احتياطات هوائية مؤقتة إضافية لزيادة الحماية.",
    ],
    "rule": "الإنفلونزا تنتقل بالرذاذ التنفسي وتحتاج احتياطات قطروية (droplet)، مو هوائية.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[75] = {
    "A": "الاحتياطات التماسية تناسب عدوى تنتقل باللمس المباشر، مو الإنفلونزا اللي تنتقل بالرذاذ.",
    "B": "الاحتياطات القياسية وحدها غير كافية مع <bdi>disease</bdi> تنفسي معدٍ ينتقل بالرذاذ.",
    "C": "الاحتياطات الهوائية تُحجز ل<bdi>diseases</bdi> تنتقل بجزيئات دقيقة معلقة بالهواء زي <bdi>tuberculosis</bdi>، مو الإنفلونزا.",
}
HIGHLIGHT_TERMS[75] = ["on oseltamivir"]

EXPLANATIONS[76] = {
    "idea": "امرأة معها صداع وألم عضلي وحمى وطفح على الوجه بعد سفر لجدة قبل 10 أيام، ومعها <bdi>anemia</bdi> ونقص صفيحات، وهذي صورة توحي ب<bdi>disease</bdi> فيروسي حموي، والمبدأ الأهم هنا إن أغلب هالأمراض الفيروسية علاجها داعم فقط.",
    "clues": [
        ("headache and myalgia for 5 days", "<bdi>symptoms</bdi> فيروسية جهازية"),
        ("returned from Jeddah 10-days ago", "توقيت يتوافق مع فترة حضانة <bdi>disease</bdi> معدٍ مكتسب بالسفر"),
        ("Platelets count 80", "نقص صفيحات يدعم <bdi>cause</bdi> فيروسي حموي"),
    ],
    "why_correct": [
        "أغلب الـ<bdi>diseases</bdi> الفيروسية الحموية المصحوبة بطفح ونقص صفيحات و<bdi>anemia</bdi> <bdi>mild</bdi> تكون محدودة لنفسها وتُعالج بالـ<bdi>treatment</bdi> الداعم (سوائل، خافض حرارة، مراقبة).",
        "الستيرويد قد يزيد سوء بعض العدوى الفيروسية ولا يوجد دليل يدعم استخدامه هنا ك<bdi>step</bdi> أولى.",
        "المضادات الفيروسية والمضادات الحيوية الوريدية تحتاج <bdi>diagnosis</bdi> نوعي مؤكد قبل استخدامها، وهذا غير متوفر بعد بالمعطيات الحالية.",
    ],
    "when_changes": [
        "لو تأكد الـ<bdi>diagnosis</bdi> ب<bdi>disease</bdi> فيروسي محدد له <bdi>treatment</bdi> نوعي معتمد (كالهربس مثلًا)، يضاف الـ<bdi>treatment</bdi> النوعي المناسب لذاك الـ<bdi>disease</bdi>.",
        "لو ظهرت <bdi>signs</bdi> نزيف <bdi>severe</bdi> أو صدمة، يحتاج الـ<bdi>patient</bdi> رعاية داعمة أكثر تدخلية بالمستشفى.",
    ],
    "rule": "أغلب الحميات الفيروسية المصحوبة بطفح ونقص صفيحات <bdi>mild</bdi> تُدار بالـ<bdi>treatment</bdi> الداعم ما لم يثبت <bdi>cause</bdi> نوعي يحتاج <bdi>treatment</bdi> خاصًا.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[76] = {
    "A": "الستيرويد قد يزيد سوء بعض العدوى الفيروسية وما يوجد دليل يدعم استخدامه هنا.",
    "B": "المضاد الفيروسي الوريدي يحتاج <bdi>diagnosis</bdi> نوعي مؤكد يستهدفه، وهذا غير متوفر حاليًا.",
    "C": "المضادات الحيوية الوريدية تستهدف عدوى بكتيرية، والصورة هنا أقرب لعدوى فيروسية.",
}
HIGHLIGHT_TERMS[76] = ["headache and myalgia for 5 days", "Platelets count 80"]

EXPLANATIONS[77] = {
    "idea": "جندي مسافر لمنطقة موبوءة بالملاريا وعنده تاريخ <bdi>depression</bdi> مسيطر عليه بالدواء، والسؤال يبي أفضل وقاية دوائية تتجنب تفاقم حالته النفسية.",
    "clues": [
        ("positive history of depression, which is controlled by medication", "تاريخ نفسي يحدد الدواء الوقائي المناسب ويستبعد أدوية معينة"),
    ],
    "why_correct": [
        "<bdi>Atovaquone-proguanil</bdi> خيار وقائي آمن نفسيًا وما يتعارض مع تاريخ <bdi>depression</bdi>، بعكس بعض الأدوية الثانية المرتبطة ب<bdi>complications</bdi> نفسية.",
        "<bdi>Mefloquine</bdi> معروف بارتباطه ب<bdi>complications</bdi> نفسية عصبية (كوابيس، <bdi>anxiety</bdi>، <bdi>depression</bdi>) فيُتجنب عند مرضى <bdi>depression</bdi>.",
        "<bdi>Chloroquine</bdi> غير فعال أصلًا بمناطق كثيرة ب<bdi>cause</bdi> المقاومة الواسعة، والدوكسيسايكلين خيار مقبول بس أقل تفضيلًا من أتوفاكون-بروغوانيل بوجود <bdi>factor</bdi> نفسي.",
    ],
    "when_changes": [
        "لو ما فيه تاريخ نفسي عند المسافر، يصير الدوكسيسايكلين أو الميفلوكين خيارات مقبولة حسب المنطقة الموبوءة.",
    ],
    "rule": "عند وجود تاريخ اضطراب نفسي، يُتجنب الميفلوكين ويُفضّل أتوفاكون-بروغوانيل كوقاية من الملاريا.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[77] = {
    "B": "الدوكسيسايكلين خيار مقبول بس أقل تفضيلًا هنا مقارنة بأتوفاكون-بروغوانيل.",
    "C": "الميفلوكين معروف بمضاعفاته النفسية العصبية ويُتجنب عند مرضى <bdi>depression</bdi>.",
    "D": "الكلوروكين غير فعال أصلًا بمعظم المناطق الموبوءة ب<bdi>cause</bdi> المقاومة الواسعة.",
}
HIGHLIGHT_TERMS[77] = ["positive history of depression, which is controlled by medication"]

EXPLANATIONS[78] = {
    "idea": "رجل معه حمى <bdi>severe</bdi> وصداع بعد سفر للسودان مع نقص صفيحات وارتفاع إنزيمات الكبد وتضخم طحال، وهذي صورة ملاريا <bdi>severe</bdi> معقدة تحتاج <bdi>treatment</bdi> قوي فوري.",
    "clues": [
        ("palpable spleen 3 cm below costal margin", "تضخم طحال، شائع بالملاريا"),
        ("Platelets count 90", "نقص صفيحات، متوافق مع الملاريا الـ<bdi>severe</bdi>"),
        ("Aspartate aminotransferase 88", "ارتفاع إنزيمات الكبد يدعم ملاريا <bdi>severe</bdi> معقدة"),
    ],
    "why_correct": [
        "الصورة هنا (حمى <bdi>severe</bdi> 40°م، نقص صفيحات، ارتفاع إنزيمات الكبد، تضخم طحال) توحي بملاريا <bdi>severe</bdi>/معقدة تحتاج الـ<bdi>treatment</bdi> الأقوى المتاح.",
        "<bdi>Artemisinin-based combination therapy (ACT)</bdi> هو الخط الأول الموصى به عالميًا حاليًا ل<bdi>treatment</bdi> الملاريا بالمناطق ذات مقاومة الكلوروكين مثل السودان.",
        "الكينين والميفلوكين والكلوروكين بدائل أقل تفضيلًا حاليًا أو محدودة الفعالية ب<bdi>cause</bdi> المقاومة أو الآثار الجانبية مقارنة بالـACT.",
    ],
    "when_changes": [
        "لو المنطقة معروفة بحساسية الطفيلي للكلوروكين، يصير الكلوروكين خيار مقبول هناك تحديدًا.",
    ],
    "rule": "الـ<bdi>treatment</bdi> المركب المعتمد على الأرتيميسينين (ACT) هو الخط الأول الحالي ل<bdi>treatment</bdi> الملاريا بمناطق مقاومة الكلوروكين.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[78] = {
    "A": "الكينين خيار قديم أقل تفضيلًا حاليًا مقارنة بالـACT ب<bdi>cause</bdi> الآثار الجانبية والحاجة لمدة <bdi>treatment</bdi> أطول.",
    "B": "الميفلوكين أضعف فعالية من الـACT بالحالات الـ<bdi>severe</bdi>.",
    "C": "الكلوروكين غير فعال أصلًا بمناطق كالسودان ب<bdi>cause</bdi> انتشار المقاومة.",
}
HIGHLIGHT_TERMS[78] = ["palpable spleen 3 cm below costal margin", "Platelets count 90", "Aspartate aminotransferase 88"]

EXPLANATIONS[79] = {
    "idea": "رجل مدخن معه حمى وطفح جلدي حويصلي متقشر مع ضيق نفس ونقص أكسجين <bdi>severe</bdi> وتسلل رئوي <bdi>bilateral</bdi>، وهذي صورة كلاسيكية ل<bdi>pneumonia</bdi> بفيروس الحماق (جدري الماء) عند بالغ.",
    "clues": [
        ("vesicular lesions<br>over the truck and extremities, some of the lesions were crusted", "طفح حويصلي متقشر، صورة كلاسيكية لجدري الماء"),
        ("Oxygen saturation 82 %", "نقص أكسجين <bdi>severe</bdi> يدل على <bdi>pneumonia</bdi> فيروسي خطير"),
        ("Diffuse bilateral infiltrate", "تسلل رئوي <bdi>bilateral</bdi>، متوافق مع <bdi>pneumonia</bdi> بالحماق"),
    ],
    "why_correct": [
        "الطفح الحويصلي المتقشر مع <bdi>pneumonia</bdi> <bdi>bilateral</bdi> الجانب ونقص أكسجين <bdi>severe</bdi> عند بالغ مدخن صورة كلاسيكية ل<bdi>pneumonia</bdi> بفيروس الحماق النطاقي، وهذا <bdi>complication</bdi> خطيرة أشيع بالبالغين المدخنين.",
        "<bdi>Acyclovir</bdi> الوريدي هو الـ<bdi>treatment</bdi> النوعي المعتمد ل<bdi>pneumonia</bdi> الحماق عند البالغين، ولازم يبدأ مبكرًا لتقليل خطورة الـ<bdi>disease</bdi>.",
        "المضادات الحيوية تستهدف عدوى بكتيرية، والستيرويد وحده بدون مضاد فيروسي قد يزيد انتشار الفيروس، والـ<bdi>furosemide</bdi> يخص <bdi>congestion</bdi> قلبي مو عدوى فيروسية.",
    ],
    "when_changes": [
        "لو الطفح كان موزعًا بتوزيع عصبي محدد (جلدة واحدة) بدون إصابة رئوية، يصير الـ<bdi>diagnosis</bdi> هربس نطاقي عادي بدل <bdi>pneumonia</bdi> بالحماق.",
    ],
    "rule": "<bdi>pneumonia</bdi> مصحوب بطفح حويصلي منتشر عند بالغ يعني <bdi>pneumonia</bdi> بفيروس الحماق ويحتاج أسيكلوفير وريدي فوري.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[79] = {
    "A": "المضادات الحيوية تستهدف عدوى بكتيرية، والصورة هنا فيروسية بوضوح ب<bdi>cause</bdi> الطفح الحويصلي.",
    "C": "الستيرويد وحده بدون مضاد فيروسي قد يزيد انتشار الفيروس ويسوء الـ<bdi>case</bdi>.",
    "D": "الـ<bdi>furosemide</bdi> يعالج <bdi>congestion</bdi> سوائل قلبي، وهذا غير مذكور، والمشكلة هنا عدوى فيروسية رئوية.",
}
HIGHLIGHT_TERMS[79] = ["Oxygen saturation 82 %", "Diffuse bilateral infiltrate"]

EXPLANATIONS[80] = {
    "idea": "رجل عائد من العمرة معه حمى وصداع وتشنجات و<bdi>sign</bdi> كيرنيغ إيجابية مع سائل شوكي فيه غلبة عدلات <bdi>severe</bdi> وبروتين <bdi>elevated</bdi> جدًا، وهذي صورة التهاب سحايا بكتيري <bdi>acute</bdi> و<bdi>severe</bdi> يحتاج <bdi>treatment</bdi> تجريبي عاجل وقوي.",
    "clues": [
        ("positive Kering sign", "<bdi>sign</bdi> تهيج سحائي إيجابية"),
        ("87% neutrophils and 5% lymphocytes", "غلبة عدلات <bdi>severe</bdi>، نموذجية للبكتيري الـ<bdi>acute</bdi>"),
        ("Total protein (Men) 1.2", "بروتين <bdi>elevated</bdi> جدًا يدعم التهاب بكتيري <bdi>severe</bdi>"),
    ],
    "why_correct": [
        "غلبة العدلات الـ<bdi>severe</bdi> مع بروتين <bdi>elevated</bdi> جدًا وتشنجات توحي بالتهاب سحايا بكتيري <bdi>acute</bdi> <bdi>severe</bdi>، يحتاج تغطية تجريبية عاجلة وواسعة.",
        "توليفة <bdi>Ceftriaxone</bdi> مع <bdi>Vancomycin</bdi> تغطي المكورات الرئوية المقاومة والمستدمية والمكورات السحائية، والستيرويد يُضاف لتقليل <bdi>risk</bdi> الـ<bdi>complications</bdi> العصبية خصوصًا بحال المكورات الرئوية.",
        "الـ<bdi>treatment</bdi> المضاد للفيروسات (<bdi>acyclovir</bdi>) وحده غير كافٍ هنا لأن الصورة بكتيرية بوضوح (غلبة عدلات <bdi>severe</bdi>)، مو فيروسية.",
    ],
    "when_changes": [
        "لو كانت الغلبة لمفاوية مع جلوكوز <bdi>normal</bdi> وبروتين أقل ارتفاعًا، يميل الـ<bdi>treatment</bdi> للفيروسي بالأسيكلوفير وحده بدل التغطية البكتيرية الثلاثية.",
    ],
    "rule": "التهاب سحايا بكتيري <bdi>acute</bdi> <bdi>severe</bdi> مع تشنجات يُعالج تجريبيًا بـ Ceftriaxone وVancomycin مع Steroid لتغطية أوسع وتقليل الـ<bdi>complications</bdi>.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[80] = {
    "B": "بدون الستيرويد، تزيد فرصة الـ<bdi>complications</bdi> العصبية طويلة المدى خصوصًا لو كان الـ<bdi>cause</bdi> مكورات رئوية.",
    "C": "الأسيكلوفير غير مناسب هنا لأن الصورة بكتيرية بوضوح (غلبة عدلات <bdi>severe</bdi>)، مو فيروسية.",
    "D": "الـ<bdi>treatment</bdi> الفيروسي وحده بدون تغطية بكتيرية غير كافٍ مع هالصورة الواضحة لالتهاب سحايا بكتيري.",
}
HIGHLIGHT_TERMS[80] = ["positive Kering sign", "87% neutrophils and 5% lymphocytes", "Total protein (Men) 1.2"]

EXPLANATIONS[81] = {
    "idea": "رجل معه حمى وصداع ولخبطة و<bdi>sign</bdi> كيرنيغ إيجابية، بس هذي المرة السائل الشوكي فيه غلبة لمفاويات <bdi>severe</bdi> (90%) وجلوكوز <bdi>normal</bdi>، وهذي صورة توحي بالتهاب سحايا/دماغ فيروسي (يُرجّح الهربس ب<bdi>cause</bdi> اللخبطة).",
    "clues": [
        ("Kemig's sign is present", "<bdi>sign</bdi> تهيج سحائي إيجابية"),
        ("5% neutrophil and 90% lymphocytes", "غلبة لمفاويات <bdi>severe</bdi>، نموذجية للفيروسي"),
        ("Glucose 3.7", "جلوكوز <bdi>normal</bdi>، يبعد البكتيري الـ<bdi>acute</bdi>"),
    ],
    "why_correct": [
        "غلبة اللمفاويات الـ<bdi>severe</bdi> مع جلوكوز <bdi>normal</bdi> تبعد الالتهاب البكتيري الـ<bdi>acute</bdi> وتوجه للفيروسي، واللخبطة الذهنية المصاحبة ترفع احتمال التهاب دماغ الهربس البسيط تحديدًا.",
        "<bdi>Acyclovir</bdi> يبدأ تجريبيًا فورًا عند أي اشتباه بالتهاب دماغ الهربس لأن التأخير يزيد <bdi>risk</bdi> تلف دماغي دائم، ولا يُنتظر تأكيد PCR قبل البدء.",
        "التغطية البكتيرية (سيفترياكسون وفانكومايسين) تُحجز للصورة العدلاتية الـ<bdi>severe</bdi>، وهذا غير موجود هنا بوضوح (غلبة لمفاويات 90%).",
    ],
    "when_changes": [
        "لو كانت الغلبة عدلاتية <bdi>severe</bdi> مع جلوكوز <bdi>low</bdi> جدًا، يتغيّر الـ<bdi>treatment</bdi> للتغطية البكتيرية الثلاثية بدل الأسيكلوفير وحده.",
    ],
    "rule": "غلبة لمفاويات <bdi>severe</bdi> مع لخبطة ذهنية وجلوكوز <bdi>normal</bdi> بالسائل الشوكي توجّه لبدء الأسيكلوفير فورًا تغطية لالتهاب دماغ الهربس.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[81] = {
    "A": "التغطية الثلاثية مع الستيرويد تناسب الصورة البكتيرية الـ<bdi>severe</bdi>، وهذا غير موجود هنا بغلبة اللمفاويات.",
    "B": "سيفترياكسون وفانكومايسين يغطون بكتيريا، والصورة هنا فيروسية بوضوح بغلبة اللمفاويات والجلوكوز الـ<bdi>normal</bdi>.",
    "C": "سيفترياكسون وحده لا يغطي الهربس المشتبه به ب<bdi>cause</bdi> اللخبطة الذهنية المصاحبة.",
}
HIGHLIGHT_TERMS[81] = ["Kemig's sign is present", "5% neutrophil and 90% lymphocytes", "Glucose 3.7"]

EXPLANATIONS[82] = {
    "idea": "رجل عائد من الحج معه حمى وصداع وطفح نمشي (بيتيكيال) مع سائل شوكي غلبة عدلات <bdi>severe</bdi>، وهذي صورة كلاسيكية لالتهاب سحايا بالمكورات السحائية (Meningococcemia)، والسؤال يبي نوع احتياطات العزل المناسب.",
    "clues": [
        ("recently returned from Hajj", "ازدحام الحج يزيد <bdi>risk</bdi> انتقال المكورات السحائية"),
        ("petechial rash on extremities and trunk", "طفح نمشي مميز جدًا للمكورات السحائية"),
        ("87% neutrophils and 5% lymphocytes", "غلبة عدلات <bdi>severe</bdi>، بكتيري <bdi>acute</bdi>"),
    ],
    "why_correct": [
        "الطفح النمشي مع التهاب سحايا بكتيري <bdi>acute</bdi> بعد ازدحام الحج يوجّه بقوة للمكورات السحائية (<bdi>Neisseria meningitidis</bdi>) اللي تنتقل عبر الرذاذ التنفسي.",
        "المكورات السحائية تحتاج احتياطات قطروية (<bdi>droplet</bdi>) لمنع انتقالها للعاملين الصحيين والمخالطين.",
        "الاحتياطات الهوائية أو التماسية أو القياسية وحدها غير مناسبة أو غير كافية لهالجرثومة اللي تنتقل بالرذاذ القريب المدى تحديدًا.",
    ],
    "when_changes": [
        "بعد مرور 24 ساعة من الـ<bdi>treatment</bdi> الفعال بالمضاد الحيوي المناسب، يمكن إيقاف احتياطات العزل القطروية.",
    ],
    "rule": "التهاب سحايا مع طفح نمشي بعد ازدحام (كالحج) يوحي بالمكورات السحائية ويحتاج احتياطات قطروية (droplet).",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[82] = {
    "A": "الاحتياطات التماسية لا تكفي لمنع انتقال المكورات السحائية عبر الرذاذ التنفسي.",
    "C": "الاحتياطات القياسية وحدها غير كافية مع <bdi>disease</bdi> ينتقل بالرذاذ القريب زي المكورات السحائية.",
    "D": "الاحتياطات الهوائية تُحجز ل<bdi>diseases</bdi> تنتقل بجزيئات دقيقة معلقة بالهواء زي <bdi>tuberculosis</bdi>، مختلفة عن آلية انتقال المكورات السحائية.",
}
HIGHLIGHT_TERMS[82] = ["recently returned from Hajj", "petechial rash on extremities and trunk", "87% neutrophils and 5% lymphocytes"]

EXPLANATIONS[83] = {
    "idea": "نفس صورة التهاب سحايا المكورات السحائية بعد العمرة مع طفح نمشي، والسؤال هذي المرة عن كم ساعة بعد بدء المضاد الحيوي الفعال يمكن إيقاف العزل.",
    "clues": [
        ("started on antibiotics", "بدء <bdi>treatment</bdi> فعال يقلل قدرة الجرثومة على الانتقال"),
    ],
    "why_correct": [
        "احتياطات العزل القطروية تُوقف بعد 24 ساعة من بدء مضاد حيوي فعال ضد المكورات السحائية، لأن الجرثومة تصير غير قادرة على الانتقال بعد هالمدة تقريبًا.",
        "إيقاف العزل بعد 12 ساعة فقط مبكر جدًا ولا يضمن زوال قدرة الجرثومة على الانتقال بشكل كافٍ.",
        "الانتظار لـ 48 أو 72 ساعة أطول من اللازم ويطيل مدة العزل غير الضرورية بعد زوال <bdi>risk</bdi> الانتقال الفعلي.",
    ],
    "when_changes": [
        "لو المضاد الحيوي المستخدم غير فعال ضد المكورات السحائية أو تأخر بدؤه، يمتد وقت العزل المطلوب.",
    ],
    "rule": "يُوقف عزل التهاب سحايا المكورات السحائية بعد 24 ساعة من بدء مضاد حيوي فعال.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[83] = {
    "A": "12 ساعة مبكر جدًا ولا يضمن زوال قدرة الجرثومة على الانتقال.",
    "C": "48 ساعة أطول من اللازم ويطيل مدة العزل غير الضرورية.",
    "D": "72 ساعة أطول بكثير من المدة المعتمدة فعليًا لإيقاف العزل.",
}
HIGHLIGHT_TERMS[83] = ["started on antibiotics"]

EXPLANATIONS[84] = {
    "idea": "<bdi>patient</bdi> غسيل كلوي عبر قسطرة فخذية معها قشعريرة وحمى واحمرار وصديد بموقع القسطرة، وهذي صورة عدوى موقع القسطرة المركزية تحتاج إزالتها فورًا مع الـ<bdi>treatment</bdi>.",
    "clues": [
        ("shivering", "قشعريرة، <bdi>sign</bdi> إنتان دم محتمل"),
        ("central line site was red with pus discharge", "احمرار وصديد بموقع القسطرة، دليل واضح على عدوى موضعية بالقسطرة"),
    ],
    "why_correct": [
        "وجود صديد واحمرار واضح بموقع القسطرة مع قشعريرة وحمى يعني عدوى قسطرة مؤكدة تستوجب سحب زراعة دم وبدء مضادات وريدية وإزالة القسطرة المصابة فورًا.",
        "ترك القسطرة أو مجرد تبديلها بدون إزالة كاملة أولًا يعرّض الـ<bdi>patient</bdi> لاستمرار مصدر العدوى و<bdi>risk</bdi> إنتان دم مستمر.",
        "إيقاف الغسيل لمدة 3 أيام بدون إزالة مصدر العدوى الفعلي (القسطرة) لا يعالج المشكلة الأساسية.",
    ],
    "when_changes": [
        "لو كان الاحمرار <bdi>mild</bdi> جدًا بدون صديد أو حمى، يمكن محاولة <bdi>treatment</bdi> الـ<bdi>patient</bdi> بمضادات مع مراقبة عن قرب قبل اتخاذ قرار إزالة القسطرة.",
    ],
    "rule": "عدوى قسطرة مركزية مؤكدة (صديد واحمرار وحمى) تستوجب سحب زراعة دم وبدء مضادات وإزالة القسطرة فورًا.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[84] = {
    "A": "ترك القسطرة بمكانها رغم وجود صديد واضح يُبقي مصدر العدوى مستمرًا.",
    "B": "إيقاف الغسيل فقط بدون إزالة القسطرة المصابة لا يعالج مصدر العدوى الفعلي.",
    "C": "تبديل القسطرة والاستمرار بالغسيل فورًا <bdi>risk</bdi> لأن مصدر العدوى الفعلي (القسطرة القديمة المصابة) لازم يُزال مع بدء الـ<bdi>treatment</bdi> أول.",
}
HIGHLIGHT_TERMS[84] = ["shivering", "central line site was red with pus discharge"]

EXPLANATIONS[85] = {
    "idea": "<bdi>patient</bdi> على فانكومايسين ل<bdi>treatment</bdi> إنتان دم بـ MRSA، وبعد بدء التسريب مباشرة صار عندها احمرار وحكة بالوجه والرقبة، وهذي صورة كلاسيكية لمتلازمة الرجل الأحمر الناتجة عن سرعة التسريب مو حساسية حقيقية.",
    "clues": [
        ("to be infused over 20 min", "سرعة تسريب سريعة جدًا لجرعة كبيرة من الفانكومايسين"),
        ("flushing, redness and itching over the face, neck and trunk", "صورة كلاسيكية لمتلازمة الرجل الأحمر"),
    ],
    "why_correct": [
        "متلازمة الرجل الأحمر (<bdi>Red man syndrome</bdi>) رد فعل غير تحسسي ناتج عن سرعة تسريب الفانكومايسين، وتُدار بإبطاء سرعة التسريب مع الاستمرار بنفس الدواء.",
        "التسريب خلال 20 دقيقة فقط لجرعة 1000 مجم سريع جدًا (الموصى به عادة تسريب أبطأ لمدة ساعة أو أكثر)، وهذا <bdi>cause</bdi> مباشر للتفاعل.",
        "تصنيف الـ<bdi>patient</bdi> كمتحسسة للفانكومايسين وإيقافه نهائيًا غير صحيح، لأن هذا التفاعل ليس حساسية حقيقية (IgE-mediated) بل ناتج عن سرعة التسريب فقط.",
    ],
    "when_changes": [
        "لو ظهرت <bdi>symptoms</bdi> حساسية حقيقية زي صعوبة تنفس أو هبوط ضغط <bdi>severe</bdi> أو شرى منتشر مع تورم حنجري، يُعتبر ذلك تحسسًا حقيقيًا يستوجب إيقاف الدواء فورًا.",
    ],
    "rule": "متلازمة الرجل الأحمر ناتجة عن سرعة تسريب الفانكومايسين، وتُدار بإبطاء التسريب مع الاستمرار بالدواء نفسه.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[85] = {
    "A": "تصنيفها كمتحسسة وإيقاف الدواء نهائيًا خطأ لأن هذا رد فعل غير تحسسي مرتبط بسرعة التسريب.",
    "B": "تقليل الجرعة لا يعالج <bdi>cause</bdi> المشكلة الحقيقي وهو سرعة التسريب، وقد يقلل فعالية الـ<bdi>treatment</bdi> ضد MRSA.",
    "D": "السيفازولين ما يغطي MRSA أصلًا، فتبديله يفشل ب<bdi>treatment</bdi> العدوى الأساسية.",
}
HIGHLIGHT_TERMS[85] = ["to be infused over 20 min", "flushing, redness and itching over the face, neck and trunk"]

EXPLANATIONS[86] = {
    "idea": "امرأة بعد الولادة بشهرين بدون <bdi>symptoms</bdi> بولية طلعت عندها زراعة بول إيجابية، وهذي بكتيريا بولية لا عرضية (asymptomatic bacteriuria)، والقاعدة إنها ما تُعالج خارج الحمل.",
    "clues": [
        ("She has no symptoms", "غياب أي <bdi>symptoms</bdi> بولية يعني بكتيريا لا عرضية"),
        ("2-months after delivery", "خارج فترة الحمل، تنطبق قاعدة عدم الـ<bdi>treatment</bdi>"),
    ],
    "why_correct": [
        "البكتيريا البولية اللا عرضية (<bdi>asymptomatic bacteriuria</bdi>) لا تُعالج خارج الحمل أو قبل <bdi>procedure</bdi> بولي تدخلي، لأن الـ<bdi>treatment</bdi> غير المبرر يزيد <bdi>risk</bdi> المقاومة الدوائية بدون فائدة سريرية حقيقية.",
        "الـ<bdi>patient</bdi> ليست حاملًا الآن (بعد الولادة بشهرين) وما فيها أي <bdi>symptoms</bdi> بولية، فلا يوجد استطباب لل<bdi>treatment</bdi> بأي مضاد حيوي.",
        "إعطاء مضاد حيوي (سيبروفلوكساسين أو نيتروفيورانتوين أو تريميثوبريم سلفاميثوكسازول) بدون استطباب يعرّضها لآثار جانبية غير ضرورية.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>patient</bdi> حاملًا حاليًا، يجب <bdi>treatment</bdi> البكتيريا البولية اللا عرضية لتجنب <bdi>complications</bdi> الحمل مثل الولادة المبكرة.",
        "لو كانت الـ<bdi>symptoms</bdi> البولية موجودة (حرقان، تكرار)، يصير الـ<bdi>treatment</bdi> مبررًا بغض النظر عن الحمل.",
    ],
    "rule": "البكتيريا البولية اللا عرضية لا تُعالج خارج الحمل أو قبل <bdi>procedure</bdi> بولي تدخلي.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[86] = {
    "A": "السيبروفلوكساسين غير مبرر بدون <bdi>symptoms</bdi> بولية وخارج الحمل.",
    "B": "النيتروفيورانتوين أيضًا غير ضروري بدون استطباب علاجي واضح.",
    "C": "تريميثوبريم سلفاميثوكسازول نفس الفكرة، ما فيه داعي لل<bdi>treatment</bdi> بدون <bdi>symptoms</bdi> أو حمل.",
}
HIGHLIGHT_TERMS[86] = ["She has no symptoms", "2-months after delivery"]

EXPLANATIONS[87] = {
    "idea": "امرأة حامل بالأسبوع 28 بدون <bdi>symptoms</bdi> بولية طلعت زراعة بولها إيجابية، وبعكس الـ<bdi>patient</bdi> السابقة، الحمل يغيّر القاعدة فتستوجب <bdi>treatment</bdi> البكتيريا اللا عرضية.",
    "clues": [
        ("28-weeks pregnant", "الحمل يغيّر قاعدة <bdi>treatment</bdi> البكتيريا البولية اللا عرضية"),
        ("She has no symptoms", "بكتيريا بولية لا عرضية، بس بالحمل تحتاج <bdi>treatment</bdi>"),
    ],
    "why_correct": [
        "بعكس المرأة غير الحامل، البكتيريا البولية اللا عرضية بالحمل تُعالج دايمًا لأنها ترفع <bdi>risk</bdi> <bdi>pyelonephritis</bdi> والولادة المبكرة لو تُركت بدون <bdi>treatment</bdi>.",
        "<bdi>Nitrofurantoin</bdi> الفموي خيار آمن ومناسب بالحمل (بعيدًا عن قرب الولادة) وحساس للجرثومة حسب <bdi>result</bdi> الزراعة.",
        "السيبروفلوكساسين يُتجنب بالحمل لتأثيره المحتمل على الغضاريف الجنينية، وعدم الـ<bdi>treatment</bdi> خطأ هنا لأن الحمل يستوجب الـ<bdi>treatment</bdi> دايمًا.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>patient</bdi> قريبة جدًا من الولادة (الأسابيع الأخيرة)، يُراعى اختيار مضاد حيوي آمن بهالمرحلة تحديدًا بعيدًا عن النيتروفيورانتوين قرب الولادة.",
    ],
    "rule": "البكتيريا البولية اللا عرضية بالحمل تُعالج دايمًا لمنع <bdi>complications</bdi> الحمل، بعكس المرأة غير الحامل.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[87] = {
    "A": "السيبروفلوكساسين يُتجنب بالحمل لتأثيره المحتمل على الغضاريف الجنينية.",
    "C": "تريميثوبريم سلفاميثوكسازول يُتجنب خصوصًا بالثلث الأول والأخير من الحمل، والنيتروفيورانتوين أنسب هنا.",
    "D": "عدم الـ<bdi>treatment</bdi> خطأ لأن البكتيريا البولية اللا عرضية بالحمل تحتاج <bdi>treatment</bdi> دايمًا لمنع الـ<bdi>complications</bdi>.",
}
HIGHLIGHT_TERMS[87] = ["28-weeks pregnant", "She has no symptoms"]

EXPLANATIONS[88] = {
    "idea": "امرأة سكرية معها حمى وألم خاصرة وحرقان بول (صورة التهاب حويضة وكلية) وعندها حساسية من البنسلين، والسؤال يبي أي مضاد حيوي ممنوع منعًا مطلقًا ب<bdi>cause</bdi> الحساسية.",
    "clues": [
        ("allergic to penicillin", "حساسية تمنع استخدام أي دواء من مجموعة البنسلين أو مشتقاته"),
        ("flank tenderness", "ألم خاصرة يدعم <bdi>diagnosis</bdi> التهاب حويضة وكلية"),
    ],
    "why_correct": [
        "<bdi>Piperacillin/tazobactam</bdi> يحتوي بيتالاكتام من مجموعة البنسلين، فهو ممنوع منعًا مطلقًا عند <bdi>patient</bdi> تعاني حساسية حقيقية من البنسلين.",
        "السيبروفلوكساسين من الكينولونات، والميروبينيم كاربابينيم، والسيفترياكسون سيفالوسبورين، وهذي فئات مختلفة عن البنسلين ويمكن استخدامها بحذر (مع مراقبة تحسس متصالب طفيف محتمل مع السيفالوسبورينات لو الحساسية <bdi>severe</bdi>).",
        "استخدام بيبيراسيلين تازوباكتام يعرّض الـ<bdi>patient</bdi> ل<bdi>risk</bdi> تفاعل تحسسي <bdi>severe</bdi> قد يهدد الحياة (صدمة تأقية).",
    ],
    "when_changes": [
        "لو كانت الحساسية <bdi>mild</bdi> (طفح بسيط قديم) وليست تأقية <bdi>severe</bdi>، يمكن أحيانًا التفكير بمراقبة دقيقة عند استخدام سيفالوسبورين، بس البنسلين يبقى ممنوعًا.",
    ],
    "rule": "أي دواء من مجموعة البنسلين (بما فيها بيبيراسيلين تازوباكتام) ممنوع منعًا مطلقًا عند حساسية بنسلين حقيقية.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[88] = {
    "B": "السيبروفلوكساسين من الكينولونات، فئة مختلفة تمامًا عن البنسلين، آمن هنا.",
    "C": "الميروبينيم كاربابينيم، ورغم وجود تحسس متصالب نادر، إلا أنه ليس ممنوعًا منعًا مطلقًا كالبنسلين نفسه.",
    "D": "السيفترياكسون سيفالوسبورين، فئة مختلفة عن البنسلين ويمكن استخدامه غالبًا بأمان.",
}
HIGHLIGHT_TERMS[88] = ["allergic to penicillin", "flank tenderness"]

EXPLANATIONS[89] = {
    "idea": "امرأة معها حمى وألم خاصرة وحرقان بول مع زراعة بول إيجابية، وهذي صورة التهاب حويضة وكلية، والسؤال يبي أفضل <bdi>treatment</bdi> تجريبي أولي.",
    "clues": [
        ("flank pain and dysuria", "صورة كلاسيكية لالتهاب حويضة وكلية"),
        ("WBC 14", "ارتفاع كريات الدم البيضاء يدعم عدوى بكتيرية نشطة"),
    ],
    "why_correct": [
        "<bdi>Ceftriaxone</bdi> الوريدي خيار تجريبي ممتاز وواسع الاستخدام ل<bdi>pyelonephritis</bdi> لأنه يغطي أغلب الجراثيم المعوية سالبة الغرام المسببة زي الإي كولاي.",
        "<bdi>Nitrofurantoin</bdi> لا يصل لتركيز كافٍ بأنسجة الكلية، فما يناسب <bdi>treatment</bdi> <bdi>pyelonephritis</bdi> رغم فعاليته بالتهاب المثانة السفلي.",
        "بيبيراسيلين تازوباكتام والميروبينيم تغطية أوسع من اللازم لالتهاب حويضة وكلية غير معقد بدون <bdi>factors</bdi> <bdi>risk</bdi> لجراثيم مقاومة.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عندها حساسية <bdi>severe</bdi> للسيفالوسبورينات أو <bdi>factors</bdi> <bdi>risk</bdi> لمقاومة، يُفكر ببديل زي أمينوغليكوزيد أو كاربابينيم حسب الـ<bdi>case</bdi>.",
    ],
    "rule": "السيفترياكسون خيار تجريبي أول ممتاز ل<bdi>treatment</bdi> <bdi>pyelonephritis</bdi> ب<bdi>cause</bdi> تغطيته الجيدة وتركيزه الكافي بأنسجة الكلية.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[89] = {
    "A": "بيبيراسيلين تازوباكتام تغطية أوسع من اللازم لالتهاب حويضة وكلية غير معقد.",
    "B": "النيتروفيورانتوين لا يصل لتركيز كافٍ بأنسجة الكلية، فما يناسب هالتشخيص.",
    "C": "الميروبينيم مضاد واسع الطيف جدًا محجوز لعدوى <bdi>severe</bdi> مقاومة، مبالغ فيه هنا.",
}
HIGHLIGHT_TERMS[89] = ["flank pain and dysuria", "WBC 14"]

EXPLANATIONS[90] = {
    "idea": "امرأة سكرية معها حرقان بول وضعف واضح بوظائف الكلى (كرياتينين 230)، والسؤال يبي أي مضاد حيوي ممنوع ب<bdi>cause</bdi> <bdi>renal failure</bdi>، وليس ب<bdi>cause</bdi> حساسية.",
    "clues": [
        ("Creatinine 230", "ارتفاع واضح بالكرياتينين يدل على قصور كلوي يمنع بعض الأدوية"),
    ],
    "why_correct": [
        "<bdi>Nitrofurantoin</bdi> يحتاج ترشيح كلوي كافٍ ليصل لتركيز علاجي فعال بالبول، ومع <bdi>renal failure</bdi> يتراكم بالجسم ويفقد فعاليته ويزيد <bdi>risk</bdi> السمية دون <bdi>treatment</bdi> كافٍ.",
        "الميروبينيم والسيبروفلوكساسين والتريميثوبريم سلفاميثوكسازول ممكن استخدامهم مع تعديل الجرعة حسب درجة <bdi>renal failure</bdi>، مو ممنوعين منعًا مطلقًا.",
        "استخدام النيتروفيورانتوين مع كرياتينين <bdi>elevated</bdi> كهذا (يدل على تصفية كلوية ضعيفة جدًا) يعتبر مضاد استطباب واضح.",
    ],
    "when_changes": [
        "لو كانت وظائف الكلى <bdi>normal</bdi>، يصير النيتروفيورانتوين خيار ممتاز وآمن لالتهاب المثانة السفلي.",
    ],
    "rule": "النيتروفيورانتوين ممنوع مع <bdi>renal failure</bdi> الـ<bdi>severe</bdi> لأنه يفقد فعاليته وتتراكم مستقلباته السامة.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[90] = {
    "B": "السيبروفلوكساسين يحتاج تعديل جرعة مع <bdi>renal failure</bdi>، مو ممنوعًا منعًا مطلقًا.",
    "C": "بيبيراسيلين تازوباكتام أيضًا يحتاج تعديل جرعة حسب درجة <bdi>renal failure</bdi>، مو ممنوعًا بالكامل.",
    "D": "تريميثوبريم سلفاميثوكسازول يحتاج تعديل جرعة ب<bdi>renal failure</bdi>، مو منع كامل مثل النيتروفيورانتوين هنا.",
}
HIGHLIGHT_TERMS[90] = ["Creatinine 230"]

EXPLANATIONS[91] = {
    "idea": "رجل معه تعب وضيق نفس وحمى مع <bdi>murmur</bdi> قلبية انقباضية شاملة (Pan-systolic) عند القمة ونزيف شظوي بالأظافر، وهذي صورة كلاسيكية لالتهاب شغاف تحت <bdi>acute</bdi> على صمام <bdi>normal</bdi>، وأشيع <bdi>cause</bdi> له هو العقديات.",
    "clues": [
        ("pan-systolic murmur at the apex", "<bdi>murmur</bdi> قلبية توحي بقصور صمام تاجي مرتبط ب<bdi>endocarditis</bdi>"),
        ("splinter hemorrhage on nails", "<bdi>sign</bdi> كلاسيكية ل<bdi>infective endocarditis</bdi>"),
        ("No previous surgical history", "صمام <bdi>normal</bdi>، يحدد أشيع الجراثيم المسببة"),
    ],
    "why_correct": [
        "<bdi>endocarditis</bdi> تحت الـ<bdi>acute</bdi> (مسار أسابيع مع <bdi>symptoms</bdi> تدريجية) على صمام <bdi>normal</bdi> بدون تاريخ جراحي أشيع <bdi>cause</bdi> له هو <bdi>Streptococcus species</bdi> (خصوصًا العقديات الفموية viridans).",
        "الستافيلوكوكس إبيديرميديس أشيع ب<bdi>endocarditis</bdi> على صمام صناعي، والإنتيروكوكس أكثر ارتباطًا ب<bdi>procedures</bdi> بولية أو معوية سابقة، وهذا غير مذكور.",
        "الكليبسيلا <bdi>cause</bdi> نادر ل<bdi>endocarditis</bdi> مقارنة بالعقديات بهالسياق تحت الـ<bdi>acute</bdi>.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> مستخدم مخدرات وريدية، تصير الستافيلوكوكس أوريوس هي الـ<bdi>cause</bdi> الأشيع بدل العقديات.",
        "لو كان عنده صمام صناعي حديث، يصير الستافيلوكوكس إبيديرميديس هو الـ<bdi>cause</bdi> الأشيع.",
    ],
    "rule": "<bdi>endocarditis</bdi> تحت الـ<bdi>acute</bdi> على صمام <bdi>normal</bdi> بدون تاريخ جراحي أشيع سببه العقديات الفموية (Streptococcus viridans).",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[91] = {
    "A": "الستافيلوكوكس إبيديرميديس أشيع ب<bdi>endocarditis</bdi> على صمام صناعي، وهذا <bdi>patient</bdi> بلا تاريخ جراحي.",
    "B": "الإنتيروكوكس أكثر ارتباطًا ب<bdi>procedures</bdi> بولية أو معوية سابقة، وهذا غير مذكور بالسؤال.",
    "C": "الكليبسيلا <bdi>cause</bdi> نادر ل<bdi>endocarditis</bdi> مقارنة بالعقديات بهالسياق تحت الـ<bdi>acute</bdi>.",
}
HIGHLIGHT_TERMS[91] = ["pan-systolic murmur at the apex", "splinter hemorrhage on nails", "No previous surgical history"]

EXPLANATIONS[92] = {
    "idea": "نفس صورة <bdi>endocarditis</bdi> تحت الـ<bdi>acute</bdi>، والسؤال هذي المرة عن الـ<bdi>treatment</bdi> التجريبي المناسب قبل معرفة <bdi>result</bdi> الزراعة.",
    "clues": [
        ("pan systolic murmur at the apex", "<bdi>murmur</bdi> قلبية توحي بالتهاب شغاف محتمل"),
        ("splinter hemorrhage on nails", "<bdi>sign</bdi> كلاسيكية ل<bdi>infective endocarditis</bdi>"),
    ],
    "why_correct": [
        "الـ<bdi>treatment</bdi> التجريبي ل<bdi>endocarditis</bdi> المشتبه به يجب أن يغطي أشيع الـ<bdi>causes</bdi> المحتملة (عقديات وستافيلوكوكس) قبل ظهور <bdi>result</bdi> الزراعة، وتوليفة <bdi>Ceftriaxone</bdi> و<bdi>Vancomycin</bdi> تحقق هالتغطية الواسعة.",
        "أي دواء منفرد وحده (سيفترياكسون أو جنتامايسين أو بيبيراسيلين تازوباكتام) لا يغطي كل الاحتمالات المهمة بما فيها المقاومة المحتملة للستافيلوكوكس.",
        "التغطية المزدوجة تقلل <bdi>risk</bdi> فشل الـ<bdi>treatment</bdi> التجريبي ريثما تظهر <bdi>result</bdi> الزراعة وحساسية الجرثومة.",
    ],
    "when_changes": [
        "بعد ظهور <bdi>result</bdi> الزراعة والحساسية، يُعدّل الـ<bdi>treatment</bdi> ليصير موجّهًا نوعيًا حسب الجرثومة المؤكدة.",
    ],
    "rule": "الـ<bdi>treatment</bdi> التجريبي ل<bdi>endocarditis</bdi> المشتبه به يجمع بين سيفترياكسون وفانكومايسين لتغطية واسعة قبل <bdi>result</bdi> الزراعة.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[92] = {
    "A": "سيفترياكسون وحده لا يغطي احتمال ستافيلوكوكس مقاوم للميثيسيلين.",
    "B": "الجنتامايسين وحده تغطية ضيقة وغير كافية ك<bdi>treatment</bdi> تجريبي وحيد ل<bdi>endocarditis</bdi>.",
    "C": "بيبيراسيلين تازوباكتام لا يغطي بفعالية كافية احتمال الستافيلوكوكس المقاوم.",
}
HIGHLIGHT_TERMS[92] = ["pan systolic murmur at the apex", "splinter hemorrhage on nails"]

EXPLANATIONS[93] = {
    "idea": "امرأة حامل بالأسبوع العاشر تقريبًا معها التهاب مسالك بولية، والسؤال يبي المضاد الحيوي الممنوع ب<bdi>cause</bdi> الحمل تحديدًا.",
    "clues": [
        ("10-weeks pregnant", "الحمل يحدد أي مضادات حيوية ممنوعة ب<bdi>cause</bdi> تأثيرها على الجنين"),
    ],
    "why_correct": [
        "<bdi>Ciprofloxacin</bdi> (كينولون) ممنوع بالحمل لتأثيره المحتمل على الغضاريف النامية عند الجنين، مبني على دراسات حيوانية وقلة بيانات أمان بالبشر.",
        "النيتروفيورانتوين والأموكسيسيلين والسيفترياكسون خيارات آمنة نسبيًا وتُستخدم بشكل شائع ل<bdi>treatment</bdi> <bdi>UTI</bdi> أثناء الحمل.",
        "تجنب الكينولونات بالحمل مبدأ عام مهم يجب تذكره بكل أسئلة اختيار المضاد الحيوي للمرأة الحامل.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> قريبة جدًا من الولادة (الأسابيع الأخيرة)، يُتجنب النيتروفيورانتوين أيضًا ب<bdi>cause</bdi> <bdi>risk</bdi> <bdi>anemia</bdi> انحلالي عند المولود G6PD.",
    ],
    "rule": "السيبروفلوكساسين وكل الكينولونات ممنوعة بالحمل ب<bdi>cause</bdi> تأثيرها المحتمل على غضاريف الجنين.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[93] = {
    "A": "النيتروفيورانتوين خيار آمن عمومًا أثناء الحمل بعيدًا عن الأسابيع الأخيرة جدًا.",
    "C": "الأموكسيسيلين من المضادات الآمنة المستخدمة بشكل شائع أثناء الحمل.",
    "D": "السيفترياكسون أيضًا خيار آمن نسبيًا ويُستخدم أثناء الحمل عند الحاجة.",
}
HIGHLIGHT_TERMS[93] = ["10-weeks pregnant"]

EXPLANATIONS[94] = {
    "idea": "شاب معه نفث دم متقطع ودم بالبول وزيادة وزن مفاجئة مع انتفاخ حول العينين وارتفاع كرياتينين، وخزعة الرئة أظهرت ترسب أجسام مضادة على الغشاء القاعدي، وهذي صورة كلاسيكية لمتلازمة غودباستشر.",
    "clues": [
        ("intermittent hemoptysis", "نفث دم متكرر، يوحي بإصابة سنخية رئوية"),
        ("blood in his urine", "دم بالبول يدل على إصابة كلوية مصاحبة"),
        ("elevated serum creatinine", "قصور كلوي <bdi>acute</bdi> مصاحب"),
        ("Serum immunoglobulin on basement membranes", "ترسب أجسام مضادة على الغشاء القاعدي، <bdi>diagnosis</bdi> مؤكد لغودباستشر"),
    ],
    "why_correct": [
        "توليفة نفث الدم (نزيف سنخي رئوي) مع دم بالبول وقصور كلوي وترسب أجسام مضادة على الغشاء القاعدي صورة تشخيصية مؤكدة لمتلازمة غودباستشر (<bdi>Anti-GBM disease</bdi>).",
        "متلازمة غودباستشر تصيب الغشاء القاعدي بالرئة والكلية معًا بأجسام مضادة نوعية، وهذا يفسر الإصابة المزدوجة (رئوية وكلوية) بنفس الوقت.",
        "الاحتشاء القلبي ومتلازمة دي جورج و<bdi>disease</bdi> غريفز ما لها علاقة بترسب أجسام مضادة على الغشاء القاعدي بالرئة والكلية.",
    ],
    "when_changes": [
        "لو ما فيه إصابة كلوية مصاحبة وبس نزيف رئوي، يفكر ب<bdi>causes</bdi> نزيف سنخي ثانية زي الورم الحبيبي الوعائي (Granulomatosis with polyangiitis).",
    ],
    "rule": "نفث دم مع دم بالبول وقصور كلوي وترسب أجسام مضادة على الغشاء القاعدي يعني متلازمة غودباستشر.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[94] = {
    "A": "الاحتشاء القلبي لا يفسر إصابة الرئة والكلية معًا ولا ترسب الأجسام المضادة على الغشاء القاعدي.",
    "C": "متلازمة دي جورج <bdi>disease</bdi> خلقي بنقص مناعي وقلبي عند الأطفال، لا علاقة لها بهالصورة.",
    "D": "<bdi>disease</bdi> غريفز يخص الغدة الدرقية، ولا يفسر نفث الدم والإصابة الكلوية المصاحبة.",
}
HIGHLIGHT_TERMS[94] = ["intermittent hemoptysis", "blood in his urine", "elevated serum creatinine"]

EXPLANATIONS[95] = {
    "idea": "السؤال يبي أفضل موقع لسحب عينة من <bdi>pleural effusion</bdi> الأيمن بإبرة وسرنجة، ولازم يكون تحت مستوى السائل وفوق الحجاب الحاجز وبعيد عن الحزمة العصبية الوعائية.",
    "clues": [
        ("right pleural effusion", "تجمع سائل بالجنب يحتاج تحديد موقع آمن للسحب"),
    ],
    "why_correct": [
        "الخط الإبطي الأوسط عند المسافة الوربية التاسعة موقع آمن ومناسب لسحب <bdi>pleural effusion</bdi>، لأنه تحت مستوى تجمع السائل عادة وفوق مستوى الحجاب الحاجز بما يكفي لتجنب إصابة أعضاء البطن.",
        "المسافة الوربية السادسة أعلى من اللازم وقد تكون فوق مستوى السائل المتجمع، خصوصًا لو كان الـ<bdi>effusion</bdi> كبيرًا يمتد لأسفل.",
        "الخط الجانب القصي (Parasternal) <bdi>risk</bdi> لقربه من القلب والأوعية الكبيرة، وغير مناسب أبدًا لسحب <bdi>pleural effusion</bdi>.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>effusion</bdi> صغيرًا ومحدودًا لقاعدة الرئة فقط، يُحدد الموقع بالفحص السريري أو بالسونار مباشرة قبل السحب بدل الاعتماد على قاعدة ثابتة.",
    ],
    "rule": "أفضل موقع آمن لسحب <bdi>pleural effusion</bdi> هو الخط الإبطي الأوسط عند مسافة وربية <bdi>low</bdi> نسبيًا (حوالي التاسعة)، بعيدًا عن القلب والحجاب الحاجز.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[95] = {
    "A": "الخط الترقوي المنتصف عند المسافة السادسة قريب جدًا من القلب وغير مناسب لسحب <bdi>pleural effusion</bdi>.",
    "B": "الخط الإبطي الأوسط عند المسافة السادسة أعلى من اللازم وقد يكون فوق مستوى السائل المتجمع.",
    "D": "الخط الجانب القصي <bdi>risk</bdi> جدًا لقربه من القلب والأوعية الكبيرة.",
}
HIGHLIGHT_TERMS[95] = ["right pleural effusion"]

EXPLANATIONS[96] = {
    "idea": "رجل معه ضيق نفس وكحة ليلية مع سعة حيوية قسرية ونسبة FEV1/FVC أقل من الـ<bdi>normal</bdi>، وهذي صورة نمط انسدادي بوظائف الرئة، والسؤال يبي الـ<bdi>cause</bdi> الفسيولوجي المطابق.",
    "clues": [
        ("difficulty in breathing and a nocturnal cough", "<bdi>symptoms</bdi> تنفسية توحي ب<bdi>disease</bdi> مجرى هوائي انسدادي"),
        ("FEV/FVC ratio lower than<br>normal", "نمط انسدادي واضح بوظائف الرئة"),
    ],
    "why_correct": [
        "انخفاض نسبة <bdi>FEV1/FVC</bdi> <bdi>sign</bdi> النمط الانسدادي، وسببه الفسيولوجي الأساسي هو زيادة مقاومة مجرى الهواء (<bdi>increased airway resistance</bdi>) اللي تبطئ إخراج الهواء بالثانية الأولى.",
        "ضعف عضلات الشهيق يعطي نمط تقييدي (restrictive) بانخفاض السعات كلها مع نسبة FEV1/FVC <bdi>normal</bdi> أو <bdi>elevated</bdi>، مو انخفاضها.",
        "نقص أو زيادة مطاوعة الرئة (compliance) مفاهيم تخص المرونة الرئوية وترتبط أكثر بالـ<bdi>diseases</bdi> التقييدية أو النفاخ الرئوي بطريقة مختلفة عن مجرد انخفاض النسبة الانسدادي المباشر هنا.",
    ],
    "when_changes": [
        "لو كانت النسبة <bdi>normal</bdi> أو <bdi>elevated</bdi> مع انخفاض كل السعات الرئوية، يتجه الـ<bdi>diagnosis</bdi> لنمط تقييدي بدل انسدادي.",
    ],
    "rule": "انخفاض نسبة FEV1/FVC يعني نمط انسدادي سببه زيادة مقاومة مجرى الهواء.",
    "comparison": {
        "headers": ["النمط", "FEV1/FVC", "مثال"],
        "rows": [
            ["انسدادي (Obstructive)", "<bdi>low</bdi>", "<bdi>asthma</bdi>، COPD"],
            ["تقييدي (Restrictive)", "<bdi>normal</bdi> أو <bdi>elevated</bdi>", "<bdi>pulmonary fibrosis</bdi>"],
        ],
    },
    "guideline_note": None,
}
WHY_WRONG[96] = {
    "A": "ضعف عضلات الشهيق يعطي نمط تقييدي بنسبة FEV1/FVC <bdi>normal</bdi> أو <bdi>elevated</bdi>، مو <bdi>low</bdi>.",
    "B": "نقص المطاوعة الرئوية يرتبط أكثر بالـ<bdi>diseases</bdi> التقييدية، مو بانخفاض نسبة FEV1/FVC الانسدادي هنا.",
    "C": "زيادة المطاوعة الرئوية ترتبط بالنفاخ الرئوي المتقدم بشكل مختلف عن مجرد تفسير انخفاض النسبة المباشر.",
}
HIGHLIGHT_TERMS[96] = ["difficulty in breathing and a nocturnal cough", "FEV/FVC ratio lower than"]

EXPLANATIONS[97] = {
    "idea": "السؤال يبي أفضل <bdi>treatment</bdi> ل<bdi>pneumonia</bdi> مكتسب من المجتمع عند <bdi>patient</bdi> سليم بدون <bdi>diseases</bdi> مصاحبة، والماكروليد خيار قياسي بسيط وفعال بهالفئة.",
    "clues": [
        ("optimal treatment for community-acquired pneumonia", "يبي تحديد خط الـ<bdi>treatment</bdi> الأمثل ل<bdi>pneumonia</bdi> مجتمعي بدون <bdi>factors</bdi> <bdi>risk</bdi> إضافية"),
    ],
    "why_correct": [
        "<bdi>Azithromycin</bdi> (ماكروليد) هو الـ<bdi>treatment</bdi> التجريبي الأمثل الموصى به ل<bdi>pneumonia</bdi> مكتسب من المجتمع عند <bdi>patient</bdi> سليم بدون <bdi>diseases</bdi> مصاحبة، لأنه يغطي الجراثيم النموذجية وغير النموذجية بفعالية جيدة.",
        "الكينولون التنفسي يُحجز عادة لمرضى عندهم <bdi>diseases</bdi> مصاحبة أو فشل بالـ<bdi>treatment</bdi> الأولي، مو كخط أول ل<bdi>patient</bdi> سليم تمامًا.",
        "الفانكومايسين والديكلوكساسيللين يغطون ستافيلوكوكس بشكل أساسي، وهذا ليس الـ<bdi>cause</bdi> الأشيع ل<bdi>pneumonia</bdi> مجتمعي بسيط عند <bdi>patient</bdi> سليم.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عنده <bdi>diseases</bdi> مصاحبة (<bdi>diabetes</bdi>، قصور كلوي أو قلب <bdi>chronic</bdi>)، يصير الكينولون التنفسي أو توليفة بيتالاكتام مع ماكروليد هو الأنسب.",
    ],
    "rule": "الماكروليد (Azithromycin) هو خط الـ<bdi>treatment</bdi> الأول ل<bdi>pneumonia</bdi> مكتسب من المجتمع عند الـ<bdi>patient</bdi> السليم بدون <bdi>diseases</bdi> مصاحبة.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[97] = {
    "A": "الكينولون التنفسي يُحجز غالبًا لمرضى عندهم <bdi>diseases</bdi> مصاحبة، مو خط أول ل<bdi>patient</bdi> سليم.",
    "C": "الفانكومايسين يغطي ستافيلوكوكس مقاوم، وهذا ليس الـ<bdi>cause</bdi> الأشيع ب<bdi>patient</bdi> سليم مجتمعي.",
    "D": "الديكلوكساسيللين يغطي ستافيلوكوكس حساس، وليس خط أول ل<bdi>pneumonia</bdi> مجتمعي نموذجي.",
}
HIGHLIGHT_TERMS[97] = ["community-acquired pneumonia in an otherwise", "healthy patient"]

EXPLANATIONS[98] = {
    "idea": "السؤال يبي المدة المثلى لمضادات التخثر بعد أول نوبة <bdi>embolism</bdi> رئوي، والملف يعتمد مدة 6 أشهر كخط عام.",
    "clues": [
        ("optimal duration of anticoagulation following an initial episode of pulmonary", "يبي تحديد مدة الـ<bdi>treatment</bdi> المضاد للتخثر بعد أول نوبة <bdi>embolism</bdi>"),
    ],
    "why_correct": [
        "مدة 6 أشهر من مضادات التخثر تعتبر مدة معتمدة ومتوازنة بعد أول نوبة <bdi>embolism</bdi> رئوي بحسب هالملف، توازن بين منع تكرار الـ<bdi>thrombus</bdi> و<bdi>risk</bdi> النزيف من الـ<bdi>treatment</bdi> المطول.",
        "6 أسابيع مدة قصيرة جدًا ولا تكفي لتقليل <bdi>risk</bdi> تكرار <bdi>pulmonary embolism</bdi> بشكل كافٍ.",
        "3 أشهر مدة مقبولة أحيانًا بحالات معينة (<bdi>cause</bdi> مؤقت واضح) بس الملف هنا يعتمد 6 أشهر، و12 شهر أطول من اللازم لأول نوبة غير مبررة ب<bdi>factors</bdi> <bdi>risk</bdi> دائمة.",
    ],
    "when_changes": [
        "لو كانت النوبة ب<bdi>cause</bdi> مؤقت واضح وزال (كجراحة حديثة)، ممكن تُقصّر المدة لـ 3 أشهر بحسب <bdi>assessment</bdi> الطبيب.",
        "لو تكررت نوبات <bdi>pulmonary embolism</bdi> أو فيه <bdi>factor</bdi> <bdi>risk</bdi> دائم (كنقص <bdi>factor</bdi> تخثر وراثي)، يصير الـ<bdi>treatment</bdi> مطولًا أو مدى الحياة.",
    ],
    "rule": "المدة المعتمدة لمضادات التخثر بعد أول نوبة <bdi>embolism</bdi> رئوي هي 6 أشهر.",
    "comparison": None,
    "guideline_note": "بعض الإرشادات الحديثة تسمح بمدة أقصر (3 أشهر) لو كان الـ<bdi>cause</bdi> مؤقتًا وزال، بس جواب الملف هنا (6 أشهر) هو المعتمد على البطاقة.",
}
WHY_WRONG[98] = {
    "A": "6 أسابيع قصيرة جدًا ولا تكفي لتقليل <bdi>risk</bdi> تكرار <bdi>pulmonary embolism</bdi>.",
    "B": "3 أشهر تناسب أكثر حالات الـ<bdi>cause</bdi> المؤقت الواضح، والملف هنا يعتمد مدة أطول.",
    "D": "12 شهر أطول من اللازم لأول نوبة <bdi>embolism</bdi> رئوي بدون <bdi>factors</bdi> <bdi>risk</bdi> دائمة موثقة.",
}
HIGHLIGHT_TERMS[98] = ["optimal duration of anticoagulation following an initial episode of pulmonary", "embolism"]

EXPLANATIONS[99] = {
    "idea": "السؤال يبي الـ<bdi>disease</bdi> اللي فيه <bdi>pneumonia</bdi> خلالي (interstitial pneumonitis) <bdi>sign</bdi> نسيجية مميزة، وهذا نموذج مرتبط بالعدوى الفيروسية.",
    "clues": [
        ("interstitial pneumonitis a characteristic", "<bdi>sign</bdi> نسيجية توجه لنمط الإصابة الفيروسي بالرئة"),
    ],
    "why_correct": [
        "<bdi>pneumonia</bdi> الفيروسي يصيب النسيج الخلالي حول الحويصلات الهوائية بشكل أساسي، فيعطي صورة نسيجية من نوع <bdi>interstitial pneumonitis</bdi>.",
        "<bdi>pneumonia</bdi> الفصي والقصبي (البكتيري) يملأ الحويصلات الهوائية نفسها بإفرازات التهابية (نمط سنخي)، مو النسيج الخلالي المحيط.",
        "<bdi>tuberculosis</bdi> الثانوي يعطي صورة نسيجية مميزة بالورم الحبيبي الجبني (caseating granuloma)، مختلفة تمامًا عن الالتهاب الخلالي.",
    ],
    "when_changes": [
        "لو الصورة النسيجية أظهرت امتلاء الحويصلات بإفرازات صديدية، يتجه الـ<bdi>diagnosis</bdi> للالتهاب الرئوي البكتيري الفصي أو القصبي بدل الفيروسي.",
    ],
    "rule": "<bdi>pneumonia</bdi> الفيروسي يصيب النسيج الخلالي (interstitial pneumonitis)، بعكس البكتيري اللي يملأ الحويصلات نفسها.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[99] = {
    "B": "<bdi>pneumonia</bdi> الفصي يعطي نمط سنخي بإفرازات تملأ الحويصلات، مو خلالي.",
    "C": "الالتهاب القصبي الرئوي أيضًا نمط سنخي التهابي، مختلف عن الالتهاب الخلالي.",
    "D": "<bdi>tuberculosis</bdi> الثانوي يعطي ورم حبيبي جبني مميز، مختلف تمامًا عن الالتهاب الخلالي.",
}
HIGHLIGHT_TERMS[99] = ["interstitial pneumonitis a characteristic"]

EXPLANATIONS[100] = {
    "idea": "السؤال يبي أي نوع تغبر رئوي (pneumoconiosis) يهيئ بقوة للإصابة ب<bdi>tuberculosis</bdi> الرئوي، وهذا معروف جدًا مع السيليكوزس.",
    "clues": [
        ("predispose to the development of", "يبي تحديد نوع التغبر الرئوي المرتبط بزيادة <bdi>risk</bdi> <bdi>tuberculosis</bdi>"),
    ],
    "why_correct": [
        "<bdi>Silicosis</bdi> (تغبر السيليكا) معروف علميًا بارتباطه القوي والموثق جدًا بزيادة <bdi>risk</bdi> الإصابة ب<bdi>tuberculosis</bdi> الرئوي، ب<bdi>cause</bdi> تأثير جزيئات السيليكا على وظيفة الخلايا البلعمية بالرئة.",
        "الأسبستوزس والأنثراكوزس ما لهم نفس الارتباط القوي الموثق بزيادة <bdi>risk</bdi> <bdi>tuberculosis</bdi> مقارنة بالسيليكوزس.",
        "رئة المزارع (Farmer's lung) سببها تحسسي (فرط حساسية رئوي) وليست مرتبطة بزيادة <bdi>risk</bdi> <bdi>tuberculosis</bdi>.",
    ],
    "when_changes": [
        "لو السؤال عن تغبر مرتبط بزيادة <bdi>risk</bdi> سرطان الرئة بدل <bdi>tuberculosis</bdi>، يصير الأسبستوزس هو الإجابة الأنسب.",
    ],
    "rule": "السيليكوزس هو تغبر الرئة الأشهر والأكثر ارتباطًا بزيادة <bdi>risk</bdi> الإصابة ب<bdi>tuberculosis</bdi> الرئوي.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[100] = {
    "B": "الأسبستوزس أشهر ارتباطه بسرطان الرئة والورم المتوسطي، مو <bdi>tuberculosis</bdi> تحديدًا.",
    "C": "الأنثراكوزس (تغبر الفحم) ارتباطه ب<bdi>tuberculosis</bdi> أضعف بكثير من السيليكوزس.",
    "D": "رئة المزارع <bdi>disease</bdi> تحسسي وليس مرتبطًا بزيادة <bdi>risk</bdi> <bdi>tuberculosis</bdi>.",
}
HIGHLIGHT_TERMS[100] = ["predispose to the development of"]

EXPLANATIONS[101] = {
    "idea": "امرأة معها ذات الجنب وتحتاج بزل صدري، والسؤال يبي المستوى الضلعي الصحيح للإبرة على الخط الإبطي الأوسط لتجنب إصابة أعضاء البطن والحزمة العصبية الوعائية.",
    "clues": [
        ("needle should be<br>placed on the midaxillary line of the affected side", "تحديد الخط التشريحي المستخدم لإدخال الإبرة"),
    ],
    "why_correct": [
        "المستوى بين الضلعين الثامن والعاشر على الخط الإبطي الأوسط يعتبر آمنًا لأنه فوق مستوى الحجاب الحاجز غالبًا وتحت مستوى قمة الرئة، ويجنب إصابة أعضاء البطن أو الحزمة العصبية الوعائية.",
        "الإبرة يجب أن تدخل فوق حافة الضلع السفلي مباشرة (مو تحته) لتجنب الحزمة العصبية الوعائية الموجودة أسفل كل ضلع.",
        "المستويات الأعلى (الرابع أو الخامس أو بين السادس والسابع) قد تكون قريبة جدًا من الرئة أو فوق مستوى السائل المتجمع فعليًا.",
    ],
    "when_changes": [
        "لو تحديد المستوى تم بالتوجيه بالسونار مباشرة، يُختار الموقع الفعلي لتجمع السائل بدل الاعتماد فقط على قاعدة تشريحية ثابتة.",
    ],
    "rule": "بزل الصدر على الخط الإبطي الأوسط يتم عادة بين الضلعين الثامن والعاشر، فوق حافة الضلع السفلي مباشرة، لتجنب أعضاء البطن والحزمة العصبية الوعائية.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[101] = {
    "A": "المستوى الرابع أعلى من اللازم وقريب جدًا من أنسجة الرئة السليمة.",
    "B": "المستوى الخامس أيضًا <bdi>elevated</bdi> وقد يكون فوق مستوى السائل المتجمع فعليًا.",
    "C": "المستوى بين السادس والسابع أعلى من المستوى الأكثر أمانًا الموصى به على الخط الإبطي الأوسط.",
}
HIGHLIGHT_TERMS[101] = ["needle should be", "placed on the midaxillary line of the affected side"]

EXPLANATIONS[102] = {
    "idea": "نفس فكرة السؤال 17 بالضبط: رجل معه حمى وتعرق ليلي وكحة لأسبوعين مع تصلب بالفص العلوي الأيمن بالأشعة، وهذي صورة <bdi>tuberculosis</bdi> رئوي نشط تستدعي عزل فوري.",
    "clues": [
        ("fever, night sweats, and<br>cough for 2 weeks", "صورة كلاسيكية توحي ب<bdi>tuberculosis</bdi> الرئوي النشط"),
        ("Right upper lobe consolidation", "تصلب بالفص العلوي، موقع كلاسيكي لل<bdi>tuberculosis</bdi> الرئوي"),
    ],
    "why_correct": [
        "تصلب الفص العلوي مع حمى وتعرق ليلي وكحة <bdi>chronic</bdi> يوجّه بقوة لل<bdi>tuberculosis</bdi> الرئوي النشط، ويجب عزل الـ<bdi>patient</bdi> فورًا بغرفة ضغط سلبي قبل أي <bdi>procedure</bdi> آخر.",
        "العزل <bdi>step</bdi> إدارية فورية تسبق حتى تأكيد الـ<bdi>diagnosis</bdi>، لأن <bdi>tuberculosis</bdi> ينتقل بالهواء (<bdi>airborne</bdi>) وتأخير العزل يعرض الآخرين ل<bdi>risk</bdi> العدوى.",
        "منظار القصبات أو الدخول للعناية العادية <bdi>procedures</bdi> لاحقة، والتأجيل لعيادة خارجية بعد أسبوعين <bdi>risk</bdi> جدًا مع اشتباه <bdi>tuberculosis</bdi> نشط.",
    ],
    "when_changes": [
        "بعد العزل، الـ<bdi>step</bdi> التالية المنطقية تكون إرسال القشع لفحص العصيات الصامدة للحمض.",
    ],
    "rule": "أي اشتباه ب<bdi>tuberculosis</bdi> رئوي نشط (تصلب فص علوي، حمى وتعرق ليلي <bdi>chronic</bdi>) يستوجب العزل بغرفة ضغط سلبي فورًا.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[102] = {
    "A": "منظار القصبات <bdi>procedure</bdi> تشخيصي يأتي لاحقًا، مو الـ<bdi>procedure</bdi> الفوري الأول.",
    "B": "الدخول للعناية المركزة غير ضروري إلا لو فيه فشل تنفسي أو صدمة إنتانية، وهذا غير مذكور.",
    "C": "تأجيل الـ<bdi>patient</bdi> لعيادة خارجية بعد أسبوعين <bdi>risk</bdi> جدًا مع اشتباه <bdi>tuberculosis</bdi> نشط قد ينشر العدوى.",
}
HIGHLIGHT_TERMS[102] = ["fever, night sweats, and", "Right upper lobe consolidation"]

EXPLANATIONS[103] = {
    "idea": "السؤال يبي أي <bdi>treatment</bdi> فعليًا يحسّن معدل البقيا (survival) بمرضى <bdi>COPD</bdi> الـ<bdi>severe</bdi>، وهذا مثبت فقط مع الأكسجين المكمل عند وجود نقص أكسجين <bdi>chronic</bdi>.",
    "clues": [
        ("improve survival in patients with severe chronic obstructive", "يبي تحديد الـ<bdi>treatment</bdi> المثبت لتحسين البقيا بالـ<bdi>disease</bdi> الـ<bdi>severe</bdi>"),
    ],
    "why_correct": [
        "الأكسجين المكمل طويل المدى (<bdi>long-term oxygen therapy</bdi>) هو الـ<bdi>treatment</bdi> الوحيد المثبت أنه يحسّن معدل البقيا بمرضى <bdi>COPD</bdi> الـ<bdi>severe</bdi> مع نقص أكسجين <bdi>chronic</bdi>.",
        "الستيرويدات المستنشقة وناهضات بيتا يحسنون الـ<bdi>symptoms</bdi> ومعدل التفاقم بس ما أثبتوا تحسين معدل البقيا بنفس درجة الأكسجين المكمل.",
        "الإقلاع عن التدخين يبطئ تدهور وظيفة الرئة بشكل مهم جدًا، بس السؤال هنا يخص تحسين البقيا تحديدًا بالـ<bdi>disease</bdi> الـ<bdi>severe</bdi> المتقدم، والأكسجين هو الإجابة المثبتة الأقوى بهالسياق.",
    ],
    "when_changes": [
        "لو السؤال عن أهم <bdi>procedure</bdi> يبطئ تدهور الـ<bdi>disease</bdi> بمراحله المبكرة، يصير الإقلاع عن التدخين هو الإجابة الأهم.",
    ],
    "rule": "الأكسجين المكمل طويل المدى هو الـ<bdi>treatment</bdi> الوحيد المثبت لتحسين معدل البقيا بمرضى <bdi>COPD</bdi> الـ<bdi>severe</bdi> مع نقص أكسجين <bdi>chronic</bdi>.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[103] = {
    "A": "الستيرويدات المستنشقة تحسّن الـ<bdi>symptoms</bdi> ومعدل التفاقم بس ما أثبتت نفس تحسين البقيا.",
    "C": "الإقلاع عن التدخين مهم جدًا لإبطاء تدهور الـ<bdi>disease</bdi>، بس السؤال هنا عن تحسين البقيا بالمرحلة الـ<bdi>severe</bdi> تحديدًا.",
    "D": "ناهضات بيتا تحسّن الـ<bdi>symptoms</bdi> بس ما تحسّن معدل البقيا.",
}
HIGHLIGHT_TERMS[103] = ["improve survival in patients with severe chronic obstructive"]

EXPLANATIONS[104] = {
    "idea": "شاب عنده <bdi>asthma</bdi> معتدل مستمر على جرعة <bdi>low</bdi> من الستيرويد المستنشق بس يحتاج ناهض بيتا سريع المفعول يوميًا تقريبًا، وهذا يعني التحكم غير كافٍ ويحتاج <bdi>step</bdi> إضافية بالـ<bdi>treatment</bdi>.",
    "clues": [
        ("moderate persistent asthma", "درجة <bdi>asthma</bdi> تحدد الـ<bdi>step</bdi> العلاجية المناسبة"),
        ("needs to use a beta-2 agonist rescue inhaler at least once a day", "استخدام يومي للبخاخ السريع يعني التحكم غير كافٍ بالـ<bdi>treatment</bdi> الحالي"),
    ],
    "why_correct": [
        "إضافة ناهض بيتا طويل المفعول (<bdi>LABA</bdi>) للستيرويد المستنشق هي الـ<bdi>step</bdi> القياسية التالية عند عدم التحكم الكافي ب<bdi>asthma</bdi> مع جرعة <bdi>low</bdi> من الستيرويد وحده.",
        "توليفة الستيرويد المستنشق مع LABA أفضل من مجرد زيادة جرعة الستيرويد وحده بهالمرحلة، وأكثر فعالية من إضافة الثيوفيللين أو مضاد اللوكوترايين ك<bdi>step</bdi> تالية أولى.",
        "الإيبراتروبيوم بروميد يستخدم أكثر ب<bdi>treatment</bdi> <bdi>COPD</bdi>، دوره محدود ب<bdi>treatment</bdi> <bdi>asthma</bdi> الـ<bdi>chronic</bdi> الروتيني.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عنده تفضيل أو مانع لاستخدام LABA، يصير مضاد اللوكوترايين بديلًا مقبولًا ك<bdi>step</bdi> إضافية.",
    ],
    "rule": "إضافة ناهض بيتا طويل المفعول للستيرويد المستنشق هي الـ<bdi>step</bdi> التالية القياسية عند عدم التحكم ب<bdi>asthma</bdi> المعتدل المستمر.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[104] = {
    "A": "الثيوفيللين خيار إضافي أقل تفضيلًا من LABA ب<bdi>cause</bdi> ضيق نافذته العلاجية وآثاره الجانبية.",
    "B": "مضاد اللوكوترايين خيار بديل مقبول بس أقل فعالية عمومًا من إضافة LABA بهالمرحلة.",
    "D": "الإيبراتروبيوم بروميد دوره الأساسي ب<bdi>treatment</bdi> <bdi>COPD</bdi>، مو الـ<bdi>step</bdi> القياسية ب<bdi>asthma</bdi>.",
}
HIGHLIGHT_TERMS[104] = ["moderate persistent asthma", "needs to use a beta-2 agonist rescue inhaler at least once a day"]

EXPLANATIONS[105] = {
    "idea": "<bdi>patient</bdi> انسداد رئوي <bdi>chronic</bdi> بضيق نفس <bdi>severe</bdi> ونقص أكسجين وحماض تنفسي <bdi>mild</bdi> (pH 7.3) بدون تحسن على الموسعات، بس واعٍ تمامًا، والسؤال يبي الـ<bdi>step</bdi> التالية قبل اللجوء للتنبيب.",
    "clues": [
        ("no improvement after bronchodilators", "فشل الـ<bdi>treatment</bdi> الأولي بالموسعات يستدعي <bdi>step</bdi> أقوى"),
        ("conscious with a pH of 7.3", "وعي محفوظ مع حماض تنفسي <bdi>mild</bdi> إلى متوسط، يسمح بتجربة التهوية غير الغازية أولًا"),
    ],
    "why_correct": [
        "التهوية بالضغط الإيجابي غير الغازية (<bdi>NIV</bdi>) هي الـ<bdi>step</bdi> التالية الموصى بها ل<bdi>patient</bdi> واعٍ بفشل تنفسي <bdi>acute</bdi> مع حماض تنفسي (pH 7.3) لم يتحسن على الموسعات، قبل اللجوء للتنبيب الغازي.",
        "الأمينوفيللين الوريدي أقل فعالية وأكثر خطورة (تسمم) مقارنة بـ NIV ك<bdi>step</bdi> تالية بهالحالة.",
        "تكرار الموسعات وحدها بدون NIV غير كافٍ لأن الـ<bdi>patient</bdi> أصلًا لم يستجب لها، والميثيل <bdi>prednisolone</bdi> <bdi>treatment</bdi> داعم مهم بس ما يعالج الفشل التنفسي الـ<bdi>acute</bdi> فورًا.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> فقد الوعي أو تدهور الحماض بشدة رغم NIV، يصير التنبيب والتهوية الغازية هي الـ<bdi>step</bdi> التالية الضرورية.",
    ],
    "rule": "ب<bdi>patient</bdi> واعٍ بتفاقم COPD وفشل تنفسي <bdi>acute</bdi> لم يتحسن على الموسعات، التهوية غير الغازية (NIV) هي الـ<bdi>step</bdi> التالية قبل التنبيب.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[105] = {
    "A": "الأمينوفيللين الوريدي أقل فعالية وأكثر خطورة من NIV ك<bdi>step</bdi> تالية.",
    "B": "الميثيل <bdi>prednisolone</bdi> <bdi>treatment</bdi> داعم مهم بس ما يعالج الفشل التنفسي الـ<bdi>acute</bdi> فورًا مثل NIV.",
    "C": "تكرار الموسعات غير كافٍ لأن الـ<bdi>patient</bdi> أصلًا لم يستجب لها من البداية.",
}
HIGHLIGHT_TERMS[105] = ["no improvement after bronchodilators", "conscious with a pH of 7.3"]

EXPLANATIONS[106] = {
    "idea": "السؤال يبي أفعل <bdi>treatment</bdi> لتوقف التنفس الانسدادي أثناء النوم (OSA) عند البالغين، وهو جهاز الضغط الهوائي الإيجابي المستمر.",
    "clues": [
        ("obstructive sleep", "<bdi>case</bdi> توقف تنفس أثناء النوم تحتاج <bdi>treatment</bdi> فعال ومثبت"),
    ],
    "why_correct": [
        "<bdi>Continuous positive airway pressure (CPAP)</bdi> هو الـ<bdi>treatment</bdi> الأكثر فعالية وموثوقية المثبت لتوقف التنفس الانسدادي أثناء النوم عند البالغين.",
        "المودافينيل يعالج النعاس النهاري ك<bdi>symptom</bdi> مصاحب بس ما يعالج الـ<bdi>cause</bdi> الأساسي وهو انسداد مجرى الهواء أثناء النوم.",
        "إنقاص الوزن وأجهزة الفم المساعدة تحسّن الـ<bdi>case</bdi> بدرجات متفاوتة بس أقل فعالية بشكل عام من CPAP ك<bdi>treatment</bdi> أول للحالات المتوسطة والـ<bdi>severe</bdi>.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>case</bdi> <bdi>mild</bdi> جدًا أو الـ<bdi>patient</bdi> لا يتحمل CPAP، تصير أجهزة الفم أو إنقاص الوزن خيارات بديلة مقبولة.",
    ],
    "rule": "جهاز CPAP هو الـ<bdi>treatment</bdi> الأكثر فعالية لتوقف التنفس الانسدادي أثناء النوم عند البالغين.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[106] = {
    "A": "المودافينيل يعالج النعاس ك<bdi>symptom</bdi> بس ما يعالج انسداد مجرى الهواء الأساسي.",
    "B": "إنقاص الوزن يحسّن الـ<bdi>case</bdi> بس أقل فعالية بمفرده من CPAP ك<bdi>treatment</bdi> أول.",
    "C": "أجهزة الفم المساعدة خيار بديل بس أقل فعالية عمومًا من CPAP بالحالات المتوسطة والـ<bdi>severe</bdi>.",
}
HIGHLIGHT_TERMS[106] = ["obstructive sleep"]

EXPLANATIONS[107] = {
    "idea": "شاب عنده <bdi>asthma</bdi> متقطع <bdi>mild</bdi> (<bdi>symptoms</bdi> نهارية مرة أو مرتين أسبوعيًا وبدون <bdi>symptoms</bdi> ليلية)، والسؤال يبي الـ<bdi>treatment</bdi> المناسب عند الحاجة فقط لهالدرجة الـ<bdi>mild</bdi>.",
    "clues": [
        ("mild intermittent asthma", "درجة <bdi>asthma</bdi> <bdi>mild</bdi> تحدد الـ<bdi>treatment</bdi> المناسب"),
        ("daytime symptoms about once to<br>twice a week and none at night", "تكرار <bdi>symptoms</bdi> قليل جدًا، يطابق <bdi>asthma</bdi> المتقطع الـ<bdi>mild</bdi>"),
    ],
    "why_correct": [
        "ب<bdi>asthma</bdi> المتقطع الـ<bdi>mild</bdi>، يكفي استخدام ناهض بيتا قصير المفعول (<bdi>SABA</bdi>) عند الحاجة فقط بدون <bdi>treatment</bdi> يومي منتظم.",
        "الستيرويد المستنشق بجرعة عالية أو مضادات اللوكوترايين <bdi>treatment</bdi> يومي منتظم يُحجز لدرجات أعلى من <bdi>asthma</bdi> (المستمر) مو المتقطع الـ<bdi>mild</bdi>.",
        "الأمينوفيللين الفموي دواء قديم أقل أمانًا وفعالية، وما يستخدم كخط أول لأي درجة من <bdi>asthma</bdi> حاليًا.",
    ],
    "when_changes": [
        "لو زادت الـ<bdi>symptoms</bdi> النهارية لأكثر من مرتين أسبوعيًا أو ظهرت <bdi>symptoms</bdi> ليلية، يصير التصنيف <bdi>asthma</bdi> مستمر <bdi>mild</bdi> ويحتاج ستيرويد مستنشق يومي منتظم.",
    ],
    "rule": "ب<bdi>asthma</bdi> المتقطع الـ<bdi>mild</bdi>، يكفي ناهض بيتا قصير المفعول عند الحاجة فقط بدون <bdi>treatment</bdi> يومي.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[107] = {
    "B": "الستيرويد المستنشق بجرعة عالية <bdi>treatment</bdi> مبالغ فيه لدرجة <bdi>asthma</bdi> الـ<bdi>mild</bdi> المتقطعة هنا.",
    "C": "مضادات اللوكوترايين <bdi>treatment</bdi> يومي منتظم يُحجز لدرجات أعلى من <bdi>asthma</bdi>، مو المتقطع الـ<bdi>mild</bdi>.",
    "D": "الأمينوفيللين الفموي دواء قديم أقل أمانًا، وما يستخدم كخط أول لأي درجة من <bdi>asthma</bdi> حاليًا.",
}
HIGHLIGHT_TERMS[107] = ["mild intermittent asthma", "daytime symptoms about once to"]

EXPLANATIONS[108] = {
    "idea": "امرأة كان عندها <bdi>asthma</bdi> متقطع <bdi>mild</bdi>، وصارت تستخدم البخاخ السريع 3 مرات أسبوعيًا مع <bdi>symptoms</bdi> ليلية، وهذا تدهور يصنف الآن ك<bdi>asthma</bdi> مستمر <bdi>mild</bdi> يحتاج <bdi>treatment</bdi> يومي.",
    "clues": [
        ("using<br>her inhaler at least 3 times a week", "زيادة تكرار الاستخدام تدل على تدهور درجة <bdi>asthma</bdi>"),
        ("wake up in the middle of<br>the night to use her inhaler", "<bdi>symptoms</bdi> ليلية جديدة، <bdi>sign</bdi> مهمة على تدهور التحكم ب<bdi>asthma</bdi>"),
    ],
    "why_correct": [
        "استخدام البخاخ السريع 3 مرات أسبوعيًا مع <bdi>symptoms</bdi> ليلية يعني تحول التصنيف من <bdi>asthma</bdi> متقطع ل<bdi>asthma</bdi> مستمر <bdi>mild</bdi>، ويستوجب إضافة ستيرويد مستنشق يومي منتظم.",
        "الستيرويد المستنشق هو الـ<bdi>treatment</bdi> المضاد للالتهاب الأكثر فعالية وأساسًا للتحكم طويل المدى ب<bdi>asthma</bdi> المستمر، ويُفضّل ك<bdi>step</bdi> أولى قبل أي إضافات أخرى.",
        "مضاد مستقبلات اللوكوترايين وناهض بيتا طويل المفعول والكرومولين خيارات ثانوية أو مساعدة، بس مو الـ<bdi>step</bdi> الأولى المفضلة للتحول من متقطع لمستمر <bdi>mild</bdi>.",
    ],
    "when_changes": [
        "لو استمرت الـ<bdi>symptoms</bdi> غير متحكم بها رغم الستيرويد المستنشق بجرعة <bdi>low</bdi>، تضاف بعدها ناهض بيتا طويل المفعول ك<bdi>step</bdi> تالية.",
    ],
    "rule": "زيادة استخدام البخاخ السريع مع ظهور <bdi>symptoms</bdi> ليلية يعني تحول <bdi>asthma</bdi> لمستمر <bdi>mild</bdi>، ويستوجب بدء ستيرويد مستنشق يومي.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[108] = {
    "A": "مضاد مستقبلات اللوكوترايين خيار بديل أضعف من الستيرويد المستنشق ك<bdi>step</bdi> أولى بهالتحول.",
    "B": "ناهض بيتا طويل المفعول يُضاف لاحقًا مع الستيرويد لو ما تحكم الستيرويد وحده، مو الـ<bdi>step</bdi> الأولى.",
    "D": "الكرومولين أقل فعالية عمومًا من الستيرويد المستنشق ك<bdi>treatment</bdi> مضاد التهاب أساسي ب<bdi>asthma</bdi> المستمر.",
}
HIGHLIGHT_TERMS[108] = ["using", "wake up in the middle of"]

EXPLANATIONS[109] = {
    "idea": "رجل مدخن معه ضيق نفس وكحة منتجة و<bdi>wheeze</bdi> منتشر بالفحص، بس الأشعة وغازات الدم <bdi>normal</bdi>، وهذي صورة كلاسيكية للانسداد الرئوي الـ<bdi>chronic</bdi> (التهاب الشعب الهوائية الـ<bdi>chronic</bdi>) بمرحلة مستقرة نسبيًا.",
    "clues": [
        ("history of smoking", "<bdi>factor</bdi> الـ<bdi>risk</bdi> الرئيسي للانسداد الرئوي الـ<bdi>chronic</bdi>"),
        ("wheezing throughout the chest", "<bdi>wheeze</bdi> منتشر يدعم <bdi>disease</bdi> مجرى هوائي انسدادي <bdi>chronic</bdi>"),
        ("Chest X-ray: Normal", "أشعة <bdi>normal</bdi> لا تنفي <bdi>disease</bdi> مجرى هوائي انسدادي <bdi>chronic</bdi> مبكر أو مستقر"),
    ],
    "why_correct": [
        "تاريخ تدخين طويل مع كحة منتجة و<bdi>wheeze</bdi> منتشر يطابق الصورة الكلاسيكية للانسداد الرئوي الـ<bdi>chronic</bdi> (<bdi>COPD</bdi>)، حتى مع أشعة صدر <bdi>normal</bdi> بمراحل مبكرة أو مستقرة.",
        "<bdi>pulmonary fibrosis</bdi> يعطي صورة أشعة غير <bdi>normal</bdi> (خطوط شبكية) عادة، وهذا يخالف الأشعة الـ<bdi>normal</bdi> هنا.",
        "<bdi>disease</bdi> الرئة المهني وداء ترسب الهيموسيديرين الرئوي مجهول الـ<bdi>cause</bdi> <bdi>causes</bdi> أندر بكثير من COPD عند مدخن بهالعرض الكلاسيكي.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> غير مدخن أبدًا مع تعرض مهني واضح لغبار أو مواد كيميائية، يميل الـ<bdi>diagnosis</bdi> ل<bdi>disease</bdi> الرئة المهني بدل COPD.",
    ],
    "rule": "تاريخ تدخين طويل مع كحة منتجة و<bdi>wheeze</bdi> <bdi>chronic</bdi> يوجّه للانسداد الرئوي الـ<bdi>chronic</bdi> حتى مع أشعة وغازات دم <bdi>normal</bdi> بالمراحل المبكرة.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[109] = {
    "A": "<bdi>pulmonary fibrosis</bdi> يعطي صورة أشعة غير <bdi>normal</bdi> عادة (خطوط شبكية)، بعكس الأشعة الـ<bdi>normal</bdi> هنا.",
    "B": "<bdi>disease</bdi> الرئة المهني يحتاج تاريخ تعرض مهني واضح، وهذا غير مذكور، والتدخين هو <bdi>factor</bdi> الـ<bdi>risk</bdi> الوحيد المذكور.",
    "C": "داء ترسب الهيموسيديرين الرئوي مجهول الـ<bdi>cause</bdi> <bdi>disease</bdi> نادر جدًا مقارنة بـ COPD عند مدخن بهالعرض الكلاسيكي.",
}
HIGHLIGHT_TERMS[109] = ["history of smoking", "wheezing throughout the chest"]

EXPLANATIONS[110] = {
    "idea": "شاب فجأة صار عنده ألم صدر وضيق نفس مع نقص وضوح اللمس الصوتي وغياب أصوات التنفس، والأشعة تظهر غياب تام ل<bdi>signs</bdi> الرئة باليسار، وهذي صورة كلاسيكية ل<bdi>pneumothorax</bdi> التلقائي.",
    "clues": [
        ("suddenly develops chest pain and dyspnea", "بداية مفاجئة، نموذجية ل<bdi>pneumothorax</bdi> التلقائي عند شاب"),
        ("Vocal and tactile<br>fremitus are reduced, and breath sounds are diminished", "<bdi>signs</bdi> فحص كلاسيكية لهواء محبوس بالجنب"),
        ("absent lung markings on the left side", "غياب تام ل<bdi>signs</bdi> الرئة بالأشعة، تأكيد تشخيصي ل<bdi>pneumothorax</bdi>"),
    ],
    "why_correct": [
        "البداية المفاجئة عند شاب مع غياب تام ل<bdi>signs</bdi> الرئة بالأشعة على جانب واحد صورة تشخيصية مؤكدة ل<bdi>pneumothorax</bdi> التلقائي (<bdi>Spontaneous pneumothorax</bdi>).",
        "غياب أصوات التنفس ونقص وضوح اللمس الصوتي يحدثان لأن الهواء المحبوس بالجنب يعزل الرئة عن جدار الصدر، وهذا يطابق الفحص السريري تمامًا.",
        "<bdi>tuberculosis</bdi> و<bdi>pulmonary embolism</bdi> والنفاخ الرئوي ما يعطون غياب تام مفاجئ ل<bdi>signs</bdi> الرئة بهالشكل الـ<bdi>acute</bdi> المفاجئ عند شاب سليم.",
    ],
    "when_changes": [
        "لو كانت البداية تدريجية مع تاريخ تدخين طويل وصورة أشعة تظهر فرط هوائية منتشر بدل غياب تام لل<bdi>signs</bdi>، يتجه الـ<bdi>diagnosis</bdi> للنفاخ الرئوي بدل الاسترواح التلقائي.",
    ],
    "rule": "بداية مفاجئة لألم صدر وضيق نفس عند شاب مع غياب تام ل<bdi>signs</bdi> الرئة بالأشعة على جانب واحد تعني استرواح صدر تلقائي.",
    "comparison": None,
    "guideline_note": None,
}
WHY_WRONG[110] = {
    "B": "<bdi>tuberculosis</bdi> الرئوي <bdi>disease</bdi> تدريجي <bdi>chronic</bdi>، ولا يعطي بداية مفاجئة بهالشكل الـ<bdi>acute</bdi>.",
    "C": "<bdi>pulmonary embolism</bdi> يعطي ألم صدر وضيق نفس مفاجئ بس عادة بدون غياب تام ل<bdi>signs</bdi> الرئة بالأشعة.",
    "D": "النفاخ الرئوي <bdi>disease</bdi> <bdi>chronic</bdi> تدريجي، ما يعطي بداية مفاجئة <bdi>acute</bdi> بهالشكل عند شاب.",
}
HIGHLIGHT_TERMS[110] = ["suddenly develops chest pain and dyspnea", "absent lung markings on the left side"]
