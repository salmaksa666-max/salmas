# -*- coding: utf-8 -*-
# Explanations for questions 693-789

TOPICS = {
693: "Endocrinology", 694: "Endocrinology", 695: "Endocrinology", 696: "Endocrinology",
697: "Endocrinology", 698: "Nephrology", 699: "Nephrology", 700: "Nephrology",
701: "Nephrology", 702: "Nephrology", 703: "Endocrinology", 704: "Nephrology",
705: "Nephrology", 706: "Nephrology", 707: "Nephrology", 708: "Nephrology",
709: "Nephrology", 710: "Nephrology", 711: "Nephrology", 712: "Nephrology",
713: "Nephrology", 714: "Nephrology", 715: "Nephrology", 716: "Nephrology",
717: "Nephrology", 718: "Nephrology", 719: "Nephrology", 720: "Nephrology",
721: "Nephrology", 722: "Nephrology", 723: "Nephrology", 724: "Nephrology",
725: "Nephrology", 726: "Nephrology", 727: "Nephrology", 728: "Nephrology",
729: "Nephrology", 730: "Nephrology", 731: "Nephrology", 732: "Nephrology",
733: "Neurology", 734: "Neurology", 735: "Neurology", 736: "Neurology",
737: "Neurology", 738: "Neurology", 739: "Neurology", 740: "Neurology",
741: "Neurology", 742: "Neurology", 743: "Neurology", 744: "Neurology",
745: "Neurology", 746: "Neurology", 747: "Neurology", 748: "Neurology",
749: "Neurology", 750: "Neurology", 751: "Neurology", 752: "Neurology",
753: "Neurology", 754: "Neurology", 755: "Neurology", 756: "Neurology",
757: "Preventive & Community Medicine", 758: "Preventive & Community Medicine",
759: "Neurology", 760: "Neurology", 761: "ENT", 762: "Neurology", 763: "Neurology",
764: "Neurology", 765: "Neurology", 766: "Neurology", 767: "Neurology",
768: "Neurology", 769: "Neurology", 770: "Neurology", 771: "Neurology",
772: "Neurology", 773: "Neurology",
774: "Preventive & Community Medicine", 775: "Preventive & Community Medicine",
776: "Preventive & Community Medicine", 777: "Preventive & Community Medicine",
778: "Preventive & Community Medicine", 779: "Preventive & Community Medicine",
780: "Preventive & Community Medicine", 781: "Preventive & Community Medicine",
782: "Preventive & Community Medicine", 783: "Preventive & Community Medicine",
784: "Preventive & Community Medicine", 785: "Preventive & Community Medicine",
786: "Preventive & Community Medicine", 787: "Preventive & Community Medicine",
788: "Preventive & Community Medicine", 789: "Preventive & Community Medicine",
}

EXPLANATIONS = {
693: {
    "idea": "الرجل عنده <bdi>symptoms</bdi> نقص هرمون الذكورة (ضعف رغبة وطاقة)، والتحاليل تبين قصور بكل محاور الغدة النخامية (تناسلي ودرقي) مع وجود ورم نخامي 2.5 سم، فالسؤال يبي الـ<bdi>diagnosis</bdi> الأدق.",
    "clues": [
        ("reduced libido", "<bdi>symptom</bdi> ناتج عن نقص التستوستيرون"),
        ("FSH 2.5, LH 1.3, Testosterone 8.0", "قيم <bdi>low</bdi> كلها معًا، يعني قصور مركزي (نخامي) مو قصور خصية أولي"),
        ("TSH 0.3, T4 7.5", "TSH <bdi>low</bdi> مع T4 <bdi>low</bdi>، يدل على قصور درقية مركزي مو أولي"),
        ("Prolactin 450", "<bdi>normal</bdi> (أقل من 652)، يبعد ورم الـ<bdi>prolactin</bdi> الكبير"),
        ("2.5 cm pituitary adenoma", "كتلة نخامية كبيرة تضغط على باقي أنسجة الغدة"),
    ],
    "why_correct": [
        "انخفاض <bdi>FSH/LH</bdi> مع انخفاض <bdi>testosterone</bdi> معًا يدل على قصور تناسلي مركزي (من النخامية) مو مشكلة بالخصية نفسها.",
        "نفس الفكرة تنطبق على الدرقية: <bdi>TSH</bdi> <bdi>low</bdi> مع <bdi>T4</bdi> <bdi>low</bdi> يعني قصور درقي مركزي، وهذا نمط كلاسيكي لضغط ورم نخامي كبير على باقي الخلايا الـ<bdi>normal</bdi>.",
        "الـ<bdi>prolactin</bdi> <bdi>normal</bdi> فعليًا، فلو كان الورم يفرز <bdi>prolactin</bdi> لكان <bdi>elevated</bdi> جدًا، فهذا يستبعد <bdi>macroprolactinoma</bdi> ويدعم إنه ورم غير مفرز يضغط بس.",
    ],
    "when_changes": [
        "لو الـ<bdi>prolactin</bdi> كان <bdi>elevated</bdi> جدًا (بالآلاف)، يصير الـ<bdi>diagnosis</bdi> <bdi>macroprolactinoma</bdi> بدل الورم غير المفرز.",
        "لو TSH كان <bdi>elevated</bdi> مع T4 <bdi>low</bdi>، يصير الـ<bdi>diagnosis</bdi> قصور درقية أولي مو مركزي.",
    ],
    "rule": "وجود قصور بأكثر من محور هرموني نخامي مع كتلة كبيرة و<bdi>prolactin</bdi> <bdi>normal</bdi> يدل على ورم نخامي غير مفرز يضغط على الغدة.",
    "comparison": {
        "headers": ["التحليل", "القيمة", "الدلالة"],
        "rows": [
            ["<bdi>TSH / T4</bdi>", "<bdi>low</bdi> / <bdi>low</bdi>", "قصور درقي مركزي"],
            ["<bdi>FSH, LH, Testosterone</bdi>", "<bdi>low</bdi> كلها", "قصور تناسلي مركزي"],
            ["<bdi>Prolactin</bdi>", "<bdi>normal</bdi> (450)", "يبعد ورم <bdi>prolactin</bdi> مفرز"],
        ],
    },
    "guideline_note": None,
},
694: {
    "idea": "الـ<bdi>patient</bdi> الشاب عنده <bdi>signs</bdi> كلاسيكية لمتلازمة <bdi>Cushing</bdi> (سمنة مركزية وخطوط أرجوانية)، والتحاليل تأكد ارتفاع الكورتيزول مع ارتفاع ACTH، فالسؤال يبي الـ<bdi>step</bdi> التالية لتحديد مصدر الزيادة.",
    "clues": [
        ("central adiposity", "سمنة مركزية، من <bdi>signs</bdi> Cushing"),
        ("purple striae", "خطوط أرجوانية، <bdi>sign</bdi> مميزة لـ Cushing"),
        ("ACTH 20", "<bdi>elevated</bdi> عن الـ<bdi>normal</bdi>، يدل على زيادة معتمدة على ACTH"),
        ("Cortisol 8 a.m. 600 / 4 p.m. 550", "فقدان التذبذب اليومي الـ<bdi>normal</bdi> للكورتيزول، يؤكد فرط الإفراز"),
    ],
    "why_correct": [
        "ارتفاع الكورتيزول مع ارتفاع ACTH يعني الزيادة معتمدة على ACTH، والـ<bdi>cause</bdi> الأشيع بكثير هو ورم نخامي صغير يفرز ACTH.",
        "الـ<bdi>step</bdi> التالية المنطقية هي تصوير الغدة النخامية بـ <bdi>MRI</bdi> للبحث عن الورم قبل أي فحص أكثر تعقيدًا.",
        "فحوصات مثل أخذ عينات الجيب الصخري (<bdi>IPSS</bdi>) أو تصوير الصدر والبطن تُحجز لو الـMRI طلع سلبي أو غير واضح.",
    ],
    "when_changes": [
        "لو الـMRI طلع سلبي أو مو متوافق مع الصورة السريرية، الـ<bdi>step</bdi> التالية تصير أخذ عينات الجيب الصخري لتمييز المصدر النخامي عن المصدر خارج النخامية.",
        "لو الشك بمصدر خارج النخامية (زي ورم رئة يفرز ACTH)، يصير التصوير بالصدر والبطن هو المطلوب.",
    ],
    "rule": "بفرط الكورتيزول المعتمد على ACTH، أول <bdi>step</bdi> تصوير هي MRI الغدة النخامية لأنها الـ<bdi>cause</bdi> الأشيع.",
    "comparison": None,
    "guideline_note": None,
},
695: {
    "idea": "شاب عنده كسر هش غير متوقع بعمره، ومعه <bdi>signs</bdi> نقص هرمون ذكورة (شعر <bdi>mild</bdi> بالوجه والإبط)، فالسؤال يبي الفحص اللي يكشف <bdi>cause</bdi> ضعف العظم.",
    "clues": [
        ("fragility fracture", "كسر بدون إصابة كبيرة، يدل على ضعف عظم غير متوقع بهالعمر"),
        ("sparse facial and axillary hair growth", "<bdi>sign</bdi> نقص التستوستيرون (قصور الغدد التناسلية)"),
        ("BMI 23", "وزن <bdi>normal</bdi>، يبعد <bdi>causes</bdi> مرتبطة بالسمنة أو سوء التغذية"),
    ],
    "why_correct": [
        "نقص شعر الوجه والإبط <bdi>sign</bdi> واضحة على نقص التستوستيرون، وهذا <bdi>cause</bdi> معروف ومهم ل<bdi>osteoporosis</bdi> عند الرجال الشباب.",
        "فحص <bdi>testosterone and gonadotrophin levels</bdi> يحدد إذا كان القصور تناسلي هو الـ<bdi>cause</bdi> وراء ضعف العظم، وهذا يوجه الـ<bdi>treatment</bdi> المناسب.",
        "لازم نبحث عن الـ<bdi>cause</bdi> (etiology) مو بس شدة الكسر، وهذا الفحص يستهدف الـ<bdi>cause</bdi> المشتبه به من الفحص السريري مباشرة.",
    ],
    "when_changes": [
        "لو ما فيه <bdi>signs</bdi> نقص هرمون ذكورة والـ<bdi>patient</bdi> طويل القامة بشكل غير متناسب، يصير التفكير بزيادة <bdi>IGF1</bdi> أو <bdi>causes</bdi> ثانية.",
        "لو الهدف قياس شدة <bdi>osteoporosis</bdi> مو الـ<bdi>cause</bdi>، يصير فحص <bdi>DEXA</bdi> هو المطلوب.",
    ],
    "rule": "أي كسر هش بشاب لازم نفتش عن <bdi>cause</bdi> ثانوي، و<bdi>signs</bdi> نقص هرمون الذكورة توجهنا لفحص التستوستيرون والهرمونات المنشطة له.",
    "comparison": None,
    "guideline_note": None,
},
696: {
    "idea": "ورم كظري صغير اكتُشف صدفة، شكله حميد وضغط الـ<bdi>patient</bdi> <bdi>normal</bdi>، لكن قاعدة أورام الكظر العرضية تفرض فحص وظيفي دايمًا قبل أي قرار، حتى لو ما فيه <bdi>symptoms</bdi>.",
    "clues": [
        ("incidentally detected", "اكتُشف صدفة، مو ب<bdi>cause</bdi> <bdi>symptoms</bdi> هرمونية"),
        ("benign 2.0-cm right adrenal adenoma", "حجم صغير وشكل حميد بالتصوير"),
        ("Blood pressure 130/70 mmHg", "ضغط <bdi>normal</bdi>، لكن هذا لا ينفي وجود ورم مفرز للكاتيكولامينات"),
    ],
    "why_correct": [
        "أي كتلة كظرية تُكتشف صدفة لازم تُفحص وظيفيًا بغض النظر عن الـ<bdi>symptoms</bdi>، لأن بعض الأورام المفرزة (زي الفيوكروموسيتوما) ممكن تكون صامتة سريريًا.",
        "اختبار قمع الديكساميثازون الليلي يكشف فرط الكورتيزول تحت السريري، والميتانفرين البولي يكشف الفيوكروموسيتوما.",
        "لو الورم غير وظيفي وصغير الحجم بشكل حميد، الـ<bdi>procedure</bdi> التالي مراقبة مو جراحة فورية.",
    ],
    "when_changes": [
        "لو الفحص الوظيفي طلع إيجابي لفرط كورتيزول أو كاتيكولامينات، تصير الـ<bdi>step</bdi> التالية تحضير الـ<bdi>patient</bdi> للجراحة.",
        "لو حجم الكتلة أكبر من 4 سم أو فيها ملامح مشبوهة، تصير الإحالة الجراحية أقرب بغض النظر عن الوظيفة الهرمونية.",
    ],
    "rule": "كل كتلة كظرية عرضية تحتاج فحص وظيفي (كورتيزول وكاتيكولامينات) قبل أي قرار، حتى لو ما فيه <bdi>symptoms</bdi> أو الضغط <bdi>normal</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
697: {
    "idea": "كتلة كظرية كبيرة بملامح مشبوهة (حدود غير منتظمة، كثافة عالية، تصريف صبغة ضعيف) والخطة جراحة استئصال، والسؤال يبي الفحص الضروري قبل أي عملية على الكظر.",
    "clues": [
        ("5.5-cm left adrenal mass with irregular borders", "حجم كبير وحدود غير منتظمة، ملامح مشبوهة بالخباثة"),
        ("density of > 10 HU", "كثافة عالية، غير متوافقة مع ورم حميد بسيط"),
        ("&lt;30% contrast wash out at 15 minutes", "تصريف صبغة بطيء، يدعم الشك بالخباثة"),
        ("elective adrenalectomy", "خطة جراحة مخطط لها، مو طارئة"),
    ],
    "why_correct": [
        "أي <bdi>patient</bdi> رايح لعملية على الكظر لازم يُستبعد عنده <bdi>pheochromocytoma</bdi> أولًا مهما كانت شكل الكتلة أو الـ<bdi>symptoms</bdi>، لأن التخدير والتلاعب الجراحي ممكن يسبب أزمة ضغط قاتلة لو الورم يفرز كاتيكولامينات بدون علم.",
        "تحليل <bdi>24-hour urinary fractionated metanephrines</bdi> هو الفحص المعياري لاستبعاد الفيوكروموسيتوما قبل الجراحة.",
        "هذا الفحص لازم يسبق أي <bdi>procedure</bdi> جراحي على الكظر بغض النظر عن ملامح التصوير المشبوهة بالخباثة.",
    ],
    "when_changes": [
        "لو طلع الفحص إيجابي، لازم يبدأ <bdi>block</bdi> ألفا قبل الجراحة لمنع أزمة الضغط أثناء العملية.",
        "لو السؤال يبي استبعاد فرط الـ<bdi>aldosterone</bdi> بدل الفيوكروموسيتوما، يصير الفحص نسبة الـ<bdi>aldosterone</bdi> للرينين.",
    ],
    "rule": "قبل أي جراحة كظرية، لازم يُستبعد الفيوكروموسيتوما بتحليل الميتانفرين البولي، بغض النظر عن شكل الكتلة أو وجود ضغط <bdi>elevated</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
698: {
    "idea": "شاب عنده وذمة <bdi>severe</bdi> وبروتين بول ثقيل مع أجسام دهنية وأسطوانات هيالينية وبعض كريات الدم الحمراء، وحسب مفتاح الملف الجواب المعتمد هنا هو التهاب الكلى الخلالي.",
    "clues": [
        ("4+ edema", "وذمة <bdi>severe</bdi> بالأطراف السفلية"),
        ("Albumin 18", "ألبومين <bdi>low</bdi> جدًا (<bdi>normal</bdi> 34-56)"),
        ("4+ proteins", "بروتين بول عالي جدًا بالفحص السريع"),
        ("hyaline casts and occasional RBCs", "أسطوانات هيالينية وكريات دم حمراء متفرقة بتحليل البول"),
    ],
    "why_correct": [
        "بحسب الملف، الصورة المخبرية المجتمعة هنا (بروتين ثقيل مع أسطوانات هيالينية وكريات دم حمراء متفرقة) تُصنَّف كإصابة أنبوبية خلالية (<bdi>interstitial nephritis</bdi>) لا كمتلازمة نفروزية بحتة.",
        "الوذمة الـ<bdi>severe</bdi> ونقص الألبومين ناتجان هنا عن فقد البروتين المصاحب للإصابة الأنبوبية الخلالية الـ<bdi>severe</bdi> حسب تصنيف الملف.",
        "لازم نتعامل مع إجابة الملف كما هي حتى لو الصورة المخبرية تشبه كثيرًا متلازمة نفروزية كلاسيكية، لأن مفتاح الإجابة هو المعتمد بالبطاقة.",
    ],
    "when_changes": [
        "لو كانت الصورة بروتين بول ثقيل جدًا مع أجسام دهنية بيضاوية بارزة بدون أي مؤشر لالتهاب أنبوبي، يميل الـ<bdi>diagnosis</bdi> الكلاسيكي التقليدي لمتلازمة الكلى النفروزية.",
        "لو فيه حمى وكريات دم بيضاء وحمضات بالبول مع تاريخ دواء جديد، يقوّي هذا الشك بالتهاب الكلى الخلالي فعليًا.",
    ],
    "rule": "بروتين بول ثقيل مع وذمة ونقص ألبومين <bdi>severe</bdi> قد يُصنَّف أحيانًا ضمن إصابة أنبوبية خلالية حسب سياق السؤال ومفتاح الإجابة المعتمد، لا يُفترض دايمًا إنه نفروزي بحت.",
    "comparison": None,
    "guideline_note": None,
},
699: {
    "idea": "السؤال يبي التغيّر النسيجي المميز ل<bdi>glomerulonephritis</bdi> سريع التطور (RPGN)، وهو تكوّن الأهلة داخل كبسولة بومان.",
    "clues": [
        ("rapidly progressive glomerulonephritis", "<bdi>diagnosis</bdi> محدد بالسؤال، يوجه للتغيّر النسيجي المرتبط فيه"),
    ],
    "why_correct": [
        "التغيّر النسيجي المميز والمعرّف لـ<bdi>RPGN</bdi> هو تكوّن الأهلة (<bdi>crescents</bdi>) داخل كبسولة بومان <bdi>result</bdi> التهاب <bdi>severe</bdi> وتسرب فيبرين.",
        "هذا التغيّر هو اللي يعطي الـ<bdi>disease</bdi> اسمه (تطور سريع) لأنه يدمر الكبيبات بسرعة إذا ما عولج بشكل عاجل.",
        "باقي الخيارات تصف تغيّرات نسيجية ل<bdi>diseases</bdi> كلوية ثانية مختلفة تمامًا عن RPGN.",
    ],
    "when_changes": [
        "لو السؤال يبي التغيّر المميز لالتهاب الكلى الخلالي، يصير الجواب توسع الأنابيب مع ارتشاح التهابي.",
        "لو يبي التغيّر المميز ل<bdi>disease</bdi> IgA nephropathy تحديدًا، يصير ترسب IgA بالكبيبات.",
    ],
    "rule": "تكوّن الأهلة داخل كبسولة بومان هو الـ<bdi>sign</bdi> النسيجية المميزة ل<bdi>glomerulonephritis</bdi> سريع التطور.",
    "comparison": None,
    "guideline_note": None,
},
700: {
    "idea": "<bdi>patient</bdi> <bdi>diabetes</bdi> كبير بالسن بعد عملية بطنية، صار عنده صوديوم <bdi>low</bdi> مع أسمولية دم <bdi>low</bdi> وأسمولية بول <bdi>elevated</bdi> نسبيًا، وهذا يطابق إفراز هرمون مضاد الإدرار غير المناسب بعد الجراحة.",
    "clues": [
        ("Sodium 124", "صوديوم <bdi>low</bdi> (<bdi>normal</bdi> 134-146)"),
        ("Serum osmolality 270", "أسمولية دم <bdi>low</bdi>، تؤكد نقص صوديوم حقيقي مو كاذب"),
        ("Urine Osmolality 310", "أسمولية بول مركزة نسبيًا رغم انخفاض أسمولية الدم، تدل على وجود ADH نشط رغم إنه مو المفروض"),
        ("2 days after the operation", "التوتر الجراحي <bdi>cause</bdi> شائع لإفراز ADH غير مناسب"),
    ],
    "why_correct": [
        "انخفاض صوديوم وأسمولية الدم مع أسمولية بول غير مخفّفة (310 بدل تكون أقل من 100) يعني الكلى ما تطرح الماء الزايد بشكل <bdi>normal</bdi>، وهذا توقيع <bdi>SIADH</bdi>.",
        "التوتر الجراحي والألم من الـ<bdi>causes</bdi> الشائعة جدًا لـ SIADH بعد العمليات.",
        "البوتاسيوم والكرياتينين طبيعيين، وهذا يبعد <bdi>causes</bdi> ثانية مثل قصور الكلى أو أديسون.",
    ],
    "when_changes": [
        "لو أسمولية البول كانت <bdi>low</bdi> جدًا (أقل من 100)، يصير الـ<bdi>diagnosis</bdi> فرط شرب الماء (تسمم مائي) بدل SIADH.",
        "لو الـ<bdi>patient</bdi> عنده جفاف وهبوط ضغط مع بوتاسيوم <bdi>elevated</bdi>، يميل الـ<bdi>diagnosis</bdi> لقصور الكظر (Addison).",
    ],
    "rule": "نقص صوديوم مع أسمولية دم <bdi>low</bdi> وأسمولية بول غير مخفّفة بعد عملية أو توتر جسدي يوجه لـ SIADH.",
    "comparison": None,
    "guideline_note": None,
},
701: {
    "idea": "<bdi>patient</bdi> بسرطان رئة صغير الخلايا وعنده نقص صوديوم <bdi>severe</bdi> وعرَضي (لخبطة ذهنية)، وهذا نقص صوديوم <bdi>acute</bdi> <bdi>severe</bdi> يحتاج تصحيح عاجل ومراقب.",
    "clues": [
        ("small cell carcinoma of the lung", "<bdi>cause</bdi> معروف لإفراز ADH غير مناسب"),
        ("altered sensorium", "<bdi>symptom</bdi> عصبي خطير من نقص الصوديوم الـ<bdi>severe</bdi>"),
        ("Sodium 115", "صوديوم <bdi>low</bdi> جدًا (<bdi>normal</bdi> 134-146)"),
        ("euvolemic", "الـ<bdi>patient</bdi> غير جاف وغير محتقن، يدعم SIADH"),
    ],
    "why_correct": [
        "نقص صوديوم <bdi>severe</bdi> ومصحوب ب<bdi>symptoms</bdi> عصبية (لخبطة ذهنية) <bdi>case</bdi> إسعافية تحتاج تصحيح سريع بمحلول ملحي مفرط التوتر (<bdi>hypertonic saline</bdi>) لمنع تشنجات أو أذى دماغي.",
        "المحاليل الأخرى (سكر 5%، محلول ملحي عادي أو نصف <bdi>normal</bdi>) ما ترفع الصوديوم بسرعة كافية، وبعضها ممكن يزيد النقص سوء ب<bdi>case</bdi> SIADH.",
        "الهدف رفع الصوديوم بحذر وبمراقبة لتجنب التصحيح السريع الزائد اللي يسبب متلازمة تكسر الميالين.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> بدون <bdi>symptoms</bdi> عصبية وصوديومه <bdi>low</bdi> بشكل <bdi>chronic</bdi> و<bdi>mild</bdi>، الـ<bdi>treatment</bdi> يصير تقييد السوائل بدل المحلول المفرط التوتر.",
        "لو صار تصحيح سريع جدًا للصوديوم، يجب إبطاء المعدل لتجنب تكسر الميالين الجسري.",
    ],
    "rule": "نقص الصوديوم الـ<bdi>severe</bdi> العرضي (تشنج أو لخبطة) <bdi>case</bdi> إسعافية تُعالج بمحلول ملحي مفرط التوتر بحذر ومراقبة.",
    "comparison": None,
    "guideline_note": None,
},
702: {
    "idea": "<bdi>patient</bdi> عمل أشعة مقطعية بصبغة قبل يومين، وصار عنده ارتفاع كرياتينين وبولينا، وهذا تسمم كلوي بالصبغة (Contrast Induced Nephropathy) والسؤال يبي الآلية.",
    "clues": [
        ("2 days ago, he had CT brain with contrast", "التوقيت يطابق تسمم الصبغة الكلوي (يظهر خلال 48-72 ساعة)"),
        ("Creatinine 378", "ارتفاع واضح عن الـ<bdi>normal</bdi> (44-115)، يؤكد إصابة كلوية <bdi>acute</bdi>"),
    ],
    "why_correct": [
        "الصبغة الوريدية تسبب تضيق أوعية كلوية وسمية مباشرة على الخلايا الأنبوبية، والآلية النسيجية المعروفة هي <bdi>acute tubular necrosis</bdi>.",
        "التوقيت (يومين بعد الصبغة) يطابق تمامًا نمط تسمم الصبغة الكلوي الكلاسيكي.",
        "ما فيه <bdi>signs</bdi> حمى أو حساسية دوائية تدعم التهاب خلالي، ولا <bdi>signs</bdi> التهاب كبيبي نشط.",
    ],
    "when_changes": [
        "لو الإصابة الكلوية صارت ب<bdi>cause</bdi> جفاف أو هبوط ضغط بدون صبغة، تصير الآلية الأرجح قصور ما قبل الكلى (Pre-renal).",
        "لو فيه طفح جلدي وحمى وارتفاع الحمضات مع دواء جديد، يميل الـ<bdi>diagnosis</bdi> لالتهاب كلوي خلالي <bdi>acute</bdi>.",
    ],
    "rule": "ارتفاع الكرياتينين خلال يومين إلى ثلاثة من إعطاء صبغة وريدية يشير لتسمم كلوي بالصبغة، وآليته نخر أنبوبي <bdi>acute</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
703: {
    "idea": "شاب عنده ضغط <bdi>elevated</bdi> جدًا وبوتاسيوم <bdi>low</bdi> جدًا بدون <bdi>cause</bdi> واضح، وهذا الاجتماع يوجه ل<bdi>cause</bdi> هرموني كظري وليس ضغط أساسي.",
    "clues": [
        ("repeated BP of 170/110", "ضغط <bdi>severe</bdi> ومتكرر بشاب، يوجه للبحث عن <bdi>cause</bdi> ثانوي"),
        ("Potassium 2.1", "بوتاسيوم <bdi>low</bdi> جدًا (<bdi>normal</bdi> 3.5-5.1)، غير مفسر بدواء"),
        ("not on any medications", "يبعد كون البوتاسيوم الـ<bdi>low</bdi> ب<bdi>cause</bdi> مدرات"),
    ],
    "why_correct": [
        "ضغط <bdi>elevated</bdi> <bdi>severe</bdi> مع بوتاسيوم <bdi>low</bdi> جدًا بدون أي دواء مدرّ هو نمط كلاسيكي لفرط الـ<bdi>aldosterone</bdi> الأولي (<bdi>Conn syndrome</bdi>).",
        "زيادة الـ<bdi>aldosterone</bdi> تسبب احتباس صوديوم (يرفع الضغط) وفقد بوتاسيوم بالبول (يخفضه بالدم) في نفس الوقت.",
        "عمر الـ<bdi>patient</bdi> الصغير وعدم وجود <bdi>cause</bdi> واضح آخر يقوي الشك ب<bdi>cause</bdi> كظري ثانوي بدل ضغط أساسي.",
    ],
    "when_changes": [
        "لو فيه فرق بالضغط بين الذراعين والأرجل مع تأخر نبض فخذي، يصير الـ<bdi>diagnosis</bdi> تضيق الأبهر.",
        "لو الفحص السريري أظهر كتل بطنية كبيرة، يميل الـ<bdi>diagnosis</bdi> ل<bdi>disease</bdi> الكلى متعددة الكيسات.",
    ],
    "rule": "ضغط <bdi>elevated</bdi> مع بوتاسيوم <bdi>low</bdi> غير مفسر بدواء يوجه للبحث عن فرط الـ<bdi>aldosterone</bdi> الأولي.",
    "comparison": None,
    "guideline_note": None,
},
704: {
    "idea": "شاب عنده دم بالبول بعد يوم واحد فقط من التهاب حلق، وهذا التوقيت القصير جدًا (متزامن مع العدوى) هو الـ<bdi>sign</bdi> المميزة ل<bdi>disease</bdi> IgA nephropathy.",
    "clues": [
        ("hematuria, 1-day following a throat infection", "دم بالبول بعد يوم واحد بس من العدوى، توقيت قصير جدًا ومميز"),
    ],
    "why_correct": [
        "دم البول اللي يصاحب أو يتبع التهاب الحلق مباشرة (خلال 1-2 يوم) يسمى <bdi>synpharyngitic hematuria</bdi>، وهو <bdi>sign</bdi> كلاسيكية لـ<bdi>IgA nephropathy</bdi>.",
        "الـ<bdi>cause</bdi> إن IgA يترسب بالكبيبات كجزء من الاستجابة المناعية السريعة للعدوى، فالدم بالبول يظهر بسرعة مو بعد أسابيع.",
        "هذا يميزه بوضوح عن التهاب الكلى بعد العقديات اللي له فترة كمون أطول بكثير.",
    ],
    "when_changes": [
        "لو الدم بالبول ظهر بعد 1-3 أسابيع من التهاب الحلق، يصير الـ<bdi>diagnosis</bdi> التهاب كبيبات ما بعد العدوى.",
        "لو الصورة نفروزية (وذمة وبروتين ثقيل) بدل الدم بالبول، يميل الـ<bdi>diagnosis</bdi> ل<bdi>disease</bdi> ثاني مثل التصلب القطعي البؤري.",
    ],
    "rule": "دم البول اللي يظهر خلال يوم أو يومين من عدوى الحلق (توقيت متزامن) يوجه مباشرة لـ IgA nephropathy.",
    "comparison": None,
    "guideline_note": None,
},
705: {
    "idea": "الـ<bdi>patient</bdi> عندها نزيف رئوي مع التهاب كبيبات سريع التطور، مع تاريخ التهاب جيوب متكرر و<bdi>symptoms</bdi> عصبية طرفية (اعتلال أعصاب متعدد)، وهذي الصورة الثلاثية الكلاسيكية لالتهاب الأوعية الحبيبي (GPA).",
    "clues": [
        ("pulmonary hemorrhage and rapidly progressive glomerulonephritis", "إصابة رئوية وكلوية معًا، توجه لالتهاب أوعية جهازي"),
        ("recurrent sinusitis", "إصابة الجهاز التنفسي العلوي المتكررة، مميزة لـ GPA"),
        ("numbness in her right upper limb and left lower limb", "اعتلال أعصاب متعدد غير متناظر (mononeuritis multiplex)، شائع بالتهاب الأوعية"),
    ],
    "why_correct": [
        "اجتماع إصابة الجهاز التنفسي العلوي (الجيوب) والسفلي (نزيف رئوي) والكلى (RPGN) هو الثلاثية الكلاسيكية لـ<bdi>granulomatosis with polyangitis</bdi>.",
        "الـ<bdi>neuropathy</bdi> المتعدد غير المتناظر يدعم وجود التهاب أوعية جهازي يصيب الأعصاب الطرفية أيضًا.",
        "باقي أنواع التهاب الأوعية المذكورة ما تجمع نفس الثلاثية (تنفسي علوي+سفلي+كلوي) بهالشكل المميز.",
    ],
    "when_changes": [
        "لو ما فيه إصابة رئوية أو جيبية وكانت الصورة بطن وجلد بس ب<bdi>patient</bdi> متوسط العمر، يميل الـ<bdi>diagnosis</bdi> لالتهاب الشرايين متعدد العقد.",
        "لو الـ<bdi>patient</bdi> أصغر سنًا مع فرفرية جلدية وألم بطن، يصير الـ<bdi>diagnosis</bdi> فرفرية هينوخ شونلاين.",
    ],
    "rule": "نزيف رئوي مع التهاب كبيبات سريع التطور وتاريخ جيوب متكرر يوجه لـ granulomatosis with polyangitis.",
    "comparison": None,
    "guideline_note": None,
},
706: {
    "idea": "<bdi>patient</bdi> كلى <bdi>chronic</bdi> عنده بوتاسيوم <bdi>elevated</bdi> جدًا (6.5)، والسؤال يبي أول وأسرع <bdi>step</bdi> حماية للقلب قبل أي <bdi>procedure</bdi> ثاني.",
    "clues": [
        ("Potassium 6.5", "ارتفاع <bdi>severe</bdi> وخطير على نظم القلب"),
        ("Creatinine 440", "قصور كلوي متقدم، يفسر تراكم البوتاسيوم"),
    ],
    "why_correct": [
        "أول <bdi>step</bdi> بأي فرط بوتاسيوم خطير هي حماية عضلة القلب من تأثيره الكهربائي بإعطاء <bdi>IV calcium gluconate</bdi> فورًا.",
        "الكالسيوم يثبّت غشاء خلايا القلب بسرعة خلال دقائق، بينما باقي العلاجات تحتاج وقت أطول لتخفض البوتاسيوم فعليًا.",
        "بعد الكالسيوم، تُستخدم وسائل تنقل البوتاسيوم داخل الخلايا (<bdi>insulin</bdi> وجلوكوز) ثم الديلزة ك<bdi>treatment</bdi> نهائي لو احتاج الأمر.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> مستقر وبوتاسيومه أقل ارتفاعًا بدون تغيّرات تخطيط قلب، ممكن نبدأ مباشرة بالـ<bdi>insulin</bdi> والجلوكوز بدون كالسيوم.",
        "لو فشلت كل الوسائل بخفض البوتاسيوم أو الـ<bdi>patient</bdi> بقصور كلوي نهائي، تصير الديلزة هي الحل النهائي.",
    ],
    "rule": "بفرط البوتاسيوم الخطير، الكالسيوم الوريدي هو أول <bdi>step</bdi> لحماية القلب قبل أي <bdi>treatment</bdi> آخر.",
    "comparison": None,
    "guideline_note": None,
},
707: {
    "idea": "شاب عنده دم بالبول وضغط <bdi>elevated</bdi> بعد تاريخ التهاب لوزتين قبل 3 أسابيع، وهذا التوقيت المتأخر (أسابيع) يطابق التهاب الكلى بعد العقديات.",
    "clues": [
        ("red urine for 5 days", "دم بول مستمر"),
        ("tonsillitis 3 weeks ago", "فترة كمون 3 أسابيع بين العدوى وظهور الـ<bdi>symptoms</bdi> الكلوية"),
        ("elevated blood pressure", "ضغط <bdi>elevated</bdi>، شائع بالتهاب الكلى ما بعد العقديات"),
    ],
    "why_correct": [
        "فترة الكمون حوالي 3 أسابيع بين عدوى الحلق وظهور دم البول تطابق تمامًا <bdi>post streptococcal glomerulonephritis</bdi>.",
        "الضغط الـ<bdi>elevated</bdi> المصاحب يدعم الـ<bdi>diagnosis</bdi> أكثر لأنه شائع بهذا النوع <bdi>result</bdi> احتباس الملح والسوائل.",
        "عدم وجود ألم أو <bdi>symptoms</bdi> بولية أخرى يبعد <bdi>causes</bdi> ميكانيكية زي الحصوة.",
    ],
    "when_changes": [
        "لو دم البول ظهر خلال يوم أو يومين بس من العدوى، يصير الـ<bdi>diagnosis</bdi> الأرجح IgA nephropathy.",
        "لو فيه ألم جانبي <bdi>severe</bdi> مفاجئ، يميل الـ<bdi>diagnosis</bdi> لحصوة كلوية.",
    ],
    "rule": "دم البول بعد 1-3 أسابيع من عدوى حلق يوجه لالتهاب الكلى ما بعد العقديات، بخلاف IgA اللي فترة كمونه أقصر بكثير.",
    "comparison": None,
    "guideline_note": None,
},
708: {
    "idea": "<bdi>patient</bdi> قلبية عندها إسهال وتقيؤ <bdi>severe</bdi> أدى لجفاف حقيقي، ورغم مرضها القلبي الـ<bdi>chronic</bdi> الصورة الحالية جفاف واضح (ضغط <bdi>low</bdi>، JVP <bdi>low</bdi>، صوديوم بول <bdi>low</bdi>)، فالـ<bdi>treatment</bdi> المناسب سوائل وريدية بحذر.",
    "clues": [
        ("repeated vomiting and watery diarrhea", "فقد سوائل حقيقي من الجهاز الهضمي"),
        ("JVP is 1 cm above the sternal angle", "ضغط وريدي <bdi>low</bdi>، يدل على نقص حجم مو <bdi>congestion</bdi>"),
        ("Central venous line... 3 cm of H20", "ضغط وريدي مركزي <bdi>low</bdi> جدًا، يؤكد الجفاف"),
        ("Fractional excretion of sodium: 0.6%", "أقل من 1%، يدعم قصور كلوي ما قبل الكلى ب<bdi>cause</bdi> نقص الحجم"),
    ],
    "why_correct": [
        "كل المؤشرات (JVP <bdi>low</bdi>، CVP <bdi>low</bdi>، صوديوم بول <bdi>low</bdi>، FeNa أقل من 1%) تؤكد إن المشكلة نقص حجم حقيقي مو <bdi>congestion</bdi> قلبي، رغم إن الـ<bdi>patient</bdi> قلبية أصلًا.",
        "الـ<bdi>treatment</bdi> المناسب هو إعطاء سوائل وريدية بحذر وتدرج لتصحيح الجفاف مع مراقبة دقيقة لعدم إحداث <bdi>congestion</bdi> رئوي ب<bdi>patient</bdi> ضعيفة القلب.",
        "زيادة الـ<bdi>furosemide</bdi> أو الـ<bdi>spironolactone</bdi> بهالحالة تزيد الجفاف وتسوّي <bdi>renal failure</bdi> أسوأ، وهي خطأ شائع لو ما انتبهنا ل<bdi>signs</bdi> الجفاف.",
    ],
    "when_changes": [
        "لو كان الـJVP <bdi>elevated</bdi> مع <bdi>crepitations</bdi> رئوية، يصير الـ<bdi>diagnosis</bdi> <bdi>congestion</bdi> قلبي والـ<bdi>treatment</bdi> مدرات مو سوائل.",
        "لو ما تحسن الضغط بعد سوائل كافية ب<bdi>patient</bdi> قلبية، يصير التفكير بدعم مؤثر بالتقلص القلبي مثل الدوبوتامين.",
    ],
    "rule": "حتى ب<bdi>patient</bdi> قلبي <bdi>chronic</bdi>، <bdi>signs</bdi> الجفاف الواضحة (JVP وCVP منخفضين وFeNa أقل من 1%) تعني نقص حجم حقيقي يحتاج سوائل بحذر مو مدرات.",
    "comparison": {
        "headers": ["المؤشر", "القيمة", "الدلالة"],
        "rows": [
            ["<bdi>JVP</bdi>", "<bdi>low</bdi> (1 سم)", "نقص حجم مو <bdi>congestion</bdi>"],
            ["<bdi>CVP</bdi>", "<bdi>low</bdi> جدًا (3 سم H2O)", "يؤكد الجفاف"],
            ["<bdi>FeNa</bdi>", "0.6%", "قصور ما قبل الكلى (أقل من 1%)"],
        ],
    },
    "guideline_note": None,
},
709: {
    "idea": "<bdi>patient</bdi> <bdi>diabetes</bdi> عنده اعتلال كلوي <bdi>chronic</bdi> متقدم (تصفية كرياتينين 22 بس) وعلى مدر ثيازيدي، والوذمة مستمرة رغم استقرار وظيفة الكلى، والسؤال يبي التعديل الأنسب على الـ<bdi>treatment</bdi>.",
    "clues": [
        ("Creatinine clearance 22", "قصور كلوي متقدم (مرحلة 4)، عند هذا المستوى المدرات الثيازيدية تفقد فعاليتها"),
        ("progressive lower limbs edema for the last 4 months", "وذمة <bdi>chronic</bdi> ومستمرة رغم الـ<bdi>treatment</bdi> الحالي"),
        ("Renal function was similar to 3 months ago", "الوظيفة الكلوية مستقرة، يبعد كون الوذمة من تدهور <bdi>acute</bdi>"),
    ],
    "why_correct": [
        "المدرات الثيازيدية تفقد فعاليتها الكبيرة عند تصفية كرياتينين <bdi>low</bdi> جدًا زي هالمريض، فما تسيطر على احتباس السوائل بشكل كافٍ.",
        "تبديل المدر الثيازيدي لمدر عروي (<bdi>furosemide</bdi>) يعطي سيطرة أفضل على الوذمة عند هالمستوى من <bdi>renal failure</bdi>.",
        "وظيفة الكلى مستقرة، فما فيه داعي لإيقاف <bdi>ramipril</bdi> الحامي للكلى ب<bdi>patient</bdi> <bdi>diabetes</bdi> نفروباثي.",
    ],
    "when_changes": [
        "لو ارتفع البوتاسيوم أو تدهورت وظيفة الكلى بشكل <bdi>acute</bdi> بعد رامبريل، يصير إيقافه أو تخفيض جرعته منطقي.",
        "لو الوذمة كانت بسيطة ومستقرة وما تزعج الـ<bdi>patient</bdi>، ممكن نكتفي بالمراقبة بدون تغيير الدواء.",
    ],
    "rule": "عند قصور كلوي متقدم، المدرات الثيازيدية تفقد فعاليتها، والتبديل لمدر عروي مثل furosemide هو الأنسب للسيطرة على الوذمة.",
    "comparison": None,
    "guideline_note": None,
},
710: {
    "idea": "<bdi>patient</bdi> كلى <bdi>chronic</bdi> متقدم مقبل على غسيل كلوي مخطط له، والسؤال يبي أفضل نوع وصول وعائي دائم.",
    "clues": [
        ("Creatinine clearance 10", "قصور كلوي <bdi>severe</bdi>، يقارب الحاجة للديلزة"),
        ("Haemodialysis is planned to start soon", "التخطيط مسبق يسمح بتحضير وصول دائم مثالي"),
    ],
    "why_correct": [
        "الناسور الشرياني الوريدي (<bdi>arteriovenous fistula</bdi>) هو أفضل وصول دائم للغسيل الكلوي لأنه أقل عرضة للعدوى والتجلط ويدوم أطول.",
        "بما إن الديلزة مخطط لها مسبقًا، فيه وقت كافٍ لتحضير الناسور ونضوجه قبل الحاجة الفعلية.",
        "الطعم الوعائي والقساطر تُستخدم لو الأوعية ما تسمح بعمل ناسور أو لو الحاجة عاجلة بدون وقت كافٍ.",
    ],
    "when_changes": [
        "لو أوعية الـ<bdi>patient</bdi> ضعيفة وما تسمح بعمل ناسور، يصير الطعم الوعائي الخيار البديل.",
        "لو الديلزة محتاجة تبدأ فورًا بدون وقت للتحضير، تُستخدم قسطرة وريدية مؤقتة (نفقية أو غير نفقية) لحين تجهيز وصول دائم.",
    ],
    "rule": "الناسور الشرياني الوريدي هو الخيار المفضل دايمًا للوصول الدائم بالغسيل الكلوي المخطط له مسبقًا.",
    "comparison": None,
    "guideline_note": None,
},
711: {
    "idea": "السؤال يبي أي سيناريو بإصابة كلوية <bdi>acute</bdi> يستدعي إحالة عاجلة لديلزة طارئة، وهذا يعتمد على معايير محددة لخطورة الـ<bdi>case</bdi> مو مجرد رقم تصفية.",
    "clues": [
        ("Potassium of 7.5 after 3 courses of medical management", "بوتاسيوم خطير جدًا وفشل الـ<bdi>treatment</bdi> الدوائي بالسيطرة عليه"),
    ],
    "why_correct": [
        "فرط بوتاسيوم <bdi>severe</bdi> (7.5) ومقاوم لل<bdi>treatment</bdi> الدوائي (بعد 3 محاولات) هو مؤشر إسعافي واضح لديلزة عاجلة لخطورته على نظم القلب.",
        "هذا من المعايير الكلاسيكية لديلزة طارئة (الحموضة، اضطراب الشوارد، التسمم، <bdi>congestion</bdi> السوائل، اليوريميا) المعروفة باختصار AEIOU.",
        "باقي الخيارات (رقم تصفية <bdi>low</bdi> بمفرده، بول قليل جدًا، أو تكرار سابق للإصابة) مؤشرات مهمة بس مو بحد ذاتها معيار إسعافي قاطع بدون سياق شوارد أو <bdi>symptoms</bdi>.",
    ],
    "when_changes": [
        "لو انخفض إخراج البول بشدة مع <bdi>congestion</bdi> رئوي مقاوم للمدرات، يصير هذا مؤشر إسعافي إضافي لديلزة عاجلة.",
        "لو الـ<bdi>patient</bdi> عنده حموضة استقلابية <bdi>severe</bdi> مقاومة لل<bdi>treatment</bdi>، يصير هذا أيضًا مؤشر عاجل للديلزة.",
    ],
    "rule": "فرط البوتاسيوم الـ<bdi>severe</bdi> المقاوم لل<bdi>treatment</bdi> الدوائي من أهم مؤشرات الديلزة العاجلة بالإصابة الكلوية الـ<bdi>acute</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
712: {
    "idea": "<bdi>patient</bdi> كلى <bdi>chronic</bdi> مرحلة 3 محتاج أشعة مقطعية بصبغة عاجلة، والسؤال يبي أهم <bdi>procedure</bdi> يقلل <bdi>risk</bdi> تسمم الكلى بالصبغة.",
    "clues": [
        ("chronic kidney disease stage 3", "وظيفة كلوية <bdi>low</bdi> أصلًا، <bdi>factor</bdi> <bdi>risk</bdi> رئيسي لتسمم الصبغة"),
        ("Creatinine 160", "ارتفاع فوق الـ<bdi>normal</bdi>، يؤكد ضعف الوظيفة الكلوية"),
    ],
    "why_correct": [
        "الترطيب الوريدي بمحلول ملحي 0.9% قبل وبعد الـ<bdi>procedure</bdi> هو أهم وأثبت <bdi>procedure</bdi> لتقليل <bdi>risk</bdi> تسمم الكلى بالصبغة.",
        "الترطيب يحسّن تروية الكلى ويقلل تركيز الصبغة بالأنابيب الكلوية، وهذا يقلل الضرر المباشر عليها.",
        "خيارات مثل الأسيتيل سيستين أو البيكربونات الفموي أدلتها أضعف بكثير مقارنة بالترطيب الوريدي المباشر.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عنده <bdi>congestion</bdi> سوائل واضح (قصور قلب)، لازم تعديل سرعة وكمية الترطيب لتجنب زيادة الحمل على القلب.",
        "لو الـ<bdi>procedure</bdi> طارئ جدًا وما فيه وقت للترطيب المسبق، يُعطى الترطيب أثناء وبعد الـ<bdi>procedure</bdi> بأقصى سرعة ممكنة وآمنة.",
    ],
    "rule": "الترطيب الوريدي بمحلول ملحي قبل وبعد الصبغة هو أهم <bdi>procedure</bdi> لتقليل <bdi>risk</bdi> تسمم الكلى بالصبغة.",
    "comparison": None,
    "guideline_note": None,
},
713: {
    "idea": "<bdi>patient</bdi> عنده فرط بوتاسيوم <bdi>severe</bdi> جدًا مع تغيّرات تخطيط قلب خطيرة (موجات T مدببة)، فالـ<bdi>step</bdi> الأولى الإسعافية حماية القلب فورًا.",
    "clues": [
        ("Potassium 6.9", "فرط بوتاسيوم <bdi>severe</bdi> جدًا"),
        ("ECG: Showed tall peaked T waves", "تغيّر تخطيط قلب خطير، دليل على تأثير مباشر على عضلة القلب"),
        ("Creatinine 240", "قصور كلوي واضح، <bdi>cause</bdi> محتمل لفرط البوتاسيوم"),
    ],
    "why_correct": [
        "وجود تغيّرات تخطيط قلب (موجات T مدببة) يجعل حماية غشاء القلب أولوية قصوى وفورية بإعطاء <bdi>IV calcium gluconate</bdi>.",
        "الكالسيوم لا يخفض البوتاسيوم لكنه يثبّت غشاء الخلايا القلبية خلال دقائق ويمنع اضطراب النظم الخطير ريثما تُعطى علاجات تخفض البوتاسيوم فعليًا.",
        "الـ<bdi>insulin</bdi> والسالبوتامول يساعدون بنقل البوتاسيوم داخل الخلايا، بس يُعطون بعد أو مع الكالسيوم مو بدل عنه عند وجود تغيّرات تخطيط قلب.",
    ],
    "when_changes": [
        "لو ما فيه تغيّرات تخطيط قلب رغم ارتفاع البوتاسيوم، يمكن البدء بالـ<bdi>insulin</bdi> والجلوكوز مباشرة بدون كالسيوم أولًا.",
        "لو فشلت كل الوسائل الدوائية أو الـ<bdi>patient</bdi> بقصور كلوي نهائي، تصير الديلزة هي الحل النهائي.",
    ],
    "rule": "فرط بوتاسيوم مع تغيّرات تخطيط قلب يستدعي كالسيوم وريدي فورًا لحماية القلب قبل أي <bdi>treatment</bdi> آخر يخفض البوتاسيوم.",
    "comparison": None,
    "guideline_note": None,
},
714: {
    "idea": "<bdi>patient</bdi> عنده فرط بوتاسيوم واضح بس بدون تغيّرات تخطيط قلب <bdi>acute</bdi>، فالأولوية هنا نقل البوتاسيوم داخل الخلايا مباشرة بدون حاجة ماسة لحماية غشاء القلب أولًا.",
    "clues": [
        ("Potassium 6.6", "فرط بوتاسيوم واضح لكن أقل شدة من الـ<bdi>case</bdi> السابقة"),
        ("ECG shows no acute changes", "غياب تغيّرات تخطيط القلب الخطيرة، يقلل إلحاح الحماية القلبية الفورية"),
    ],
    "why_correct": [
        "بغياب تغيّرات تخطيط القلب، الـ<bdi>treatment</bdi> الأولي الأنسب هو نقل البوتاسيوم داخل الخلايا بـ<bdi>insulin with dextrose infusion</bdi>.",
        "هذا يخفض مستوى البوتاسيوم بالدم بسرعة معقولة خلال دقائق إلى ساعة، ويعطي وقت للعلاجات الطويلة المدى تشتغل.",
        "الكالسيوم الوريدي يُحجز للحالات اللي فيها تغيّرات تخطيط قلب فعلية، وهنا مو موجودة.",
    ],
    "when_changes": [
        "لو ظهرت تغيّرات تخطيط قلب لاحقًا أو ارتفع البوتاسيوم أكثر، يصير الكالسيوم الوريدي أولوية فورية.",
        "لو فشل الـ<bdi>treatment</bdi> الدوائي بالسيطرة على البوتاسيوم، تصير الديلزة الـ<bdi>step</bdi> التالية.",
    ],
    "rule": "فرط بوتاسيوم بدون تغيّرات تخطيط قلب يُعالج أولًا بنقل البوتاسيوم داخل الخلايا (<bdi>insulin</bdi> وجلوكوز)، والكالسيوم يُحجز لوجود تغيّرات تخطيط قلب.",
    "comparison": None,
    "guideline_note": None,
},
715: {
    "idea": "<bdi>patient</bdi> عندها متلازمة كلى نفروزية سببها <bdi>disease</bdi> التغيّر الأدنى، والـ<bdi>treatment</bdi> الأولي المعروف لهذا الـ<bdi>disease</bdi> بالذات هو الستيرويد.",
    "clues": [
        ("minimal change glomerulonephritis", "<bdi>cause</bdi> نفروزي محدد له <bdi>treatment</bdi> نوعي معروف"),
        ("proteinuria", "الـ<bdi>symptom</bdi> الرئيسي المطلوب تقليله"),
    ],
    "why_correct": [
        "<bdi>disease</bdi> التغيّر الأدنى (<bdi>minimal change disease</bdi>) يستجيب بشكل ممتاز للستيرويدات (<bdi>prednisolone</bdi>)، وأغلب المرضى يدخلون هدأة كاملة بهذا الـ<bdi>treatment</bdi>.",
        "الستيرويد هو الـ<bdi>treatment</bdi> النوعي الأولي المستهدف لل<bdi>disease</bdi> نفسه، مو بس دعم عرضي.",
        "الحمية والمراقبة بدون <bdi>treatment</bdi> لا تعالج الـ<bdi>cause</bdi>، ومثبطات الإنزيم المحول تُستخدم كدعم إضافي مو ك<bdi>treatment</bdi> أساسي لهالمرض بالذات.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> قاومت الستيرويد أو تكرر الـ<bdi>disease</bdi> بشكل متكرر، يصير التفكير بأدوية مثبطة مناعية ثانية.",
        "لو الـ<bdi>cause</bdi> النفروزي كان اعتلال كلوي غشائي بدل التغيّر الأدنى، يختلف الـ<bdi>treatment</bdi> الأولي المستخدم.",
    ],
    "rule": "الستيرويد هو الـ<bdi>treatment</bdi> الأولي القياسي لمتلازمة الكلى النفروزية الناتجة عن <bdi>disease</bdi> التغيّر الأدنى.",
    "comparison": None,
    "guideline_note": None,
},
716: {
    "idea": "<bdi>patient</bdi> عندها كرون ونقص بوتاسيوم ما يتحسن رغم تعويض قوي بالبوتاسيوم، وهذا نمط كلاسيكي لنقص مغنيسيوم مصاحب يمنع تصحيح البوتاسيوم.",
    "clues": [
        ("Crohn's disease", "<bdi>disease</bdi> يسبب سوء امتصاص وفقد مغنيسيوم من الأمعاء"),
        ("hypokalemia refractory to aggressive paranteral and oral KCI supplementation", "فشل تعويض البوتاسيوم المكثف، <bdi>sign</bdi> مميزة لنقص مغنيسيوم مصاحب"),
    ],
    "why_correct": [
        "نقص المغنيسيوم يمنع الكلى من الاحتفاظ بالبوتاسيوم ويعيق تصحيحه مهما أعطينا بوتاسيوم، لأن المغنيسيوم ضروري لعمل مضخات البوتاسيوم بالخلايا.",
        "مرضى كرون معرضون لنقص المغنيسيوم ب<bdi>cause</bdi> سوء الامتصاص الـ<bdi>chronic</bdi> والإسهال، فتصحيح المغنيسيوم أولًا يخلي البوتاسيوم يستقر بعد كذا.",
        "الـ<bdi>step</bdi> الصحيحة هنا إعطاء <bdi>IV magnesium sulfate</bdi> قبل أي محاولة ثانية لتعويض البوتاسيوم.",
    ],
    "when_changes": [
        "لو المغنيسيوم كان <bdi>normal</bdi> والبوتاسيوم ما زال <bdi>low</bdi> رغم التعويض، يصير التفكير ب<bdi>causes</bdi> ثانية زي فرط الـ<bdi>aldosterone</bdi>.",
        "لو تحسن البوتاسيوم بعد تصحيح المغنيسيوم، يؤكد هذا إن نقص المغنيسيوم كان الـ<bdi>cause</bdi> الأساسي.",
    ],
    "rule": "نقص البوتاسيوم المقاوم للتعويض المكثف يوجه دايمًا لفحص وتصحيح المغنيسيوم أولًا.",
    "comparison": None,
    "guideline_note": None,
},
717: {
    "idea": "<bdi>patient</bdi> سكرية عندها ضغط <bdi>elevated</bdi> حديث وبروتين بول جديد، وهذا يوجه لبدء <bdi>treatment</bdi> يحمي الكلى ويخفض الضغط بنفس الوقت.",
    "clues": [
        ("10-year history of type 2 diabetes", "مدة كافية لتطور اعتلال كلوي <bdi>diabetes</bdi>"),
        ("hypertension and proteinuria", "علامتان تدلان على بداية اعتلال كلوي <bdi>diabetes</bdi>"),
        ("Creatinine 80", "وظيفة كلوية لسه <bdi>normal</bdi>، فرصة للحماية المبكرة"),
    ],
    "why_correct": [
        "ظهور بروتين بول جديد مع ضغط <bdi>elevated</bdi> ب<bdi>patient</bdi> سكرية يستدعي بدء <bdi>ACE inhibitors</bdi> فورًا لأنها تخفض الضغط وتحمي الكلى بتقليل الضغط داخل الكبيبات.",
        "الانتظار 6 أشهر لتعديل نمط الحياة بس غير كافٍ هنا لأن البروتينيوريا وارتفاع الضغط يحتاجون تدخل دوائي عاجل يحمي الكلى.",
        "التحكم <bdi>diabetes</bdi> الحالي (HbA1c 7%) مقبول نسبيًا، فزيادة جرعة الـ<bdi>insulin</bdi> مو الأولوية الآن مقارنة بحماية الكلى من الضغط.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> ما عندها بروتين بول أصلًا وبس ضغطها <bdi>elevated</bdi> بسيط، يمكن نجرب تعديل نمط الحياة أولًا لفترة قصيرة.",
        "لو ارتفع البوتاسيوم بشكل واضح بعد بدء الدواء، يحتاج تعديل الجرعة أو المراقبة الدقيقة.",
    ],
    "rule": "ظهور بروتين بول مع ضغط <bdi>elevated</bdi> ب<bdi>patient</bdi> <bdi>diabetes</bdi> يستدعي بدء مثبطات الإنزيم المحول للأنجيوتنسين فورًا لحماية الكلى.",
    "comparison": None,
    "guideline_note": None,
},
718: {
    "idea": "السؤال يبي أفضل <bdi>treatment</bdi> لتقليل تكوّن الحصوات عند <bdi>patient</bdi> عنده زيادة كالسيوم بالبول (hypercalciuria)، وهذا له <bdi>treatment</bdi> دوائي محدد ومعروف.",
    "clues": [
        ("hypercalciuria", "زيادة إفراز الكالسيوم بالبول، <bdi>cause</bdi> رئيسي لحصوات الكالسيوم"),
    ],
    "why_correct": [
        "المدرات الثيازيدية (<bdi>thiazide diuretics</bdi>) تزيد امتصاص الكالسيوم بالأنابيب الكلوية وتقلل طرحه بالبول، وهذا يقلل تكوّن حصوات الكالسيوم بشكل مباشر.",
        "هذا الـ<bdi>treatment</bdi> يستهدف الـ<bdi>cause</bdi> الفسيولوجي نفسه (زيادة كالسيوم البول) مو بس يعالج نوع ثاني من الحصوات.",
        "تقييد الكالسيوم الغذائي فكرة خاطئة شائعة، لأنه فعليًا يزيد امتصاص الأوكسالات ويرفع <bdi>risk</bdi> الحصوات بدل ما يقلله.",
    ],
    "when_changes": [
        "لو الـ<bdi>cause</bdi> حصوات حمض اليوريك بدل الكالسيوم، يصير الـ<bdi>treatment</bdi> المناسب الألوبيورينول.",
        "لو الـ<bdi>cause</bdi> حصوات السيستين، يصير الدواء المناسب البنسيلامين.",
    ],
    "rule": "المدرات الثيازيدية هي الـ<bdi>treatment</bdi> الأساسي لتقليل تكوّن حصوات الكالسيوم عند وجود فرط كالسيوم البول.",
    "comparison": None,
    "guideline_note": None,
},
719: {
    "idea": "<bdi>patient</bdi> كلى <bdi>chronic</bdi> متقدم جدًا (كرياتينين عالي جدًا) وعنده اعتلال أعصاب طرفي (<bdi>paresthesia</bdi> وغياب منعكسات)، وهذا <bdi>symptom</bdi> يوريمي يدل إن الوقت حان لبدء الديلزة.",
    "clues": [
        ("chronic kidney disease for 3 years", "<bdi>disease</bdi> كلوي <bdi>chronic</bdi> معروف"),
        ("decrease sensation... absent ankle reflexes", "اعتلال أعصاب طرفي، من <bdi>complications</bdi> اليوريميا المتقدمة"),
        ("Creatinine 674", "ارتفاع <bdi>severe</bdi> جدًا يدل على مرحلة كلوية نهائية"),
        ("Urea 46", "بولينا <bdi>elevated</bdi> جدًا، تدعم التسمم اليوريمي"),
    ],
    "why_correct": [
        "<bdi>neuropathy</bdi> الطرفي عند <bdi>patient</bdi> كلى <bdi>chronic</bdi> مع كرياتينين <bdi>elevated</bdi> جدًا هو أحد <bdi>symptoms</bdi> اليوريميا المتقدمة، وهو مؤشر لبدء الديلزة مو بس <bdi>treatment</bdi> عرضي.",
        "لا فيتامين B ولا تصحيح الحموضة أو <bdi>anemia</bdi> يعالج الـ<bdi>cause</bdi> الجذري هنا، لأن المشكلة تراكم سموم يوريمية تحتاج إزالة فعلية بالديلزة.",
        "بدء <bdi>dialysis</bdi> يزيل السموم المسببة لل<bdi>neuropathy</bdi> ويمنع تدهوره أكثر.",
    ],
    "when_changes": [
        "لو الأنيميا كانت هي الـ<bdi>cause</bdi> الوحيد لل<bdi>symptoms</bdi> بدون <bdi>signs</bdi> يوريميا <bdi>severe</bdi>، يصير <bdi>treatment</bdi> الإريثروبويتين هو الأنسب.",
        "لو المشكلة الأساسية حموضة استقلابية بسيطة بدون <bdi>symptoms</bdi> عصبية، يكفي تصحيحها ببيكربونات فموي.",
    ],
    "rule": "<bdi>neuropathy</bdi> الطرفي عند <bdi>patient</bdi> كلى <bdi>chronic</bdi> مع كرياتينين <bdi>elevated</bdi> جدًا هو <bdi>symptom</bdi> يوريمي يستدعي بدء الديلزة.",
    "comparison": None,
    "guideline_note": None,
},
720: {
    "idea": "<bdi>patient</bdi> ذئبة مستقرة من سنين طلع عندها بروتين بول ودم بالبول جديد مع ارتفاع كرياتينين، وهذا تغيّر مقلق يوجه ل<bdi>assessment</bdi> مباشر لنشاط الـ<bdi>disease</bdi> بالكلى.",
    "clues": [
        ("stable for several years", "استقرار سابق طويل، يخلي أي تغيّر جديد مهم"),
        ("Protein 500", "بروتين بول <bdi>elevated</bdi> جدًا عن الـ<bdi>normal</bdi> (0-150)"),
        ("RBC 5000", "دم بول <bdi>elevated</bdi> جدًا عن الـ<bdi>normal</bdi> (حتى 4000)"),
        ("Creatinine 160", "ارتفاع كرياتينين جديد، يدل على تأثر وظيفة الكلى"),
    ],
    "why_correct": [
        "ظهور بروتين ودم بالبول مع ارتفاع كرياتينين ب<bdi>patient</bdi> ذئبة مستقرة يوجه بقوة لانتكاسة كلوية (<bdi>lupus nephritis</bdi>) تحتاج <bdi>diagnosis</bdi> دقيق.",
        "الخزعة الكلوية (<bdi>renal biopsy</bdi>) هي الطريقة الوحيدة لتحديد نوع ودرجة التهاب الكلى الذئبي وتوجيه الـ<bdi>treatment</bdi> المناسب (أي نوع مثبط مناعي وبأي جرعة).",
        "الانتظار أو تكرار فحص البول بس بدون خزعة يؤخر <bdi>treatment</bdi> قد يكون عاجل لمنع تلف كلوي دائم.",
    ],
    "when_changes": [
        "لو التغيّر كان بسيط جدًا وغير مؤكد، يمكن نبدأ بتكرار الفحص وتأكيد الأجسام المضادة قبل خزعة مباشرة.",
        "لو الفحوصات أظهرت مشكلة انسدادية أو وعائية بدل التهاب كلوي، يصير دوبلر الكلى هو المطلوب.",
    ],
    "rule": "أي تدهور كلوي جديد (بروتين، دم بول، ارتفاع كرياتينين) ب<bdi>patient</bdi> ذئبة مستقرة يستدعي خزعة كلوية لتحديد نوع الإصابة وتوجيه الـ<bdi>treatment</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
721: {
    "idea": "<bdi>patient</bdi> <bdi>diabetes</bdi> ظهر عنده ألبومين بول بمستوى الألبومينيوريا الدقيقة لأول مرة، والسؤال يبي الـ<bdi>step</bdi> التالية الصحيحة قبل اتخاذ أي قرار علاجي كبير.",
    "clues": [
        ("microalbuminuria range for the first time", "أول مرة يظهر هذا المستوى، يحتاج تأكيد قبل التصنيف ك<bdi>disease</bdi> <bdi>chronic</bdi>"),
        ("no diagnosis of hypertension", "يبعد كون الألبومين ب<bdi>cause</bdi> ضغط غير مضبوط"),
    ],
    "why_correct": [
        "أي <bdi>result</bdi> ألبومينيوريا دقيقة لأول مرة لازم تُعاد للتأكد إنها مو مؤقتة (ممكن تحصل من تمرين <bdi>severe</bdi> أو عدوى أو حمى قريبة)، قبل ما نعتبرها اعتلال كلوي <bdi>diabetes</bdi> حقيقي.",
        "<bdi>Repeat urine albumin/creatinine ratio</bdi> هي الـ<bdi>step</bdi> المنطقية التالية للتأكيد قبل أي تغيير بالـ<bdi>treatment</bdi>.",
        "ما فيه داعي لإيقاف الـ<bdi>metformin</bdi> لأن وظيفة الكلى (الكرياتينين وHbA1c) <bdi>normal</bdi> وما فيه مؤشر لقصور كلوي حالي.",
    ],
    "when_changes": [
        "لو تأكدت الألبومينيوريا بفحص متكرر، يصير بدء مثبطات الإنزيم المحول للأنجيوتنسين هو الـ<bdi>step</bdi> التالية المنطقية.",
        "لو ظهرت وظيفة كلوية متدهورة فعليًا، يصير إيقاف أو تعديل جرعة الـ<bdi>metformin</bdi> ضروري.",
    ],
    "rule": "أي <bdi>result</bdi> ألبومينيوريا دقيقة لأول مرة تحتاج تأكيد بإعادة الفحص قبل اعتبارها اعتلال كلوي <bdi>diabetes</bdi> وبدء <bdi>treatment</bdi> جديد.",
    "comparison": None,
    "guideline_note": None,
},
722: {
    "idea": "<bdi>patient</bdi> شابة عندها إعياء ودم بالبول ووذمة بعد التهاب حلق قبل 3 أسابيع بالضبط، وهذا التوقيت المتأخر يطابق التهاب الكلى ما بعد العقديات مو IgA.",
    "clues": [
        ("sore throat 3 weeks ago", "فترة كمون 3 أسابيع، مميزة لالتهاب الكلى ما بعد العقديات"),
        ("bloody urine and swelling of her hands and feet", "دم بول ووذمة، صورة نفريتية كلاسيكية"),
        ("Blood pressure 166/108", "ضغط <bdi>elevated</bdi> <bdi>severe</bdi>، شائع بهذا الـ<bdi>disease</bdi> ب<bdi>cause</bdi> احتباس الملح"),
    ],
    "why_correct": [
        "فترة الكمون 3 أسابيع بالضبط بين التهاب الحلق وظهور الـ<bdi>symptoms</bdi> الكلوية تطابق تمامًا <bdi>poststreptococcal glomerulonephritis</bdi>.",
        "الصورة الكاملة (دم بول، وذمة، ضغط <bdi>elevated</bdi>) نمط نفريتي كلاسيكي يدعم هذا الـ<bdi>diagnosis</bdi>.",
        "IgA nephropathy وBerger disease (اللي هو نفس <bdi>disease</bdi> IgA) فترة كمونهم أقصر بكثير (يوم أو يومين)، فما يطابقون هالتوقيت.",
    ],
    "when_changes": [
        "لو ظهر دم البول بعد يوم أو يومين بس من العدوى، يصير الـ<bdi>diagnosis</bdi> IgA nephropathy بدل PSGN.",
        "لو الصورة كانت نفروزية (وذمة <bdi>severe</bdi> وبروتين ثقيل بدون دم بول بارز) يميل الـ<bdi>diagnosis</bdi> لاعتلال كلوي غشائي.",
    ],
    "rule": "فترة كمون حوالي 3 أسابيع بين عدوى الحلق والـ<bdi>symptoms</bdi> الكلوية تميز التهاب الكلى ما بعد العقديات عن IgA nephropathy اللي كمونه أقصر بكثير.",
    "comparison": None,
    "guideline_note": None,
},
723: {
    "idea": "<bdi>patient</bdi> كلى <bdi>chronic</bdi> متقدم مقبل على ديلزة، والسؤال يبي الـ<bdi>cause</bdi> الأشيع للوفاة بمرضى الكلى الـ<bdi>chronic</bdi> عمومًا، وهو غالبًا مو الكلى نفسها.",
    "clues": [
        ("chronic and progressing renal disease", "<bdi>disease</bdi> كلوي <bdi>chronic</bdi> متقدم"),
        ("need dialysis sometime within the next year", "مرحلة متأخرة من <bdi>renal failure</bdi>"),
    ],
    "why_correct": [
        "<bdi>diseases</bdi> القلب والأوعية الدموية (<bdi>cardiovascular disease</bdi>) هي الـ<bdi>cause</bdi> الأشيع للوفاة بمرضى الكلى الـ<bdi>chronic</bdi>، حتى أكثر من <bdi>renal failure</bdi> نفسه.",
        "<bdi>renal failure</bdi> الـ<bdi>chronic</bdi> يسرّع <bdi>atherosclerosis</bdi> ويزيد <bdi>risk</bdi> احتشاء القلب والسكتة ب<bdi>cause</bdi> اضطرابات الشحوم والكالسيوم والضغط المصاحبة.",
        "هذا مفهوم إحصائي مهم بالطب الكلوي: أغلب مرضى الكلى الـ<bdi>chronic</bdi> يموتون ب<bdi>cause</bdi> <bdi>complications</bdi> قلبية وعائية قبل ما يوصلون لمرحلة <bdi>renal failure</bdi> الكامل أحيانًا.",
    ],
    "when_changes": [
        "لو السؤال يبي الـ<bdi>cause</bdi> المباشر لدخول الـ<bdi>patient</bdi> بمرحلة الديلزة، يصير الجواب <bdi>renal failure</bdi> نفسه.",
        "لو الـ<bdi>patient</bdi> عنده نزيف <bdi>acute</bdi> غير مسيطر عليه، يصير هذا هو <bdi>cause</bdi> الوفاة المباشر بذاك السياق المحدد.",
    ],
    "rule": "الـ<bdi>cause</bdi> الأشيع للوفاة بمرضى الكلى الـ<bdi>chronic</bdi> هو <bdi>diseases</bdi> القلب والأوعية الدموية، مو <bdi>renal failure</bdi> نفسه.",
    "comparison": None,
    "guideline_note": None,
},
724: {
    "idea": "<bdi>patient</bdi> كبير بالسن عنده ضغط مقاوم على 4 أدوية والأشعة تبين كليتين غير متساويتين بالحجم، وهذا يوجه ل<bdi>cause</bdi> وعائي كلوي وراء الضغط المقاوم.",
    "clues": [
        ("taking 4 anti-hypertensives drugs", "ضغط مقاوم لل<bdi>treatment</bdi> رغم عدة أدوية"),
        ("Abdominal ultrasound shows asymmetrical kidneys", "اختلاف حجم الكليتين، <bdi>sign</bdi> مباشرة على تضيق وعائي بجهة واحدة"),
        ("history of ischemic heart disease", "<bdi>factor</bdi> <bdi>risk</bdi> ل<bdi>atherosclerosis</bdi> اللي يشمل شرايين الكلى أيضًا"),
    ],
    "why_correct": [
        "اختلاف حجم الكليتين هو <bdi>sign</bdi> تصويرية مباشرة تدل على نقص تروية <bdi>chronic</bdi> لكلية واحدة ب<bdi>cause</bdi> تضيق بشريانها.",
        "ضغط مقاوم رغم 4 أدوية مع تاريخ <bdi>disease</bdi> قلبي إقفاري (<bdi>factor</bdi> <bdi>risk</bdi> ل<bdi>atherosclerosis</bdi>) يدعم <bdi>diagnosis</bdi> <bdi>renal artery stenosis</bdi> تصلبيًا.",
        "باقي الـ<bdi>causes</bdi> المذكورة (كوشينغ، فرط <bdi>aldosterone</bdi>، كلى متعددة الكيسات) عادة تعطي كليتين متماثلتين بالحجم أو صورة مختلفة تمامًا بالأشعة.",
    ],
    "when_changes": [
        "لو الكليتان كانتا متساويتين بالحجم مع كتل كيسية متعددة، يميل الـ<bdi>diagnosis</bdi> ل<bdi>disease</bdi> الكلى متعددة الكيسات.",
        "لو فيه سمنة مركزية وخطوط أرجوانية مع الضغط المقاوم، يصير التفكير بمتلازمة كوشينغ.",
    ],
    "rule": "اختلاف حجم الكليتين ب<bdi>patient</bdi> ضغط مقاوم لل<bdi>treatment</bdi> يوجه مباشرة لتضيق الشريان الكلوي.",
    "comparison": None,
    "guideline_note": None,
},
725: {
    "idea": "<bdi>patient</bdi> كلى <bdi>chronic</bdi> متقدم يبي يعرف أي طعام يحتوي بوتاسيوم عالي يتجنبه أو يقلله، والسؤال يختبر معرفة الأطعمة الغنية بالبوتاسيوم.",
    "clues": [
        ("chronic kidney disease stage 4", "مرحلة متقدمة تحتاج ضبط دقيق للبوتاسيوم الغذائي"),
        ("potassium rich food should be consumed in moderate amount", "يبي تحديد أي طعام من الخيارات غني بالبوتاسيوم فعليًا"),
    ],
    "why_correct": [
        "الطماطم (<bdi>tomatoes</bdi>) من الأطعمة الغنية نسبيًا بالبوتاسيوم، خصوصًا لو استُخدمت بكميات كبيرة أو كصلصة مركزة.",
        "<bdi>patient</bdi> الكلى الـ<bdi>chronic</bdi> بمرحلة 4 معرض لتراكم البوتاسيوم بسهولة، فلازم يقلل الأطعمة الغنية فيه زي الطماطم.",
        "العنب والفاصوليا الخضراء وعصير التوت البري من الأطعمة الأقل بوتاسيوم نسبيًا مقارنة بالطماطم، فهي أأمن بكمية أكبر.",
    ],
    "when_changes": [
        "لو السؤال يبي فاكهة عالية البوتاسيوم بدل خضار، يصير الجواب الموز أو البرتقال.",
        "لو الـ<bdi>patient</bdi> عنده بوتاسيوم <bdi>low</bdi> أصلًا (نادر بهالمرحلة)، يختلف التركيز الغذائي تمامًا.",
    ],
    "rule": "بمرضى الكلى الـ<bdi>chronic</bdi> المتقدمة، الأطعمة الغنية بالبوتاسيوم زي الطماطم تحتاج تقليل استهلاكها.",
    "comparison": {
        "headers": ["الطعام", "محتوى البوتاسيوم"],
        "rows": [
            ["<bdi>Tomatoes</bdi>", "<bdi>elevated</bdi> نسبيًا"],
            ["<bdi>Grapes</bdi>", "<bdi>low</bdi>"],
            ["<bdi>Green beans</bdi>", "<bdi>low</bdi> إلى متوسط"],
            ["<bdi>Cranberry juice</bdi>", "<bdi>low</bdi>"],
        ],
    },
    "guideline_note": None,
},
726: {
    "idea": "امرأة حامل بأسبوع 38 عندها عدوى مسالك بولية مؤكدة، والسؤال يبي المضاد الآمن المناسب لهذا العمر الحملي المتأخر تحديدًا.",
    "clues": [
        ("38 weeks pregnant", "قرب الولادة، يستبعد أدوية معينة خطرة على الجنين بهالمرحلة"),
        ("urine dipstick is positive for nitrites and leucocytes", "تأكيد وجود عدوى بولية بكتيرية"),
    ],
    "why_correct": [
        "<bdi>Cefalexin</bdi> مضاد حيوي آمن طوال فترة الحمل بما فيها قرب الولادة، ويغطي الجراثيم الشائعة المسببة لعدوى المسالك البولية.",
        "عدوى المسالك البولية بالحامل لازم تُعالج بمضاد حيوي فعلي مو بس نصيحة شرب سوائل، لتجنب <bdi>complications</bdi> مثل <bdi>pyelonephritis</bdi>.",
        "اختيار مضاد آمن ومناسب للمرحلة الحملية مهم جدًا هنا لأن بعض المضادات لها قيود خاصة قرب الولادة.",
    ],
    "when_changes": [
        "لو كانت الحامل بالثلث الأول أو الثاني بدون مشاكل، يمكن اعتبار النيتروفيورانتوين خيار مقبول أيضًا.",
        "لو تطورت الـ<bdi>symptoms</bdi> لألم جانبي وحمى (التهاب حويضة وكلية)، يحتاج الـ<bdi>patient</bdi> دخول ومضاد حيوي وريدي.",
    ],
    "rule": "عدوى المسالك البولية بالحامل قرب الولادة تُعالج بمضاد آمن مثل cefalexin، وتُتجنب أدوية لها قيود خاصة بهالمرحلة.",
    "comparison": None,
    "guideline_note": None,
},
727: {
    "idea": "شاب عنده أخت مصابة ب<bdi>disease</bdi> الكلى متعددة الكيسات الوراثي (ADPKD) وجاء للفحص الوقائي، والسؤال يبي أفضل فحص فحص مبدئي للكشف عن الـ<bdi>disease</bdi>.",
    "clues": [
        ("sister with adult polycystic kidney disease", "تاريخ عائلي إيجابي يستدعي فحص وقائي"),
        ("came to screen for the disease", "الهدف فحص كشف مبكر مو <bdi>diagnosis</bdi> <bdi>symptoms</bdi> موجودة"),
    ],
    "why_correct": [
        "الموجات فوق الصوتية على البطن (<bdi>ultrasound abdomen</bdi>) هي الفحص المعياري والأول للكشف عن الكيسات الكلوية عند الأقارب المعرضين ل<bdi>risk</bdi> ADPKD.",
        "هذا الفحص بسيط، رخيص، ما فيه إشعاع، وحساس كفاية للكشف عن الكيسات المميزة لهالمرض.",
        "الأشعة المقطعية أدق بس مو ضرورية كفحص أول، والفحوصات الجينية أو أجسام مضادة معينة مو فحص كشف روتيني معتمد هنا.",
    ],
    "when_changes": [
        "لو <bdi>result</bdi> الموجات فوق الصوتية غير حاسمة بشاب صغير السن، ممكن نحتاج فحص جيني أو أشعة مقطعية للتأكيد.",
        "لو الـ<bdi>patient</bdi> عنده <bdi>symptoms</bdi> فعلية (ألم جانبي أو دم بول) بدل الفحص الوقائي، يتغير مسار الـ<bdi>assessment</bdi> ل<bdi>diagnosis</bdi> الـ<bdi>symptoms</bdi> مباشرة.",
    ],
    "rule": "الموجات فوق الصوتية على البطن هي الفحص الأول والمعياري لفحص ADPKD عند الأقارب المعرضين لل<bdi>risk</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
728: {
    "idea": "<bdi>patient</bdi> كلى <bdi>chronic</bdi> مرحلة 3 مستقر، والسؤال يبي أي دواء من الخيارات آمن نسبيًا للاستخدام بهذا المستوى من <bdi>renal failure</bdi>.",
    "clues": [
        ("stable chronic kidney disease stage 3", "قصور كلوي متوسط، يحتاج انتباه لسمية الأدوية الكلوية"),
    ],
    "why_correct": [
        "<bdi>Warfarin</bdi> يُستقلب بشكل رئيسي بالكبد وليس بالكلى، فهو من الأدوية الآمنة نسبيًا للاستخدام بقصور كلوي مرحلة 3 مع <bdi>follow-up</bdi> معتادة لمعدل التخثر.",
        "هذا يجعله الخيار الأنسب مقارنة بباقي الأدوية المذكورة اللي لها مشاكل معروفة بهالمرحلة من <bdi>renal failure</bdi>.",
        "لازم دايمًا مراجعة آلية تخلص الدواء (كبدي أو كلوي) قبل وصفه ل<bdi>patient</bdi> قصور كلوي.",
    ],
    "when_changes": [
        "لو <bdi>renal failure</bdi> كان أشد (مرحلة 4 أو 5)، حتى الـ<bdi>warfarin</bdi> يحتاج حذر إضافي بالمراقبة لزيادة <bdi>risk</bdi> النزيف.",
        "لو الـ<bdi>patient</bdi> محتاج مضاد حيوي بولي، لازم يتجنب النيتروفيورانتوين وتختار بديل آمن أكثر بهالمرحلة.",
    ],
    "rule": "الأدوية اللي تُستقلب كبديًا مثل الـ<bdi>warfarin</bdi> أأمن نسبيًا بقصور الكلى الـ<bdi>chronic</bdi> مقارنة بالأدوية اللي تعتمد على التخلص الكلوي أو السمية الكلوية المباشرة.",
    "comparison": {
        "headers": ["الدواء", "المشكلة بقصور الكلى"],
        "rows": [
            ["<bdi>Nitrofurantoin</bdi>", "تراكم وسمية، تخلص كلوي ضعيف الفعالية"],
            ["<bdi>Metformin</bdi>", "<bdi>risk</bdi> حماض لاكتيكي"],
            ["<bdi>Lithium</bdi>", "سمية كلوية وتراكم"],
            ["<bdi>Warfarin</bdi>", "استقلاب كبدي، آمن نسبيًا"],
        ],
    },
    "guideline_note": None,
},
729: {
    "idea": "<bdi>patient</bdi> على غسيل كلوي منذ 8 سنين، والسؤال يبي الـ<bdi>cause</bdi> الأشيع للوفاة بمرضى الغسيل الكلوي الـ<bdi>chronic</bdi> على المدى الطويل.",
    "clues": [
        ("haemodialysis for chronic kidney disease for the past 8 years", "مدة طويلة على الغسيل، يعني تعرض تراكمي ل<bdi>factors</bdi> <bdi>risk</bdi> قلبية وعائية"),
    ],
    "why_correct": [
        "<bdi>diseases</bdi> القلب الإقفارية (<bdi>ischaemic heart disease</bdi>) هي الـ<bdi>cause</bdi> الأشيع للوفاة بمرضى الغسيل الكلوي الـ<bdi>chronic</bdi>، أكثر من أي <bdi>cause</bdi> ثاني.",
        "مرضى الغسيل الكلوي معرضون بشكل كبير ل<bdi>atherosclerosis</bdi> المتسارع ب<bdi>cause</bdi> اضطرابات الشحوم والكالسيوم والفوسفات الـ<bdi>chronic</bdi> المصاحبة للقصور الكلوي.",
        "العدوى المرتبطة بالغسيل وفرط البوتاسيوم والأورام <bdi>causes</bdi> وفاة معروفة بس أقل شيوعًا مقارنة ب<bdi>diseases</bdi> القلب الإقفارية إحصائيًا.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عنده حمى وتدهور مفاجئ حول جلسة غسيل، يصير الـ<bdi>cause</bdi> الأرجح المباشر عدوى مرتبطة بالقسطرة أو الوصول الوعائي.",
        "لو صار توقف مفاجئ للقلب بعد جلسة غسيل متأخرة، يصير فرط البوتاسيوم هو الـ<bdi>cause</bdi> المباشر بذاك الموقف تحديدًا.",
    ],
    "rule": "الـ<bdi>cause</bdi> الأشيع للوفاة على المدى الطويل بمرضى الغسيل الكلوي الـ<bdi>chronic</bdi> هو <bdi>diseases</bdi> القلب الإقفارية.",
    "comparison": None,
    "guideline_note": None,
},
730: {
    "idea": "امرأة حامل عندها <bdi>symptoms</bdi> والتهاب بولي مؤكد بعدد كريات دم بيضاء عالي جدًا بالبول، والسؤال يبي أفضل مضاد حيوي مناسب لحالتها.",
    "clues": [
        ("pregnant woman presented with frequency and dysuria", "<bdi>symptoms</bdi> التهاب مسالك بولية واضحة"),
        ("Leukocytes 30", "عدد كريات دم بيضاء عالي جدًا بالبول (<bdi>normal</bdi> 0-3)، يؤكد عدوى فعلية"),
    ],
    "why_correct": [
        "<bdi>Augmentin</bdi> (أموكسيسيلين-كلافولانيك) مضاد آمن أثناء الحمل وواسع الطيف بما يكفي لتغطية الجراثيم الشائعة المسببة للعدوى البولية.",
        "شدة العدوى هنا (كريات دم بيضاء عالية جدًا) تحتاج مضاد فعال وموثوق التغطية، وليس فقط نصيحة أو مراقبة.",
        "اختيار مضاد آمن للحمل ضروري لتجنب أي تأثير سلبي على الجنين مع ضمان <bdi>treatment</bdi> فعال للعدوى.",
    ],
    "when_changes": [
        "لو كانت الحامل قريبة جدًا من الولادة (بعد 36 أسبوع)، يُفضّل تجنب النيتروفيورانتوين واختيار بديل آمن مثل أوجمنتين أو سيفالكسين.",
        "لو تطورت الـ<bdi>symptoms</bdi> لحمى وألم جانبي، يصير الـ<bdi>diagnosis</bdi> التهاب حويضة وكلية ويحتاج دخول ومضاد وريدي.",
    ],
    "rule": "عدوى المسالك البولية عند الحامل تُعالج بمضاد حيوي آمن وفعال مثل الأوجمنتين، وتُتجنب المضادات الممنوعة بالحمل مثل الفلوروكينولونات والدوكسيسيكلين.",
    "comparison": None,
    "guideline_note": None,
},
731: {
    "idea": "<bdi>patient</bdi> على <bdi>heparin</bdi> ل<bdi>thrombus</bdi> وريدية عميقة، وعنده فرط بوتاسيوم مع قصور كلوي <bdi>mild</bdi>، والسؤال يبي أي دواء من أدويته الحالية يسبب أو يفاقم فرط البوتاسيوم ولازم يوقف.",
    "clues": [
        ("Potassium 6,0", "فرط بوتاسيوم واضح"),
        ("insulin; furosemide and enalapril", "قائمة الأدوية الحالية، لازم تحديد المسبب من بينها"),
        ("Creatinine 120", "قصور كلوي بسيط يزيد تأثير الأدوية المرتبطة بالبوتاسيوم"),
    ],
    "why_correct": [
        "<bdi>Enalapril</bdi> (مثبط إنزيم محول للأنجيوتنسين) من أشهر الأدوية اللي ترفع البوتاسيوم بتقليل إفراز الـ<bdi>aldosterone</bdi>، خصوصًا مع وجود قصور كلوي بسيط.",
        "إيقاف الإنالابريل مؤقتًا يعتبر الـ<bdi>step</bdi> الأنسب لتصحيح فرط البوتاسيوم بدون التأثير على <bdi>treatment</bdi> الـ<bdi>thrombus</bdi> أو <bdi>diabetes</bdi>.",
        "الـ<bdi>heparin</bdi> ضروري ل<bdi>treatment</bdi> الـ<bdi>thrombus</bdi> الوريدية العميقة ولا يوقف لمجرد فرط بوتاسيوم بسيط، والـ<bdi>furosemide</bdi> أصلًا يخفض البوتاسيوم مو يرفعه.",
    ],
    "when_changes": [
        "لو كان البوتاسيوم <bdi>elevated</bdi> بشكل خطير مع تغيّرات تخطيط قلب، يحتاج <bdi>treatment</bdi> إسعافي فوري بغض النظر عن أي دواء يوقف.",
        "لو تبين إن <bdi>cause</bdi> فرط البوتاسيوم دواء ثاني غير الإنالابريل، يصير إيقاف ذاك الدواء هو الأنسب بدلًا منه.",
    ],
    "rule": "مثبطات الإنزيم المحول للأنجيوتنسين مثل enalapril من أشيع <bdi>causes</bdi> فرط البوتاسيوم الدوائي، خصوصًا مع وجود قصور كلوي ولو بسيط.",
    "comparison": None,
    "guideline_note": None,
},
732: {
    "idea": "<bdi>patient</bdi> كبير بالسن عنده <bdi>diabetes</bdi> من النوع الثاني وقصور كلوي مع بروتين بول ثقيل جدًا، وأشيع <bdi>cause</bdi> لهذي الصورة ب<bdi>patient</bdi> <bdi>diabetes</bdi> طويل الأمد هو الـ<bdi>nephropathy</bdi> <bdi>diabetes</bdi> نفسه.",
    "clues": [
        ("type 2 diabetes mellitus", "<bdi>disease</bdi> <bdi>chronic</bdi> معروف يسبب اعتلال كلوي تدريجي مع الوقت"),
        ("Creatinine 196", "ارتفاع واضح عن الـ<bdi>normal</bdi>، يدل على تأثر وظيفة الكلى"),
        ("Urinary protein: creatinine ratio 154 mg/mmol (&lt;30)", "بروتين بول ثقيل جدًا، أعلى بكثير من الـ<bdi>normal</bdi>"),
    ],
    "why_correct": [
        "الـ<bdi>nephropathy</bdi> <bdi>diabetes</bdi> (<bdi>diabetic nephropathy</bdi>) هو أشيع <bdi>cause</bdi> لبروتين بول ثقيل مع قصور كلوي تدريجي ب<bdi>patient</bdi> <bdi>diabetes</bdi> طويل الأمد، وهو التفسير الأبسط والأرجح هنا.",
        "الكالسيوم الـ<bdi>elevated</bdi> بشكل بسيط والألم الظهري ممكن يكونان مصادفة أو مرتبطين ب<bdi>factors</bdi> ثانية عند كبار السن، بينما الـ<bdi>cause</bdi> الرئيسي المباشر للبروتينيوريا و<bdi>renal failure</bdi> يبقى <bdi>diabetes</bdi>.",
        "الروماتويد الـ<bdi>chronic</bdi> <bdi>factor</bdi> <bdi>risk</bdi> إضافي معروف ل<bdi>diseases</bdi> كلوية ثانوية، لكن وجود <bdi>diabetes</bdi> طويل الأمد يجعل الـ<bdi>cause</bdi> <bdi>diabetes</bdi> هو الأرجح إحصائيًا بمثل هالعمر والتاريخ المرضي.",
    ],
    "when_changes": [
        "لو كان الكالسيوم <bdi>elevated</bdi> جدًا بشكل بارز بدون تفسير واضح، يميل الـ<bdi>diagnosis</bdi> أكثر لفرط جارات الدرقية الأولي أو <bdi>cause</bdi> ورمي مرتبط بخلايا البلازما.",
        "لو ما فيه تاريخ <bdi>diabetes</bdi> أصلًا وكانت الصورة بروتين بول ثقيل مع ألم عظمي ب<bdi>patient</bdi> كبير بالسن، يصير التفكير بأميلويد أو مايلوما أقوى.",
    ],
    "rule": "بروتين بول ثقيل مع قصور كلوي تدريجي ب<bdi>patient</bdi> <bdi>diabetes</bdi> طويل الأمد يوجه أولًا لل<bdi>nephropathy</bdi> <bdi>diabetes</bdi> ك<bdi>cause</bdi> أشيع وأبسط تفسيرًا.",
    "comparison": None,
    "guideline_note": None,
},
733: {
    "idea": "<bdi>patient</bdi> ضغط عنده سكتة دماغية إقفارية قديمة (10 أيام) ومستقر الآن، والسؤال يبي أفضل <bdi>treatment</bdi> للوقاية الثانوية من سكتة جديدة.",
    "clues": [
        ("10-day history of a left-sided hemiparesis", "سكتة إقفارية مؤكدة قبل فترة، مستقرة حاليًا"),
        ("CT scan of the brain confirmed an area of infarction", "تأكيد إقفار مو نزيف، يسمح بإعطاء مضاد صفائح"),
        ("already started physiotherapy", "مرحلة تأهيل، تؤكد استقرار الـ<bdi>case</bdi> الـ<bdi>acute</bdi>"),
    ],
    "why_correct": [
        "بعد تأكيد السكتة الإقفارية وثبات الـ<bdi>case</bdi>، الـ<bdi>treatment</bdi> القياسي للوقاية الثانوية هو مضاد الصفائح <bdi>aspirin</bdi>.",
        "مضادات التخثر (<bdi>warfarin</bdi> أو أبيكسابان) تُحجز للسكتات ذات المصدر القلبي (زي <bdi>atrial fibrillation</bdi>)، ومو مذكور هنا مصدر قلبي.",
        "الـ<bdi>t-PA</bdi> <bdi>treatment</bdi> <bdi>acute</bdi> يُعطى خلال ساعات من بداية الـ<bdi>symptoms</bdi>، والسكتة هنا عمرها 10 أيام فات وقتها تمامًا.",
    ],
    "when_changes": [
        "لو كان مصدر السكتة قلبي (<bdi>atrial fibrillation</bdi> مثلًا)، يصير مضاد التخثر هو الـ<bdi>treatment</bdi> الأنسب بدل الـ<bdi>aspirin</bdi>.",
        "لو كان الـ<bdi>patient</bdi> بأول 4.5 ساعة من بداية الـ<bdi>symptoms</bdi> بدون نزيف، يصير الـt-PA هو الخيار العلاجي الـ<bdi>acute</bdi>.",
    ],
    "rule": "بعد السكتة الإقفارية غير القلبية المصدر ومرور نافذة الـ<bdi>treatment</bdi> الـ<bdi>acute</bdi>، مضاد الصفائح (<bdi>aspirin</bdi>) هو الأساس للوقاية الثانوية.",
    "comparison": None,
    "guideline_note": None,
},
734: {
    "idea": "<bdi>patient</bdi> سكرية عندها فقدان بصر مفاجئ بعين واحدة لمدة قصيرة ثم رجع <bdi>normal</bdi> تمامًا، وهذي الصورة الكلاسيكية لنوبة نقص تروية عابرة بالعين (amaurosis fugax).",
    "clues": [
        ("sudden left eye visual loss for 20 minutes", "فقدان بصر مفاجئ ومؤقت، يزول تلقائيًا"),
        ("vision returned to normal after this episode", "تعافي كامل، يستبعد <bdi>cause</bdi> دائم مثل انفصال الشبكية"),
        ("diabetes mellitus", "<bdi>factor</bdi> <bdi>risk</bdi> وعائي يدعم <bdi>cause</bdi> نقص تروية"),
    ],
    "why_correct": [
        "فقدان بصر مفاجئ وعابر بعين واحدة يرجع <bdi>normal</bdi> تلقائيًا هو صورة كلاسيكية لنوبة نقص تروية عابرة تصيب شريان الشبكية (نوع من <bdi>TIA</bdi>).",
        "وجود <bdi>diabetes</bdi> ك<bdi>factor</bdi> <bdi>risk</bdi> وعائي يدعم الـ<bdi>cause</bdi> الإقفاري العابر للوعاء الدموي.",
        "التعافي الكامل خلال دقائق يبعد <bdi>causes</bdi> دائمة زي انفصال الشبكية اللي عادة ما يرجع <bdi>normal</bdi> من نفسه بهالسرعة.",
    ],
    "when_changes": [
        "لو الفقدان كان مؤلم ومصحوب ب<bdi>symptoms</bdi> عصبية ثانية عند شاب، يصير التفكير بالتهاب العصب البصري ضمن <bdi>multiple sclerosis</bdi>.",
        "لو الفقدان دائم ومصحوب بومضات ضوء وذباب طائر، يصير الـ<bdi>diagnosis</bdi> الأرجح انفصال الشبكية.",
    ],
    "rule": "فقدان بصر مفاجئ وعابر بعين واحدة يرجع <bdi>normal</bdi> تلقائيًا ب<bdi>patient</bdi> عنده <bdi>factors</bdi> <bdi>risk</bdi> وعائية هو نوبة نقص تروية عابرة حتى يثبت العكس.",
    "comparison": None,
    "guideline_note": None,
},
735: {
    "idea": "الـ<bdi>patient</bdi> عنده <bdi>symptoms</bdi> ضعف عام تدريجي مع <bdi>signs</bdi> إصابة عصبون علوي (منعكسات نشطة وتشنج) وإصابة عصبون سفلي (رجفان لساني وفخذي) بنفس الوقت، وهذا الاجتماع المميز يوجه ل<bdi>disease</bdi> العصبون الحركي.",
    "clues": [
        ("stumbling, weak grip, dysphagia, and generalized weakness", "ضعف منتشر متعدد الأجهزة العضلية"),
        ("2 episodes of aspiration pneumonia", "ضعف بلع (بصلي)، <bdi>complication</bdi> خطيرة"),
        ("brisk reflexes, spastic muscles", "<bdi>signs</bdi> عصبون حركي علوي"),
        ("fasciculation of the tongue and thigh", "<bdi>signs</bdi> عصبون حركي سفلي بمناطق متعددة"),
    ],
    "why_correct": [
        "اجتماع <bdi>signs</bdi> عصبون علوي (منعكسات نشطة وتشنج) وعصبون سفلي (رجفان عضلي) بنفس الـ<bdi>patient</bdi> بدون خلل حسي هو التوقيع المميز ل<bdi>disease</bdi> العصبون الحركي (<bdi>motor neuron disease</bdi>).",
        "صعوبة البلع والتهاب رئة استنشاقي متكرر يعكسان ضعف عضلات البصلة، وهذا شائع ب<bdi>disease</bdi> العصبون الحركي المتقدم.",
        "غياب أي خلل حسي مهم جدًا هنا، لأنه يستبعد <bdi>diseases</bdi> الأعصاب الطرفية ويدعم كون المشكلة بالعصبونات الحركية بس.",
    ],
    "when_changes": [
        "لو الضعف كان بعصب واحد محدد بس بدون <bdi>signs</bdi> عصبون علوي، يصير الـ<bdi>diagnosis</bdi> اعتلال عصب مفرد.",
        "لو الضعف يتحسن مع الراحة ويسوء مع الجهد المتكرر بدون <bdi>signs</bdi> عصبون علوي، يميل الـ<bdi>diagnosis</bdi> لوهن عضلي وبيل.",
    ],
    "rule": "اجتماع <bdi>signs</bdi> عصبون حركي علوي وسفلي بنفس الـ<bdi>patient</bdi> وبدون خلل حسي يوجه ل<bdi>disease</bdi> العصبون الحركي.",
    "comparison": None,
    "guideline_note": None,
},
736: {
    "idea": "<bdi>patient</bdi> تصلب متعدد على <bdi>treatment</bdi> مثبت، وصار عنده انتكاسة <bdi>acute</bdi> جديدة (<bdi>symptoms</bdi> جديدة وآفات نشطة بالرنين)، والسؤال يبي <bdi>treatment</bdi> هذي النوبة الـ<bdi>acute</bdi> تحديدًا مو الـ<bdi>treatment</bdi> طويل المدى.",
    "clues": [
        ("acute onset diplopia, ataxia, and weakness of the right hand", "<bdi>symptoms</bdi> عصبية <bdi>acute</bdi> جديدة، تشير لانتكاسة"),
        ("New active lesions compared to previous scans", "تأكيد الانتكاسة بالتصوير، آفات جديدة نشطة"),
    ],
    "why_correct": [
        "<bdi>treatment</bdi> النوبة الـ<bdi>acute</bdi> ب<bdi>multiple sclerosis</bdi> هو <bdi>IV corticosteroids</bdi> بجرعة عالية لتقصير مدة الانتكاسة وتسريع التعافي.",
        "الإنترفيرون دواء وقائي طويل المدى لتقليل تكرار النوبات، والـ<bdi>patient</bdi> أصلًا عليه، فهو مو <bdi>treatment</bdi> للنوبة الـ<bdi>acute</bdi> الحالية.",
        "الستيرويد الوريدي يعطي تركيز أعلى وأسرع تأثير من الستيرويد الفموي بالنوبات الـ<bdi>acute</bdi> المصحوبة ب<bdi>symptoms</bdi> مقلقة زي ضعف اليد.",
    ],
    "when_changes": [
        "لو النوبة كانت <bdi>mild</bdi> جدًا وما تؤثر على الوظيفة اليومية، ممكن يُكتفى بالستيرويد الفموي بدل الوريدي.",
        "لو ما استجاب الـ<bdi>patient</bdi> للستيرويد الوريدي، يصير التفكير بفصادة البلازما ك<bdi>step</bdi> تالية بالنوبات الـ<bdi>severe</bdi> المقاومة.",
    ],
    "rule": "انتكاسة <bdi>multiple sclerosis</bdi> الـ<bdi>acute</bdi> تُعالج بالستيرويد الوريدي بجرعة عالية، بينما الإنترفيرون <bdi>treatment</bdi> وقائي طويل المدى مو للنوبة الـ<bdi>acute</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
737: {
    "idea": "رجل كبير بالسن عنده صورة كلاسيكية ل<bdi>disease</bdi> <bdi>Parkinson's disease</bdi> (رجفان بالراحة، وجه بلا تعابير، مشية بخطوات قصيرة بدون تلويح ذراع)، والسؤال يبي موقع الخلل التشريحي المسؤول.",
    "clues": [
        ("expressionless face, slow and slurred speech", "<bdi>signs</bdi> نمطية ل<bdi>disease</bdi> <bdi>Parkinson's disease</bdi>"),
        ("hand tremor at rest", "رجفان بالراحة، مميز ل<bdi>Parkinson's disease</bdi> مو ل<bdi>diseases</bdi> مخيخية"),
        ("gait is quick, with short steps and diminished associated movements", "مشية <bdi>parkinsonism</bdi> كلاسيكية"),
    ],
    "why_correct": [
        "كل الـ<bdi>signs</bdi> (رجفان بالراحة، بطء حركة، تيبس، مشية <bdi>parkinsonism</bdi>) تعكس خلل بالعقد القاعدية <bdi>result</bdi> نقص الـ<bdi>dopamine</bdi> من تنكس <bdi>substantia nigra</bdi>.",
        "هذا هو الموقع التشريحي المسؤول تحديدًا عن <bdi>disease</bdi> <bdi>Parkinson's disease</bdi>، لأن الخلايا المفرزة لل<bdi>dopamine</bdi> موجودة فيه.",
        "المخيخ يسبب رعاش قصدي و<bdi>ataxia</bdi> مو رجفان بالراحة، والفص الجبهي يسبب تغيّر شخصية ووظائف تنفيذية مو هالصورة الحركية.",
    ],
    "when_changes": [
        "لو كان الرجفان قصديًا (يزيد عند الحركة الهادفة) مع <bdi>ataxia</bdi>، يصير موقع الخلل الأرجح المخيخ.",
        "لو الـ<bdi>symptoms</bdi> الرئيسية تغيّر شخصية وصعوبة تخطيط بدون <bdi>symptoms</bdi> حركية، يصير موقع الخلل الفص الجبهي.",
    ],
    "rule": "رجفان بالراحة مع بطء حركة وتيبس ومشية <bdi>parkinsonism</bdi> يعكس خلل بالـsubstantia nigra ضمن العقد القاعدية.",
    "comparison": None,
    "guideline_note": None,
},
738: {
    "idea": "<bdi>patient</bdi> كبير بالسن عنده تدهور إدراكي ووعي مع <bdi>signs</bdi> <bdi>parkinsonism</bdi> واضحة (بطء حركة، رجفان بالراحة، وجه بلا تعابير، مشية متعثرة)، والسؤال يبي الـ<bdi>diagnosis</bdi> الأرجح.",
    "clues": [
        ("decline in cognitive capacity and conscious level", "تدهور إدراكي مصاحب"),
        ("bradykinesia, resting tremors, a mask-like face, and a shuffling gait", "الـ<bdi>symptoms</bdi> الحركية الأربعة الكلاسيكية ل<bdi>Parkinson's disease</bdi>"),
    ],
    "why_correct": [
        "اجتماع بطء الحركة والرجفان بالراحة والوجه الجامد والمشية المتعثرة هي الـ<bdi>signs</bdi> الحركية الأساسية الأربعة ل<bdi>disease</bdi> <bdi>Parkinson disease</bdi>.",
        "هذي الصورة الحركية المركّبة أوضح وأشمل من أي <bdi>diagnosis</bdi> ثاني من الخيارات المطروحة.",
        "خلل الحركة المتأخر (تارديف) يعطي حركات لا إرادية مختلفة تمامًا، وهنتنغتون يعطي كوريا لا بطء حركة.",
    ],
    "when_changes": [
        "لو كان التدهور الإدراكي هو الأبرز من البداية مع هلاوس بصرية وتذبذب بالوعي، يميل الـ<bdi>diagnosis</bdi> ل<bdi>dementia</bdi> أجسام ليوي.",
        "لو كانت الحركات لا إرادية سريعة (كوريا) مع تاريخ عائلي، يصير الـ<bdi>diagnosis</bdi> هنتنغتون.",
    ],
    "rule": "اجتماع بطء الحركة والرجفان بالراحة والوجه الجامد والمشية المتعثرة يشخّص <bdi>disease</bdi> <bdi>Parkinson's disease</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
739: {
    "idea": "<bdi>patient</bdi> ب<bdi>case</bdi> <bdi>epilepsy</bdi> مستمر (نوبات متكررة أكثر من 30 دقيقة) وما استجاب للبنزوديازيبين الوريدي، والسؤال يبي الدواء التالي بخط الـ<bdi>treatment</bdi>.",
    "clues": [
        ("repetitive generalized seizures that continue for 35 minutes", "<bdi>case</bdi> <bdi>epilepsy</bdi> مستمر مؤكدة"),
        ("received 20 mg of diazepam intravenously, but there has been no response", "فشل خط الـ<bdi>treatment</bdi> الأول (بنزوديازيبين)"),
    ],
    "why_correct": [
        "بعد فشل البنزوديازيبين، الخط الثاني ب<bdi>case</bdi> <bdi>epilepsy</bdi> المستمر هو <bdi>phenytoin IV</bdi> كجرعة تحميل.",
        "الفينيتوين يعطي تحكم أطول أمدًا بعد ما يخفف البنزوديازيبين النوبة مؤقتًا، ويمنع تكرارها.",
        "الفينوباربيتال يُحجز للخط الثالث لو فشل الفينيتوين، والأدوية الفموية (إيثوسكسيمايد وكاربامازيبين) ما تُستخدم أصلًا ب<bdi>case</bdi> <bdi>epilepsy</bdi> المستمر الإسعافية.",
    ],
    "when_changes": [
        "لو فشل الفينيتوين أيضًا بالسيطرة على النوبات، تصير الـ<bdi>step</bdi> التالية فينوباربيتال وريدي أو تخدير عام.",
        "لو النوبة توقفت بعد البنزوديازيبين الأول، لا حاجة لإضافة فينيتوين فورًا ويُراقب الـ<bdi>patient</bdi>.",
    ],
    "rule": "ب<bdi>case</bdi> <bdi>epilepsy</bdi> المستمر، لو فشل البنزوديازيبين الوريدي، الخط التالي هو الفينيتوين الوريدي.",
    "comparison": None,
    "guideline_note": None,
},
740: {
    "idea": "الـ<bdi>patient</bdi> ما تقدر تقفل عينها اليسرى مع عدم تناسق بالوجه وعدم القدرة على تجعيد الجبهة بنفس الجهة، وهذا يعني إصابة كاملة (علوي وسفلي) بالعصب الوجهي.",
    "clues": [
        ("unable to close her left eye", "ضعف عضلة إغلاق الجفن، وظيفة العصب الوجهي"),
        ("inability to wrinkle the left side of her forehead", "إصابة الجزء العلوي من الوجه أيضًا، يدل على إصابة محيطية كاملة للعصب"),
    ],
    "why_correct": [
        "العصب الوجهي (<bdi>facial nerve</bdi>) هو المسؤول عن كل عضلات تعابير الوجه، وإصابته المحيطية تسبب ضعف كامل بنصف الوجه (علوي وسفلي).",
        "عدم القدرة على تجعيد الجبهة مهم جدًا هنا لأنه يميز الإصابة المحيطية (تصيب كل الوجه) عن إصابة مركزية (تجنّب الجبهة عادة).",
        "الأعصاب الثانية المذكورة (البصري، الفكي العلوي، البصري) حسية أو خاصة بالرؤية، ما لها علاقة بحركة عضلات الوجه.",
    ],
    "when_changes": [
        "لو الجبهة كانت محفوظة (يقدر يجعّدها) مع ضعف أسفل الوجه بس، يصير الـ<bdi>diagnosis</bdi> إصابة مركزية (سكتة مثلًا) مو محيطية.",
        "لو صاحب الضعف ألم أذن وطفح جلدي، يصير الـ<bdi>diagnosis</bdi> متلازمة رامزي هانت.",
    ],
    "rule": "ضعف كامل بنصف الوجه (علوي وسفلي معًا) يدل على إصابة محيطية بالعصب الوجهي، بينما حفظ الجبهة يدل على إصابة مركزية.",
    "comparison": None,
    "guideline_note": None,
},
741: {
    "idea": "امرأة تعمل كاتبة (typist) عندها <bdi>paresthesia</bdi> بظهر اليد بمناطق الإبهام والسبابة والوسطى مع ضعف بسط الرسغ والأصابع، وهذا نمط يطابق إصابة العصب الكعبري لا الوسيط.",
    "clues": [
        ("pins and needles... on the dorsum of her left hand", "توزيع حسي بظهر اليد، منطقة العصب الكعبري"),
        ("weakness of wrist dorsiflexion and fingers extension", "ضعف بسط الرسغ والأصابع، وظيفة حركية مميزة للعصب الكعبري"),
    ],
    "why_correct": [
        "توزيع الـ<bdi>paresthesia</bdi> بظهر اليد مع ضعف بسط الرسغ والأصابع يطابق تمامًا إصابة العصب <bdi>radial</bdi> (أو فرعه العظمي بين العظام).",
        "هذا يختلف عن متلازمة النفق الرسغي (العصب الوسيط) اللي تصيب راحة اليد وضعف قبض/معارضة الإبهام مو بسط الرسغ.",
        "العمل ككاتبة يزيد <bdi>risk</bdi> ضغط متكرر على العصب الكعبري بمنطقة الساعد أو المرفق حسب وضعية اليد المتكررة.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>paresthesia</bdi> براحة اليد بأول 3 أصابع ونصف مع ضعف قبض الإبهام، يصير الـ<bdi>diagnosis</bdi> متلازمة النفق الرسغي (العصب الوسيط).",
        "لو الضعف بعضلات اليد الصغيرة مع <bdi>paresthesia</bdi> الخنصر، يصير الـ<bdi>diagnosis</bdi> إصابة العصب الزندي.",
    ],
    "rule": "<bdi>paresthesia</bdi> ظهر اليد مع ضعف بسط الرسغ والأصابع يشير لإصابة العصب الكعبري، بخلاف <bdi>paresthesia</bdi> الراحة اللي يشير للعصب الوسيط.",
    "comparison": None,
    "guideline_note": None,
},
742: {
    "idea": "<bdi>patient</bdi> عنده ضعف عضلي متقلب (<bdi>ptosis</bdi> وضعف عضلات قريبة) مع اختبار سيمبسون إيجابي وتحسن مع إدروفونيوم، وهذي صورة كلاسيكية للوهن العضلي الوبيل، والسؤال يبي الـ<bdi>treatment</bdi> الأنسب طويل المدى.",
    "clues": [
        ("bilateral ptosis and weakness of the proximal upper and lower limb muscles", "ضعف عضلي متقلب ومتماثل، نمط الوهن العضلي الوبيل"),
        ("positive Simpson test", "تفاقم <bdi>ptosis</bdi> مع التحديق المستمر، مميز للوهن العضلي"),
        ("Edrophonium test... transient improvement", "تحسن مؤقت مع مثبط كولينستراز، يؤكد الـ<bdi>diagnosis</bdi>"),
    ],
    "why_correct": [
        "<bdi>Pyridostigmine</bdi> هو الـ<bdi>treatment</bdi> الأول ل<bdi>disease</bdi> الوهن العضلي الوبيل لأنه مثبط كولينستراز لا يعبر حاجز الدم-الدماغ، فيتجنب <bdi>symptoms</bdi> جانبية مركزية.",
        "هذا يخليه الـ<bdi>treatment</bdi> الـ<bdi>chronic</bdi> الآمن اليومي بعكس أدوية ثانية مشابهة الآلية بس لها استخدامات مختلفة.",
        "الأشعة الصدرية الـ<bdi>normal</bdi> تستبعد وجود ورم غدة زعترية كبير بس ما تغيّر خطة الـ<bdi>treatment</bdi> الدوائي الأولي.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عنده تسمم أتروبين أو مضادات كولينية، يصير الفيزوستيجمين هو الـ<bdi>treatment</bdi> المناسب لأنه يعبر الحاجز الدموي الدماغي.",
        "لو كان الـ<bdi>diagnosis</bdi> <bdi>Alzheimer's disease</bdi> بدل الوهن العضلي، يصير الريفاستيجمين هو الخيار المناسب.",
    ],
    "rule": "بيريدوستيجمين هو الـ<bdi>treatment</bdi> الأول للوهن العضلي الوبيل لأنه لا يعبر حاجز الدم-الدماغ، بعكس أدوية أخرى من نفس المجموعة تُستخدم لحالات ثانية.",
    "comparison": {
        "headers": ["الدواء", "الاستخدام الرئيسي"],
        "rows": [
            ["<bdi>Pyridostigmine</bdi>", "الوهن العضلي الوبيل (لا يعبر الحاجز الدموي الدماغي)"],
            ["<bdi>Rivastigmine</bdi>", "<bdi>dementia</bdi> <bdi>Alzheimer's disease</bdi>"],
            ["<bdi>Physostigmine</bdi>", "تسمم الأتروبين/مضادات الكولين"],
            ["<bdi>Echothiophate</bdi>", "الجلوكوما موضعيًا"],
        ],
    },
    "guideline_note": None,
},
743: {
    "idea": "<bdi>patient</bdi> سكرية كبيرة بالسن وضغطها غير منضبط منذ فترة طويلة، تعاني دوخة عند الوقوف مع هبوط ضغط واضح لكن بدون زيادة بمعدل النبض التعويضي المتوقع، وهذا نمط يوجه لخلل بالجهاز العصبي المستقل.",
    "clues": [
        ("Sitting: 140/85... Standing: 115/80", "هبوط ضغط واضح عند الوقوف، يطابق هبوط ضغط وضعي"),
        ("Heart rate 95 /min (unchanged on standing)", "عدم زيادة النبض تعويضيًا رغم هبوط الضغط، غير <bdi>normal</bdi>"),
        ("poorly controlled long-standing type 2 diabetes", "مدة كافية لتطور اعتلال أعصاب مستقل <bdi>diabetes</bdi>"),
    ],
    "why_correct": [
        "<bdi>diabetes</bdi> طويل الأمد وغير المنضبط من أشيع <bdi>causes</bdi> اعتلال الجهاز العصبي المستقل (<bdi>autonomic neuropathy</bdi>)، اللي يعطل منعكس الباروريسبتور الـ<bdi>normal</bdi>.",
        "المفروض إن هبوط الضغط عند الوقوف يصاحبه زيادة بمعدل النبض تعويضيًا، وعدم حدوث هذا يدل على خلل بالقوس العصبي المستقل نفسه لا مجرد تأثير دواء.",
        "هذا النمط (هبوط ضغط وضعي بدون تسرّع قلب تعويضي) توقيع كلاسيكي ل<bdi>neuropathy</bdi> المستقل <bdi>diabetes</bdi>.",
    ],
    "when_changes": [
        "لو زاد معدل النبض بشكل <bdi>normal</bdi> تعويضيًا مع هبوط الضغط، يصير التفكير ب<bdi>cause</bdi> حجمي (جفاف أو نزيف) بدل <bdi>neuropathy</bdi> المستقل.",
        "لو الـ<bdi>patient</bdi> توقفت مؤخرًا عن دواء ضغط أو زادت جرعة الـ<bdi>atenolol</bdi>، يصير التأثير الدوائي احتمال أقوى.",
    ],
    "rule": "هبوط ضغط وضعي بدون تسارع قلب تعويضي ب<bdi>patient</bdi> <bdi>diabetes</bdi> طويل الأمد يوجه لاعتلال الجهاز العصبي المستقل.",
    "comparison": None,
    "guideline_note": None,
},
744: {
    "idea": "<bdi>patient</bdi> عندها متلازمة الألم الموضعي المعقد بعد عملية جراحية باليد، وشافها أخصائيون العظام والألم فعلًا، والسؤال يبي الـ<bdi>treatment</bdi> الأهم بعد كذا.",
    "clues": [
        ("complex regional pain syndrome", "<bdi>diagnosis</bdi> محدد له <bdi>treatment</bdi> أساسي معروف"),
        ("pain around her hand and wrist, which started after carpal tunnel release surgery", "بداية الألم بعد جراحة، نمط كلاسيكي لهذي المتلازمة"),
        ("reviewed by orthopaedics and a specialist in Pain Clinic", "استبعاد <bdi>causes</bdi> أخرى واستشارات تخصصية سابقة"),
    ],
    "why_correct": [
        "الـ<bdi>treatment</bdi> الفيزيائي (<bdi>physiotherapy</bdi>) هو حجر الأساس ب<bdi>treatment</bdi> متلازمة الألم الموضعي المعقد، لأنه يحافظ على حركة المفصل ويقلل الجمود والألم الـ<bdi>chronic</bdi>.",
        "الحركة المبكرة والتأهيل الوظيفي أثبتت فعاليتها أكثر من الاعتماد على المسكنات وحدها بهذي المتلازمة.",
        "المسكنات الأفيونية ما تحل المشكلة الأساسية وفيها <bdi>risk</bdi> إدمان، والتريبتان خاص ب<bdi>migraine</bdi> ما له علاقة هنا.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عندها <bdi>depression</bdi> أو <bdi>anxiety</bdi> <bdi>severe</bdi> مصاحب يعيق التأهيل، تصير الاستشارة النفسية <bdi>treatment</bdi> مساعد مهم بجانب الـ<bdi>treatment</bdi> الفيزيائي.",
        "لو الألم <bdi>severe</bdi> جدًا ويمنع بدء الـ<bdi>treatment</bdi> الفيزيائي، يمكن إضافة مسكنات مؤقتة لتسهيل المشاركة بالتأهيل.",
    ],
    "rule": "الـ<bdi>treatment</bdi> الفيزيائي هو الـ<bdi>treatment</bdi> الأساسي والأهم لمتلازمة الألم الموضعي المعقد.",
    "comparison": None,
    "guideline_note": None,
},
745: {
    "idea": "السؤال يختبر تحديد العصب المصاب اعتمادًا على العين اللي ما تقدر تُبعّد (abduct) أثناء النظر لجهة معينة، وهذا يدل على شلل بالعصب المُبعِد (السادس) بتلك العين.",
    "clues": [
        ("left eye turns towards the nose", "انحراف العين للداخل بالوضع الأمامي، يوحي بغلبة العضلة المقرّبة"),
        ("unable to abduct the left eye", "فشل تبعيد العين عند النظر لتلك الجهة، الـ<bdi>sign</bdi> المفتاحية لتحديد العصب المصاب"),
        ("double vision worsens", "ازدواج الرؤية يزيد كلما احتاج الـ<bdi>patient</bdi> يستخدم العضلة الضعيفة أكثر"),
    ],
    "why_correct": [
        "العضلة المبعِّدة للعين (<bdi>lateral rectus</bdi>) يغذيها العصب السادس (المُبعِد)، وفشل تبعيد العين عند النظر لجهة معينة هو الـ<bdi>sign</bdi> التشخيصية المباشرة لشلل هذا العصب.",
        "انحراف العين للداخل بالوضع الأمامي (بدون معارضة العضلة المقرّبة) يزيد الشك بضعف العضلة المبعّدة المقابلة لها.",
        "بحسب مفتاح الملف، القاعدة الأساسية المطلوبة هنا هي ربط فشل التبعيد بالعصب السادس تحديدًا لا الثالث، بغض النظر عن أي التباس بتحديد الجهة أثناء الفحص.",
    ],
    "when_changes": [
        "لو كان الخلل بتقريب العين (adduction) بدل تبعيدها مع <bdi>ptosis</bdi> وتوسع حدقة، يصير الـ<bdi>diagnosis</bdi> شلل العصب الثالث بدل السادس.",
        "لو صاحب الشلل ألم <bdi>severe</bdi> مفاجئ وتوسع حدقة غير متفاعلة، يوجه الشك لتمدد وعائي ضاغط على العصب الثالث.",
    ],
    "rule": "فشل تبعيد العين عند النظر لجهة معينة هو الـ<bdi>sign</bdi> المفتاحية ل<bdi>diagnosis</bdi> شلل العصب السادس (المُبعِد) في تلك العين.",
    "comparison": None,
    "guideline_note": "وصف الـ<bdi>case</bdi> بالسؤال (انحراف العين اليسرى للداخل وفشل تبعيدها) يطابق طبيًا شلل عصب سادس يسار، بينما مفتاح إجابة الملف الأصلي يحدد <bdi>Right 6th</bdi>. يبدو هذا تعارض ظاهري بمفتاح الملف نفسه (احتمال خطأ كتابي بالجهة)، وبما إن قاعدة العمل تعتمد جواب الملف دايمًا، خلّينا <bdi>Right 6th</bdi> هو الجواب المعتمد بالبطاقة.",
},
746: {
    "idea": "رجل منتصف العمر صار عنده تغيّر شخصية وسلوك (تهيّج وانتقاد الكل) قبل أي مشكلة بالذاكرة، مع صعوبة بدء الكلام وتوقف بمنتصف الجملة، وهذا النمط السلوكي المبكر يوجه ل<bdi>dementia</bdi> الفص الجبهي الصدغي.",
    "clues": [
        ("irritable and criticizes everyone at home", "تغيّر شخصية وسلوك بارز، سمة أساسية لهذا النوع من الـ<bdi>dementia</bdi>"),
        ("difficulty initiating conversation and even pauses halfway through sentences", "صعوبة كلامية وتنفيذية، من <bdi>symptoms</bdi> إصابة الفص الجبهي"),
        ("no family history of note", "لا يستبعد الـ<bdi>diagnosis</bdi>، فهو أشيع بدون تاريخ عائلي واضح"),
    ],
    "why_correct": [
        "تغيّر الشخصية والسلوك (تهيّج، فقدان لباقة، انتقاد الآخرين) كأول وأبرز <bdi>symptom</bdi> قبل أي مشكلة ذاكرة يطابق <bdi>frontotemporal dementia</bdi> النمط السلوكي.",
        "صعوبة بدء الكلام والتوقف بمنتصف الجملة يعكس إصابة الفص الجبهي المسؤول عن الطلاقة الكلامية والتخطيط التنفيذي.",
        "<bdi>dementia</bdi> <bdi>Alzheimer's disease</bdi> يبدأ عادة بمشكلة ذاكرة أولًا، والـ<bdi>dementia</bdi> الوعائي يحتاج تاريخ أوعية دموية أو سكتات، وهنتنغتون يصاحبه حركات لا إرادية وتاريخ عائلي.",
    ],
    "when_changes": [
        "لو بدأت الـ<bdi>symptoms</bdi> بفقدان ذاكرة تدريجي قبل أي تغيّر بالشخصية، يميل الـ<bdi>diagnosis</bdi> لل<bdi>Alzheimer's disease</bdi>.",
        "لو صاحبت الـ<bdi>symptoms</bdi> حركات كوريّة لا إرادية مع تاريخ عائلي واضح، يصير الـ<bdi>diagnosis</bdi> الأرجح هنتنغتون.",
    ],
    "rule": "تغيّر الشخصية والسلوك كأول <bdi>symptom</bdi> بارز قبل مشكلة الذاكرة يوجه ل<bdi>dementia</bdi> الفص الجبهي الصدغي.",
    "comparison": None,
    "guideline_note": None,
},
747: {
    "idea": "<bdi>patient</bdi> كبير بالسن سبق له عملية على الرقبة ب<bdi>cause</bdi> اعتلال نخاعي عنقي تنكسي، وصار عنده تدهور جديد بالمشي وإلحاح بولي، وهذا يوحي بتكرار أو تفاقم نفس الـ<bdi>disease</bdi> التنكسي.",
    "clues": [
        ("previous cervical laminectomy for degenerative cervical myelopathy", "تاريخ مرضي وجراحي سابق بنفس المشكلة"),
        ("worsening gait instability and urinary urgency", "<bdi>symptoms</bdi> نخاعية جديدة تطابق تفاقم الـ<bdi>disease</bdi> السابق"),
    ],
    "why_correct": [
        "ب<bdi>patient</bdi> له تاريخ مؤكد باعتلال نخاعي عنقي تنكسي وعملية سابقة، ظهور نفس نمط الـ<bdi>symptoms</bdi> (مشي وإلحاح بولي) يوجه أولًا لتكرار أو تفاقم نفس الـ<bdi>disease</bdi> التنكسي.",
        "التنكس الفقري <bdi>disease</bdi> <bdi>chronic</bdi> تقدمي ممكن يستمر أو يتكرر حتى بعد جراحة تخفيف الضغط السابقة.",
        "الـ<bdi>causes</bdi> الأخرى (تصلب متعدد، التهاب نخاع مستعرض، متلازمة ذيل الفرس) أقل احتمالًا هنا مقارنة بالـ<bdi>cause</bdi> المعروف والمباشر المرتبط بتاريخه المرضي.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>symptoms</bdi> <bdi>acute</bdi> ومصحوبة بألم <bdi>severe</bdi> مفاجئ وخلل حسي بمستوى واضح، يميل الـ<bdi>diagnosis</bdi> لالتهاب نخاع مستعرض.",
        "لو صاحب الـ<bdi>symptoms</bdi> خدر بمنطقة السرج وضعف بالساقين مع احتباس بولي <bdi>acute</bdi>، يصير الـ<bdi>diagnosis</bdi> متلازمة ذيل الفرس.",
    ],
    "rule": "ب<bdi>patient</bdi> له تاريخ اعتلال نخاعي عنقي تنكسي، تكرار أو تفاقم نفس الـ<bdi>symptoms</bdi> يوجه أولًا لعودة أو تطور نفس الـ<bdi>disease</bdi> قبل التفكير ب<bdi>causes</bdi> أخرى.",
    "comparison": None,
    "guideline_note": None,
},
748: {
    "idea": "<bdi>patient</bdi> مشخّص باعتلال نخاعي عنقي تنكسي، تأخر موعده ب<bdi>cause</bdi> مشكلة قلبية، ولسه عنده <bdi>symptoms</bdi> عصبية مستمرة، والسؤال يبي أهم <bdi>step</bdi> تالية لمنع ضرر دائم.",
    "clues": [
        ("diagnosed with degenerative cervical myelopathy", "<bdi>diagnosis</bdi> مؤكد ل<bdi>disease</bdi> تقدمي يؤثر على النخاع الشوكي"),
        ("mentions his ongoing neurological symptoms", "استمرار الـ<bdi>symptoms</bdi> العصبية، يعني الـ<bdi>disease</bdi> ما زال نشط"),
    ],
    "why_correct": [
        "الـ<bdi>myelopathy</bdi> العنقي التنكسي <bdi>disease</bdi> جراحي بطبيعته، والتأخير بالتحويل للجراحة يزيد <bdi>risk</bdi> ضرر عصبي دائم لا يمكن الرجوع فيه.",
        "أهم <bdi>step</bdi> تالية هي <bdi>refer to spinal surgery</bdi> بأسرع وقت، خصوصًا مع استمرار الـ<bdi>symptoms</bdi> رغم تأخر الـ<bdi>follow-up</bdi>.",
        "الـ<bdi>treatment</bdi> الفيزيائي أو مسكنات الألم العصبي <bdi>treatment</bdi> داعم بس ما يوقف تطور الضغط على النخاع الشوكي، والطمأنة غير مناسبة مع <bdi>symptoms</bdi> مستمرة فعلية.",
    ],
    "when_changes": [
        "لو تحسنت الـ<bdi>symptoms</bdi> تمامًا وأصبح الفحص <bdi>normal</bdi>، يمكن الاكتفاء بالـ<bdi>follow-up</bdi> الدورية بدون إحالة عاجلة.",
        "لو كانت الـ<bdi>symptoms</bdi> بسيطة جدًا ومستقرة تمامًا لفترة طويلة، يمكن البدء ب<bdi>treatment</bdi> محافظ مع مراقبة دقيقة قبل الجراحة.",
    ],
    "rule": "الـ<bdi>myelopathy</bdi> العنقي التنكسي المستمر الـ<bdi>symptoms</bdi> يحتاج إحالة عاجلة لجراحة العمود الفقري لمنع ضرر عصبي دائم.",
    "comparison": None,
    "guideline_note": None,
},
749: {
    "idea": "<bdi>patient</bdi> <bdi>diabetes</bdi> وضغط عنده ضعف مفاجئ بنصف الجسم مع شلل وجهي من النوع العلوي، وهذا يوحي بسكتة دماغية <bdi>acute</bdi>، والسؤال يبي أول <bdi>step</bdi> قبل أي <bdi>treatment</bdi>.",
    "clues": [
        ("sudden onset left sided body weakness for 4 hours", "بداية مفاجئة و<bdi>acute</bdi>، خلال نافذة الـ<bdi>treatment</bdi> الـ<bdi>acute</bdi> للسكتة"),
        ("left sided upper motor neuron facial palsy and left sided hemiparesis", "نمط سكتة دماغية مركزية كلاسيكي"),
    ],
    "why_correct": [
        "أي شك بسكتة دماغية <bdi>acute</bdi> لازم يبدأ بـ<bdi>brain CT scan</bdi> فورًا لتحديد نوعها (إقفارية أم نزفية) قبل أي <bdi>treatment</bdi>.",
        "إعطاء <bdi>aspirin</bdi> أو كلوبيدوجريل قبل استبعاد النزيف <bdi>risk</bdi> جدًا لأنه يزيد النزيف لو كانت السكتة نزفية.",
        "الرنين المغناطيسي أدق أحيانًا بس أبطأ وأقل توفرًا بالطوارئ مقارنة بالأشعة المقطعية اللي تعطي إجابة سريعة كافية لاتخاذ القرار العلاجي الأولي.",
    ],
    "when_changes": [
        "لو أكدت الأشعة المقطعية إقفار وكان الـ<bdi>patient</bdi> ضمن نافذة الـ<bdi>treatment</bdi> الـ<bdi>acute</bdi>، تصير الـ<bdi>step</bdi> التالية النظر بإعطاء <bdi>treatment</bdi> حال للتخثر.",
        "لو أظهرت الأشعة نزيف، يتغير المسار العلاجي بالكامل نحو السيطرة على الضغط ومنع تمدد النزيف.",
    ],
    "rule": "أي اشتباه بسكتة دماغية <bdi>acute</bdi> يبدأ بأشعة مقطعية للدماغ فورًا قبل أي <bdi>treatment</bdi> دوائي.",
    "comparison": None,
    "guideline_note": None,
},
750: {
    "idea": "مراهق عنده ضعف تصاعدي متماثل بعد عدوى تنفسية قبل أسبوعين، مع غياب منعكسات وحس سليم وعدم استقرار بالـ<bdi>signs</bdi> الحيوية، وهذي الصورة الكلاسيكية لمتلازمة غيلان باريه.",
    "clues": [
        ("upper respiratory infection 2 weeks ago", "عدوى سابقة، محفز معروف لمتلازمة غيلان باريه"),
        ("symmetrical weakness of the face and all four extremities", "ضعف تصاعدي متماثل، نمط مميز للمتلازمة"),
        ("Deep tendon reflexes are absent, and sensations are intact", "غياب منعكسات مع حس سليم، توقيع كلاسيكي"),
        ("breathing is slow and shallow... heart rate and blood pressure are fluctuant", "إصابة عضلات تنفسية وخلل عصبي مستقل، <bdi>complications</bdi> خطيرة معروفة بالمتلازمة"),
    ],
    "why_correct": [
        "ضعف تصاعدي متماثل بعد عدوى تنفسية مع غياب المنعكسات وسلامة الحس هو التوقيع الكلاسيكي لمتلازمة <bdi>Guillain-Barre</bdi>.",
        "إصابة عضلات التنفس وعدم استقرار الضغط والنبض تعكس تأثر الجهاز العصبي المستقل والعضلات التنفسية، وهذي <bdi>complication</bdi> خطيرة معروفة بالمتلازمة تحتاج مراقبة دقيقة.",
        "الوهن العضلي الوبيل يعطي ضعف متقلب بدون غياب منعكسات، والتهاب النخاع المستعرض يعطي مستوى حسي واضح، وهذا غير موجود هنا.",
    ],
    "when_changes": [
        "لو كان الضعف يتحسن بالراحة ويسوء بالجهد المتكرر بدون غياب منعكسات، يصير الـ<bdi>diagnosis</bdi> الأرجح وهن عضلي وبيل.",
        "لو صاحب الضعف مستوى حسي واضح واحتباس بولي، يميل الـ<bdi>diagnosis</bdi> لالتهاب النخاع المستعرض.",
    ],
    "rule": "ضعف تصاعدي متماثل بعد عدوى مع غياب المنعكسات وسلامة الحس يشخّص متلازمة غيلان باريه.",
    "comparison": None,
    "guideline_note": None,
},
751: {
    "idea": "<bdi>patient</bdi> عنده صداع عنقودي كلاسيكي (نوبات بنفس الوقت يوميًا مع دماع واحمرار عين)، والسؤال يبي الدواء المناسب للوقاية من النوبات مو <bdi>treatment</bdi> النوبة الـ<bdi>acute</bdi>.",
    "clues": [
        ("occurred at the same time each day, about 2 a.m.", "نمط توقيت ثابت يوميًا، مميز جدًا للصداع العنقودي"),
        ("last around 30 minutes", "مدة قصيرة نسبيًا، تطابق الصداع العنقودي"),
        ("lacrimation and redness of the right eye", "<bdi>symptoms</bdi> مصاحبة نباتية بالعين بنفس الجهة، مميزة لهذا النوع"),
    ],
    "why_correct": [
        "<bdi>Verapamil</bdi> هو الدواء الأول للوقاية من نوبات الصداع العنقودي على المدى الطويل.",
        "النمط الزمني المنتظم (نفس الوقت يوميًا) مع الـ<bdi>symptoms</bdi> النباتية بالعين (دماع واحمرار) نموذج كلاسيكي للصداع العنقودي يحتاج <bdi>treatment</bdi> وقائي مو بس <bdi>treatment</bdi> نوبة.",
        "الأكسجين والسوماتريبتان علاجات للنوبة الـ<bdi>acute</bdi> نفسها وقت حدوثها، مو للوقاية من تكرارها.",
    ],
    "when_changes": [
        "لو السؤال يبي أسرع <bdi>treatment</bdi> للنوبة الـ<bdi>acute</bdi> وقت حدوثها، يصير الجواب الأكسجين 100% أو السوماتريبتان.",
        "لو كان الصداع نصفي الطابع (نابض، مصحوب بغثيان وحساسية للضوء) بدل عنقودي، يصير الـ<bdi>propranolol</bdi> هو خيار الوقاية الأنسب.",
    ],
    "rule": "فيراباميل هو الـ<bdi>treatment</bdi> الوقائي الأول للصداع العنقودي، بينما الأكسجين والسوماتريبتان ل<bdi>treatment</bdi> النوبة الـ<bdi>acute</bdi> فقط.",
    "comparison": None,
    "guideline_note": None,
},
752: {
    "idea": "<bdi>patient</bdi> <bdi>diabetes</bdi> وضغط عنده شلل جزئي بالعصب الثالث (<bdi>ptosis</bdi> وضعف بحركات العين المختلفة) مع سلامة تامة للحدقة، وهذا النمط (حفظ الحدقة) يميّز شلل العصب الثالث <bdi>diabetes</bdi> عن الـ<bdi>causes</bdi> الضاغطة.",
    "clues": [
        ("ptosis, limited adduction, elevation, and depression of the right eye", "شلل جزئي بالعصب الثالث يصيب أغلب عضلات العين"),
        ("The pupils are equal and reactive in both sides", "سلامة تامة بحركة الحدقة، <bdi>sign</bdi> مفتاحية تميز الـ<bdi>cause</bdi> <bdi>diabetes</bdi> عن الضاغط"),
        ("diabetes and hypertension", "<bdi>factors</bdi> <bdi>risk</bdi> وعائية تدعم <bdi>cause</bdi> نقص تروية العصب"),
    ],
    "why_correct": [
        "شلل العصب الثالث <bdi>diabetes</bdi> (<bdi>diabetic third nerve neuropathy</bdi>) كلاسيكيًا يصيب الألياف الحركية بس ويحفظ الألياف السمبثاوية الحدقية اللي تكون بالمحيط الخارجي للعصب.",
        "هذا يفسر <bdi>cause</bdi> سلامة الحدقة رغم شلل واضح بحركات العين، وهذا التمييز مهم جدًا سريريًا.",
        "أم الدم بالشريان الموصل الخلفي كلاسيكيًا تضغط على الألياف الحدقية الخارجية أول شي وتسبب توسع حدقة وعدم تفاعلها، وهذا غير موجود هنا.",
    ],
    "when_changes": [
        "لو كانت الحدقة متوسعة وغير متفاعلة مع الشلل، يصير الـ<bdi>cause</bdi> الأرجح أم دم ضاغطة بالشريان الموصل الخلفي وتحتاج تصوير عاجل.",
        "لو صاحب الشلل إصابة أعصاب ثانية متعددة (الرابع والسادس) مع جحوظ، يصير الـ<bdi>diagnosis</bdi> الأرجح التهاب الجيب الكهفي.",
    ],
    "rule": "شلل العصب الثالث مع حفظ الحدقة (equal and reactive) يوجه ل<bdi>cause</bdi> <bdi>diabetes</bdi> نقص تروية، بينما توسع الحدقة يوجه ل<bdi>cause</bdi> ضاغط مثل أم الدم.",
    "comparison": None,
    "guideline_note": None,
},
753: {
    "idea": "<bdi>patient</bdi> <bdi>epilepsy</bdi> ب<bdi>case</bdi> <bdi>epilepsy</bdi> مستمر (نوبات متكررة ووعي غائب)، وبعد تأمين الطريق الهوائي والأكسجين، السؤال يبي أول دواء وريدي يُعطى.",
    "clues": [
        ("repeated tonic-clonic seizures at home", "نوبات متكررة، يوحي ب<bdi>case</bdi> <bdi>epilepsy</bdi> مستمر"),
        ("unconscious and continuously convulsing", "<bdi>case</bdi> إسعافية نشطة تحتاج تدخل فوري"),
        ("After oxygenation and securing the airway", "الخطوات الأولية (الطريق الهوائي والأكسجين) تمت، الآن دور الدواء"),
    ],
    "why_correct": [
        "الخط الأول العلاجي ب<bdi>case</bdi> <bdi>epilepsy</bdi> المستمر بعد تأمين الطريق الهوائي هو بنزوديازيبين وريدي مثل <bdi>diazepam</bdi>.",
        "البنزوديازيبين يوقف النشاط الكهربائي الزائد بسرعة نسبية ويعتبر الـ<bdi>step</bdi> الدوائية الأولى المعتمدة عالميًا.",
        "الفينيتوين والفينوباربيتال أدوية الخط الثاني والثالث بعد فشل البنزوديازيبين، والثيوبنتال يُحجز لحالات مقاومة تحت تخدير كامل.",
    ],
    "when_changes": [
        "لو ما استجاب الـ<bdi>patient</bdi> للبنزوديازيبين خلال دقائق، تصير الـ<bdi>step</bdi> التالية فينيتوين وريدي.",
        "لو استمرت النوبات رغم الفينيتوين، يصير التفكير بفينوباربيتال أو تخدير عام تحت مراقبة مركزة.",
    ],
    "rule": "بعد تأمين الطريق الهوائي ب<bdi>case</bdi> <bdi>epilepsy</bdi> المستمر، البنزوديازيبين الوريدي هو الدواء الأول المعطى.",
    "comparison": None,
    "guideline_note": None,
},
754: {
    "idea": "السؤال يبي أفضل <bdi>treatment</bdi> لمتلازمة غيلان باريه، وهنا نقطة تعليمية مهمة إن الستيرويد ما يفيد بهذا الـ<bdi>disease</bdi> بعكس أغلب <bdi>diseases</bdi> المناعة الذاتية الثانية.",
    "clues": [
        ("Guillain Barre Syndrome", "<bdi>diagnosis</bdi> محدد له علاجات نوعية مثبتة"),
    ],
    "why_correct": [
        "<bdi>Plasmapheresis</bdi> (فصادة البلازما) من العلاجات المثبتة فعاليتها بمتلازمة غيلان باريه، إلى جانب الغلوبولين المناعي الوريدي.",
        "نقطة تعليمية مهمة: الستيرويد أثبتت الدراسات إنه غير فعال بهذا الـ<bdi>disease</bdi> تحديدًا، بعكس <bdi>diseases</bdi> مناعية ذاتية عصبية ثانية كثيرة يكون فيها الستيرويد الخط الأول.",
        "السيكلوسبورين والسيكلوفوسفامايد أدوية مناعية ثانية ما لها دور مثبت ب<bdi>treatment</bdi> غيلان باريه.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>diagnosis</bdi> التهاب عصبي مزيل للميالين <bdi>chronic</bdi> (CIDP) بدل غيلان باريه الـ<bdi>acute</bdi>، يصير الستيرويد خيار علاجي فعال هناك.",
        "لو ما توفرت فصادة البلازما، يصير الغلوبولين المناعي الوريدي هو البديل المعادل بالفعالية.",
    ],
    "rule": "<bdi>treatment</bdi> متلازمة غيلان باريه هو فصادة البلازما أو الغلوبولين المناعي الوريدي، والستيرويد غير فعّال بهذا الـ<bdi>disease</bdi> تحديدًا.",
    "comparison": None,
    "guideline_note": None,
},
755: {
    "idea": "<bdi>patient</bdi> شابة عندها التهاب عصب بصري بعين واحدة مع <bdi>symptoms</bdi> عصبية بمناطق مختلفة تمامًا (وجه وساقين)، وهذا التشتت بالمكان يوجه لتصلب متعدد، والفحص الأدق لإثبات ذلك تصوير الدماغ والنخاع بالرنين.",
    "clues": [
        ("pain in the right eye associated progressive visual loss", "التهاب عصب بصري مؤلم، <bdi>symptom</bdi> شائع ب<bdi>multiple sclerosis</bdi>"),
        ("numbness in the left side of the face and weakness in both lower limbs", "إصابات بمناطق عصبية مختلفة تمامًا، تشتت بالمكان"),
        ("weakness, clasp knife rigidity, hyperreflexia", "<bdi>signs</bdi> عصبون حركي علوي بالساقين، يوحي بإصابة نخاعية"),
    ],
    "why_correct": [
        "وجود إصابات بمناطق عصبية متعددة ومختلفة (عصب بصري، وجه، نخاع شوكي) بنفس الـ<bdi>patient</bdi> يوحي ب<bdi>disease</bdi> مزيل للميالين منتشر بالمكان.",
        "<bdi>Brain and spine MRI</bdi> هو الفحص الأعلى قيمة تشخيصية لأنه يُظهر آفات إزالة الميالين المتعددة بالدماغ والنخاع، وهذا أساس <bdi>diagnosis</bdi> <bdi>multiple sclerosis</bdi>.",
        "تخطيط العضل والأعصاب يفحص الأعصاب الطرفية والعضلات، وهذا <bdi>disease</bdi> بالجهاز العصبي المركزي، فما يفيد هنا.",
    ],
    "when_changes": [
        "لو كانت الإصابة محصورة بعصب طرفي واحد فقط، يصير تخطيط الأعصاب هو الفحص الأنسب.",
        "لو الشك بورم أو انضغاط نخاعي محدد بمكان واحد بدل تشتت بالمكان، تصير الأشعة المقطعية الموجهة كافية أحيانًا.",
    ],
    "rule": "تشتت الإصابات العصبية بأماكن مختلفة (عصب بصري وجذع دماغ ونخاع) يوجه لتصلب متعدد، وأفضل فحص لإثباته رنين مغناطيسي للدماغ والنخاع.",
    "comparison": None,
    "guideline_note": None,
},
756: {
    "idea": "<bdi>patient</bdi> كبير بالسن عنده ثلاثية كلاسيكية: صعوبة مشي واحتباس بولي وتدهور إدراكي، مع تمدد بطينات الدماغ بالأشعة، وهذا يطابق استسقاء الدماغ بضغط <bdi>normal</bdi>.",
    "clues": [
        ("progressive gait disturbance and incontinence", "اثنين من الثلاثية الكلاسيكية"),
        ("forgetful, confused, and withdrawn", "العنصر الثالث بالثلاثية: تدهور إدراكي"),
        ("dilated ventricles", "تمدد بطينات الدماغ، الـ<bdi>sign</bdi> التصويرية المميزة"),
    ],
    "why_correct": [
        "الثلاثية الكلاسيكية (اضطراب مشي، سلس بولي، تدهور إدراكي) مع تمدد البطينات بالأشعة تطابق تمامًا <bdi>normal-pressure hydrocephalus</bdi>.",
        "هذا الـ<bdi>diagnosis</bdi> مهم لأنه من <bdi>causes</bdi> الـ<bdi>dementia</bdi> القابلة لل<bdi>treatment</bdi> الجراحي (تحويلة تصريف السائل الدماغي الشوكي).",
        "<bdi>Alzheimer's disease</bdi> والـ<bdi>dementia</bdi> الجبهي الصدغي ما يعطون تمدد بطينات بارز كسمة أساسية، والصورة السريرية هنا مختلفة تمامًا عنهم.",
    ],
    "when_changes": [
        "لو كان التدهور سريع جدًا خلال أسابيع مع رمع عضلي واضح، يميل الـ<bdi>diagnosis</bdi> ل<bdi>disease</bdi> كروتزفيلد جاكوب.",
        "لو بدأت الـ<bdi>symptoms</bdi> بفقدان ذاكرة تدريجي بدون اضطراب مشي أو سلس بولي مبكر، يصير الـ<bdi>diagnosis</bdi> الأرجح <bdi>Alzheimer's disease</bdi>.",
    ],
    "rule": "ثلاثية اضطراب المشي والسلس البولي والتدهور الإدراكي مع تمدد بطينات الدماغ تشخّص استسقاء الدماغ بضغط <bdi>normal</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
757: {
    "idea": "<bdi>patient</bdi> كتب رغبته بعدم الإنعاش وهو ب<bdi>case</bdi> حرجة، وتم احترام رغبته المكتوبة، والابن اعترض معتبرًا والده ما كان أهل لاتخاذ القرار. السؤال يبي أول <bdi>step</bdi> إجرائية مناسبة قبل الرد على اعتراض الابن.",
    "clues": [
        ("managed to write in the bed clothes that he wants to die in peace", "تعبير الـ<bdi>patient</bdi> عن رغبته بنفسه، أساس احترام الاستقلالية"),
        ("His son was very angry", "اعتراض من طرف يدّعي صلة قرابة، يستدعي التحقق أولًا من صفته الرسمية"),
    ],
    "why_correct": [
        "قبل الدخول بنقاش أخلاقي أو قانوني مع أي طرف يعترض على قرار طبي، الـ<bdi>step</bdi> الإجرائية الأولى هي التأكد من صفته الرسمية كأقرب الأقارب أو الوصي الشرعي.",
        "التحقق من هوية الابن كولي أمر فعلي (<bdi>next of kin</bdi>) يحدد مدى أحقيته بالنقاش بتفاصيل القرار الطبي والوصول للمعلومات أصلًا.",
        "هذي <bdi>step</bdi> تمهيدية مهمة قبل أي شرح أو دفاع عن القرار الطبي المتخذ بناء على رغبة الـ<bdi>patient</bdi> الموثّقة.",
    ],
    "when_changes": [
        "لو تأكدنا إن الابن هو فعلًا أقرب الأقارب الشرعي، تصير الـ<bdi>step</bdi> التالية توضيح إن الفريق الطبي احترم رغبة والده الموثّقة بشفافية وتعاطف.",
        "لو تبين إن الابن ليس له صفة قانونية بالوصاية أو القرابة المباشرة، يتغير مستوى الإفصاح المسموح به له من الناحية القانونية.",
    ],
    "rule": "عند اعتراض أي طرف على قرار طبي متعلق ب<bdi>patient</bdi> متوفى أو حرج، الـ<bdi>step</bdi> الأولى المناسبة هي التحقق من صفته الرسمية كأقرب الأقارب قبل أي نقاش أخلاقي أو تفصيلي.",
    "comparison": None,
    "guideline_note": None,
},
758: {
    "idea": "امرأة شابة انهارت عاطفيًا عند تبليغها ب<bdi>diagnosis</bdi> <bdi>multiple sclerosis</bdi>، والسؤال يبي أنسب عبارة تعبّر عن تعاطف حقيقي بدون تجاهل مشاعرها أو تطمين كاذب.",
    "clues": [
        ("emotional breakdown during breaking bad news", "رد فعل عاطفي <bdi>normal</bdi> متوقع عند تبليغ خبر صعب"),
    ],
    "why_correct": [
        "عبارة \"أشاركك شعورك وسأدعمك\" تعكس تعاطف حقيقي واعتراف بمشاعر الـ<bdi>patient</bdi> مع التزام واضح بالدعم المستمر.",
        "التعاطف الحقيقي يعني الاعتراف بصعوبة الموقف والوقوف مع الـ<bdi>patient</bdi>، مو إعطاء نصيحة جافة أو تطمين غير واقعي.",
        "هذا النوع من الرد يبني ثقة ويفتح المجال لل<bdi>patient</bdi> تعبّر عن مخاوفها بدون خوف من الحكم عليها.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> طلبت معلومات عملية أكثر عن خطة الـ<bdi>treatment</bdi> بدل الدعم العاطفي، يصير التركيز على شرح واضح ومباشر للخطوات القادمة.",
        "لو كانت الـ<bdi>patient</bdi> هادئة ومستقرة عاطفيًا، يمكن الانتقال مباشرة لمناقشة خطة الـ<bdi>treatment</bdi> دون الحاجة لعبارات دعم مطوّلة.",
    ],
    "rule": "التعاطف الحقيقي عند تبليغ خبر صعب يعني الاعتراف بمشاعر الـ<bdi>patient</bdi> والالتزام بالدعم، لا التطمين الكاذب ولا النصيحة الجافة.",
    "comparison": None,
    "guideline_note": None,
},
759: {
    "idea": "<bdi>patient</bdi> كبير بالسن عنده صورة <bdi>parkinsonism</bdi> مع <bdi>dementia</bdi> مبكر وتذبذب واضح بالوعي والإدراك مع هلاوس بصرية، وهذا الثلاثي المميز يطابق <bdi>dementia</bdi> أجسام ليوي.",
    "clues": [
        ("Parkinsonism, early dementia", "<bdi>dementia</bdi> يبدأ قريب من أو مع بداية الـ<bdi>symptoms</bdi> الحركية، مو متأخر"),
        ("fluctuations in cognition", "تذبذب بالوعي والإدراك، <bdi>sign</bdi> مميزة"),
        ("visual hallucinations", "هلاوس بصرية، من المعايير الأساسية لهذا الـ<bdi>dementia</bdi>"),
    ],
    "why_correct": [
        "اجتماع الـ<bdi>parkinsonism</bdi> مع <bdi>dementia</bdi> مبكر (قريب من بداية الـ<bdi>symptoms</bdi> الحركية) مع تذبذب الإدراك والهلاوس البصرية هو المعايير الأساسية ل<bdi>diagnosis</bdi> <bdi>dementia with Lewy bodies</bdi>.",
        "ب<bdi>disease</bdi> <bdi>Parkinson's disease</bdi> الأصلي، الـ<bdi>dementia</bdi> عادة يظهر متأخر (بعد سنة أو أكثر من بداية الـ<bdi>symptoms</bdi> الحركية)، وهذا يخالف الصورة هنا.",
        "الهلاوس البصرية المبكرة والتذبذب الواضح بالإدراك مو سمة أساسية ب<bdi>Alzheimer's disease</bdi> ولا بمتلازمة كورتيكوباسال.",
    ],
    "when_changes": [
        "لو ظهر الـ<bdi>dementia</bdi> بعد أكثر من سنة من بداية <bdi>symptoms</bdi> <bdi>Parkinson's disease</bdi> الحركية، يصير الـ<bdi>diagnosis</bdi> الأنسب <bdi>dementia</bdi> مرتبط ب<bdi>Parkinson's disease</bdi>.",
        "لو كانت السمة الأساسية فقدان ذاكرة تدريجي بدون تذبذب أو هلاوس، يميل الـ<bdi>diagnosis</bdi> لل<bdi>Alzheimer's disease</bdi>.",
    ],
    "rule": "<bdi>parkinsonism</bdi> مع <bdi>dementia</bdi> مبكر وتذبذب بالإدراك وهلاوس بصرية يشخّص <bdi>dementia</bdi> أجسام ليوي.",
    "comparison": None,
    "guideline_note": None,
},
760: {
    "idea": "<bdi>patient</bdi> كبير جدًا بالسن عنده فقدان ذاكرة وصعوبة تعرف على أقاربه بدون <bdi>factors</bdi> <bdi>risk</bdi> قلبية وعائية، والسؤال يبي الـ<bdi>cause</bdi> الأشيع لل<bdi>dementia</bdi> بشكل عام.",
    "clues": [
        ("memory loss and difficulty recognizing his grandsons", "فقدان ذاكرة تدريجي واضح، سمة أساسية"),
        ("no cardiovascular risk factors", "يبعد كون الـ<bdi>cause</bdi> وعائي (نوبات إقفارية متعددة)"),
    ],
    "why_correct": [
        "<bdi>disease</bdi> <bdi>Alzheimer's disease</bdi> هو الـ<bdi>cause</bdi> الأشيع لل<bdi>dementia</bdi> عمومًا بكبار السن، خصوصًا لو ما فيه <bdi>factors</bdi> <bdi>risk</bdi> وعائية تدعم <bdi>cause</bdi> ثاني.",
        "فقدان الذاكرة التدريجي وصعوبة التعرف على الأقارب سمات كلاسيكية مبكرة ب<bdi>Alzheimer's disease</bdi>.",
        "غياب <bdi>factors</bdi> الـ<bdi>risk</bdi> القلبية الوعائية يقلل احتمال الـ<bdi>dementia</bdi> متعدد الاحتشاءات ك<bdi>cause</bdi> رئيسي هنا.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> عنده تاريخ سكتات متكررة و<bdi>factors</bdi> <bdi>risk</bdi> وعائية واضحة، يصير الـ<bdi>diagnosis</bdi> الأرجح <bdi>dementia</bdi> متعدد الاحتشاءات.",
        "لو كان هناك تاريخ إدمان كحول طويل الأمد، يصير التفكير باعتلال دماغي كحولي.",
    ],
    "rule": "<bdi>disease</bdi> <bdi>Alzheimer's disease</bdi> هو الـ<bdi>cause</bdi> الأشيع لل<bdi>dementia</bdi> بشكل عام بكبار السن، خصوصًا بغياب <bdi>factors</bdi> <bdi>risk</bdi> وعائية.",
    "comparison": None,
    "guideline_note": None,
},
761: {
    "idea": "<bdi>patient</bdi> مسنة عندها انسداد شمع بالأذنين وتستخدم سماعات، وفحص التوليف (Weber وRinne) يوجه للتفكير بضعف سمع حسي عصبي مرتبط بالعمر بعد استبعاد الانسداد كمسبب وحيد.",
    "clues": [
        ("wears hearing aids", "استخدام سماعات <bdi>chronic</bdi>، يدعم ضعف سمع حسي عصبي <bdi>chronic</bdi> سابق"),
        ("bilateral cerumen impaction", "انسداد شمع بالأذنين، لازم يُعالج قبل تفسير أي فحص توليف بدقة"),
        ("bilaterally positive Rinne test", "<bdi>result</bdi> تستبعد وجود فجوة توصيلية كبيرة بأي من الأذنين"),
    ],
    "why_correct": [
        "أول <bdi>step</bdi> منطقية هي إزالة انسداد الشمع لأنه يشوّش تفسير أي فحص سمعي، وبعدها يتضح إن الصورة الأساسية هي ضعف سمع حسي عصبي مرتبط بالعمر (<bdi>presbycusis</bdi>) وهو الأشيع عند كبار السن خصوصًا مع استخدامها سماعات من قبل.",
        "كون اختبار رين إيجابي بالأذنين يبعد وجود فجوة توصيلية كبيرة تفسّر لوحدها كل الصورة، فيدعم كون الأساس حسي عصبي.",
        "ضعف السمع الحسي العصبي المرتبط بالعمر شائع جدًا وممكن يكون بدرجات متفاوتة بين الأذنين، وهذا يفسر استمرار استخدامها للسماعات أصلًا.",
    ],
    "when_changes": [
        "لو استمرت <bdi>results</bdi> فحص رين تدل على فجوة توصيلية واضحة بعد إزالة الشمع بالكامل، يصير التفكير ب<bdi>cause</bdi> توصيلي إضافي مثل التهاب أذن وسطى <bdi>chronic</bdi>.",
        "لو صاحب فقدان السمع <bdi>tinnitus</bdi> أحادي الجانب ودوخة، يصير التفكير بورم العصب السمعي ضروري.",
    ],
    "rule": "قبل تفسير فحوصات التوليف السمعي (Weber وRinne)، لازم يُعالج أي انسداد شمعي أولًا، والـ<bdi>cause</bdi> الأشيع لضعف السمع الـ<bdi>chronic</bdi> بكبار السن هو ضعف السمع الحسي العصبي المرتبط بالعمر.",
    "comparison": None,
    "guideline_note": None,
},
762: {
    "idea": "<bdi>patient</bdi> كبير بالسن عنده صورة إكلينيكية واضحة ل<bdi>dementia</bdi> <bdi>Alzheimer's disease</bdi> المبكر، والسؤال يبي الفحص التشخيصي الأولي المناسب.",
    "clues": [
        ("1-year history of progressive memory impairment", "فقدان ذاكرة تدريجي، سمة أساسية لل<bdi>Alzheimer's disease</bdi>"),
        ("clinical evidence of early Alzheimer dementia", "الـ<bdi>diagnosis</bdi> السريري مبدئيًا واضح، والفحص المطلوب لاستبعاد <bdi>causes</bdi> أخرى"),
    ],
    "why_correct": [
        "تصوير الدماغ (<bdi>brain imaging</bdi> بالأشعة المقطعية أو الرنين) هو الفحص الأولي المعياري ب<bdi>assessment</bdi> أي <bdi>dementia</bdi> جديد، لاستبعاد <bdi>causes</bdi> هيكلية قابلة لل<bdi>treatment</bdi> (ورم، استسقاء، نزيف <bdi>chronic</bdi>).",
        "حتى مع <bdi>diagnosis</bdi> سريري واضح لل<bdi>Alzheimer's disease</bdi>، لازم نستبعد <bdi>causes</bdi> ثانية قابلة للتصحيح قبل الجزم بالـ<bdi>diagnosis</bdi> النهائي.",
        "البزل القطني وتخطيط الدماغ ليسا فحوصات روتينية أولية إلا بوجود <bdi>signs</bdi> غير نمطية تستدعيها.",
    ],
    "when_changes": [
        "لو كانت هناك <bdi>signs</bdi> توحي بعدوى الجهاز العصبي المركزي أو <bdi>disease</bdi> سريع التطور، يصير البزل القطني مبررًا.",
        "لو ظهرت نوبات تشنجية مصاحبة لل<bdi>dementia</bdi>، يصير تخطيط الدماغ الكهربائي فحص مناسب إضافي.",
    ],
    "rule": "تصوير الدماغ هو الفحص التشخيصي الأولي القياسي عند <bdi>assessment</bdi> أي <bdi>case</bdi> <bdi>dementia</bdi> جديدة، حتى مع وضوح الصورة السريرية.",
    "comparison": None,
    "guideline_note": None,
},
763: {
    "idea": "<bdi>patient</bdi> كبير بالسن ضغطه <bdi>elevated</bdi> وعنده تدهور إدراكي تدريجي بضعف تنفيذي بارز، والرنين يبين تغيّرات منتشرة بالمادة البيضاء حول البطينات، وهذي الصورة تطابق الضعف الإدراكي الوعائي.",
    "clues": [
        ("hypertension", "<bdi>factor</bdi> <bdi>risk</bdi> رئيسي ل<bdi>disease</bdi> الأوعية الصغيرة الدماغية"),
        ("predominant executive function impairment", "ضعف بالوظائف التنفيذية أبرز من الذاكرة، نمط مميز للضعف الإدراكي الوعائي"),
        ("diffuse periventricular white-matter hyperintensities", "تغيّرات المادة البيضاء الوعائية الـ<bdi>chronic</bdi>، الـ<bdi>sign</bdi> التصويرية المميزة"),
    ],
    "why_correct": [
        "الضغط الـ<bdi>elevated</bdi> طويل الأمد يسبب <bdi>disease</bdi> أوعية دماغية صغيرة <bdi>chronic</bdi>، ويظهر بالرنين كتغيّرات مادة بيضاء منتشرة حول البطينات.",
        "الضعف التنفيذي البارز (بدل ضعف الذاكرة الأساسي) نمط كلاسيكي يميز <bdi>vascular cognitive impairment</bdi> عن <bdi>Alzheimer's disease</bdi>.",
        "صورة التصوير هنا مختلفة تمامًا عن نمط ضمور الحُصين المميز لل<bdi>Alzheimer's disease</bdi> أو تمدد البطينات المميز لاستسقاء الدماغ بضغط <bdi>normal</bdi>.",
    ],
    "when_changes": [
        "لو كان ضعف الذاكرة هو الأبرز مع ضمور بمنطقة الحُصين بالرنين، يميل الـ<bdi>diagnosis</bdi> لل<bdi>Alzheimer's disease</bdi>.",
        "لو صاحب التدهور الإدراكي اضطراب مشي وسلس بولي مع تمدد بطينات، يصير الـ<bdi>diagnosis</bdi> استسقاء الدماغ بضغط <bdi>normal</bdi>.",
    ],
    "rule": "تدهور إدراكي بضعف تنفيذي بارز مع تغيّرات مادة بيضاء منتشرة بالرنين عند <bdi>patient</bdi> ضغط <bdi>chronic</bdi> يشخّص الضعف الإدراكي الوعائي.",
    "comparison": None,
    "guideline_note": None,
},
764: {
    "idea": "<bdi>patient</bdi> <bdi>Parkinson's disease</bdi> متقدم عنده تدهور حركي وهلاوس وارتباك، والسؤال يبي أي <bdi>symptom</bdi> إضافي هو الأكثر ارتباطًا بزيادة <bdi>risk</bdi> تطور الـ<bdi>dementia</bdi> عنده تحديدًا.",
    "clues": [
        ("akinetic and rigid with no tremor", "نمط جامد بلا رجفان، مرتبط بزيادة <bdi>risk</bdi> الـ<bdi>dementia</bdi> أكثر من النمط الرجفاني"),
        ("prominent gait disorder and postural instability", "<bdi>symptoms</bdi> حركية متقدمة، <bdi>factor</bdi> <bdi>risk</bdi> إضافي معروف لل<bdi>dementia</bdi> ب<bdi>Parkinson's disease</bdi>"),
    ],
    "why_correct": [
        "صعوبة تذكر المواعيد تعكس بداية ضعف بالذاكرة الفعلية (episodic memory)، وهذا من أقوى المؤشرات المبكرة لتطور الـ<bdi>dementia</bdi> عند مرضى <bdi>Parkinson's disease</bdi>.",
        "النمط الجامد بدون رجفان (akinetic-rigid) مع اضطراب المشي والتوازن من <bdi>factors</bdi> الـ<bdi>risk</bdi> المعروفة لزيادة احتمال الـ<bdi>dementia</bdi> مقارنة بالنمط الرجفاني السائد.",
        "التهيّج وصعوبة إيجاد الكلمات وصعوبة القراءة <bdi>symptoms</bdi> ممكن تحدث ل<bdi>causes</bdi> ثانية (مزاجية أو انتباهية) وهي أقل تحديدًا ل<bdi>risk</bdi> الـ<bdi>dementia</bdi> من ضعف الذاكرة الفعلي.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> بالنمط الرجفاني السائد بدون اضطراب مشي أو توازن، يقل <bdi>risk</bdi> تطور الـ<bdi>dementia</bdi> نسبيًا مقارنة بالنمط الجامد.",
        "لو الـ<bdi>symptoms</bdi> المسيطرة مزاجية بس (<bdi>depression</bdi>) بدون أي دليل على ضعف ذاكرة حقيقي، يقل الترابط المباشر ب<bdi>risk</bdi> الـ<bdi>dementia</bdi>.",
    ],
    "rule": "عند مرضى <bdi>Parkinson's disease</bdi>، ضعف الذاكرة الفعلي (مثل نسيان المواعيد) والنمط الجامد بدون رجفان من أقوى مؤشرات زيادة <bdi>risk</bdi> تطور الـ<bdi>dementia</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
765: {
    "idea": "السؤال يبي المعيار الأساسي اللي يميّز الضعف الإدراكي الـ<bdi>mild</bdi> (MCI) عن الـ<bdi>dementia</bdi> الكامل، وهو وجود دليل موضوعي على تراجع الذاكرة مع الحفاظ على الاستقلالية الوظيفية.",
    "clues": [
        ("mild cognitive impairment", "مصطلح طبي محدد له معايير تشخيصية واضحة"),
    ],
    "why_correct": [
        "المعيار الأساسي لـ<bdi>mild cognitive impairment</bdi> هو وجود دليل موضوعي (باختبارات معيارية) على تراجع بالذاكرة أكثر من المتوقع للعمر، بدون أن يصل لدرجة الـ<bdi>dementia</bdi>.",
        "الفرق الجوهري بين MCI والـ<bdi>dementia</bdi> هو الحفاظ التام على الاستقلالية بأنشطة الحياة اليومية ب<bdi>case</bdi> MCI.",
        "انخفاض المزاج لمدة أسبوعين يصف <bdi>depression</bdi> مو ضعف إدراكي، والخلل الحركي الموضعي يصف مشكلة عصبية بؤرية مختلفة تمامًا.",
    ],
    "when_changes": [
        "لو صاحب ضعف الذاكرة عجز فعلي بنشاط واحد على الأقل من أنشطة الحياة اليومية، يصير التصنيف <bdi>dementia</bdi> مو ضعف إدراكي <bdi>mild</bdi>.",
        "لو كان انخفاض المزاج هو الـ<bdi>symptom</bdi> الوحيد بدون دليل موضوعي على ضعف ذاكرة، يصير الـ<bdi>diagnosis</bdi> الأرجح <bdi>depression</bdi>.",
    ],
    "rule": "الضعف الإدراكي الـ<bdi>mild</bdi> يُعرّف بوجود دليل موضوعي على تراجع الذاكرة مع الحفاظ الكامل على استقلالية أنشطة الحياة اليومية، وهذا يميزه عن الـ<bdi>dementia</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
766: {
    "idea": "<bdi>patient</bdi> عنده رجفان باليد اليمنى يظهر بوضوح عند الحركة الهادفة (الوصول لقلم) وباختبار الإصبع للأنف، وهذا رجفان قصدي مخيخي، وموقعه بنفس جهة الطرف المصاب لأن إشارات المخيخ تنظم الحركة بنفس الجانب.",
    "clues": [
        ("tremor... best displayed when he reaches for a pen", "رجفان قصدي يظهر مع الحركة الهادفة، مميز للمخيخ مو للراحة"),
        ("finger-to-nose test", "اختبار مخيخي كلاسيكي لكشف الـ<bdi>ataxia</bdi> ودقة الحركة"),
    ],
    "why_correct": [
        "الرجفان القصدي (اللي يزيد مع الحركة الهادفة والاختبارات الدقيقة مثل الإصبع للأنف) يعكس خلل بالمخيخ لا بالعقد القاعدية.",
        "المخيخ ينظم حركة نفس جهة الجسم (تأثير متماثل الجانب)، فرجفان اليد اليمنى يوجه لخلل بـ<bdi>right cerebellum</bdi>.",
        "هذا يختلف تمامًا عن رجفان الراحة الباركنسوني اللي يعكس خلل بالعقد القاعدية بالجهة المقابلة (contralateral).",
    ],
    "when_changes": [
        "لو كان الرجفان بالراحة ويتحسن مع الحركة الهادفة مع بطء حركة، يصير موقع الخلل الأرجح العقد القاعدية بالجهة المقابلة.",
        "لو صاحب الرجفان ضعف وتشنج بنفس اليد، يميل الـ<bdi>diagnosis</bdi> لإصابة القشرة الحركية بالجهة المقابلة.",
    ],
    "rule": "الرجفان القصدي مع خلل باختبار الإصبع للأنف يشير لخلل مخيخي بنفس جهة الطرف المصاب.",
    "comparison": None,
    "guideline_note": None,
},
767: {
    "idea": "<bdi>patient</bdi> <bdi>Parkinson's disease</bdi> الرجفان هو الـ<bdi>symptom</bdi> الوحيد المزعج لها فعليًا بدون <bdi>treatment</bdi> حالي، والسؤال يبي الدواء الأنسب تحديدًا لتحسين الرجفان.",
    "clues": [
        ("very annoying tremor of the dominant right hand", "الرجفان هو الـ<bdi>symptom</bdi> الرئيسي والمزعج المستهدف بالـ<bdi>treatment</bdi>"),
        ("not on any medication", "لم تبدأ أي <bdi>treatment</bdi> بعد، يسمح باختيار دواء موجّه لل<bdi>symptom</bdi> المحدد"),
    ],
    "why_correct": [
        "مضادات الكولين مثل <bdi>procyclidine</bdi> فعالة بشكل خاص بتحسين الرجفان الباركنسوني تحديدًا، أكثر من تأثيرها على بطء الحركة أو التيبس.",
        "بما إن الرجفان هو الـ<bdi>symptom</bdi> الوحيد المزعج، يُفضّل دواء موجّه له تحديدًا بدل بدء <bdi>treatment</bdi> شامل قد يعطي <bdi>symptoms</bdi> جانبية غير ضرورية.",
        "لازم مراعاة الحذر من الـ<bdi>symptoms</bdi> الجانبية المعرفية لمضادات الكولين عند كبار السن، لكنها تبقى الخيار الأكثر توجّهًا ل<bdi>symptom</bdi> الرجفان تحديدًا هنا.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>symptoms</bdi> المسيطرة بطء حركة وتيبس بدل الرجفان، يصير الليفودوبا أو منبهات الـ<bdi>dopamine</bdi> الخيار الأنسب.",
        "لو كانت الـ<bdi>patient</bdi> أكبر سنًا مع ضعف إدراكي، يُتجنّب مضاد الكولين ل<bdi>risk</bdi> تفاقم الالتباس ويُفضّل بديل آخر.",
    ],
    "rule": "مضادات الكولين مثل procyclidine هي الأنسب ل<bdi>treatment</bdi> الرجفان الباركنسوني تحديدًا عندما يكون الـ<bdi>symptom</bdi> المسيطر والوحيد المزعج.",
    "comparison": None,
    "guideline_note": None,
},
768: {
    "idea": "<bdi>patient</bdi> كبير بالسن صار عنده تعب وصعوبة استيقاظ تدريجية بعد سقطات متكررة غير موثقة بإصابة رأس واضحة، والفحص العصبي والأشعة السينية للجمجمة <bdi>normal</bdi>، وهذا يوجه لنزيف تحت جافي <bdi>chronic</bdi> تدريجي التأثير.",
    "clues": [
        ("increasing fatigue and drowsiness and difficulty to arouse", "تدهور وعي تدريجي بطيء، يطابق نزيف <bdi>chronic</bdi> مو <bdi>acute</bdi>"),
        ("he admits to taking several falls", "سقطات متكررة، <bdi>cause</bdi> شائع منسي عند كبار السن"),
        ("unaware of any head injury", "غياب تذكر إصابة رأس واضحة، شائع بالنزيف تحت الجافي الـ<bdi>chronic</bdi>"),
        ("Plain X-ray of the skull is negative", "غياب كسر لا ينفي وجود نزيف داخل الجمجمة"),
    ],
    "why_correct": [
        "النزيف تحت الجافي الـ<bdi>chronic</bdi> (<bdi>chronic subdural hematoma</bdi>) شائع جدًا بكبار السن ب<bdi>cause</bdi> ضمور الدماغ اللي يمدد الأوردة الجسرية ويخليها تتمزق حتى بإصابة بسيطة منسية.",
        "التطور البطيء (أسابيع) للنعاس وصعوبة الاستيقاظ بدون <bdi>signs</bdi> بؤرية واضحة يطابق هذا النمط التدريجي، بخلاف السكتة أو النزيف الـ<bdi>acute</bdi> اللي يكون أسرع وأوضح بالـ<bdi>signs</bdi> البؤرية.",
        "الأشعة السينية العادية للجمجمة لا تكشف نزيف داخل الجمجمة أصلًا (تحتاج أشعة مقطعية للدماغ)، فسلبيتها لا تستبعد الـ<bdi>diagnosis</bdi>.",
    ],
    "when_changes": [
        "لو كان هناك ضعف بؤري واضح بجانب واحد من الجسم، يصير الشك بسكتة دماغية أقوى ويحتاج تصوير عاجل للتفريق.",
        "لو صاحبت الـ<bdi>symptoms</bdi> حمى وتيبس رقبة، يميل الـ<bdi>diagnosis</bdi> لالتهاب سحايا بكتيري <bdi>acute</bdi>.",
    ],
    "rule": "تدهور وعي تدريجي بعد سقطات متكررة عند كبير بالسن، حتى بدون تذكر إصابة رأس واضحة، يوجه لنزيف تحت جافي <bdi>chronic</bdi> يحتاج أشعة مقطعية للدماغ لتأكيده.",
    "comparison": None,
    "guideline_note": None,
},
769: {
    "idea": "<bdi>patient</bdi> <bdi>diabetes</bdi> عنده ضعف حركي بحت (وجه وذراع ورجل بنفس الدرجة) بدون أي خلل حسي أو كلامي، وهذا نمط كلاسيكي لسكتة صغيرة (لاكونار) تصيب فرع مخترق بالكبسولة الداخلية.",
    "clues": [
        ("weakness is equal in the right face, arm and leg", "ضعف حركي متساوي بالوجه والذراع والرجل، نمط كلاسيكي للسكتة الصغيرة"),
        ("Sensation, speech and comprehension are intact", "سلامة الحس والكلام، يستبعد إصابة قشرية كبيرة"),
    ],
    "why_correct": [
        "ضعف حركي بحت متساوي بالوجه والذراع والرجل مع سلامة كاملة للحس والكلام هو التوقيع الكلاسيكي لسكتة لاكونار (<bdi>pure motor stroke</bdi>) تصيب الكبسولة الداخلية.",
        "هذا النوع من السكتات ينتج عن انسداد فروع مخترقة صغيرة (<bdi>penetrating branches</bdi>) من الشريان المخي الأوسط ب<bdi>cause</bdi> <bdi>disease</bdi> الأوعية الصغيرة المرتبط ب<bdi>diabetes</bdi>.",
        "الإصابة القشرية الكبيرة (مثل جذع الشريان المخي الأوسط) عادة تصاحبها خلل بالكلام أو الحس أو إهمال، وهذا غير موجود هنا.",
    ],
    "when_changes": [
        "لو صاحب الضعف خلل بالكلام والفهم، يصير الشك بإصابة قشرية أكبر بجذع الشريان المخي الأوسط.",
        "لو كان الضعف بالرجل أبرز من الوجه والذراع، يميل الـ<bdi>diagnosis</bdi> لإصابة الشريان المخي الأمامي.",
    ],
    "rule": "ضعف حركي بحت متساوي بالوجه والذراع والرجل مع سلامة الحس والكلام يشخّص سكتة لاكونار من فرع مخترق صغير.",
    "comparison": None,
    "guideline_note": None,
},
770: {
    "idea": "<bdi>patient</bdi> كبير بالسن عنده صداع مفاجئ <bdi>severe</bdi> جدًا وصفه بأسوأ صداع بحياته أثناء مجهود بسيط، وهذا وصف كلاسيكي للنزيف تحت العنكبوتية.",
    "clues": [
        ("sudden severe headache while bending down", "بداية مفاجئة جدًا مرتبطة بمجهود، نمط كلاسيكي"),
        ("the worst headache he has ever had", "وصف مميز جدًا يوجه مباشرة للنزيف تحت العنكبوتية"),
        ("like being hit on the back of the neck", "وصف الصداع الصاعقي المفاجئ الـ<bdi>severe</bdi>"),
    ],
    "why_correct": [
        "وصف \"أسوأ صداع بحياته\" ببداية مفاجئة صاعقية (thunderclap) هو الـ<bdi>sign</bdi> التحذيرية الكلاسيكية للنزيف تحت العنكبوتية (<bdi>subarachnoid hemorrhage</bdi>).",
        "ارتباط الصداع بمجهود بسيط (كالانحناء) شائع كمحفز لتمزق أم دم دماغية مسببة لهذا النوع من النزيف.",
        "<bdi>meningitis</bdi> والصداع العنقودي والتوتري كلها تبدأ بشكل أكثر تدريجية ولا تعطي وصف \"أسوأ صداع بالحياة\" المفاجئ الصاعقي بهذي الحدة.",
    ],
    "when_changes": [
        "لو كان الصداع تدريجي البداية مع حمى وتيبس رقبة، يميل الـ<bdi>diagnosis</bdi> ل<bdi>meningitis</bdi>.",
        "لو كان الصداع متكرر بنفس النمط لسنوات وبس أثناء التوتر، يصير الـ<bdi>diagnosis</bdi> الأرجح صداع توتري.",
    ],
    "rule": "صداع مفاجئ صاعقي يوصف بأنه أسوأ صداع بالحياة يوجه فورًا للنزيف تحت العنكبوتية حتى يثبت العكس.",
    "comparison": None,
    "guideline_note": None,
},
771: {
    "idea": "<bdi>patient</bdi> عندها رجفان <bdi>bilateral</bdi> تدريجي يتداخل مع الكتابة والأكل، مع تطور صوت مهزوز وحركة رأس، وهذا نمط كلاسيكي للرجفان الأساسي، والدواء الأول له مختلف عن أدوية <bdi>Parkinson's disease</bdi>.",
    "clues": [
        ("2-year history of a slowly progressive bilateral tremor", "رجفان <bdi>bilateral</bdi> تدريجي، نمط مميز للرجفان الأساسي"),
        ("interferes with her writing and eating", "رجفان حركي/وضعي يظهر مع الأنشطة اليدوية، لا رجفان راحة"),
        ("head bobbing and a change in her voice", "إصابة الرأس والصوت، شائعة بالرجفان الأساسي المتقدم"),
    ],
    "why_correct": [
        "الرجفان الـ<bdi>bilateral</bdi> التدريجي اللي يصاحب الكتابة والأكل مع إصابة الرأس والصوت يطابق تمامًا <bdi>essential tremor</bdi> لا رجفان <bdi>Parkinson's disease</bdi>.",
        "الدواء الأول ل<bdi>treatment</bdi> الرجفان الأساسي هو <bdi>propranolol</bdi>، بعكس رجفان <bdi>Parkinson's disease</bdi> اللي علاجه الأساسي ليفودوبا أو مضادات كولين.",
        "غياب أي وصف لرجفان بالراحة أو بطء حركة يبعد <bdi>diagnosis</bdi> <bdi>Parkinson's disease</bdi> ويدعم كون المشكلة رجفان أساسي بحت.",
    ],
    "when_changes": [
        "لو كان الرجفان بالراحة بدل الحركة مع بطء حركة وتيبس، يميل الـ<bdi>diagnosis</bdi> ل<bdi>Parkinson's disease</bdi> والـ<bdi>treatment</bdi> يختلف تمامًا.",
        "لو صاحب الرجفان تسارع قلب وفقدان وزن وتعرّق، يستوجب استبعاد <bdi>hyperthyroidism</bdi> ك<bdi>cause</bdi> مساهم بالرجفان.",
    ],
    "rule": "الـ<bdi>propranolol</bdi> هو الـ<bdi>treatment</bdi> الأول للرجفان الأساسي، وهذا مختلف تمامًا عن <bdi>treatment</bdi> رجفان <bdi>Parkinson's disease</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
772: {
    "idea": "<bdi>patient</bdi> سليم صار عنده شلل وجهي محيطي مفاجئ من ساعة، وهذا شلل بيل النموذجي، والسؤال يبي الـ<bdi>treatment</bdi> اللي يقصّر مدة الـ<bdi>symptoms</bdi> ويحسّن التعافي.",
    "clues": [
        ("sudden onset of unilateral peripheral facial nerve weakness 1 hour ago", "بداية مفاجئة حديثة جدًا لشلل وجهي محيطي"),
        ("no medical illness and not on any medication", "يبعد <bdi>causes</bdi> ثانوية معروفة، يدعم كونه شلل بيل مجهول الـ<bdi>cause</bdi>"),
    ],
    "why_correct": [
        "الـ<bdi>treatment</bdi> بالستيرويد المبكر (<bdi>corticosteroid therapy</bdi>) أثبت فعاليته بتحسين وتسريع التعافي من شلل بيل، خصوصًا لو بدأ خلال 72 ساعة من بداية الـ<bdi>symptoms</bdi>.",
        "بدء الستيرويد مبكرًا (زي <bdi>case</bdi> الـ<bdi>patient</bdi> هنا، ساعة واحدة فقط) يعطي أفضل فرصة لتقصير الـ<bdi>symptoms</bdi> ومنع <bdi>complications</bdi> طويلة المدى.",
        "الـ<bdi>treatment</bdi> المضاد للفيروسات لوحده ما أثبت فعالية كافية، والـ<bdi>treatment</bdi> الحال للتخثر والأكسجين عالي الضغط ليسوا علاجات معتمدة لشلل بيل.",
    ],
    "when_changes": [
        "لو تأخر الـ<bdi>patient</bdi> بمراجعة الطبيب لأكثر من أسبوع من بداية الـ<bdi>symptoms</bdi>، تقل فائدة بدء الستيرويد الآن.",
        "لو صاحب الشلل ألم أذن <bdi>severe</bdi> وطفح جلدي حويصلي، يصير الـ<bdi>diagnosis</bdi> متلازمة رامزي هانت ويحتاج إضافة مضاد فيروسات للستيرويد.",
    ],
    "rule": "الستيرويد المبكر هو الـ<bdi>treatment</bdi> الأثبت فعالية بتقصير <bdi>symptoms</bdi> شلل بيل، خصوصًا لو بدأ بأول 72 ساعة.",
    "comparison": None,
    "guideline_note": None,
},
773: {
    "idea": "<bdi>patient</bdi> عندها صداع متكرر منذ سنتين بنمط ثابت نسبيًا (توتري/شقيقي محتمل) بدون <bdi>signs</bdi> تحذيرية بالفحص، والسؤال يبي الـ<bdi>step</bdi> التالية لتحديد <bdi>cause</bdi> هذا الصداع.",
    "clues": [
        ("2-year history of recurrent headaches", "نمط <bdi>chronic</bdi> ومستقر لفترة طويلة، يقلل احتمال <bdi>cause</bdi> خطير جديد"),
        ("Neurological examination is within normal limits", "فحص عصبي <bdi>normal</bdi>، يبعد <bdi>signs</bdi> تحذيرية"),
        ("The optic fundi are normal", "غياب <bdi>sign</bdi> ارتفاع ضغط داخل الجمجمة"),
    ],
    "why_correct": [
        "بصداع <bdi>chronic</bdi> مستقر النمط لسنتين مع فحص عصبي وفحص قاع العين طبيعيين، الـ<bdi>step</bdi> الأهم لتحديد الـ<bdi>cause</bdi> هي أخذ تاريخ مرضي دقيق وفحص سريري شامل، لأن أغلب أنواع الصداع الأولي (شقيقي أو توتري) تُشخّص إكلينيكيًا بدون تصوير.",
        "التصوير (رنين أو مقطعية) يُحجز لوجود <bdi>signs</bdi> تحذيرية (بداية جديدة مفاجئة، تغيّر بالنمط، فحص عصبي غير <bdi>normal</bdi>)، وهذي غير موجودة هنا.",
        "سرعة الترسيب تُطلب بالشك بالتهاب الشريان الصدغي عند كبار السن، وهذا مو السياق هنا (<bdi>patient</bdi> أصغر سنًا بنمط <bdi>chronic</bdi> مستقر).",
    ],
    "when_changes": [
        "لو ظهرت <bdi>sign</bdi> تحذيرية جديدة (فحص عصبي غير <bdi>normal</bdi> أو تغيّر مفاجئ بنمط الصداع)، يصير التصوير بالرنين ضروري.",
        "لو كانت الـ<bdi>patient</bdi> أكبر من 50 سنة مع صداع جديد وألم بفروة الرأس، يصير فحص سرعة الترسيب لاستبعاد التهاب الشريان الصدغي.",
    ],
    "rule": "بصداع <bdi>chronic</bdi> مستقر النمط بدون <bdi>signs</bdi> تحذيرية، أخذ تاريخ دقيق وفحص سريري شامل هو الـ<bdi>step</bdi> الأولى قبل أي تصوير.",
    "comparison": None,
    "guideline_note": None,
},
774: {
    "idea": "<bdi>patient</bdi> تحتاج شفط موجّه بالأشعة المقطعية، والسؤال يبي من المسؤول عن أخذ الموافقة المستنيرة لهذا الـ<bdi>procedure</bdi> تحديدًا.",
    "clues": [
        ("CT guided aspiration", "<bdi>procedure</bdi> تدخلي محدد يقوم به شخص معيّن"),
    ],
    "why_correct": [
        "الموافقة المستنيرة يجب أن يأخذها الشخص اللي سينفّذ الـ<bdi>procedure</bdi> فعليًا ويعرف تفاصيله ومخاطره بدقة، وهنا هو <bdi>الأشعة التداخلي (radiologist)</bdi>.",
        "الشخص المنفّذ لل<bdi>procedure</bdi> هو الأقدر على شرح خطوات الـ<bdi>procedure</bdi> ومخاطره وبدائله بدقة كافية لل<bdi>patient</bdi> لاتخاذ قرار مستنير.",
        "أعضاء الفريق العلاجي الآخرين (الممرضة أو طبيب الباطنية المقيم) ما لهم نفس المعرفة التفصيلية بالـ<bdi>procedure</bdi> التداخلي نفسه.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>procedure</bdi> جراحة عامة بدل شفط موجّه بالأشعة، يصير الجراح المسؤول هو من يأخذ الموافقة.",
        "لو كان هناك طبيب آخر من نفس التخصص ومطّلع تمامًا على تفاصيل الـ<bdi>procedure</bdi> ونتائجه، يمكن أن ينوب لأخذ الموافقة بدلًا من المنفّذ الأصلي بحالات محددة.",
    ],
    "rule": "الموافقة المستنيرة على أي <bdi>procedure</bdi> تداخلي يجب أن يأخذها الشخص اللي سيقوم بتنفيذ الـ<bdi>procedure</bdi> فعليًا.",
    "comparison": None,
    "guideline_note": None,
},
775: {
    "idea": "طالب طب نسى يسدل الستارة أثناء فحص بطن <bdi>patient</bdi>، وهذا انتهاك واضح لمبدأ الخصوصية الجسدية لل<bdi>patient</bdi> أثناء الفحص.",
    "clues": [
        ("forgot to close the curtain while exposing the patient's abdomen", "كشف جسد الـ<bdi>patient</bdi> أمام آخرين بدون حجب بصري كافٍ"),
    ],
    "why_correct": [
        "عدم إغلاق الستارة أثناء كشف جسد الـ<bdi>patient</bdi> يعتبر انتهاك مباشر لمبدأ <bdi>respect patient's privacy</bdi>، وهو حماية جسد الـ<bdi>patient</bdi> من الكشف غير الضروري أمام الآخرين.",
        "هذا يختلف عن الكرامة العامة (وهي مفهوم أوسع) أو السرية (وهي حماية المعلومات مو الجسد) أو الاستقلالية (وهي حق اتخاذ القرار).",
        "المشكلة هنا تحديدًا فيزيائية بصرية (كشف الجسد) مو معلوماتية أو قرارية، فالمصطلح الأدق هو الخصوصية.",
    ],
    "when_changes": [
        "لو المشكلة كانت تسريب معلومات طبية عن الـ<bdi>patient</bdi> لشخص غير مخوّل، يصير المبدأ المنتهك هو السرية.",
        "لو تم <bdi>procedure</bdi> فحص أو <bdi>treatment</bdi> بدون أخذ موافقة الـ<bdi>patient</bdi> أصلًا، يصير المبدأ المنتهك هو الاستقلالية.",
    ],
    "rule": "كشف جسد الـ<bdi>patient</bdi> أمام آخرين بدون حجب مناسب (زي عدم إغلاق الستارة) ينتهك مبدأ احترام خصوصية الـ<bdi>patient</bdi> تحديدًا.",
    "comparison": None,
    "guideline_note": None,
},
776: {
    "idea": "عائلة <bdi>patient</bdi> بسرطان منتشر طلبت من الطبيب إخفاء الـ<bdi>diagnosis</bdi> عنه، والسؤال يبي الموقف الأخلاقي الصحيح اللي يحترم حق الـ<bdi>patient</bdi> بمعرفة حالته.",
    "clues": [
        ("His family asked the oncologist not to tell their father", "طلب عائلي بإخفاء المعلومة عن الـ<bdi>patient</bdi> نفسه"),
    ],
    "why_correct": [
        "الـ<bdi>patient</bdi> له الحق الأساسي بمعرفة تشخيصه (مبدأ الاستقلالية والصدق)، وهذا الحق أعلى من رغبة العائلة بإخفاء المعلومة عنه ما لم يطلب الـ<bdi>patient</bdi> نفسه عدم المعرفة.",
        "إبلاغ الـ<bdi>patient</bdi> بتشخيصه يسمح له باتخاذ قرارات مستنيرة عن علاجه ومستقبله، وهذا حق أساسي في الرعاية الطبية.",
        "استشارة المستشار القانوني أو لجنة الأخلاقيات مو ضرورية هنا لأن المبدأ الأخلاقي واضح ومباشر بدون تعقيد حقيقي يستدعي تصعيد.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> نفسه هو من طلب عدم معرفة تفاصيل تشخيصه، يُحترم هذا الطلب باعتباره حق الـ<bdi>patient</bdi> أيضًا.",
        "لو كان هناك شك حقيقي بعدم أهلية الـ<bdi>patient</bdi> العقلية لاستيعاب المعلومة، يصير <bdi>assessment</bdi> الأهلية <bdi>step</bdi> أولى قبل الإفصاح المباشر.",
    ],
    "rule": "الـ<bdi>patient</bdi> له الحق الأساسي بمعرفة تشخيصه، وهذا الحق يُحترم حتى لو طلبت العائلة إخفاءه، ما لم يطلب الـ<bdi>patient</bdi> نفسه عدم المعرفة.",
    "comparison": None,
    "guideline_note": None,
},
777: {
    "idea": "طبيب زاد جرعة مسكن ل<bdi>patient</bdi> بمرحلة نهائية يعاني ألم لا يُحتمل، موضحًا للعائلة إن الجرعة الأعلى ممكن تسرّع الوفاة، وهذا تطبيق مباشر لمبدأ الأثر المزدوج بالأخلاق الطبية.",
    "clues": [
        ("unbearable pain", "ألم <bdi>severe</bdi> جدًا يستدعي تصعيد جرعة المسكن"),
        ("explaining to the family that the higher doses may hasten their father's death", "الطبيب أوضح الأثر الجانبي المحتمل بصدق قبل اتخاذ القرار"),
    ],
    "why_correct": [
        "مبدأ الأثر المزدوج (<bdi>principle of double effect</bdi>) يسمح أخلاقيًا بعمل له <bdi>result</bdi> جيدة مقصودة (تخفيف الألم) حتى لو له أثر جانبي غير مقصود ممكن يكون ضار (تسريع الوفاة)، بشرط أن يكون القصد الأساسي هو الأثر الجيد.",
        "هنا القصد الأساسي واضح وصريح: تخفيف معاناة الـ<bdi>patient</bdi>، والأثر الجانبي (تسريع الوفاة المحتمل) غير مقصود بذاته بل <bdi>result</bdi> ثانوية مقبولة أخلاقيًا.",
        "هذا يختلف عن القتل الرحيم المباشر، لأن الهدف هنا علاجي بحت (تسكين الألم) مو إنهاء الحياة كهدف مباشر.",
    ],
    "when_changes": [
        "لو كان القصد الأساسي والمباشر من زيادة الجرعة هو إنهاء حياة الـ<bdi>patient</bdi> مباشرة، يصير هذا قتل رحيم مو تطبيق لمبدأ الأثر المزدوج.",
        "لو كانت الزيادة بالجرعة بدون أي احتمال حقيقي لتسريع الوفاة، فلا حاجة أصلًا لتطبيق هذا المبدأ.",
    ],
    "rule": "مبدأ الأثر المزدوج يبرر أخلاقيًا <bdi>treatment</bdi> مقصود بهدف جيد (تخفيف الألم) حتى لو صاحبه أثر جانبي غير مقصود قد يكون ضارًا، طالما القصد الأساسي هو الأثر الجيد.",
    "comparison": None,
    "guideline_note": None,
},
778: {
    "idea": "<bdi>patient</bdi> طلبت من الجراح إنه ما يشرح لها تفاصيل العملية، واحترم الجراح رغبتها، لكن طبيب التخدير أصرّ على شرح كل التفاصيل لها رغم كذا. السؤال يبي أنسب تصرف للجراح بهذا التعارض المهني.",
    "clues": [
        ("expressed her wish to not knowing the details", "رغبة صريحة من الـ<bdi>patient</bdi> بعدم المعرفة، حق معترف به"),
        ("The surgeon respected her wish", "الجراح احترم رغبتها بشكل صحيح مبدئيًا"),
        ("anesthesiologist who insisted to explain to the patient all details", "تعارض واضح بين فريقين علاجيين حول احترام رغبة الـ<bdi>patient</bdi>"),
    ],
    "why_correct": [
        "وجود تعارض مهني حقيقي بين تصرف الجراح (احترام رغبة الـ<bdi>patient</bdi>) وإصرار طبيب التخدير على مخالفتها يستدعي تصعيد الأمر لجهة محايدة تحل الخلاف بطريقة منهجية.",
        "استشارة <bdi>لجنة الأخلاقيات بالمستشفى</bdi> هي الطريقة المناسبة لحل هذا التعارض المهني بشكل رسمي ومنهجي يحمي حق الـ<bdi>patient</bdi> ويوضح الموقف لكل الأطراف.",
        "ترك الأمر لطبيب التخدير بدون تدخل يعني التخلي عن مسؤولية حماية رغبة الـ<bdi>patient</bdi> اللي احترمها الجراح مسبقًا بشكل صحيح.",
    ],
    "when_changes": [
        "لو اتفق الفريق الطبي كامله على احترام رغبة الـ<bdi>patient</bdi> بدون أي خلاف، فلا حاجة لتصعيد الأمر للجنة الأخلاقيات.",
        "لو تغيّرت رغبة الـ<bdi>patient</bdi> بنفسها وطلبت معرفة التفاصيل من الجميع، ينتهي التعارض تلقائيًا بدون حاجة لتدخل خارجي.",
    ],
    "rule": "عند تعارض حقيقي بين أعضاء الفريق الطبي حول احترام رغبة الـ<bdi>patient</bdi>، استشارة لجنة الأخلاقيات بالمستشفى هي الطريقة المنهجية المناسبة لحل الخلاف.",
    "comparison": None,
    "guideline_note": None,
},
779: {
    "idea": "<bdi>patient</bdi> <bdi>diabetes</bdi> رفض عملية بتر ضرورية ل<bdi>case</bdi> قدم شاركو المتقدمة، والسؤال يبي الـ<bdi>step</bdi> الأولى الصحيحة قبل أي <bdi>procedure</bdi> آخر تجاه رفضه.",
    "clues": [
        ("The patient refused", "رفض صريح من الـ<bdi>patient</bdi> ل<bdi>procedure</bdi> طبي موصى به بشدة"),
    ],
    "why_correct": [
        "قبل قبول أو التعامل مع أي رفض علاجي، لازم نتأكد أولًا إن الـ<bdi>patient</bdi> يملك الأهلية العقلية الكاملة لفهم قراره وتبعاته (<bdi>assess the patient's mental capacity</bdi>).",
        "رفض الـ<bdi>patient</bdi> المستنير له الحق فيه فقط إذا كان يملك أهلية عقلية كاملة، وهذا الـ<bdi>assessment</bdi> يجب أن يسبق أي <bdi>step</bdi> أخرى.",
        "تحويل الـ<bdi>patient</bdi> لمستشفى آخر أو طلب توقيعه على نموذج خروج بدون <bdi>assessment</bdi> أهليته أولًا يتجاوز <bdi>step</bdi> أساسية وضرورية بالـ<bdi>assessment</bdi> الأخلاقي والقانوني.",
    ],
    "when_changes": [
        "لو تأكدنا إن الـ<bdi>patient</bdi> يملك أهلية عقلية كاملة ويفهم تمامًا عواقب رفضه، يُحترم قراره ويُوثّق برفض الـ<bdi>treatment</bdi>.",
        "لو تبين إن الـ<bdi>patient</bdi> غير مؤهل عقليًا لاتخاذ هذا القرار (ب<bdi>cause</bdi> هذيان أو <bdi>disease</bdi> عقلي مثلًا)، يصير القرار يُتخذ وفق مصلحته الفضلى مع أقرب أقاربه.",
    ],
    "rule": "أي رفض علاجي من <bdi>patient</bdi> يجب أولًا <bdi>assessment</bdi> أهليته العقلية قبل اتخاذ أي <bdi>step</bdi> أخرى تجاه هذا الرفض.",
    "comparison": None,
    "guideline_note": None,
},
780: {
    "idea": "حدث خطأ جراحي بسيط أثال إطالة مدة العملية بدون أي ضرر نهائي لل<bdi>patient</bdi>، وسأل الـ<bdi>patient</bdi> عن الـ<bdi>cause</bdi>، والسؤال يبي الرد الأخلاقي الصحيح المبني على الصدق والشفافية.",
    "clues": [
        ("bleeding resulted from a surgical error", "خطأ جراحي فعلي حصل أثناء العملية"),
        ("fully recovered with no complications", "لا ضرر دائم نتج عن الخطأ"),
        ("asked the surgeon why his operation took longer time", "سؤال مباشر من الـ<bdi>patient</bdi> يستحق إجابة صادقة"),
    ],
    "why_correct": [
        "مبدأ الإفصاح الصادق (<bdi>open disclosure</bdi>) بالأخطاء الطبية يفرض على الطبيب إخبار الـ<bdi>patient</bdi> بما حصل فعليًا حتى لو لم ينتج ضرر دائم.",
        "الجراح المسؤول عن العملية هو من يجب أن يشرح لل<bdi>patient</bdi> بنفسه ما حدث بأسلوب مطمئن وصادق بنفس الوقت.",
        "إخفاء المعلومة أو تجاهل السؤال يخالف مبدأ الصدق ويقوّض ثقة الـ<bdi>patient</bdi> بالفريق الطبي على المدى الطويل.",
    ],
    "when_changes": [
        "لو نتج عن الخطأ ضرر دائم لل<bdi>patient</bdi>، يصير الإفصاح أكثر إلحاحًا ويحتاج توثيق رسمي إضافي مع <bdi>management</bdi> المستشفى.",
        "لو كان السؤال عن تفاصيل تقنية بحتة غير متعلقة بالخطأ نفسه، يمكن الإجابة المباشرة بدون الحاجة لتفصيل الخطأ بشكل موسّع.",
    ],
    "rule": "عند وجود خطأ طبي، حتى لو لم ينتج عنه ضرر دائم، يجب على الطبيب المسؤول إخبار الـ<bdi>patient</bdi> بصدق عندما يسأل.",
    "comparison": None,
    "guideline_note": None,
},
781: {
    "idea": "أثناء عملية شك بالتهاب زائدة دودية طلعت الزائدة سليمة، واستُؤصلت حسب الممارسة المتبعة عادة رغم عدم تذكر الجراح شرح هذي النقطة تحديدًا بالموافقة، والسؤال يبي رد الجراح الصحيح لو سأله الـ<bdi>patient</bdi> لاحقًا.",
    "clues": [
        ("the appendix found in normal state", "الزائدة طلعت سليمة أثناء العملية"),
        ("common practice is to remove the appendix even if it is not inflamed", "استئصالها ممارسة معيارية متبعة حتى لو سليمة، جزء من نطاق العملية المتفق عليه أصلًا"),
        ("does not remember that he informed the patient about this decision", "شك بعدم تذكر شرح هذي النقطة تحديدًا، مو تأكيد إخفاء متعمد"),
    ],
    "why_correct": [
        "استئصال الزائدة حتى لو طلعت سليمة أثناء عملية شك بالتهابها هو جزء من الممارسة الجراحية المعيارية المتفق عليها ضمن نطاق العملية الأصلية، ومو خطأ طبي منفصل يحتاج إفصاح خاص.",
        "أنسب رد للجراح هو إخبار الـ<bdi>patient</bdi> بصدق إن هذا جزء من الـ<bdi>procedure</bdi> القياسي المتبع بحالات الشك ب<bdi>appendicitis</bdi>، وهذا بحد ذاته شفافية وصدق.",
        "هذا يختلف عن سيناريو الخطأ الجراحي الفعلي (زي <bdi>case</bdi> النزيف ب<bdi>cause</bdi> خطأ) لأن استئصال الزائدة هنا <bdi>procedure</bdi> مقصود ومبرر طبيًا ضمن نطاق العملية المتفق عليها.",
    ],
    "when_changes": [
        "لو كان استئصال الزائدة قرار غير مبرر طبيًا وخارج نطاق العملية المتفق عليه تمامًا، يصير الوضع أقرب لخطأ يحتاج إفصاح أوسع ومراجعة.",
        "لو رفض الـ<bdi>patient</bdi> صراحة استئصال الزائدة إذا طلعت سليمة أثناء المناقشة قبل العملية، يصير عدم الالتزام بهذا الرفض مخالفة حقيقية تحتاج معالجة مختلفة.",
    ],
    "rule": "الـ<bdi>procedures</bdi> المعيارية المتبعة ضمن نطاق العملية المتفق عليها (كاستئصال زائدة مشتبه بها حتى لو سليمة) تُشرح لل<bdi>patient</bdi> بصدق كجزء من الممارسة القياسية، لا كخطأ يحتاج إفصاح خاص.",
    "comparison": None,
    "guideline_note": None,
},
782: {
    "idea": "<bdi>patient</bdi> كبير جدًا بالسن بسرطان منتشر ومصنّف بعدم الإنعاش لتدهور وظائفه الرئوية، والجراح يفكر بعملية كبيرة غير مؤكد نجاحها، والسؤال يبي القرار الأنسب أخلاقيًا بهذا السياق.",
    "clues": [
        ("advanced metastatic lung cancer", "<bdi>disease</bdi> نهائي متقدم، يحدد توقعات الـ<bdi>treatment</bdi>"),
        ("labelled a do not resuscitate case", "قرار سابق يعكس <bdi>assessment</bdi> شامل لتوقعات سيئة"),
        ("not sure, if the patient could survive the operation", "شك حقيقي بفائدة العملية مقابل خطورتها الكبيرة"),
    ],
    "why_correct": [
        "ب<bdi>patient</bdi> بمرحلة نهائية مصنّف مسبقًا بعدم الإنعاش وغير مؤكد قدرته على تحمّل عملية كبيرة، القرار الأنسب هو عدم <bdi>procedure</bdi> العملية طالما احتمال التحسن الحقيقي <bdi>low</bdi> جدًا مقابل خطورة كبيرة.",
        "<bdi>procedure</bdi> عملية كبيرة بفائدة غير مؤكدة على <bdi>patient</bdi> بهذي الـ<bdi>case</bdi> يُعتبر <bdi>treatment</bdi> عبثي (<bdi>futile intervention</bdi>) يزيد المعاناة بدون فائدة حقيقية متوقعة.",
        "قرار عدم الإنعاش المسبق يعكس أصلًا <bdi>assessment</bdi> شامل سابق لتوقعات الـ<bdi>patient</bdi> السيئة، وهذا يدعم منطقيًا تجنّب تدخل جراحي كبير غير مضمون الفائدة.",
    ],
    "when_changes": [
        "لو كان هناك احتمال معقول وواضح للتحسن بعد العملية مع تحمّل جيد متوقع، يصير النقاش حول الخيارات العلاجية مبررًا أكثر.",
        "لو رغب الـ<bdi>patient</bdi> نفسه (وهو مؤهل عقليًا) بالمخاطرة رغم الشرح الكامل للمخاطر، يُحترم قراره المستنير بعد نقاش صريح وموثّق.",
    ],
    "rule": "ب<bdi>patient</bdi> بمرحلة نهائية و<bdi>results</bdi> غير مؤكدة لعملية كبيرة الخطورة، تجنّب التدخل الجراحي العبثي هو القرار الأنسب أخلاقيًا.",
    "comparison": None,
    "guideline_note": None,
},
783: {
    "idea": "السؤال معلومة إحصائية صحية عامة عن نسبة انتشار التدخين بين الرجال السعوديين البالغين، والمصدر المعتمد بهالبنك يحدد النسبة تحديدًا.",
    "clues": [
        ("percentage prevalence of smoking among Saudi adult men", "سؤال إحصائي مباشر عن نسبة انتشار محددة"),
    ],
    "why_correct": [
        "حسب المصادر الوطنية المستخدمة بهذا البنك، نسبة انتشار التدخين بين الرجال البالغين بالسعودية تقارب <bdi>21%</bdi>.",
        "هذي المعرفة مهمة لفهم حجم المشكلة الصحية العامة وتوجيه برامج الوقاية والتوعية بمكافحة التدخين على المستوى الوطني.",
        "النسب الأخرى المطروحة (11%، 37%، 51%) بعيدة عن الرقم المعتمد بهذا السياق الإحصائي.",
    ],
    "when_changes": [
        "لو تغيّرت بيانات المسح الوطني بمصدر أحدث رسميًا، ممكن تختلف النسبة المعتمدة مستقبلًا.",
        "لو السؤال عن نسبة التدخين بين النساء بدل الرجال، يختلف الرقم المطلوب تمامًا.",
    ],
    "rule": "معرفة النسب الوطنية لانتشار التدخين مهمة لفهم حجم المشكلة الصحية العامة وتوجيه جهود الوقاية.",
    "comparison": None,
    "guideline_note": None,
},
784: {
    "idea": "مدخّن طويل الأمد ما عنده أي نية للإقلاع حاليًا، والسؤال يبي أفضل تدخل يناسب مرحلة استعداده هذي تحديدًا، مو خطوات تناسب شخص جاهز للإقلاع فعليًا.",
    "clues": [
        ("smoking 1-pack of cigarettes a day for 22 years", "تدخين <bdi>chronic</bdi> طويل الأمد"),
        ("He has no intention of quitting and feels fine", "غياب تام للنية بالإقلاع، مرحلة ما قبل التفكير بالتغيير"),
    ],
    "why_correct": [
        "ب<bdi>patient</bdi> ما عنده أي نية للإقلاع، الـ<bdi>step</bdi> الأنسب هي إعطاء نصيحة واضحة وشخصية (<bdi>clear, personalized advice to quit</bdi>) توضح له مخاطر التدخين على صحته بالذات.",
        "هذا يتماشى مع <bdi>step</bdi> \"Advise\" من نهج الـ5A's، وهي مناسبة لكل المدخنين بغض النظر عن استعدادهم، بعكس خطوات لاحقة تحتاج استعداد فعلي للتغيير.",
        "تحديد موعد إقلاع أو وصف <bdi>treatment</bdi> بديل النيكوتين أو الإحالة لبرامج إقلاع كلها خطوات تناسب <bdi>patient</bdi> جاهز فعليًا للتغيير، وهذا مو موجود هنا.",
    ],
    "when_changes": [
        "لو أبدى الـ<bdi>patient</bdi> استعداد حقيقي ورغبة بالإقلاع خلال الأشهر القادمة، تصير الخطوات العملية (تحديد موعد، <bdi>treatment</bdi> بديل، إحالة) مناسبة.",
        "لو كان الـ<bdi>patient</bdi> بمرحلة الإقلاع الفعلي وبدأ فعلًا، يصير دعم الاستمرارية ومنع الانتكاسة هو التركيز.",
    ],
    "rule": "ب<bdi>patient</bdi> بمرحلة ما قبل التفكير بالإقلاع، النصيحة الواضحة والشخصية هي التدخل الأنسب، بينما الخطوات العملية تُحجز لمن أبدى استعداد فعلي للتغيير.",
    "comparison": None,
    "guideline_note": None,
},
785: {
    "idea": "<bdi>patient</bdi> مدخّن اعترف إن التدخين مضر لصحته ويخطط يقلع هالسنة، وهذا يعكس مرحلة معينة بنموذج مراحل التغيير السلوكي، وهي مرحلة التفكير الجدي بدون خطة تنفيذ فورية.",
    "clues": [
        ("acknowledged that smoking is not good for his health", "وعي بالمشكلة، <bdi>step</bdi> أولى بمراحل التغيير"),
        ("plans to quit this year", "نية بالتغيير خلال فترة قريبة نسبيًا بدون التزام بخطوات فورية محددة"),
    ],
    "why_correct": [
        "الاعتراف بالمشكلة مع نية بالتغيير خلال فترة (عادة تُعرّف بأقل من 6 أشهر بنموذج مراحل التغيير) بدون خطة تنفيذ فورية يطابق مرحلة <bdi>contemplation</bdi> (التفكير الجدي).",
        "هذي المرحلة تختلف عن مرحلة ما قبل التفكير اللي فيها الـ<bdi>patient</bdi> ما يعترف أصلًا بوجود مشكلة، وعن مرحلة التحضير اللي فيها خطوات فعلية عملية قريبة جدًا.",
        "معرفة المرحلة الصحيحة مهمة لأنها توجه نوع الدعم المناسب: هنا يحتاج تعزيز الدافع والمناقشة أكثر من تقديم خطة عملية فورية.",
    ],
    "when_changes": [
        "لو حدد الـ<bdi>patient</bdi> تاريخ محدد قريب جدًا (خلال 30 يوم) وبدأ خطوات فعلية، تصير مرحلته التحضير مو التفكير الجدي.",
        "لو رفض الـ<bdi>patient</bdi> الاعتراف إن التدخين مشكلة أصلًا، تصير مرحلته ما قبل التفكير.",
    ],
    "rule": "الاعتراف بضرر التدخين مع نية بالإقلاع خلال أشهر قادمة بدون خطة فورية يمثل مرحلة التفكير الجدي بنموذج مراحل التغيير.",
    "comparison": None,
    "guideline_note": None,
},
786: {
    "idea": "السؤال يميّز بين تأثيرات النيكوتين نفسه وتأثيرات باقي مكونات دخان التبغ، والنيكوتين تحديدًا مسؤول بشكل أساسي عن الإدمان مو عن الـ<bdi>diseases</bdi> الجسدية الـ<bdi>chronic</bdi>.",
    "clues": [
        ("thousands of chemical compounds including nicotine", "التمييز بين النيكوتين كمكوّن واحد وباقي مكونات الدخان الضارة"),
    ],
    "why_correct": [
        "<bdi>Addiction</bdi> هو التأثير الأكثر ارتباطًا مباشرة بالنيكوتين نفسه، لأنه المادة المسؤولة عن التعلق النفسي والجسدي بالتدخين.",
        "أما <bdi>diseases</bdi> مثل <bdi>COPD</bdi> وسرطان الرئة و<bdi>diseases</bdi> القلب فهي ناتجة بشكل رئيسي عن مواد أخرى بدخان التبغ (القطران والمواد المسرطنة وأول أكسيد الكربون) مو النيكوتين نفسه.",
        "هذا التمييز مهم سريريًا لأنه يفسر لماذا تُستخدم بدائل النيكوتين (لصقات أو علكة) بأمان نسبي ب<bdi>treatment</bdi> الإدمان، رغم إن النيكوتين نفسه هو مصدر الإدمان.",
    ],
    "when_changes": [
        "لو السؤال يبي التأثير المرتبط بالقطران أو المواد المسرطنة تحديدًا، يصير الجواب سرطان الرئة.",
        "لو السؤال يبي التأثير المرتبط بأول أكسيد الكربون تحديدًا، يصير الجواب <bdi>diseases</bdi> القلب.",
    ],
    "rule": "النيكوتين هو المسؤول الرئيسي عن الإدمان بالتدخين، بينما باقي مكونات دخان التبغ مسؤولة عن الـ<bdi>diseases</bdi> الجسدية الـ<bdi>chronic</bdi> مثل الانسداد الرئوي والسرطان و<bdi>diseases</bdi> القلب.",
    "comparison": None,
    "guideline_note": None,
},
787: {
    "idea": "السؤال يبي أي تدخل من الخيارات المطروحة له أدلة علمية معتمدة فعلًا بمساعدة الإقلاع عن التدخين، بعكس التدخلات البديلة الغير مثبتة.",
    "clues": [
        ("most approved evidence-based intervention", "يبي التدخل المدعوم بأدلة علمية قوية تحديدًا"),
    ],
    "why_correct": [
        "<bdi>Varenicline</bdi> دواء معتمد ومثبت فعاليته بالدراسات العلمية القوية بمساعدة الإقلاع عن التدخين، ويُستخدم ك<bdi>treatment</bdi> دوائي معياري بعيادات الإقلاع.",
        "هذا يجعله من الخيارات القليلة المذكورة اللي فعلًا لها أساس علمي صلب مقارنة بالتدخلات البديلة غير المثبتة علميًا.",
        "التنويم المغناطيسي والوخز بالإبر وأجهزة الرنين الحيوي (BICOM) كلها تدخلات بديلة بدون أدلة علمية كافية تدعم فعاليتها بالإقلاع عن التدخين.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> يفضّل <bdi>treatment</bdi> غير دوائي أولًا، يمكن البدء ببدائل النيكوتين أو الدعم السلوكي قبل الانتقال لفارينيكلين.",
        "لو كان هناك مانع طبي لاستخدام فارينيكلين، يصير بوبروبيون أو بدائل النيكوتين خيارات دوائية معتمدة بديلة.",
    ],
    "rule": "فارينيكلين من التدخلات الدوائية المعتمدة والمثبتة علميًا بفعاليتها لمساعدة الإقلاع عن التدخين، بعكس التدخلات البديلة غير المثبتة.",
    "comparison": None,
    "guideline_note": None,
},
788: {
    "idea": "السؤال يبي أكثر <bdi>procedure</bdi> وقائي يحسّن توقعات الـ<bdi>patient</bdi> بعد <bdi>myocardial infarction</bdi>، ومن بين كل خيارات الوقاية الثانوية، الإقلاع عن التدخين له الأثر الأكبر على تحسين البقيا.",
    "clues": [
        ("improve post-myocardial infarction prognosis", "يبي الـ<bdi>procedure</bdi> الأكثر تأثيرًا على الـ<bdi>results</bdi> طويلة المدى بعد الاحتشاء"),
    ],
    "why_correct": [
        "الإقلاع عن التدخين (<bdi>smoking cessation</bdi>) يعطي أكبر تقليل نسبي ب<bdi>risk</bdi> الوفاة والاحتشاء المتكرر مقارنة بباقي <bdi>procedures</bdi> الوقاية الثانوية بعد احتشاء القلب.",
        "التدخين يسرّع <bdi>atherosclerosis</bdi> ويزيد تجلط الدم بشكل مباشر، فإيقافه يقلل هذا الـ<bdi>risk</bdi> بشكل كبير وسريع نسبيًا بعد الاحتشاء.",
        "خفض الشحوم والتمرين المنتظم والوزن المثالي كلها مفيدة ومهمة، لكن الأثر الإحصائي للإقلاع عن التدخين على تحسين البقيا يبقى الأكبر من بينها.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> غير مدخّن أصلًا، يصير التركيز على خفض الشحوم والتمرين المنتظم كأهم <bdi>procedures</bdi> وقائية متاحة له.",
        "لو كان الـ<bdi>patient</bdi> يعاني سمنة مفرطة مع <bdi>factors</bdi> <bdi>risk</bdi> متعددة أخرى، تصير كل الـ<bdi>procedures</bdi> مجتمعة (شاملة إنقاص الوزن) ضرورية بنفس الوقت.",
    ],
    "rule": "الإقلاع عن التدخين هو أكثر <bdi>procedure</bdi> وقائي فردي يحسّن توقعات الـ<bdi>patient</bdi> بعد <bdi>myocardial infarction</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
789: {
    "idea": "السؤال يبي الترتيب الصحيح والدقيق لخطوات نهج الـ5A's المستخدم بإرشاد المرضى نحو الإقلاع عن التدخين.",
    "clues": [
        ("the 5 A's approach during smoking cessation counselling", "نهج محدد له ترتيب ومكونات ثابتة معروفة"),
    ],
    "why_correct": [
        "الترتيب الصحيح لنهج الـ5A's هو: <bdi>Ask</bdi> (اسأل عن <bdi>case</bdi> التدخين)، ثم <bdi>Advise</bdi> (انصح بالإقلاع بوضوح)، ثم <bdi>Assess</bdi> (قيّم الاستعداد للإقلاع)، ثم <bdi>Assist</bdi> (ساعد بخطة عملية)، وأخيرًا <bdi>Arrange follow-up</bdi> (رتّب <bdi>follow-up</bdi>).",
        "هذا الترتيب منطقي: ما تقدر تساعد أو تخطط قبل ما تعرف <bdi>case</bdi> الـ<bdi>patient</bdi> وتقيّم استعداده أولًا.",
        "باقي الخيارات المطروحة تحتوي كلمة \"advocate\" اللي أصلًا مو من مكونات الـ5A's الحقيقية، وترتيبها غير صحيح أيضًا.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> ما عنده استعداد للإقلاع بعد <bdi>step</bdi> \"Assess\"، يُكتفى بتعزيز الدافع بدل الانتقال المباشر ل<bdi>step</bdi> \"Assist\" العملية.",
        "لو الـ<bdi>patient</bdi> غير مدخّن أصلًا من البداية (<bdi>result</bdi> سؤال \"Ask\" سلبية)، تنتهي الحاجة لباقي خطوات النهج بهذا السياق.",
    ],
    "rule": "نهج الـ5A's الصحيح لإقلاع التدخين بالترتيب هو: Ask, Advise, Assess, Assist, Arrange follow-up.",
    "comparison": None,
    "guideline_note": None,
},
}

WHY_WRONG = {
693: {
    "A": "السمنة وحدها ما تفسر انخفاض FSH وLH والتستوستيرون والـ<bdi>prolactin</bdi> مع وجود ورم نخامي واضح.",
    "B": "الـ<bdi>prolactin</bdi> <bdi>normal</bdi> فعليًا (450 وأقل من 652)، ولو كان ورم <bdi>prolactin</bdi> لكان <bdi>elevated</bdi> جدًا.",
    "C": "<bdi>hypothyroidism</bdi> الأولي يعطي TSH <bdi>elevated</bdi> مو <bdi>low</bdi>؛ هنا TSH <bdi>low</bdi> مع T4 <bdi>low</bdi>، نمط مركزي.",
},
694: {
    "A": "أخذ عينات الجيب الصخري يُحجز لو الـMRI طلع سلبي أو غير حاسم، مو <bdi>step</bdi> أولى.",
    "B": "تصوير الصدر والبطن يُستخدم بالبحث عن مصدر خارج النخامية، وهذا يأتي بعد استبعاد المصدر النخامي أولًا.",
    "D": "مسح الأوكتريوتيد يُستخدم بالبحث عن أورام عصبية صماوية نادرة خفية، <bdi>step</bdi> متأخرة جدًا بالـ<bdi>assessment</bdi>.",
},
695: {
    "A": "الكالسيتونين <bdi>sign</bdi> ورمية لسرطان الدرقية النخاعي، ما له علاقة ب<bdi>assessment</bdi> <bdi>cause</bdi> <bdi>osteoporosis</bdi> هنا.",
    "B": "الديكسا يقيس شدة <bdi>osteoporosis</bdi> بس ما يحدد الـ<bdi>cause</bdi> وراءها.",
    "C": "IGF1 يُستخدم للبحث عن خلل هرمون النمو، وهذا مو الموجّه الأقوى من <bdi>signs</bdi> الـ<bdi>patient</bdi> السريرية هنا.",
},
696: {
    "A": "مسح MIBG فحص متخصص يُحجز لتأكيد فيوكروموسيتوما مؤكد، مو فحص أولي.",
    "B": "الرنين المغناطيسي ما يضيف معلومة وظيفية جديدة بعد ما التصوير الأول وصف الكتلة بأنها حميدة.",
    "C": "الإحالة الجراحية سابقة لأوانها قبل إكمال الفحص الوظيفي الأساسي.",
},
697: {
    "B": "نسبة الـ<bdi>aldosterone</bdi> للرينين تفحص فرط الـ<bdi>aldosterone</bdi>، وهذا مو أخطر احتمال يهدد الجراحة زي الفيوكروموسيتوما.",
    "C": "الخزعة بالإبرة الدقيقة غير مستحسنة بكتلة كظرية مشبوهة ب<bdi>cause</bdi> <bdi>risk</bdi> أزمة كاتيكولامينات أو انتشار الورم.",
    "D": "مسح البوزيترون يُستخدم لل<bdi>assessment</bdi> الورمي وليس لاستبعاد فيوكروموسيتوما قبل الجراحة.",
},
698: {
    "B": "المتلازمة النفريتية تتميز بدم بول نشط وضغط <bdi>elevated</bdi> أكثر من البروتينيوريا الثقيلة، وهذا عكس الصورة هنا.",
    "C": "المتلازمة النفروزية <bdi>diagnosis</bdi> قريب جدًا بالصورة المخبرية، لكن مفتاح الملف يعتمد التصنيف كإصابة أنبوبية خلالية بهذا السياق.",
    "D": "الـ<bdi>nephropathy</bdi> الإقفاري لا يفسر هذا المستوى من فقد البروتين والأجسام الدهنية بالبول.",
},
699: {
    "A": "توسع الأنابيب مع الالتهاب يصف التهاب الكلى الخلالي، مو RPGN.",
    "C": "ترسب IgA سمة مميزة ل<bdi>disease</bdi> IgA nephropathy تحديدًا، مو التعريف العام لـRPGN.",
    "D": "الأجسام الدهنية بالبول <bdi>sign</bdi> نفروزية، مو تغيّر نسيجي لـRPGN.",
},
700: {
    "A": "فرط شرب الماء يعطي أسمولية بول <bdi>low</bdi> جدًا (أقل من 100)، مو 310 المذكورة.",
    "B": "أديسون يعطي عادة بوتاسيوم <bdi>elevated</bdi> وهبوط ضغط واضح، وهذا عكس الصورة هنا (بوتاسيوم <bdi>low</bdi>).",
    "C": "الكرياتينين <bdi>normal</bdi> (80)، يبعد اعتلال كلوي <bdi>diabetes</bdi> ك<bdi>cause</bdi> مباشر لهذا الخلل بالصوديوم.",
},
701: {
    "A": "محلول السكر 5% يزيد الماء الحر ويفاقم نقص الصوديوم بدل تصحيحه.",
    "B": "المحلول الملحي العادي غالبًا يُطرح بالبول المركز أصلًا ب<bdi>case</bdi> SIADH وقد يزيد النقص سوء أحيانًا.",
    "D": "نصف المحلول الملحي أخف تركيزًا من اللازم ويعطي ماء حر إضافي غير مرغوب هنا.",
},
702: {
    "A": "قصور ما قبل الكلى عادة يرتبط بجفاف أو هبوط ضغط، مو تعرض مباشر لصبغة وريدية بهذا التوقيت.",
    "C": "التهاب الكلى الخلالي الـ<bdi>acute</bdi> يحتاج عادة <bdi>cause</bdi> حساسية دوائية مع حمى وطفح، وهذا غير مذكور.",
    "D": "التهاب كبيبي <bdi>acute</bdi> يعطي عادة دم وبروتين بول وضغط <bdi>elevated</bdi>، وهذا غير موصوف بالسؤال.",
},
703: {
    "B": "<bdi>disease</bdi> الكلى متعددة الكيسات يظهر عادة بكتل بطنية محسوسة أو بالتصوير، وغير مذكور هنا.",
    "C": "تضيق الأبهر يعطي فرق ضغط بين الأطراف العلوية والسفلية، وغير موصوف بالسؤال.",
    "D": "الضغط الأساسي وحده ما يفسر انخفاض البوتاسيوم الـ<bdi>severe</bdi> وغير المرتبط بدواء.",
},
704: {
    "B": "الـ<bdi>nephropathy</bdi> الغشائي يعطي صورة نفروزية <bdi>chronic</bdi>، مو دم بول <bdi>acute</bdi> بعد عدوى مباشرة.",
    "C": "التهاب الكلى ما بعد العقديات له فترة كمون أطول بكثير (أسابيع) مو يوم واحد.",
    "D": "التصلب القطعي البؤري يعطي صورة نفروزية مو دم بول <bdi>acute</bdi> مرتبط بعدوى حلق حديثة.",
},
705: {
    "A": "التهاب الشرايين ذو الخلايا العملاقة يصيب كبار السن ب<bdi>symptoms</bdi> صداع وبصر، مو هذا الطيف من الـ<bdi>symptoms</bdi>.",
    "B": "التهاب الشرايين متعدد العقد نادرًا ما يصيب الكبيبات ولا يسبب نزيف رئوي بهذا الشكل.",
    "C": "فرفرية هينوخ شونلاين أشيع بالأطفال وتصاحبها فرفرية جلدية، وغير مذكورة هنا.",
},
706: {
    "B": "بيكربونات الصوديوم أقل فعالية وأبطأ من الكالسيوم بحماية القلب فورًا.",
    "C": "الـ<bdi>insulin</bdi> والجلوكوز يخفضون البوتاسيوم بس ما يحمون القلب فورًا مثل الكالسيوم.",
    "D": "الديلزة <bdi>treatment</bdi> نهائي فعال لكنه يحتاج وقت للتحضير والبدء، مو الـ<bdi>step</bdi> الفورية الأولى.",
},
707: {
    "A": "حصوة الكلى تسبب ألم <bdi>severe</bdi> موضعي، وغير متوافقة مع تاريخ التهاب حلق سابق وفترة كمون كهذي.",
    "B": "ورم الكلى (Hypernephroma) نادر بهذا العمر ويعطي صورة مختلفة تمامًا بدون ارتباط بعدوى حلق.",
    "C": "IgA nephropathy فترة كمونه أقصر بكثير (يوم أو يومين) مو 3 أسابيع.",
},
708: {
    "A": "زيادة الـ<bdi>furosemide</bdi> تزيد الجفاف الموجود أصلًا وتسوّي <bdi>renal failure</bdi> أسوأ.",
    "B": "الدوبوتامين يُستخدم بالـ<bdi>congestion</bdi> القلبي، وهذي الصورة نقص حجم مو <bdi>congestion</bdi> (JVP وCVP منخفضين).",
    "D": "زيادة الـ<bdi>spironolactone</bdi> تزيد البوتاسيوم الـ<bdi>elevated</bdi> أصلًا (5.5) وتزيد الجفاف سوء.",
},
709: {
    "B": "عدم التغيير غير كافٍ لأن الوذمة مستمرة ومزعجة وتحتاج تعديل علاجي فعلي.",
    "C": "إضافة حاصرات بيتا لا تعالج احتباس السوائل ولا تفيد هذي الـ<bdi>case</bdi> تحديدًا.",
    "D": "رامبريل حامي للكلى ب<bdi>patient</bdi> <bdi>diabetes</bdi> نفروباثي والوظيفة الكلوية مستقرة، فما فيه داعي لإيقافه.",
},
710: {
    "A": "الطعم الوعائي بديل يُستخدم لو الأوعية لا تسمح بعمل ناسور، مو الخيار الأول.",
    "C": "القسطرة النفقية تُستخدم لو الحاجة عاجلة قبل جاهزية الناسور، مو وصول دائم مثالي.",
    "D": "القسطرة غير النفقية للاستخدام المؤقت جدًا فقط، ليست وصول دائم مناسب.",
},
711: {
    "A": "رقم تصفية <bdi>low</bdi> وحده بدون <bdi>symptoms</bdi> أو شوارد خطيرة ليس مؤشر إسعافي قاطع.",
    "C": "بول قليل جدًا مهم لكنه أقل إلحاحًا من فرط بوتاسيوم مقاوم لل<bdi>treatment</bdi> بحد ذاته بهذا السياق.",
    "D": "تكرار الإصابة الكلوية سابقًا تاريخ مرضي بس مو مؤشر إسعافي حالي بذاته.",
},
712: {
    "A": "الأسيتيل سيستين الفموي أدلته أضعف بكثير من الترطيب الوريدي المباشر.",
    "B": "البيكربونات الفموي أدلته أضعف وأقل استخدامًا مقارنة بالمحلول الملحي الوريدي.",
    "C": "الـ<bdi>furosemide</bdi> الوريدي قبل الـ<bdi>procedure</bdi> يزيد الجفاف وقد يرفع <bdi>risk</bdi> تسمم الصبغة بدل تقليله.",
},
713: {
    "A": "الديلزة <bdi>treatment</bdi> نهائي مهم لكنه يحتاج وقت للترتيب، مو الـ<bdi>step</bdi> الفورية الأولى مع تغيّرات تخطيط قلب خطيرة.",
    "B": "السالبوتامول ينقل البوتاسيوم داخل الخلايا لكنه أبطأ من الكالسيوم بحماية القلب مباشرة.",
    "C": "الـ<bdi>insulin</bdi> والجلوكوز يخفضون البوتاسيوم لكن لا يحمون غشاء القلب فورًا مثل الكالسيوم عند وجود تغيّرات تخطيط قلب.",
},
714: {
    "A": "الديلزة تُحجز لفشل الـ<bdi>treatment</bdi> الدوائي أو وجود مؤشرات إسعافية أقوى، مو الـ<bdi>step</bdi> الأولى هنا.",
    "B": "البيكربونات الوريدي أدلته أضعف ومو الـ<bdi>treatment</bdi> الأولي المفضل لفرط البوتاسيوم البسيط بدون تغيّرات تخطيط قلب.",
    "D": "المحلول الملحي العادي لا يخفض البوتاسيوم مباشرة، فهو غير كافٍ ك<bdi>treatment</bdi> أولي لفرط البوتاسيوم.",
},
715: {
    "B": "الحمية <bdi>low</bdi> البروتين غير فعالة وقد تضر التغذية، وليست <bdi>treatment</bdi> نوعي لل<bdi>disease</bdi>.",
    "C": "عدم الـ<bdi>treatment</bdi> غير مناسب لأن <bdi>disease</bdi> التغيّر الأدنى يحتاج <bdi>treatment</bdi> نوعي فعّال (الستيرويد) وليس مجرد مراقبة.",
    "D": "مثبطات الإنزيم المحول <bdi>treatment</bdi> داعم لتقليل البروتينيوريا لكنه ليس الـ<bdi>treatment</bdi> النوعي الأساسي لهذا الـ<bdi>disease</bdi> بالذات.",
},
716: {
    "A": "نسبة الـ<bdi>aldosterone</bdi> للرينين تفحص <bdi>cause</bdi> هرموني، وهذا مو السياق الأقوى هنا مع <bdi>patient</bdi> كرون وسوء امتصاص واضح.",
    "C": "الـ<bdi>spironolactone</bdi> لا يعالج نقص البوتاسيوم الناتج عن نقص مغنيسيوم، وقد يكون غير مناسب أصلًا هنا.",
    "D": "المراقبة بدون تدخل غير مناسبة ل<bdi>case</bdi> نقص بوتاسيوم مقاوم يحتاج تصحيح فعلي (المغنيسيوم).",
},
717: {
    "A": "الانتظار 6 أشهر غير كافٍ هنا لأن البروتينيوريا والضغط الـ<bdi>elevated</bdi> الجديد يحتاجان تدخل دوائي عاجل يحمي الكلى.",
    "B": "التحكم <bdi>diabetes</bdi> الحالي مقبول (HbA1c 7%)، فزيادة الـ<bdi>insulin</bdi> ليست الأولوية مقارنة بحماية الكلى.",
    "D": "حاصرات بيتا (<bdi>atenolol</bdi>) ليست الخيار الأول لضغط مرتبط باعتلال كلوي <bdi>diabetes</bdi> مقارنة بمثبطات الإنزيم المحول.",
},
718: {
    "A": "الألوبيورينول يُستخدم لحصوات حمض اليوريك، مو لفرط كالسيوم البول.",
    "B": "البنسيلامين يُستخدم لحصوات السيستين تحديدًا، غير مرتبط بفرط كالسيوم البول.",
    "D": "تقييد الكالسيوم الغذائي فكرة خاطئة، لأنه يزيد امتصاص الأوكسالات ويرفع <bdi>risk</bdi> الحصوات فعليًا.",
},
719: {
    "A": "الإريثروبويتين يعالج <bdi>anemia</bdi> لكنه لا يعالج الـ<bdi>neuropathy</bdi> اليوريمي المتقدم.",
    "B": "بيكربونات فموية تصحح الحموضة البسيطة، وهذا مو المشكلة الأساسية المطروحة هنا.",
    "C": "فيتامين B مفيد لاعتلال عصبي غذائي، لكن الصورة هنا يوريمية متقدمة تحتاج إزالة السموم فعليًا.",
},
720: {
    "A": "الأجسام المضادة لـDs-DNA <bdi>sign</bdi> نشاط مفيدة لكنها لا تحدد نوع أو درجة التهاب الكلى الذئبي.",
    "C": "دوبلر الكلى يقيّم مشاكل وعائية أو انسدادية، مو أداة <bdi>diagnosis</bdi> التهاب الكلى الذئبي.",
    "D": "تكرار فحص البول فقط بدون خزعة يؤخر <bdi>diagnosis</bdi> و<bdi>treatment</bdi> قد يكون عاجل.",
},
721: {
    "A": "الموجات فوق الصوتية على الكلى غير ضرورية بهذي المرحلة المبكرة من الألبومينيوريا.",
    "C": "لا يوجد مؤشر لقصور كلوي يستدعي إيقاف الـ<bdi>metformin</bdi>، والكرياتينين <bdi>normal</bdi>.",
    "D": "جمع بول 24 ساعة أكثر تعقيدًا وغير ضروري بينما نسبة الألبومين للكرياتينين كافية للتأكيد بإعادتها.",
},
722: {
    "A": "<bdi>disease</bdi> بيرغر هو نفسه IgA nephropathy، وفترة كمونه أقصر بكثير من 3 أسابيع.",
    "B": "IgA nephropathy فترة كمونه يوم أو يومين، مو 3 أسابيع كما بالسؤال.",
    "D": "الـ<bdi>nephropathy</bdi> الغشائي يعطي صورة نفروزية <bdi>chronic</bdi> تدريجية، مو نفريتية <bdi>acute</bdi> بعد عدوى مباشرة.",
},
723: {
    "A": "<bdi>renal failure</bdi> هو <bdi>cause</bdi> الحاجة للديلزة، لكنه ليس الـ<bdi>cause</bdi> الأشيع للوفاة إحصائيًا مقارنة ب<bdi>diseases</bdi> القلب الوعائية.",
    "B": "<bdi>coagulopathy</bdi> ليس <bdi>cause</bdi> الوفاة الأشيع بمرضى الكلى الـ<bdi>chronic</bdi>.",
    "C": "الـ<bdi>congestion</bdi> الرئوي <bdi>complication</bdi> ممكنة لكنه جزء من طيف <bdi>diseases</bdi> القلب الوعائية الأوسع اللي هي الـ<bdi>cause</bdi> الأشمل والأشيع.",
},
724: {
    "B": "متلازمة كوشينغ تعطي <bdi>signs</bdi> جسدية أخرى (سمنة مركزية وخطوط أرجوانية) غير مذكورة هنا، وما تفسر اختلاف حجم الكليتين.",
    "C": "فرط الـ<bdi>aldosterone</bdi> الأولي عادة كليتان متماثلتان بالحجم مع بوتاسيوم <bdi>low</bdi>، وغير مذكور هنا.",
    "D": "<bdi>disease</bdi> الكلى متعددة الكيسات يعطي كليتين متضخمتين بكيسات متعددة، وليس مجرد \"اختلاف حجم\" بسيط.",
},
725: {
    "A": "العنب من الفواكه <bdi>low</bdi> البوتاسيوم نسبيًا، فهو خيار آمن بكميات معتادة.",
    "C": "الفاصوليا الخضراء <bdi>low</bdi> إلى متوسطة البوتاسيوم، أأمن من الطماطم.",
    "D": "عصير التوت البري <bdi>low</bdi> البوتاسيوم نسبيًا مقارنة بعصائر أخرى، خيار أأمن.",
},
726: {
    "B": "الدوكسيسيكلين ممنوع أثناء الحمل ب<bdi>cause</bdi> تأثيره على أسنان وعظام الجنين.",
    "C": "النيتروفيورانتوين يُتجنّب قرب الولادة (الثلث الثالث المتأخر) ل<bdi>risk</bdi> انحلال الدم الوليدي.",
    "D": "زيادة السوائل وحدها غير كافية ل<bdi>treatment</bdi> عدوى بولية مؤكدة، تحتاج مضاد حيوي فعلي.",
},
727: {
    "A": "الأشعة المقطعية أدق لكنها تحمل إشعاع وتكلفة أعلى، وغير ضرورية كفحص فحص أول.",
    "B": "فحص البول المجهري غير حساس ولا كافٍ للكشف عن الكيسات الكلوية.",
    "D": "الأجسام المضادة لـpolycystin 1 ليست فحص كشف روتيني معتمد لهذا الـ<bdi>disease</bdi>.",
},
728: {
    "A": "النيتروفيورانتوين تخلصه كلوي ضعيف عند GFR <bdi>low</bdi>، وفعاليته وسميته تتأثران بقصور الكلى.",
    "B": "الـ<bdi>metformin</bdi> يحتاج حذر أو تجنّب بقصور كلوي مرحلة 3 ب<bdi>cause</bdi> <bdi>risk</bdi> الحماض اللاكتيكي.",
    "D": "الليثيوم سام للكلى ويحتاج مراقبة دقيقة جدًا أو تجنّب عند قصور كلوي.",
},
729: {
    "B": "العدوى المرتبطة بالديلزة <bdi>cause</bdi> وفاة معروف لكنه أقل شيوعًا من <bdi>diseases</bdi> القلب الإقفارية.",
    "C": "فرط البوتاسيوم <bdi>risk</bdi> حقيقي لكنه يُدار عادة بجلسات الديلزة المنتظمة، وأقل شيوعًا ك<bdi>cause</bdi> وفاة عام مقارنة ب<bdi>diseases</bdi> القلب.",
    "D": "الأورام تزيد خطرها بمرضى الديلزة لكنها ليست الـ<bdi>cause</bdi> الأشيع للوفاة إحصائيًا.",
},
730: {
    "A": "فلوكلوكساسيلين يغطي الجراثيم موجبة الجرام (زي المكورات العنقودية)، مو الجراثيم البولية الشائعة سالبة الجرام.",
    "C": "سيبروفلوكساسين من الفلوروكينولونات، ممنوع أثناء الحمل ب<bdi>cause</bdi> سميته المحتملة على الغضاريف.",
    "D": "النيتروفيورانتوين خيار معقول بمراحل مبكرة من الحمل لكن أوجمنتين هنا هو المختار حسب الملف لتغطية أوسع.",
},
731: {
    "A": "الـ<bdi>insulin</bdi> ضروري ل<bdi>treatment</bdi> <bdi>diabetes</bdi> ولا يسبب فرط بوتاسيوم، بل يخفضه فعليًا.",
    "C": "الـ<bdi>heparin</bdi> ضروري ل<bdi>treatment</bdi> الـ<bdi>thrombus</bdi> الوريدية العميقة الـ<bdi>acute</bdi>، ولا يوقف لمجرد فرط بوتاسيوم بسيط.",
    "D": "الـ<bdi>furosemide</bdi> مدر يطرح البوتاسيوم فعليًا، فهو يخفض البوتاسيوم مو يرفعه.",
},
732: {
    "A": "فرط جارات الدرقية الأولي يعطي عادة كالسيوم أعلى بكثير، وما يفسر بروتين البول الثقيل جدًا هنا.",
    "B": "الـ<bdi>nephropathy</bdi> الغشائي أقل احتمالًا كتفسير أول مقارنة بالـ<bdi>cause</bdi> الأشيع (<bdi>diabetes</bdi>) عند <bdi>patient</bdi> <bdi>diabetes</bdi> طويل الأمد.",
    "D": "الأميلويد الأولي احتمال وارد لكنه أقل شيوعًا بكثير من الـ<bdi>nephropathy</bdi> <bdi>diabetes</bdi> كتفسير أول ب<bdi>patient</bdi> <bdi>diabetes</bdi>.",
},
733: {
    "A": "أبيكسابان مضاد تخثر يُستخدم لمصادر قلبية للسكتة (ك<bdi>atrial fibrillation</bdi>)، وغير مذكور هنا.",
    "B": "الـ<bdi>warfarin</bdi> نفس منطق أبيكسابان، يحتاج مصدر قلبي واضح غير موجود بالسؤال.",
    "D": "الـt-PA <bdi>treatment</bdi> <bdi>acute</bdi> بنافذة زمنية قصيرة جدًا (ساعات)، والسكتة هنا عمرها 10 أيام.",
},
734: {
    "A": "<bdi>multiple sclerosis</bdi> يعطي التهاب عصب بصري مؤلم أطول أمدًا، مو نوبة عابرة تزول تلقائيًا خلال 20 دقيقة.",
    "B": "انفصال الشبكية يعطي فقدان بصر دائم مع ومضات وذباب طائر، مو نوبة عابرة تعود <bdi>normal</bdi> بسرعة.",
    "C": "الاضطراب التحولي <bdi>diagnosis</bdi> إقصائي غير مناسب هنا مع وجود <bdi>factor</bdi> <bdi>risk</bdi> وعائي واضح (<bdi>diabetes</bdi>).",
},
735: {
    "A": "اعتلال عصب مفرد يصيب توزيع عصب واحد محدد، مو ضعف منتشر بكل الأطراف والبصلة.",
    "B": "الوهن العضلي الوبيل يعطي ضعف متقلب بدون <bdi>signs</bdi> عصبون علوي مثل المنعكسات النشطة.",
    "C": "المتلازمة الوهنية العضلية (لامبرت إيتون) تعطي ضعف يتحسن بالجهد، بدون <bdi>signs</bdi> عصبون علوي أيضًا.",
},
736: {
    "A": "الإنترفيرون <bdi>treatment</bdi> وقائي طويل المدى، والـ<bdi>patient</bdi> عليه أصلًا، فهو لا يعالج النوبة الـ<bdi>acute</bdi> الحالية.",
    "C": "الغلوبولين المناعي الوريدي ليس الخط الأول ل<bdi>treatment</bdi> نوبة <bdi>multiple sclerosis</bdi> الـ<bdi>acute</bdi>.",
    "D": "الستيرويد الوريدي أسرع وأقوى تأثيرًا من الفموي بالنوبات الـ<bdi>acute</bdi> المصحوبة ب<bdi>symptoms</bdi> مقلقة كهذي.",
},
737: {
    "A": "المخيخ يسبب رعاش قصدي و<bdi>ataxia</bdi>، مو رجفان بالراحة وبطء حركة.",
    "B": "الفص الجبهي يسبب تغيّر شخصية وخلل تنفيذي، مو هذي الصورة الحركية المميزة.",
    "C": "البطين الجانبي مرتبط باستسقاء الدماغ، مو بآلية <bdi>Parkinson's disease</bdi> المباشرة.",
},
738: {
    "B": "خلل الحركة المتأخر ناتج عن أدوية مضادة لل<bdi>psychosis</bdi> ويعطي حركات لا إرادية مختلفة، مو هذي الصورة.",
    "C": "<bdi>Alzheimer's disease</bdi> يبدأ بمشكلة ذاكرة غالبًا بدون هذي الـ<bdi>symptoms</bdi> الحركية الأربعة البارزة.",
    "D": "هنتنغتون يعطي كوريا (حركات لا إرادية) لا بطء حركة، مع تاريخ عائلي مميز.",
},
739: {
    "B": "الفينوباربيتال يُحجز للخط الثالث بعد فشل الفينيتوين، مو الخط الثاني مباشرة.",
    "C": "الإيثوسكسيمايد دواء فموي لنوبات الغياب، لا يُستخدم أصلًا ب<bdi>case</bdi> <bdi>epilepsy</bdi> المستمر.",
    "D": "الكاربامازيبين دواء فموي بطيء المفعول، غير مناسب ل<bdi>case</bdi> إسعافية.",
},
740: {
    "A": "العصب البصري الشوكي (V1) حسي، لا يتحكم بحركة عضلات الوجه.",
    "B": "العصب الفكي العلوي (V2) حسي أيضًا، لا علاقة له بحركة الوجه.",
    "D": "العصب البصري (II) خاص بالرؤية، لا علاقة له بحركة عضلات الوجه.",
},
741: {
    "A": "العصب الإبطي يغذي عضلة الدالية وحس منطقة الكتف، ما له علاقة بوظائف اليد هذي.",
    "B": "العصب الوسيط يسبب <bdi>symptoms</bdi> براحة اليد وضعف قبض الإبهام، مو بسط الرسغ.",
    "D": "العصب الزندي يسبب <bdi>paresthesia</bdi> الخنصر وضعف عضلات اليد الصغيرة، مو بسط الرسغ والأصابع.",
},
742: {
    "A": "الريفاستيجمين يعبر حاجز الدم-الدماغ ويُستخدم لل<bdi>Alzheimer's disease</bdi>، غير مناسب للوهن العضلي.",
    "C": "الفيزوستيجمين يعبر الحاجز الدموي الدماغي ويُستخدم لتسمم الأتروبين، مو <bdi>treatment</bdi> <bdi>chronic</bdi> للوهن العضلي.",
    "D": "الإكوثيوفات دواء موضعي للجلوكوما، لا يُستخدم ل<bdi>treatment</bdi> الوهن العضلي الجهازي.",
},
743: {
    "A": "نقص السكر يعطي <bdi>symptoms</bdi> مختلفة (تعرّق و<bdi>palpitations</bdi> وجوع)، مو هبوط ضغط وضعي بدون تسارع نبض.",
    "B": "الـ<bdi>atenolol</bdi> ممكن يساهم لكن الـ<bdi>cause</bdi> الأعمق المؤكد ب<bdi>patient</bdi> سكرية طويلة الأمد سيئة الضبط هو <bdi>neuropathy</bdi> المستقل.",
    "D": "خلل البطين الأيسر يعطي <bdi>symptoms</bdi> قصور قلب أوضح، مو هبوط ضغط وضعي بدون تسارع نبض.",
},
744: {
    "A": "المسكنات الأفيونية لا تحل المشكلة الأساسية وفيها <bdi>risk</bdi> إدمان طويل المدى.",
    "C": "الاستشارة النفسية دعم مساعد مفيد لكنها ليست الـ<bdi>treatment</bdi> الأساسي الأهم لهذي المتلازمة.",
    "D": "التريبتان دواء خاص ب<bdi>migraine</bdi>، لا علاقة له بمتلازمة الألم الموضعي المعقد.",
},
745: {
    "A": "شلل العصب الثالث يعطي <bdi>ptosis</bdi> وتوسع حدقة وضعف تقريب وتبعيد ورفع وخفض العين معًا، مو فشل تبعيد فقط.",
    "B": "بحسب مفتاح الملف، هذا الخيار غير مطابق للجهة المحددة كإجابة هنا رغم تطابقه مع القاعدة العامة لفشل التبعيد.",
    "C": "شلل العصب الثالث بالجهة المقابلة لا يفسر فشل تبعيد نفس العين المذكورة بالسؤال.",
},
746: {
    "A": "<bdi>Alzheimer's disease</bdi> يبدأ عادة بفقدان ذاكرة أولًا، مو تغيّر شخصية وسلوك كأول <bdi>symptom</bdi> بارز.",
    "B": "الـ<bdi>dementia</bdi> الوعائي يحتاج تاريخ سكتات أو <bdi>factors</bdi> <bdi>risk</bdi> وعائية واضحة، وغير مذكورة هنا.",
    "C": "هنتنغتون يصاحبه حركات كوريّة لا إرادية وتاريخ عائلي واضح، وغير مذكور بالسؤال.",
},
747: {
    "A": "<bdi>multiple sclerosis</bdi> أقل احتمالًا بهذا العمر مع وجود تاريخ جراحي واضح لنفس المشكلة التنكسية.",
    "B": "التهاب النخاع المستعرض <bdi>case</bdi> <bdi>acute</bdi> وليست تدريجية على مدى شهرين ب<bdi>patient</bdi> له تاريخ تنكسي معروف.",
    "C": "متلازمة ذيل الفرس تصيب مستوى قطني عجزي، والجراحة السابقة كانت عنقية، فلا تفسر نفس الآلية.",
},
748: {
    "B": "الـ<bdi>treatment</bdi> الفيزيائي دعم وظيفي لكنه لا يوقف تطور الضغط على النخاع الشوكي.",
    "C": "مسكنات الألم العصبي <bdi>treatment</bdi> عرضي فقط، لا يعالج الـ<bdi>cause</bdi> الميكانيكي المستمر.",
    "D": "الطمأنة غير مناسبة مع استمرار <bdi>symptoms</bdi> عصبية فعلية تستدعي تدخل عاجل.",
},
749: {
    "A": "الـ<bdi>aspirin</bdi> قبل استبعاد النزيف بالأشعة قد يزيد <bdi>risk</bdi> تفاقم نزيف دماغي لو كان موجودًا.",
    "B": "الرنين المغناطيسي أبطأ وأقل توفرًا بالطوارئ مقارنة بالأشعة المقطعية السريعة.",
    "C": "الكلوبيدوجريل نفس مشكلة الـ<bdi>aspirin</bdi>، <bdi>risk</bdi> لو كانت السكتة نزفية غير مستبعدة بعد.",
},
750: {
    "A": "التهاب العضلات المتعدد يعطي ضعف قريب فقط عادة مع منعكسات محفوظة غالبًا، مو غياب كامل للمنعكسات.",
    "B": "الوهن العضلي الوبيل يعطي ضعف متقلب يتحسن بالراحة، بدون غياب للمنعكسات.",
    "C": "التهاب النخاع المستعرض يعطي مستوى حسي واضح واحتباس بولي، وهذا غير موجود هنا.",
},
751: {
    "B": "الـ<bdi>propranolol</bdi> <bdi>treatment</bdi> وقائي للصداع النصفي، مو الخيار الأول للصداع العنقودي.",
    "C": "السوماتريبتان <bdi>treatment</bdi> للنوبة الـ<bdi>acute</bdi> وقت حدوثها، مو للوقاية من تكرارها.",
    "D": "الأكسجين 100% <bdi>treatment</bdi> للنوبة الـ<bdi>acute</bdi> أيضًا، فعّال جدًا لكن مو للوقاية طويلة المدى.",
},
752: {
    "A": "أم الدم بالشريان الموصل الخلفي تسبب توسع حدقة وعدم تفاعلها كلاسيكيًا، وهذا غير موجود هنا (الحدقة سليمة).",
    "C": "التهاب الجيب الكهفي يصيب عادة أكثر من عصب بنفس الوقت مع جحوظ العين، وغير موصوف هنا.",
    "D": "ورم جذع الدماغ عادة يصاحبه <bdi>signs</bdi> عصبية أخرى (ضعف بالجهة المقابلة)، وغير مذكور هنا.",
},
753: {
    "A": "الفينيتوين دواء الخط الثاني بعد فشل البنزوديازيبين، مو الدواء الأول المعطى مباشرة.",
    "C": "الثيوبنتال يُحجز لحالات <bdi>epilepsy</bdi> المستمر المقاومة تحت تخدير كامل، مو الـ<bdi>step</bdi> الأولى.",
    "D": "الفينوباربيتون بديل ثانوي، مو الخيار الأول المعتمد بعد تأمين الطريق الهوائي مباشرة.",
},
754: {
    "A": "الستيرويد أثبتت الدراسات عدم فعاليته ب<bdi>treatment</bdi> متلازمة غيلان باريه تحديدًا.",
    "B": "السيكلوسبورين ليس <bdi>treatment</bdi> معتمد لمتلازمة غيلان باريه.",
    "D": "السيكلوفوسفامايد أيضًا ليس من العلاجات المثبتة فعاليتها بهذا الـ<bdi>disease</bdi>.",
},
755: {
    "A": "تخطيط العضل يفحص الأعصاب والعضلات الطرفية، مو مفيد ل<bdi>diagnosis</bdi> إصابات الجهاز العصبي المركزي المتعددة هذي.",
    "C": "أشعة مقطعية على الصدر الفقري أقل دقة بكثير من الرنين بكشف آفات إزالة الميالين.",
    "D": "دراسة توصيل الأعصاب تفحص الأعصاب الطرفية، ما تكشف آفات الجهاز العصبي المركزي المنتشرة هذي.",
},
756: {
    "A": "<bdi>Alzheimer's disease</bdi> لا يعطي عادة تمدد بطينات بارز أو سلس بولي ومشية غير <bdi>normal</bdi> كسمات أساسية مبكرة.",
    "B": "كروتزفيلد جاكوب يعطي تدهور أسرع بكثير (أسابيع) مع رمع عضلي، مختلف عن هذي الصورة التدريجية.",
    "C": "الـ<bdi>dementia</bdi> الجبهي الصدغي يبدأ بتغيّر شخصية وسلوك أولًا، مو ثلاثية المشي والسلس والإدراك.",
},
757: {
    "B": "هذا الرد يتجاهل احترام رغبة الـ<bdi>patient</bdi> الموثّقة ويبدو غير متعاطف مع مشاعر الابن.",
    "C": "توضيح احترام رغبة الوالد <bdi>step</bdi> مناسبة لاحقًا، لكنها تأتي بعد التأكد من صفة الابن الرسمية أولًا.",
    "D": "التفسير المذكور (برين ديد) غير دقيق طبيًا وغير مطابق لأساس القرار الفعلي (رغبة الـ<bdi>patient</bdi> الموثّقة).",
},
758: {
    "B": "هذا الرد قاسٍ وغير متعاطف إطلاقًا، يتجاهل مشاعر الـ<bdi>patient</bdi> تمامًا.",
    "C": "هذي العبارة تبدو كاعتذار عن خطأ حصل، مو تعبير تعاطف حقيقي مناسب ل<bdi>diagnosis</bdi> مرضي.",
    "D": "الطمأنة الكاذبة غير مناسبة أخلاقيًا ل<bdi>diagnosis</bdi> <bdi>chronic</bdi> جدي مثل <bdi>multiple sclerosis</bdi>.",
},
759: {
    "A": "ب<bdi>disease</bdi> <bdi>Parkinson's disease</bdi> الأصلي، الـ<bdi>dementia</bdi> يظهر عادة متأخر (بعد سنة أو أكثر)، مو مبكر مع تذبذب وهلاوس.",
    "B": "<bdi>Alzheimer's disease</bdi> لا يصاحبه <bdi>parkinsonism</bdi> ولا تذبذب إدراكي ولا هلاوس بصرية بارزة كسمات أساسية.",
    "C": "متلازمة كورتيكوباسال تعطي عدم تناسق حركي وابراكسيا وطرف غريب، مختلفة عن هذي الصورة.",
},
760: {
    "A": "لا يوجد تاريخ كحول مذكور بالسؤال يدعم هذا الـ<bdi>diagnosis</bdi>.",
    "B": "<bdi>dementia</bdi> <bdi>Parkinson's disease</bdi> يحتاج وجود <bdi>symptoms</bdi> <bdi>parkinsonism</bdi> حركية أولًا، وغير مذكورة هنا.",
    "C": "الـ<bdi>dementia</bdi> متعدد الاحتشاءات يحتاج <bdi>factors</bdi> <bdi>risk</bdi> وعائية، والسؤال ينص صراحة على غيابها.",
},
761: {
    "A": "ورم العصب السمعي يصاحبه عادة <bdi>tinnitus</bdi> ودوخة تدريجية أحادية الجانب، وغير مذكور هنا.",
    "C": "فقدان السمع التوصيلي يعطي اختبار رين سلبي بالأذن المصابة، وهنا الاختبار إيجابي بالجهتين.",
    "D": "التهاب الأذن الوسطى المصلي الـ<bdi>chronic</bdi> يعطي أيضًا فقدان سمع توصيلي (رين سلبي)، غير متوافق مع الـ<bdi>result</bdi> هنا.",
},
762: {
    "B": "البزل القطني ليس فحص روتيني أولي ب<bdi>assessment</bdi> <bdi>dementia</bdi> نمطي بدون <bdi>signs</bdi> تحذيرية.",
    "C": "دوبلر الشرايين السباتية يقيّم <bdi>risk</bdi> وعائي، مو الفحص الأولي المعياري ل<bdi>assessment</bdi> الـ<bdi>dementia</bdi> نفسه.",
    "D": "تخطيط الدماغ الكهربائي يُستخدم بالشك بنشاط تشنجي، مو فحص روتيني أولي لل<bdi>dementia</bdi>.",
},
763: {
    "A": "<bdi>Alzheimer's disease</bdi> يعطي عادة ضمور بمنطقة الحُصين بالرنين، مو تغيّرات مادة بيضاء منتشرة حول البطينات.",
    "B": "<bdi>dementia</bdi> أجسام ليوي يصاحبه تذبذب إدراكي وهلاوس بصرية و<bdi>parkinsonism</bdi>، وغير موصوف هنا.",
    "D": "استسقاء الدماغ بضغط <bdi>normal</bdi> يعطي تمدد بطينات بارز، مختلف عن صورة المادة البيضاء هذي.",
},
764: {
    "A": "التهيّج <bdi>symptom</bdi> مزاجي سلوكي، أقل تحديدًا بربطه ب<bdi>risk</bdi> الـ<bdi>dementia</bdi> من ضعف الذاكرة الفعلي.",
    "B": "صعوبة إيجاد الكلمات <bdi>symptom</bdi> لغوي ممكن يحدث ل<bdi>causes</bdi> متعددة، أقل تحديدًا من ضعف الذاكرة الفعلي هنا.",
    "D": "صعوبة القراءة قد تعكس مشاكل انتباه أو بصر أكثر من كونها مؤشر مباشر ل<bdi>risk</bdi> الـ<bdi>dementia</bdi>.",
},
765: {
    "A": "انخفاض المزاج لمدة أسبوعين يصف <bdi>depression</bdi>، مو معيار تشخيصي للضعف الإدراكي الـ<bdi>mild</bdi>.",
    "B": "الخلل الحركي الموضعي يصف مشكلة عصبية بؤرية، غير مرتبط بتعريف الضعف الإدراكي الـ<bdi>mild</bdi>.",
    "D": "وجود عجز بنشاط يومي واحد يعني التصنيف يرتقي ل<bdi>dementia</bdi> كامل مو ضعف إدراكي <bdi>mild</bdi>.",
},
766: {
    "A": "العقد القاعدية اليسرى تسبب رجفان بالراحة بالجهة المقابلة (اليمنى)، مو رجفان قصدي.",
    "C": "القشرة الحركية اليسرى تسبب ضعف وتشنج بالجهة المقابلة، مو رجفان قصدي مع اختبار إصبع للأنف غير <bdi>normal</bdi>.",
    "D": "المخيخ الأيسر يسبب <bdi>symptoms</bdi> بنفس جهته (اليسار)، مو باليد اليمنى المذكورة.",
},
767: {
    "B": "الأميتريبتيلين مضاد <bdi>depression</bdi> له خصائص مضادة للكولين لكنه ليس <bdi>treatment</bdi> مستهدف لرجفان <bdi>Parkinson's disease</bdi>.",
    "C": "البروموكريبتين منبه <bdi>dopamine</bdi> يفيد الـ<bdi>symptoms</bdi> العامة، وليس الأكثر توجّهًا للرجفان تحديدًا كمضادات الكولين.",
    "D": "الكاربيدوبا/ليفودوبا فعّال لل<bdi>symptoms</bdi> العامة، لكن السؤال يبي الدواء الأكثر توجّهًا ل<bdi>symptom</bdi> الرجفان تحديدًا وهي مضادات الكولين.",
},
768: {
    "A": "<bdi>stroke</bdi> عادة أسرع بداية وتعطي <bdi>signs</bdi> بؤرية واضحة، وغير موجودة هنا.",
    "B": "<bdi>meningitis</bdi> البكتيري الـ<bdi>acute</bdi> يعطي حمى وتيبس رقبة وتدهور أسرع بكثير، وغير موصوف هنا.",
    "C": "متلازمة ما بعد الارتجاج عادة أخف حدة ومرتبطة بإصابة رأس معروفة، وليست بهذا التدهور بالوعي.",
},
769: {
    "A": "الشريان الفقري يسبب <bdi>symptoms</bdi> جذع دماغ ومخيخ (دوخة و<bdi>ataxia</bdi>)، مو ضعف حركي بحت متماثل كهذا.",
    "B": "الشريان القاعدي الأوسط يسبب <bdi>symptoms</bdi> <bdi>bilateral</bdi> أو جذعية أوسع، مو ضعف أحادي الجانب بحت.",
    "C": "الشريان المخي الأمامي يسبب ضعف بالرجل أبرز من الوجه والذراع، مختلف عن التوزيع المتساوي هنا.",
},
770: {
    "A": "<bdi>meningitis</bdi> يبدأ بشكل أكثر تدريجية مع حمى وتيبس رقبة، مو صداع صاعقي مفاجئ.",
    "B": "الصداع العنقودي متكرر بنمط محدد الوقت، مو حدث وحيد مفاجئ يوصف بأنه الأسوأ بالحياة.",
    "C": "الصداع التوتري تدريجي وأخف حدة، لا يعطي وصف \"أسوأ صداع بالحياة\" الصاعقي المفاجئ.",
},
771: {
    "A": "الكاربيدوبا/ليفودوبا <bdi>treatment</bdi> لرجفان <bdi>Parkinson's disease</bdi> (بالراحة)، مو الرجفان الأساسي الحركي هنا.",
    "B": "الألبرازولام قد يفيد مؤقتًا بمواقف محددة لكنه ليس <bdi>treatment</bdi> وقائي أول ب<bdi>risk</bdi> الاعتماد.",
    "D": "الأولانزابين <bdi>antipsychotic</bdi>، لا دور له ب<bdi>treatment</bdi> الرجفان الأساسي.",
},
772: {
    "A": "الـ<bdi>treatment</bdi> المضاد للفيروسات وحده لم يثبت فعالية كافية بتحسين <bdi>results</bdi> شلل بيل.",
    "B": "الـ<bdi>treatment</bdi> الحال للتخثر غير مناسب إطلاقًا، شلل بيل ليس <bdi>case</bdi> تخثرية.",
    "D": "الأكسجين عالي الضغط ليس <bdi>treatment</bdi> معتمد أو مثبت الفعالية لشلل بيل.",
},
773: {
    "A": "الرنين المغناطيسي غير ضروري بدون <bdi>signs</bdi> تحذيرية وفحص عصبي <bdi>normal</bdi>.",
    "B": "الأشعة المقطعية للجيوب غير مبررة بدون فحص أنفي أو <bdi>symptoms</bdi> جيوب أوضح تدعمها.",
    "C": "سرعة الترسيب تُطلب بالشك بالتهاب الشريان الصدغي عند كبار السن، وهذا مو السياق هنا.",
},
774: {
    "B": "رئيسة التمريض ليست مؤهلة أو مسؤولة عن أخذ موافقة <bdi>procedure</bdi> تداخلي طبي.",
    "C": "طبيب الباطنية المقيم ليس منفّذ الـ<bdi>procedure</bdi> ولا يملك نفس التفاصيل الدقيقة عنه.",
    "D": "\"أي عضو من الفريق\" غير دقيق، لأن الأنسب هو من سينفّذ الـ<bdi>procedure</bdi> فعليًا وله معرفة كاملة بتفاصيله.",
},
775: {
    "A": "الكرامة مفهوم أوسع، والمشكلة هنا تحديدًا كشف جسدي غير محجوب، وهذا خصوصية.",
    "C": "الاستقلالية تخص حق اتخاذ القرار، وهذا الموقف عن كشف جسدي غير مرتبط بقرار الـ<bdi>patient</bdi>.",
    "D": "السرية تخص حماية المعلومات الطبية، مو كشف الجسد فيزيائيًا.",
},
776: {
    "A": "استشارة المستشار القانوني تصعيد غير ضروري لمبدأ أخلاقي واضح ومباشر.",
    "C": "استشارة لجنة الأخلاقيات غير ضرورية هنا لعدم وجود تعقيد حقيقي بالموقف.",
    "D": "عدم إخبار الـ<bdi>patient</bdi> ينتهك حقه الأساسي بمعرفة تشخيصه واتخاذ قرارات مستنيرة.",
},
777: {
    "A": "مبدأ الكلية يخص التضحية بجزء لصالح الكل (كاستئصال عضو)، غير مرتبط بهذا السياق.",
    "B": "مبدأ التبعية يخص اتخاذ القرار بأقرب مستوى ممكن، غير مرتبط بتبرير هذا الـ<bdi>procedure</bdi> الطبي.",
    "D": "مبدأ الاختيار المستنير يخص الموافقة العامة على الـ<bdi>treatment</bdi>، مو التبرير الأخلاقي لتحمّل أثر جانبي محتمل ضار.",
},
778: {
    "B": "ترك الأمر لطبيب التخدير يعني التخلي عن مسؤولية حماية رغبة الـ<bdi>patient</bdi> الموثّقة مسبقًا.",
    "C": "إخبار الـ<bdi>patient</bdi> بقرار طبيب التخدير لا يحل التعارض المهني الأساسي بين الفريقين.",
    "D": "تأجيل العملية والبحث عن طبيب تخدير آخر حل متطرف وغير عملي مقارنة باستشارة لجنة محايدة.",
},
779: {
    "B": "تحويل الـ<bdi>patient</bdi> لمستشفى آخر لا يحل المشكلة الأساسية (<bdi>assessment</bdi> أهليته) ويؤخر القرار الصحيح.",
    "C": "استشارة لجنة الأخلاقيات قد تحتاج لاحقًا، لكن <bdi>assessment</bdi> الأهلية <bdi>step</bdi> أساسية أولى قبلها.",
    "D": "طلب توقيع نموذج خروج بدون <bdi>assessment</bdi> أهلية الـ<bdi>patient</bdi> يتجاوز <bdi>step</bdi> ضرورية وأساسية.",
},
780: {
    "A": "استشارة لجنة الأخلاقيات تصعيد غير ضروري لموقف واضح المبدأ الأخلاقي (الصدق والإفصاح).",
    "C": "الجراح المسؤول عن العملية هو من يجب أن يشرح بنفسه، لا ينيب جراح آخر بدون <bdi>cause</bdi>.",
    "D": "الطمأنة بدون إخبار الحقيقة يخالف مبدأ الصدق ويحرم الـ<bdi>patient</bdi> من معرفة ما حدث فعليًا.",
},
781: {
    "B": "الجراح المنفّذ للعملية هو الأنسب للشرح بنفسه، لا داعي لإنابة جراح آخر بدون <bdi>cause</bdi> واضح.",
    "C": "استشارة لجنة الأخلاقيات تصعيد غير ضروري لممارسة جراحية قياسية ومبررة طبيًا.",
    "D": "عدم إخبار الـ<bdi>patient</bdi> يخالف مبدأ الصدق والشفافية عندما يسأل مباشرة عن تفاصيل عمليته.",
},
783: {
    "A": "11% أقل بكثير من النسبة المعتمدة بمصادر هذا البنك لانتشار التدخين بين الرجال السعوديين.",
    "C": "37% أعلى بكثير من الرقم المعتمد إحصائيًا هنا.",
    "D": "51% مبالغ فيه جدًا مقارنة بالنسبة الفعلية المعتمدة بهذا السياق.",
},
782: {
    "A": "توقيع نموذج موافقة عالي الخطورة لا يبرر <bdi>procedure</bdi> عملية عبثية الفائدة على <bdi>patient</bdi> بهذي الـ<bdi>case</bdi>.",
    "C": "استشارة لجنة الأخلاقيات تصعيد إضافي غير ضروري هنا لوضوح الموقف السريري والتصنيف المسبق بعدم الإنعاش.",
    "D": "مناقشة الـ<bdi>case</bdi> مع طبيب العناية المركزة <bdi>step</bdi> تواصل جيدة، لكن القرار الأنسب المباشر هو عدم <bdi>procedure</bdi> العملية.",
},
784: {
    "A": "تحديد موعد إقلاع مناسب ل<bdi>patient</bdi> جاهز للتغيير، وهذا الـ<bdi>patient</bdi> ما عنده نية إقلاع أصلًا.",
    "B": "<bdi>treatment</bdi> بديل النيكوتين يُستخدم لدعم محاولة إقلاع فعلية، وهذا الـ<bdi>patient</bdi> غير راغب بالإقلاع حاليًا.",
    "D": "الإحالة لبرامج إقلاع <bdi>step</bdi> تناسب <bdi>patient</bdi> مستعد للتغيير الفعلي، مو <bdi>patient</bdi> بمرحلة ما قبل التفكير.",
},
785: {
    "A": "مرحلة ما قبل التفكير تعني عدم الاعتراف بوجود مشكلة أصلًا، وهذا عكس اعتراف الـ<bdi>patient</bdi> هنا.",
    "C": "مرحلة التحضير تعني خطوات فعلية عملية قريبة جدًا (أقل من 30 يوم)، وهذا غير مذكور هنا.",
    "D": "مرحلة الحفاظ تعني إقلاع فعلي مستمر، والـ<bdi>patient</bdi> هنا لسه يدخن.",
},
786: {
    "A": "<bdi>COPD</bdi> ناتج عن مواد أخرى بدخان التبغ (القطران والتهيّج الـ<bdi>chronic</bdi>)، مو النيكوتين نفسه.",
    "C": "سرطان الرئة ناتج عن المواد المسرطنة بالدخان، مو النيكوتين تحديدًا.",
    "D": "<bdi>diseases</bdi> القلب ترتبط أكثر بأول أكسيد الكربون والأكسدة من مكونات الدخان الأخرى، مو النيكوتين بشكل مباشر.",
},
787: {
    "A": "التنويم المغناطيسي بدون أدلة علمية كافية تدعم فعاليته بالإقلاع عن التدخين.",
    "C": "الوخز بالإبر أيضًا بدون أدلة علمية قوية مثبتة بهذا المجال.",
    "D": "أجهزة الرنين الحيوي (BICOM) غير مدعومة علميًا إطلاقًا ك<bdi>treatment</bdi> للإقلاع عن التدخين.",
},
788: {
    "A": "خفض الشحوم مهم لكن أثره على البقيا أقل من الإقلاع عن التدخين إحصائيًا.",
    "B": "التمرين المنتظم مفيد لكنه أيضًا أقل تأثيرًا على البقيا من الإقلاع عن التدخين.",
    "D": "الوزن المثالي مهم لكن أثره أقل مقارنة بالإقلاع عن التدخين على تحسين التوقعات بعد الاحتشاء.",
},
789: {
    "B": "ترتيب هذا الخيار غير صحيح، وكلمة \"advocate\" ليست من مكونات الـ5A's الحقيقية.",
    "C": "الترتيب هنا مقلوب تمامًا ويحتوي كلمة \"advocate\" غير الصحيحة، والصحيح يبدأ بـAsk.",
    "D": "هذا الترتيب يبدأ بكلمة \"advocate\" غير الصحيحة أصلًا وينتهي بترتيب خاطئ لباقي الخطوات.",
},
}

HIGHLIGHT_TERMS = {
693: ["reduced libido", "BMI 40 kg/m2", "Prolactin 450", "2.5 cm pituitary adenoma"],
694: ["central adiposity", "purple striae", "ACTH 20", "Cortisol 8 a.m. 600"],
695: ["fragility fracture", "facial and axillary hair growth", "BMI 23 kg/m2"],
696: ["incidentally detected", "2.0-cm right adrenal adenoma", "Blood pressure 130/70 mmHg"],
697: ["5.5-cm left adrenal mass with irregular borders", "elective adrenalectomy"],
698: ["marked peripheral edema", "Albumin 18", "4+ proteins", "Oval fat bodies"],
699: ["rapidly progressive glomerulonephritis"],
700: ["Sodium 124", "Serum osmolality 270", "Osmolality 310"],
701: ["inoperable small cell carcinoma of the lung", "Sodium 115", "he is euvolemic"],
702: ["CT brain with contrast", "Creatinine 378"],
703: ["repeated BP of 170/110", "Potassium 2.1", "not on any medications"],
704: ["hematuria, 1-day following a throat infection"],
705: ["pulmonary hemorrhage", "recurrent sinusitis", "numbness in her right upper limb"],
706: ["Potassium 6.5", "Creatinine 440"],
707: ["red urine for 5 days", "tonsillitis 3 weeks ago", "elevated blood pressure"],
708: ["watery diarrhea for 3 days", "Fractional excretion of sodium: 0.6%"],
709: ["Creatinine clearance 22", "progressive lower limbs edema for the last 4 months"],
710: ["Creatinine clearance 10", "planned to start soon"],
711: ["acute kidney injury", "referred for urgent"],
712: ["chronic kidney disease stage 3", "Creatinine 160"],
713: ["Potassium 6.9", "tall peaked T waves", "Creatinine 240"],
714: ["Potassium 6.6", "no acute changes"],
715: ["minimal change", "proteinuria"],
716: ["Crohn's disease", "hypokalemia refractory to aggressive"],
717: ["10-year history of type 2 diabetes", "hypertension and proteinuria"],
718: ["hypercalciuria"],
719: ["chronic kidney disease for 3 years", "absent ankle reflexes", "Creatinine 674"],
720: ["stable for several years", "Protein 500", "Creatinine 160"],
721: ["microalbuminuria range for the first time", "no diagnosis of"],
722: ["sore throat 3 weeks ago", "bloody urine and swelling of her hands and feet"],
723: ["chronic and progressing renal disease", "need dialysis sometime within the next year"],
724: ["4 anti-hypertensives drugs", "asymmetrical kidneys"],
725: ["chronic kidney disease stage 4", "potassium rich food should be"],
726: ["38 weeks pregnant", "positive for nitrites and leucocytes"],
727: ["has a sister with adult polycystic kidney disease"],
728: ["stable chronic kidney disease stage 3"],
729: ["has been on haemodialysis for chronic kidney disease"],
730: ["frequency and dysuria for 5 days", "Leukocytes 30"],
731: ["Potassium 6,0", "insulin; furosemide and enalapril", "Creatinine 120"],
732: ["Calcium 2.72", "Creatinine 196", "Urinary protein: creatinine ratio 154"],
733: ["10-day history of a left-sided", "confirmed an area of infarction"],
734: ["sudden left eye visual loss for 20 minutes", "diabetes mellitus"],
735: ["dysphagia, and generalized weakness", "brisk reflexes, spastic muscles"],
736: ["acute onset diplopia, ataxia", "New active lesions compared to previous scans"],
737: ["expressionless face, slow and slurred speech", "hand tremor at rest"],
738: ["decline in cognitive capacity and", "shuffling gait"],
739: ["continue for 35 minutes", "20 mg of diazepam intravenously"],
740: ["unable to close her left eye", "wrinkle the left side of her forehead"],
741: ["pins and needles", "dorsiflexion and fingers extension"],
742: ["bilateral ptosis", "positive Simpson", "transient improvement in the ptosis"],
743: ["Blood pressure 115/80 mmH", "unchanged on standing"],
744: ["complex regional pain syndrome", "carpal tunnel release surgery"],
745: ["unable to abduct the left eye", "no obvious squint"],
746: ["irritable and criticizes everyone at", "pauses halfway through sentences"],
747: ["previous cervical laminectomy", "worsening gait instability and urinary"],
748: ["degenerative cervical myelopathy", "ongoing neurological symptoms"],
749: ["sudden onset left sided body weakness for 4 hours", "neuron facial palsy and left sided hemiparesis"],
750: ["symmetrical weakness of the face and all four extremities", "sensations are intact"],
751: ["about 2 a.m.", "lacrimation and redness of the right eye"],
752: ["depression of the right eye", "equal and reactive"],
753: ["repeated tonic-clonic seizures at home", "sodium valproate"],
754: ["Guillain Barre Syndrome"],
755: ["loss of direct light reflex with preserved indirect", "clasp knife rigidity"],
756: ["slow, short-stepped and with tendency to fall", "dilated ventricles"],
757: ["wants to die in", "passed away without resuscitation"],
758: ["during breaking bad news"],
759: ["fluctuations in cognition and visual hallucinations"],
760: ["difficulty recognizing his grandsons", "cardiovascular risk factors"],
761: ["bilateral cerumen impaction", "bilaterally positive"],
762: ["clinical evidence of early Alzheimer dementia"],
763: ["predominant executive function impairment", "diffuse periventricular white-matter hyperintensities"],
764: ["kinetic and rigid with no tremor", "prominent gait disorder and postural instability"],
765: ["mild cognitive impairment"],
766: ["reaches for a pen", "finger-to-nose test"],
767: ["dominant right hand", "not on any medication"],
768: ["increasing fatigue and drowsiness and difficulty", "unaware of any head injury"],
769: ["face, arm and leg", "comprehension are intact"],
770: ["while bending down to pick up his keys", "the worst headache he has ever had"],
771: ["slowly progressive bilateral tremor", "recently noted head bobbing and a change in her"],
772: ["sudden onset of unilateral peripheral facial nerve weakness"],
773: ["3 to 4 times per month", "usually located over the right or"],
774: ["CT guided aspiration"],
775: ["forgot to close the curtain while exposing the patient's abdomen"],
776: ["father of the diagnosis"],
777: ["father's death", "unbearable pain"],
778: ["expressed her wish to not knowing the details", "insisted to explain to the patient all details"],
779: ["charcot knee", "The patient refused"],
780: ["bleeding resulted from a surgical error", "took longer time than usual"],
781: ["the appendix found in normal", "common practice is to remove the appendix"],
782: ["labelled a do not resuscitate case", "de-bulking operation"],
783: ["percentage prevalence of smoking among Saudi adult men"],
784: ["no intention of quitting and feels fine"],
785: ["plans to quit this year"],
786: ["thousands of chemical compounds including nicotine"],
787: ["most approved evidence-based intervention"],
788: ["the most effective preventive measure to improve post-myocardial"],
789: ["5 A's approach during smoking cessation counselling"],
}
