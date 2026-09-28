# -*- coding: utf-8 -*-
# Explanations for questions 596-692 (Hematology/Oncology block + large Endocrinology block)

TOPICS = {
596: "Hematology",
597: "Hematology",
598: "Hematology",
599: "Hematology",
600: "Hematology",
601: "Oncology",
602: "Oncology",
603: "Endocrinology",
604: "Endocrinology",
605: "Endocrinology",
606: "Endocrinology",
607: "Endocrinology",
608: "Endocrinology",
609: "Endocrinology",
610: "Endocrinology",
611: "Endocrinology",
612: "Endocrinology",
613: "Endocrinology",
614: "Endocrinology",
615: "Endocrinology",
616: "Endocrinology",
617: "Endocrinology",
618: "Endocrinology",
619: "Endocrinology",
620: "Endocrinology",
621: "Endocrinology",
622: "Endocrinology",
623: "Endocrinology",
624: "Endocrinology",
625: "Endocrinology",
626: "Endocrinology",
627: "Endocrinology",
628: "Endocrinology",
629: "Endocrinology",
630: "Clinical Pharmacology & Toxicology",
631: "Endocrinology",
632: "Cardiology",
633: "Endocrinology",
634: "Endocrinology",
635: "Endocrinology",
636: "Endocrinology",
637: "Endocrinology",
638: "Endocrinology",
639: "Endocrinology",
640: "Endocrinology",
641: "Endocrinology",
642: "Endocrinology",
643: "Endocrinology",
644: "Endocrinology",
645: "Endocrinology",
646: "Endocrinology",
647: "Endocrinology",
648: "Cardiology",
649: "Endocrinology",
650: "Endocrinology",
651: "Endocrinology",
652: "Endocrinology",
653: "Endocrinology",
654: "Endocrinology",
655: "Endocrinology",
656: "Endocrinology",
657: "Endocrinology",
658: "Endocrinology",
659: "Endocrinology",
660: "Endocrinology",
661: "Endocrinology",
662: "Endocrinology",
663: "Endocrinology",
664: "Endocrinology",
665: "Endocrinology",
666: "Endocrinology",
667: "Endocrinology",
668: "Endocrinology",
669: "Endocrinology",
670: "Endocrinology",
671: "Endocrinology",
672: "Endocrinology",
673: "Endocrinology",
674: "Endocrinology",
675: "Endocrinology",
676: "Endocrinology",
677: "Endocrinology",
678: "Endocrinology",
679: "Clinical Pharmacology & Toxicology",
680: "Endocrinology",
681: "Endocrinology",
682: "Endocrinology",
683: "Endocrinology",
684: "Endocrinology",
685: "Endocrinology",
686: "Endocrinology",
687: "Endocrinology",
688: "Endocrinology",
689: "Endocrinology",
690: "Endocrinology",
691: "Endocrinology",
692: "Endocrinology",
}

EXPLANATIONS = {}
WHY_WRONG = {}
HIGHLIGHT_TERMS = {}

EXPLANATIONS.update({
596: {
    "idea": "<bdi>patient</bdi> على <bdi>warfarin</bdi> صار عندها نزيف دماغي <bdi>severe</bdi> (<bdi>subdural hematoma</bdi>) يحتاج عملية فورية، والـ INR <bdi>elevated</bdi> جدًا، فالسؤال يبي أسرع وأكمل طريقة نرجع فيها التخثر قبل الجراحة.",
    "clues": [
        ("atrial fibrillation... on warfarin", "<bdi>cause</bdi> استخدام مميع الدم"),
        ("subdural hematoma that requires evacuation", "نزيف دماغي خطير يحتاج تصحيح تخثر عاجل قبل التدخل"),
        ("INR 3.9 (0.8-1.2)", "تمييع <bdi>severe</bdi> جدًا فوق الـ<bdi>normal</bdi>، يفسر سهولة النزيف"),
    ],
    "why_correct": [
        "بأي نزيف مهدد للحياة عند <bdi>patient</bdi> على <bdi>warfarin</bdi>، لازم نرجع <bdi>factors</bdi> التخثر فورًا ونمنع رجوع الـ INR يرتفع بعدها.",
        "الـ <bdi>fresh frozen plasma</bdi> يعطي <bdi>factors</bdi> تخثر جاهزة فورًا، لكن مفعوله يزول خلال ساعات، فلازم يترافق مع <bdi>vitamin K</bdi> اللي يخلي الكبد يصنع <bdi>factors</bdi> تخثر جديدة ويثبت التصحيح.",
        "الجمع بينهم (الخيار D) يعطي تصحيح فوري ومستمر بنفس الوقت، وهذا اللي يحتاج قبل جراحة عاجلة على الدماغ.",
    ],
    "when_changes": [
        "لو النزيف بسيط وغير مهدد للحياة، ممكن نكتفي بإيقاف الـ<bdi>warfarin</bdi> وإعطاء فيتامين K لوحده.",
        "لو ما فيه تأخير ممكن نستخدم <bdi>prothrombin complex concentrate</bdi> بدل الـ FFP لأنه أسرع وأكمل تصحيحًا، بس هنا الخيار المتاح هو FFP مع فيتامين K.",
    ],
    "rule": "أي نزيف خطير عند <bdi>patient</bdi> على <bdi>warfarin</bdi> يحتاج تصحيح فوري (FFP أو PCC) مع فيتامين K مع بعض، مو أحدهم لحاله.",
    "comparison": {
        "headers": ["الـ<bdi>treatment</bdi>", "سرعة المفعول", "مدة المفعول"],
        "rows": [
            ["<bdi>Vitamin K</bdi>", "بطيء (ساعات)", "طويل، يصنع <bdi>factors</bdi> جديدة"],
            ["<bdi>Fresh frozen plasma</bdi>", "فوري", "قصير، يزول خلال ساعات"],
            ["<bdi>FFP + Vitamin K</bdi>", "فوري ومستمر", "الأنسب بنزيف مهدد للحياة"],
        ],
    },
    "guideline_note": None,
},
597: {
    "idea": "<bdi>patient</bdi> يتلقى كيماوي لسرطان دم الأطفال وصار عنده حمى مع نقص <bdi>severe</bdi> بكريات الدم البيضاء (<bdi>neutropenic fever</bdi>) بدون بؤرة عدوى واضحة، والسؤال يبي أسرع وأنسب <bdi>management</bdi>.",
    "clues": [
        ("day 17 of chemotherapy", "توقيت متوقع لنزول تعداد الدم بعد الكيماوي"),
        ("Heart rate 110 /min, Temperature 38.9", "حمى مع تسرع قلب، <bdi>sign</bdi> عدوى محتملة خطيرة"),
        ("WBC 0.6", "نقص <bdi>severe</bdi> جدًا بكريات الدم البيضاء، يعني مناعة شبه معدومة"),
        ("Platelets count 25", "نقص أيضًا بالصفائح، يؤكد تثبيط نخاع العظم من الكيماوي"),
    ],
    "why_correct": [
        "الحمى مع نقص <bdi>severe</bdi> بالعدلات (<bdi>febrile neutropenia</bdi>) <bdi>case</bdi> طارئة لأن العدوى ممكن تتفاقم بسرعة بدون مناعة كافية.",
        "لازم نأخذ مزارع (دم، بول، بلغم) فورًا، وبنفس الوقت نبدأ مضادات حيوية وريدية واسعة الطيف بدون انتظار <bdi>result</bdi> المزارع.",
        "المضاد الوريدي أفضل من الفموي هنا لأنه يعطي تغطية أسرع وأقوى وامتصاص مضمون ب<bdi>patient</bdi> خطير محتمل يتدهور بسرعة.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> مستقر وتعداد العدلات أعلى (مو نقص <bdi>severe</bdi>) وبدون <bdi>signs</bdi> خطورة، بعض البروتوكولات تسمح بمضاد فموي بالـ<bdi>follow-up</bdi> الدقيقة، بس هذا الـ<bdi>patient</bdi> عالي الخطورة.",
        "لو ظهرت بؤرة عدوى واضحة، يوجه اختيار المضاد الحيوي نحوها بشكل أدق.",
    ],
    "rule": "أي حمى مع نقص <bdi>severe</bdi> بالعدلات بعد الكيماوي تعامل كطوارئ: مزارع فورًا مع بدء مضادات حيوية وريدية واسعة الطيف بدون تأخير.",
    "comparison": None,
    "guideline_note": None,
},
598: {
    "idea": "امرأة عندها حمى وتعرق ليلي ونقص وزن غير مقصود (<bdi>symptoms</bdi> بائية) مع تضخم عقد لمفاوية متعددة الأماكن وتضخم بالطحال، صورة توحي بلمفوما، والسؤال يبي أفضل طريقة نأكد فيها الـ<bdi>diagnosis</bdi>.",
    "clues": [
        ("fever, night sweats and weight loss", "<bdi>symptoms</bdi> بائية كلاسيكية للمفوما"),
        ("lost 12 Kg in the last 3 month", "نقص وزن كبير وسريع، يدعم <bdi>disease</bdi> ورمي/جهازي"),
        ("bilateral cervical lymph nodes, largest 3 cm", "عقد لمفاوية كبيرة بمكان أكثر من واحد"),
        ("inguinal lymphadenopathy", "تضخم عقد بمكان ثاني، يدعم <bdi>disease</bdi> جهازي مو موضعي"),
        ("spleen is palpable 3 fingers", "تضخم طحال، من <bdi>signs</bdi> الـ<bdi>diseases</bdi> اللمفاوية الجهازية"),
    ],
    "why_correct": [
        "ل<bdi>diagnosis</bdi> اللمفوما بدقة لازم نشوف بنية العقدة اللمفاوية كاملة (البنية النسيجية)، وهذا ما يعطيه إلا الخزعة الاستئصالية الكاملة.",
        "الخزعة الاستئصالية (<bdi>excisional biopsy</bdi>) تحافظ على شكل العقدة كامل، وتسمح بتمييز أنواع اللمفوما (هودجكن أو لا-هودجكن) بدقة.",
        "خطوات ثانية زي فحص النخاع أو استئصال الطحال تأتي لاحقًا للتدريج (staging) بعد ما يتأكد الـ<bdi>diagnosis</bdi> أولًا، مو ك<bdi>step</bdi> أولى.",
    ],
    "when_changes": [
        "لو العقدة صغيرة وموضعية بدون <bdi>symptoms</bdi> بائية، ممكن يبدأ الـ<bdi>assessment</bdi> بفحص إبري أبسط قبل الاستئصال الكامل.",
        "بعد تأكيد الـ<bdi>diagnosis</bdi> بالخزعة، يصير فحص النخاع جزء من التدريج لمعرفة انتشار الـ<bdi>disease</bdi>.",
    ],
    "rule": "أي شك بلمفوما مع عقد لمفاوية متعددة و<bdi>symptoms</bdi> بائية، الخزعة الاستئصالية الكاملة هي الـ<bdi>step</bdi> التشخيصية الأولى، مو الإبرة الدقيقة.",
    "comparison": None,
    "guideline_note": None,
},
599: {
    "idea": "<bdi>patient</bdi> عنده سرطان دم لمفاوي <bdi>chronic</bdi> بتعداد لمفاويات عالي جدًا، بدأ كيماوي وبعد يومين طلعت عنده اضطرابات كهارل متعددة، صورة كلاسيكية لمتلازمة تحلل الورم (<bdi>tumor lysis syndrome</bdi>) والسؤال يبي أي اضطراب كهرلي مصاحب لها.",
    "clues": [
        ("lymphocyte count was 73,000", "عبء ورمي ضخم، <bdi>factor</bdi> <bdi>risk</bdi> رئيسي لمتلازمة تحلل الورم"),
        ("2 days after chemotherapy", "توقيت كلاسيكي لتحلل خلايا الورم بعد بدء الـ<bdi>treatment</bdi>"),
        ("Potassium 5.5", "ارتفاع بوتاسيوم، من <bdi>signs</bdi> تحلل الورم"),
        ("Uric acid 620", "ارتفاع حمض اليوريك، <bdi>sign</bdi> أساسية بمتلازمة تحلل الورم"),
        ("Creatinine 139", "تأثر وظائف الكلى <bdi>result</bdi> ترسب حمض اليوريك والفوسفات"),
    ],
    "why_correct": [
        "متلازمة تحلل الورم تسبب تحرر محتويات الخلايا المسرطنة فجأة: بوتاسيوم وفوسفات وحمض يوريك يرتفعون، بينما الكالسيوم ينخفض.",
        "<bdi>cause</bdi> نقص الكالسيوم إنه يترسب مع الفوسفات الزايد على شكل أملاح كالسيوم-فوسفات بالأنسجة، فيقل الكالسيوم الحر بالدم.",
        "هذا النمط (بوتاسيوم وفوسفات وحمض يوريك مرتفعين مع كالسيوم <bdi>low</bdi>) هو البصمة المميزة لمتلازمة تحلل الورم بعد كيماوي على ورم كبير الحجم.",
    ],
    "when_changes": [
        "لو الكالسيوم طلع <bdi>elevated</bdi> بدل <bdi>low</bdi>، لازم نفكر ب<bdi>cause</bdi> ثاني غير تحلل الورم مثل ورم مفرز لهرمون مشابه لـPTH.",
        "لو الصوديوم هو المتأثر الرئيسي بدون باقي التغيرات، يصير التفكير ب<bdi>cause</bdi> مختلف مثل فقد سوائل أو SIADH.",
    ],
    "rule": "متلازمة تحلل الورم تعطي ارتفاع بوتاسيوم وفوسفات وحمض يوريك مع نقص كالسيوم، وتصير غالبًا خلال أيام من بدء كيماوي على ورم كبير.",
    "comparison": {
        "headers": ["الكهرل", "التغير بمتلازمة تحلل الورم"],
        "rows": [
            ["<bdi>Potassium</bdi>", "يرتفع"],
            ["<bdi>Phosphate</bdi>", "يرتفع"],
            ["<bdi>Uric acid</bdi>", "يرتفع"],
            ["<bdi>Calcium</bdi>", "ينخفض"],
        ],
    },
    "guideline_note": None,
},
600: {
    "idea": "رجل عنده مشية غير مستقرة مع ضعف بالحس العميق و<bdi>sign</bdi> بابنسكي إيجابية (إصابة بالمسار الهرمي) مع غياب منعكسات الكاحل والركبة (إصابة أعصاب طرفية) مع <bdi>anemia</bdi>، وهذا مزيج كلاسيكي لتنكس النخاع الشوكي المشترك ب<bdi>cause</bdi> نقص فيتامين B12.",
    "clues": [
        ("decreased proprioception in the lower limbs", "إصابة العمود الخلفي بالنخاع الشوكي"),
        ("positive planter reflexes (positive Babinski)", "إصابة المسار الهرمي (upper motor neuron)"),
        ("absent ankle and knee's reflexes", "إصابة أعصاب طرفية (lower motor neuron)، يجمع مع الأول صورة مختلطة"),
        ("He has anemia", "يدعم <bdi>cause</bdi> دموي وراء الـ<bdi>symptoms</bdi> العصبية"),
        ("Peripheral smear done", "يستخدم لتأكيد نوع <bdi>anemia</bdi> (كبير الحجم ب<bdi>case</bdi> B12)"),
    ],
    "why_correct": [
        "الجمع بين <bdi>signs</bdi> المسار الهرمي (بابنسكي) و<bdi>signs</bdi> الأعصاب الطرفية (غياب المنعكسات) مع خلل الحس العميق هو الصورة الكلاسيكية لتنكس النخاع الشوكي المشترك اللي يسببه نقص <bdi>vitamin B12</bdi>.",
        "<bdi>anemia</bdi> المرافق يكون عادة كبير الخلايا (<bdi>macrocytic</bdi>) وهذا يتوافق مع دور B12 بتكوين خلايا الدم الحمراء.",
        "الكحول ونقص الحديد و<bdi>hypothyroidism</bdi> ممكن يسببون اعتلال أعصاب أو <bdi>anemia</bdi> لوحدهم، لكن ما يعطون هالصورة المشتركة (هرمي + طرفي) بنفس الوقت.",
    ],
    "when_changes": [
        "لو <bdi>anemia</bdi> كان صغير الخلايا بدون <bdi>signs</bdi> عصبية هرمية، يميل الـ<bdi>diagnosis</bdi> لنقص الحديد بدل B12.",
        "لو فيه تاريخ كحول <bdi>chronic</bdi> مع اعتلال أعصاب فقط بدون <bdi>signs</bdi> هرمية، يصير الـ<bdi>diagnosis</bdi> اعتلال أعصاب كحولي.",
    ],
    "rule": "وجود <bdi>signs</bdi> هرمية (بابنسكي) مع غياب منعكسات طرفية و<bdi>anemia</bdi> يوجه دايمًا لنقص <bdi>vitamin B12</bdi> وتنكس النخاع الشوكي المشترك.",
    "comparison": None,
    "guideline_note": None,
},
601: {
    "idea": "<bdi>patient</bdi> كبير بالسن جدًا وضعيف الـ<bdi>case</bdi> الوظيفية وعنده <bdi>dementia</bdi> وسرطان منتشر بمصدر غير معروف لأكثر من عضو، والسؤال يبي أنسب <bdi>management</bdi> تناسب حالته العامة مو الـ<bdi>diagnosis</bdi> المثالي.",
    "clues": [
        ("91-year-old man with poor performance status, dementia", "<bdi>case</bdi> وظيفية سيئة جدًا تحدد خيارات الـ<bdi>treatment</bdi> الممكنة"),
        ("adenocarcinoma of an unknown primary site", "سرطان منتشر بدون مصدر أساسي معروف"),
        ("upper abdominal lymphadenopathy, liver lesions, and pulmonary nodules", "انتشار واسع بعدة أعضاء، يدل على مرحلة متقدمة جدًا"),
    ],
    "why_correct": [
        "ب<bdi>patient</bdi> بهذا العمر مع <bdi>dementia</bdi> وضعف وظيفي <bdi>severe</bdi> و<bdi>disease</bdi> منتشر واسع، ما فيه <bdi>treatment</bdi> موجه للسرطان يقدر يتحمله أو يستفيد منه بأمان.",
        "الرعاية التلطيفية الداعمة (<bdi>comfort care</bdi>) هي الأنسب لأنها تركز على راحة الـ<bdi>patient</bdi> بدل محاولات علاجية عدوانية غير مجدية بحالته.",
        "أي <bdi>procedure</bdi> تدخلي أو كيماوي بهالحالة يزيد المخاطر والـ<bdi>symptoms</bdi> الجانبية بدون فايدة حقيقية متوقعة على البقاء أو الوظيفة.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> كان ب<bdi>case</bdi> وظيفية جيدة وبدون <bdi>dementia</bdi>، ممكن يكون البحث عن المصدر الأساسي أو الكيماوي التلطيفي خيار معقول.",
        "لو الـ<bdi>disease</bdi> كان محصور بعضو واحد قابل للاستئصال، يختلف التفكير نحو <bdi>treatment</bdi> موجه.",
    ],
    "rule": "ب<bdi>patient</bdi> كبير جدًا مع ضعف وظيفي <bdi>severe</bdi> و<bdi>dementia</bdi> و<bdi>disease</bdi> منتشر واسع، الرعاية التلطيفية الداعمة أهم من أي تدخل علاجي عدواني.",
    "comparison": None,
    "guideline_note": None,
},
602: {
    "idea": "<bdi>patient</bdi> عنده سرطان رئة بمرحلة متقدمة وتوقع بقاء قصير، جاء للعيادة ب<bdi>cause</bdi> ألم ظهر، والتحاليل تظهر ارتفاع <bdi>severe</bdi> بالكالسيوم المتأين، فالسؤال يبي أول <bdi>step</bdi> ب<bdi>treatment</bdi> ارتفاع الكالسيوم الناتج عن الورم.",
    "clues": [
        ("prognosis was poor and that he is unlikely to survive", "يوضح إن الرعاية هنا تلطيفية بس ما يمنع <bdi>treatment</bdi> الـ<bdi>complications</bdi> العاجلة"),
        ("Calcium ionised 3.2 (1.1-1.3)", "ارتفاع كبير جدًا بالكالسيوم المتأين، <bdi>case</bdi> عرضية تحتاج <bdi>treatment</bdi> فوري"),
    ],
    "why_correct": [
        "حتى ب<bdi>patient</bdi> بمرحلة تلطيفية، ارتفاع الكالسيوم الـ<bdi>severe</bdi> يعتبر <bdi>case</bdi> طارئة لازم تعالج لأنها تسبب <bdi>symptoms</bdi> مزعجة وخطيرة (لخبطة، جفاف، قصور كلوي).",
        "الـ<bdi>step</bdi> الأولى دايمًا هي الترطيب بـ <bdi>IV isotonic saline</bdi> لتحسين طرح الكالسيوم عبر الكلى، بغض النظر عن التوقع العام.",
        "الـ<bdi>morphine</bdi> يعالج الألم بس مو <bdi>cause</bdi> ارتفاع الكالسيوم، والبيسفوسفونيت الفموي ضعيف الامتصاص وما يستخدم بهالحالة العرضية الـ<bdi>acute</bdi>، والـ<bdi>furosemide</bdi> قبل الترطيب يزيد الجفاف سوء.",
    ],
    "when_changes": [
        "بعد الترطيب الكافي، يضاف بيسفوسفونيت وريدي مثل <bdi>zoledronic acid</bdi> للتحكم طويل المدى بالكالسيوم الناتج عن الورم.",
        "لو الـ<bdi>patient</bdi> بمرحلة نهائية جدًا ويفضل راحة فقط بدون تدخل، ممكن يكتفى ب<bdi>treatment</bdi> الـ<bdi>symptoms</bdi> بدل تصحيح الكالسيوم، بس هذا قرار يحتاج نقاش صريح مع الـ<bdi>patient</bdi>.",
    ],
    "rule": "ارتفاع الكالسيوم العرضي ب<bdi>patient</bdi> السرطان يعالج بالترطيب الوريدي أولًا دايمًا، حتى لو التوقع العام غير مبشر.",
    "comparison": None,
    "guideline_note": None,
},
603: {
    "idea": "<bdi>patient</bdi> عنده تشنجات لمدة 3 أيام مع صوديوم <bdi>low</bdi> جدًا (112) وبول غير مخفف رغم انخفاض الصوديوم بالدم، وهذا يدل على إفراز غير مناسب لهرمون مضاد الإدرار (<bdi>SIADH</bdi>).",
    "clues": [
        ("Sodium 112 (134-146)", "نقص صوديوم <bdi>severe</bdi> جدًا، <bdi>cause</bdi> التشنجات"),
        ("Serum osmolality 240 (280-300)", "انخفاض أسمولية الدم يتوافق مع نقص الصوديوم"),
        ("Osmolality 860 (280-910)", "بول مركّز جدًا رغم انخفاض أسمولية الدم، يعني الجسم ما يقدر يخفف البول بشكل <bdi>normal</bdi>"),
    ],
    "why_correct": [
        "الجسم الـ<bdi>normal</bdi> المفروض يخفف البول لأقصى درجة لو أسمولية الدم <bdi>low</bdi>، لكن هنا البول مركز رغم كذا، وهذا دليل على إفراز ADH غير مناسب.",
        "الـ SIADH يسبب نقص صوديوم عزلي (بدون جفاف أو احتباس سوائل واضح) وبول مركز بشكل غير متوقع، مطابق تمامًا للصورة هنا.",
        "<bdi>diseases</bdi> الغدة الكظرية زي <bdi>Conn's syndrome</bdi> و<bdi>Cushing's syndrome</bdi> عادة تسبب اضطراب بالبوتاسيوم (نقص بوتاسيوم) مو نقص صوديوم عزلي بهالشكل.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عنده جفاف واضح مع نقص بوتاسيوم، يميل الـ<bdi>diagnosis</bdi> نحو <bdi>causes</bdi> كظرية مثل Addison's بدل SIADH.",
        "لو أسمولية البول كانت <bdi>low</bdi> جدًا (مخففة) رغم نقص الصوديوم، يصير التفكير ب<bdi>cause</bdi> ثاني مثل شرب ماء زايد (polydipsia).",
    ],
    "rule": "نقص صوديوم <bdi>severe</bdi> مع بول غير مخفف (مركز) رغم انخفاض أسمولية الدم يشخص SIADH.",
    "comparison": None,
    "guideline_note": None,
},
604: {
    "idea": "رجل شاب عنده ضعف رغبة جنسية وانتصاب ضعيف مع <bdi>prolactin</bdi> <bdi>elevated</bdi> جدًا وهرمونات الغدة النخامية الثانية <bdi>normal</bdi> تقريبًا، فالسؤال يبي أفضل فحص تالي نحدد فيه الـ<bdi>cause</bdi>.",
    "clues": [
        ("decreased libido and weak erections", "<bdi>symptoms</bdi> قصور غدد تناسلية ثانوي محتمل"),
        ("Prolactin 2100 (&lt;870)", "ارتفاع كبير بالـ<bdi>prolactin</bdi>، يوحي بورم مفرز لل<bdi>prolactin</bdi>"),
        ("Follicle-stimulating hormone 12", "<bdi>normal</bdi> تقريبًا"),
        ("Luteinizing hormone 18", "<bdi>normal</bdi> تقريبًا، يستبعد قصور نخامي شامل واضح حاليًا"),
    ],
    "why_correct": [
        "ارتفاع الـ<bdi>prolactin</bdi> الـ<bdi>severe</bdi> عند رجل بدون <bdi>cause</bdi> واضح (لا حمل ولا أدوية مذكورة) يوجه بقوة نحو ورم بالغدة النخامية مفرز لل<bdi>prolactin</bdi>.",
        "أفضل فحص تالي هو <bdi>Brain MRI</bdi> مركّز على منطقة الغدة النخامية لتحديد وجود الورم وحجمه.",
        "فحوصات زي السكر الصائم أو أشعة البطن ما لها علاقة مباشرة ب<bdi>cause</bdi> ارتفاع الـ<bdi>prolactin</bdi>، وفحص التستوستيرون مفيد بس ثانوي، مو الـ<bdi>step</bdi> الأهم لتحديد الـ<bdi>cause</bdi>.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> يستخدم أدوية معروفة ترفع الـ<bdi>prolactin</bdi> (مثل مضادات الـ<bdi>psychosis</bdi>)، يصير أول <bdi>step</bdi> مراجعة الأدوية قبل التصوير.",
        "لو الـ<bdi>prolactin</bdi> <bdi>elevated</bdi> بشكل بسيط فقط، يفضل تكرار الفحص أولًا قبل التصوير المباشر.",
    ],
    "rule": "أي ارتفاع كبير وغير مفسر بالـ<bdi>prolactin</bdi> عند رجل يحتاج تصوير بالرنين المغناطيسي للغدة النخامية لاستبعاد ورم مفرز لل<bdi>prolactin</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
605: {
    "idea": "رجل عنده صورة كلاسيكية لمتلازمة كوشينغ (زيادة وزن مركزي، وجه مكتنز، سنام جاموسي، كدمات سهلة، ضغط <bdi>elevated</bdi>) مع تصبغ جلد إضافي، والتصبغ هذا يدل إن مصدر الكورتيزول الزائد من الغدة النخامية (زيادة ACTH).",
    "clues": [
        ("central weight gain, change in facial appearance", "<bdi>signs</bdi> كلاسيكية لمتلازمة كوشينغ"),
        ("buffalo hump, edema, proximal muscle wasting", "<bdi>signs</bdi> إضافية تدعم فرط الكورتيزول"),
        ("pigmentation of the skin", "<bdi>sign</bdi> تدل على ارتفاع ACTH (من نفس جزيء POMC المسبب للتصبغ)"),
        ("elevated blood pressure", "أثر شائع لفرط الكورتيزول"),
    ],
    "why_correct": [
        "الصورة السريرية كلها كوشينغية (سمنة مركزية، سنام، كدمات، ضغط <bdi>elevated</bdi>)، وهذا يثبت وجود فرط كورتيزول.",
        "تصبغ الجلد <bdi>sign</bdi> مهمة تدل إن مصدر المشكلة يفرز ACTH بكمية كبيرة، وهذا يميز <bdi>Cushing's disease</bdi> (ورم نخامي مفرز ACTH) عن <bdi>causes</bdi> كظرية.",
        "الأورام الكظرية (adenoma أو carcinoma) تسبب كبت لـACTH ب<bdi>cause</bdi> التغذية الراجعة، فما تعطي تصبغ جلد، فيستبعدون بوجود هالعلامة.",
    ],
    "when_changes": [
        "لو ما فيه تصبغ جلد مع باقي الصورة الكوشينغية، يصير التفكير بمصدر كظري (adenoma أو carcinoma) أقوى.",
        "لو الـ<bdi>patient</bdi> يأخذ ستيرويدات خارجية طويلة المدى، يصير الـ<bdi>cause</bdi> الأرجح كوشينغ علاجي المنشأ بدل ورم داخلي.",
    ],
    "rule": "وجود تصبغ جلد مع صورة كوشينغية يدل على ارتفاع ACTH ويوجه نحو Cushing's disease النخامي، بينما غيابه يوجه نحو مصدر كظري.",
    "comparison": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
596: {
    "A": "فيتامين K لحاله بطيء جدًا (يحتاج ساعات لين يعمل الكبد <bdi>factors</bdi> جديدة)، ما يكفي وحده بنزيف مهدد للحياة.",
    "B": "FFP لحاله يصحح مؤقتًا بس مفعوله يزول خلال ساعات ويرجع الـ INR يرتفع بدون فيتامين K.",
    "C": "الـ<bdi>factor</bdi> السابع المنشط مو <bdi>treatment</bdi> قياسي لعكس الـ<bdi>warfarin</bdi> وله <bdi>risk</bdi> تجلط زايد.",
},
597: {
    "A": "المزارع لوحدها بدون <bdi>treatment</bdi> تأخر البدء بمضاد ضروري ل<bdi>patient</bdi> معرض لتدهور سريع.",
    "B": "الباراسيتامول يخفض الحرارة بس ما يعالج العدوى الكامنة المحتملة الخطيرة.",
    "C": "المضاد الفموي أضعف وأبطأ من الوريدي ب<bdi>patient</bdi> عالي الخطورة بنقص عدلات <bdi>severe</bdi>.",
},
598: {
    "A": "الإبرة الدقيقة ما تعطي بنية العقدة كاملة، وما تكفي لتصنيف اللمفوما بدقة.",
    "C": "خزعة النخاع تفيد للتدريج بعد الـ<bdi>diagnosis</bdi>، مو لل<bdi>diagnosis</bdi> الأولي بهالحالة.",
    "D": "استئصال الطحال <bdi>procedure</bdi> كبير وغير ضروري ك<bdi>step</bdi> تشخيصية أولى.",
},
599: {
    "B": "الكالسيوم ينخفض بمتلازمة تحلل الورم ب<bdi>cause</bdi> الترسب مع الفوسفات، مو يرتفع.",
    "C": "نقص الصوديوم مو من الـ<bdi>signs</bdi> المميزة لمتلازمة تحلل الورم.",
    "D": "ارتفاع الصوديوم مو جزء من الصورة الكيميائية المتوقعة هنا.",
},
600: {
    "A": "الكحول يسبب اعتلال أعصاب طرفي بس نادرًا يعطي <bdi>signs</bdi> هرمية زي بابنسكي بهالوضوح.",
    "B": "نقص الحديد يعطي <bdi>anemia</bdi> صغير الخلايا بدون هالصورة العصبية المختلطة.",
    "D": "<bdi>hypothyroidism</bdi> ممكن يسبب <bdi>symptoms</bdi> عصبية بس مو بهالنمط الهرمي والطرفي المشترك.",
},
601: {
    "A": "الجراحة الاستكشافية عبء كبير على <bdi>patient</bdi> هش بدون فايدة متوقعة تذكر.",
    "B": "خزعة تحديد المصدر ما تغير خطة الـ<bdi>treatment</bdi> ب<bdi>case</bdi> <bdi>patient</bdi> ما يتحمل <bdi>treatment</bdi> موجه أصلًا.",
    "C": "الكيماوي التلطيفي غير مناسب لضعف حالته الوظيفية الـ<bdi>severe</bdi> و<bdi>risk</bdi> الـ<bdi>symptoms</bdi> الجانبية العالي.",
},
602: {
    "B": "الـ<bdi>morphine</bdi> يسكن الألم بس ما يصحح ارتفاع الكالسيوم المسبب ل<bdi>symptoms</bdi> ثانية.",
    "C": "البيسفوسفونيت الفموي ضعيف الامتصاص وغير مناسب ل<bdi>case</bdi> <bdi>acute</bdi> عرضية.",
    "D": "الـ<bdi>furosemide</bdi> قبل الترطيب الكافي يزيد الجفاف ويسوي ارتفاع الكالسيوم أسوأ.",
},
603: {
    "A": "متلازمة كون تسبب نقص بوتاسيوم مع ضغط <bdi>elevated</bdi>، مو نقص صوديوم <bdi>severe</bdi> بهالشكل.",
    "B": "أديسون يعطي نقص صوديوم مع زيادة بوتاسيوم عادة مع هبوط ضغط وجفاف واضح، مو مذكورين هنا.",
    "C": "كوشينغ يسبب نقص بوتاسيوم وضغط <bdi>elevated</bdi>، مو الصورة الكهرلية هنا.",
},
604: {
    "A": "أشعة البطن ما لها علاقة مباشرة ب<bdi>cause</bdi> ارتفاع الـ<bdi>prolactin</bdi> عند هالمريض.",
    "B": "سكر الدم الصائم ما يوضح <bdi>cause</bdi> أعراضه التناسلية وارتفاع الـ<bdi>prolactin</bdi>.",
    "C": "مستوى التستوستيرون مفيد كفحص مكمل بس مو الـ<bdi>step</bdi> الأهم لتحديد <bdi>cause</bdi> الـ<bdi>prolactin</bdi> الـ<bdi>elevated</bdi>.",
},
605: {
    "B": "أورام الكظر الحميدة تسبب كبت لـACTH فما تعطي تصبغ جلد.",
    "C": "سرطان الكظر أيضًا يكبت ACTH بنفس الآلية، فما يفسر التصبغ الموجود.",
    "D": "الصورة السريرية والمخبرية تدعم <bdi>diagnosis</bdi> واضح، فخيار عدم وجود <bdi>diagnosis</bdi> غير صحيح.",
},
})

EXPLANATIONS.update({
606: {
    "idea": "رجل عنده كثرة تبول وعطش، واختبار الحرمان من الماء أظهر أسمولية دم عالية بدون تركيز كافٍ للبول، والسؤال يبي الـ<bdi>diagnosis</bdi> الأرجح من بين أنواع كثرة البول.",
    "clues": [
        ("increased urine output, especially during the<br>night and increased thirst", "<bdi>symptoms</bdi> كثرة بول وعطش تدعم داء <bdi>diabetes</bdi> الكاذب أو شرب زايد للماء"),
        ("Serum osmolality above normal without adequate concentration of urine osmolality", "فشل بتركيز البول رغم الحاجة له، يستبعد شرب الماء الزايد الـ<bdi>normal</bdi> (polydipsia)"),
        ("no response to desmopressin administration", "غياب الاستجابة لمشابه الـ ADH، نقطة أساسية بالتفريق بين أنواع الـ DI"),
    ],
    "why_correct": [
        "فشل تركيز البول رغم ارتفاع أسمولية الدم يثبت وجود <bdi>diabetes insipidus</bdi> حقيقي، ويستبعد شرب الماء النفسي (الكلى بهذه الـ<bdi>case</bdi> تقدر تركز البول لو أعطيناها الفرصة).",
        "اختبار الاستجابة للـ <bdi>desmopressin</bdi> هو اللي يميز بين المركزي (يستجيب لأن المشكلة نقص إفراز ADH) والكلوي (ما يستجيب لأن المشكلة بمقاومة الكلى نفسها).",
        "الملف هنا يصنف الـ<bdi>case</bdi> ك<bdi>diabetes</bdi> كاذب مركزي، وهذا هو الجواب المعتمد على البطاقة.",
    ],
    "when_changes": [
        "لو استجاب الـ<bdi>patient</bdi> جيدًا لإعطاء الـ desmopressin (تركز البول بعده)، يثبت الـ<bdi>diagnosis</bdi> المركزي بشكل واضح.",
        "لو فيه شرب ماء زايد بدون <bdi>cause</bdi> عضوي وتحسن التركيز مع تقييد الماء تدريجيًا، يصير الـ<bdi>diagnosis</bdi> شرب نفسي زائد بدل DI حقيقي.",
    ],
    "rule": "اختبار الحرمان من الماء يثبت وجود DI، واستجابة الـ desmopressin هي اللي تفرق بين المركزي والكلوي.",
    "comparison": {
        "headers": ["النوع", "الاستجابة لـ Desmopressin"],
        "rows": [
            ["<bdi>Central DI</bdi>", "يستجيب (يتركز البول)"],
            ["<bdi>Nephrogenic DI</bdi>", "لا يستجيب"],
        ],
    },
    "guideline_note": "بشكل كلاسيكي بالمراجع، عدم الاستجابة لمشابه الـ ADH (desmopressin) هو الـ<bdi>sign</bdi> المميزة لـ nephrogenic diabetes insipidus وليس المركزي (اللي يفترض يستجيب). ملاحظة الطالب المرفقة بالملف نفسه تشير لنفس النقطة. رغم كذا، الجواب المعتمد على البطاقة يبقى Central DI كما بالملف.",
},
607: {
    "idea": "<bdi>patient</bdi> عنده <bdi>symptoms</bdi> فرط نشاط درقي واضحة (عصبية، حرارة، <bdi>palpitations</bdi>) مع فحص رقبة <bdi>normal</bdi> (بدون تضخم درقي محسوس)، والتحاليل تظهر TSH <bdi>low</bdi> وT4 وT3 مرتفعين معًا، فالسؤال يبي الـ<bdi>diagnosis</bdi> العام الصحيح.",
    "clues": [
        ("irritability, heat intolerance and recent onset of heart<br>palpitations", "<bdi>symptoms</bdi> كلاسيكية لفرط نشاط الدرقية"),
        ("The neck examination is normal", "يستبعد وجود ضخامة درقية واضحة"),
        ("Thyroid-Stimulating Hormone 0.1", "TSH <bdi>low</bdi> جدًا، يدل على فرط نشاط الدرقية الأساسي"),
        ("Thyroxine (T4 free) 30.4", "T4 <bdi>elevated</bdi> بوضوح"),
        ("Triiodothyronine (T3 free) 9.5", "T3 أيضًا <bdi>elevated</bdi>"),
    ],
    "why_correct": [
        "ارتفاع T4 وT3 معًا مع انخفاض TSH يثبت فرط نشاط درقية حقيقي (<bdi>thyrotoxicosis</bdi>) بغض النظر عن الـ<bdi>cause</bdi> الدقيق.",
        "المتلازمة اليوثيرويدية الـ<bdi>patient</bdi> (sick euthyroid) تعطي عادة TSH <bdi>normal</bdi> أو <bdi>low</bdi> بسيط مع T3 <bdi>low</bdi>، وهذا عكس الصورة هنا تمامًا.",
        "T3 toxicosis <bdi>case</bdi> خاصة يكون فيها T3 <bdi>elevated</bdi> وT4 <bdi>normal</bdi>، لكن هنا الاثنين مرتفعين معًا، فالـ<bdi>diagnosis</bdi> العام الأشمل هو thyrotoxicosis.",
    ],
    "when_changes": [
        "لو كان T4 <bdi>normal</bdi> وT3 فقط هو الـ<bdi>elevated</bdi>، يصير الـ<bdi>diagnosis</bdi> الأدق T3 toxicosis.",
        "لو TSH كان <bdi>elevated</bdi> مع T4 <bdi>low</bdi>، يصير الـ<bdi>diagnosis</bdi> قصور درقية أولي بدل فرط النشاط.",
    ],
    "rule": "انخفاض TSH مع ارتفاع T4 وT3 معًا يعني فرط نشاط درقية حقيقي (thyrotoxicosis) بشكل عام.",
    "comparison": None,
    "guideline_note": None,
},
608: {
    "idea": "<bdi>patient</bdi> على جرعة ثابتة من الثيروكسين وعنده <bdi>symptoms</bdi> قصور درقية (تعب، برودة، زيادة وزن) وTSH <bdi>elevated</bdi>، فالسؤال يبي التعديل الصحيح بالجرعة وموعد إعادة الفحص.",
    "clues": [
        ("fatigue, cold<br>intolerance, and weight gain", "<bdi>symptoms</bdi> قصور درقية غير مسيطر عليها"),
        ("Heart Rate 57 /min", "بطء قلب، يتوافق مع قصور درقية"),
        ("TSH 19.9 mU/L (0.4-6.5)", "ارتفاع واضح بالـTSH يعني الجرعة الحالية غير كافية"),
    ],
    "why_correct": [
        "ارتفاع TSH مع <bdi>symptoms</bdi> قصور يعني الجرعة الحالية من الثيروكسين ناقصة، فالـ<bdi>step</bdi> الصحيحة زيادة الجرعة.",
        "بعد أي تعديل بجرعة الثيروكسين، لازم ننتظر حوالي 6 أسابيع قبل إعادة فحص TSH، لأن نصف عمر الدواء طويل ويحتاج وقت لين يوصل لمستوى ثابت بالدم.",
        "إعادة الفحص بعد 3 أسابيع فقط مبكر جدًا وما يعكس التأثير الحقيقي للجرعة الجديدة على الـTSH.",
    ],
    "when_changes": [
        "لو TSH كان <bdi>low</bdi> مع <bdi>symptoms</bdi> فرط جرعة، الـ<bdi>step</bdi> الصحيحة تنقيص الجرعة بدل زيادتها.",
        "لو الـ<bdi>patient</bdi> حامل، فترة إعادة الفحص بعد تعديل الجرعة تكون أقصر (حوالي 4 أسابيع) ب<bdi>cause</bdi> سرعة تغير الاحتياج.",
    ],
    "rule": "أي تعديل بجرعة الثيروكسين يحتاج إعادة فحص TSH بعد حوالي 6 أسابيع، مو أبكر من كذا.",
    "comparison": None,
    "guideline_note": None,
},
609: {
    "idea": "رجل عنده تحسس وثر لبني من الثديين مع صداع وضعف رغبة جنسية وعقم، والتحاليل تظهر <bdi>prolactin</bdi> <bdi>elevated</bdi> جدًا مع قصور درقية ثانوي بسيط، صورة توحي بورم كبير نخامي مفرز لل<bdi>prolactin</bdi> يضغط على التصالب البصري.",
    "clues": [
        ("discomfort in both breasts with milk production", "ثر لبني من الثديين عند رجل، <bdi>sign</bdi> قوية لفرط <bdi>prolactin</bdi>"),
        ("headache and low sexual interest", "<bdi>symptoms</bdi> إضافية تدعم ورم نخامي كبير مع قصور غدد تناسلية"),
        ("Prolactin 2350 (&lt;870)", "ارتفاع كبير جدًا بالـ<bdi>prolactin</bdi>"),
        ("Thyroid-Stimulating Hormone 6.8", "ارتفاع بسيط بالـTSH مع T4 <bdi>low</bdi> حدي، يوحي بتأثر محور الدرقية من ضغط الورم"),
    ],
    "why_correct": [
        "الورم النخامي المفرز لل<bdi>prolactin</bdi> لما يكبر يضغط على التصالب البصري (<bdi>optic chiasm</bdi>) من الوسط، فيصيب الألياف العابرة القادمة من الجزء الأنفي بكل عين.",
        "هذا الضغط يسبب فقدان الرؤية بالمجال الصدغي بكلا العينين، وهو ما يسمى <bdi>bitemporal hemianopia</bdi>.",
        "باقي أنواع فقدان المجال البصري (سكوتوما تقاطعي، ربعي علوي، أو نصفي متماثل) تنتج عن إصابات بمواقع مختلفة عن الضغط المباشر على وسط التصالب.",
    ],
    "when_changes": [
        "لو الورم صغير جدًا (ميكروأدينوما) بدون ضغط على التصالب، غالبًا ما يكون فيه أي عيب بالمجال البصري أصلًا.",
        "لو الإصابة كانت بمكان خلف التصالب بدل عنده، يصير العيب البصري نصفي متماثل بدل صدغي مزدوج.",
    ],
    "rule": "ورم نخامي كبير يضغط على وسط التصالب البصري يعطي كلاسيكيًا bitemporal hemianopia.",
    "comparison": None,
    "guideline_note": None,
},
610: {
    "idea": "امرأة توقف دورتها الشهرية 9 أشهر مع ثر لبني وضعف رغبة جنسية وعقم، والـ<bdi>prolactin</bdi> عندها <bdi>elevated</bdi> جدًا بينما باقي الهرمونات <bdi>normal</bdi> تقريبًا، والسؤال يبي أنسب فحص تالي.",
    "clues": [
        ("menstrual cycle has stopped for the last 9 months", "انقطاع طمث ثانوي، من آثار فرط الـ<bdi>prolactin</bdi>"),
        ("discomfort in both breasts with milk production", "ثر لبني، <bdi>sign</bdi> مباشرة لفرط الـ<bdi>prolactin</bdi>"),
        ("pregnancy test is negative", "يستبعد الحمل ك<bdi>cause</bdi> لانقطاع الطمث والثر اللبني"),
        ("Prolactin 2450 (&lt;870)", "ارتفاع كبير جدًا بالـ<bdi>prolactin</bdi> يوجه نحو ورم نخامي"),
    ],
    "why_correct": [
        "ارتفاع الـ<bdi>prolactin</bdi> الكبير وغير المفسر بعد استبعاد الحمل يوجه بقوة نحو ورم نخامي مفرز لل<bdi>prolactin</bdi>.",
        "أفضل فحص لتأكيد وتحديد الورم هو <bdi>Brain MRI</bdi> مركّز على الغدة النخامية.",
        "فحوصات الرقبة والحوض والثدي ما تفسر <bdi>cause</bdi> ارتفاع الـ<bdi>prolactin</bdi> نفسه، فهي مو الفحص الأنسب هنا.",
    ],
    "when_changes": [
        "لو الفحص الجسدي والتاريخ يوحي بمشكلة درقية واضحة، يصير فحص وظائف الدرقية أولوية قبل التصوير.",
        "لو الـ<bdi>prolactin</bdi> كان <bdi>elevated</bdi> بشكل بسيط فقط، يفضل تكراره أولًا لاستبعاد <bdi>causes</bdi> عابرة قبل التصوير المباشر.",
    ],
    "rule": "ارتفاع الـ<bdi>prolactin</bdi> الكبير وغير المفسر عند امرأة غير حامل يحتاج Brain MRI ل<bdi>assessment</bdi> الغدة النخامية.",
    "comparison": None,
    "guideline_note": None,
},
611: {
    "idea": "امرأة عندها تضخم درقي مع <bdi>symptoms</bdi> فرط نشاط درقية وثر لبني وانقطاع طمث، والتحاليل تظهر T4 <bdi>elevated</bdi> مع TSH <bdi>elevated</bdi> أيضًا بدل أن يكون <bdi>low</bdi>، وهذا نمط غير متوقع يوجه لورم نخامي مفرز TSH.",
    "clues": [
        ("frequent bowel movement, increased appetite and weight loss", "<bdi>symptoms</bdi> فرط نشاط درقية واضحة"),
        ("period has stopped and she has noticed a milky discharge", "انقطاع طمث وثر لبني، يدعم تأثر محور نخامي أوسع"),
        ("small diffuse goiter", "تضخم درقي منتشر بسيط"),
        ("Thyroxine (T4 free) 19.5", "T4 <bdi>elevated</bdi>، يتوافق مع فرط النشاط"),
        ("Thyroid-Stimulating Hormone 8.7", "TSH <bdi>elevated</bdi> رغم ارتفاع T4، وهذا غير منطقي بفرط النشاط الدرقي الأولي (المفروض يكون <bdi>low</bdi>)"),
    ],
    "why_correct": [
        "بفرط النشاط الدرقي الأولي الـ<bdi>normal</bdi>، لازم يكون TSH <bdi>low</bdi> لأن الجسم يكبت إفرازه ب<bdi>cause</bdi> زيادة T4، لكن هنا TSH <bdi>elevated</bdi> رغم ارتفاع T4، وهذا نمط غير ملائم (inappropriate).",
        "هذا النمط يوجه لورم بالغدة النخامية يفرز TSH بشكل مستقل (<bdi>TSH-secreting pituitary adenoma</bdi>)، وهو ما يفسر أيضًا اضطراب الدورة والثر اللبني من تأثر باقي الغدة.",
        "أفضل تصوير لتأكيد هذا الـ<bdi>diagnosis</bdi> هو <bdi>Pituitary MRI</bdi> لتحديد الورم النخامي المسبب.",
    ],
    "when_changes": [
        "لو كان TSH <bdi>low</bdi> مع T4 <bdi>elevated</bdi> (الصورة الـ<bdi>normal</bdi> بفرط النشاط الأولي)، يصير تصوير الدرقية نفسها (ultrasound) هو المنطقي بدل النخامية.",
        "لو التضخم الدرقي كان عقدة واحدة سامة، يوجه التفكير نحو مسح درقي باليود بدل تصوير النخامية.",
    ],
    "rule": "ارتفاع T4 مع TSH غير مكبوت (<bdi>normal</bdi> أو <bdi>elevated</bdi>) نمط غير متوقع يوجه للبحث عن ورم نخامي مفرز TSH بالرنين المغناطيسي.",
    "comparison": None,
    "guideline_note": None,
},
612: {
    "idea": "امرأة عندها سرطان ثدي منتشر لرئتيها، جاءت بكثرة بول وعطش، والتحاليل تظهر صوديوم <bdi>elevated</bdi> مع بول مخفف جدًا رغم الحاجة لتركيزه، وهذا يوحي ب<bdi>diabetes</bdi> كاذب ناتج عن انتشار الورم للدماغ.",
    "clues": [
        ("excessive urination and thirst", "<bdi>symptoms</bdi> كثرة بول وعطش"),
        ("right mastectomy 1 year ago", "تاريخ سرطان ثدي، <bdi>risk</bdi> انتشار للدماغ"),
        ("lung metastases were diagnosed", "دليل على <bdi>disease</bdi> منتشر فعليًا يزيد احتمال انتشار للدماغ أيضًا"),
        ("Sodium 150 (134-146)", "ارتفاع صوديوم، يتوافق مع فقد ماء زائد"),
        ("Osmolality 110 (280-910)", "بول مخفف جدًا رغم ارتفاع صوديوم الدم، فشل بتركيز البول"),
    ],
    "why_correct": [
        "ارتفاع الصوديوم مع بول مخفف جدًا (فشل بتركيزه رغم الحاجة) هو نمط <bdi>diabetes insipidus</bdi> الكلاسيكي، ناتج غالبًا هنا عن انتشار الورم للغدة النخامية أو تحت المهاد.",
        "الـ SIADH والشرب النفسي الزائد يعطون نقص صوديوم (hyponatremia) ب<bdi>cause</bdi> احتباس أو زيادة الماء، وهذا عكس الصورة هنا تمامًا.",
        "التاريخ الورمي المنتشر يدعم وجود <bdi>cause</bdi> عضوي (نقيلة بالمنطقة النخامية) وراء <bdi>diabetes</bdi> الكاذب المركزي.",
    ],
    "when_changes": [
        "لو كان الصوديوم <bdi>low</bdi> بدل <bdi>elevated</bdi> مع بول مركز بشكل غير متوقع، يصير الـ<bdi>diagnosis</bdi> SIADH.",
        "لو ما فيه تاريخ ورمي وكان الصوديوم <bdi>low</bdi> مع شرب ماء زائد موثق، يصير الـ<bdi>diagnosis</bdi> شرب نفسي زائد (psychogenic polydipsia).",
    ],
    "rule": "فرط صوديوم الدم مع بول مخفف رغم الحاجة لتركيزه يشخص diabetes insipidus، بعكس SIADH والشرب النفسي اللي يعطون نقص صوديوم.",
    "comparison": {
        "headers": ["الـ<bdi>case</bdi>", "اتجاه الصوديوم"],
        "rows": [
            ["<bdi>Diabetes insipidus</bdi>", "ارتفاع (فقد ماء)"],
            ["<bdi>SIADH</bdi>", "انخفاض (احتباس ماء)"],
            ["<bdi>Psychogenic polydipsia</bdi>", "انخفاض (زيادة ماء)"],
        ],
    },
    "guideline_note": None,
},
613: {
    "idea": "امرأة شابة عندها تورم مؤلم بالرقبة مع صعوبة بلع وحرارة، و<bdi>symptoms</bdi> فرط نشاط درقية مع ارتفاع كبير بمعدل الترسيب، صورة كلاسيكية لالتهاب درقية تحت <bdi>acute</bdi> (<bdi>subacute thyroiditis</bdi>) بعد عدوى فيروسية غالبًا، وعلاجها التهابي مو مضاد للدرقية.",
    "clues": [
        ("painful neck swelling for the last week", "تورم مؤلم بالرقبة، يميز التهاب تحت الـ<bdi>acute</bdi> عن <bdi>Graves' disease</bdi> غير المؤلم"),
        ("sore throat and difficulty in swallowing", "<bdi>symptoms</bdi> تدعم عدوى فيروسية سابقة بالحلق"),
        ("diffuse tender anterior neck<br>swelling", "غدة درقية مؤلمة عند الجس، <bdi>sign</bdi> مميزة لالتهاب تحت <bdi>acute</bdi>"),
        ("ESR 58 (3-15)", "ارتفاع كبير بمعدل الترسيب، يدعم التهاب <bdi>acute</bdi> بالغدة"),
        ("Thyroid-Stimulating Hormone 0.03", "TSH <bdi>low</bdi> جدًا مع T4 <bdi>elevated</bdi>، فرط نشاط عابر من تسرب الهرمون المخزن"),
    ],
    "why_correct": [
        "الالتهاب الدرقي تحت الـ<bdi>acute</bdi> ينتج عن تسرب الهرمون المخزن من خلايا الغدة الملتهبة، مو زيادة إنتاج حقيقي، فمضادات الدرقية زي methimazole وPTU ما تفيد هنا.",
        "الـ<bdi>treatment</bdi> الأساسي التهابي؛ <bdi>prednisone</bdi> فعال بالحالات المؤلمة والـ<bdi>severe</bdi> مثل هذي لتخفيف الالتهاب والألم بسرعة.",
        "الترسيب العالي والألم الـ<bdi>severe</bdi> بالجس يدعمان اختيار الستيرويد بدل الانتظار على مضادات الالتهاب البسيطة فقط.",
    ],
    "when_changes": [
        "لو الألم بسيط والـ<bdi>case</bdi> <bdi>mild</bdi>، يفضل البدء بمضادات الالتهاب غير الستيرويدية (NSAIDs) قبل اللجوء للستيرويد.",
        "لو كانت الغدة غير مؤلمة مع فرط نشاط مستمر (مو عابر)، يصير الـ<bdi>diagnosis</bdi> <bdi>Graves' disease</bdi> والـ<bdi>treatment</bdi> مضاد درقية حقيقي.",
    ],
    "rule": "تضخم درقي مؤلم مع فرط نشاط عابر وترسيب <bdi>elevated</bdi> يشخص التهاب درقية تحت <bdi>acute</bdi>، وعلاجه مضاد التهاب (ستيرويد أو NSAIDs) مو مضاد درقية.",
    "comparison": None,
    "guideline_note": None,
},
614: {
    "idea": "امرأة بدأت <bdi>treatment</bdi> <bdi>hypothyroidism</bdi> بالليفوثيروكسين قبل أسبوعين بس، وTSH لسا <bdi>elevated</bdi> بشكل بسيط، والسؤال يبي القرار الصحيح بهالمرحلة المبكرة جدًا من الـ<bdi>treatment</bdi>.",
    "clues": [
        ("started on levothyroxine<br>for treatment of hypothyroidism 2 weeks before", "مدة قصيرة جدًا منذ بدء الـ<bdi>treatment</bdi>"),
        ("TSH 7.5 (0.4-6.5)", "ارتفاع بسيط فقط فوق الـ<bdi>normal</bdi>"),
    ],
    "why_correct": [
        "الثيروكسين يحتاج حوالي 6 أسابيع لين يوصل لمستوى ثابت بالدم ويعكس تأثيره الحقيقي على TSH.",
        "أسبوعين فترة قصيرة جدًا ل<bdi>assessment</bdi> الاستجابة، فمن الخطأ تغيير الجرعة الآن بناءً على TSH لسا في طور التعديل.",
        "الصح هو الاستمرار على نفس الجرعة وإعادة فحص TSH بعد 1 إلى 2 شهر لإعطاء وقت كافٍ يعكس تأثير الجرعة الحالية.",
    ],
    "when_changes": [
        "لو مر أكثر من 6 أسابيع على نفس الجرعة وTSH لسا <bdi>elevated</bdi>، يصير تعديل الجرعة منطقي.",
        "لو الـ<bdi>patient</bdi> حامل، يفضل إعادة الفحص بفترة أقصر (حوالي 4 أسابيع) لأهمية الضبط السريع بالحمل.",
    ],
    "rule": "لا يعدّل جرعة الثيروكسين قبل مرور فترة كافية (حوالي 6 أسابيع) على الجرعة الحالية.",
    "comparison": None,
    "guideline_note": None,
},
615: {
    "idea": "امرأة حامل عندها فرط نشاط درقي عرضي مع غدة درقية عقيدية منتشرة، وأجسام مضادة درقية سلبية، والسؤال يبي أفضل <bdi>step</bdi> علاجية تناسب الحمل.",
    "clues": [
        ("23-year-old pregnant patient", "الحمل يحدد الخيارات العلاجية المسموحة (يستبعد اليود المشع)"),
        ("thyroid gland is nodular, diffusely enlarged", "تضخم عقيدي منتشر، يوجه ل<bdi>cause</bdi> غير <bdi>Graves' disease</bdi> النموذجي"),
        ("Thyroid-Stimulating Hormone 0.1", "فرط نشاط درقي حقيقي (TSH <bdi>low</bdi>)"),
        ("Antithyroid Antibody negative", "يقلل احتمال <bdi>Graves' disease</bdi> النموذجي بس ما يستبعد فرط النشاط نفسه"),
    ],
    "why_correct": [
        "الـ<bdi>patient</bdi> حامل وعندها فرط نشاط درقي عرضي يحتاج <bdi>treatment</bdi> فوري وآمن للحمل.",
        "الدواء المضاد للدرقية (<bdi>antithyroid medication</bdi>) هو الخيار الآمن نسبيًا بالحمل للسيطرة على فرط النشاط بسرعة.",
        "اليود المشع ممنوع تمامًا بالحمل لأنه يعبر المشيمة ويضر الغدة الدرقية الجنينية، والجراحة والخزعة <bdi>procedures</bdi> تحفظ لحالات معينة مو ك<bdi>step</bdi> أولى هنا.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>patient</bdi> غير حامل، ممكن يكون اليود المشع خيار علاجي معقول حسب باقي الصورة.",
        "لو فشل الـ<bdi>treatment</bdi> الدوائي بالسيطرة على الـ<bdi>symptoms</bdi> بالحمل، يصير التفكير بجراحة (subtotal thyroidectomy) بالثلث الثاني ك<bdi>step</bdi> تالية.",
    ],
    "rule": "فرط النشاط الدرقي العرضي بالحمل يعالج بمضادات الدرقية الدوائية، ويمنع اليود المشع تمامًا طول فترة الحمل.",
    "comparison": None,
    "guideline_note": None,
},
})

EXPLANATIONS.update({
616: {
    "idea": "<bdi>patient</bdi> عنده عقيدة صلبة بحجم 2 سم بالموجات فوق الصوتية على الدرقية، والسؤال يبي أفضل <bdi>step</bdi> تالية لتقييمها.",
    "clues": [
        ("2 cm solid thyroid nodule", "عقيدة صلبة بحجم يستحق <bdi>assessment</bdi> إضافي للاستبعاد سرطان"),
    ],
    "why_correct": [
        "أي عقيدة درقية صلبة بحجم 1 سم فأكثر (وTSH <bdi>normal</bdi> أو <bdi>elevated</bdi>) تحتاج <bdi>assessment</bdi> نسيجي مباشر لاستبعاد السرطان.",
        "الخزعة بالإبرة الدقيقة (<bdi>fine needle aspiration</bdi>) هي الفحص الأدق والأرخص والأقل تدخلًا لتحديد طبيعة العقيدة (حميدة أو خبيثة).",
        "تكرار الموجات فوق الصوتية أو تصوير مقطعي أو مسح باليود ما يعطي <bdi>diagnosis</bdi> نسيجي مباشر، فهي مو الـ<bdi>step</bdi> الأنسب أولًا.",
    ],
    "when_changes": [
        "لو العقيدة كانت أقل من 1 سم وبدون ملامح مشبوهة، ممكن تكتفى بالـ<bdi>follow-up</bdi> بالموجات فوق الصوتية.",
        "لو كان TSH <bdi>low</bdi> (يوحي بعقيدة ساخنة نشطة)، يفضل مسح باليود قبل الخزعة لأن العقيدات الساخنة نادرًا ما تكون خبيثة.",
    ],
    "rule": "أي عقيدة درقية صلبة بحجم يستحق الـ<bdi>assessment</bdi>، الخزعة بالإبرة الدقيقة هي الـ<bdi>step</bdi> التشخيصية التالية القياسية.",
    "comparison": None,
    "guideline_note": None,
},
617: {
    "idea": "<bdi>patient</bdi> <bdi>diabetes</bdi> مسيطر عليه بشكل ممتاز (سكر وHbA1c طبيعيين) وبدون <bdi>signs</bdi> <bdi>complications</bdi>، لكن ضغطه <bdi>elevated</bdi> بثلاث قراءات متكررة، والسؤال يبي أفضل <bdi>step</bdi> ب<bdi>management</bdi> الضغط عنده.",
    "clues": [
        ("HbA1c level of 5.8%", "سيطرة ممتازة على <bdi>diabetes</bdi>، يستبعد الحاجة لتعديل <bdi>treatment</bdi> <bdi>diabetes</bdi>"),
        ("no signs of retinopathy", "يستبعد <bdi>complications</bdi> دقيقة الأوعية حاليًا"),
        ("Blood pressure 149/90 mmHg (three readings)", "ضغط <bdi>elevated</bdi> مؤكد بعدة قراءات، يحتاج <bdi>treatment</bdi>"),
    ],
    "why_correct": [
        "<bdi>patient</bdi> <bdi>diabetes</bdi> مع ضغط <bdi>elevated</bdi> مؤكد بعدة قراءات يحتاج بدء <bdi>treatment</bdi> خافض للضغط، والخيار الأفضل عنده مثبطات الإنزيم المحول للأنجيوتنسين (<bdi>ACE inhibitor</bdi>) لحمايتها الكلوية الإضافية.",
        "لا داعي لتغيير <bdi>treatment</bdi> <bdi>diabetes</bdi> نفسه لأن الضبط ممتاز حاليًا، فالمشكلة المطروحة هنا هي الضغط فقط.",
        "حاصرات البيتا والسلفونيل يوريا ما تعالجان مشكلة الضغط المطروحة بشكل مباشر ومناسب بهذا السياق.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عنده بروتين بالبول (اعتلال كلوي <bdi>diabetes</bdi>) يصير الـACE inhibitor أهم وأوضح استطبابًا.",
        "لو ما فيه <bdi>diabetes</bdi> أصلًا وضغطه <bdi>elevated</bdi> بشكل معزول، تصير خيارات ثانية زي مدرات البول خيار أول مقبول أيضًا.",
    ],
    "rule": "ب<bdi>patient</bdi> <bdi>diabetes</bdi> المصاب بارتفاع ضغط مؤكد، مثبطات الإنزيم المحول للأنجيوتنسين هي الخيار الأول لحمايتها الكلوية.",
    "comparison": None,
    "guideline_note": None,
},
618: {
    "idea": "<bdi>patient</bdi> شاب مصاب بالحماض الكيتوني <bdi>diabetes</bdi> وبصدمة (ضغط <bdi>low</bdi> جدًا وتسرع قلب <bdi>severe</bdi>)، مع بوتاسيوم <bdi>elevated</bdi> وبيكربونات <bdi>low</bdi> جدًا، والسؤال يبي أفضل <bdi>step</bdi> علاجية أولية.",
    "clues": [
        ("Blood pressure 80/50 mmHg", "صدمة نقص حجم <bdi>severe</bdi> تحتاج سوائل عاجلة قبل أي شي ثاني"),
        ("Heart rate 140 /min", "تسرع قلب <bdi>severe</bdi> يدعم الصدمة"),
        ("Random Glucose 52.7", "سكر <bdi>elevated</bdi> جدًا يفسر الجفاف الـ<bdi>severe</bdi>"),
        ("Potassium 6", "بوتاسيوم <bdi>elevated</bdi>، يعني ما يحتاج تعويض بوتاسيوم فورًا"),
        ("Bicarbonate 5", "حماض استقلابي <bdi>severe</bdi> جدًا"),
    ],
    "why_correct": [
        "الـ<bdi>patient</bdi> بصدمة نقص حجم <bdi>severe</bdi>، فالـ<bdi>step</bdi> الأولى العاجلة هي إعطاء جرعة سوائل وريدية سريعة (<bdi>bolus</bdi>) لتحسين التروية قبل أي شي ثاني.",
        "بعد بدء السوائل، يبدأ تسريب الـ<bdi>insulin</bdi> الوريدي البطيء (0.1 وحدة/كغ/ساعة) للسيطرة التدريجية على السكر والكيتونات بدون هبوط سكر مفاجئ.",
        "البوتاسيوم <bdi>elevated</bdi> حاليًا (6)، فما يحتاج إضافة بوتاسيوم للسوائل الآن؛ يضاف لاحقًا لما ينخفض تحت 5.2 أثناء الـ<bdi>treatment</bdi> بالـ<bdi>insulin</bdi>.",
    ],
    "when_changes": [
        "لو البوتاسيوم كان <bdi>low</bdi> من البداية (أقل من 3.3)، لازم نعوضه أولًا قبل بدء الـ<bdi>insulin</bdi> لتجنب هبوطه أكثر.",
        "لو الضغط ما تحسن رغم السوائل الكافية، يصير التفكير بدعم ضغط بأدوية رافعة للضغط مثل الـ<bdi>dopamine</bdi>.",
    ],
    "rule": "<bdi>treatment</bdi> الحماض الكيتوني <bdi>diabetes</bdi> بوجود صدمة يبدأ بجرعة سوائل وريدية سريعة، ثم تسريب <bdi>insulin</bdi> تدريجي، مع تعديل البوتاسيوم حسب مستواه.",
    "comparison": None,
    "guideline_note": None,
},
619: {
    "idea": "رجل بدون <bdi>symptoms</bdi> يفحص لل<bdi>diabetes</bdi> ب<bdi>cause</bdi> تاريخ عائلي، ونتيجته متناقضة: سكر صائم <bdi>elevated</bdi> (يدخل بمعيار <bdi>diabetes</bdi>) لكن HbA1c بمرحلة ما قبل <bdi>diabetes</bdi> فقط، فالسؤال يبي الـ<bdi>step</bdi> الصحيحة للتأكيد.",
    "clues": [
        ("family history of type 2 diabetes undergoes screening", "فحص روتيني بدون <bdi>symptoms</bdi>"),
        ("Glucose, fasting 7.4 (3.5-6.5)", "قيمة تدخل بمعيار <bdi>diagnosis</bdi> <bdi>diabetes</bdi> (≥7)"),
        ("Hemoglobin A1C 6.3 (4.7-5.6)", "قيمة بمرحلة ما قبل <bdi>diabetes</bdi> (تحت حد الـ<bdi>diagnosis</bdi>)، تناقض مع السكر الصائم"),
    ],
    "why_correct": [
        "بالشخص بدون <bdi>symptoms</bdi>، <bdi>diagnosis</bdi> <bdi>diabetes</bdi> يحتاج فحصين غير طبيعيين متوافقين، وهنا الفحصين متناقضين ببعض.",
        "الـ<bdi>step</bdi> الصحيحة هي <bdi>procedure</bdi> فحص تحمل السكر الفموي لمدة ساعتين (<bdi>2-hour 75 g OGTT</bdi>) لحسم الـ<bdi>diagnosis</bdi> بدقة أكبر.",
        "إعادة السكر العشوائي أو تكرار HbA1c بعد 6 أسابيع ما يحل التناقض الحالي بنفس دقة اختبار تحمل السكر الفموي.",
    ],
    "when_changes": [
        "لو كان الفحصان متوافقين على <bdi>diagnosis</bdi> <bdi>diabetes</bdi> (كلاهما بمعيار <bdi>diabetes</bdi>)، ما نحتاج فحص إضافي، الـ<bdi>diagnosis</bdi> يثبت مباشرة.",
        "لو الـ<bdi>patient</bdi> عنده <bdi>symptoms</bdi> <bdi>diabetes</bdi> واضحة (عطش، كثرة بول)، يكفي فحص واحد غير <bdi>normal</bdi> لإثبات الـ<bdi>diagnosis</bdi> بدون تكرار.",
    ],
    "rule": "بالشخص بدون <bdi>symptoms</bdi> مع <bdi>results</bdi> فحوصات <bdi>diabetes</bdi> متناقضة، فحص تحمل السكر الفموي لمدة ساعتين يحسم الـ<bdi>diagnosis</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
620: {
    "idea": "نفس الـ<bdi>patient</bdi> السابق تقريبًا لكن هذي المرة عنده <bdi>symptom</bdi> (كثرة بول) والفحصين متوافقين على مستوى <bdi>diabetes</bdi>، فالـ<bdi>diagnosis</bdi> يثبت مباشرة بدون حاجة لفحص إضافي.",
    "clues": [
        ("history of polyuria", "<bdi>symptom</bdi> إيجابي يدعم <bdi>diagnosis</bdi> <bdi>diabetes</bdi> ويقلل الحاجة لفحص تأكيدي إضافي"),
        ("Glucose, fasting 7.0 (3.5-5.5)", "قيمة تشخيصية لل<bdi>diabetes</bdi> (≥7)"),
        ("Hemoglobin A1C 7.1 (5.7-6.4)", "قيمة تشخيصية لل<bdi>diabetes</bdi> (≥6.5%) هنا أيضًا"),
    ],
    "why_correct": [
        "الفحصين هنا (السكر الصائم وHbA1c) متوافقين ويقعان ضمن معيار <bdi>diagnosis</bdi> <bdi>diabetes</bdi>، فالـ<bdi>diagnosis</bdi> يثبت مباشرة.",
        "وجود <bdi>symptom</bdi> إيجابي (كثرة بول) يدعم الـ<bdi>diagnosis</bdi> السريري بشكل إضافي بجانب المخبري.",
        "لا حاجة لفحص تحمل سكر فموي إضافي لأن الـ<bdi>diagnosis</bdi> أصلًا واضح ومؤكد بفحصين متوافقين.",
    ],
    "when_changes": [
        "لو كان أحد الفحصين فقط غير <bdi>normal</bdi> والثاني بمنطقة ما قبل <bdi>diabetes</bdi>، نحتاج فحص إضافي (OGTT) لحسم الأمر كما بالسؤال السابق.",
        "لو الـ<bdi>patient</bdi> شاب جدًا مع سمنة <bdi>severe</bdi> و<bdi>signs</bdi> مقاومة <bdi>insulin</bdi>، يبقى النوع الثاني هو الأرجح رغم صغر السن.",
    ],
    "rule": "وجود <bdi>symptom</bdi> إيجابي مع فحصين متوافقين ضمن معيار <bdi>diabetes</bdi> يكفي لتأكيد <bdi>diagnosis</bdi> النوع الثاني من <bdi>diabetes</bdi> مباشرة.",
    "comparison": None,
    "guideline_note": None,
},
621: {
    "idea": "رجل بدأ حديثًا على الـ<bdi>metformin</bdi> لل<bdi>diabetes</bdi> النوع الثاني ويأتي لأول <bdi>follow-up</bdi>، والسؤال يبي أي فحص يستخدم سنويًا ل<bdi>assessment</bdi> تأثر الكلى ب<bdi>diabetes</bdi> تحديدًا.",
    "clues": [
        ("started on metformin 500 mg TDS", "بداية <bdi>treatment</bdi> <bdi>diabetes</bdi>، <bdi>follow-up</bdi> روتينية مطلوبة"),
        ("Creatinine 125 (44-115)", "ارتفاع بسيط بالكرياتينين يستدعي <bdi>follow-up</bdi> دقيقة لوظائف الكلى"),
    ],
    "why_correct": [
        "الفحص السنوي القياسي لكشف <bdi>nephropathy</bdi> <bdi>diabetes</bdi> المبكر هو نسبة الألبومين للكرياتينين بعينة بول عشوائية (<bdi>urine albumin/creatinine ratio</bdi>).",
        "هذا الفحص يكشف تسرب بروتين <bdi>mild</bdi> (ميكروالبومين) قبل ما يصير واضح بتحليل بول عادي أو يرتفع الكرياتينين بشكل كبير.",
        "الكرياتينين والفلتره الكبيبية المقدرة مفيدين ل<bdi>assessment</bdi> الوظيفة العامة، لكن نسبة الألبومين للكرياتينين أكثر حساسية لكشف الضرر الكلوي المبكر المرتبط ب<bdi>diabetes</bdi> تحديدًا.",
    ],
    "when_changes": [
        "لو ظهرت نسبة الألبومين للكرياتينين <bdi>elevated</bdi> بشكل متكرر، يصير التركيز على <bdi>treatment</bdi> وقائي كلوي إضافي (مثل ACE inhibitor) بجانب <bdi>follow-up</bdi> السكر.",
        "لو كان لدى الـ<bdi>patient</bdi> بروتين واضح بتحليل البول العادي أصلًا، يعني المرحلة متقدمة أكثر من الميكروالبومين البسيط.",
    ],
    "rule": "الـ<bdi>follow-up</bdi> السنوية ل<bdi>nephropathy</bdi> <bdi>diabetes</bdi> تكون بنسبة الألبومين للكرياتينين بالبول، مو الكرياتينين وحده.",
    "comparison": None,
    "guideline_note": None,
},
622: {
    "idea": "امرأة عندها <bdi>diabetes</bdi> نوع ثاني منذ 20 سنة، ضبطها الحالي غير كافٍ (HbA1c 7.8%)، والسؤال يبي الهدف الصحيح لنسبة السكر التراكمي عندها.",
    "clues": [
        ("type 2 diabetes for the past 20 years", "<bdi>patient</bdi> <bdi>diabetes</bdi> طويلة الأمد"),
        ("HbA1C 7.8", "أعلى من الهدف المعتاد للأغلبية"),
    ],
    "why_correct": [
        "الهدف العام المتعارف عليه لأغلب مرضى <bdi>diabetes</bdi> النوع الثاني (بدون <bdi>osteoporosis</bdi> أو <bdi>complications</bdi> <bdi>severe</bdi>) هو HbA1c أقل من 7%.",
        "هذا الهدف يوازن بين تقليل <bdi>complications</bdi> <bdi>diabetes</bdi> طويلة المدى وتجنب <bdi>risk</bdi> هبوط السكر الـ<bdi>severe</bdi> من ضبط صارم جدًا.",
        "أهداف أقل من ذلك (5% أو 5.5% أو 6%) صارمة جدًا وغير واقعية ولا يوصى بها بشكل عام لأغلب المرضى.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> كبيرة بالسن جدًا أو عندها هبوط سكر متكرر أو <bdi>complications</bdi> <bdi>severe</bdi>، يصير الهدف أعلى قليلًا (مثل أقل من 8%) لتقليل <bdi>risk</bdi> هبوط السكر.",
        "لو الـ<bdi>patient</bdi> شابة بدون <bdi>complications</bdi> وحديثة الـ<bdi>diagnosis</bdi>، ممكن يستهدف هدف أكثر صرامة قريب من الـ<bdi>normal</bdi>.",
    ],
    "rule": "الهدف العام لـHbA1c بأغلب مرضى <bdi>diabetes</bdi> النوع الثاني هو أقل من 7%.",
    "comparison": None,
    "guideline_note": None,
},
623: {
    "idea": "السؤال يبي أي <bdi>sign</bdi> بالبول تدل على <bdi>nephropathy</bdi> <bdi>diabetes</bdi> تحديدًا، من بين عدة خيارات ممكنة ب<bdi>diseases</bdi> كلوية مختلفة.",
    "clues": [
        ("diabetic nephropathy in type 2\ndiabetes", "يبحث عن الـ<bdi>sign</bdi> النموذجية لهذا النوع من <bdi>nephropathy</bdi> تحديدًا"),
    ],
    "why_correct": [
        "<bdi>nephropathy</bdi> <bdi>diabetes</bdi> يبدأ بتسرب البروتين (البومين) عبر الغشاء الكبيبي المتضرر، فالبروتينية (<bdi>proteinuria</bdi>) هي الـ<bdi>sign</bdi> المميزة له.",
        "هذا التسرب يتطور تدريجيًا من ميكروالبومين بسيط إلى بروتينية واضحة مع تقدم الـ<bdi>disease</bdi> بمرور السنين.",
        "الدم بالبول والقوالب الخلوية الحمراء يوجهان أكثر ل<bdi>diseases</bdi> كبيبية التهابية أو نزفية، والقوالب الهيالينية غير نوعية وتظهر حتى بحالات <bdi>normal</bdi>.",
    ],
    "when_changes": [
        "لو ظهر دم بالبول مع قوالب خلوية حمراء، يصير التفكير بالتهاب كبيبي غير <bdi>diabetes</bdi> (glomerulonephritis) بدل <bdi>nephropathy</bdi> <bdi>diabetes</bdi> النموذجي.",
        "لو كان التحليل يظهر قوالب هيالينية فقط بدون بروتين، هذا غالبًا لا يدل على أي <bdi>disease</bdi> كلوي مهم.",
    ],
    "rule": "البروتينية هي الـ<bdi>sign</bdi> البولية النموذجية والمبكرة ل<bdi>nephropathy</bdi> <bdi>diabetes</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
624: {
    "idea": "امرأة عندها <bdi>diabetes</bdi> حملي سابق وتاريخ عائلي قوي لل<bdi>diabetes</bdi>، وأرقامها الحالية على الحد الفاصل لما قبل <bdi>diabetes</bdi>، والسؤال يبي أفضل <bdi>treatment</bdi> وقائي لها الآن.",
    "clues": [
        ("gestational diabetes during her second pregnancy", "<bdi>factor</bdi> <bdi>risk</bdi> قوي للإصابة ب<bdi>diabetes</bdi> النوع الثاني مستقبلًا"),
        ("strong family history of type 2 diabetes", "<bdi>factor</bdi> <bdi>risk</bdi> إضافي"),
        ("Glucose, fasting 6.5 (3.5-6.5)", "على الحد الأعلى الـ<bdi>normal</bdi>/ما قبل <bdi>diabetes</bdi>"),
        ("HbA1C 5.5 (4.7-5.6)", "على الحد الأعلى الـ<bdi>normal</bdi> أيضًا، يدعم مرحلة ما قبل <bdi>diabetes</bdi>"),
    ],
    "why_correct": [
        "الـ<bdi>patient</bdi> عندها <bdi>factors</bdi> <bdi>risk</bdi> متعددة جدًا (<bdi>diabetes</bdi> حملي سابق، تاريخ عائلي قوي، سمنة) مع أرقام على حافة ما قبل <bdi>diabetes</bdi>.",
        "الـ<bdi>metformin</bdi> (<bdi>metformin</bdi>) يعتبر خيار وقائي مناسب وفعال بهذه الفئة عالية الخطورة لتأخير أو منع تطور <bdi>diabetes</bdi> النوع الثاني.",
        "الـ<bdi>insulin</bdi> والسلفونيل يوريا أدوية علاجية لل<bdi>diabetes</bdi> الفعلي وليست للوقاية، والأكاربوز أقل فعالية وأقل استخدامًا كخط أول وقائي.",
    ],
    "when_changes": [
        "لو أرقامها كانت <bdi>normal</bdi> تمامًا بدون <bdi>factors</bdi> <bdi>risk</bdi> إضافية، يكتفى بنصائح نمط الحياة فقط بدون دواء.",
        "لو تطور لديها <bdi>diagnosis</bdi> <bdi>diabetes</bdi> فعلي واضح، يصير الـ<bdi>metformin</bdi> <bdi>treatment</bdi> أساسي مو وقائي فقط.",
    ],
    "rule": "المرأة عالية الخطورة (<bdi>diabetes</bdi> حملي سابق + تاريخ عائلي قوي) مع أرقام على حافة ما قبل <bdi>diabetes</bdi>، الـ<bdi>metformin</bdi> خيار وقائي معقول.",
    "comparison": None,
    "guideline_note": None,
},
625: {
    "idea": "رجل سمين جدًا (سمنة <bdi>severe</bdi>) فشل بإنقاص وزنه رغم التزامه الكامل بحمية <bdi>low</bdi> السعرات وممارسة الرياضة، والسؤال يبي أفضل نصيحة لإنقاص الوزن عنده الآن.",
    "clues": [
        ("unable to lose weight despite being on an intensive lifestyle", "فشل واضح رغم التزام كامل بنمط حياة صحي"),
        ("Weight 125 kg", "وزن كبير جدًا مع الطول المعطى (BMI <bdi>elevated</bdi> جدًا)"),
        ("HbA1C 8.1", "<bdi>diabetes</bdi> غير مسيطر عليه أيضًا، <bdi>disease</bdi> مرافق للسمنة"),
    ],
    "why_correct": [
        "مؤشر كتلة الجسم عند هالمريض <bdi>elevated</bdi> جدًا (حوالي 42) مع فشل واضح بالطرق المحافظة رغم الالتزام الكامل ووجود <bdi>diabetes</bdi> مرافق غير مضبوط.",
        "بهذا المستوى من السمنة الـ<bdi>severe</bdi> مع <bdi>disease</bdi> مرافق، الجراحة الاستقلابية (<bdi>bariatric surgery</bdi>) هي الأكثر فعالية لإنقاص وزن كبير ومستدام وتحسين <bdi>diabetes</bdi>.",
        "زيادة الرياضة أو تقليل السعرات أكثر غير واقعية وغير كافية بعد فشل برنامج مكثف أصلًا، والأدوية المخفضة للوزن أقل فعالية من الجراحة بهالدرجة من السمنة.",
    ],
    "when_changes": [
        "لو مؤشر كتلة الجسم أقل (بين 27-30) بدون <bdi>disease</bdi> مرافق <bdi>severe</bdi>، تكون الأدوية المخفضة للوزن خيار أنسب من الجراحة.",
        "لو الـ<bdi>patient</bdi> ما جرب برنامج نمط حياة مكثف بعد، يفضل تجربته أولًا قبل التفكير بالجراحة.",
    ],
    "rule": "بالسمنة الـ<bdi>severe</bdi> مع <bdi>disease</bdi> مرافق (زي <bdi>diabetes</bdi>) وفشل الطرق المحافظة، الجراحة الاستقلابية هي الخيار الأكثر فعالية.",
    "comparison": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
606: {
    "A": "الـ<bdi>patient</bdi> حسب تصنيف الملف عنده <bdi>diabetes</bdi> كاذب مركزي، مو كلوي.",
    "B": "سوء استخدام مدرات يسبب فرط بول بس ما يعطي فشل تركيز مع أسمولية دم <bdi>elevated</bdi> بهذا النمط.",
    "D": "الشرب الزائد النفسي يعطي أسمولية دم <bdi>low</bdi> عادة، وهنا أسمولية الدم <bdi>elevated</bdi>.",
},
607: {
    "A": "المتلازمة اليوثيرويدية الـ<bdi>patient</bdi> تعطي TSH <bdi>normal</bdi> أو <bdi>low</bdi> مع T3 <bdi>low</bdi>، مو T4 وT3 مرتفعين بهذا الشكل.",
    "B": "<bdi>hypothyroidism</bdi> الأولي يعطي TSH <bdi>elevated</bdi> مع T4 <bdi>low</bdi>، عكس الصورة هنا تمامًا.",
    "D": "T3 toxicosis يكون فيه T4 <bdi>normal</bdi> مع T3 <bdi>elevated</bdi> فقط، وهنا الاثنين مرتفعين.",
},
608: {
    "B": "3 أسابيع فترة قصيرة جدًا ما تعكس تأثير الجرعة الجديدة على TSH بشكل دقيق.",
    "C": "تنقيص الجرعة خطأ هنا لأن الـ<bdi>patient</bdi> ب<bdi>case</bdi> قصور (TSH <bdi>elevated</bdi>) يحتاج زيادة مو تنقيص.",
    "D": "نفس خطأ تنقيص الجرعة، مع توقيت <bdi>follow-up</bdi> مبكر جدًا كمان.",
},
609: {
    "A": "السكوتوما التقاطعي يصيب عين واحدة بشكل رئيسي مع جزء من الأخرى، مو الصورة النموذجية هنا.",
    "C": "الربعي العلوي ينتج عادة عن إصابة بالفص الصدغي، مو ضغط مباشر على وسط التصالب.",
    "D": "النصفي المتماثل ينتج عن إصابة خلف التصالب البصري، مو عنده مباشرة.",
},
610: {
    "B": "الموجات فوق الصوتية على الرقبة ما تفسر <bdi>cause</bdi> ارتفاع الـ<bdi>prolactin</bdi> نفسه.",
    "C": "فحص الحوض لا علاقة له ب<bdi>cause</bdi> انقطاع الطمث الهرموني هنا.",
    "D": "الماموغرام يفحص الثدي بنيويًا بس ما يوضح <bdi>cause</bdi> فرط الـ<bdi>prolactin</bdi>.",
},
611: {
    "B": "الموجات فوق الصوتية على الدرقية تفيد لو كان الـ<bdi>cause</bdi> بالغدة نفسها، بس هنا نمط الهرمونات يوجه لمصدر نخامي.",
    "C": "فحص المبيض لا علاقة له ب<bdi>symptoms</bdi> الدرقية والـ<bdi>prolactin</bdi> هنا.",
    "D": "الماموغرام لا يوضح <bdi>cause</bdi> اضطراب محور الدرقية والـ<bdi>prolactin</bdi>.",
},
612: {
    "B": "فرط صوديوم عطشي (adipsic) نادر ولا يفسر بول مخفف بهذا الشكل مع تاريخ ورمي منتشر يدعم <bdi>cause</bdi> مركزي.",
    "C": "الشرب النفسي الزائد يعطي نقص صوديوم عادة، مو ارتفاعه.",
    "D": "الصورة السريرية والمخبرية تدعم <bdi>diagnosis</bdi> واضح (<bdi>diabetes</bdi> كاذب)، فخيار عدم وجود <bdi>diagnosis</bdi> غير صحيح.",
},
613: {
    "B": "الميثيمازول مضاد درقية ما يفيد لأن المشكلة تسرب هرمون مخزن مو زيادة إنتاج.",
    "C": "نفس الـ<bdi>cause</bdi>، البروبيلثيوراسيل مضاد درقية غير فعال بالتهاب تحت <bdi>acute</bdi>.",
    "D": "اليود المشع <bdi>treatment</bdi> لفرط نشاط حقيقي مستمر، غير مناسب لالتهاب عابر مؤلم.",
},
614: {
    "B": "تنقيص الجرعة خطأ لأن TSH <bdi>elevated</bdi> يعني الـ<bdi>patient</bdi> بحاجة لنفس الجرعة أو أكثر لا أقل.",
    "C": "نفس خطأ تنقيص الجرعة، مع فحص مبكر جدًا (48-72 ساعة) لا يعكس شي.",
    "D": "إيقاف الـ<bdi>treatment</bdi> يرجع الـ<bdi>patient</bdi> لقصور درقية واضح بدون <bdi>cause</bdi> لذلك.",
},
615: {
    "A": "خزعة الغدة تفيد ل<bdi>assessment</bdi> عقيدة مشبوهة بس مو الـ<bdi>step</bdi> الأولى ل<bdi>treatment</bdi> فرط النشاط العرضي الحالي.",
    "B": "اليود المشع ممنوع تمامًا خلال الحمل لأنه يضر الغدة الدرقية الجنينية.",
    "C": "الجراحة تحفظ لحالات فشل الـ<bdi>treatment</bdi> الدوائي أو خصوصية معينة، مو ك<bdi>step</bdi> أولى.",
},
})

EXPLANATIONS.update({
626: {
    "idea": "امرأة كبيرة بالسن اكتشف عندها ضغط <bdi>elevated</bdi> حديثًا مع نقص بوتاسيوم واضح وارتفاع بيكربونات (قلوية استقلابية)، وهذا نمط كلاسيكي لفرط الـ<bdi>aldosterone</bdi> الأولي.",
    "clues": [
        ("uses ibuprofen", "يستخدم مسكن مضاد التهاب، ممكن يسبب احتباس سوائل بس نمط الكهارل هنا مختلف"),
        ("Blood pressure 160/95 mmHg", "ضغط <bdi>elevated</bdi> جديد"),
        ("Potassium 2.9 (3.5-5.1)", "نقص بوتاسيوم واضح، دليل مهم على زيادة إفراز الـ<bdi>aldosterone</bdi>"),
        ("Bicarbonate 31 (21-28)", "ارتفاع بيكربونات (قلوية استقلابية)، يتوافق مع فرط الـ<bdi>aldosterone</bdi>"),
        ("Sodium 142 (134-146)", "صوديوم <bdi>normal</bdi> رغم فرط الـ<bdi>aldosterone</bdi> ب<bdi>cause</bdi> ظاهرة الإفلات (aldosterone escape)"),
    ],
    "why_correct": [
        "نمط نقص البوتاسيوم مع القلوية الاستقلابية والصوديوم الـ<bdi>normal</bdi> هو البصمة الكلاسيكية لفرط الـ<bdi>aldosterone</bdi> الأولي (<bdi>Conn's syndrome</bdi>).",
        "الصوديوم يبقى <bdi>normal</bdi> رغم زيادة الـ<bdi>aldosterone</bdi> ب<bdi>cause</bdi> ظاهرة الإفلات الكلوي (aldosterone escape) اللي تمنع احتباس صوديوم مفرط.",
        "أدوية الـNSAIDs مثل الإيبوبروفين تسبب ارتفاع ضغط مع ميل لفرط بوتاسيوم (ب<bdi>cause</bdi> تقليل تدفق الدم الكلوي)، عكس الصورة هنا تمامًا (نقص بوتاسيوم).",
    ],
    "when_changes": [
        "لو كان البوتاسيوم <bdi>elevated</bdi> بدل <bdi>low</bdi> مع استخدام مسكنات مضادة للالتهاب، يصير الـ<bdi>diagnosis</bdi> الأرجح ضغط ناتج عن الـNSAIDs.",
        "لو فيه نوبات ضغط <bdi>severe</bdi> متكررة مع صداع و<bdi>palpitations</bdi> وتعرق، يصير الفيوكروموسايتوما هو الـ<bdi>diagnosis</bdi> الأرجح بدل فرط الـ<bdi>aldosterone</bdi>.",
    ],
    "rule": "نقص بوتاسيوم مع قلوية استقلابية وصوديوم <bdi>normal</bdi> في <bdi>patient</bdi> بضغط <bdi>elevated</bdi> جديد يوجه لفرط الـ<bdi>aldosterone</bdi> الأولي.",
    "comparison": None,
    "guideline_note": None,
},
627: {
    "idea": "<bdi>patient</bdi> شاب عنده <bdi>palpitations</bdi> وتعرق وانزعاج بالرقبة مع ارتفاع كبير بمعدل الترسيب وفرط نشاط درقي واضح، صورة تدعم التهاب درقية تحت <bdi>acute</bdi> بدل <bdi>Graves' disease</bdi>.",
    "clues": [
        ("10 days of palpitations, sweating and neck<br>discomfort", "مدة قصيرة نسبيًا مع انزعاج بالرقبة يوجه لالتهاب أكثر من <bdi>Graves' disease</bdi> الـ<bdi>chronic</bdi>"),
        ("Thyroxine (T4 free) 76.5", "ارتفاع <bdi>severe</bdi> جدًا بT4"),
        ("Thyroid-Stimulating Hormone 0.15", "TSH <bdi>low</bdi>، فرط نشاط حقيقي"),
        ("ESR 73 (2-10)", "ارتفاع كبير جدًا بمعدل الترسيب، يدعم التهاب <bdi>acute</bdi> أكثر من <bdi>Graves' disease</bdi>"),
    ],
    "why_correct": [
        "الارتفاع الـ<bdi>severe</bdi> بمعدل الترسيب مع انزعاج بالرقبة ومدة قصيرة الـ<bdi>symptoms</bdi> يدعم التهاب درقية تحت <bdi>acute</bdi> (<bdi>subacute thyroiditis</bdi>) أكثر من <bdi>Graves' disease</bdi>.",
        "التهاب الدرقية تحت الـ<bdi>acute</bdi> ينتج عن تسرب هرمون مخزن من غدة ملتهبة، فيعطي فرط نشاط عابر مع ترسيب <bdi>elevated</bdi> جدًا يميزه عن <bdi>causes</bdi> فرط النشاط الأخرى.",
        "<bdi>Graves' disease</bdi> وهاشيموتو والدراق العقدي السام عادة ما يعطون ارتفاع بهذا الحجم بمعدل الترسيب بدون التهاب <bdi>acute</bdi> مرافق.",
    ],
    "when_changes": [
        "لو كانت الغدة متضخمة بشكل غير مؤلم مع أجسام مضادة إيجابية وترسيب <bdi>normal</bdi> تقريبًا، يصير الـ<bdi>diagnosis</bdi> <bdi>Graves' disease</bdi>.",
        "لو كانت هناك عقدة واحدة واضحة نشطة بالمسح، يصير الدراق سام عقدي هو الأرجح.",
    ],
    "rule": "فرط نشاط درقي مع ترسيب <bdi>elevated</bdi> جدًا وانزعاج بالرقبة يوجه لالتهاب درقية تحت <bdi>acute</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
628: {
    "idea": "رجل كبير بالسن عنده ألم ظهر وكسور انضغاطية بالفقرات مع T-score بمنطقة <bdi>osteoporosis</bdi> تقريبًا، ووجود الكسر الفعلي يثبت <bdi>diagnosis</bdi> <bdi>osteoporosis</bdi> بغض النظر عن دقة رقم الـT-score.",
    "clues": [
        ("mild dorsal kyphosis with mild tenderness", "تشوه وألم بالعمود يتوافق مع كسور انضغاطية"),
        ("T-Score (Bone mineral Spine L1-4) -1.9", "بمنطقة نقص كثافة العظم (osteopenia) حسب الرقم وحده"),
        ("T-Score (Bone mineral Total hip) -2.1", "نفس المنطقة تقريبًا بمعيار الرقم وحده"),
        ("Compression fractures at T8, L2 and L3", "وجود كسور انضغاطية فعلية، وهذا يغير الـ<bdi>diagnosis</bdi> ل<bdi>osteoporosis</bdi> عظام بغض النظر عن رقم T-score"),
    ],
    "why_correct": [
        "بحسب التعريف الطبي، وجود كسر <bdi>osteoporosis</bdi> (fragility fracture) مثل الكسر الانضغاطي هنا يكفي وحده ل<bdi>diagnosis</bdi> <bdi>osteoporosis</bdi> (<bdi>osteoporosis</bdi>)، حتى لو كان الـT-score بمنطقة osteopenia فقط.",
        "الكالسيوم والفوسفات طبيعيين تقريبًا هنا، وهذا يبعد <bdi>causes</bdi> أخرى زي لين العظام (<bdi>osteomalacia</bdi>) اللي عادة تعطي كالسيوم وفوسفات منخفضين مع ألكالين فوسفاتيز <bdi>elevated</bdi> بشكل أوضح.",
        "<bdi>disease</bdi> باجيت يعطي صورة مختلفة بالأشعة (تضخم وتشوه عظمي موضعي) مو كسور انضغاطية متعددة بهذا النمط.",
    ],
    "when_changes": [
        "لو ما فيه أي كسر فعلي وT-score بمنطقة -1.9، الـ<bdi>diagnosis</bdi> الصحيح يكون osteopenia فقط مو osteoporosis.",
        "لو كان الكالسيوم والفوسفات منخفضين بوضوح مع ألكالين فوسفاتيز <bdi>elevated</bdi> جدًا، يصير osteomalacia هو الـ<bdi>diagnosis</bdi> الأرجح.",
    ],
    "rule": "وجود كسر <bdi>osteoporosis</bdi> فعلي يشخص <bdi>osteoporosis</bdi> مباشرة حتى لو كان T-score بمنطقة osteopenia فقط.",
    "comparison": None,
    "guideline_note": None,
},
629: {
    "idea": "امرأة قصور درقيتها كانت مضبوطة، زادوا جرعتها قبل 3 أشهر، لكن الآن TSH طلع <bdi>elevated</bdi> بشكل غير متوقع رغم زيادة الجرعة، والفحص الجسدي <bdi>normal</bdi>، فالسؤال يبي التفسير الأرجح.",
    "clues": [
        ("dose was increased 3 months ago", "زيادة جرعة كافية بالوقت لتظهر تأثيرها لو انتظمت بأخذها"),
        ("Thyroxine (T4 free) 12.4 (8.5-15.2)", "T4 <bdi>normal</bdi>، يعني تلقت الدواء مؤخرًا بشكل كافٍ"),
        ("Thyroid-Stimulating Hormone 17.2", "TSH <bdi>elevated</bdi> بشكل واضح رغم T4 <bdi>normal</bdi>، تناقض يوحي بعدم انتظام بالأخذ"),
    ],
    "why_correct": [
        "التناقض بين T4 <bdi>normal</bdi> وTSH <bdi>elevated</bdi> جدًا يوحي إن الـ<bdi>patient</bdi> تاخذ الدواء بشكل متقطع (تاخذ جرعات مركزة قبل الفحص بس تهمل باقي الأيام).",
        "الـT4 يعكس الجرعات الأخيرة القريبة من الفحص، بينما TSH يعكس المستوى العام على مدى أسابيع، فهذا التناقض يدعم <bdi>poor medication adherence</bdi>.",
        "لو كانت الجرعة صغيرة فعلًا لكل الفترة، كان المفروض يكون T4 <bdi>low</bdi> أيضًا مو <bdi>normal</bdi>.",
    ],
    "when_changes": [
        "لو كان T4 <bdi>low</bdi> مع TSH <bdi>elevated</bdi> بشكل متناسق، يصير التفسير الأرجح فعلًا جرعة غير كافية.",
        "لو كانت الـ<bdi>patient</bdi> تاخذ الدواء من مصدر غير موثوق أو دواء مقلد، يصير هذا <bdi>cause</bdi> محتمل إضافي لضعف الاستجابة.",
    ],
    "rule": "تناقض T4 <bdi>normal</bdi> مع TSH <bdi>elevated</bdi> جدًا بعد زيادة جرعة الثيروكسين يوجه لسوء الالتزام بأخذ الدواء بانتظام.",
    "comparison": None,
    "guideline_note": None,
},
630: {
    "idea": "رجل يعالج اضطراب دهون الدم واحمر وجهه بشدة بعد أول جرعة، وتحسن تمامًا بإعطاء جرعة كاملة من الـ<bdi>aspirin</bdi> قبل الدواء، وهذا تفاعل جانبي كلاسيكي لدواء معين من أدوية الدهون.",
    "clues": [
        ("intense face flushing after taking the tablet", "احمرار وجه <bdi>severe</bdi>، <bdi>symptom</bdi> جانبي مميز لدواء واحد من أدوية الدهون"),
        ("full dose of aspirin 3 times daily instead of a low<br>dose once daily", "الـ<bdi>aspirin</bdi> بجرعة كاملة يمنع الاحمرار، يدعم آلية بروستاغلاندين"),
        ("Cholesterol (LDL) 5.30", "اضطراب دهون واضح يحتاج <bdi>treatment</bdi> دوائي"),
    ],
    "why_correct": [
        "دواء <bdi>Niacin</bdi> (النياسين) يسبب احمرار وجه <bdi>severe</bdi> (flushing) عبر تحرير بروستاغلاندين D2 بالجلد.",
        "الـ<bdi>aspirin</bdi> يمنع إنتاج البروستاغلاندين، فإعطاء جرعة كاملة منه قبل النياسين يمنع أو يقلل الاحمرار بشكل فعال، وهذا يفسر تحسن الـ<bdi>patient</bdi> تمامًا بعدها.",
        "باقي أدوية الدهون (الـ<bdi>statin</bdi>، الكوليستيرامين، الكلوفايبرات) ما تسبب احمرار وجه بهذه الطريقة النموذجية المرتبطة بالبروستاغلاندين.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>symptom</bdi> الجانبي ألم عضلي وارتفاع إنزيمات الكبد بدل الاحمرار، يصير الـ<bdi>statin</bdi> هو المشتبه به بدل النياسين.",
        "لو ما تحسن الاحمرار بالـ<bdi>aspirin</bdi> إطلاقًا، يصير التفكير ب<bdi>cause</bdi> ثاني غير النياسين للاحمرار.",
    ],
    "rule": "احمرار الوجه بعد بدء دواء لدهون الدم ويتحسن بالـ<bdi>aspirin</bdi> يشخص النياسين ك<bdi>cause</bdi>، لأن آليته عبر بروستاغلاندين D2.",
    "comparison": {
        "headers": ["الدواء", "الأثر الجانبي المميز"],
        "rows": [
            ["<bdi>Niacin</bdi>", "احمرار وجه (flushing) يتحسن بالـ<bdi>aspirin</bdi>"],
            ["<bdi>Statins</bdi>", "ألم عضلي وارتفاع إنزيمات الكبد"],
            ["<bdi>Cholestyramine</bdi>", "انتفاخ وإمساك"],
        ],
    },
    "guideline_note": None,
},
631: {
    "idea": "امرأة عندها عقم وثر لبني من الثديين مع <bdi>prolactin</bdi> <bdi>elevated</bdi> وورم نخامي صغير (ميكروأدينوما) مؤكد بالرنين المغناطيسي، والسؤال يبي أفضل <bdi>treatment</bdi>.",
    "clues": [
        ("infertility for 3 years", "أثر فرط الـ<bdi>prolactin</bdi> على الخصوبة"),
        ("excessive breast milk production", "ثر لبني، <bdi>sign</bdi> مباشرة لفرط الـ<bdi>prolactin</bdi>"),
        ("Prolactin 1452 (&lt;870)", "ارتفاع واضح بالـ<bdi>prolactin</bdi>"),
        ("Well-defined pituitary mass about 0.7 cm", "ورم صغير (ميكروأدينوما، أقل من 1 سم)"),
    ],
    "why_correct": [
        "ناهضات الـ<bdi>dopamine</bdi> مثل <bdi>Cabergoline</bdi> هي خط الـ<bdi>treatment</bdi> الأول لأي ورم مفرز لل<bdi>prolactin</bdi> (بروﻻكتينوما)، سواء صغير أو كبير.",
        "هذا الـ<bdi>treatment</bdi> فعال جدًا بتقليص حجم الورم وخفض الـ<bdi>prolactin</bdi> واستعادة الخصوبة والدورة الـ<bdi>normal</bdi> غالبًا.",
        "الجراحة والـ<bdi>treatment</bdi> الإشعاعي يحفظان للحالات اللي ما تستجيب لل<bdi>treatment</bdi> الدوائي، والمراقبة وحدها غير كافية مع وجود ورم مثبت و<bdi>symptoms</bdi> فعلية.",
    ],
    "when_changes": [
        "لو فشل الـ<bdi>treatment</bdi> الدوائي بالسيطرة على الورم أو الـ<bdi>symptoms</bdi>، يصير التفكير بالجراحة عبر الأنف والوتد.",
        "لو كان الورم كبير جدًا ويضغط على أعصاب حيوية بشكل عاجل، ممكن تحتاج الجراحة ك<bdi>step</bdi> أسرع.",
    ],
    "rule": "ناهضات الـ<bdi>dopamine</bdi> هي الـ<bdi>treatment</bdi> الأول لأي بروﻻكتينوما بغض النظر عن حجمها الأولي.",
    "comparison": None,
    "guideline_note": None,
},
632: {
    "idea": "رجل كبير بالسن اكتشف ضغطه <bdi>elevated</bdi> بشكل <bdi>mild</bdi> بعدة قراءات بدون أي دليل على ضرر بالأعضاء المستهدفة (قلب سليم، تخطيط <bdi>normal</bdi>، بول <bdi>normal</bdi>)، والسؤال يبي أفضل <bdi>step</bdi> أولى قبل الأدوية.",
    "clues": [
        ("blood pressure to be<br>around 150/84 mmHg on several occasions", "ضغط <bdi>elevated</bdi> مؤكد بعدة قراءات بس بدرجة <bdi>mild</bdi>"),
        ("urine dipstick demonstrates no blood or protein", "لا دليل على تأثر كلوي"),
        ("no evidence<br>of left ventricular hypertrophy", "لا دليل على تضخم قلب من الضغط"),
        ("BMI 31 kg/m2", "سمنة، هدف قابل للتعديل بنمط الحياة"),
    ],
    "why_correct": [
        "الضغط هنا <bdi>elevated</bdi> بدرجة <bdi>mild</bdi> (مرحلة أولى) بدون أي دليل على تضرر أعضاء مستهدفة، وهذا يسمح بتجربة تعديل نمط الحياة أولًا قبل الأدوية.",
        "تعديلات نمط الحياة وإنقاص الوزن (<bdi>lifestyle modifications and weight loss</bdi>) فعالة بتخفيض الضغط بهذه المرحلة المبكرة وتتماشى مع سمنته الموجودة (BMI 31).",
        "بدء دواء خافض ضغط مباشرة (<bdi>amlodipine</bdi> أو حاصرات بيتا) مبكر جدًا قبل إعطاء فرصة كافية لتعديل نمط الحياة ب<bdi>patient</bdi> بدون ضرر أعضاء مستهدف.",
    ],
    "when_changes": [
        "لو كان فيه دليل على ضرر بالأعضاء المستهدفة (تضخم قلب، بروتين بالبول) أو ضغط أعلى بكثير، يصير بدء الدواء مباشرة هو الأنسب.",
        "لو ما تحسن الضغط بعد فترة كافية من تعديل نمط الحياة، يصير بدء دواء خافض للضغط هو الـ<bdi>step</bdi> التالية.",
    ],
    "rule": "ارتفاع الضغط الـ<bdi>mild</bdi> بدون ضرر أعضاء مستهدفة يبدأ علاجه بتعديل نمط الحياة أولًا قبل الأدوية.",
    "comparison": None,
    "guideline_note": None,
},
633: {
    "idea": "رجل عنده <bdi>diabetes</bdi> وضغط <bdi>elevated</bdi> حديث الـ<bdi>diagnosis</bdi> وبروتين ظاهر بتحليل البول، والسؤال يبي أفضل دواء خافض للضغط يناسب حالته الكلوية.",
    "clues": [
        ("newly diagnosed<br>hypertension and diabetes mellitus", "<bdi>diagnosis</bdi> جديد للضغط و<bdi>diabetes</bdi> معًا"),
        ("Protein Present", "بروتين ظاهر بالبول، دليل على تأثر كلوي مبكر يحتاج حماية إضافية"),
    ],
    "why_correct": [
        "وجود بروتين بالبول عند <bdi>patient</bdi> <bdi>diabetes</bdi> يدل على تأثر كلوي مبكر، وهذا يجعل مثبطات الإنزيم المحول للأنجيوتنسين (<bdi>Lisinopril</bdi>) الخيار الأفضل لتقليل البروتينية وحماية الكلى بجانب خفض الضغط.",
        "هذي الأدوية تقلل الضغط داخل الكبيبات الكلوية بشكل مباشر، وهذا مفيد جدًا بوجود بروتينية سكرية.",
        "باقي الأدوية (<bdi>atenolol</bdi>، <bdi>amlodipine</bdi>، هيدروكلوروثيازيد) تخفض الضغط بس بدون نفس الفايدة الكلوية النوعية بوجود بروتينية سكرية.",
    ],
    "when_changes": [
        "لو ما فيه بروتين بالبول ولا دليل تأثر كلوي، تصير باقي أدوية الضغط خيارات مقبولة بنفس القوة تقريبًا.",
        "لو الـ<bdi>patient</bdi> عنده حساسية أو سعال من مثبطات الإنزيم المحول، يصير حاصر مستقبلات الأنجيوتنسين البديل المناسب بدلًا عنه.",
    ],
    "rule": "ب<bdi>patient</bdi> <bdi>diabetes</bdi> المصاحب لبروتينية بالبول، مثبطات الإنزيم المحول للأنجيوتنسين هي الخيار الأول لخفض الضغط وحماية الكلى.",
    "comparison": None,
    "guideline_note": None,
},
634: {
    "idea": "شابة تشخصت حديثًا ب<bdi>diabetes</bdi> نوع أول بعد حماض كيتوني، وأصبحت مستقرة وجاهزة للخروج، والسؤال يبي أفضل نظام <bdi>insulin</bdi> طويل المدى لل<bdi>follow-up</bdi> بالمنزل.",
    "clues": [
        ("diagnosed of type 1 diabetes mellitus", "<bdi>diabetes</bdi> نوع أول يحتاج <bdi>insulin</bdi> دائم من الأساس"),
        ("blood sugars are now stable and she is ready for discharge", "جاهزة لنظام <bdi>insulin</bdi> منزلي طويل المدى"),
    ],
    "why_correct": [
        "أفضل نظام ل<bdi>diabetes</bdi> النوع الأول هو نظام القاعدة والجرعات (<bdi>basal-bolus</bdi>)، يعطي تحكم أقرب لل<bdi>normal</bdi> بمستوى السكر طول اليوم.",
        "الـ<bdi>insulin</bdi> طويل المفعول مرة يوميًا مثل <bdi>glargine</bdi> يوفر التغطية القاعدية المستمرة (بدون ذروة واضحة)، ويحتاج معه <bdi>insulin</bdi> سريع قبل كل وجبة.",
        "أنظمة NPH مرتين يوميًا أو mixtard مرة واحدة أقل مرونة وأصعب بالتحكم الدقيق مقارنة بنظام القاعدة والجرعات الحديث.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> تستخدم مضخة <bdi>insulin</bdi>، يصير نظام التسريب المستمر تحت الجلد بديل معقول عن الحقن المتعددة.",
        "لو كانت الـ<bdi>patient</bdi> كبيرة بالسن وتحتاج نظام أبسط بأقل عدد حقن، ممكن يفكر بنظام أقل صرامة رغم إنه أقل دقة.",
    ],
    "rule": "نظام القاعدة والجرعات مع <bdi>insulin</bdi> قاعدي طويل مرة يوميًا هو الأنسب لمرضى <bdi>diabetes</bdi> النوع الأول بعد الاستقرار.",
    "comparison": None,
    "guideline_note": None,
},
635: {
    "idea": "امرأة كبيرة بالسن عندها <bdi>diabetes</bdi> نوع ثاني، ضبطها الحالي جيد نسبيًا على الـ<bdi>metformin</bdi>، وكلاها ووظائفها <bdi>normal</bdi>، فالسؤال يبي القرار الصحيح بالـ<bdi>treatment</bdi>.",
    "clues": [
        ("currently taking metformin 1g bid", "جرعة علاجية قياسية كاملة"),
        ("physical examination is unremarkable", "لا <bdi>complications</bdi> ظاهرة حاليًا"),
        ("Creatinine 80 (44-115)", "وظيفة كلى <bdi>normal</bdi>، لا مانع من الاستمرار على الـ<bdi>metformin</bdi>"),
        ("НbА1C 6.9", "ضبط جيد نسبيًا لل<bdi>diabetes</bdi>"),
    ],
    "why_correct": [
        "الـ<bdi>patient</bdi> ضبطها الحالي مقبول (HbA1c قريب من الهدف المعتاد لكبار السن) وهي على جرعة كاملة من الـ<bdi>metformin</bdi> بدون <bdi>complications</bdi>.",
        "لا داعي حاليًا لإضافة دواء ثاني أو تعديل الجرعة طالما الضبط مقبول والوظائف <bdi>normal</bdi>، فالقرار الصحيح هو عدم <bdi>procedure</bdi> أي تغيير.",
        "إضافة أدوية إضافية بدون حاجة فعلية تزيد <bdi>risk</bdi> الـ<bdi>symptoms</bdi> الجانبية (مثل هبوط السكر من glimepiride) بدون فايدة إضافية واضحة حاليًا.",
    ],
    "when_changes": [
        "لو كان HbA1c فوق الهدف المناسب لعمرها وحالتها الصحية، يصير إضافة دواء ثاني منطقيًا.",
        "لو ساءت وظائف كلاها بشكل كبير، يحتاج تعديل جرعة الـ<bdi>metformin</bdi> أو إيقافه حسب درجة التأثر.",
    ],
    "rule": "إذا كان ضبط <bdi>diabetes</bdi> مناسبًا لعمر الـ<bdi>patient</bdi> وحالته وبدون <bdi>complications</bdi>، لا داعي لتغيير الـ<bdi>treatment</bdi> فقط لأجل التغيير.",
    "comparison": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
616: {
    "A": "تأخير الفحص 6 أشهر بدون <bdi>assessment</bdi> نسيجي غير مناسب لعقيدة صلبة بهذا الحجم.",
    "B": "المسح باليود يفيد أكثر لو كان TSH <bdi>low</bdi> (عقيدة ساخنة)، مو ك<bdi>step</bdi> أولى هنا.",
    "D": "الأشعة المقطعية على الرقبة ما تعطي <bdi>diagnosis</bdi> نسيجي، وغير ضرورية ك<bdi>step</bdi> أولى.",
},
617: {
    "A": "عدم تغيير الـ<bdi>treatment</bdi> غير مناسب لأن ضغطه <bdi>elevated</bdi> بشكل مؤكد بعدة قراءات ويحتاج <bdi>treatment</bdi>.",
    "C": "حاصرات البيتا ليست الخيار الأول ب<bdi>patient</bdi> <bdi>diabetes</bdi> بدون مؤشر قلبي محدد يستدعيها.",
    "D": "السلفونيل يوريا دواء لضبط السكر، والسكر هنا مضبوط أصلًا، فلا داعي له.",
},
618: {
    "A": "الـ<bdi>dopamine</bdi> لرفع الضغط يستخدم لو ما استجاب الضغط للسوائل الكافية، مو ك<bdi>step</bdi> أولى قبل السوائل.",
    "B": "إضافة بوتاسيوم للسوائل الآن خطأ لأن بوتاسيومه <bdi>elevated</bdi> أصلًا (6).",
    "C": "بدء الـ<bdi>insulin</bdi> قبل السوائل ب<bdi>patient</bdi> بصدمة قد يزيد الهبوط بالضغط ويسبب هبوط بوتاسيوم مفاجئ خطير.",
},
619: {
    "A": "السكر العشوائي فحص أقل دقة ولا يحسم التناقض بين الفحصين الحاليين.",
    "B": "تكرار HbA1c بعد 6 أسابيع فقط لا يضيف معلومة حاسمة لحل التناقض الحالي بنفس قوة اختبار تحمل السكر.",
    "C": "الانتظار 3 أشهر لإعادة السكر الصائم يؤخر الـ<bdi>diagnosis</bdi> بدون داعٍ بينما فيه فحص أدق متاح الآن.",
},
620: {
    "A": "ما قبل <bdi>diabetes</bdi> لا يتوافق مع فحصين واقعين ضمن معيار <bdi>diagnosis</bdi> <bdi>diabetes</bdi> الفعلي.",
    "C": "ضعف تحمل السكر يشخص بفحص تحمل السكر الفموي تحديدًا، مو بهذي الفحوصات.",
    "D": "<bdi>diabetes</bdi> الشباب الناضج (MODY) <bdi>case</bdi> وراثية نادرة، لا دليل عليها هنا من التاريخ المعطى.",
},
621: {
    "A": "الكرياتينين وحده لا يكشف الضرر الكلوي المبكر الناتج عن <bdi>diabetes</bdi> بنفس حساسية نسبة الألبومين للكرياتينين.",
    "B": "الميكروالبومين وحده بدون نسبته للكرياتينين أقل دقة ويتأثر بتركيز البول.",
    "D": "معدل الترشيح الكبيبي المقدر يقيّم الوظيفة العامة بس مو الفحص المخصص لكشف <bdi>nephropathy</bdi> <bdi>diabetes</bdi> المبكر.",
},
622: {
    "A": "هدف أقل من 5% صارم جدًا وغير واقعي وقد يسبب هبوط سكر متكرر.",
    "B": "هدف أقل من 5.5% أيضًا صارم أكثر من اللازم للأغلبية.",
    "C": "هدف أقل من 6% أقرب من الـ<bdi>normal</bdi> وغير الهدف المعتمد عمومًا لأغلب المرضى.",
},
623: {
    "A": "الدم بالبول يوجه أكثر ل<bdi>causes</bdi> نزفية أو التهابية كبيبية غير سكرية نموذجية.",
    "C": "القوالب الهيالينية غير نوعية وتظهر حتى بأشخاص أصحاء.",
    "D": "القوالب الخلوية الحمراء تدل على التهاب كبيبي نشط أكثر من كونها <bdi>sign</bdi> نموذجية ل<bdi>nephropathy</bdi> <bdi>diabetes</bdi> الـ<bdi>chronic</bdi>.",
},
624: {
    "A": "الـ<bdi>insulin</bdi> <bdi>treatment</bdi> لل<bdi>diabetes</bdi> الفعلي المتقدم، مبالغ فيه لمرحلة ما قبل <bdi>diabetes</bdi> الحالية.",
    "B": "الأكاربوز أقل فعالية وأقل استخدامًا كخط أول وقائي مقارنة بالـ<bdi>metformin</bdi>.",
    "C": "الغليبورايد دواء ل<bdi>treatment</bdi> <bdi>diabetes</bdi> الفعلي وله <bdi>risk</bdi> هبوط سكر، غير مناسب للوقاية هنا.",
},
625: {
    "B": "زيادة الرياضة أكثر غير واقعية بعد التزام كامل ببرنامج مكثف أصلًا وفشل الوصول ل<bdi>result</bdi>.",
    "C": "تقليل السعرات أكثر من حمية <bdi>low</bdi> السعرات أصلًا قد يكون غير آمن وغير فعال بهذا المستوى من السمنة.",
    "D": "الأدوية المخفضة للوزن أقل فعالية من الجراحة بهذا المستوى من السمنة الـ<bdi>severe</bdi> مع <bdi>disease</bdi> مرافق.",
},
626: {
    "A": "الضغط الأساسي (essential) لا يفسر نقص البوتاسيوم والقلوية الاستقلابية الواضحين هنا.",
    "B": "الفيوكروموسايتوما تعطي نوبات ضغط <bdi>severe</bdi> مع <bdi>palpitations</bdi> وتعرق، مو نمط الكهارل الـ<bdi>chronic</bdi> هنا.",
    "D": "ضغط الـNSAIDs يترافق مع ميل لفرط بوتاسيوم لا نقصه.",
},
627: {
    "A": "<bdi>Graves' disease</bdi> عادة يعطي غدة غير مؤلمة مع أجسام مضادة إيجابية، وترسيب أقل ارتفاعًا من هذا الحد.",
    "C": "هاشيموتو يسبب قصور درقية غالبًا وليس فرط نشاط <bdi>acute</bdi> بهذا الترسيب الـ<bdi>elevated</bdi>.",
    "D": "الدراق السام متعدد العقيدات عادة عند كبار السن مع عقيدات واضحة، وما يعطي هذا الترسيب الـ<bdi>elevated</bdi> جدًا.",
},
628: {
    "A": "<bdi>disease</bdi> باجيت يعطي صورة أشعة مختلفة (تضخم وتشوه عظمي موضعي مميز) وليس كسور انضغاطية متعددة بهذا النمط.",
    "B": "لين العظام يترافق عادة بكالسيوم وفوسفات منخفضين بوضوح، وهذا غير مطابق تمامًا هنا.",
    "D": "نقص كثافة العظم وحده لا يفسر وجود كسور فعلية بالفقرات، والـ<bdi>diagnosis</bdi> الأدق مع الكسر هو <bdi>osteoporosis</bdi>.",
},
629: {
    "A": "لو كانت الجرعة صغيرة فعلًا طول الوقت، كان يفترض يكون T4 <bdi>low</bdi> أيضًا مو <bdi>normal</bdi>.",
    "B": "الغدة خارج مكانها الـ<bdi>normal</bdi> <bdi>case</bdi> نادرة جدًا ولا يوجد دليل عليها هنا.",
    "D": "<bdi>hypothyroidism</bdi> الثانوي يعطي TSH <bdi>low</bdi> أو غير مناسب مع T4 <bdi>low</bdi>، عكس الصورة هنا تمامًا.",
},
630: {
    "B": "الكلوفايبرات لا يسبب احمرار وجه بهذه الآلية النموذجية المرتبطة بالبروستاغلاندين.",
    "C": "الـ<bdi>statin</bdi> يسبب ألم عضلي وارتفاع إنزيمات كبدية غالبًا، لا احمرار وجه نموذجي بهذا الشكل.",
    "D": "الكوليستيرامين يسبب <bdi>symptoms</bdi> هضمية (انتفاخ وإمساك) وليس احمرار وجه.",
},
631: {
    "A": "الجراحة تحفظ لحالات فشل الـ<bdi>treatment</bdi> الدوائي، وهنا الورم صغير ومتوقع استجابته جيدة للدواء أولًا.",
    "C": "المراقبة وحدها غير كافية مع وجود <bdi>symptoms</bdi> فعلية (عقم وثر لبني) وورم مثبت يحتاج <bdi>treatment</bdi> فعال.",
    "D": "الـ<bdi>treatment</bdi> الإشعاعي بطيء المفعول ويحفظ لحالات نادرة لا تستجيب لل<bdi>treatment</bdi> الدوائي ولا يمكن جراحتها.",
},
632: {
    "A": "الانتظار 4 أشهر لإعادة القياس طويل جدًا بدون أي تدخل رغم تأكد الضغط الـ<bdi>elevated</bdi> بعدة قراءات سابقة.",
    "C": "بدء الـ<bdi>amlodipine</bdi> مباشرة يتخطى فرصة تجربة تعديل نمط الحياة أولًا ب<bdi>patient</bdi> بدون ضرر أعضاء مستهدفة.",
    "D": "حاصرات البيتا ليست الخط الأول لضغط بدون مؤشر قلبي واضح يستدعيها.",
},
633: {
    "B": "<bdi>atenolol</bdi> لا يعطي نفس الفايدة الكلوية النوعية بوجود بروتينية سكرية.",
    "C": "<bdi>amlodipine</bdi> خافض ضغط فعال بس بدون الفايدة الكلوية الخاصة لمثبطات الإنزيم المحول هنا.",
    "D": "هيدروكلوروثيازيد خيار مقبول عمومًا بس أقل ملاءمة من ACE inhibitor بوجود بروتينية سكرية واضحة.",
},
634: {
    "A": "NPH مرتين يوميًا أقل مرونة ودقة من نظام القاعدة والجرعات الحديث.",
    "B": "Mixtard مرة واحدة يوميًا غير كافٍ للتحكم الدقيق ب<bdi>diabetes</bdi> نوع أول.",
    "D": "غياب الـ<bdi>insulin</bdi> طويل المفعول (القاعدي) يترك فجوات بتغطية السكر بين الوجبات وأثناء الليل.",
},
635: {
    "A": "زيادة جرعة الـ<bdi>metformin</bdi> غير ضرورية لأن الضبط الحالي مقبول أصلًا.",
    "B": "إضافة غليميبرايد تزيد <bdi>risk</bdi> هبوط السكر بدون حاجة فعلية حاليًا.",
    "C": "إضافة سيتاغليبتين دواء إضافي غير ضروري طالما الضبط الحالي مناسب لعمرها وحالتها.",
},
})

HIGHLIGHT_TERMS.update({
596: ["atrial fibrillation", "warfarin", "subdural hematoma that requires evacuation", "INR 3.9"],
597: ["day 17 of", "he has fever", "no focus of infection", "WBC 0.6"],
598: ["fever, night sweats and weight loss", "lost 12 Kg in the last 3 month", "cervical lymph nodes, largest 3 cm", "inguinal lymphadenopathy", "spleen is palpable 3 fingers"],
599: ["count was 73,000", "fatigue and dry mouth", "Potassium 5.5", "Uric acid 620"],
600: ["decreased proprioception in the lower", "positive planter reflexes", "absent ankle and knee's reflexes", "anemia"],
601: ["poor performance status, dementia", "adenocarcinoma of an unknown primary site", "liver lesions, and pulmonary nodules"],
602: ["prognosis was poor", "unlikely to survive for more than a", "Calcium ionised 3.2"],
603: ["3-day history of seizures", "Sodium 112", "Osmolality 860"],
604: ["decreased libido and weak erections", "Prolactin 2100"],
605: ["central weight gain, change in", "pigmentation of the skin", "buffalo hump, edema, proximal muscle wasting"],
606: ["increased urine output, especially during the", "response to desmopressin administration"],
607: ["irritability, heat intolerance", "Thyroid-Stimulating Hormone 0.1", "Thyroxine (T4 free) 30.4"],
608: ["intolerance, and weight gain", "TSH 19.9"],
609: ["discomfort in both breasts with milk production", "Prolactin 2350"],
610: ["menstrual cycle has stopped for the last 9 months", "pregnancy test is", "Prolactin 2450"],
611: ["frequent bowel movement, increased appetite and weight loss", "small diffuse goiter", "Thyroid-Stimulating Hormone 8.7"],
612: ["excessive urination and thirst", "Sodium 150", "Osmolality 110"],
613: ["painful neck swelling for the last week", "diffuse tender anterior neck", "ESR 58"],
614: ["for treatment of hypothyroidism 2 weeks before", "TSH 7.5"],
615: ["thyroid gland is nodular, diffusely enlarged", "Antithyroid Antibody negative"],
616: ["2 cm solid thyroid nodule"],
617: ["HbA1c level of 5.8%", "no signs of retinopathy", "Blood pressure 149/90 mmHg"],
618: ["Blood pressure 80/50 mmHg", "Heart rate 140 /min", "Potassium 6", "Bicarbonate 5"],
619: ["family history of type 2 diabetes undergoes screening", "Glucose, fasting 7.4", "Hemoglobin A1C 6.3"],
620: ["history of polyuria", "Glucose, fasting 7.0", "Hemoglobin A1C 7.1"],
621: ["metformin 500 mg TDS", "Creatinine 125"],
622: ["type 2 diabetes for the past 20 years", "HbA1C 7.8"],
623: ["diabetic nephropathy in type 2"],
624: ["gestational diabetes during her second pregnancy", "strong family history of type 2 diabetes", "Glucose, fasting 6.5"],
625: ["unable to lose weight despite being on an intensive lifestyle", "Weight 125 kg", "HbA1C 8.1"],
626: ["for which she uses", "Potassium 2.9", "Bicarbonate 31", "Sodium 142"],
627: ["10 days of palpitations, sweating", "Thyroxine (T4 free) 76.5", "ESR 73"],
628: ["mild dorsal kyphosis with mild tenderness", "Compression fractures at T8, L2 and L3"],
629: ["dose was increased 3 months ago", "Thyroxine (T4 free) 12.4", "Thyroid-Stimulating Hormone 17.2"],
630: ["intense face flushing after taking the tablet", "full dose of aspirin 3 times daily", "Cholesterol (LDL) 5.30"],
631: ["infertility for 3 years", "excessive breast milk production", "Prolactin 1452", "Well-defined pituitary mass about 0.7 cm"],
632: ["around 150/84 mmHg on several occasions", "urine dipstick demonstrates no blood or protein", "of left ventricular hypertrophy"],
633: ["hypertension and diabetes mellitus", "Protein Present"],
634: ["diagnosed of type 1 diabetes mellitus after presenting with diabetic", "ready for discharge"],
635: ["currently taking metformin 1g", "Creatinine 80"],
})

EXPLANATIONS.update({
636: {
    "idea": "امرأة توقف طمثها بعد إيقاف حبوب منع الحمل مع صداع وعيب بالمجال البصري وقصور بمحاور نخامية متعددة (درقية، تناسلية، كظرية)، وتصوير يظهر ورم نخامي كبير يضغط على التصالب البصري، فالسؤال يبي الـ<bdi>treatment</bdi> الحاسم.",
    "clues": [
        ("bilateral defects in the upper outer quadrants", "عيب بصري يدل على ضغط بالجزء السفلي من التصالب البصري"),
        ("Thyroid-Stimulating Hormone 0.1", "<bdi>low</bdi> مع T4 <bdi>low</bdi>، قصور درقي ثانوي (نخامي)"),
        ("Follicle-stimulating hormone 0.2", "<bdi>low</bdi> جدًا، قصور تناسلي ثانوي"),
        ("Cortisol 8 a.m. 30", "<bdi>low</bdi> جدًا، قصور كظري ثانوي محتمل"),
        ("4 cm pituitary mass compressing optic chiasm", "ورم نخامي كبير يضغط على التصالب، يسبب كل هذا القصور المتعدد"),
    ],
    "why_correct": [
        "ورم نخامي كبير (4 سم) يضغط على التصالب البصري ويسبب قصور بعدة محاور هرمونية بنفس الوقت (قصور مشترك)، وهذا يحتاج إزالة الضغط جراحيًا.",
        "الجراحة عبر الأنف والوتد (<bdi>trans-sphenoidal surgery</bdi>) هي الـ<bdi>treatment</bdi> الحاسم اللي يزيل الضغط على العصب البصري ويحسن الرؤية ويقلل حجم الورم مباشرة.",
        "الـ<bdi>prolactin</bdi> الـ<bdi>elevated</bdi> هنا بسيط نسبيًا (950) ويفسر أكثر بتأثير الضغط على ساق الغدة (stalk effect) مو بروﻻكتينوما حقيقية تستجيب للدواء وحده، فالـ<bdi>treatment</bdi> الدوائي وحده غير كافٍ بهذا الحجم من الورم.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>prolactin</bdi> <bdi>elevated</bdi> جدًا جدًا (آلاف) بما يتناسب مع حجم الورم، يصير ناهض الـ<bdi>dopamine</bdi> خيار علاجي أولي معقول قبل الجراحة.",
        "لو الورم صغير بدون ضغط على التصالب أو <bdi>symptoms</bdi> بصرية، الـ<bdi>treatment</bdi> التحفظي أو الدوائي يكون كافٍ.",
    ],
    "rule": "ورم نخامي كبير يضغط على التصالب البصري مع <bdi>symptoms</bdi> بصرية وقصور هرموني متعدد يحتاج إزالة جراحية عبر الأنف والوتد.",
    "comparison": None,
    "guideline_note": None,
},
637: {
    "idea": "امرأة تشخصت حديثًا ب<bdi>disease</bdi> أديسون وبدأت على هيدروكورتيزون وفلودروكورتيزون، وتسأل عن كيفية تعديل جرعات الستيرويد أثناء عملها بنظام الورديات الليلية.",
    "clues": [
        ("Addison's disease", "قصور كظري أولي يحتاج تعويض ستيرويد دائم بجرعات مقسمة تحاكي الإيقاع اليومي الـ<bdi>normal</bdi>"),
        ("she informs the medical team that she sometimes does shift-work", "تغيّر نمط النوم يعقد جدولة الجرعات المعتادة حسب الساعة"),
    ],
    "why_correct": [
        "هدف تعويض الستيرويد هو تقليد الإيقاع اليومي الـ<bdi>normal</bdi> للكورتيزول (أعلى عند الاستيقاظ ويقل تدريجيًا خلال اليوم)، مو الالتزام بساعات ثابتة بالساعة الحقيقية.",
        "بيوم الوردية الليلية، الاستيقاظ يصير بوقت مختلف، فلازم تاخذ أول جرعة عند استيقاظها هي (بغض النظر عن الساعة الفعلية)، ثم باقي الجرعات بعد 3 و6 ساعات من ذلك.",
        "هذا يحافظ على نفس نمط التوزيع الفسيولوجي للكورتيزول بغض النظر عن توقيت نومها واستيقاظها الفعلي.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عندها <bdi>disease</bdi> <bdi>acute</bdi> أو تقيؤ أو جراحة، تحتاج جرعات إضافية <bdi>complication</bdi> (sick day rules) بغض النظر عن الجدول المعتاد.",
        "لو رجعت لنظام نوم ليلي <bdi>normal</bdi>، ترجع للجدول القياسي بالساعات الثابتة (9، 12، 15).",
    ],
    "rule": "تعويض الستيرويد بمرضى أديسون يعتمد على وقت الاستيقاظ الفعلي وليس الساعة الثابتة، خصوصًا بأنظمة العمل بالورديات.",
    "comparison": None,
    "guideline_note": None,
},
638: {
    "idea": "امرأة حامل بالثلث الثالث ومصابة بفرط نشاط درقي معروف على كاربيمازول، وساءت أعراضها مع ارتفاع T4 وT3، فالسؤال يبي أفضل تعديل بالـ<bdi>treatment</bdi>.",
    "clues": [
        ("28 weeks pregnant", "بالثلث الثالث من الحمل، مرحلة مختلفة عن الثلث الأول بخصوص خيارات الـ<bdi>treatment</bdi>"),
        ("currently treated with 15 mg carbimazole", "على <bdi>treatment</bdi> فعلي بس غير كافٍ حاليًا"),
        ("Thyroxine (T4 free serum) 25", "T4 <bdi>elevated</bdi>، يدل على عدم سيطرة كافية"),
    ],
    "why_correct": [
        "بالثلث الثاني والثالث من الحمل، الكاربيمازول هو الخيار المفضل (بعكس الثلث الأول اللي يفضل فيه البروبيلثيوراسيل لتجنب تشوهات الكاربيمازول المبكرة).",
        "بما إن الـ<bdi>symptoms</bdi> ساءت وT4 لسا <bdi>elevated</bdi> رغم 15 ملغم، الـ<bdi>step</bdi> الصحيحة زيادة جرعة الكاربيمازول إلى 20 ملغم مع <bdi>follow-up</bdi> الاستجابة.",
        "التحول للـPTU بهذا التوقيت (28 أسبوع) غير ضروري لأن <bdi>risk</bdi> تشوهات الكاربيمازول يخص الثلث الأول فقط، والقيصرية أو الاستئصال غير مبررين لمجرد سوء الضبط الدوائي.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>patient</bdi> بالثلث الأول من الحمل، يفضل التحول للبروبيلثيوراسيل بدل زيادة الكاربيمازول.",
        "لو فشل الـ<bdi>treatment</bdi> الدوائي كليًا بالسيطرة رغم الجرعات القصوى، يصير التفكير باستئصال الغدة الجراحي بالثلث الثاني.",
    ],
    "rule": "الكاربيمازول هو الخيار المفضل لفرط نشاط الدرقية بالثلث الثاني والثالث من الحمل، بينما يفضل PTU بالثلث الأول فقط.",
    "comparison": None,
    "guideline_note": None,
},
639: {
    "idea": "امرأة بالثلث الأول من الحمل عندها فرط نشاط درقي واضح مع أجسام مضادة إيجابية لمستقبل TSH (<bdi>Graves' disease</bdi>)، والسؤال يبي أفضل <bdi>treatment</bdi> بهذي المرحلة المبكرة من الحمل تحديدًا.",
    "clues": [
        ("6 weeks pregnant", "بالثلث الأول من الحمل، فترة حرجة لتشوهات الأجنة من بعض أدوية الدرقية"),
        ("TSH receptor antibodies Positive", "يؤكد <bdi>diagnosis</bdi> <bdi>Graves' disease</bdi> ك<bdi>cause</bdi> فرط النشاط"),
        ("TSH 0.001", "فرط نشاط درقي <bdi>severe</bdi> جدًا"),
    ],
    "why_correct": [
        "بالثلث الأول من الحمل، <bdi>Propylthiouracil (PTU)</bdi> هو الـ<bdi>treatment</bdi> المفضل لأن الكاربيمازول بهذي المرحلة مرتبط بتشوهات جنينية معينة (مثل عيوب فروة الرأس والمريء).",
        "بعد الثلث الأول، ينصح بالتحول للكاربيمازول لتجنب <bdi>risk</bdi> التسمم الكبدي النادر المرتبط بـPTU طويل المدى.",
        "الـ<bdi>propranolol</bdi> يفيد ك<bdi>treatment</bdi> مساعد لل<bdi>symptoms</bdi> (<bdi>palpitations</bdi>، رجفة) بس ما يعالج فرط النشاط نفسه، والاستئصال الجراحي <bdi>procedure</bdi> يحفظ لحالات خاصة مو كخط أول بالحمل المبكر.",
    ],
    "when_changes": [
        "بعد إتمام الثلث الأول من الحمل، تتحول الـ<bdi>patient</bdi> للكاربيمازول ك<bdi>treatment</bdi> أساسي.",
        "لو فشل الـ<bdi>treatment</bdi> الدوائي أو فيه حساسية <bdi>severe</bdi> له، يصير استئصال الغدة الجراحي بالثلث الثاني خيار بديل.",
    ],
    "rule": "بالثلث الأول من الحمل، PTU هو الخط الأول ل<bdi>treatment</bdi> <bdi>Graves' disease</bdi>، ثم يتحول للكاربيمازول بعد ذلك.",
    "comparison": None,
    "guideline_note": None,
},
640: {
    "idea": "امرأة بدون <bdi>symptoms</bdi> واضحة اكتشف عندها TSH <bdi>elevated</bdi> جدًا (فوق 10) مع T4 <bdi>low</bdi>، وهذا يعتبر قصور درقية واضح يحتاج <bdi>treatment</bdi> رغم غياب الـ<bdi>symptoms</bdi> الظاهرة.",
    "clues": [
        ("Otherwise, she is asymptomatic", "غياب الـ<bdi>symptoms</bdi> الظاهرة، بس هذا لا يمنع الـ<bdi>treatment</bdi> إذا كان الاضطراب المخبري <bdi>severe</bdi>"),
        ("Thyroid-Stimulating Hormone 15", "TSH <bdi>elevated</bdi> بشكل كبير جدًا، فوق حد الـ10 اللي يعتبر مؤشر قوي لبدء الـ<bdi>treatment</bdi>"),
        ("Thyroxine (T4 free serum) 6.5", "T4 <bdi>low</bdi> بوضوح، يؤكد قصور درقية واضح مو تحت سريري فقط"),
    ],
    "why_correct": [
        "TSH فوق 10 مع T4 <bdi>low</bdi> يمثل قصور درقية واضح (overt hypothyroidism)، وهذا يستدعي بدء الـ<bdi>treatment</bdi> بغض النظر عن غياب الـ<bdi>symptoms</bdi> الظاهرة.",
        "بدء <bdi>levothyroxine replacement</bdi> يمنع تطور الـ<bdi>complications</bdi> طويلة المدى ل<bdi>hypothyroidism</bdi> غير المعالج (مثل اضطراب الدهون و<bdi>diseases</bdi> القلب).",
        "التطمين والخروج بدون <bdi>treatment</bdi>، أو تكرار الفحص فقط، غير كافٍ مع هذا المستوى الـ<bdi>severe</bdi> من ارتفاع TSH مع انخفاض T4 المؤكد.",
    ],
    "when_changes": [
        "لو كان TSH بين 5 و10 فقط مع T4 <bdi>normal</bdi> (قصور تحت سريري)، القرار بالـ<bdi>treatment</bdi> يعتمد أكثر على الـ<bdi>symptoms</bdi> والـ<bdi>factors</bdi> الأخرى.",
        "لو كانت الـ<bdi>patient</bdi> حامل، عتبة بدء الـ<bdi>treatment</bdi> تكون أخفض من غير الحامل.",
    ],
    "rule": "TSH فوق 10 مع T4 <bdi>low</bdi> يمثل قصور درقية واضح يستحق بدء الـ<bdi>treatment</bdi> حتى بدون <bdi>symptoms</bdi> ظاهرة.",
    "comparison": None,
    "guideline_note": None,
},
641: {
    "idea": "<bdi>patient</bdi> <bdi>diabetes</bdi> نوع أول بحماض كيتوني <bdi>severe</bdi>، بدأ علاجها بالسوائل والـ<bdi>insulin</bdi>، والسؤال يبي معدل النزول الآمن لسكر الدم أثناء الـ<bdi>treatment</bdi> لتجنب <bdi>complication</bdi> خطيرة.",
    "clues": [
        ("blood sugar<br>is reviewed 3 hours after treatment was initiated", "<bdi>follow-up</bdi> مبكرة أثناء الـ<bdi>treatment</bdi> النشط للحماض الكيتوني"),
        ("ABG HCO3- 8", "بيكربونات <bdi>low</bdi> جدًا، حماض <bdi>severe</bdi>"),
        ("pH 7.2", "حماض دم واضح"),
        ("Random Glucose 32", "سكر <bdi>elevated</bdi> جدًا يحتاج تصحيح تدريجي لا مفاجئ"),
    ],
    "why_correct": [
        "خفض سكر الدم بسرعة كبيرة جدًا أثناء <bdi>treatment</bdi> الحماض الكيتوني يزيد <bdi>risk</bdi> وذمة دماغية خطيرة خصوصًا بالحماض الـ<bdi>severe</bdi>.",
        "الهدف الآمن هو خفض سكر الدم تدريجيًا بمعدل حوالي 3 مليمول/لتر بالساعة، مو أسرع ولا أبطأ من كذا.",
        "خفض السكر لأقل من 14 بسرعة قصوى، أو خفضه بمعدل 6 بالساعة، أو إبقاؤه فوق 18 عمدًا، كلها لا تتماشى مع مبدأ التصحيح التدريجي الآمن.",
    ],
    "when_changes": [
        "لو نزل السكر بسرعة كبيرة تحت المعدل المستهدف، يحتاج تقليل معدل تسريب الـ<bdi>insulin</bdi> أو إضافة دكستروز للسوائل.",
        "بعد ما يصل السكر لحوالي 14 مليمول/لتر، يضاف دكستروز للسوائل الوريدية للاستمرار بالـ<bdi>insulin</bdi> بأمان دون هبوط سكر <bdi>severe</bdi>.",
    ],
    "rule": "تصحيح سكر الدم بالحماض الكيتوني <bdi>diabetes</bdi> لازم يكون تدريجي بمعدل حوالي 3 مليمول/لتر بالساعة، تجنبًا ل<bdi>risk</bdi> الوذمة الدماغية.",
    "comparison": None,
    "guideline_note": None,
},
642: {
    "idea": "شاب <bdi>diabetes</bdi> نوع أول دخل بحماض كيتوني <bdi>diabetes</bdi> ب<bdi>cause</bdi> إيقاف الـ<bdi>insulin</bdi>، وبدأ على سوائل وريدية، والسؤال يبي أنسب نظام <bdi>insulin</bdi> أثناء <bdi>treatment</bdi> الحماض تحديدًا.",
    "clues": [
        ("has not had his insulin for the last 24 hours", "توقف كامل عن الـ<bdi>insulin</bdi> هو الـ<bdi>cause</bdi> المباشر للحماض"),
        ("basal bolus regime with Glargine", "نظامه المعتاد بالمنزل يحتوي <bdi>insulin</bdi> قاعدي طويل المفعول"),
        ("diagnosed<br>with diabetic ketoacidosis", "تأكيد الـ<bdi>diagnosis</bdi>، يحتاج بروتوكول <bdi>treatment</bdi> حماض كيتوني"),
    ],
    "why_correct": [
        "<bdi>treatment</bdi> الحماض الكيتوني يحتاج تسريب <bdi>insulin</bdi> وريدي ثابت المعدل (<bdi>fixed rate IV insulin</bdi>) للسيطرة السريعة على الحماض والكيتونات.",
        "الإرشادات الحديثة توصي بالاستمرار على الـ<bdi>insulin</bdi> القاعدي طويل المفعول (<bdi>glargine</bdi>) المعتاد لل<bdi>patient</bdi> بجانب التسريب الوريدي، لتجنب ارتداد الحماض بعد إيقاف التسريب لاحقًا.",
        "استخدام <bdi>insulin</bdi> تحت الجلد فقط (سلايدنق سكيل أو mixtard) غير كافٍ للسيطرة السريعة على الحماض الكيتوني الـ<bdi>acute</bdi>، والـ<bdi>insulin</bdi> الوريدي وحده بدون القاعدي يترك فجوة عند إيقافه لاحقًا.",
    ],
    "when_changes": [
        "بعد حل الحماض الكيتوني تمامًا واستقرار الأكل، يتحول الـ<bdi>patient</bdi> تدريجيًا لنظامه المعتاد تحت الجلد (القاعدة والجرعات) مع تداخل بسيط قبل إيقاف الوريدي.",
        "لو ما كان الـ<bdi>patient</bdi> على <bdi>insulin</bdi> قاعدي أصلًا بالمنزل، يكتفى بالتسريب الوريدي فقط أثناء الـ<bdi>treatment</bdi> الـ<bdi>acute</bdi>.",
    ],
    "rule": "<bdi>treatment</bdi> الحماض الكيتوني <bdi>diabetes</bdi> يحتاج تسريب <bdi>insulin</bdi> وريدي ثابت المعدل مع الاستمرار على الـ<bdi>insulin</bdi> القاعدي طويل المفعول المعتاد لل<bdi>patient</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
643: {
    "idea": "<bdi>patient</bdi> تأكد تشخيصه بضخامة الأطراف (أكروميغالي)، والسؤال يبي أي فحص مستقبلي إضافي ضروري ب<bdi>cause</bdi> <bdi>complication</bdi> معروفة لهذا الـ<bdi>disease</bdi>.",
    "clues": [
        ("confirm the diagnosis of acromegaly", "تأكيد <bdi>diagnosis</bdi> الأكروميغالي، <bdi>disease</bdi> له <bdi>complications</bdi> معروفة تستحق <bdi>follow-up</bdi> دورية"),
    ],
    "why_correct": [
        "مرضى الأكروميغالي عندهم <bdi>risk</bdi> متزايد لتكوّن سلائل وسرطان القولون ب<bdi>cause</bdi> تأثير هرمون النمو الزائد على تكاثر خلايا القولون.",
        "لذلك يوصى بعمل <bdi>colonoscopy</bdi> دوري لهؤلاء المرضى ك<bdi>follow-up</bdi> إضافية ضرورية بعد تأكيد الـ<bdi>diagnosis</bdi>.",
        "فحوصات مثل تخطيط صدى القلب عبر المريء أو أشعة البطن المقطعية ما تمثل الـ<bdi>follow-up</bdi> القياسية الموصى بها لهذا الـ<bdi>disease</bdi> تحديدًا.",
    ],
    "when_changes": [
        "لو ظهرت <bdi>symptoms</bdi> قلبية واضحة (اعتلال عضلة قلب ناتج عن الأكروميغالي)، يصير تخطيط صدى القلب فحص مهم إضافي.",
        "لو كانت الـ<bdi>patient</bdi> تعاني من <bdi>symptoms</bdi> هضمية أو تاريخ عائلي لسرطان قولون، تزيد أهمية الـ<bdi>follow-up</bdi> بالمنظار بشكل أوضح.",
    ],
    "rule": "مرضى الأكروميغالي يحتاجون <bdi>follow-up</bdi> دورية بمنظار القولون ب<bdi>cause</bdi> زيادة <bdi>risk</bdi> السلائل والسرطان.",
    "comparison": None,
    "guideline_note": None,
},
644: {
    "idea": "رجل سمين ومصاب حديثًا ب<bdi>diabetes</bdi> النوع الثاني مع HbA1c <bdi>elevated</bdi> بشكل واضح فوق الهدف، والسؤال يبي أفضل <bdi>treatment</bdi> أولي يبدأ فيه.",
    "clues": [
        ("strong family history of type 2 diabetes mellitus", "<bdi>factor</bdi> <bdi>risk</bdi> داعم ل<bdi>diagnosis</bdi> <bdi>diabetes</bdi> النوع الثاني"),
        ("BMI 34 kg/m2", "سمنة واضحة"),
        ("Glucose, fasting 9", "سكر صائم <bdi>elevated</bdi> بوضوح"),
        ("НА1C 7.8", "<bdi>elevated</bdi> بشكل واضح فوق الهدف المعتاد (أكثر من 1.5% فوق الهدف)"),
    ],
    "why_correct": [
        "لما يكون HbA1c <bdi>elevated</bdi> بشكل واضح عند الـ<bdi>diagnosis</bdi> (هنا 7.8%، أعلى من الهدف بوضوح)، الإرشادات توصي ببدء الـ<bdi>metformin</bdi> فورًا مع نصائح نمط الحياة معًا، مو الاكتفاء بنمط الحياة فقط.",
        "الجمع بين الحمية والرياضة والـ<bdi>metformin</bdi> (<bdi>Dietary advice, exercise and metformin</bdi>) يعطي فرصة أسرع وأقوى للوصول للهدف مقارنة بنمط الحياة لوحده.",
        "السلفونيل يوريا أو الإكسيناتيد أدوية خط ثاني أو لاحق، مو خيار أولي معتاد قبل تجربة الـ<bdi>metformin</bdi>.",
    ],
    "when_changes": [
        "لو كان HbA1c عند الـ<bdi>diagnosis</bdi> قريب جدًا من الهدف (أقل من 7.5% تقريبًا)، يمكن البدء بنمط الحياة وحده لفترة قبل إضافة دواء.",
        "لو كان الـ<bdi>patient</bdi> عنده موانع لاستخدام الـ<bdi>metformin</bdi> (قصور كلوي <bdi>severe</bdi>)، يحتاج دواء بديل من البداية.",
    ],
    "rule": "عند <bdi>diagnosis</bdi> <bdi>diabetes</bdi> النوع الثاني مع HbA1c <bdi>elevated</bdi> بوضوح فوق الهدف، يبدأ الـ<bdi>metformin</bdi> مباشرة مع نمط الحياة، مو الانتظار.",
    "comparison": None,
    "guideline_note": None,
},
645: {
    "idea": "رجل مصاب حديثًا ب<bdi>diabetes</bdi> النوع الثاني التزم بنمط حياة صحي فترة، وHbA1c لسا فوق الهدف قليلًا، والسؤال يبي الـ<bdi>step</bdi> العلاجية التالية المناسبة.",
    "clues": [
        ("recently diagnosed with type 2<br>diabetes", "<bdi>diagnosis</bdi> حديث نسبيًا"),
        ("following a plan of lifestyle measures", "جرب نمط الحياة فترة كافية قبل هالمتابعة"),
        ("НА1C 6.9", "لسا فوق الهدف المعتاد (أقل من 7%) بس بشكل بسيط"),
    ],
    "why_correct": [
        "الـ<bdi>patient</bdi> التزم بنمط حياة صحي فترة كافية لكن HbA1c لسا فوق الهدف، وهذا يعني نمط الحياة وحده غير كافٍ الآن.",
        "الـ<bdi>step</bdi> التالية الصحيحة هي إضافة <bdi>Metformin</bdi> كخط أول دوائي لل<bdi>diabetes</bdi> النوع الثاني بجانب الاستمرار بنمط الحياة.",
        "الـ<bdi>insulin</bdi> والسلفونيل يوريا أدوية أقوى تحفظ لمراحل لاحقة أو حالات أشد، والاكتفاء بمزيد من الحمية والرياضة وحدها فقط غير كافٍ بعد فشلها أصلًا بالوصول للهدف.",
    ],
    "when_changes": [
        "لو كان HbA1c رجع للهدف الـ<bdi>normal</bdi> بنمط الحياة وحده، لا داعي لإضافة دواء بعد.",
        "لو كان HbA1c <bdi>elevated</bdi> جدًا من البداية (فوق 9% مثلًا)، قد يحتاج الـ<bdi>patient</bdi> <bdi>insulin</bdi> مبكرًا بدل الـ<bdi>metformin</bdi> فقط.",
    ],
    "rule": "إذا فشل نمط الحياة وحده بالوصول للهدف ب<bdi>diabetes</bdi> النوع الثاني، يضاف الـ<bdi>metformin</bdi> كخط أول دوائي.",
    "comparison": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
636: {
    "A": "الأوكتريوتيد يستخدم ل<bdi>treatment</bdi> زيادة هرمون النمو بالأكروميغالي مثلًا، لا علاقة له بورم مضغوط على التصالب هنا.",
    "B": "بروموكريبتين ناهض <bdi>dopamine</bdi> أقدم وأقل تحملًا، وحتى لو استخدم فالـ<bdi>prolactin</bdi> هنا <bdi>elevated</bdi> بشكل بسيط لا يتناسب مع ورم يستجيب دوائيًا كليًا.",
    "C": "الـ<bdi>treatment</bdi> الإشعاعي بطيء المفعول جدًا وغير مناسب ك<bdi>treatment</bdi> أول ل<bdi>symptoms</bdi> ضغط <bdi>acute</bdi> على العصب البصري.",
},
637: {
    "A": "إيقاف الستيرويد أيام العمل <bdi>risk</bdi> جدًا وقد يسبب أزمة كظرية <bdi>acute</bdi>.",
    "B": "الالتزام بساعات ثابتة بالساعة الحقيقية غير مناسب لمن يعمل بالليل وينام بالنهار.",
    "C": "أخذ جرعات بالليل أثناء محاولة النوم بعد يوم عمل ليلي يكسر الإيقاع الفسيولوجي المطلوب تقليده.",
},
638: {
    "A": "القيصرية غير مرتبطة بضبط فرط نشاط الدرقية الدوائي، وقرار الولادة يعتمد على مؤشرات أخرى.",
    "C": "التحول لـPTU غير ضروري بالثلث الثالث لأن <bdi>risk</bdi> تشوهات الكاربيمازول يخص الثلث الأول فقط.",
    "D": "الاستئصال الجراحي <bdi>procedure</bdi> يحفظ لفشل الـ<bdi>treatment</bdi> الدوائي الكامل، مو <bdi>step</bdi> أولى لمجرد سوء ضبط بسيط.",
},
639: {
    "A": "الـ<bdi>propranolol</bdi> يخفف الـ<bdi>symptoms</bdi> بس ما يعالج فرط النشاط نفسه ولا يكفي <bdi>treatment</bdi> وحيدًا.",
    "B": "الكاربيمازول يحمل <bdi>risk</bdi> تشوهات جنينية أعلى خلال الثلث الأول تحديدًا.",
    "D": "استئصال الغدة الجراحي <bdi>procedure</bdi> يحفظ لحالات خاصة، مو خط أول بحمل مبكر مستقر نسبيًا.",
},
640: {
    "A": "التطمين والخروج بدون <bdi>treatment</bdi> غير مناسب مع TSH <bdi>elevated</bdi> جدًا وT4 <bdi>low</bdi> مؤكد (قصور واضح).",
    "B": "الموجات فوق الصوتية على الرقبة لا تفيد ب<bdi>assessment</bdi> شدة القصور الوظيفي أو الحاجة لل<bdi>treatment</bdi> الهرموني.",
    "C": "تكرار الفحص فقط دون <bdi>treatment</bdi> يؤخر بدء <bdi>treatment</bdi> ضروري مع هذا المستوى الـ<bdi>severe</bdi> من الخلل.",
},
641: {
    "A": "خفض السكر لأقل من 14 بأسرع وقت ممكن <bdi>risk</bdi> ويزيد احتمال الوذمة الدماغية.",
    "C": "خفض بمعدل 6 بالساعة أسرع من المعدل الآمن الموصى به.",
    "D": "إبقاء السكر فوق 18 عمدًا لا يمثل هدف علاجي صحيح ل<bdi>case</bdi> حماض كيتوني نشط يحتاج تصحيح تدريجي.",
},
642: {
    "B": "السلايدنق سكيل تحت الجلد أبطأ وأقل فعالية من التسريب الوريدي المستمر بحماض كيتوني نشط.",
    "C": "التسريب الوريدي وحده بدون الاستمرار على القاعدي يترك فجوة تسبب ارتداد الحماض عند إيقاف التسريب لاحقًا.",
    "D": "<bdi>insulin</bdi> المكستارد تحت الجلد غير كافٍ للسيطرة السريعة على حماض كيتوني نشط بهذي المرحلة الـ<bdi>acute</bdi>.",
},
643: {
    "A": "تخطيط صدى القلب عبر المريء ليس الـ<bdi>follow-up</bdi> القياسية الموصى بها ل<bdi>complications</bdi> الأكروميغالي الشائعة.",
    "B": "عدم الحاجة ل<bdi>follow-up</bdi> إضافية غير صحيح لأن <bdi>risk</bdi> سلائل القولون مثبت ومهم بهذا الـ<bdi>disease</bdi>.",
    "D": "الأشعة المقطعية على البطن ليست الفحص الموصى به ل<bdi>follow-up</bdi> <bdi>risk</bdi> سرطان القولون بالأكروميغالي.",
},
644: {
    "B": "نمط الحياة وحده غير كافٍ هنا لأن HbA1c <bdi>elevated</bdi> بشكل واضح فوق الهدف عند الـ<bdi>diagnosis</bdi>.",
    "C": "السلفونيل يوريا دواء خط ثاني عادة، مو خيار أولي معتاد قبل تجربة الـ<bdi>metformin</bdi>.",
    "D": "الإكسيناتيد دواء حقني متقدم أكثر من اللازم كخط علاجي أولي هنا.",
},
645: {
    "A": "الـ<bdi>insulin</bdi> <bdi>treatment</bdi> متقدم جدًا مقارنة ب<bdi>case</bdi> بسيطة الارتفاع فوق الهدف بعد فشل نمط الحياة فقط.",
    "C": "السلفونيل يوريا دواء خط ثاني بعد الـ<bdi>metformin</bdi> عادة، مو الـ<bdi>step</bdi> التالية المباشرة هنا.",
    "D": "الاكتفاء بمزيد من الحمية والرياضة غير كافٍ لأنها جُربت فعلًا ولم تصل للهدف.",
},
})

HIGHLIGHT_TERMS.update({
636: ["bilateral defects in the upper outer quadrants", "Follicle-stimulating hormone 0.2", "Cortisol 8 a.m. 30", "4 cm pituitary mass compressing optic chiasm"],
637: ["Addison's disease", "she informs the medical team that she sometimes does shift-work"],
638: ["28 weeks pregnant", "currently treated with 15 mg carbimazole", "Thyroxine (T4 free serum) 25"],
639: ["6 weeks pregnant", "TSH receptor antibodies Positive", "TSH 0.001"],
640: ["Otherwise, she is asymptomatic", "Thyroid-Stimulating Hormone 15", "Thyroxine (T4 free serum) 6.5"],
641: ["ABG HCO3- 8", "pH 7.2", "Random Glucose 32"],
642: ["has not had his insulin for the last 24 hours", "basal bolus regime with Glargine"],
643: ["confirm the diagnosis of acromegaly"],
644: ["strong family history of type 2 diabetes mellitus", "BMI 34 kg/m2", "Glucose, fasting 9"],
645: ["following a plan of lifestyle measures", "BMI 32"],
})

EXPLANATIONS.update({
646: {
    "idea": "رجل تأكد تشخيصه بفرط نشاط جارات الدرقية الأولي (كالسيوم <bdi>elevated</bdi>، فوسفات <bdi>low</bdi>، PTH <bdi>elevated</bdi>) مع ورم حميد محدد بالموجات فوق الصوتية، والسؤال يبي أي مؤشر يعتبر استطباب صحيح لإزالة الغدة جراحيًا.",
    "clues": [
        ("primary hyperparathyroidism", "<bdi>diagnosis</bdi> مؤكد يحتاج <bdi>assessment</bdi> استطبابات الجراحة"),
        ("elevated calcium, low phosphate and raised PTH levels", "الصورة الكيميائية الكلاسيكية لفرط جارات الدرقية الأولي"),
        ("left lower parathyroid adenoma", "ورم حميد محدد الموقع، يجعل الجراحة ممكنة وموجهة"),
    ],
    "why_correct": [
        "من الاستطبابات المعتمدة لاستئصال الغدة جراحيًا بفرط جارات الدرقية غير العرضي وجود دليل على تأثر العظم مثل <bdi>osteoporosis</bdi> (قياس كثافة عظم <bdi>low</bdi> بشكل كبير).",
        "هذا يعكس ضرر فعلي على العظم من زيادة PTH الـ<bdi>chronic</bdi>، وهذا <bdi>cause</bdi> كافٍ لتوصية الجراحة حتى بدون <bdi>symptoms</bdi> واضحة أخرى.",
        "العمر أكبر من 50، وظيفة كلى <bdi>normal</bdi>، أو ارتفاع PTH لوحده بدون معايير أخرى، كلها ليست من الاستطبابات المعتمدة (العمر أقل من 50 هو الاستطباب، ووظيفة كلى ضعيفة مو <bdi>normal</bdi> هي الاستطباب).",
    ],
    "when_changes": [
        "لو كان عمر الـ<bdi>patient</bdi> أقل من 50 سنة، هذا نفسه يعتبر استطباب ل<bdi>procedure</bdi> الجراحة حتى بدون <bdi>symptoms</bdi>.",
        "لو كانت وظائف الكلى متأثرة (تصفية كرياتينين <bdi>low</bdi>) أو فيه حصوات كلوية، تصير هذي استطبابات إضافية للجراحة.",
    ],
    "rule": "من استطبابات جراحة فرط جارات الدرقية الأولي: <bdi>osteoporosis</bdi> عظام، عمر أقل من 50، تأثر وظيفة الكلى، أو ارتفاع كالسيوم كبير جدًا فوق الـ<bdi>normal</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
647: {
    "idea": "شابة عندها تشنجات يد و<bdi>tremor</bdi> حول الفم مع نقص <bdi>severe</bdi> بالكالسيوم وفيتامين D <bdi>low</bdi> جدًا وإطالة بفترة QT، فالسؤال يبي أول <bdi>step</bdi> علاجية عاجلة لنقص الكالسيوم العرضي الـ<bdi>severe</bdi>.",
    "clues": [
        ("spasms of hands along with twitching<br>around the mouth", "<bdi>signs</bdi> تكزز عصبي عضلي (تيتاني) من نقص كالسيوم <bdi>severe</bdi>"),
        ("prolonged QT interval on ECG", "<bdi>complication</bdi> قلبية خطيرة لنقص الكالسيوم الـ<bdi>severe</bdi>"),
        ("Calcium 1.6 (2.15-2.62)", "نقص كالسيوم <bdi>severe</bdi> جدًا يعادل تقريبًا 6.4 مقابل الـ<bdi>normal</bdi> 8.6-10.5 mg/dL"),
        ("25-Hydroxy Vitamin D3 10", "نقص فيتامين D <bdi>severe</bdi>، الـ<bdi>cause</bdi> الأساسي وراء نقص الكالسيوم هنا"),
    ],
    "why_correct": [
        "نقص الكالسيوم الـ<bdi>severe</bdi> العرضي (تكزز + إطالة QT) <bdi>case</bdi> طارئة تحتاج تصحيح فوري لتجنب تشنجات أو اضطراب نظم قلبي خطير.",
        "الـ<bdi>treatment</bdi> الأولي بهذي الـ<bdi>case</bdi> الـ<bdi>acute</bdi> هو <bdi>Intravenous calcium</bdi> لرفع مستوى الكالسيوم بسرعة وإيقاف الـ<bdi>symptoms</bdi> العصبية والقلبية.",
        "الكالسيوم الفموي وفيتامين D الفموي (cholecalciferol) بطيئين جدًا لل<bdi>case</bdi> الـ<bdi>acute</bdi>، ويستخدمان لاحقًا لل<bdi>treatment</bdi> طويل المدى بعد استقرار الـ<bdi>case</bdi> الـ<bdi>acute</bdi>.",
    ],
    "when_changes": [
        "بعد السيطرة على الـ<bdi>symptoms</bdi> الـ<bdi>acute</bdi>، يبدأ الـ<bdi>treatment</bdi> طويل المدى بمكملات الكالسيوم الفموي وفيتامين D لتصحيح النقص الأساسي.",
        "لو كان النقص <bdi>mild</bdi> بدون <bdi>symptoms</bdi> عصبية أو قلبية، يكتفى بمكملات فموية من البداية بدون حاجة لتسريب وريدي.",
    ],
    "rule": "نقص الكالسيوم العرضي الـ<bdi>severe</bdi> (تكزز، تشنجات، إطالة QT) يعالج بالكالسيوم الوريدي فورًا، والفموي يأتي لاحقًا للصيانة.",
    "comparison": None,
    "guideline_note": None,
},
648: {
    "idea": "رجل كبير بالسن عنده <bdi>disease</bdi> شرايين طرفية عولج بقسطرة وتوسيع، مع قصور كلوي <bdi>chronic</bdi> مرحلة 3 وارتفاع كوليسترول LDL، والسؤال يبي أفضل <bdi>treatment</bdi> وقائي ثانوي ل<bdi>diseases</bdi> القلب والأوعية عنده.",
    "clues": [
        ("acute leg ischemia treated with<br>angioplasty and stenting", "حدث وعائي واضح يستدعي وقاية ثانوية قوية"),
        ("stage 3 chronic kidney disease", "يحدد اختيار وجرعة بعض أدوية الوقاية"),
        ("LDL (cholesterol) 4.9 (&lt;4.0)", "ارتفاع LDL فوق الهدف رغم وجود <bdi>disease</bdi> وعائي مثبت"),
    ],
    "why_correct": [
        "أي <bdi>patient</bdi> بحدث وعائي واضح (نقص تروية <bdi>acute</bdi> بالساق) يحتاج <bdi>treatment</bdi> وقاية ثانوية قوي يشمل خفض الكوليسترول بشكل فعال.",
        "الـ<bdi>statin</bdi> القوي مثل <bdi>Rosuvastatin</bdi> يستخدم بحذر وجرعة معدّلة عند وجود قصور كلوي، لكنه يبقى مستطبب وفعال للوقاية الثانوية حتى بهذي الـ<bdi>case</bdi>.",
        "عدم إعطاء <bdi>treatment</bdi> إضافي غير مناسب مع LDL فوق الهدف بعد حدث وعائي مثبت، والنياسين والإيزتيميب ليسا الخط الأول للوقاية الثانوية بوجود دليل قوي لفائدة الـ<bdi>statin</bdi>.",
    ],
    "when_changes": [
        "لو كان <bdi>renal failure</bdi> <bdi>severe</bdi> جدًا (مرحلة متقدمة أكثر)، يحتاج تعديل جرعة الـ<bdi>statin</bdi> بعناية أكبر بدل تجنبه كليًا.",
        "لو كان LDL أصلًا ضمن الهدف رغم الحدث الوعائي، ممكن الاكتفاء بالجرعة الحالية دون تصعيد.",
    ],
    "rule": "بعد أي حدث وعائي واضح، يستطب الـ<bdi>statin</bdi> للوقاية الثانوية حتى بوجود قصور كلوي <bdi>chronic</bdi>، مع تعديل الجرعة حسب الحاجة.",
    "comparison": None,
    "guideline_note": None,
},
649: {
    "idea": "امرأة سمينة بشكل بسيط نسبيًا (BMI أقل من 35) عندها <bdi>diabetes</bdi> وضغط مضبوطين، وفشلت بإنقاص وزنها رغم محاولات جادة متعددة، والسؤال يبي أفضل إضافة دوائية تناسب حالتها بأقل <bdi>symptoms</bdi> جانبية.",
    "clues": [
        ("attempted<br>to lose weight through various commercial diets", "محاولات جادة ومتعددة سابقة بدون نجاح"),
        ("BMI 28,5 kg/m2", "سمنة <bdi>mild</bdi> نسبيًا، أقل من عتبة الجراحة الاستقلابية المعتادة"),
        ("tolerable side effect", "يوجه الاختيار نحو الدواء الأقل <bdi>symptoms</bdi> جانبية من بين الخيارات"),
    ],
    "why_correct": [
        "مؤشر كتلة الجسم هنا أقل من 35، وهذا أقل من العتبة المعتادة للجراحة الاستقلابية حتى مع وجود <bdi>diabetes</bdi> وضغط.",
        "من أدوية إنقاص الوزن، <bdi>Orlistat</bdi> يعتبر من الأقل <bdi>symptoms</bdi> جانبية جهازية (يعمل موضعيًا بالأمعاء) مقارنة بأدوية أخرى مؤثرة على الجهاز العصبي المركزي.",
        "لوركاسيرين وفينترمين-توبيراميت لهما <bdi>symptoms</bdi> جانبية جهازية أو قلبية أكثر، وهذا يجعل أورليستات الخيار الأنسب هنا بناءً على طلب السؤال عن أقل <bdi>symptoms</bdi> جانبية.",
    ],
    "when_changes": [
        "لو كان مؤشر كتلة الجسم 35 فأكثر مع <bdi>disease</bdi> مرافق، تصير الجراحة الاستقلابية خيار أقوى وأكثر فعالية.",
        "لو كان الـ<bdi>patient</bdi> يتحمل الـ<bdi>symptoms</bdi> الجانبية الجهازية بشكل جيد، ممكن تفكر أدوية ثانية أقوى تأثيرًا على إنقاص الوزن.",
    ],
    "rule": "بسمنة أقل من عتبة الجراحة مع فشل الطرق المحافظة، الدواء الأقل <bdi>symptoms</bdi> جانبية مثل أورليستات خيار مناسب للإضافة.",
    "comparison": None,
    "guideline_note": None,
},
650: {
    "idea": "شابة عندها هبوط ضغط عند الوقوف ونقص وزن مع تصبغ داكن بندبة قديمة بيدها، صورة تدعم <bdi>disease</bdi> أديسون (قصور كظري أولي)، والسؤال يبي الفحص التأكيدي الصحيح.",
    "clues": [
        ("dizziness feeling light-headed frequently with standing up", "هبوط ضغط وضعي، من <bdi>signs</bdi> قصور كظري"),
        ("weight loss around 5 kg", "نقص وزن غير مقصود"),
        ("scar on the back of her hand, which has started to turn very dark", "تصبغ جلد غير <bdi>normal</bdi>، <bdi>sign</bdi> مهمة لارتفاع ACTH بقصور كظري أولي"),
        ("Blood pressure 90/60 mmHg", "ضغط <bdi>low</bdi> نسبيًا، يدعم قصور كظري"),
    ],
    "why_correct": [
        "الصورة كاملة (هبوط ضغط وضعي، نقص وزن، تصبغ جلد) تدعم بقوة <bdi>diagnosis</bdi> <bdi>disease</bdi> أديسون (قصور كظري أولي).",
        "الفحص التأكيدي القياسي هو <bdi>Synacthen test</bdi> (اختبار تحفيز ACTH)، اللي يقيس استجابة الكظر لتحفيز خارجي، وفشل الاستجابة يؤكد القصور الكظري الأولي.",
        "قياس الكورتيزول العشوائي وحده أقل دقة لأنه يتأثر بوقت اليوم والتوتر، وأشعة البطن أو اختبار الكبت بالديكساميثازون لا يستخدمان لتأكيد قصور الكظر.",
    ],
    "when_changes": [
        "لو كان الشك بفرط كورتيزول (كوشينغ) بدل قصوره، يصير اختبار الكبت بالديكساميثازون <bdi>low</bdi> الجرعة هو الفحص المناسب بدل سيناكثين.",
        "بعد تأكيد القصور الكظري بسيناكثين، تحتاج فحوصات إضافية لتحديد الـ<bdi>cause</bdi> (مناعي ذاتي أو غيره).",
    ],
    "rule": "الصورة الكلاسيكية لقصور الكظر الأولي (هبوط ضغط وضعي، نقص وزن، تصبغ جلد) تؤكد بـSynacthen test.",
    "comparison": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
646: {
    "A": "العمر أكبر من 50 ليس استطباب، بالعكس العمر أقل من 50 هو الاستطباب المعتمد.",
    "C": "وظيفة الكلى الـ<bdi>normal</bdi> ليست استطباب للجراحة، بالعكس تأثر وظيفة الكلى هو الاستطباب.",
    "D": "ارتفاع PTH وحده بدون معايير أخرى ليس استطباب منفرد كافٍ للجراحة.",
},
647: {
    "A": "الكالسيوم الفموي بطيء جدًا ل<bdi>case</bdi> <bdi>acute</bdi> عرضية بتكزز وإطالة QT.",
    "B": "الكوليكالسيفيرول (فيتامين D فموي) يعالج الـ<bdi>cause</bdi> الأساسي بس بطيء جدًا للسيطرة على الـ<bdi>symptoms</bdi> الـ<bdi>acute</bdi> الآن.",
    "D": "الفوسفات الفموي غير مناسب هنا وقد يزيد ترسب الكالسيوم-فوسفات، وليس <bdi>treatment</bdi> نقص الكالسيوم الـ<bdi>acute</bdi>.",
},
648: {
    "A": "النياسين ليس الخط الأول للوقاية الثانوية من <bdi>diseases</bdi> القلب والأوعية بعد حدث وعائي.",
    "B": "الإيزتيميب يستخدم عادة كإضافة لل<bdi>statin</bdi> وليس بديلًا أول عنه.",
    "D": "عدم إعطاء <bdi>treatment</bdi> إضافي غير مناسب مع LDL فوق الهدف بعد حدث وعائي مثبت مؤخرًا.",
},
649: {
    "B": "لوركاسيرين له تحفظات تتعلق بالسلامة القلبية طويلة المدى مقارنة بأورليستات.",
    "C": "فينترمين-توبيراميت له <bdi>symptoms</bdi> جانبية جهازية وقلبية أكثر من أورليستات الموضعي.",
    "D": "الجراحة الاستقلابية غير مناسبة هنا لأن مؤشر كتلة الجسم أقل من العتبة المعتادة لها.",
},
650: {
    "A": "اختبار الكبت بالديكساميثازون يستخدم ل<bdi>diagnosis</bdi> فرط الكورتيزول (كوشينغ) مو قصوره.",
    "B": "أشعة البطن لا تؤكد الـ<bdi>diagnosis</bdi> الوظيفي للقصور الكظري، فقط تفيد لاحقًا بتحديد الـ<bdi>cause</bdi> التشريحي.",
    "C": "قياس الكورتيزول العشوائي وحده أقل دقة من اختبار التحفيز لتأكيد القصور الكظري.",
},
})

HIGHLIGHT_TERMS.update({
646: ["primary hyperparathyroidism", "elevated calcium, low phosphate and raised PTH levels", "left lower parathyroid adenoma"],
647: ["spasms of hands along with twitching", "prolonged QT interval on ECG", "Calcium 1.6"],
648: ["angioplasty and stenting", "stage 3 chronic kidney disease", "LDL (cholesterol) 4.9"],
649: ["to lose weight through various commercial diets", "BMI 28,5 kg/m2", "tolerable side effect"],
650: ["dizziness feeling light-headed frequently with standing up", "weight loss around 5 kg", "started to turn very dark"],
})

EXPLANATIONS.update({
651: {
    "idea": "رجل كبير بالسن يستخدم <bdi>amiodarone</bdi> ويشتكي من أرق وعصبية و<bdi>palpitations</bdi>، وهذا نمط <bdi>symptoms</bdi> يوجه لتأثير الـ<bdi>amiodarone</bdi> على الغدة الدرقية، فالسؤال يبي الـ<bdi>step</bdi> التالية الصحيحة.",
    "clues": [
        ("He is on amiodarone, fluoxetine and enalopril", "الـ<bdi>amiodarone</bdi> معروف بتأثيره على وظائف الدرقية سواء بفرط أو قصور نشاطها"),
        ("insomnia, irritability and palpitation for 3 months", "<bdi>symptoms</bdi> تتوافق مع فرط نشاط درقي محتمل"),
    ],
    "why_correct": [
        "الـ<bdi>amiodarone</bdi> دواء غني باليود وله تأثير معروف ومباشر على الغدة الدرقية، يسبب إما فرط نشاط أو قصور نشاط درقي.",
        "الـ<bdi>step</bdi> الصحيحة الأولى عند ظهور <bdi>symptoms</bdi> كهذي عند <bdi>patient</bdi> على <bdi>amiodarone</bdi> هي قياس وظائف الدرقية (<bdi>thyroxin level and TSH</bdi>) لتحديد إذا كان الـ<bdi>cause</bdi> درقي قبل أي تفسير آخر.",
        "الـ<bdi>symptoms</bdi> (أرق، عصبية، <bdi>palpitations</bdi>) قد تشبه <bdi>symptoms</bdi> <bdi>anxiety</bdi> أو أثر جانبي لدواء نفسي، لكن مع وجود <bdi>amiodarone</bdi> لازم نستبعد الـ<bdi>cause</bdi> الدرقي أولًا لأنه شائع جدًا ويغير خطة الـ<bdi>treatment</bdi> كليًا.",
    ],
    "when_changes": [
        "لو رجعت وظائف الدرقية <bdi>normal</bdi> تمامًا، عندها يصير التفكير بمراجعة الأدوية النفسية أو <bdi>assessment</bdi> نفسي أكثر منطقية.",
        "لو أكد الفحص فرط نشاط درقي ناتج عن الـ<bdi>amiodarone</bdi>، يحتاج قرار مشترك مع اختصاصي الغدد حول الاستمرار أو إيقاف الـ<bdi>amiodarone</bdi> و<bdi>treatment</bdi> فرط النشاط.",
    ],
    "rule": "أي <bdi>patient</bdi> على <bdi>amiodarone</bdi> تظهر عليه <bdi>symptoms</bdi> تشبه فرط أو قصور نشاط الدرقية، أول <bdi>step</bdi> قياس وظائف الدرقية قبل أي تفسير آخر.",
    "comparison": None,
    "guideline_note": None,
},
652: {
    "idea": "امرأة حامل بالثلث الأول عندها فرط نشاط درقي واضح مع تضخم درقي منتشر وصوت <bdi>crackles</bdi> (bruit) وجحوظ عيون غائب، صورة <bdi>Graves' disease</bdi> على الأغلب، والسؤال يبي أفضل <bdi>treatment</bdi> مناسب لمرحلة الحمل هذي.",
    "clues": [
        ("9 weeks pregnant", "بالثلث الأول من الحمل، فترة حرجة بخصوص اختيار الدواء"),
        ("diffusely enlarged thyroid with an audible bruit", "تضخم درقي نشط مع زيادة تدفق دموي، يدعم <bdi>Graves' disease</bdi>"),
        ("Thyroid-Stimulating Hormone &lt; 0.01", "فرط نشاط درقي <bdi>severe</bdi> جدًا"),
    ],
    "why_correct": [
        "بالثلث الأول من الحمل، <bdi>Propylthiouracil</bdi> هو الـ<bdi>treatment</bdi> المفضل لتجنب <bdi>risk</bdi> التشوهات الجنينية النادرة المرتبطة بالكاربيمازول بهذي المرحلة تحديدًا.",
        "فرط النشاط هنا <bdi>severe</bdi> وعرضي (<bdi>palpitations</bdi>، حرارة، تضخم مع bruit)، فلازم <bdi>treatment</bdi> فعلي فورًا مو مجرد ملاحظة.",
        "الإشعاع واستئصال الغدة الجراحي <bdi>procedures</bdi> لا تناسب هذي المرحلة المبكرة والـ<bdi>mild</bdi> نسبيًا من فرط النشاط، وتحفظ لحالات خاصة لاحقًا.",
    ],
    "when_changes": [
        "بعد إتمام الثلث الأول من الحمل، تتحول الـ<bdi>patient</bdi> للكاربيمازول ك<bdi>treatment</bdi> أساسي بدل البروبيلثيوراسيل.",
        "لو كان فرط النشاط بسيط جدًا وعابر (مثل فرط نشاط الحمل الفسيولوجي المبكر)، قد يكتفى بالمراقبة فقط بدون دواء.",
    ],
    "rule": "بالثلث الأول من الحمل، PTU هو الـ<bdi>treatment</bdi> المفضل لفرط نشاط الدرقية العرضي مثل <bdi>Graves' disease</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
653: {
    "idea": "رجل تأكد عنده متلازمة كوشينغ مع ACTH <bdi>low</bdi> جدًا (يعني المصدر مو نخامي، بل مستقل عن ACTH)، والسؤال يبي أفضل فحص تالي لتحديد مصدر المشكلة بدقة.",
    "clues": [
        ("ACTH &lt; 1 (2-11)", "ACTH <bdi>low</bdi> جدًا، يدل على مصدر كورتيزول مستقل عن ACTH (كظري على الأغلب)"),
        ("24-\nhour urine free cortisol level was greater than 3 times the upper limit", "تأكيد وجود فرط كورتيزول حقيقي وواضح"),
    ],
    "why_correct": [
        "انخفاض ACTH بشكل واضح مع تأكد فرط الكورتيزول يدل على مصدر كورتيزول مستقل عن ACTH، وهذا يعني الأرجح مصدر كظري (ورم أو تضخم كظري).",
        "الـ<bdi>step</bdi> التالية المنطقية هي <bdi>CT scan of the adrenal glands</bdi> لتحديد وتوصيف الكتلة الكظرية المسؤولة.",
        "أخذ عينات من الجيب البترى السفلي أو تصوير النخامية يفيدان لو كان المصدر نخاميًا (ACTH <bdi>elevated</bdi> أو غير مكبوت)، وهذا عكس الصورة هنا تمامًا.",
    ],
    "when_changes": [
        "لو كان ACTH <bdi>elevated</bdi> أو <bdi>normal</bdi> غير مكبوت، يصير تصوير النخامية أو أخذ عينات الجيب البتري هو الـ<bdi>step</bdi> المناسبة بدل تصوير الكظر.",
        "لو كان الكورتيزول الليلي اللعابي هو الفحص المطلوب أصلًا لل<bdi>diagnosis</bdi> الأولي (مو تحديد المصدر)، فهذا سبق فعليًا بتأكيد فرط الكورتيزول بالسؤال.",
    ],
    "rule": "ACTH <bdi>low</bdi> مع فرط كورتيزول مؤكد يوجه لمصدر كظري، و<bdi>step</bdi> التصوير التالية تكون تصوير الكظر لا النخامية.",
    "comparison": None,
    "guideline_note": None,
},
654: {
    "idea": "امرأة عندها صداع <bdi>severe</bdi> مفاجئ وقيء وفقدان رؤية مفاجئ بعين واحدة، وتصوير يظهر نزيف <bdi>acute</bdi> داخل ورم نخامي كبير (نزيف الغدة النخامية أو ما يعرف بـ pituitary apoplexy)، والسؤال يبي أول <bdi>step</bdi> علاجية عاجلة.",
    "clues": [
        ("sudden severe headache,<br>vomiting and right eye vision loss", "صورة كلاسيكية لنزيف نخامي <bdi>acute</bdi> (apoplexy)"),
        ("amenorrhea for the past 2 years", "دليل على قصور هرموني نخامي <bdi>chronic</bdi> سابق من الورم"),
        ("CT of the head: Shows acute pituitary hemorrhage", "تأكيد الـ<bdi>diagnosis</bdi> بالتصوير"),
        ("compressing the optic chiasm and the right\ncavernous sinus", "ضغط خطير على هياكل حيوية مجاورة"),
    ],
    "why_correct": [
        "نزيف الغدة النخامية الـ<bdi>acute</bdi> (<bdi>pituitary apoplexy</bdi>) يسبب <bdi>risk</bdi> قصور كظري <bdi>acute</bdi> مفاجئ ومهدد للحياة ب<bdi>cause</bdi> توقف إفراز ACTH فجأة.",
        "أول <bdi>step</bdi> عاجلة بالطوارئ هي إعطاء <bdi>IV hydrocortisone</bdi> فورًا لتغطية القصور الكظري المحتمل، حتى قبل معرفة <bdi>results</bdi> فحوصات الهرمونات.",
        "<bdi>assessment</bdi> وظائف الغدة النخامية أو التصوير المتكرر يأتيان لاحقًا، وقرار الجراحة العاجلة يعتمد على الاستجابة الأولية وشدة الـ<bdi>symptoms</bdi> العصبية بعد تثبيت الـ<bdi>case</bdi> الهرمونية أولًا.",
    ],
    "when_changes": [
        "لو ساءت الرؤية بسرعة أو ظهرت <bdi>signs</bdi> عصبية متدهورة رغم الهيدروكورتيزون، يصير التفكير بتخفيف الضغط الجراحي العاجل ضروري.",
        "بعد تثبيت الـ<bdi>case</bdi> الحرجة بالهيدروكورتيزون، يجرى <bdi>assessment</bdi> كامل لوظائف الغدة النخامية لتحديد الاحتياج الهرموني طويل المدى.",
    ],
    "rule": "نزيف الغدة النخامية الـ<bdi>acute</bdi> يعالج فورًا بالهيدروكورتيزون الوريدي لتغطية <bdi>risk</bdi> القصور الكظري المفاجئ، قبل أي <bdi>procedure</bdi> آخر.",
    "comparison": None,
    "guideline_note": None,
},
655: {
    "idea": "رجل بدون <bdi>symptoms</bdi> اكتشف عنده عقيدة درقية بالفحص الروتيني، والموجات فوق الصوتية تظهر ملامح مشبوهة (كتل تكلسية دقيقة داخل عقيدة كبيرة نسبيًا)، والسؤال يبي أفضل <bdi>step</bdi> تالية.",
    "clues": [
        ("no palpable cervical lymphadenopathy", "لا دليل على انتشار موضعي حاليًا، بس هذا ما يستبعد الحاجة لل<bdi>assessment</bdi>"),
        ("left 3-cm hypochoic nodule with internal microcalcifications", "ملامح مشبوهة بالموجات فوق الصوتية (حجم كبير + تكلسات دقيقة) توحي باحتمال خباثة"),
    ],
    "why_correct": [
        "وجود عقيدة كبيرة نسبيًا (3 سم) مع تكلسات دقيقة داخلية من أهم الملامح المشبوهة بالموجات فوق الصوتية للسرطان الدرقي الحليمي.",
        "الـ<bdi>step</bdi> التالية القياسية هي <bdi>Fine-needle aspiration</bdi> للعقيدة لتحديد طبيعتها النسيجية بدقة.",
        "التصوير المقطعي أو مسح اليود ما يعطيان <bdi>diagnosis</bdi> نسيجي، والـ<bdi>treatment</bdi> بالثيروكسين غير مبرر أصلًا لأن وظائف الدرقية <bdi>normal</bdi> والمشكلة تشريحية موضعية.",
    ],
    "when_changes": [
        "لو كانت العقيدة صغيرة (أقل من 1 سم) وبدون ملامح مشبوهة، يمكن الاكتفاء بالـ<bdi>follow-up</bdi> بالموجات فوق الصوتية.",
        "لو كان TSH <bdi>low</bdi> (عقيدة نشطة ساخنة)، يفضل مسح باليود قبل الخزعة لأن العقيدات الساخنة نادرًا ما تكون خبيثة.",
    ],
    "rule": "عقيدة درقية بحجم كبير مع ملامح مشبوهة بالموجات فوق الصوتية تحتاج خزعة بالإبرة الدقيقة ك<bdi>step</bdi> تالية مباشرة.",
    "comparison": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
651: {
    "A": "إضافة <bdi>propranolol</bdi> قبل معرفة <bdi>cause</bdi> الـ<bdi>symptoms</bdi> قد تخفي <bdi>sign</bdi> مهمة وتؤخر الـ<bdi>diagnosis</bdi> الصحيح.",
    "C": "استبدال مضاد <bdi>depression</bdi> سابق لأوانه قبل استبعاد الـ<bdi>cause</bdi> الدرقي الشائع مع الـ<bdi>amiodarone</bdi>.",
    "D": "التحويل للطب النفسي مباشرة يتجاوز <bdi>step</bdi> أساسية وسهلة (فحص الدرقية) يجب عملها أولًا.",
},
652: {
    "A": "الأوكتريوتيد وأدوية أخرى لا علاقة لها ب<bdi>treatment</bdi> فرط النشاط الدرقي هنا (خيار غير مطروح فعليًا بهذا السؤال بس القاعدة العامة تبقى PTU هو الصحيح مقارنة بالخيارات الفعلية).",
    "C": "الإشعاع باليود ممنوع تمامًا بالحمل لأنه يضر الغدة الدرقية الجنينية.",
    "D": "استئصال الغدة الجراحي <bdi>procedure</bdi> يحفظ لحالات خاصة أو فشل الـ<bdi>treatment</bdi> الدوائي، مو خط أول هنا.",
},
653: {
    "A": "أخذ عينات الجيب البتري يفيد لو كان المصدر نخاميًا (ACTH غير مكبوت)، وهنا ACTH <bdi>low</bdi> جدًا يستبعد ذلك.",
    "B": "الكورتيزول الليلي اللعابي فحص تشخيصي أولي لفرط الكورتيزول، والـ<bdi>diagnosis</bdi> هنا مؤكد فعلًا والمطلوب تحديد المصدر.",
    "D": "تصوير النخامية غير منطقي مع ACTH <bdi>low</bdi> جدًا يستبعد المصدر النخامي.",
},
654: {
    "B": "<bdi>assessment</bdi> وظائف الغدة النخامية مهم لكنه يأتي بعد تغطية <bdi>risk</bdi> القصور الكظري الفوري بالهيدروكورتيزون.",
    "C": "الانتظار أسبوعين لإعادة التصوير <bdi>risk</bdi> جدًا مع نزيف <bdi>acute</bdi> و<bdi>symptoms</bdi> ضغط عصبي نشطة الآن.",
    "D": "الجراحة العاجلة تأتي بعد أو بالتوازي مع تثبيت الـ<bdi>case</bdi> الهرمونية بالهيدروكورتيزون، مو أول <bdi>procedure</bdi> قبل أي شي.",
},
655: {
    "B": "التصوير المقطعي بالصبغة لا يعطي <bdi>diagnosis</bdi> نسيجي ولا يعتبر الـ<bdi>step</bdi> التالية القياسية لعقيدة مشبوهة.",
    "C": "<bdi>treatment</bdi> الثيروكسين غير مبرر لأن وظائف الدرقية <bdi>normal</bdi> والمشكلة تشريحية موضعية بالعقيدة.",
    "D": "مسح اليود يفيد أكثر لو كان TSH <bdi>low</bdi> (عقيدة نشطة)، وهنا TSH <bdi>normal</bdi> فلا يغير قرار الخزعة.",
},
})

HIGHLIGHT_TERMS.update({
651: ["He is on amiodarone, fluoxetine and enalopril", "insomnia, irritability and palpitation for 3 months"],
652: ["9 weeks pregnant", "diffusely enlarged thyroid with an audible bruit", "Thyroid-Stimulating Hormone &lt; 0.01"],
653: ["ACTH &lt; 1", "hour urine free cortisol level was greater than 3 times the upper limit"],
654: ["vomiting and right eye vision loss", "amenorrhea for the past 2 years", "acute pituitary hemorrhage"],
655: ["no palpable cervical lymphadenopathy", "left 3-cm hypochoic nodule with internal microcalcifications"],
})

EXPLANATIONS.update({
656: {
    "idea": "امرأة شابة عندها ألم رقبة <bdi>severe</bdi> و<bdi>symptoms</bdi> فرط نشاط درقي بعد عدوى فيروسية بالجهاز التنفسي قبل أسابيع، مع نسبة امتصاص يود <bdi>low</bdi> جدًا، صورة كلاسيكية لالتهاب درقية تحت <bdi>acute</bdi> بمرحلة فرط النشاط العابر.",
    "clues": [
        ("viral upper respiratory tract\ninfection 4 weeks ago", "<bdi>cause</bdi> سابق شائع لالتهاب الدرقية تحت الـ<bdi>acute</bdi>"),
        ("normal-\nsized tender gland", "غدة مؤلمة عند الجس، <bdi>sign</bdi> مميزة لالتهاب تحت <bdi>acute</bdi>"),
        ("24-Hour radioactive iodine 5% (low) uptake", "نسبة امتصاص يود <bdi>low</bdi>، تميز الالتهاب التخريبي عن فرط النشاط الحقيقي مثل <bdi>Graves' disease</bdi>"),
    ],
    "why_correct": [
        "نسبة امتصاص اليود الـ<bdi>low</bdi> رغم فرط النشاط الدرقي الواضح تدل إن الهرمون يتسرب من غدة ملتهبة (مو إنتاج زائد حقيقي)، وهذا نموذجي لالتهاب درقية تحت <bdi>acute</bdi>.",
        "بما إن المشكلة تسرب هرمون مخزن مو زيادة إنتاج، فمضادات الدرقية (ميثيمازول أو PTU) ما تفيد هنا لأنها تثبط الإنتاج الجديد فقط.",
        "الـ<bdi>treatment</bdi> بهذي المرحلة الـ<bdi>mild</bdi> نسبيًا يكون داعم وعرضي؛ <bdi>Propranolol</bdi> يخفف <bdi>symptoms</bdi> فرط النشاط العصبية (<bdi>palpitations</bdi>، رجفة، <bdi>anxiety</bdi>) لحين ما يزول الالتهاب من تلقاء نفسه.",
    ],
    "when_changes": [
        "لو كان الألم <bdi>severe</bdi> جدًا مع ترسيب <bdi>elevated</bdi> جدًا وعدم استجابة للمسكنات البسيطة، يصير الستيرويد الفموي (بريدنيزون) خيار علاجي أقوى.",
        "لو كانت نسبة امتصاص اليود <bdi>elevated</bdi> بدل <bdi>low</bdi>، يصير الـ<bdi>diagnosis</bdi> <bdi>Graves' disease</bdi> والـ<bdi>treatment</bdi> مضاد درقية حقيقي.",
    ],
    "rule": "فرط نشاط درقي مع نسبة امتصاص يود <bdi>low</bdi> وغدة مؤلمة بعد عدوى فيروسية يشخص التهاب درقية تحت <bdi>acute</bdi>، وعلاجه داعم (<bdi>propranolol</bdi> لل<bdi>symptoms</bdi>) وليس مضاد درقية.",
    "comparison": None,
    "guideline_note": None,
},
657: {
    "idea": "<bdi>patient</bdi> كبيرة بالسن ب<bdi>case</bdi> إنتان <bdi>severe</bdi> بالعناية المركزة، وتحاليل الدرقية تظهر انخفاض بكل من TSH وT3 وT4، وهذا النمط النموذجي للمتلازمة اليوثيرويدية الـ<bdi>patient</bdi> (sick euthyroid) ب<bdi>cause</bdi> الـ<bdi>disease</bdi> الـ<bdi>acute</bdi> الـ<bdi>severe</bdi> وليس <bdi>disease</bdi> درقي حقيقي.",
    "clues": [
        ("pneumonia<br>requiring intubation, intravenous fluids, and dopamine support", "<bdi>disease</bdi> حرج <bdi>severe</bdi> بالعناية المركزة، سياق نموذجي للمتلازمة اليوثيرويدية الـ<bdi>patient</bdi>"),
        ("no proposis, examination or the neck shows a normal-sized thyroid without nodules", "لا دليل جسدي على <bdi>disease</bdi> درقي أولي حقيقي"),
        ("Triiodothyronine (T3 free serum) 2 (3.5-6.5)", "T3 <bdi>low</bdi> بوضوح"),
        ("Thyroxine (T4 free serum) 11 (8.5-15.2)", "T4 <bdi>normal</bdi>-<bdi>low</bdi> الحد"),
    ],
    "why_correct": [
        "بالـ<bdi>disease</bdi> الحرج الـ<bdi>severe</bdi>، الجسم يقلل تحويل T4 إلى T3 النشط ويزيد تحويله لـreverse T3 غير النشط، فينخفض T3 بشكل واضح مع T4 <bdi>normal</bdi> أو <bdi>low</bdi> حدي وTSH <bdi>normal</bdi> أو <bdi>low</bdi> بسيط.",
        "الفحص الجسدي الـ<bdi>normal</bdi> للغدة الدرقية (بدون تضخم أو جحوظ) يدعم إن المشكلة مو <bdi>disease</bdi> درقي أولي، بل استجابة جهازية لل<bdi>disease</bdi> الحرج.",
        "هذا النمط يسمى <bdi>euthyroid sick syndrome</bdi> ولا يحتاج <bdi>treatment</bdi> هرموني درقي، بل يتحسن تلقائيًا بعد الشفاء من الـ<bdi>disease</bdi> الحرج الأساسي.",
    ],
    "when_changes": [
        "لو كان TSH <bdi>elevated</bdi> بوضوح مع T4 <bdi>low</bdi>، يصير الـ<bdi>diagnosis</bdi> قصور درقية أولي حقيقي يحتاج <bdi>treatment</bdi>.",
        "لو كان فيه جحوظ عيون وتضخم درقي واضح، يصير التفكير ب<bdi>disease</bdi> <bdi>Graves' disease</bdi> حقيقي بدل المتلازمة اليوثيرويدية الـ<bdi>patient</bdi>.",
    ],
    "rule": "بالـ<bdi>disease</bdi> الحرج الـ<bdi>severe</bdi>، انخفاض T3 مع T4 <bdi>normal</bdi> أو <bdi>low</bdi> حدي وTSH شبه <bdi>normal</bdi> يمثل متلازمة يوثيرويدية <bdi>patient</bdi>، ولا يحتاج <bdi>treatment</bdi> درقي.",
    "comparison": None,
    "guideline_note": None,
},
658: {
    "idea": "امرأة عندها تعب وزيادة وزن رغم الالتزام بحمية ورياضة، مع جلد جاف وغدة درقية متضخمة عقيدية بشكل <bdi>mild</bdi>، وأجسام مضادة TPO <bdi>elevated</bdi> جدًا مع TSH <bdi>elevated</bdi> بشكل ثابت بفحصين متكررين، صورة كلاسيكية لالتهاب هاشيموتو مع قصور درقي واضح يحتاج <bdi>treatment</bdi>.",
    "clues": [
        ("her mother had hypothyroidism", "تاريخ عائلي يدعم <bdi>disease</bdi> درقي مناعي ذاتي"),
        ("thyroid gland mildly enlarged with a diffusely nodular texture", "تضخم درقي منتشر نموذجي لهاشيموتو"),
        ("Laboratory studies are with similar results for\nTSH and T4 were obtained 4 months ago", "تأكيد ثبات الاضطراب بفحصين متكررين، يستبعد خطأ عابر"),
        ("Thyroid peroxidase antibody (TPOAb) 150 (&lt;35)", "ارتفاع كبير جدًا بأجسام مضادة TPO، يؤكد <bdi>cause</bdi> مناعي ذاتي (هاشيموتو)"),
    ],
    "why_correct": [
        "ارتفاع TSH بشكل ثابت متكرر مع T4 <bdi>low</bdi> حدي وأجسام مضادة TPO <bdi>elevated</bdi> جدًا يؤكد قصور درقية أولي حقيقي ب<bdi>cause</bdi> التهاب هاشيموتو المناعي الذاتي.",
        "بما إن الاضطراب مؤكد بفحصين متباعدين بنفس الـ<bdi>result</bdi> تقريبًا، الـ<bdi>step</bdi> الصحيحة هي البدء ب<bdi>treatment</bdi> <bdi>levothyroxine therapy</bdi> مباشرة بدل الانتظار أكثر.",
        "الموجات فوق الصوتية أو مسح اليود المشع لا يغيران قرار الـ<bdi>treatment</bdi> الهرموني الأساسي هنا، والانتظار سنة كاملة لإعادة الفحص يؤخر <bdi>treatment</bdi> ضروري ومؤكد.",
    ],
    "when_changes": [
        "لو كانت هذي أول مرة تظهر فيها الـ<bdi>result</bdi> غير الـ<bdi>normal</bdi> بدون تأكيد سابق، يفضل تكرار الفحص أولًا قبل البدء بالـ<bdi>treatment</bdi>.",
        "لو كان TSH <bdi>elevated</bdi> بشكل بسيط جدًا فقط مع T4 <bdi>normal</bdi> تمامًا (قصور تحت سريري <bdi>mild</bdi>)، القرار بالـ<bdi>treatment</bdi> يعتمد أكثر على الـ<bdi>symptoms</bdi> و<bdi>factors</bdi> أخرى.",
    ],
    "rule": "ارتفاع TSH المؤكد بفحصين متكررين مع أجسام مضادة TPO <bdi>elevated</bdi> يشخص هاشيموتو مع قصور درقي يستحق بدء الـ<bdi>treatment</bdi> الهرموني.",
    "comparison": None,
    "guideline_note": None,
},
659: {
    "idea": "رجل عالج حصوة كلوية مؤخرًا واكتشف عنده ارتفاع كالسيوم واضح مع فوسفات <bdi>low</bdi> وPTH <bdi>elevated</bdi> جدًا جدًا، صورة كلاسيكية لفرط جارات الدرقية الأولي.",
    "clues": [
        ("treated of\na kidney stone in the Emergency Department", "حصوة كلوية، من <bdi>complications</bdi> ارتفاع الكالسيوم الـ<bdi>chronic</bdi>"),
        ("Calcium 2.95 (2.15-2.62)", "ارتفاع واضح بالكالسيوم"),
        ("Phosphate, inorganic 0.76 (0.82-1.51)", "فوسفات <bdi>low</bdi>، يتوافق مع زيادة إفراز جارات الدرقية"),
        ("Parathyroid hormone (intact PTH levels) 200 (1.1-5.3)", "ارتفاع هائل بـPTH، يؤكد المصدر"),
    ],
    "why_correct": [
        "ارتفاع الكالسيوم مع انخفاض الفوسفات وارتفاع PTH بشكل كبير جدًا هو النمط الكلاسيكي لفرط جارات الدرقية الأولي (<bdi>primary hyperparathyroidism</bdi>).",
        "الحصوة الكلوية <bdi>complication</bdi> شائعة ومتوقعة لارتفاع الكالسيوم الـ<bdi>chronic</bdi> الناتج عن زيادة إفراز جارات الدرقية.",
        "الـ<bdi>causes</bdi> الأخرى (متلازمة الحليب والقلوي، فرط جارات الدرقية الثانوي، زيادة فيتامين D النشط) تعطي أنماط PTH وفوسفات مختلفة عن هذي الصورة تمامًا.",
    ],
    "when_changes": [
        "لو كان PTH <bdi>low</bdi> بدل <bdi>elevated</bdi> مع ارتفاع كالسيوم، يصير الـ<bdi>cause</bdi> الأرجح غير جارات الدرقية (مثل ورم خبيث أو زيادة فيتامين D).",
        "لو كان فيه قصور كلوي <bdi>chronic</bdi> <bdi>severe</bdi> مسبق مع فرط جارات ثانوي، يكون PTH <bdi>elevated</bdi> أيضًا بس الكالسيوم عادة <bdi>low</bdi> أو <bdi>normal</bdi> مو <bdi>elevated</bdi>.",
    ],
    "rule": "ارتفاع كالسيوم مع انخفاض فوسفات وارتفاع PTH كبير جدًا يشخص فرط جارات الدرقية الأولي.",
    "comparison": None,
    "guideline_note": None,
},
660: {
    "idea": "امرأة تستخدم كريم ستيرويد موضعي قوي جدًا (كلوبيتاسول) لفترة طويلة على مساحة كبيرة من الجلد ل<bdi>treatment</bdi> الصدفية، وطورت صورة كوشينغية كاملة مع ACTH وكورتيزول منخفضين جدًا، وهذا يؤكد إن المصدر خارجي (من الكريم الموضعي) لا داخلي.",
    "clues": [
        ("using clobetasol cream (topical steroid)", "استخدام ستيرويد موضعي قوي، مصدر محتمل لامتصاص جهازي كافٍ يسبب كوشينغ"),
        ("ACTH 1.4 (2-11)", "ACTH <bdi>low</bdi> جدًا، يدل على كبت المحور من مصدر ستيرويد خارجي"),
        ("Cortisol 8 a.m. 55 (138-635)", "كورتيزول <bdi>low</bdi> جدًا أيضًا، يتوافق مع كبت المحور الكظري من الخارج"),
    ],
    "why_correct": [
        "انخفاض ACTH والكورتيزول معًا (بدل ارتفاع الكورتيزول الداخلي) يدل إن مصدر الصورة الكوشينغية خارجي (من الكريم الموضعي المستخدم بكثرة)، وهذا يسمى <bdi>iatrogenic Cushing syndrome</bdi>.",
        "الاستخدام الموضعي المكثف والمطول للستيرويدات القوية على مساحة جلدية كبيرة (خصوصًا مع جلد ملتهب من الصدفية) يسمح بامتصاص جهازي كافٍ يكبت المحور الـ<bdi>normal</bdi> بالكامل.",
        "<bdi>causes</bdi> كوشينغ الداخلية (نخامية، كظرية، أو خارج نخامية) كلها تعطي ارتفاع كورتيزول حقيقي مع ACTH <bdi>elevated</bdi> أو <bdi>low</bdi> حسب المصدر، مو انخفاض الاثنين معًا كما هنا.",
    ],
    "when_changes": [
        "لو ما فيه تاريخ استخدام ستيرويد خارجي وكان ACTH والكورتيزول مرتفعين، يصير التفكير ب<bdi>cause</bdi> داخلي حقيقي (نخامي أو كظري).",
        "بعد إيقاف الستيرويد الموضعي تدريجيًا، يحتاج المحور الكظري وقت لين يرجع لعمله الـ<bdi>normal</bdi>، وقد تحتاج تغطية ستيرويد مؤقتة أثناء ذلك.",
    ],
    "rule": "انخفاض ACTH والكورتيزول معًا عند <bdi>patient</bdi> بصورة كوشينغية يشخص كوشينغ علاجي المنشأ من مصدر ستيرويد خارجي (حتى لو موضعي).",
    "comparison": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
656: {
    "B": "ميثيمازول مضاد درقية يثبط الإنتاج الجديد، وهذا غير مفيد ب<bdi>case</bdi> تسرب هرمون مخزن من غدة ملتهبة.",
    "C": "بروبيلثيوراسيل بنفس آلية الميثيمازول تقريبًا، غير فعال هنا لنفس الـ<bdi>cause</bdi>.",
    "D": "اليود المشع <bdi>treatment</bdi> لفرط نشاط حقيقي مستمر، غير مناسب لالتهاب عابر بامتصاص يود <bdi>low</bdi> أصلًا.",
},
657: {
    "A": "<bdi>Graves' disease</bdi> يعطي فحص جسدي غير <bdi>normal</bdi> عادة (تضخم درقي، جحوظ)، وهذا غير موجود هنا.",
    "B": "التهاب تحت <bdi>acute</bdi> يترافق مع ألم وتضخم درقي واضح، وهذا غائب هنا تمامًا.",
    "C": "هاشيموتو يسبب قصور درقية أولي حقيقي مع TSH <bdi>elevated</bdi> عادة، مو هذا النمط من <bdi>disease</bdi> حرج.",
},
658: {
    "A": "الموجات فوق الصوتية تفيد ل<bdi>assessment</bdi> شكل الغدة بس لا تغير قرار بدء الـ<bdi>treatment</bdi> الهرموني هنا.",
    "C": "الانتظار سنة كاملة يؤخر <bdi>treatment</bdi> قصور درقية مؤكد ومتكرر بفحصين متباعدين بنفس الـ<bdi>result</bdi>.",
    "D": "مسح اليود المشع لا يفيد ب<bdi>case</bdi> قصور درقية، يستخدم أكثر ل<bdi>assessment</bdi> فرط النشاط.",
},
659: {
    "A": "متلازمة الحليب والقلوي تنتج عادة عن إفراط تناول الكالسيوم والقلويات، ولا تعطي PTH <bdi>elevated</bdi> بهذا الشكل (بل <bdi>low</bdi>).",
    "C": "فرط جارات الدرقية الثانوي يحصل استجابة لنقص كالسيوم <bdi>chronic</bdi> (زي قصور كلوي)، والكالسيوم فيه يكون <bdi>low</bdi> أو <bdi>normal</bdi> لا <bdi>elevated</bdi>.",
    "D": "زيادة فيتامين D النشط ترفع الكالسيوم بس تكبت PTH (يكون <bdi>low</bdi>)، عكس الصورة هنا.",
},
660: {
    "A": "الإفراز خارج نخامي لـACTH يعطي ACTH وكورتيزول مرتفعين، عكس الصورة هنا تمامًا.",
    "C": "سرطان قشرة الكظر يعطي كورتيزول <bdi>elevated</bdi> مع ACTH <bdi>low</bdi> بس عادة بشكل أشد وأسرع تطورًا، والقصة هنا تدعم مصدر خارجي من الكريم.",
    "D": "متلازمة كوشينغ الداخلية العامة تفترض ارتفاع كورتيزول حقيقي، وهذا عكس الكورتيزول الـ<bdi>low</bdi> هنا.",
},
})

HIGHLIGHT_TERMS.update({
656: ["viral upper respiratory tract", "tender gland", "5% (low) uptake"],
657: ["requiring intubation, intravenous fluids, and dopamine support", "Triiodothyronine (T3 free serum) 2", "Thyroxine (T4 free serum) 11"],
658: ["her mother had hypothyroidism", "gland mildly enlarged with a diffusely nodular texture", "Thyroid peroxidase antibody (TPOAb) 150"],
659: ["Calcium 2.95", "Phosphate, inorganic 0.76", "Parathyroid hormone (intact PTH levels) 200"],
660: ["using clobetasol cream (topical steroid)", "ACTH 1.4", "Cortisol 8 a.m. 55"],
})

EXPLANATIONS.update({
661: {
    "idea": "شاب عنده حماض كيتوني <bdi>diabetes</bdi> جديد الـ<bdi>diagnosis</bdi> مع حماض <bdi>severe</bdi> جدًا (pH 7.10) وبوتاسيوم <bdi>normal</bdi> (مو <bdi>low</bdi>)، بدأ على سوائل وريدية بالفعل، والسؤال يبي الـ<bdi>step</bdi> التالية الصحيحة بالـ<bdi>treatment</bdi>.",
    "clues": [
        ("Intravenous 0.9% saline is initiated", "السوائل بدأت فعلًا، والـ<bdi>step</bdi> التالية هي إكمال بروتوكول الحماض الكيتوني"),
        ("pH 7.10", "حماض <bdi>severe</bdi> جدًا يؤكد الـ<bdi>diagnosis</bdi> ويستدعي <bdi>treatment</bdi> فعال بسرعة"),
        ("Potassium 4.4", "بوتاسيوم <bdi>normal</bdi>، آمن لبدء الـ<bdi>insulin</bdi> بدون تأخير"),
        ("Random Glucose 25", "سكر <bdi>elevated</bdi> جدًا، يحتاج تصحيح بالـ<bdi>insulin</bdi>"),
    ],
    "why_correct": [
        "بعد بدء السوائل الوريدية، الـ<bdi>step</bdi> التالية القياسية ب<bdi>treatment</bdi> الحماض الكيتوني هي بدء <bdi>intravenous insulin therapy</bdi> للسيطرة على الحماض والكيتونات وخفض السكر تدريجيًا.",
        "البوتاسيوم هنا <bdi>normal</bdi> (4.4)، وهذا آمن تمامًا لبدء الـ<bdi>insulin</bdi> مباشرة بدون تأخير أو تعويض بوتاسيوم إضافي أولًا.",
        "المضادات الحيوية غير مبررة بدون دليل واضح على عدوى بكتيرية محددة، والبيكربونات الوريدي لا يستخدم بشكل روتيني بالحماض الكيتوني إلا بحالات حماض <bdi>severe</bdi> جدًا خاصة (pH أقل من 6.9 عادة).",
    ],
    "when_changes": [
        "لو كان البوتاسيوم <bdi>low</bdi> (أقل من 3.3)، لازم نعوضه أولًا قبل بدء الـ<bdi>insulin</bdi> لتجنب هبوطه أكثر بشكل خطير.",
        "لو ظهرت <bdi>signs</bdi> عدوى واضحة (بؤرة محددة، ارتفاع حرارة موثق مع <bdi>results</bdi> مزارع)، يضاف <bdi>treatment</bdi> مضاد حيوي موجه بجانب <bdi>treatment</bdi> الحماض.",
    ],
    "rule": "بعد بدء السوائل ب<bdi>treatment</bdi> الحماض الكيتوني <bdi>diabetes</bdi>، الـ<bdi>step</bdi> التالية هي بدء تسريب الـ<bdi>insulin</bdi> الوريدي طالما البوتاسيوم ليس <bdi>low</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
662: {
    "idea": "رجل عنده كوشينغ واضح مع ACTH <bdi>low</bdi> جدًا (مصدر كظري) وكتلة كظرية كبيرة (5 سم) بخصائص تصوير تثير <bdi>anxiety</bdi> من الخباثة (نسبة انغسال تباين <bdi>low</bdi>)، والسؤال يبي أفضل <bdi>step</bdi> علاجية تالية.",
    "clues": [
        ("moon like face, dorsocervical fat pad", "<bdi>signs</bdi> كوشينغية كلاسيكية"),
        ("ACTH 1.3 (2-11)", "<bdi>low</bdi> جدًا، يؤكد مصدر مستقل عن ACTH (كظري)"),
        ("5-cm right adrenal mass with\ncontrast washout at 10 minutes is 60%", "كتلة كظرية كبيرة مع نسبة انغسال <bdi>low</bdi>، ملامح تثير شك بالخباثة"),
    ],
    "why_correct": [
        "كتلة كظرية كبيرة (أكبر من 4 سم) مع نسبة انغسال تباين <bdi>low</bdi> (أقل من 60% بعد 10 دقائق تقريبًا يعتبر مقلق) تزيد احتمال الخباثة أو على الأقل تستدعي إزالة الكتلة بغض النظر.",
        "بما إنها مسؤولة أيضًا عن إفراز كورتيزول زائد يسبب <bdi>symptoms</bdi> و<bdi>diseases</bdi> واضحة (<bdi>diabetes</bdi> وضغط جديدين)، الاستئصال الجراحي (<bdi>surgical excision</bdi>) هو الـ<bdi>treatment</bdi> الأنسب لإزالة المصدر كليًا.",
        "الـ<bdi>treatment</bdi> الكيميائي والإشعاعي غير مناسبين كخط أول لكتلة كظرية موضعية قابلة للاستئصال، والميتوتان يستخدم أكثر لحالات سرطان كظري منتشر أو غير قابل للاستئصال الكامل.",
    ],
    "when_changes": [
        "لو كانت الكتلة صغيرة (أقل من 4 سم) بخصائص تصوير حميدة تمامًا وغير مفرزة، يمكن الاكتفاء بالمراقبة الدورية.",
        "لو كان الورم منتشر أو غير قابل للاستئصال الكامل عند الـ<bdi>diagnosis</bdi>، يصير الميتوتان أو الـ<bdi>treatment</bdi> الكيميائي خيار علاجي مساعد.",
    ],
    "rule": "كتلة كظرية كبيرة مفرزة للكورتيزول مع ملامح تصوير مقلقة تستأصل جراحيًا كخط <bdi>treatment</bdi> أول.",
    "comparison": None,
    "guideline_note": None,
},
663: {
    "idea": "رجل تشخص حديثًا ب<bdi>diabetes</bdi> النوع الثاني قبل 12 أسبوع وكان HbA1c <bdi>elevated</bdi> بوضوح عند الـ<bdi>diagnosis</bdi>، والتزم بنمط الحياة فقط، لكن سجل السكر اليومي لسا <bdi>elevated</bdi> فوق الهدف، والسؤال يبي أفضل إضافة دوائية.",
    "clues": [
        ("managed with lifestyle modifications", "جرب نمط الحياة فقط فترة كافية (12 أسبوع)"),
        ("НА 1C 8.5%", "<bdi>elevated</bdi> بوضوح عند الـ<bdi>diagnosis</bdi> قبل بدء تعديل نمط الحياة"),
        ("preprandial blood glucose 150 to 160 mg/dL", "لسا <bdi>elevated</bdi> فوق الهدف رغم الالتزام بنمط الحياة"),
    ],
    "why_correct": [
        "الـ<bdi>patient</bdi> جرب نمط الحياة فترة كافية (12 أسبوع) وسجل السكر لسا فوق الهدف بوضوح، فهذا يعني نمط الحياة وحده غير كافٍ الآن.",
        "الـ<bdi>step</bdi> العلاجية التالية القياسية هي إضافة <bdi>Metformin</bdi> كخط أول دوائي لل<bdi>diabetes</bdi> النوع الثاني، خصوصًا مع عدم وجود موانع مذكورة (وظائف كلى <bdi>normal</bdi>).",
        "الأدوية الأخرى (داباغليفلوزين، سيتاغليبتين، غليبيزايد) خيارات لاحقة أو إضافية تستخدم عادة بعد الـ<bdi>metformin</bdi> أو معه، مو كبديل أول عنه.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> عنده قصور كلوي <bdi>severe</bdi> يمنع الـ<bdi>metformin</bdi>، يصير اختيار دواء بديل من البداية ضروري.",
        "لو رجع HbA1c للهدف بنمط الحياة وحده، لا داعي لإضافة دواء بعد.",
    ],
    "rule": "بعد فشل نمط الحياة وحده بالوصول للهدف ب<bdi>diabetes</bdi> النوع الثاني، يضاف الـ<bdi>metformin</bdi> كخط أول دوائي.",
    "comparison": None,
    "guideline_note": None,
},
664: {
    "idea": "رجل <bdi>diabetes</bdi> نوع أول يعاني من هبوط سكر مطول أثناء الرياضة المكثفة رغم أكله وجبة قبلها، والسؤال يبي أفضل تعديل بجرعات الـ<bdi>insulin</bdi> أيام ممارسة الرياضة تحديدًا.",
    "clues": [
        ("prolonged hypoglycemia during intense exercise", "هبوط سكر مطول مرتبط بالرياضة تحديدًا"),
        ("despite eating a meal prior to the activity", "الأكل قبل الرياضة ما كان كافي لمنع الهبوط، يعني المشكلة بجرعة الـ<bdi>insulin</bdi> نفسها"),
        ("insulin glargine and insulin aspart", "نظام قاعدة وجرعات كامل، يحتاج تعديل جزء محدد منه أيام الرياضة"),
    ],
    "why_correct": [
        "الرياضة المكثفة تزيد حساسية الجسم لل<bdi>insulin</bdi> وتستهلك سكر أكثر، فجرعة الـ<bdi>insulin</bdi> السريع المعتادة قبل الوجبة تصير زايدة عن الحاجة أيام الرياضة.",
        "الحل الصحيح هو تقليل جرعة الـ<bdi>insulin</bdi> السريع (<bdi>insulin aspart</bdi>) قبل الوجبة اللي تسبق الرياضة، مع الاستمرار على نفس جرعة الـ<bdi>insulin</bdi> القاعدي (<bdi>glargine</bdi>) بدون تغيير.",
        "زيادة البروتين بالوجبة أو تغيير نوع النظام كليًا لا يعالجان المشكلة الأساسية بنفس الدقة والأمان مثل تعديل جرعة الـ<bdi>insulin</bdi> السريع المباشر المرتبط بالرياضة.",
    ],
    "when_changes": [
        "لو كان الهبوط يحصل بدون علاقة واضحة بالرياضة (أوقات عشوائية باليوم)، يصير التفكير بمراجعة كل الجرعات مو فقط جرعة الرياضة.",
        "لو كانت الرياضة <bdi>mild</bdi> قصيرة مو مكثفة، قد لا يحتاج تعديل كبير بالجرعة أصلًا.",
    ],
    "rule": "هبوط السكر المرتبط بالرياضة المكثفة يعالج بتقليل جرعة الـ<bdi>insulin</bdi> السريع قبل الرياضة، مع إبقاء الجرعة القاعدية ثابتة.",
    "comparison": None,
    "guideline_note": None,
},
665: {
    "idea": "رجل كبير بالسن عنده <bdi>symptoms</bdi> قصور درقية واضحة بعد <bdi>treatment</bdi> إشعاعي سابق للمنطقة (<bdi>factor</bdi> <bdi>risk</bdi> معروف ل<bdi>hypothyroidism</bdi> لاحقًا)، وTSH عنده عند الحد الأعلى الـ<bdi>normal</bdi> تمامًا (5.0)، والسؤال يبي أفضل فحص لتأكيد الـ<bdi>diagnosis</bdi> بدقة.",
    "clues": [
        ("Hodgkin lymphoma treated with radiation therapy 3 years\nago", "<bdi>treatment</bdi> إشعاعي سابق بالرقبة، <bdi>factor</bdi> <bdi>risk</bdi> معروف ل<bdi>hypothyroidism</bdi> اللاحق"),
        ("Thyroid-Stimulating Hormone 5.0 (0.4 - 5.0)", "بالحد الأعلى الـ<bdi>normal</bdi> تمامًا، <bdi>case</bdi> حدية تحتاج توضيح إضافي"),
        ("Sodium 129 (134-146)", "نقص صوديوم بسيط، يمكن أن يترافق مع قصور درقية"),
    ],
    "why_correct": [
        "TSH عند الحد الأعلى الـ<bdi>normal</bdi> بالضبط لا يحسم وجود قصور درقية واضح أو لا، فيحتاج فحص إضافي لتوضيح الصورة الكاملة.",
        "قياس <bdi>Free thyroxine (T4)</bdi> يوضح إذا كان القصور واضح (T4 <bdi>low</bdi>) أو تحت سريري فقط (T4 <bdi>normal</bdi> مع TSH حدي)، وهذا يغير قرار الـ<bdi>treatment</bdi>.",
        "إعادة TSH بعد 4 أسابيع فقط لا يضيف معلومة حاسمة الآن، وتصوير الغدة (موجات صوتية أو مسح) لا يفيد لتحديد الوظيفة الهرمونية نفسها.",
    ],
    "when_changes": [
        "لو كان T4 <bdi>low</bdi> فعلًا، يتأكد قصور درقية واضح ويبدأ الـ<bdi>treatment</bdi> بالليفوثيروكسين مباشرة.",
        "لو كان T4 <bdi>normal</bdi> تمامًا، يكون الـ<bdi>diagnosis</bdi> قصور درقية تحت سريري <bdi>mild</bdi> يحتاج قرار <bdi>treatment</bdi> حسب الـ<bdi>symptoms</bdi> والـ<bdi>factors</bdi> الأخرى.",
    ],
    "rule": "TSH عند الحد الحدي يحتاج قياس Free T4 لتحديد هل القصور واضح أو تحت سريري قبل اتخاذ قرار الـ<bdi>treatment</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
661: {
    "A": "المضادات الحيوية غير مبررة بدون دليل واضح على عدوى بكتيرية محددة عند هذا الـ<bdi>patient</bdi>.",
    "C": "البوتاسيوم <bdi>normal</bdi> حاليًا (4.4)، فلا حاجة لإضافته الآن، ويعاد تقييمه أثناء الـ<bdi>treatment</bdi> بالـ<bdi>insulin</bdi>.",
    "D": "البيكربونات الوريدي لا يستخدم بشكل روتيني بالحماض الكيتوني <bdi>diabetes</bdi> إلا بحالات حماض <bdi>severe</bdi> جدًا استثنائية.",
},
662: {
    "A": "الـ<bdi>treatment</bdi> الكيميائي غير مناسب كخط أول لكتلة كظرية موضعية قابلة للاستئصال الجراحي.",
    "C": "الميتوتان يستخدم أكثر لحالات سرطان كظري منتشر أو غير قابل للاستئصال الكامل، مو كخط أول هنا.",
    "D": "الـ<bdi>treatment</bdi> الإشعاعي ليس الخيار القياسي لكتلة كظرية موضعية قابلة للجراحة.",
},
663: {
    "A": "داباغليفلوزين دواء إضافي متقدم أكثر من اللازم كخط أول قبل تجربة الـ<bdi>metformin</bdi>.",
    "C": "سيتاغليبتين أيضًا خيار لاحق أو إضافي، مو الخط الأول المعتاد.",
    "D": "غليبيزايد (سلفونيل يوريا) دواء خط ثاني عادة وله <bdi>risk</bdi> هبوط سكر أعلى من الـ<bdi>metformin</bdi> كخيار أول.",
},
664: {
    "B": "زيادة البروتين بالوجبة لا تعالج المشكلة الأساسية بنفس فعالية تعديل جرعة الـ<bdi>insulin</bdi> السريع المباشرة.",
    "C": "التحول لنظام سلايدنق سكيل يعقد الأمر بدون داعٍ ولا يعالج المشكلة بنفس الدقة والبساطة.",
    "D": "إيقاف الـ<bdi>insulin</bdi> القاعدي (glargine) <bdi>risk</bdi> ويترك الـ<bdi>patient</bdi> بدون تغطية أساسية طول اليوم، وهذا مو الحل الصحيح لمشكلة مرتبطة بوقت الرياضة تحديدًا.",
},
665: {
    "A": "إعادة TSH بعد 4 أسابيع فقط لا تضيف معلومة حاسمة الآن مقارنة بقياس T4 مباشرة.",
    "C": "الموجات فوق الصوتية على الغدة تقيّم الشكل التشريحي فقط ولا توضح شدة القصور الوظيفي.",
    "D": "مسح اليود المشع يستخدم أكثر ل<bdi>assessment</bdi> فرط النشاط، مو لتوضيح شدة <bdi>hypothyroidism</bdi>.",
},
})

HIGHLIGHT_TERMS.update({
661: ["Intravenous 0.9% saline is initiated", "pH 7.10", "Potassium 4.4"],
662: ["moon like face, dorsocervical fat pad", "ACTH 1.3", "60%"],
663: ["managed with lifestyle modifications", "preprandial blood glucose 150 to 160 mg/dL"],
664: ["hypoglycemia during intense exercise", "despite eating a meal prior to the activity"],
665: ["Hodgkin lymphoma treated with radiation therapy 3 years", "Sodium 129"],
})

EXPLANATIONS.update({
666: {
    "idea": "امرأة راح تستأصل غدة كظرية جراحيًا ب<bdi>cause</bdi> كوشينغ مستقل عن ACTH (ورم كظري حميد مفرز للكورتيزول)، والسؤال يبي أهم <bdi>procedure</bdi> وقائي حول وقت العملية.",
    "clues": [
        ("elective adrenalectomy for non-ACTH\ndependent Cushing syndrome", "استئصال كظر مخطط له لكوشينغ من مصدر كظري"),
        ("benign right adrenal adenoma", "ورم حميد يفرز كورتيزول زائد لفترة طويلة"),
    ],
    "why_correct": [
        "الورم الكظري المفرز للكورتيزول لفترة طويلة يكبت الغدة الكظرية الأخرى (السليمة) وأيضًا يكبت محور ACTH النخامي بالكامل عبر التغذية الراجعة.",
        "بعد استئصال الورم، الجسم يفتقد فجأة مصدر الكورتيزول (لا الورم ولا الغدة الأخرى المكبوتة تقدر تنتج كفاية فورًا)، فيحتاج تغطية بـ<bdi>hydrocortisone</bdi> قبل وأثناء وبعد العملية مباشرة لتجنب أزمة كظرية <bdi>acute</bdi>.",
        "الفلودروكورتيزون والميتوتان يستخدمان بسياقات مختلفة (قصور كظري دائم أو سرطان كظري)، مو ك<bdi>procedure</bdi> وقائي روتيني حول عملية استئصال ورم حميد واحد.",
    ],
    "when_changes": [
        "لو كان الاستئصال لكلا الغدتين الكظريتين معًا، يحتاج الـ<bdi>patient</bdi> تعويض ستيرويد دائم مدى الحياة (كورتيزول وفلودروكورتيزون) بعد العملية.",
        "لو كان الورم غير مفرز للكورتيزول أصلًا، لا يحتاج نفس درجة التغطية الستيرويدية المحيطة بالعملية.",
    ],
    "rule": "استئصال ورم كظري مفرز للكورتيزول يحتاج تغطية بالهيدروكورتيزون حول وقت العملية لتجنب أزمة كظرية من كبت الغدة الأخرى والمحور النخامي.",
    "comparison": None,
    "guideline_note": None,
},
667: {
    "idea": "امرأة حامل معروف عندها قصور درقية على جرعة ثابتة من الليفوثيروكسين، وTSH عندها بالحد الأعلى الـ<bdi>normal</bdi> غير الحملي مع T4 <bdi>low</bdi> حدي، والسؤال يبي التعديل الصحيح بالجرعة أثناء الحمل.",
    "clues": [
        ("first prenatal visit", "بداية <bdi>follow-up</bdi> الحمل، وقت مهم لمراجعة جرعة الثيروكسين"),
        ("Thyroid-Stimulating Hormone 4.4 (0.4 - 5.0)", "ضمن الـ<bdi>normal</bdi> لغير الحوامل بس أعلى من الهدف الموصى به بالحمل"),
        ("Thyroxine (T4 free serum) 9.5 (8.5 - 15.2)", "<bdi>low</bdi> حدي، يدعم عدم كفاية الجرعة الحالية للحمل"),
    ],
    "why_correct": [
        "احتياج الجسم من هرمون الدرقية يزيد بشكل كبير أثناء الحمل (حوالي 30-50%) ب<bdi>cause</bdi> زيادة بروتين حامل الهرمون وحاجة الجنين.",
        "الهدف الموصى به لـTSH أثناء الحمل أقل من المعتاد لغير الحوامل، فمستوى 4.4 مع T4 <bdi>low</bdi> حدي يعتبر غير كافٍ لحمل صحي، ويحتاج زيادة الجرعة.",
        "الاستمرار على نفس الجرعة أو تنقيصها أو إيقافها كلها تعرض الأم والجنين ل<bdi>risk</bdi> قصور درقية غير مصحح أثناء الحمل.",
    ],
    "when_changes": [
        "لو كان TSH <bdi>low</bdi> جدًا مع T4 <bdi>elevated</bdi> (فرط جرعة)، يصير تنقيص الجرعة هو الصحيح بدل زيادتها.",
        "بعد الولادة، تحتاج الجرعة مراجعة ورجوع تدريجي للجرعة السابقة للحمل غالبًا.",
    ],
    "rule": "أثناء الحمل، تحتاج المرأة المصابة بقصور درقية زيادة جرعة الليفوثيروكسين للوصول لهدف TSH أقل من المعتاد لغير الحوامل.",
    "comparison": None,
    "guideline_note": None,
},
668: {
    "idea": "رجل مصاب ب<bdi>diabetes</bdi> نوع ثاني دخل المستشفى ب<bdi>cause</bdi> ألم صدر وله <bdi>disease</bdi> شرايين تاجي، وHbA1c <bdi>elevated</bdi> وسكر الدم متذبذب بالمستشفى، والسؤال يبي أفضل نظام <bdi>insulin</bdi> أثناء الإقامة بالمستشفى.",
    "clues": [
        ("admitted to the hospital for evaluation of chest pain", "دخول مستشفى ب<bdi>disease</bdi> <bdi>acute</bdi>، سياق مختلف عن <bdi>management</bdi> <bdi>diabetes</bdi> بالمنزل"),
        ("HbA1C 8.5", "ضبط غير جيد قبل الدخول"),
        ("Plasma Glucose 9.4-14.9 mmol/L", "تذبذب <bdi>elevated</bdi> بسكر الدم أثناء الإقامة"),
    ],
    "why_correct": [
        "بالمرضى المقيمين بالمستشفى (خصوصًا ب<bdi>case</bdi> <bdi>acute</bdi> زي ألم صدر مع <bdi>disease</bdi> شرايين تاجي)، الإرشادات توصي بإيقاف الأدوية الفموية لل<bdi>diabetes</bdi> واستخدام الـ<bdi>insulin</bdi> لضبط دقيق وآمن.",
        "نظام <bdi>basal and prandial insulin</bdi> (قاعدة وجرعات) يعطي تحكم أفضل وأكثر استقرارًا بسكر الدم مقارنة بالسلايدنق سكيل وحده.",
        "الـ<bdi>metformin</bdi> يوقف بالمستشفى (<bdi>risk</bdi> حماض لبني ب<bdi>case</bdi> عدم استقرار أو احتمال تصوير بالصبغة)، والسلفونيل يوريا وسلايدنق سكيل وحده أقل فعالية وأمان من نظام القاعدة والجرعات.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> مستقر تمامًا بدون <bdi>disease</bdi> <bdi>acute</bdi> ومقيم لفترة قصيرة جدًا ل<bdi>procedure</bdi> بسيط، ممكن الاستمرار على أدويته الفموية المعتادة بحذر.",
        "بعد الخروج من المستشفى واستقرار الـ<bdi>case</bdi>، يعاد <bdi>assessment</bdi> الـ<bdi>treatment</bdi> للرجوع لنظامه المعتاد بالمنزل حسب ضبطه.",
    ],
    "rule": "المرضى المقيمين بالمستشفى ب<bdi>case</bdi> <bdi>acute</bdi> يفضل لهم نظام <bdi>insulin</bdi> قاعدة وجرعات بدل الأدوية الفموية أو السلايدنق سكيل وحده.",
    "comparison": None,
    "guideline_note": None,
},
669: {
    "idea": "امرأة شابة تشخصت بمتلازمة <bdi>loculation</bdi> المبايض تعاني من زيادة شعر ودورة غير منتظمة، وما تخطط للحمل حاليًا، والسؤال يبي أفضل <bdi>treatment</bdi> يعالج المشكلتين معًا.",
    "clues": [
        ("not planning for pregnancy at this time", "يسمح باستخدام <bdi>treatment</bdi> هرموني مانع للحمل"),
        ("mild hirsutism", "زيادة شعر <bdi>mild</bdi>، من <bdi>symptoms</bdi> <bdi>loculation</bdi> المبايض"),
        ("irregular menses", "اضطراب دورة، من <bdi>symptoms</bdi> <bdi>loculation</bdi> المبايض الأساسية"),
    ],
    "why_correct": [
        "حبوب منع الحمل المركبة (<bdi>combined oral contraceptive pills</bdi>) تعالج مشكلتين معًا: تنظم الدورة الشهرية وتقلل الأندروجينات المسؤولة عن زيادة الشعر.",
        "هذا الخيار مناسب جدًا ل<bdi>patient</bdi> ما تخطط للحمل حاليًا وتبي <bdi>treatment</bdi> شامل لل<bdi>symptoms</bdi> الهرمونية.",
        "الـ<bdi>metformin</bdi> يفيد أكثر لتحسين حساسية الـ<bdi>insulin</bdi> وقد يساعد بالخصوبة مستقبلًا، والـ<bdi>spironolactone</bdi> يعالج زيادة الشعر بس ما ينظم الدورة لوحده ويحتاج غالبًا يترافق مع منع حمل فعال لخطره على الجنين لو حصل حمل.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>patient</bdi> تخطط للحمل قريبًا، يصير الـ<bdi>metformin</bdi> أو تحفيز التبويض هو التركيز العلاجي بدل حبوب منع الحمل.",
        "لو كان الشعر الزائد <bdi>severe</bdi> جدًا ومقاوم لحبوب منع الحمل وحدها، يضاف الـ<bdi>spironolactone</bdi> ك<bdi>treatment</bdi> مساعد مع تأكيد منع الحمل الفعال.",
    ],
    "rule": "ب<bdi>patient</bdi> <bdi>loculation</bdi> المبايض غير الراغبة بالحمل حاليًا، حبوب منع الحمل المركبة هي الخيار الأول ل<bdi>treatment</bdi> اضطراب الدورة وزيادة الشعر معًا.",
    "comparison": None,
    "guideline_note": None,
},
670: {
    "idea": "رجل <bdi>diabetes</bdi> طويل الأمد ومسيطر عليه بشكل ممتاز حاليًا، عنده اعتلال أعصاب طرفي مؤلم (حرقان بالقدمين يزيد ليلًا)، والسؤال يبي أفضل <bdi>treatment</bdi> للألم العصبي نفسه بعد ما السيطرة على السكر أصلًا جيدة.",
    "clues": [
        ("bilateral burning<br>sensation in his feet", "ألم عصبي حارق نموذجي ل<bdi>neuropathy</bdi> <bdi>diabetes</bdi>"),
        ("worsens at night", "نمط الألم العصبي الليلي الكلاسيكي"),
        ("haemoglobin Ac levels have\nremained less than 7.0%", "سيطرة سكرية ممتازة حاليًا، تستبعد الحاجة لتشديد الضبط كحل أساسي للألم"),
        ("distal symmetrical polyneuropathy", "تأكيد <bdi>diagnosis</bdi> <bdi>neuropathy</bdi> الطرفي المتناظر"),
    ],
    "why_correct": [
        "بما إن السيطرة على السكر ممتازة أصلًا (أقل من 7%)، تشديدها أكثر ما راح يحل الألم العصبي الموجود فعلًا، فالتركيز يكون على <bdi>treatment</bdi> الألم نفسه.",
        "مضادات <bdi>depression</bdi> ثلاثية الحلقات مثل <bdi>Amitriptyline</bdi> من الخط الأول المثبت ل<bdi>treatment</bdi> الألم العصبي <bdi>diabetes</bdi>، خصوصًا اللي يسوء ليلًا.",
        "الـ<bdi>treatment</bdi> الـ<bdi>normal</bdi> وفيتامين B12 ما يعالجان الألم العصبي <bdi>diabetes</bdi> النموذجي هنا بدون دليل نقص B12 موثق، وهذا يجعلهم أقل ملاءمة من أميتريبتيلين المباشر للألم.",
    ],
    "when_changes": [
        "لو كان ضبط السكر سيء (HbA1c <bdi>elevated</bdi>)، يصير تحسين الضبط جزء أساسي من الخطة بجانب <bdi>treatment</bdi> الألم.",
        "لو فشل أميتريبتيلين أو كانت له <bdi>symptoms</bdi> جانبية غير محتملة، تصير أدوية بديلة مثل غابابنتين أو بريغابالين خيار تالٍ.",
    ],
    "rule": "الألم العصبي <bdi>diabetes</bdi> رغم ضبط سكر ممتاز يعالج بمضادات <bdi>depression</bdi> ثلاثية الحلقات مثل أميتريبتيلين كخط أول.",
    "comparison": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
666: {
    "A": "الميتوتان دواء ل<bdi>treatment</bdi> سرطان الكظر أو حالات خاصة، مو <bdi>procedure</bdi> وقائي روتيني حول عملية ورم حميد.",
    "C": "الفلودروكورتيزون يستخدم بقصور كظري أولي دائم (زي أديسون)، مو ك<bdi>procedure</bdi> وقائي روتيني حول استئصال ورم كظري واحد.",
    "D": "فينوكسي بنزامين يستخدم قبل جراحة الفيوكروموسايتوما تحديدًا، لا علاقة له بورم مفرز للكورتيزول.",
},
667: {
    "B": "الاستمرار على نفس الجرعة غير كافٍ لأن الاحتياج يزيد أثناء الحمل والمستوى الحالي حدي <bdi>low</bdi>.",
    "C": "تنقيص الجرعة خطأ تمامًا لأن الـ<bdi>patient</bdi> تحتاج جرعة أعلى أثناء الحمل لا أقل.",
    "D": "إيقاف الجرعة كليًا <bdi>risk</bdi> جدًا ويعرض الأم والجنين لقصور درقية غير مصحح.",
},
668: {
    "A": "غليبيزايد (سلفونيل يوريا) غير مفضل بالمرضى الحادين المقيمين بالمستشفى ب<bdi>cause</bdi> <bdi>risk</bdi> هبوط سكر غير متوقع.",
    "B": "الـ<bdi>metformin</bdi> يوقف عادة بالمستشفى ب<bdi>case</bdi> <bdi>acute</bdi> ل<bdi>risk</bdi> الحماض اللبني أو احتمال <bdi>procedure</bdi> تصوير بالصبغة.",
    "C": "السلايدنق سكيل وحده أقل فعالية واستقرارًا من نظام القاعدة والجرعات المتكامل.",
},
669: {
    "A": "الـ<bdi>metformin</bdi> يحسن حساسية الـ<bdi>insulin</bdi> بس لا ينظم الدورة أو يقلل الشعر بنفس فعالية حبوب منع الحمل المركبة.",
    "B": "الـ<bdi>spironolactone</bdi> يعالج زيادة الشعر بس لا ينظم الدورة الشهرية لوحده وله <bdi>risk</bdi> على الجنين لو حصل حمل بدون منع فعال.",
    "D": "اللولب الهرموني ينظم الدورة موضعيًا بس ما يعالج زيادة الشعر (الأندروجينات الجهازية) بنفس فعالية حبوب منع الحمل المركبة.",
},
670: {
    "B": "الـ<bdi>treatment</bdi> الـ<bdi>normal</bdi> لا يعالج الألم العصبي <bdi>diabetes</bdi> النموذجي بنفس فعالية الأدوية المثبتة لهذا النوع من الألم.",
    "C": "تشديد ضبط السكر أكثر لن يحل الألم العصبي الموجود فعلًا لأن الضبط ممتاز أصلًا.",
    "D": "فيتامين B12 يفيد لو فيه نقص موثق فقط، ولا دليل هنا على نقصه عند هذا الـ<bdi>patient</bdi>.",
},
})

HIGHLIGHT_TERMS.update({
666: ["elective adrenalectomy for non-ACTH", "right adrenal adenoma"],
667: ["first prenatal visit", "Thyroid-Stimulating Hormone 4.4", "Thyroxine (T4 free serum) 9.5"],
668: ["admitted to the hospital for evaluation of chest pain", "HbA1C 8.5"],
669: ["not planning for pregnancy at this time", "mild hirsutism", "irregular menses"],
670: ["worsens at night", "distal symmetrical polyneuropathy"],
})

EXPLANATIONS.update({
671: {
    "idea": "امرأة عندها ثر لبني وتعب وصداع ودورة غير منتظمة، والتحاليل تظهر قصور درقية أولي واضح (TSH <bdi>elevated</bdi>) مع <bdi>prolactin</bdi> <bdi>elevated</bdi> بشكل معتدل يفسر على الأغلب بأثر القصور الدرقي نفسه، فالسؤال يبي الـ<bdi>treatment</bdi> الأنسب.",
    "clues": [
        ("galactorrhea, worsening fatigue, malaise", "ثر لبني وتعب، <bdi>symptoms</bdi> تتوافق مع قصور درقية وفرط <bdi>prolactin</bdi> معًا"),
        ("Thyroid-Stimulating Hormone 16 (0.4 - 5.0)", "ارتفاع واضح بالـTSH، قصور درقية أولي حقيقي"),
        ("Prolactin 1000", "ارتفاع معتدل بالـ<bdi>prolactin</bdi>، ضمن المدى المتوقع كأثر ثانوي ل<bdi>hypothyroidism</bdi> الـ<bdi>severe</bdi>"),
        ("Human chorionic gonadotropin 0.0", "يستبعد الحمل ك<bdi>cause</bdi> لهذي الـ<bdi>symptoms</bdi>"),
    ],
    "why_correct": [
        "<bdi>hypothyroidism</bdi> الأولي الـ<bdi>severe</bdi> يرفع هرمون TRH، وهذا الهرمون يحفز أيضًا إفراز الـ<bdi>prolactin</bdi> من الغدة النخامية، فيسبب ارتفاع <bdi>prolactin</bdi> ثانوي معتدل.",
        "<bdi>treatment</bdi> الـ<bdi>cause</bdi> الأساسي بـ<bdi>levothyroxine</bdi> يصحح <bdi>hypothyroidism</bdi>، وغالبًا يرجع الـ<bdi>prolactin</bdi> لطبيعته تلقائيًا بدون حاجة ل<bdi>treatment</bdi> مباشر لل<bdi>prolactin</bdi> نفسه.",
        "البدء مباشرة بناهض <bdi>dopamine</bdi> أو تصوير النخامية سابق لأوانه قبل ما نعالج الـ<bdi>cause</bdi> الواضح (<bdi>hypothyroidism</bdi>) ونشوف استجابة الـ<bdi>prolactin</bdi> له أولًا.",
    ],
    "when_changes": [
        "لو ما رجع الـ<bdi>prolactin</bdi> لطبيعته بعد تصحيح وظائف الدرقية بشكل كامل، عندها يصير تصوير النخامية بالرنين المغناطيسي منطقي لاستبعاد ورم حقيقي.",
        "لو كان TSH <bdi>normal</bdi> من البداية مع <bdi>prolactin</bdi> <bdi>elevated</bdi> جدًا جدًا، يصير الشك بورم نخامي مفرز لل<bdi>prolactin</bdi> أقوى من البداية.",
    ],
    "rule": "<bdi>hypothyroidism</bdi> الأولي الـ<bdi>severe</bdi> قد يسبب ارتفاع <bdi>prolactin</bdi> ثانوي معتدل، و<bdi>treatment</bdi> الـ<bdi>cause</bdi> الأساسي (الليفوثيروكسين) هو الـ<bdi>step</bdi> الصحيحة الأولى.",
    "comparison": None,
    "guideline_note": None,
},
672: {
    "idea": "شابة <bdi>diabetes</bdi> نوع أول حديث الـ<bdi>diagnosis</bdi>، ضبطها صار ممتاز جدًا (قريب من الـ<bdi>normal</bdi>) وصارت تعاني هبوط سكر متكرر صائم وبعد الأكل، والسؤال يبي أفضل تعديل بجرعات الـ<bdi>insulin</bdi>.",
    "clues": [
        ("episodes of both fasting and postprandial hypoglycemia", "هبوط سكر متكرر بأوقات مختلفة من اليوم، يدل على زيادة عامة بجرعات الـ<bdi>insulin</bdi>"),
        ("НА1С 6.0", "ضبط قريب جدًا من الـ<bdi>normal</bdi>، أقرب من الهدف المعتاد ل<bdi>diabetes</bdi> نوع أول"),
        ("Random Glucose 4.5", "سكر <bdi>low</bdi> نسبيًا وقت الفحص، يدعم فرط جرعة الـ<bdi>insulin</bdi>"),
    ],
    "why_correct": [
        "هبوط السكر يحصل بأوقات مختلفة (صائم وبعد الأكل معًا)، وهذا يدل إن كل مكونات نظام الـ<bdi>insulin</bdi> (القاعدي والسريع) زايدة عن حاجتها الحالية.",
        "الحل الصحيح هو تقليل كل من <bdi>insulin glargine</bdi> (القاعدي) و<bdi>insulin aspart</bdi> (السريع) معًا، مو تعديل واحد منهم فقط.",
        "الاستمرار على نفس الجرعات أو إيقاف أحدهما كليًا لا يعالج مشكلة الهبوط المتكرر بأمان ودقة مثل تخفيض الجرعتين تدريجيًا.",
    ],
    "when_changes": [
        "لو كان الهبوط مرتبط بوقت محدد فقط (مثلًا بعد الرياضة)، يكفي تعديل جزء محدد من الجرعة مرتبط بذاك الوقت فقط.",
        "لو كان الهبوط صائم فقط بدون بعد الأكل، يصير تقليل الـ<bdi>insulin</bdi> القاعدي وحده هو الأنسب.",
    ],
    "rule": "هبوط السكر المتكرر بأوقات مختلفة من اليوم عند <bdi>patient</bdi> <bdi>diabetes</bdi> نوع أول يعالج بتقليل كل من الـ<bdi>insulin</bdi> القاعدي والسريع معًا.",
    "comparison": None,
    "guideline_note": None,
},
673: {
    "idea": "رجل عنده ضعف رغبة جنسية وضعف انتصاب <bdi>severe</bdi> وغياب انتصاب الصباح، وتحاليله تظهر قصور غدد تناسلية ثانوي (تستوستيرون <bdi>low</bdi> مع FSH وLH منخفضين) ب<bdi>cause</bdi> ورم نخامي صغير مفرز لل<bdi>prolactin</bdi>، وهو ووزوجته يبون يحملون، فالسؤال يبي أفضل <bdi>treatment</bdi> يحفظ الخصوبة.",
    "clues": [
        ("would like to conceive", "يبي <bdi>treatment</bdi> يحافظ على أو يحسن الخصوبة، مو يثبطها أكثر"),
        ("Testosterone 4.2 (10.4-41.6)", "تستوستيرون <bdi>low</bdi> جدًا"),
        ("Follicle-stimulating hormone 1.2", "<bdi>low</bdi>، قصور غدد تناسلية ثانوي (نخامي المنشأ)"),
        ("Prolactin 1500", "ارتفاع واضح بالـ<bdi>prolactin</bdi>، الـ<bdi>cause</bdi> الأرجح لقصور الغدد التناسلية"),
        ("0.8-cm anterior pituitary mass consistent with an adenoma", "ورم صغير (ميكروأدينوما) يفسر ارتفاع الـ<bdi>prolactin</bdi>"),
    ],
    "why_correct": [
        "ارتفاع الـ<bdi>prolactin</bdi> يثبط محور الغدد التناسلية (FSH وLH) مباشرة، وهذا هو <bdi>cause</bdi> قصور الخصوبة والانتصاب عند هذا الـ<bdi>patient</bdi>.",
        "ناهض الـ<bdi>dopamine</bdi> <bdi>Cabergoline</bdi> يخفض الـ<bdi>prolactin</bdi> ويقلص الورم، وهذا يرجع محور الغدد التناسلية للعمل الـ<bdi>normal</bdi> ويحسن فرصة الحمل الـ<bdi>normal</bdi>.",
        "التستوستيرون البديل يحسن الـ<bdi>symptoms</bdi> الجنسية بس يثبط محور الغدد التناسلية أكثر ويقلل إنتاج الحيوانات المنوية، وهذا عكس هدف الـ<bdi>patient</bdi> بتحقيق حمل <bdi>normal</bdi>.",
    ],
    "when_changes": [
        "لو ما كان الـ<bdi>patient</bdi> والزوجة يخططون للحمل، ممكن يكون التستوستيرون البديل خيار مقبول لتحسين الـ<bdi>symptoms</bdi> فقط.",
        "لو فشل الـ<bdi>treatment</bdi> بناهض الـ<bdi>dopamine</bdi> بالسيطرة على الورم، يصير التفكير بالجراحة خيار تالٍ.",
    ],
    "rule": "بروﻻكتينوما تسبب قصور خصوبة يعالج بناهض الـ<bdi>dopamine</bdi> لأنه يعالج الـ<bdi>cause</bdi> ويحسن الخصوبة، بعكس التستوستيرون البديل اللي يزيد كبت الخصوبة.",
    "comparison": None,
    "guideline_note": None,
},
674: {
    "idea": "<bdi>patient</bdi> بالعناية المركزة بإنتان <bdi>severe</bdi>، والسؤال يبي النمط النموذجي لاضطراب وظائف الدرقية ب<bdi>case</bdi> الـ<bdi>disease</bdi> الحرج الـ<bdi>severe</bdi> (sick euthyroid) من ناحية T3 وT4 والـreverse T3.",
    "clues": [
        ("septicaemia due to<br>severe urinary tract infection", "<bdi>disease</bdi> حرج <bdi>severe</bdi>، سياق نموذجي للمتلازمة اليوثيرويدية الـ<bdi>patient</bdi>"),
        ("non-thyroidal illness or sick euthyroid state", "تحديد مباشر لل<bdi>case</bdi> المطلوب معرفة نمطها"),
    ],
    "why_correct": [
        "بالـ<bdi>disease</bdi> الحرج، يقل تحويل T4 إلى T3 النشط ويزيد تحويله لـ<bdi>reverse T3</bdi> غير النشط، فينخفض T3 وT4 بينما يرتفع الـreverse T3.",
        "هذا النمط (T3 وT4 منخفضين مع reverse T3 <bdi>elevated</bdi>) هو البصمة الكلاسيكية لمتلازمة sick euthyroid.",
        "TSH عادة يبقى <bdi>normal</bdi> أو <bdi>low</bdi> بسيط بهذي الـ<bdi>case</bdi>، مو <bdi>elevated</bdi>، وهذا يميزها عن <bdi>hypothyroidism</bdi> الأولي الحقيقي.",
    ],
    "when_changes": [
        "لو كان TSH <bdi>elevated</bdi> بوضوح مع T4 <bdi>low</bdi>، يصير الـ<bdi>diagnosis</bdi> قصور درقية أولي حقيقي بدل متلازمة الـ<bdi>disease</bdi> الحرج.",
        "بعد شفاء الـ<bdi>patient</bdi> من الـ<bdi>disease</bdi> الحرج، ترجع قيم الدرقية تدريجيًا لطبيعتها بدون حاجة ل<bdi>treatment</bdi> هرموني.",
    ],
    "rule": "متلازمة sick euthyroid تتميز بانخفاض T3 وT4 مع ارتفاع reverse T3، وTSH <bdi>normal</bdi> أو <bdi>low</bdi> بسيط.",
    "comparison": None,
    "guideline_note": None,
},
675: {
    "idea": "شاب عنده <bdi>Graves' disease</bdi> مع اعتلال عيني نشط (احمرار، حرقان، ألم بحركة العين، جحوظ وسحب جفن)، والسؤال يبي أهم <bdi>factor</bdi> <bdi>risk</bdi> معروف لتطور اعتلال عيني <bdi>Graves' disease</bdi> الـ<bdi>severe</bdi>.",
    "clues": [
        ("redness and grittiness of eyes, with painful eye<br>movements", "<bdi>symptoms</bdi> اعتلال عيني نشط مرافق ل<bdi>Graves' disease</bdi>"),
        ("proposis, and lid retraction", "<bdi>signs</bdi> جحوظ وسحب جفن كلاسيكية لاعتلال <bdi>Graves' disease</bdi> العيني"),
    ],
    "why_correct": [
        "التدخين (<bdi>Smoking</bdi>) هو أقوى <bdi>factor</bdi> <bdi>risk</bdi> قابل للتعديل ومثبت جيدًا لتطور اعتلال عيني <bdi>Graves' disease</bdi> الـ<bdi>severe</bdi> وزيادة شدته وسوء استجابته لل<bdi>treatment</bdi>.",
        "التدخين يزيد الالتهاب المناعي خلف العين ويقلل استجابة الـ<bdi>treatment</bdi> المناعي أو الإشعاعي المستخدم ل<bdi>retinopathy</bdi>.",
        "عدم الاستجابة للثيوناميدات، مستويات T4 وT3، أو الجنس الذكري <bdi>factors</bdi> أقل أهمية وأقل ثباتًا ك<bdi>factor</bdi> <bdi>risk</bdi> رئيسي مقارنة بالتدخين.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> غير مدخن أبدًا، يقل احتمال شدة <bdi>retinopathy</bdi> بشكل عام مقارنة بالمدخنين.",
        "الإقلاع عن التدخين يعتبر جزء أساسي من <bdi>management</bdi> اعتلال عيني <bdi>Graves' disease</bdi> لتقليل شدته وتحسين الاستجابة لل<bdi>treatment</bdi>.",
    ],
    "rule": "التدخين هو أهم <bdi>factor</bdi> <bdi>risk</bdi> قابل للتعديل لتطور وشدة اعتلال عيني <bdi>Graves' disease</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
671: {
    "A": "ناهض الـ<bdi>dopamine</bdi> خيار لبروﻻكتينوما حقيقية أولية، مو الـ<bdi>step</bdi> الأولى هنا مع <bdi>cause</bdi> أرجح (<bdi>hypothyroidism</bdi>) لم يعالج بعد.",
    "C": "تصوير النخامية سابق لأوانه قبل تصحيح <bdi>hypothyroidism</bdi> ومشاهدة استجابة الـ<bdi>prolactin</bdi> له.",
    "D": "المراقبة فقط لمدة 6 أشهر تؤخر <bdi>treatment</bdi> قصور درقية واضح وعرضي يحتاج تصحيح فوري.",
},
672: {
    "B": "الاستمرار على نفس الجرعات يديم مشكلة هبوط السكر المتكرر الموجودة فعلًا.",
    "C": "إيقاف كل الـ<bdi>insulin</bdi> <bdi>risk</bdi> جدًا ب<bdi>patient</bdi> <bdi>diabetes</bdi> نوع أول تحتاج <bdi>insulin</bdi> دائم للحياة.",
    "D": "إيقاف الـ<bdi>insulin</bdi> القاعدي كليًا وتحويل السريع لسلايدنق سكيل يترك فجوة تغطية خطيرة بين الوجبات وبالليل.",
},
673: {
    "A": "التستوستيرون البديل يحسن الـ<bdi>symptoms</bdi> بس يثبط الخصوبة أكثر، عكس هدف الـ<bdi>patient</bdi> بالحمل الـ<bdi>normal</bdi>.",
    "B": "كلوميفين سيترات يستخدم أكثر لتحفيز التبويض عند النساء، وليس الـ<bdi>treatment</bdi> الموجه ل<bdi>cause</bdi> المشكلة هنا (ورم مفرز لل<bdi>prolactin</bdi>).",
    "D": "السيلدينافيل يحسن الانتصاب بس لا يعالج الـ<bdi>cause</bdi> الهرموني الأساسي ولا يحسن الخصوبة.",
},
674: {
    "A": "ارتفاع T3 وT4 مع انخفاض reverse T3 عكس الصورة النموذجية لمتلازمة الـ<bdi>disease</bdi> الحرج تمامًا.",
    "B": "ارتفاع الثلاثة معًا غير متوافق مع الآلية الفسيولوجية المعروفة لمتلازمة sick euthyroid.",
    "D": "reverse T3 يرتفع لا يبقى <bdi>normal</bdi> بهذي المتلازمة، وهذا جزء أساسي من الآلية الفسيولوجية المعروفة.",
},
675: {
    "A": "عدم الاستجابة للثيوناميدات <bdi>factor</bdi> أقل ثباتًا وأهمية ك<bdi>factor</bdi> <bdi>risk</bdi> رئيسي مقارنة بالتدخين.",
    "B": "مستويات T4 وT3 لا تعتبر من <bdi>factors</bdi> الـ<bdi>risk</bdi> الرئيسية المثبتة لشدة <bdi>retinopathy</bdi> مقارنة بالتدخين.",
    "C": "الجنس الذكري ليس <bdi>factor</bdi> الـ<bdi>risk</bdi> الأقوى أو الأكثر ثباتًا مقارنة بالتدخين المثبت جيدًا بالدراسات.",
},
})

HIGHLIGHT_TERMS.update({
671: ["galactorrhea, worsening fatigue, malaise", "Thyroid-Stimulating Hormone 16", "Prolactin 1000"],
672: ["episodes of both fasting and postprandial hypoglycemia", "НА1С 6.0", "Random Glucose 4.5"],
673: ["would like to conceive", "Testosterone 4.2", "0.8-cm anterior pituitary mass consistent with an adenoma"],
674: ["non-thyroidal iliness or sick euthyroid state"],
675: ["proposis, and lid retraction"],
})

EXPLANATIONS.update({
676: {
    "idea": "امرأة اكتشفت عندها كتلة كظرية صغيرة صدفة أثناء تصوير ل<bdi>cause</bdi> ثاني، والسؤال يبي أكثر <bdi>cause</bdi> شائع لهذي الكتل الكظرية العرضية بشكل عام.",
    "clues": [
        ("incidentally found to have a 2-cm left adrenal gland mass", "اكتشاف صدفة بدون <bdi>symptoms</bdi> موجهة للكظر"),
        ("CT of the abdomen to investigate the cause of her pelvic pain", "<bdi>cause</bdi> التصوير غير متعلق بالكظر أصلًا، يؤكد الطبيعة العرضية للاكتشاف"),
    ],
    "why_correct": [
        "أغلب الكتل الكظرية المكتشفة صدفة بالتصوير هي أورام حميدة غير مفرزة وظيفيًا (<bdi>non-functional adenoma</bdi>)، ولا تسبب <bdi>symptoms</bdi> أو اضطراب هرموني.",
        "هذا هو الـ<bdi>cause</bdi> الأشيع إحصائيًا مقارنة ب<bdi>causes</bdi> أخرى أقل شيوعًا زي كوشينغ تحت السريري أو كون أو سرطان الكظر.",
        "رغم كذا، كل كتلة كظرية عرضية تحتاج <bdi>assessment</bdi> هرموني بسيط لاستبعاد الإفراز الوظيفي الصامت قبل الجزم بأنها غير وظيفية.",
    ],
    "when_changes": [
        "لو كانت الكتلة كبيرة جدًا (أكبر من 4-6 سم) أو بملامح تصوير مشبوهة، يزيد احتمال الخباثة ويحتاج <bdi>assessment</bdi> أدق.",
        "لو ظهرت <bdi>symptoms</bdi> أو <bdi>signs</bdi> هرمونية واضحة (ضغط مقاوم، <bdi>case</bdi> كوشينغية)، يصير التفكير ب<bdi>cause</bdi> وظيفي محدد أقوى.",
    ],
    "rule": "أغلب الكتل الكظرية المكتشفة صدفة هي أورام حميدة غير وظيفية، وهذا أشيع <bdi>cause</bdi> إحصائيًا.",
    "comparison": None,
    "guideline_note": None,
},
677: {
    "idea": "امرأة اكتشف عندها ورم نخامي كبير نسبيًا (13 مم، ماكرو أدينوما) صدفة بدون <bdi>symptoms</bdi> هرمونية واضحة، والسؤال يبي أفضل <bdi>step</bdi> تالية بالـ<bdi>assessment</bdi>.",
    "clues": [
        ("incidentally detected to have a 13-mm pituitary macro-adenoma", "اكتشاف صدفة لورم نخامي بحجم يعتبر ماكرو أدينوما (أكبر من 10 مم)"),
        ("no history of any significant medical illness", "لا <bdi>symptoms</bdi> هرمونية واضحة سريريًا حاليًا"),
    ],
    "why_correct": [
        "أي ورم نخامي مكتشف صدفة (خصوصًا الماكرو أدينوما) يحتاج <bdi>assessment</bdi> كامل لوظيفة الغدة النخامية لاستبعاد إفراز هرموني زائد صامت أو قصور هرموني ناتج عن الضغط.",
        "فحص <bdi>Anterior pituitary hormone profile</bdi> يشمل قياس الـ<bdi>prolactin</bdi> وACTH وTSH وIGF-1 وغيرها لتحديد إذا كان الورم وظيفيًا أو لا، وهذا ضروري قبل أي قرار آخر.",
        "التحويل الجراحي المباشر أو الخروج من الـ<bdi>follow-up</bdi> كلاهما سابق لأوانه قبل معرفة الـ<bdi>case</bdi> الهرمونية الكاملة للورم، واختبار تحمل الـ<bdi>insulin</bdi> فحص متخصص يستخدم لاحقًا فقط عند الحاجة ل<bdi>assessment</bdi> قصور محور معين.",
    ],
    "when_changes": [
        "لو أظهر الـ<bdi>assessment</bdi> الهرموني ورم مفرز (مثل برولاكتينوما)، يوجه الـ<bdi>treatment</bdi> حسب نوع الإفراز (دوائي أو جراحي).",
        "لو كان الورم يضغط على التصالب البصري مع <bdi>symptoms</bdi> بصرية، يصير التحويل الجراحي أولوية أوضح بجانب الـ<bdi>assessment</bdi> الهرموني.",
    ],
    "rule": "أي ورم نخامي مكتشف صدفة يحتاج <bdi>assessment</bdi> كامل لوظيفة الغدة النخامية أولًا قبل أي قرار علاجي آخر.",
    "comparison": None,
    "guideline_note": None,
},
678: {
    "idea": "امرأة شابة عندها دوخة عند الوقوف ونقص وزن غير مقصود مع تصبغ جلد وندبة داكنة، صورة تدعم <bdi>disease</bdi> أديسون، والسؤال يبي الفحص التأكيدي الصحيح لنفس الـ<bdi>case</bdi> الكلاسيكية.",
    "clues": [
        ("dizziness and feeling light-headed", "هبوط ضغط وضعي محتمل، <bdi>sign</bdi> قصور كظري"),
        ("lost 5 kg", "نقص وزن غير مقصود"),
        ("started to turn very dark as well as generalized skin hyperpigmentation", "تصبغ جلد منتشر، <bdi>sign</bdi> مهمة لارتفاع ACTH بقصور كظري أولي"),
    ],
    "why_correct": [
        "الصورة الكاملة (دوخة وضعية، نقص وزن، تصبغ جلد منتشر) تدعم بقوة <bdi>diagnosis</bdi> <bdi>disease</bdi> أديسون (قصور كظري أولي).",
        "الفحص التأكيدي القياسي هو <bdi>Synacthen test (ACTH stimulation test)</bdi>، اللي يقيس استجابة الكظر لتحفيز خارجي بـACTH.",
        "فشل ارتفاع الكورتيزول بعد التحفيز يؤكد القصور الكظري الأولي، وهذا أدق من قياس الكورتيزول العشوائي وحده أو فحوصات تصويرية.",
    ],
    "when_changes": [
        "لو كان الشك بفرط كورتيزول بدل قصوره، يصير اختبار الكبت بالديكساميثازون <bdi>low</bdi> الجرعة هو الفحص المناسب بدل سيناكثين.",
        "بعد تأكيد القصور بسيناكثين، تحتاج فحوصات إضافية (أجسام مضادة كظرية) لتحديد الـ<bdi>cause</bdi> المناعي الذاتي غالبًا.",
    ],
    "rule": "الصورة الكلاسيكية لقصور الكظر الأولي تؤكد بـSynacthen test (اختبار تحفيز ACTH).",
    "comparison": None,
    "guideline_note": None,
},
679: {
    "idea": "السؤال يبي أي دواء من عائلة مثبطات DPP4 لا يحتاج تعديل جرعة عند وجود قصور كلوي، وهذي معلومة دوائية مباشرة تعتمد على طريقة إخراج كل دواء من الجسم.",
    "clues": [
        ("does not require any dose modification in renal disease", "يبحث عن الدواء اللي إخراجه غير كلوي بشكل أساسي"),
    ],
    "why_correct": [
        "<bdi>Linagliptin</bdi> يختلف عن باقي مثبطات DPP4 لأنه يُطرح بشكل أساسي عبر الجهاز الصفراوي والأمعاء، مو الكلى.",
        "هذا يعني إن تراكمه بالجسم لا يتأثر بشكل كبير بضعف وظائف الكلى، فلا يحتاج تعديل جرعة حتى بقصور كلوي متقدم.",
        "باقي مثبطات DPP4 (فيلداغليبتين، ساكساغليبتين، سيتاغليبتين) تُطرح بشكل أساسي عبر الكلى، فتحتاج تقليل جرعة مع تدهور وظائف الكلى.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> بوظائف كلى <bdi>normal</bdi>، كل مثبطات DPP4 تستخدم بجرعاتها القياسية بدون فرق يذكر.",
        "لو كان <bdi>renal failure</bdi> <bdi>severe</bdi> جدًا (غسيل كلوي)، لينالغليبتين يبقى الخيار الأسهل من ناحية الجرعة من بين هذي المجموعة.",
    ],
    "rule": "لينالغليبتين هو مثبط DPP4 الوحيد من بين هذي المجموعة اللي لا يحتاج تعديل جرعة بقصور الكلى، لأن إخراجه كبدي-صفراوي بشكل أساسي.",
    "comparison": {
        "headers": ["الدواء", "طريقة الإخراج الأساسية", "يحتاج تعديل بقصور الكلى؟"],
        "rows": [
            ["<bdi>Linagliptin</bdi>", "كبدي-صفراوي", "لا"],
            ["<bdi>Sitagliptin</bdi>", "كلوي", "نعم"],
            ["<bdi>Saxagliptin</bdi>", "كلوي", "نعم"],
            ["<bdi>Vildagliptin</bdi>", "كلوي", "نعم"],
        ],
    },
    "guideline_note": None,
},
680: {
    "idea": "امرأة تشخصت حديثًا بسرطان درقي حليمي، والسؤال يبي مثال على مهارة تواصل إيجابية أثناء شرح خطة الـ<bdi>treatment</bdi> لها.",
    "clues": [
        ("recently diagnosed with papillary thyroid carcinoma", "سياق <bdi>diagnosis</bdi> جديد يحتاج تواصل واضح وداعم"),
    ],
    "why_correct": [
        "طلب من الـ<bdi>patient</bdi> إنها تعيد شرح التعليمات (<bdi>teach-back method</bdi>) يتأكد الطبيب إنها فهمت المعلومة صح، وهذي من أهم مهارات التواصل الإيجابية بالطب.",
        "هذي الطريقة تكشف أي سوء فهم مبكرًا وتسمح بتوضيح إضافي قبل ما تخرج الـ<bdi>patient</bdi> من العيادة بمعلومة ناقصة أو خاطئة.",
        "باقي الخيارات (نسيان الشكر، مقاطعة الـ<bdi>patient</bdi>، عدم إخبارها بانتهاء الوقت) كلها سلوكيات سلبية تضعف التواصل وتزيد <bdi>anxiety</bdi> الـ<bdi>patient</bdi>.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>patient</bdi> تفهم بسرعة وتؤكد الفهم من نفسها، ممكن تختصر هذي الـ<bdi>step</bdi> بشكل بسيط بدون تكرار مطول.",
        "بمواقف الشرح المعقدة (خيارات <bdi>treatment</bdi> متعددة)، تصير طريقة إعادة الشرح أهم وأكثر فائدة.",
    ],
    "rule": "طلب إعادة الشرح من الـ<bdi>patient</bdi> (Teach-back) من أهم مهارات التواصل الإيجابية للتأكد من الفهم الصحيح.",
    "comparison": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
676: {
    "A": "كوشينغ تحت السريري <bdi>cause</bdi> حقيقي بس أقل شيوعًا من الورم غير الوظيفي ك<bdi>cause</bdi> للكتل الكظرية العرضية عمومًا.",
    "B": "سرطان قشرة الكظر نادر جدًا مقارنة بالورم الحميد غير الوظيفي ك<bdi>cause</bdi> لكتلة عرضية صغيرة.",
    "D": "متلازمة كون <bdi>cause</bdi> أقل شيوعًا بكثير من الورم غير الوظيفي ك<bdi>cause</bdi> عام للكتل الكظرية العرضية.",
},
677: {
    "B": "الخروج من الـ<bdi>follow-up</bdi> بدون <bdi>assessment</bdi> هرموني كامل غير مناسب لورم نخامي بهذا الحجم (ماكرو أدينوما).",
    "C": "التحويل الجراحي المباشر سابق لأوانه قبل معرفة الـ<bdi>case</bdi> الهرمونية الكاملة للورم ووجود <bdi>symptoms</bdi> ضغط فعلية.",
    "D": "اختبار تحمل الـ<bdi>insulin</bdi> فحص متخصص يستخدم لاحقًا فقط ل<bdi>assessment</bdi> قصور محور معين، مو الـ<bdi>step</bdi> الأولى الشاملة.",
},
678: {
    "B": "أشعة البطن لا تؤكد الـ<bdi>diagnosis</bdi> الوظيفي للقصور الكظري، فقط تفيد لاحقًا بتحديد الـ<bdi>cause</bdi> التشريحي إن وجد.",
    "C": "اختبار الكبت بالديكساميثازون يستخدم ل<bdi>diagnosis</bdi> فرط الكورتيزول (كوشينغ) مو قصوره.",
    "D": "قياس الكورتيزول الصباحي العشوائي وحده أقل دقة من اختبار التحفيز لتأكيد القصور الكظري.",
},
679: {
    "A": "فيلداغليبتين يُطرح بشكل أساسي عبر الكلى ويحتاج تعديل جرعة بقصور الكلى.",
    "C": "ساكساغليبتين أيضًا يحتاج تعديل جرعة مع تدهور وظائف الكلى.",
    "D": "سيتاغليبتين من أكثر مثبطات DPP4 حاجة لتعديل جرعة واضح حسب درجة <bdi>renal failure</bdi>.",
},
680: {
    "A": "نسيان الشكر سلوك سلبي بسيط بس لا يعتبر مهارة تواصل إيجابية.",
    "C": "مقاطعة الـ<bdi>patient</bdi> أثناء سؤالها سلوك سلبي يضعف التواصل ويزيد شعورها بعدم الاهتمام.",
    "D": "إخبار الـ<bdi>patient</bdi> المفاجئ بانتهاء الوقت بدون تمهيد سلوك سلبي يزيد <bdi>anxiety</bdi> الـ<bdi>patient</bdi> وشعورها بالإهمال.",
},
})

HIGHLIGHT_TERMS.update({
676: ["incidentally found to have a 2-cm left adrenal gland mass", "investigate the cause of her pelvic pain"],
677: ["incidentally detected to have a 13-mm pituitary macro-adenoma", "no history of any significant medical illness"],
678: ["dizziness and feeling light-headed", "lost 5 kg", "started to turn very dark as well as generalized skin hyperpigmentation"],
679: ["does not require any dose modification in renal disease"],
680: ["recently diagnosed with papillary thyroid carcinoma"],
})

EXPLANATIONS.update({
681: {
    "idea": "امرأة تشخصت حديثًا بكوشينغ، والسؤال يبي مثال على سلوك تواصل سلبي أثناء شرح مسار مرضها لها، عكس السؤال السابق تمامًا.",
    "clues": [
        ("recently diagnosed with Cushing's syndrome", "سياق <bdi>diagnosis</bdi> جديد يحتاج تواصل واضح وصبور"),
    ],
    "why_correct": [
        "مقاطعة الـ<bdi>patient</bdi> (<bdi>Interrupt a patient</bdi>) وهي ما فهمت بعد سلوك سلبي واضح، لأنه يمنعها من استيعاب المعلومة ويشعرها بعدم الاهتمام.",
        "التواصل الجيد يتطلب إعطاء الـ<bdi>patient</bdi> وقت كافٍ لتستوعب وتسأل، خصوصًا مع <bdi>diagnosis</bdi> جديد ومقلق مثل كوشينغ.",
        "باقي الخيارات (الكلام الواضح البطيء، التواصل بالعين، تشجيع الأسئلة) كلها سلوكيات إيجابية تحسّن التواصل، عكس المقاطعة.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>patient</bdi> تفهم بسرعة ومرتاحة بالحوار، لا يزال إعطاؤها وقت كافٍ سلوك جيد يجب الحفاظ عليه.",
        "بمواقف الشرح المعقدة، تصير مهارات التواصل الإيجابية (الوضوح، الصبر، تشجيع الأسئلة) أهم وأكثر تأثيرًا.",
    ],
    "rule": "مقاطعة الـ<bdi>patient</bdi> أثناء عدم فهمه من أوضح سلوكيات التواصل السلبية اللي يجب تجنبها.",
    "comparison": None,
    "guideline_note": None,
},
682: {
    "idea": "السؤال يبي عند أي مستوى من معدل الترشيح الكبيبي المقدر (eGFR) يجب إيقاف الـ<bdi>metformin</bdi> تمامًا بمرضى <bdi>diabetes</bdi>، بناءً على القاعدة الدوائية المعتمدة لأمان هذا الدواء.",
    "clues": [
        ("metformin should be stopped in diabetic patients", "يبحث عن العتبة الدقيقة لإيقاف الدواء كليًا لا مجرد تقليل الجرعة"),
    ],
    "why_correct": [
        "الإرشادات الحديثة توصي بإيقاف الـ<bdi>metformin</bdi> تمامًا عندما ينخفض eGFR إلى أقل من 30 مل/دقيقة، ب<bdi>cause</bdi> زيادة <bdi>risk</bdi> الحماض اللبني (lactic acidosis) بهذا المستوى من <bdi>renal failure</bdi>.",
        "بين 30 و45 يوصى بتقليل الجرعة والمراقبة الدقيقة، مو الإيقاف الكامل بعد.",
        "بين 45 و60 عادة يستمر الدواء بجرعته المعتادة مع <bdi>follow-up</bdi> دورية لوظائف الكلى.",
    ],
    "when_changes": [
        "لو كان eGFR بين 30-45، الـ<bdi>step</bdi> الصحيحة تقليل الجرعة مع مراقبة دقيقة، مو الإيقاف الكامل.",
        "لو تحسنت وظائف الكلى لاحقًا فوق 30 بعد إيقافه، ممكن يعاد <bdi>assessment</bdi> إمكانية إعادة الدواء حسب الـ<bdi>case</bdi> السريرية.",
    ],
    "rule": "الـ<bdi>metformin</bdi> يوقف تمامًا عند eGFR أقل من 30 مل/دقيقة ب<bdi>cause</bdi> <bdi>risk</bdi> الحماض اللبني.",
    "comparison": {
        "headers": ["eGFR", "قرار الـ<bdi>metformin</bdi>"],
        "rows": [
            ["45-60", "استمرار بالجرعة المعتادة"],
            ["30-45", "تقليل الجرعة ومراقبة دقيقة"],
            ["أقل من 30", "إيقاف كامل"],
        ],
    },
    "guideline_note": None,
},
683: {
    "idea": "السؤال يبي أي دواء من أدوية <bdi>osteoporosis</bdi> معتمد من هيئة الدواء الأمريكية ل<bdi>treatment</bdi> ارتفاع الكالسيوم الناتج عن الخباثة تحديدًا، وهذي معلومة دوائية مباشرة.",
    "clues": [
        ("FDA approval to treat malignancy induced\nhypercalcemia", "يبحث عن استطباب دوائي محدد ومعتمد رسميًا لهذي الـ<bdi>case</bdi> تحديدًا"),
    ],
    "why_correct": [
        "<bdi>Denosumab</bdi> حاصل على اعتماد FDA ل<bdi>treatment</bdi> ارتفاع الكالسيوم الناتج عن الخباثة عند المرضى اللي ما استجابوا ل<bdi>treatment</bdi> البيسفوسفونيت.",
        "آليته مختلفة عن البيسفوسفونيت (يثبط RANKL بدل الترسب بالعظم مباشرة)، وهذا يجعله فعال حتى بحالات مقاومة للبيسفوسفونيت الوريدي.",
        "الأليندرونيت والإيباندرونيت أدوية فموية أساسًا ل<bdi>treatment</bdi> <bdi>osteoporosis</bdi> الـ<bdi>chronic</bdi>، ما تستخدم ل<bdi>treatment</bdi> ارتفاع الكالسيوم الـ<bdi>acute</bdi>، والتيريباراتيد (نظير PTH) ممنوع أصلًا بحالات ارتفاع الكالسيوم لأنه يرفعه أكثر.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> يستجيب جيدًا للبيسفوسفونيت الوريدي، يبقى هو الخط الأول المعتاد، والدينوسوماب يحفظ لحالات المقاومة.",
        "لو كان الهدف <bdi>treatment</bdi> <bdi>osteoporosis</bdi> عظام <bdi>chronic</bdi> عادية بدون ارتفاع كالسيوم <bdi>acute</bdi>، تصير أدوية البيسفوسفونيت الفموية خيارات مناسبة تمامًا.",
    ],
    "rule": "دينوسوماب هو دواء <bdi>osteoporosis</bdi> المعتمد من FDA ل<bdi>treatment</bdi> ارتفاع الكالسيوم الناتج عن الخباثة، خصوصًا عند مقاومة البيسفوسفونيت.",
    "comparison": None,
    "guideline_note": None,
},
684: {
    "idea": "امرأة حامل عندها <bdi>diabetes</bdi> حملي غير مضبوط بالحمية، وترفض حقن الـ<bdi>insulin</bdi> وتسأل عن بديل فموي آمن بالحمل، والسؤال يبي أي دواء فموي له بيانات أمان كافية للاستخدام بالحمل.",
    "clues": [
        ("gestational diabetes mellitus (GDM) at week 24", "<bdi>diagnosis</bdi> <bdi>diabetes</bdi> حملي مؤكد"),
        ("blood sugar<br>reading between (150-200 mg/di)", "ضبط غير كافٍ بالحمية وحدها"),
        ("totally refusing injections", "تستبعد الـ<bdi>insulin</bdi> كخيار مقبول لها، تحتاج بديل فموي"),
    ],
    "why_correct": [
        "<bdi>Glyburide</bdi> من أدوية السلفونيل يوريا اللي لها بيانات أمان واستخدام موثق تاريخيًا كبديل فموي لل<bdi>insulin</bdi> ب<bdi>diabetes</bdi> الحملي عند رفض الحقن.",
        "هذا الدواء يعبر المشيمة بكمية أقل نسبيًا من بعض أدوية السلفونيل يوريا الأخرى، وله سجل استخدام أطول بالحمل مقارنة بباقي الخيارات المذكورة.",
        "الغليبيزايد أقل بيانات أمان موثقة بالحمل، والسيتاغليبتين والروزيغليتازون ليس لهما بيانات أمان كافية أو موصى بهما بالحمل.",
    ],
    "when_changes": [
        "لو وافقت الـ<bdi>patient</bdi> على الـ<bdi>insulin</bdi>، يبقى الـ<bdi>insulin</bdi> الخيار الأفضل والأكثر أمانًا بشكل عام لل<bdi>diabetes</bdi> الحملي غير المضبوط.",
        "لو فشل الغليبورايد بالسيطرة الكافية، يحتاج إعادة نقاش مع الـ<bdi>patient</bdi> حول الحاجة لل<bdi>insulin</bdi> رغم رفضها الأولي.",
    ],
    "rule": "عند رفض الـ<bdi>insulin</bdi> ب<bdi>diabetes</bdi> الحملي، الغليبورايد من الخيارات الفموية اللي لها بيانات أمان مقبولة بالحمل.",
    "comparison": None,
    "guideline_note": None,
},
685: {
    "idea": "رجل عنده ما قبل <bdi>diabetes</bdi> وتاريخ عائلي قوي ل<bdi>diseases</bdi> قلبية و<bdi>diabetes</bdi>، جاء يستشير عن أفضل نصيحة نمط حياة تمنع تطور <bdi>diabetes</bdi> وتحمي قلبه بنفس الوقت، والسؤال يبي أشمل نصيحة صحيحة.",
    "clues": [
        ("strong family history of type 2 diabetes and cardiovascular disease", "<bdi>factor</bdi> <bdi>risk</bdi> مضاعف يستدعي نصيحة شاملة (<bdi>diabetes</bdi> وقلب معًا)"),
        ("recently diagnosed with pre-diabetes", "مرحلة مبكرة قابلة للتعديل بنمط الحياة"),
        ("HbA1C 6.1", "ضمن مرحلة ما قبل <bdi>diabetes</bdi>"),
    ],
    "why_correct": [
        "الجمع بين الرياضة المنتظمة (على الأقل 30 دقيقة معظم أيام الأسبوع) وحمية <bdi>low</bdi> الكربوهيدرات هو النصيحة الأشمل اللي تستهدف الوقاية من <bdi>diabetes</bdi> وتحسين <bdi>factors</bdi> <bdi>risk</bdi> القلب معًا.",
        "هذا الجمع يعطي فايدة مزدوجة على الوزن ومقاومة الـ<bdi>insulin</bdi> ودهون الدم، مقارنة بأي عنصر واحد لوحده.",
        "الرياضة وحدها أو تقليل السعرات وحده أو حمية عالية الكربوهيدرات كلها أقل شمولية من الجمع بين النشاط البدني المنتظم وحمية <bdi>low</bdi> الكربوهيدرات لهذا الـ<bdi>patient</bdi> عالي الخطورة.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> عنده <bdi>disease</bdi> كلوي أو <bdi>case</bdi> تمنع حمية <bdi>low</bdi> الكربوهيدرات، يحتاج تعديل النهج الغذائي حسب حالته.",
        "لو تطور لديه <bdi>diabetes</bdi> فعلي واضح رغم نمط الحياة، يحتاج إضافة <bdi>treatment</bdi> دوائي مثل الـ<bdi>metformin</bdi>.",
    ],
    "rule": "ب<bdi>patient</bdi> ما قبل <bdi>diabetes</bdi> عالي الخطورة، الجمع بين رياضة منتظمة وحمية <bdi>low</bdi> الكربوهيدرات يعطي أفضل وقاية شاملة من <bdi>diabetes</bdi> و<bdi>diseases</bdi> القلب.",
    "comparison": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
681: {
    "A": "الكلام الواضح البطيء سلوك تواصل إيجابي يساعد فهم الـ<bdi>patient</bdi>، عكس المطلوب هنا.",
    "B": "التواصل البصري المباشر سلوك إيجابي يبني الثقة، عكس المطلوب هنا.",
    "D": "تشجيع الأسئلة سلوك إيجابي يحسن الفهم والمشاركة، عكس المطلوب هنا.",
},
682: {
    "A": "بين 45-60 يستمر الدواء بجرعته المعتادة، هذا مو مستوى الإيقاف.",
    "B": "بين 30-45 يقلل الجرعة مع مراقبة دقيقة، مو إيقاف كامل بعد.",
    "D": "أقل من 15 مستوى متأخر جدًا؛ الإيقاف الفعلي الموصى به يبدأ عند أقل من 30 لا ننتظر لهذا الحد.",
},
683: {
    "B": "الأليندرونيت دواء فموي ل<bdi>osteoporosis</bdi> الـ<bdi>chronic</bdi>، غير معتمد ل<bdi>treatment</bdi> ارتفاع الكالسيوم الـ<bdi>acute</bdi> الناتج عن الخباثة.",
    "C": "الإيباندرونيت أيضًا دواء فموي ل<bdi>osteoporosis</bdi> الـ<bdi>chronic</bdi>، بنفس القيد السابق.",
    "D": "التيريباراتيد (نظير PTH) ممنوع أصلًا بحالات ارتفاع الكالسيوم لأنه يرفع الكالسيوم أكثر لا يخفضه.",
},
684: {
    "A": "الغليبيزايد أقل بيانات أمان موثقة بالحمل مقارنة بالغليبورايد.",
    "B": "السيتاغليبتين ليس له بيانات أمان كافية موصى بها للاستخدام أثناء الحمل.",
    "D": "الروزيغليتازون غير موصى باستخدامه أثناء الحمل لغياب بيانات أمان كافية.",
},
685: {
    "A": "الرياضة وحدها أقل شمولية من الجمع بينها وبين تعديل غذائي مناسب لهذا الـ<bdi>patient</bdi> عالي الخطورة.",
    "B": "تحديد الرياضة فقط بدون تعديل غذائي مصاحب أقل فعالية من النصيحة الشاملة.",
    "C": "حمية عالية بالكربوهيدرات و<bdi>low</bdi> بالبروتين لا تناسب هدف الوقاية من <bdi>diabetes</bdi> و<bdi>diseases</bdi> القلب هنا.",
},
})

HIGHLIGHT_TERMS.update({
681: ["recently diagnosed with Cushing's syndrome"],
682: ["metformin should be stopped in diabetic patients"],
683: ["FDA approval to treat malignancy induced"],
684: ["gestational diabetes mellitus (GDM) at week 24", "totally refusing injections"],
685: ["strong family history of type 2 diabetes and cardiovascular disease", "recently diagnosed with pre-diabetes", "HbA1C 6.1"],
})

EXPLANATIONS.update({
686: {
    "idea": "امرأة حامل عندها <bdi>diabetes</bdi> حملي تسأل عن أفضل نمط غذائي يساعدها تضبط سكرها وتتجنب الحاجة لل<bdi>insulin</bdi>، والسؤال يبي أفضل نوع حمية موصى بها بهذي الـ<bdi>case</bdi> تحديدًا.",
    "clues": [
        ("diagnosed with gestational diabetes\nmellitus (GDM) at week 24", "<bdi>diagnosis</bdi> <bdi>diabetes</bdi> حملي مؤكد"),
        ("best dietary habits she can\nfollow to control her blood sugar and avoid insulin injection", "الهدف تحديدًا هو ضبط السكر غذائيًا لتجنب الـ<bdi>insulin</bdi>"),
    ],
    "why_correct": [
        "حمية <bdi>low</bdi> المؤشر الجلايسيمي (<bdi>low glycemic index diet</bdi>) تساعد بالتحكم بارتفاع السكر بعد الوجبات بشكل أفضل من الحميات العادية.",
        "هذا النوع من الحمية يقلل التذبذب الـ<bdi>acute</bdi> بسكر الدم بعد الأكل، وهذا مهم جدًا لضبط <bdi>diabetes</bdi> الحملي بدون أدوية إضافية.",
        "الحمية <bdi>low</bdi> الدهون وحمية البحر المتوسط أقل تركيزًا على ضبط استجابة السكر المباشرة بعد الوجبات مقارنة بحمية <bdi>low</bdi> المؤشر الجلايسيمي المخصصة لهذا الهدف.",
    ],
    "when_changes": [
        "لو فشلت الحمية بضبط السكر لمستويات آمنة رغم الالتزام الكامل، يحتاج التفكير بإضافة <bdi>insulin</bdi> أو دواء فموي آمن بالحمل.",
        "الحد من السعرات بشكل صارم غير موصى به أثناء الحمل ب<bdi>cause</bdi> حاجة الجنين للتغذية الكافية.",
    ],
    "rule": "حمية <bdi>low</bdi> المؤشر الجلايسيمي هي الخيار الغذائي الموصى به لضبط <bdi>diabetes</bdi> الحملي وتقليل الحاجة لل<bdi>insulin</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
687: {
    "idea": "امرأة كبيرة بالسن عندها ما قبل <bdi>diabetes</bdi> مع سمنة ونمط حياة غير نشط و<bdi>signs</bdi> مقاومة <bdi>insulin</bdi> (اسمرار الجلد بمؤخرة الرقبة)، والسؤال يبي أفضل نصيحة غذائية إضافية لتقليل <bdi>risk</bdi> تطور <bdi>diabetes</bdi> لديها.",
    "clues": [
        ("mildly elevated glycated hemoglobin", "ما قبل <bdi>diabetes</bdi> مؤكد بالتحليل"),
        ("has had obesity for many years", "<bdi>factor</bdi> <bdi>risk</bdi> رئيسي للتطور ل<bdi>diabetes</bdi> كامل"),
        ("trace acanthosis nigricans at the nape of the neck", "<bdi>sign</bdi> جسدية على مقاومة الـ<bdi>insulin</bdi>"),
    ],
    "why_correct": [
        "الدراسة المرجعية الكبرى لبرنامج الوقاية من <bdi>diabetes</bdi> (<bdi>Diabetes Prevention Program</bdi>) استخدمت حمية <bdi>low</bdi> الدهون مع تقييد سعرات لتحقيق إنقاص وزن 5-10% كنهج فعال مثبت للوقاية من تطور <bdi>diabetes</bdi>.",
        "استهداف إنقاص وزن معتدل (5-10% من وزن الجسم) عبر حمية <bdi>low</bdi> الدهون مع زيادة النشاط البدني يقلل بشكل كبير <bdi>risk</bdi> تطور <bdi>diabetes</bdi> النوع الثاني.",
        "هذا النهج المثبت بالدراسات الكبرى أقوى دليلًا من حمية <bdi>low</bdi> المؤشر الجلايسيمي وحدها أو الاعتماد على الدواء فقط بدل التدخل الغذائي.",
    ],
    "when_changes": [
        "لو فشل نمط الحياة المكثف (حمية ورياضة) بمنع تطور <bdi>diabetes</bdi>، يصير الـ<bdi>metformin</bdi> خيار وقائي دوائي إضافي معقول.",
        "لو كانت الـ<bdi>patient</bdi> تفضل نهج آخر مدعوم بدراسات (<bdi>low</bdi> الكربوهيدرات)، يبقى النقاش مفتوح لكن الدليل الأقوى تاريخيًا لبرنامج الوقاية هو الحمية <bdi>low</bdi> الدهون مع إنقاص الوزن.",
    ],
    "rule": "حمية <bdi>low</bdi> الدهون تستهدف إنقاص وزن 5-10% هي النهج الغذائي المثبت للوقاية من تطور <bdi>diabetes</bdi> بمرضى ما قبل <bdi>diabetes</bdi> عالي الخطورة.",
    "comparison": None,
    "guideline_note": None,
},
688: {
    "idea": "رجل عنده سمنة مفرطة جدًا (BMI 55) مع <bdi>complications</bdi> متعددة (<bdi>diabetes</bdi>، ضغط، انقطاع نفس نومي، دهون، مشاكل مفاصل، <bdi>depression</bdi>) وضعف التزام بالـ<bdi>treatment</bdi> الدوائي، والسؤال يبي أفضل نصيحة تعالج المشكلة الأساسية بشكل جذري.",
    "clues": [
        ("obesity is\ncomplicated by type 2 diabetes mellitus", "سمنة مرضية مع <bdi>complications</bdi> متعددة مرتبطة بها مباشرة"),
        ("not compliant to treatments", "ضعف التزام بالـ<bdi>treatment</bdi> الدوائي التقليدي لكل مشكلة على حدة"),
        ("BMI 55 kg/m2", "سمنة مفرطة جدًا، أعلى بكثير من عتبة الجراحة الاستقلابية"),
    ],
    "why_correct": [
        "مؤشر كتلة الجسم هنا <bdi>elevated</bdi> جدًا جدًا (55) مع <bdi>complications</bdi> متعددة مرتبطة مباشرة بالسمنة نفسها، وهذا يجعل السمنة هي المشكلة الجذرية اللي يجب معالجتها مباشرة.",
        "الجراحة الاستقلابية (<bdi>bariatric surgery</bdi>) هي الأكثر فعالية لإنقاص وزن كبير ومستدام بهذا المستوى من السمنة، وتتحسن بعدها أغلب الـ<bdi>complications</bdi> المرافقة (<bdi>diabetes</bdi>، الضغط، انقطاع النفس، آلام المفاصل) بشكل كبير.",
        "التركيز على الالتزام بالأدوية فقط أو معالجة كل <bdi>complication</bdi> على حدة (الركبة، الأدوية) يتجاهل المشكلة الجذرية ولن يحل أغلب الـ<bdi>complications</bdi> المرتبطة بالسمنة نفسها.",
    ],
    "when_changes": [
        "لو كان مؤشر كتلة الجسم أقل بكثير (27-30) بدون <bdi>complications</bdi> <bdi>severe</bdi>، تكون أدوية إنقاص الوزن أو تعديل نمط الحياة كافية دون جراحة.",
        "بعد الجراحة، يبقى الالتزام بالـ<bdi>follow-up</bdi> الغذائية والدوائية طويلة المدى ضروري لثبات الـ<bdi>result</bdi>.",
    ],
    "rule": "بسمنة مفرطة جدًا مع <bdi>complications</bdi> متعددة وضعف التزام بالـ<bdi>treatment</bdi> التقليدي، الإحالة للجراحة الاستقلابية هي النصيحة الأنسب لمعالجة المشكلة الجذرية.",
    "comparison": None,
    "guideline_note": None,
},
689: {
    "idea": "امرأة <bdi>diabetes</bdi> نوع أول طويل الأمد عندها تلف كلوي مبدئي وضبط سكر سيء جدًا (HbA1c <bdi>elevated</bdi>)، وتبي تحمل الشهر الجاي، والسؤال يبي أفضل نصيحة لحماية الجنين من التشوهات المرتبطة ب<bdi>diabetes</bdi> غير المضبوط.",
    "clues": [
        ("would try to become pregnant next month", "تخطط للحمل قريبًا جدًا، وقت حرج لضبط السكر قبل الحمل"),
        ("24 hr urine protein\n2000", "بروتينية واضحة، دليل تأثر كلوي من <bdi>diabetes</bdi> طويل الأمد"),
        ("HbA1C 8.0", "ضبط سيء جدًا فوق الهدف الآمن للحمل بمسافة كبيرة"),
    ],
    "why_correct": [
        "ضبط السكر السيء وقت الحمل (خصوصًا بالأسابيع الأولى الحرجة لتكوّن أعضاء الجنين) يزيد بشكل كبير <bdi>risk</bdi> التشوهات الخلقية.",
        "النصيحة الصحيحة هي تأجيل محاولة الحمل لحين تحسين HbA1c ليصبح أقرب ما يمكن لل<bdi>normal</bdi> بأمان، لتقليل <bdi>risk</bdi> التشوهات الخلقية قدر الإمكان.",
        "تعديل الوجبات أو الأدوية الأخرى (الـ<bdi>statin</bdi>، الـ<bdi>insulin</bdi> بديل عن ACE inhibitor) مهمة بس مو الأولوية الأهم مقارنة بضبط السكر قبل الحمل مباشرة لحماية الجنين.",
    ],
    "when_changes": [
        "بعد تحسن HbA1c لمستوى آمن، يصير التوقيت مناسب لمحاولة الحمل مع مراقبة دقيقة لوظائف الكلى والضغط طوال الحمل.",
        "استبدال مثبط الإنزيم المحول بحاصر مستقبلات الأنجيوتنسين ما يفضل أثناء التخطيط للحمل، لأن الاثنين ممنوعين بالحمل ويحتاج إيقافهما تمامًا واستبدالهما بدواء ضغط آمن بالحمل عند تأكد الحمل.",
    ],
    "rule": "قبل محاولة الحمل ب<bdi>patient</bdi> <bdi>diabetes</bdi> نوع أول، لازم تأجيل الحمل لحين تحسين HbA1c لأقرب ما يمكن لل<bdi>normal</bdi> لتقليل <bdi>risk</bdi> التشوهات الخلقية.",
    "comparison": None,
    "guideline_note": None,
},
690: {
    "idea": "امرأة حامل بالثلث الأول عندها <bdi>Graves' disease</bdi> مؤكد ب<bdi>symptoms</bdi> و<bdi>signs</bdi> واضحة (جحوظ، تضخم درقي، <bdi>palpitations</bdi> <bdi>severe</bdi>)، لكنها ترفض بدء أي <bdi>treatment</bdi> أثناء الحمل، والسؤال يبي أفضل تصرف طبي مناسب يحترم قرارها بس يحميها وجنينها.",
    "clues": [
        ("refusing to start any treatment while she is pregnant", "رفض واضح لل<bdi>treatment</bdi> رغم تأكد الـ<bdi>diagnosis</bdi>"),
        ("Heart rate 125 /min", "فرط نشاط <bdi>severe</bdi> وعرضي يحمل <bdi>risk</bdi> حقيقي على الأم والجنين لو ترك بدون <bdi>treatment</bdi>"),
        ("Thyroid-Stimulating Hormone &lt; 0.01", "فرط نشاط درقي <bdi>severe</bdi> جدًا"),
    ],
    "why_correct": [
        "فرط النشاط الدرقي غير المعالج بالحمل يحمل مخاطر حقيقية وخطيرة على الأم (تسمم حملي، قصور قلب) وعلى الجنين (ولادة مبكرة، تأخر نمو)، فترك الـ<bdi>patient</bdi> بدون أي تدخل غير مقبول طبيًا.",
        "الأنسب هو شرح واضح وصريح للمخاطر على صحتها وصحة الجنين، مع محاولة إقناعها بأهمية الـ<bdi>treatment</bdi> بطريقة تحترم استقلاليتها وقرارها النهائي.",
        "هذا يحقق التوازن بين احترام حق الـ<bdi>patient</bdi> باتخاذ القرار وبين واجب الطبيب بتوضيح المخاطر الحقيقية بأمانة وشفافية كاملة.",
    ],
    "when_changes": [
        "لو استمرت برفضها بعد شرح كامل وواضح للمخاطر، يحترم قرارها النهائي ك<bdi>patient</bdi> راشدة واعية طالما فهمت المخاطر بوضوح.",
        "لو كانت الـ<bdi>case</bdi> مهددة للحياة بشكل فوري و<bdi>acute</bdi> جدًا (عاصفة درقية)، يصير التدخل الطارئ أولوية أخلاقية وقانونية أعلى من مجرد الرفض العادي.",
    ],
    "rule": "عند رفض الـ<bdi>patient</bdi> الحامل لل<bdi>treatment</bdi> الضروري، الأنسب شرح المخاطر بوضوح تام ومحاولة الإقناع، مو فرضه عليها ولا تجاهل الموضوع.",
    "comparison": None,
    "guideline_note": None,
},
691: {
    "idea": "رجل عنده سرطان درقي حليمي وخائف من <bdi>complications</bdi> الجراحة المخطط لها، والسؤال يبي أفضل تصرف يترك انطباع نهائي جيد وواضح بنهاية الاستشارة.",
    "clues": [
        ("proven to be papillary thyroid carcinoma", "<bdi>diagnosis</bdi> مؤكد يحتاج شرح خطة <bdi>treatment</bdi> واضحة"),
        ("afraid from the surgical complication", "<bdi>anxiety</bdi> مشروع من الـ<bdi>patient</bdi> يحتاج طمأنة بمعلومات كافية لا تجاهل"),
        ("create a lasting impression at the end of the consultation", "الهدف تحديدًا هو ختام الاستشارة بطريقة فعالة"),
    ],
    "why_correct": [
        "مفتاح الإجابة بالملف يحدد <bdi>Avoid answering all patient's questions</bdi> كالخيار الصحيح لهذا السؤال.",
        "بشكل عام بالتواصل الطبي، تجاهل أسئلة الـ<bdi>patient</bdi> مو سلوك يُنصح فيه، وهذا يخلق تعارض واضح بين المفتاح والمبدأ الطبي الراسخ (تفاصيل ذلك بالملاحظة تحت).",
        "خلّينا إجابة الملف هي المعتمدة على البطاقة زي ما توضح قاعدة العمل بهذا المشروع.",
    ],
    "when_changes": [
        "بالممارسة الفعلية، أفضل تصرف يترك انطباع جيد بختام الاستشارة هو شرح موجز وصادق لخطة الـ<bdi>treatment</bdi> مع الـ<bdi>results</bdi> المتوقعة وغير المتوقعة، لا تجاهل أسئلة الـ<bdi>patient</bdi>.",
        "بأي <bdi>procedure</bdi> جراحي، مناقشة الـ<bdi>complications</bdi> المحتملة والإجابة على استفسارات الـ<bdi>patient</bdi> جزء أساسي من الموافقة المستنيرة قانونيًا وأخلاقيًا.",
    ],
    "rule": "المبدأ الطبي السليم بختام الاستشارة هو شرح موجز وصادق لخطة العمل ونتائجها، بس بهالسؤال تحديدًا اعتمدنا مفتاح الملف كما هو.",
    "comparison": None,
    "guideline_note": "الخيار D (<bdi>briefly explain the action plan with possible expected and unexpected outcome</bdi>) يمثل المبدأ الطبي الراسخ بالتواصل الصادق والموافقة المستنيرة، ويبدو إنه الإجابة الأنسب سريريًا لهالسؤال. مع هذا، مفتاح الملف الأصلي يحدد الخيار A كصحيح، وبما إن قاعدة العمل تعتمد جواب الملف دايمًا، خلّينا A هو الجواب المعتمد بالبطاقة مع توضيح هذا التعارض.",
},
692: {
    "idea": "شاب أصيب بشلل نصفي سفلي بعد حادث وبقي بلا حركة لفترة طويلة، وطلعت عنده زيادة كالسيوم مع PTH <bdi>low</bdi>-<bdi>normal</bdi> (مكبوت نسبيًا)، وهذا يوجه ل<bdi>cause</bdi> ميكانيكي غير هرموني وراء ارتفاع الكالسيوم.",
    "clues": [
        ("traumatic paraplegia", "شلل نصفي سفلي، <bdi>cause</bdi> لعدم الحركة لفترة طويلة"),
        ("requiring prolonged immobilization", "عدم حركة طويل الأمد، <bdi>factor</bdi> <bdi>risk</bdi> مباشر لفقد كالسيوم من العظم"),
        ("Parathyroid hormone 1.0 (1.1-5.3)", "PTH بأدنى الحدود الـ<bdi>normal</bdi> تقريبًا، مكبوت نسبيًا رغم ارتفاع الكالسيوم، يستبعد فرط جارات الدرقية ك<bdi>cause</bdi>"),
    ],
    "why_correct": [
        "عدم الحركة الطويل (<bdi>immobilization</bdi>) يزيد ارتشاف العظم ويطلق كالسيوم زائد للدم، خصوصًا عند الشباب اللي عندهم دوران عظمي نشط أصلًا.",
        "انخفاض PTH النسبي هنا (بأدنى الـ<bdi>normal</bdi>) يتوافق تمامًا مع كبت <bdi>normal</bdi> للغدة استجابة لارتفاع الكالسيوم من مصدر خارج عنها (العظم نفسه)، مو من فرط إفراز جارات الدرقية.",
        "لا يوجد بالسؤال أي دليل على ورم خبيث أو مايلوما (لا <bdi>symptoms</bdi> ولا فحوصات موحية)، والفحص الجسدي والمخبري الـ<bdi>normal</bdi> غير ذلك يدعم الـ<bdi>cause</bdi> الميكانيكي البسيط (عدم الحركة).",
    ],
    "when_changes": [
        "لو كان PTH <bdi>elevated</bdi> بوضوح مع ارتفاع الكالسيوم، يصير فرط جارات الدرقية الأولي هو الـ<bdi>diagnosis</bdi> الأرجح بدل عدم الحركة.",
        "لو ظهرت <bdi>signs</bdi> نقص وزن أو ألم عظمي أو كسور مرضية أو خلايا غير <bdi>normal</bdi> بفحوصات الدم، يصير الورم الخبيث أو المايلوما احتمال أقوى يستحق البحث عنه.",
    ],
    "rule": "عدم الحركة الطويل عند شخص شاب <bdi>cause</bdi> معروف لارتفاع كالسيوم مع PTH مكبوت نسبيًا، من دون حاجة لافتراض <bdi>cause</bdi> ورمي أو غدي.",
    "comparison": None,
    "guideline_note": None,
},
})

WHY_WRONG.update({
686: {
    "A": "الحمية <bdi>low</bdi> الدهون تركز على تقليل الدهون الكلية بس ليست الأكثر فعالية بضبط استجابة السكر المباشرة بعد الوجبات.",
    "B": "حمية البحر المتوسط مفيدة صحيًا بشكل عام بس ليست الأكثر توجيهًا تحديدًا لضبط سكر الحمل بعد الوجبات.",
    "D": "تقييد الطاقة (السعرات) بشكل صارم غير موصى به أثناء الحمل لضمان تغذية كافية للجنين.",
},
687: {
    "A": "حمية <bdi>low</bdi> المؤشر الجلايسيمي مفيدة بس الدليل الأقوى من الدراسات الكبرى للوقاية من <bdi>diabetes</bdi> كان بحمية <bdi>low</bdi> الدهون مع إنقاص وزن محدد.",
    "C": "القول إن الحمية أقل فعالية من الـ<bdi>metformin</bdi> غير دقيق؛ الدراسات الكبرى أظهرت تعديل نمط الحياة (حمية ورياضة) أكثر فعالية من الـ<bdi>metformin</bdi> وحده بالوقاية من <bdi>diabetes</bdi>.",
    "D": "الأدلة الحالية لا تدعم بشكل قاطع تفوق الحمية <bdi>low</bdi> الكربوهيدرات على <bdi>low</bdi> الدهون بمنع <bdi>diabetes</bdi> طويل المدى.",
},
688: {
    "A": "التركيز على الالتزام بالأدوية فقط يتجاهل المشكلة الجذرية (السمنة المفرطة) المسببة لكل هذي الـ<bdi>complications</bdi>.",
    "B": "تبديل مفصل الركبة <bdi>procedure</bdi> موضعي لا يعالج الـ<bdi>cause</bdi> الجذري ولن ينجح جيدًا مع استمرار السمنة المفرطة.",
    "C": "إضافة أدوية إنقاص الوزن أقل فعالية بكثير من الجراحة الاستقلابية بهذا المستوى الـ<bdi>severe</bdi> جدًا من السمنة (BMI 55).",
},
689: {
    "A": "تعديل الوجبات مهم بس لا يمثل الأولوية الأهم مقارنة بضبط السكر قبل الحمل لحماية الجنين من التشوهات.",
    "B": "استبدال نوع دواء الضغط لا يمثل الأولوية الأهم مقارنة بضبط السكر، وكلا الدواءين أصلًا يوقفان تمامًا عند تأكد الحمل.",
    "C": "بدء <bdi>statin</bdi> غير مناسب أصلًا أثناء التخطيط للحمل، وليس الأولوية المطلوبة هنا.",
},
690: {
    "A": "الموافقة على قرارها وتركها بدون أي محاولة توضيح للمخاطر إهمال لواجب الطبيب بتقديم معلومة كافية.",
    "B": "إجبارها على الـ<bdi>treatment</bdi> عبر طرف ثالث (الزوج) يتعارض مع حق الـ<bdi>patient</bdi> الراشدة باتخاذ قرارها الطبي الخاص.",
    "C": "الانتظار شهرين بدون أي تدخل أو توضيح للمخاطر <bdi>risk</bdi> جدًا مع فرط نشاط درقي <bdi>severe</bdi> وعرضي غير معالج.",
},
691: {
    "B": "موافقة الـ<bdi>patient</bdi> ضرورية دائمًا لأي <bdi>procedure</bdi> جراحي، والقول بعكس ذلك مخالف لمبدأ الموافقة المستنيرة.",
    "C": "تجنب مناقشة الـ<bdi>complications</bdi> الجدية يخالف مبدأ الصدق والموافقة المستنيرة الكاملة قبل الجراحة.",
    "D": "حسب مفتاح الملف هذا مو الخيار المحدد كصحيح هنا، رغم إنه يمثل المبدأ الطبي السليم بالتواصل الصادق (انظر الملاحظة بالشرح الكامل).",
},
692: {
    "A": "لا يوجد دليل بالسؤال على ورم خبيث (لا <bdi>symptoms</bdi> بائية ولا فحوصات موحية)، والصورة الكيميائية هنا تدعم <bdi>cause</bdi> ميكانيكي بسيط.",
    "C": "المايلوما المتعددة تعطي عادة صورة مخبرية وسريرية مختلفة (<bdi>anemia</bdi>، قصور كلوي، آفات عظمية)، وغير مذكورة هنا.",
    "D": "فرط جارات الدرقية الأولي يعطي PTH <bdi>elevated</bdi> بوضوح، بينما هنا PTH <bdi>low</bdi>-<bdi>normal</bdi> (مكبوت)، عكس الصورة تمامًا.",
},
})

HIGHLIGHT_TERMS.update({
686: ["best dietary habits she can", "avoid insulin injection"],
687: ["elevated glycated hemoglobin", "has had obesity for many years", "trace acanthosis nigricans at the nape of the neck"],
688: ["not compliant to treatments", "BMI 55 kg/m2"],
689: ["would try to become pregnant next month", "HbA1C 8.0"],
690: ["refusing to start any treatment while she is pregnant", "Heart rate 125 /min", "Thyroid-Stimulating Hormone &lt; 0.01"],
691: ["proven to be papillary thyroid carcinoma", "afraid from the surgical complication"],
692: ["traumatic paraplegia", "requiring prolonged immobilization", "Parathyroid hormone 1.0"],
})
