# -*- coding: utf-8 -*-
# Batch 16 — 02- Pediatrics (AS-1078 .. AS-1734), 145 questions.

EXPLANATIONS = {
"AS-1078": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال يبي نفرق سبب <bdi>thrombocytopenia</bdi> عند <bdi>neonate</bdi> أمه عندها <bdi>SLE</bdi> بالاعتماد على <bdi>coagulation screen</bdi> الطبيعي.",
    "clues": [
        ("mother has a history of systemic lupus erythematosus (SLE)", "أجسام مضادة من الأم (<bdi>anti-platelet antibodies</bdi>) تعبر المشيمة وتدمر صفائح الجنين"),
        ("thrombocytopenia with normal PT and PTT", "المشكلة بالصفائح فقط، عوامل التجلط سليمة، فمو مشكلة <bdi>coagulation factors</bdi>"),
    ],
    "why_correct": [
        "<bdi>neonate</bdi> أمه عندها <bdi>SLE</bdi> ويجيه <bdi>thrombocytopenia</bdi> مع <bdi>PT</bdi> و<bdi>PTT</bdi> طبيعيين، يعني عنده مشكلة <bdi>immune-mediated</bdi> بالصفائح بس: أضداد الأم عبرت المشيمة ودمرت صفائح الطفل.",
        "بما إن عوامل التجلط سليمة، <bdi>treatment</bdi> يستهدف الصفائح مباشرة: <bdi>platelet transfusion</bdi> لوقف <bdi>active bleeding</bdi>، و<bdi>IVIG</bdi> يمنع تدمير الصفائح بالأضداد.",
        "هذا نفس نمط <bdi>management</bdi> المعياري لأي <bdi>immune thrombocytopenia</bdi> عند <bdi>neonate</bdi> مع <bdi>coagulation screen</bdi> طبيعي.",
    ],
    "when_changes": [
        "لو كانت <bdi>PT</bdi> و<bdi>PTT</bdi> طويلة مع صفائح طبيعية وما أخذ <bdi>vitamin K</bdi> بالولادة، الجواب يصير إعطاء <bdi>vitamin K</bdi>.",
        "لو كان فيه <bdi>bleeding</bdi> مع <bdi>PT/PTT</bdi> طويلة وفيبرينوجين منخفض (صورة <bdi>DIC</bdi>)، الجواب يصير <bdi>FFP</bdi> و<bdi>cryoprecipitate</bdi>.",
    ],
    "rule": "اقرأ <bdi>coagulation screen</bdi> قبل لا تختار العلاج: صفائح منخفضة مع <bdi>PT/PTT</bdi> طبيعي وسبب <bdi>immune</bdi> يعني <bdi>platelets</bdi> + <bdi>IVIG</bdi>، مو <bdi>FFP</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1080": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال يفرق بين <bdi>TTN</bdi> و<bdi>RDS</bdi> عند <bdi>newborn</bdi> أمه سكرية بالاعتماد على <bdi>gestational age</bdi> وشدة الأعراض.",
    "clues": [
        ("newborn term", "<bdi>term baby</bdi> ينقص احتمال <bdi>RDS</bdi> اللي أصلاً سببه نقص <bdi>surfactant</bdi> بالخدج"),
        ("diabetic mother", "عامل خطر معروف لكل من <bdi>TTN</bdi> و<bdi>RDS</bdi>، بس مو كافي لوحده للتشخيص"),
        ("mild tachypnea", "عرض خفيف وفحص طبيعي، يناسب حالة <bdi>self-limiting</bdi> مثل <bdi>TTN</bdi>"),
    ],
    "why_correct": [
        "<bdi>term baby</bdi> وزنه طبيعي (3800g) وعنده بس <bdi>mild tachypnea</bdi> مع فحص طبيعي، يعني <bdi>transient tachypnea of the newborn (TTN)</bdi>.",
        "سبب <bdi>TTN</bdi> تأخر امتصاص سوائل الرئة الجنينية، و<bdi>maternal diabetes</bdi> والولادة <bdi>cesarean</bdi> من عوامل الخطر المعروفة له.",
        "الحالة <bdi>benign</bdi> ومؤقتة وتتحسن خلال الأيام الأولى بـ<bdi>supportive care</bdi> فقط.",
    ],
    "when_changes": [
        "لو كان الطفل <bdi>preterm</bdi> ومع <bdi>progressive distress</bdi> و<bdi>grunting</bdi>، الجواب يصير <bdi>respiratory distress syndrome (RDS)</bdi>.",
        "لو كان فيه <bdi>meconium stained liquor</bdi> وولادة بعد الميعاد، فكر بـ<bdi>meconium aspiration</bdi> بدل <bdi>TTN</bdi>.",
    ],
    "rule": "<bdi>term baby</bdi> + <bdi>mild tachypnea</bdi> = <bdi>TTN</bdi>؛ ما نفكر بـ<bdi>RDS</bdi> إلا لو الطفل <bdi>preterm</bdi> ومع صورة <bdi>ground glass</bdi>.",
    "comparison": None,
    "labs": [["Weight", "3800 g", "term-appropriate weight"]],
    "guideline_note": None,
},
"AS-1085": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "سؤال يبي خطوة <bdi>management</bdi> الأولى عند رضيع عنده <bdi>bronchiolitis</bdi> مع <bdi>hypoxia</bdi> خفيف وسوء <bdi>feeding</bdi>، قبل التصعيد لـ<bdi>HFNC</bdi>.",
    "clues": [
        ("3 month", "عمر نموذجي لـ<bdi>bronchiolitis</bdi>"),
        ("O2 89%", "<bdi>hypoxia</bdi> يستدعي <bdi>admission</bdi> وأكسجين، لكن ما يقول إن الخطوة الأولى فشلت"),
    ],
    "why_correct": [
        "علاج <bdi>bronchiolitis</bdi> أساسه <bdi>supportive care</bdi>، والتصعيد يكون تدريجي.",
        "هذا الرضيع عنده <bdi>SpO2 89%</bdi> وسوء <bdi>feeding</bdi>، فيحتاج <bdi>admission</bdi> مع <bdi>low flow oxygen</bdi> أولًا، دعم للتغذية/الترطيب، و<bdi>nasal suctioning</bdi> لتنظيف الإفرازات.",
        "نبدأ بأقل تدخل يصحح <bdi>hypoxia</bdi>، ونصعّد فقط لو ما تحسن.",
    ],
    "when_changes": [
        "لو استمر يسقط <bdi>SpO2</bdi> أو ازداد <bdi>work of breathing</bdi> رغم <bdi>low flow oxygen</bdi>، الجواب يصير <bdi>high flow nasal cannula (HFNC)</bdi>.",
        "لو ما قدر يتحمل <bdi>feeding</bdi> عن طريق الفم أو الأنبوب الأنفي، نضيف <bdi>IV fluids</bdi>.",
    ],
    "rule": "علاج <bdi>bronchiolitis</bdi> خطوة بخطوة: ابدأ بـ<bdi>low flow O2</bdi> ودعم التغذية، وصعّد لـ<bdi>HFNC</bdi> فقط لو السؤال يذكر فشل الخطوة الأولى.",
    "comparison": None,
    "labs": [["SpO2", "89%", "≥95% (room air)"]],
    "guideline_note": None,
},
"AS-1092": {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "المصدر ما حسم الجواب، لكن الصورة (<bdi>skip lesions</bdi> + <bdi>terminal ileum</bdi> + <bdi>chronic diarrhea</bdi>) تطابق <bdi>pediatric Crohn's disease</bdi>، والسؤال يبي خطوة <bdi>induction</bdi> الأولى.",
    "clues": [
        ("chronic diarrhea", "عرض مزمن يوجه لـ<bdi>inflammatory bowel disease</bdi>"),
        ("skip lesions", "علامة مميزة لـ<bdi>Crohn's disease</bdi> (مو <bdi>ulcerative colitis</bdi>)"),
        ("terminal ileum", "موقع كلاسيكي لإصابة <bdi>Crohn's disease</bdi>"),
    ],
    "why_correct": [
        "الصورة (<bdi>skip lesions</bdi> + إصابة <bdi>terminal ileum</bdi> + <bdi>chronic diarrhea</bdi>) تشخيصها <bdi>Crohn's disease</bdi> عند طفل.",
        "خط <bdi>induction</bdi> الأول عند الأطفال بمرض <bdi>luminal Crohn's</bdi> هو <bdi>exclusive enteral nutrition</bdi> (تغذية علاجية كاملة)، وهو أفضل من <bdi>steroids</bdi> من ناحية الآثار الجانبية والنمو.",
        "<bdi>systemic steroids</bdi> بديل مقبول للـ<bdi>induction</bdi> بس مو الخيار الأول عند الأطفال، و<bdi>MTX</bdi> دوره بـ<bdi>maintenance</bdi> مو البداية.",
    ],
    "when_changes": [
        "لو السؤال يبي علاج <bdi>maintenance</bdi> بعد الاستقرار، الجواب يصير <bdi>thiopurines</bdi> أو <bdi>methotrexate</bdi>.",
        "لو المرض شديد أو عالي الخطورة، الجواب يصير <bdi>anti-TNF</bdi> مثل <bdi>infliximab</bdi>.",
    ],
    "rule": "عند طفل تشخيصه <bdi>Crohn's disease</bdi> جديد، «وش نعطي» غالبًا يعني <bdi>induction</bdi>، و<bdi>exclusive enteral nutrition</bdi> أفضل من <bdi>steroids</bdi> فيه.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1101": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "سؤال نصيحة وقائية لأهل طفل عنده <bdi>cystic fibrosis</bdi> يتكرر عنده <bdi>URTI</bdi> رغم العلاج الفيزيائي.",
    "clues": [
        ("cystic fibrosis", "<bdi>chronic lung disease</bdi> يحتاج عناية خاصة من العدوى"),
        ("recurrent URTI 6-7 cold / year", "عدوى فيروسية متكررة، والحل وقائي مو عزل أو مضاد حيوي"),
    ],
    "why_correct": [
        "أطفال <bdi>cystic fibrosis</bdi> لازم ياخذون <bdi>annual influenza vaccine</bdi> مع التطعيمات الروتينية، لأن <bdi>influenza</bdi> يسبب <bdi>pulmonary exacerbations</bdi> وعدوى بكتيرية ثانوية.",
        "الأم قلقانة من عدوى <bdi>school</bdi>، والخطوة الوقائية الناقصة هنا هي <bdi>vaccination</bdi>، بدون ما نقيّد حياة الطفل الاجتماعية.",
        "هذا الحل يحافظ على <bdi>normal school and activity</bdi> ويقلل خطر <bdi>exacerbation</bdi> بنفس الوقت.",
    ],
    "when_changes": [
        "لو السؤال عن منع <bdi>cross infection</bdi> بين مرضى <bdi>CF</bdi> أنفسهم، الجواب يصير تجنب التقارب مع مرضى <bdi>CF</bdi> آخرين.",
        "لو فيه علامات <bdi>bacterial exacerbation</bdi> فعلية، الجواب يصير <bdi>antibiotics</bdi> موجهة، مو وقائية.",
    ],
    "rule": "عدوى فيروسية متكررة عند طفل <bdi>chronic lung disease</bdi>: الجواب <bdi>vaccination</bdi>، مو عزل اجتماعي ولا <bdi>prophylactic antibiotics</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1109": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال يفرق أسباب <bdi>congenital stridor</bdi> بالاعتماد على تأثير وضعية النوم (<bdi>prone</bdi> مقابل <bdi>supine</bdi>).",
    "clues": [
        ("noisy breath since birth", "<bdi>congenital stridor</bdi> منذ الولادة يوجه لـ<bdi>laryngomalacia</bdi> غالبًا"),
        ("disappear in prone position", "علامة مميزة لـ<bdi>laryngomalacia</bdi>"),
        ("more obvious with supine position", "يعاكس <bdi>tracheomalacia</bdi> اللي يتحسن بالعكس"),
    ],
    "why_correct": [
        "<bdi>noisy breathing</bdi> منذ الولادة يختفي بوضعية <bdi>prone</bdi> ويزيد بـ<bdi>supine</bdi>، مع فحص ونمو طبيعيين، هذا <bdi>laryngomalacia</bdi>.",
        "السبب انهيار نسيج <bdi>supraglottic</bdi> الرخو للداخل أثناء الشهيق، ويزيد سوء بوضعية الاستلقاء على الظهر وبالبكاء أو الرضاعة.",
        "هو أشيع سبب لـ<bdi>congenital stridor</bdi>، وغالبًا يتحسن لوحده بعمر 1-2 سنة.",
    ],
    "when_changes": [
        "لو تحسن بوضعية <bdi>supine</bdi> بدل <bdi>prone</bdi>، الجواب يصير <bdi>tracheomalacia</bdi>.",
        "لو فيه علامات خطر مثل سوء نمو أو <bdi>apnea</bdi> أو زرقة، نحتاج تقييم إضافي (<bdi>laryngoscopy</bdi>) مو بس طمأنة.",
    ],
    "rule": "يتحسن بـ<bdi>prone</bdi> = <bdi>laryngomalacia</bdi>؛ يتحسن بـ<bdi>supine</bdi> = <bdi>tracheomalacia</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1114": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال عن العلامة التحذيرية اللي لازم الأهل ينتبهون لها بعد علاج <bdi>Kawasaki disease</bdi>، مرتبطة بمضاعفات <bdi>aspirin</bdi> أو المرض نفسه.",
    "clues": [
        ("Kawasaki disease", "مرض وعائي يُعالج غالبًا بـ<bdi>aspirin</bdi> و<bdi>IVIG</bdi>"),
        ("warning signs that require urgent medical attention", "نبي عرض خطير مرتبط فعليًا بالعلاج أو المرض، مو عرض حميد"),
    ],
    "why_correct": [
        "بعد علاج <bdi>Kawasaki disease</bdi> الطفل على <bdi>aspirin</bdi>، اللي ممكن يسبب تآكل بالمعدة ونزيف هضمي، وأحيانًا الالتهاب الوعائي نفسه يصيب الأوعية المساريقية.",
        "<bdi>severe abdominal pain</bdi> مع <bdi>blood in stool</bdi> علامة تحذيرية حقيقية تحتاج مراجعة عاجلة.",
        "باقي الخيارات أعراض حميدة أو ما لها علاقة بمضاعفات <bdi>Kawasaki</bdi> أو <bdi>aspirin</bdi>.",
    ],
    "when_changes": [
        "لو السؤال عن علامة مضاعفة قلبية، الجواب يصير ألم صدر أو ضيق تنفس أو إغماء (تلميح لـ<bdi>coronary</bdi> involvement).",
        "لو السؤال عن <bdi>Reye syndrome</bdi>، الخطر يرتفع مع <bdi>aspirin</bdi> + عدوى <bdi>influenza</bdi> أو <bdi>varicella</bdi>.",
    ],
    "rule": "بعد <bdi>Kawasaki</bdi>، العلامة التحذيرية الحقيقية ترتبط بنزيف (<bdi>aspirin</bdi>) أو مشكلة قلبية، مو الأعراض الحميدة مثل الاحمرار أو ألم المفاصل الخفيف.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1124": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال عن أفضل فحص يدعم تشخيص <bdi>abdominal mass</bdi> عند رضيع، بناءً على وجود <bdi>calcification</bdi>.",
    "clues": [
        ("14 months old", "عمر نموذجي لـ<bdi>neuroblastoma</bdi>"),
        ("large abdominal mass without pain", "كتلة بدون ألم، يحتاج تمييز بين عدة أورام بطنية عند الأطفال"),
        ("X-ray showing calcification", "علامة مميزة لـ<bdi>neuroblastoma</bdi> أكثر من <bdi>Wilms tumor</bdi>"),
    ],
    "why_correct": [
        "رضيع عمره 14 شهر عنده <bdi>abdominal mass</bdi> كبيرة مع <bdi>calcification</bdi> بالأشعة، هذا يوجه بقوة لـ<bdi>neuroblastoma</bdi> (ينشأ من نسيج <bdi>adrenal</bdi> أو <bdi>sympathetic neural crest</bdi>).",
        "هذا الورم يفرز <bdi>catecholamines</bdi>، فارتفاع <bdi>urinary metabolites (VMA, HVA)</bdi> يدعم التشخيص.",
        "التأكيد النهائي يحتاج تصوير و<bdi>biopsy</bdi>، لكن الفحص اللي «يقترح» التشخيص هو <bdi>urine catecholamine metabolites</bdi>.",
    ],
    "when_changes": [
        "لو الكتلة بدون <bdi>calcification</bdi> عند طفل أكبر وبصحة جيدة، فكر بـ<bdi>Wilms tumor</bdi> وتحري <bdi>renal function</bdi> و<bdi>hematuria</bdi>.",
        "لو فيه <bdi>hepatomegaly</bdi> مع كتلة كبدية، الفحص المناسب يصير <bdi>alpha fetoprotein</bdi> (<bdi>hepatoblastoma</bdi>).",
    ],
    "rule": "كتلة بطنية + <bdi>calcification</bdi> عند رضيع = <bdi>neuroblastoma</bdi>، والفحص الداعم <bdi>urine catecholamine metabolites</bdi>.",
    "comparison": {
        "headers": ["الورم", "الصورة", "الفحص الداعم"],
        "rows": [
            ["<bdi>Neuroblastoma</bdi>", "طفل أصغر، يعبر خط الوسط، <bdi>calcification</bdi>", "<bdi>urine VMA/HVA</bdi>"],
            ["<bdi>Wilms tumor</bdi>", "طفل بصحة جيدة، كتلة ناعمة بجهة واحدة", "<bdi>renal function</bdi>، لا يوجد <bdi>calcification</bdi> عادة"],
            ["<bdi>Hepatoblastoma</bdi>", "كتلة كبدية", "<bdi>alpha fetoprotein</bdi>"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},
"AS-1137": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال عن نصيحة <bdi>management</bdi> لمراهق عنده <bdi>prolonged QT</bdi> مع <bdi>echo</bdi> طبيعي وتاريخ عائلي لموت مفاجئ.",
    "clues": [
        ("family hx of sudden death", "يرفع احتمال سبب وراثي للقلب مثل <bdi>long QT syndrome</bdi>"),
        ("Q T prolongation", "علامة مباشرة لـ<bdi>long QT syndrome</bdi>"),
    ],
    "why_correct": [
        "مراهق عنده <bdi>prolonged QT</bdi> بال<bdi>ECG</bdi> و<bdi>echo</bdi> طبيعي وتاريخ عائلي لموت مفاجئ، هذا <bdi>congenital long QT syndrome</bdi> على الأغلب، و<bdi>echo</bdi> الطبيعي يستبعد سبب هيكلي مثل <bdi>hypertrophic cardiomyopathy</bdi>.",
        "العلاج الأساسي <bdi>beta blockers</bdi> لتقليل خطر اضطراب النظم، مع تقييد <bdi>strenuous</bdi> أو الرياضة التنافسية (السباحة خصوصًا بنوع 1 معروف كمحفز).",
        "ترك المراهق بدون علاج (الخيار A) يهمل خطر حقيقي بموت مفاجئ.",
    ],
    "when_changes": [
        "لو <bdi>echo</bdi> أظهر <bdi>LVH</bdi>، الجواب يتجه لـ<bdi>hypertrophic cardiomyopathy</bdi> مو <bdi>long QT syndrome</bdi>.",
        "لو استمرت أحداث اضطراب نظم خطيرة رغم <bdi>beta blocker</bdi>، الخطوة التالية <bdi>ICD</bdi>.",
    ],
    "rule": "تاريخ عائلي لموت مفاجئ + <bdi>QT</bdi> طويل + <bdi>echo</bdi> طبيعي = <bdi>long QT syndrome</bdi>: <bdi>beta blocker</bdi> وتقييد الرياضة الشديدة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1140": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال يفرق بين أسباب غياب الخصية من كيس الصفن عند رضيع بالاعتماد على إمكانية إرجاعها للصفن بسهولة.",
    "clues": [
        ("easily moved to scrotum", "العلامة الحاسمة: الخصية ترجع للصفن بسهولة بدون شد، يعني هبوط مكتمل"),
    ],
    "why_correct": [
        "العلامة الحاسمة هنا إن الخصية بقناة <bdi>inguinal canal</bdi> لكن <bdi>easily moved to scrotum</bdi>، وهذا تعريف <bdi>retractile testis</bdi>.",
        "الخصية <bdi>retractile</bdi> أكملت هبوطها الطبيعي لكن يسحبها منعكس <bdi>cremasteric reflex</bdi> النشط للأعلى، وترجع للصفن بدون شد.",
        "يحتاج فقط متابعة لأن بعضها يرتفع لاحقًا، وما يحتاج تدخل جراحي.",
    ],
    "when_changes": [
        "لو الخصية ما ترجع للصفن أو ترجع فورًا للأعلى، الجواب يصير <bdi>undescended testis</bdi> ويحتاج <bdi>orchidopexy</bdi>.",
        "لو الخصية خارج مسار الهبوط الطبيعي (مثل منطقة <bdi>perineum</bdi>)، الجواب يصير <bdi>ectopic testis</bdi>.",
    ],
    "rule": "لو الخصية ترجع للصفن بسهولة وتبقى = <bdi>retractile testis</bdi> (ملاحظة فقط)؛ لو ما ترجع أو تنط فورًا = <bdi>undescended testis</bdi> (علاج جراحي).",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
}

WHY_WRONG = {
"AS-1078": {
    "A": "<bdi>FFP</bdi> يعوض عوامل التجلط، وهي طبيعية هنا (<bdi>PT/PTT</bdi> طبيعي)، و<bdi>corticosteroids</bdi> لحالها بطيئة لرضيع ينزف وصفائحه منخفضة؛ <bdi>FFP</bdi> مناسب لنقص عوامل تجلط مع <bdi>PT/PTT</bdi> طويلة مثل <bdi>DIC</bdi> أو مرض كبدي.",
},
"AS-1080": {
    "A": "«<bdi>respiratory distress symptoms</bdi>» مجرد وصف للأعراض مو تشخيص؛ ولو قصدها <bdi>RDS</bdi> الحقيقي، فهذا مرض <bdi>preterm</bdi> بنقص <bdi>surfactant</bdi> مع تدهور تدريجي وصورة <bdi>ground glass</bdi>، بينما هذا طفل <bdi>term</bdi> بأعراض خفيفة.",
},
"AS-1085": {
    "B": "<bdi>HFNC</bdi> تصعيد يُستخدم لو استمر انخفاض الأكسجين أو زاد <bdi>work of breathing</bdi> رغم <bdi>low flow oxygen</bdi>، و<bdi>IV fluids</bdi> فقط لو ما قدر ياخذ تغذية بالفم أو الأنبوب؛ ما فيه بالسؤال إشارة إن الخطوة الأولى فشلت.",
},
"AS-1092": {
    "B": "<bdi>systemic steroids</bdi> بديل مقبول لـ<bdi>induction</bdi> لكن مو الخط الأول عند الأطفال بسبب آثاره على النمو؛ الأفضلية لـ<bdi>exclusive enteral nutrition</bdi>.",
    "C": "<bdi>MTX</bdi> دوره بمرحلة <bdi>maintenance</bdi>، مو كخطوة أولى عند التشخيص.",
},
"AS-1101": {
    "B": "<bdi>airway clearance</bdi> أصلاً يُطبق، وما يمنع نزلات البرد الفيروسية؛ زيادة تكراره تكون وقت <bdi>exacerbation</bdi> مو كوقاية من عدوى المدرسة.",
    "C": "تجنب الأنشطة الجماعية والمدرسة يعزل الطفل وغير موصى به؛ النصيحة الصحيحة تجنب قرب مرضى <bdi>CF</bdi> الآخرين (خطر العدوى المتبادلة)، مو الأصدقاء الأصحاء.",
    "D": "نزلات البرد فيروسية، فالمضاد الحيوي ما يمنعها ويزيد خطر المقاومة؛ المضاد الحيوي يُعطى لـ<bdi>bacterial exacerbation</bdi> محددة، مو لتكرار 6-7 نزلات سنويًا.",
},
"AS-1109": {
    "A": "<bdi>choanal atresia</bdi> يظهر بالولادة بزرقة تتحسن بالبكاء وصعوبة إدخال قسطرة أنفية، مو ضجيج تنفسي يتغير بالوضعية عند طفل بصحة جيدة.",
    "C": "<bdi>subglottic stenosis</bdi> (غالبًا بعد تنبيب) يعطي <bdi>stridor</bdi> ثنائي الطور لا يتغير بالوضعية ويميل للاستمرار أو التفاقم.",
    "D": "<bdi>vocal cord paralysis</bdi> يعطي <bdi>stridor</bdi> مع بكاء ضعيف أو أجش ومشاكل رضاعة أو استنشاق، غالبًا بعد إصابة ولادية أو جراحة قلب، وبدون تغير بالوضعية.",
},
"AS-1114": {
    "A": "الاحمرار المتقطع بالوجه عرض حميد ما له علاقة بمضاعفات <bdi>Kawasaki</bdi> أو <bdi>aspirin</bdi>.",
    "C": "الطفح الجلدي الملموس بالأطراف علامة كلاسيكية لـ<bdi>Henoch-Schönlein purpura</bdi>، وهو التهاب وعائي مختلف، مو علامة تحذير لـ<bdi>Kawasaki</bdi>.",
    "D": "ألم المفاصل الخفيف اللي يتحسن بالراحة ممكن يصير أثناء <bdi>Kawasaki disease</bdi> نفسه وهو <bdi>self-limiting</bdi>، مو حالة طارئة.",
},
"AS-1124": {
    "A": "فحوصات وظائف الكبد غير محددة؛ ورم كبدي (<bdi>hepatoblastoma</bdi>) يُقترح بارتفاع <bdi>alpha fetoprotein</bdi> مو بـ<bdi>LFT</bdi>.",
    "B": "وظائف الكلى تُفحص بـ<bdi>Wilms tumor</bdi> لكنها غالبًا طبيعية وما تقترح التشخيص؛ <bdi>Wilms</bdi> عادة بدون <bdi>calcification</bdi> وعند طفل بصحة جيدة.",
    "C": "<bdi>alpha fetoprotein</bdi> هو مؤشر <bdi>hepatoblastoma</bdi> (وأورام الخلايا الجرثومية)، وليس مرتفعًا بـ<bdi>neuroblastoma</bdi>.",
},
"AS-1137": {
    "A": "تشجيع النشاط البدني الحر مع متابعة <bdi>ECG</bdi> سنوية فقط يترك مريض عالي الخطورة بدون علاج؛ المراقبة لوحدها غير مقبولة مع <bdi>QT</bdi> طويل وتاريخ عائلي لموت مفاجئ.",
},
"AS-1140": {
    "A": "الخصية <bdi>ectopic</bdi> تكون خارج مسار الهبوط الطبيعي (منطقة <bdi>perineum</bdi> أو <bdi>femoral</bdi> أو فوق العانة)، مو داخل <bdi>inguinal canal</bdi>.",
    "B": "الخصية <bdi>undescended</bdi> متوقفة على طول مسار الهبوط ولا يمكن إرجاعها للصفن أو ترجع فورًا للأعلى؛ الحالات الملموسة تحتاج <bdi>orchidopexy</bdi>.",
    "C": "<bdi>testicular torsion</bdi> حالة طارئة مؤلمة مع خصية مرتفعة ومؤلمة وغياب <bdi>cremasteric reflex</bdi>، مو موجود بالصدفة بزيارة روتينية.",
},
}

HIGHLIGHT_TERMS = {
"AS-1078": ["neonate", "mother has a history of systemic lupus erythematosus (SLE)", "thrombocytopenia with normal PT and PTT"],
"AS-1080": ["newborn term", "diabetic mother", "mild tachypnea"],
"AS-1085": ["3 month", "bronchiolitis", "O2 89%"],
"AS-1092": ["chronic diarrhea", "skip lesions", "terminal ileum"],
"AS-1101": ["cystic fibrosis", "recurrent URTI 6-7 cold / year"],
"AS-1109": ["noisy breath since birth", "disappear in prone position", "more obvious with supine position"],
"AS-1114": ["Kawasaki disease", "warning signs that require urgent medical attention"],
"AS-1124": ["14 months old", "large abdominal mass without pain", "X-ray showing calcification"],
"AS-1137": ["family hx of sudden death", "Q T prolongation"],
"AS-1140": ["easily moved to scrotum"],
}
