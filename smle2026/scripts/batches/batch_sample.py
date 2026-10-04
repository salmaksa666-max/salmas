# -*- coding: utf-8 -*-
# Worked reference example for questions 1-5 (mix of source-answer and
# self-judged questions). Study this before writing any real batch.

TOPICS = {
    1: "General Surgery",
    2: "Preventive & Community Medicine",
    3: "Obstetrics & Gynecology",
    4: "Nephrology",
    5: "Pediatrics",
    53: "General Surgery",
}

EXPLANATIONS = {
1: {
    "correct_letter": "B",
    "self_judged": True,
    "idea": "هذا سيناريو <bdi>near-miss wrong-site surgery</bdi>، ممرضة لاحظت خطأ بس سكتت، وموظف ثاني اكتشفه بمراجعة الملف قبل الشق. السؤال يبي أفضل إجراء يمنع تكرار هالخطأ.",
    "clues": [
        ("incision on the wrong leg", "خطأ وشيك بتحديد مكان الجراحة، النوع يسمى <bdi>wrong-site surgery</bdi>"),
        ("nurse knew but kept quite", "فشل بالتواصل داخل الفريق، سبب رئيسي لمثل هالأخطاء"),
        ("checked the patient's file before the incision", "المراجعة الفعلية اللي كشفت الخطأ بالوقت المناسب"),
    ],
    "why_correct": [
        "اللي فعليًا منع الخطأ بهالموقف هو مراجعة ملف الـ<bdi>patient</bdi> قبل الشق، وهذا يوضح إن مراجعة الملف خطوة أساسية بأي <bdi>surgical safety protocol</bdi>.",
        "السؤال يسأل عن الإجراء اللي يمنع مثل هالحالة مستقبلًا، ومراجعة الملف هي الخطوة اللي كشفت الخطأ فعليًا بالسيناريو نفسه.",
        "تجاهل الممرضة لشكها (الخيار A) هو بالضبط سبب المشكلة، مو حل لها.",
    ],
    "when_changes": [
        "لو السؤال يركز على منع الخطأ من الأساس قبل دخول غرفة العمليات، يصير الجواب الأقوى هو <bdi>proper site marking</bdi> (جزء من <bdi>WHO Surgical Safety Checklist</bdi>).",
        "لو السؤال يبي خطوة أثناء <bdi>time-out</bdi> بغرفة العمليات تحديدًا، يصير الجواب التحقق الجماعي اللفظي من هوية الـ<bdi>patient</bdi> والموقع قبل الشق.",
    ],
    "rule": "مراجعة ملف الـ<bdi>patient</bdi> والتحقق من البيانات قبل أي إجراء جراحي خطوة أساسية لمنع أخطاء الموقع الجراحي.",
    "comparison": None,
    "guideline_note": None,
},
2: {
    "correct_letter": "C",
    "self_judged": True,
    "idea": "سؤال حساب <bdi>sensitivity</bdi> لفحص فحص جديد مقارنة بمعيار مرجعي (<bdi>mammogram</bdi>). لازم نرجع لتعريف <bdi>sensitivity</bdi> ونطبقه بالأرقام المعطاة بالضبط.",
    "clues": [
        ("mammogram identifies 200 women", "عدد الحالات الموجبة الحقيقية حسب المعيار المرجعي (<bdi>true positives + false negatives</bdi>)"),
        ("correctly identifies 180", "عدد <bdi>true positives</bdi> للفحص الجديد"),
        ("misses 20", "عدد <bdi>false negatives</bdi> للفحص الجديد"),
    ],
    "why_correct": [
        "<bdi>Sensitivity</bdi> = <bdi>true positives</bdi> ÷ (<bdi>true positives + false negatives</bdi>) = 180 ÷ (180+20) = 180/200 = 90%.",
        "المرجع هنا هو الـ200 حالة اللي أكدها الـ<bdi>mammogram</bdi> (المعيار الذهبي بالسؤال)، مو كل الـ1000 امرأة.",
        "عدد الـ<bdi>false positives</bdi> (50) ما يدخل بحساب الـ<bdi>sensitivity</bdi> إطلاقًا، هو يدخل بحساب الـ<bdi>specificity</bdi> بس.",
    ],
    "when_changes": [
        "لو السؤال يبي الـ<bdi>specificity</bdi> بدل الـ<bdi>sensitivity</bdi>، نحتاج نعرف عدد <bdi>true negatives</bdi> من الأصحاء الحقيقيين (800 امرأة)، ونحسب <bdi>TN/(TN+FP)</bdi>.",
        "لو تغيّر عدد الـ<bdi>false negatives</bdi> لرقم ثاني، تتغير النتيجة مباشرة لأنها بالمقام.",
    ],
    "rule": "<bdi>Sensitivity</bdi> = <bdi>TP / (TP + FN)</bdi>، ويُحسب دايمًا من بين الحالات الموجبة الحقيقية فقط حسب المعيار المرجعي.",
    "comparison": {
        "headers": ["المقياس", "المعادلة", "يعتمد على"],
        "rows": [
            ["<bdi>Sensitivity</bdi>", "TP / (TP+FN)", "الحالات الموجبة الحقيقية"],
            ["<bdi>Specificity</bdi>", "TN / (TN+FP)", "الحالات السالبة الحقيقية"],
        ],
    },
    "guideline_note": None,
},
3: {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "حامل نباتية (<bdi>vegetarian</bdi>) من 4 سنوات، والسؤال يبي أهم فيتامين لازم نتابعه بسبب نمط أكلها. النباتيين طويلي المدى معرضين لنقص فيتامين معين مرتبط بمصادر حيوانية.",
    "clues": [
        ("primigravida", "حمل أول، لازم ننتبه للتغذية الأساسية من البداية"),
        ("vegetarian since 4 years", "نظام غذائي طويل المدى بدون مصادر حيوانية، عامل الخطر الأساسي هنا"),
    ],
    "why_correct": [
        "<bdi>Vitamin B12</bdi> موجود بشكل أساسي بمصادر حيوانية (لحم، سمك، بيض، ألبان)، والنباتيين طويلي المدى (خصوصًا <bdi>vegans</bdi>) معرضين لنقصه.",
        "نقص <bdi>B12</bdi> بالحمل خطير لأنه ضروري لتكوين الحمض النووي وكريات الدم الحمراء ونمو الجهاز العصبي للجنين، ونقصه يسبب <bdi>megaloblastic anemia</bdi> للأم أو <bdi>neural tube defects</bdi> للجنين.",
        "باقي الفيتامينات (K، C، E) نقصها نادر بالحمل أو غير مرتبط تحديدًا بنظام نباتي.",
    ],
    "when_changes": [
        "لو كانت المريضة تاكل بيض وألبان (نباتية لاكتو-أوفو مو <bdi>vegan</bdi> صارمة)، يقل خطر نقص <bdi>B12</bdi> بس يبقى أهم فيتامين يتابع بهالفئة.",
        "لو السؤال يذكر نزيف مولود جديد بدل مخاوف تغذوية، يصير التركيز على <bdi>Vitamin K</bdi> (يُعطى روتينيًا للمواليد).",
    ],
    "rule": "الحوامل النباتيات طويلات المدى (خصوصًا <bdi>vegan</bdi>) لازم يتابعن مستوى <bdi>Vitamin B12</bdi> لأنه أهم فيتامين معرض للنقص بنظامهن.",
    "comparison": None,
    "guideline_note": None,
},
4: {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "شاب عسكري بعد تدريب مجهد جدًا، عنده علامات جفاف واضحة (<bdi>postural hypotension</bdi>، تعب) مع بول مركّز جدًا (<bdi>osmolality &gt;500</bdi>). هذا نمط كلاسيكي لأذية كلوية سببها نقص التروية مو تلف مباشر بالكلية.",
    "clues": [
        ("excessive military training", "فقدان سوائل كبير بالتعرّق، سبب شائع لـ<bdi>volume depletion</bdi>"),
        ("postural hypotension", "علامة مباشرة على نقص الحجم داخل الأوعية"),
        ("Urine osmolality elevated &gt;500 mOsm/kg", "الكلى تركّز البول بشكل طبيعي استجابة لنقص الحجم، رد فعل كلية سليمة لا تلف فيها"),
    ],
    "why_correct": [
        "بـ<bdi>pre-renal azotemia</bdi>، الكلى سليمة تركيبيًا بس التروية الدموية لها ناقصة، فتحاول تعوّض بتركيز البول لأقصى درجة، وهذا بالضبط الموجود بالسؤال.",
        "لو كانت المشكلة <bdi>ATN</bdi> (تلف أنبوبي فعلي)، الكلى تفقد قدرتها على تركيز البول، فالـ<bdi>osmolality</bdi> يكون منخفض قريب من البلازما، عكس الموصوف هنا.",
        "ما فيه بالسؤال أي دليل حساسية دوائية (لـ<bdi>interstitial nephritis</bdi>) ولا بروتين أو دم بالبول (لـ<bdi>glomerulonephritis</bdi>).",
    ],
    "when_changes": [
        "لو كان البول مخفف (<bdi>osmolality</bdi> منخفض) رغم الجفاف، يصير الاحتمال الأقوى <bdi>ATN</bdi> ناتج عن <bdi>rhabdomyolysis</bdi> من التمرين الشاق.",
        "لو ظهر طفح جلدي وحمى مع تاريخ دوائي جديد، يصير <bdi>acute interstitial nephritis</bdi> هو الاحتمال الأقوى بدل <bdi>pre-renal</bdi>.",
    ],
    "rule": "بول مركّز جدًا مع علامات جفاف يدعم <bdi>pre-renal azotemia</bdi>، وبول مخفف رغم الجفاف يوجه لتلف أنبوبي فعلي (<bdi>ATN</bdi>).",
    "comparison": None,
    "guideline_note": None,
},
5: {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "طفل سقط من شجرة وصار عنده تورم بالرأس وتقيؤ ثم خمول (تدهور مستوى الوعي). هذا نمط يوحي بنزيف داخل الجمجمة متوسع (مثل <bdi>epidural hematoma</bdi>) يحتاج تدخل عاجل.",
    "clues": [
        ("fell from tree", "آلية إصابة قوية كافية لإحداث نزيف داخل الجمجمة"),
        ("head swelling", "دليل على إصابة مباشرة بفروة الرأس أو الجمجمة"),
        ("became drowsy", "تدهور مستوى الوعي، علامة تحذيرية لزيادة الضغط داخل الجمجمة"),
    ],
    "why_correct": [
        "التدهور التدريجي بمستوى الوعي بعد إصابة رأس مباشرة مع تورم موضعي يوحي بنزيف متوسع (<bdi>epidural</bdi> أو <bdi>subdural hematoma</bdi>) يضغط على الدماغ.",
        "الخطوة الحاسمة والعاجلة لتخفيف الضغط ومنع تلف دماغي دائم أو وفاة هي <bdi>hematoma evacuation</bdi> (تفريغ النزيف جراحيًا) بعد تأكيد التشخيص بالتصوير.",
        "الخمول المتزايد يدل على مشكلة ميكانيكية (ضغط وتمدد كتلة دموية) مو مشكلة تنفسية بحتة تحتاج <bdi>intubation</bdi> فقط كخطوة أولى.",
    ],
    "when_changes": [
        "لو كان الطفل فاقد الوعي تمامًا بدون تنفس كافٍ أو حماية مجرى هوائي، يصير تأمين مجرى الهواء (<bdi>intubation</bdi>) أولوية فورية قبل أي تصوير أو تدخل.",
        "لو كانت الأعراض خفيفة (صداع بسيط بدون تدهور وعي) بعد سقوط بسيط، المراقبة لوحدها كافية بدون تدخل جراحي.",
    ],
    "rule": "تدهور مستوى الوعي التدريجي بعد إصابة رأس مباشرة يوجه لنزيف داخل الجمجمة متوسع يحتاج تصوير عاجل وتدخل جراحي لتفريغه.",
    "comparison": None,
    "guideline_note": None,
},
53: {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفل انضرب بمقبض الدراجة (<bdi>handlebar injury</bdi>) بمنطقة البطن العلوية، وعنده ألم وتقيؤ مع <bdi>FAST</bdi> غير حاسم. هذا نمط كلاسيكي لإصابة عضو خلف الصفاق ما يظهر بسهولة بالموجات الصوتية.",
    "clues": [
        ("handlebar injury", "ضربة مباشرة بمنطقة شرسوفية، آلية كلاسيكية لإصابة البنكرياس عند الأطفال"),
        ("FAST Was Done And It Was Inconclusive", "البنكرياس عضو خلف الصفاق، إصابته ما تسبب سائل حر داخل البطن يُكتشف بسهولة بـ<bdi>FAST</bdi>"),
    ],
    "why_correct": [
        "ضربة مباشرة بمقبض الدراجة بمنطقة شرسوفية (فوق العمود الفقري) هي الآلية الكلاسيكية لإصابة <bdi>pancreas</bdi> عند الأطفال.",
        "البنكرياس عضو خلف الصفاق (<bdi>retroperitoneal</bdi>)، فإصابته غالبًا ما تنتج سائل حر كافي داخل التجويف البريتوني مبكرًا، وهذا يفسر ليش فحص <bdi>FAST</bdi> طلع غير حاسم.",
        "باقي الأعضاء (الطحال، الكبد، المثانة) داخل التجويف البريتوني أو الحوضي، وإصابتها عادة تعطي نتيجة أوضح بالـ<bdi>FAST</bdi>.",
    ],
    "when_changes": [
        "لو كانت الإصابة بالجانب الأيسر العلوي مع هبوط ضغط وفحص <bdi>FAST</bdi> إيجابي، يصير الطحال هو الاحتمال الأقوى.",
        "لو كان الدم ظاهر بالبول مع كسر حوضي، يوجه الشك للمثانة بدل البنكرياس.",
    ],
    "rule": "ضربة شرسوفية مباشرة (زي مقبض الدراجة) مع <bdi>FAST</bdi> غير حاسم تدل على إصابة عضو خلف الصفاق مثل <bdi>pancreas</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
}

WHY_WRONG = {
1: {
    "A": "تجاهل الشك وعدم التبليغ هو بالضبط سبب حدوث مثل هالأخطاء، مو حل لها.",
    "C": "التحديد الصحيح لمكان الجراحة مهم بس بهالسيناريو تحديدًا، مراجعة الملف هي اللي كشفت الخطأ فعليًا.",
},
2: {
    "A": "70% رقم غير صحيح حسابيًا حسب المعطيات.",
    "B": "80% رقم غير صحيح حسابيًا حسب المعطيات.",
    "D": "100% يعني ما فيه أي حالة فاتت الفحص الجديد، بينما السؤال يذكر صراحة 20 حالة فاتته.",
},
3: {
    "B": "نقص <bdi>Vitamin K</bdi> نادر بالحمل، ومرتبط أكثر بنزيف المواليد الجدد مو بتغذية الأم.",
    "C": "<bdi>Vitamin C</bdi> متوفر بكثرة بالفواكه والخضروات، والنباتيين عادة مستواهم كافٍ أو مرتفع.",
    "D": "نقص <bdi>Vitamin E</bdi> نادر جدًا وما يعتبر قلق معتاد بالحمل النباتي.",
},
4: {
    "B": "<bdi>Acute interstitial nephritis</bdi> يحتاج عادة دليل حساسية دوائية أو طفح جلدي وحمى، غير مذكور هنا.",
    "C": "<bdi>Acute glomerulonephritis</bdi> يعطي عادة بروتين ودم بالبول، وهذا غير مذكور بالسؤال.",
    "D": "لو كان <bdi>ATN</bdi>، لكان البول مخفف (<bdi>osmolality</bdi> منخفض) مو مركّز بهالشكل الشديد.",
},
5: {
    "B": "<bdi>Intubation</bdi> يفيد لو فيه فشل تنفسي أو فقدان وعي كامل يهدد مجرى الهواء، وهذا غير موصوف بوضوح هنا مقارنة بعلامات زيادة الضغط داخل الجمجمة.",
},
53: {
    "A": "الطحال عضو داخل الصفاق، وإصابته عادة تعطي سائل حر واضح يظهر بوضوح بفحص <bdi>FAST</bdi>.",
    "B": "الكبد كمان عضو داخل الصفاق، إصابته غالبًا تعطي نتيجة أوضح بـ<bdi>FAST</bdi> من الموصوف هنا.",
    "D": "إصابة المثانة ترتبط عادة بكسور حوضية أو دم بالبول، وهذا غير مذكور بالسؤال، والآلية هنا (ضربة شرسوفية) ما تناسبها.",
},
}

HIGHLIGHT_TERMS = {
1: ["the wrong leg", "kept quite", "checked the patient"],
2: ["identifies 200 women", "correctly identifies 180", "misses 20 women", "false positive"],
3: ["primigravida vegetarian since 4 years"],
4: ["excessive military training", "postural hypotension", "elevated"],
5: ["head swelling", "became drowsy"],
53: ["handlebar injury", "FAST Was Done And It Was Inconclusive"],
}
