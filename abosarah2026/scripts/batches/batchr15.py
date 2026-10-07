# -*- coding: utf-8 -*-
# Batch r15 — Pediatrics (AS-0512 .. AS-1020C), 141 questions.

EXPLANATIONS = {
"AS-0512": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "طفل عنده <bdi>mass</bdi> بالـ<bdi>flank</bdi> مع <bdi>calcification</bdi> على الـ<bdi>ultrasound</bdi>، والسؤال يحدد الخطوة الجاية بعد الـ<bdi>ultrasound</bdi>، مو التشخيص النهائي.",
    "clues": [
        ("mass in the abdomen in the left flank", "كتلة بالـ<bdi>flank</bdi> ترجح <bdi>neuroblastoma</bdi> أو <bdi>Wilms tumor</bdi>"),
        ("internal calcification", "التكلّس الداخلي يرجح <bdi>neuroblastoma</bdi> أكثر"),
        ("Next test", "كلمة Next تحدد إنها خطوة تصوير، مو تشخيص نهائي"),
    ],
    "why_correct": [
        "بعد الـ<bdi>ultrasound</bdi> اللي أكد الكتلة، الخطوة المعيارية الجاية هي <bdi>CT abdomen</bdi> لأنها توضح <bdi>organ of origin</bdi> والامتداد والعلاقة بالأوعية والعقد قبل أي <bdi>tissue sampling</bdi>.",
        "التكلّس الداخلي يرجح <bdi>neuroblastoma</bdi>، والـ<bdi>CT</bdi> يوضح هذا التكلّس بشكل أفضل من الـ<bdi>ultrasound</bdi>.",
        "الـ<bdi>biopsy</bdi> يجي بعد الـ<bdi>CT</bdi> للتشخيص النسيجي النهائي، مو كخطوة فورية جاية.",
    ],
    "when_changes": [
        "لو السؤال شال كلمة Next وسأل عن الفحص اللي يوصل للتشخيص نفسه، الجواب يتغير إلى <bdi>biopsy</bdi>.",
        "لو فيه خيار يجمع <bdi>CT</bdi> مع <bdi>biopsy</bdi> بنفس الخيار، هذا يصير الأفضل لأنه يغطي كل سلم التشخيص.",
    ],
    "rule": "أي سؤال فيه كلمة Next بعد <bdi>ultrasound</bdi> لكتلة بطنية عند طفل، الجواب المعياري <bdi>CT</bdi>؛ لو غابت الكلمة وصار السؤال عن تأكيد التشخيص، الجواب يصير <bdi>biopsy</bdi>.",
    "comparison": {
        "headers": ["المعيار", "Neuroblastoma", "Wilms tumor"],
        "rows": [
            ["المصدر", "<bdi>adrenal medulla</bdi> أو <bdi>sympathetic chain</bdi>", "<bdi>kidney</bdi>"],
            ["التكلّس", "شائع", "نادر"],
            ["يعبر خط الوسط", "ممكن", "نادر"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},
"AS-0512B": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "طفل عمره 3 سنوات بكتلة <bdi>flank</bdi> صلبة وثابتة مع <bdi>calcification</bdi> على الـ<bdi>X-ray</bdi>، والسؤال عن الخطوة الجاية لتأسيس التشخيص.",
    "clues": [
        ("3 year old child", "عمر نموذجي لـ<bdi>neuroblastoma</bdi>"),
        ("large mass on his flank", "كتلة ثابتة غير متحركة"),
        ("soft tissue mass with internal calcifications", "التكلّس يرجح <bdi>neuroblastoma</bdi>"),
    ],
    "why_correct": [
        "الـ<bdi>X-ray</bdi> أظهرت فقط كتلة نسيج رخو مع تكلّس، فالخطوة الجاية هي تصوير عرضي أدق، و<bdi>CT abdomen</bdi> يأكد مصدر الكتلة والامتداد والتكلّس ويخطط للـ<bdi>biopsy</bdi>.",
        "عمر الطفل والكتلة الصلبة الثابتة مع التكلّس كل هذا يرجح <bdi>neuroblastoma</bdi> أكثر من أي تشخيص آخر.",
    ],
    "when_changes": [
        "لو السؤال يبي تأكيد نسيجي للتشخيص، الجواب يصير <bdi>biopsy</bdi> بعد الـ<bdi>CT</bdi>.",
        "لو الطفل عنده علامات <bdi>leukemia</bdi> مثل <bdi>cytopenias</bdi>، الخطوة الأولى تصير <bdi>bone marrow aspiration</bdi> مو تصوير الكتلة.",
    ],
    "rule": "كتلة <bdi>flank</bdi> مع تكلّس عند طفل: صوّر بـ<bdi>CT</bdi> قبل أي عينة نسيجية؛ <bdi>bone marrow aspiration</bdi> خطوة <bdi>staging</bdi> لاحقة، مو الخطوة الأولى.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0513": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "نفس سيناريو الكتلة والتكلّس، لكن السؤال هنا عن الفحص اللي «يوصل للتشخيص» بدون كلمة Next، فالإجابة تتغير.",
    "clues": [
        ("mass in the abdomen in the left flank", "نفس الكتلة بالـ<bdi>flank</bdi>"),
        ("internal calcification", "يرجح <bdi>neuroblastoma</bdi>"),
        ("reach the diagnosis", "غياب كلمة Next يعني السؤال عن التشخيص النهائي"),
    ],
    "why_correct": [
        "كتلة بطنية خبيثة محتملة (<bdi>neuroblastoma</bdi> أو <bdi>Wilms tumor</bdi>) تحتاج تشخيص نسيجي نهائي، فالـ<bdi>biopsy</bdi> هو اللي يثبت نوع الكتلة ويوصل للتشخيص.",
        "التصوير (<bdi>ultrasound</bdi> أو <bdi>CT</bdi>) يقترح التشخيص بس ما يثبته، والـ<bdi>biopsy</bdi> هو الإثبات النسيجي.",
    ],
    "when_changes": [
        "لو رجعت كلمة Next للسؤال، الجواب يرجع إلى <bdi>CT</bdi> كخطوة تصوير جاية.",
        "لو فيه خيار يجمع <bdi>CT</bdi> مع <bdi>biopsy</bdi> بخيار واحد، هذا يتفضل على <bdi>biopsy</bdi> لوحده.",
    ],
    "rule": "التصوير يقترح، والـ<bdi>histology</bdi> يشخّص: اشطب كلمة Next ويصير الجواب <bdi>biopsy</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0514": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نفس الكتلة والتكلّس بدون كلمة Next، لكن هنا الخيار المتوفر يجمع <bdi>CT</bdi> و<bdi>biopsy</bdi> بخيار واحد.",
    "clues": [
        ("mass in the abdomen in the left flank", "كتلة <bdi>flank</bdi> مع تكلّس"),
        ("internal calcification", "يرجح <bdi>neuroblastoma</bdi>"),
        ("reach the diagnosis", "يبي سلم التشخيص الكامل"),
    ],
    "why_correct": [
        "الوصول للتشخيص الكامل يحتاج خطوتين: <bdi>CT</bdi> لتحديد مصدر الكتلة والامتداد، و<bdi>biopsy</bdi> للتشخيص النسيجي. الخيار اللي يجمعهم يغطي كل السلم.",
        "بدون كلمة Next بالسؤال، أي خيار تصوير لوحده (مثل <bdi>MRI</bdi>) ناقص لأنه ما يعطي تشخيص نسيجي.",
    ],
    "when_changes": [
        "لو السؤال كان عن الخطوة الجاية فقط بعد الـ<bdi>ultrasound</bdi>، الجواب يصير <bdi>CT</bdi> لوحده.",
        "لو كلمة Next حاضرة ونفس هذا الخيار المدمج موجود، برضو يفضل الخيار المدمج لأنه الأشمل.",
    ],
    "rule": "لما يكون فيه خيار يجمع <bdi>CT</bdi> و<bdi>biopsy</bdi> مع، هذا يتغلب على أي تصوير لوحده بسؤال «الوصول للتشخيص».",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0515": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "طفل بكتلة بطنية صغيرة بدون ألم وبدون تكلّس مذكور، والسؤال عن الفحص «التشخيصي».",
    "clues": [
        ("2 cm skin colored painless abdominal mass", "كتلة صغيرة بدون ألم بطفل سليم بالباقي"),
        ("Diagnostic test", "كلمة Diagnostic تحدد المطلوب حسب هذا الريكول"),
    ],
    "why_correct": [
        "هذا الريكول مفتاحه <bdi>abdominal CT</bdi> كالفحص التشخيصي للكتلة البطنية، لأنه يوضح مصدرها وعمقها وطبيعتها قبل أي عينة نسيجية، بما يتماشى مع نمط الأسئلة المشابهة بهذا الملف.",
        "غياب التكلّس هنا ما يمنع استخدام <bdi>CT</bdi> كخطوة توضيحية أولى حسب مفتاح هذا السؤال.",
    ],
    "when_changes": [
        "لو السؤال يبي الفحص «الأولي» أو «initial»، الجواب يتغير إلى <bdi>ultrasound</bdi>.",
        "لو يبي تأكيد نسيجي، الجواب يصير <bdi>biopsy</bdi>.",
    ],
    "rule": "الفحص «الأولي» للكتلة البطنية عند الطفل عادة <bdi>ultrasound</bdi>، لكن هذا الريكول يربط كلمة Diagnostic بـ<bdi>CT</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": "فيه تضارب بسيط بين منطق «الأولي = ultrasound» المعتاد وبين مفتاح هذا الريكول الذي يربط Diagnostic بـ<bdi>CT</bdi>؛ التزمنا بإجابة المصدر لأنها مؤكدة.",
},
"AS-0516": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفل عمره 3 سنوات بكتلة بطنية ضخمة ملموسة، والسؤال يبي كيف «نؤكد» التشخيص.",
    "clues": [
        ("huge palpable abdominal mass", "كتلة كبيرة ترجح ورم خبيث مثل <bdi>Wilms tumor</bdi> أو <bdi>neuroblastoma</bdi>"),
        ("CONFIRM", "كلمة التأكيد تحدد إننا نبي تشخيص نسيجي"),
    ],
    "why_correct": [
        "كلمة CONFIRM تعني إثبات نوع الكتلة نسيجياً، وما يأكد نوع الورم إلا <bdi>biopsy</bdi>.",
        "التصوير مهم لتوصيف الكتلة لكنه ما يثبت التشخيص النسيجي النهائي.",
    ],
    "when_changes": [
        "لو السؤال يبي الفحص «الأولي»، الجواب يصير <bdi>ultrasound</bdi>.",
        "لو يبي الخطوة الجاية بعد الـ<bdi>ultrasound</bdi>، الجواب يصير <bdi>CT</bdi>.",
    ],
    "rule": "كلمة Confirm تعني نسيج: التصوير أبداً ما يأكد نوع الورم.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0538": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفل بـ<bdi>cellulitis</bdi> بالساق مع <bdi>fever</bdi> و<bdi>irritability</bdi> وتورم متزايد بدون <bdi>abscess</bdi> واضح، والسؤال عن الإدارة.",
    "clues": [
        ("fever and irritability", "علامات جهازية مع <bdi>cellulitis</bdi>"),
        ("red warm Painful Tender swelling", "صورة <bdi>cellulitis</bdi> نمطية"),
        ("no pus or abscess", "ما فيه تجمع يحتاج تصريف"),
        ("area is Enlarging", "الالتهاب متوسع بسرعة"),
    ],
    "why_correct": [
        "<bdi>cellulitis</bdi> مع <bdi>fever</bdi> و<bdi>irritability</bdi> (علامات جهازية) والمنطقة متوسعة تحتاج <bdi>IV antibiotics</bdi> مو علاج فموي بالبيت.",
        "التوسع السريع بطفل محموم يحتاج <bdi>surgical consultation</bdi> مبكر لاستبعاد تجمع عميق أو عدوى نخرية، حتى بدون <bdi>abscess</bdi> واضح الآن.",
        "استقرار العلامات الحيوية يعني إنه مو بحاجة <bdi>ICU</bdi>، لكنه برضو يحتاج دخول وعلاج وريدي.",
    ],
    "when_changes": [
        "لو كان الالتهاب محدود بدون <bdi>fever</bdi> وبطفل مستقر، الجواب يتغير إلى علاج فموي مع متابعة بالعيادة.",
        "لو ظهر <bdi>fluctuation</bdi> أو <bdi>abscess</bdi> واضح، الخطوة تصير تصريف جراحي مباشر.",
    ],
    "rule": "الحمى تحوّل الـ<bdi>cellulitis</bdi> لمشكلة تحتاج <bdi>IV antibiotics</bdi> حتى لو باقي العلامات الحيوية مستقرة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0541": {
    "correct_letter": "B",
    "self_judged": True,
    "idea": "طفل بعمر 10 سنوات عنده <bdi>progressive respiratory distress</bdi> بعد <bdi>severe pneumonia</bdi>، ناخذ أكسجين وما تحسن، مع <bdi>hypoxia</bdi> مستمرة وفحص قلب وإيكو طبيعي، والسؤال عن اللي يظهر بصورة الصدر.",
    "clues": [
        ("10-year-old", "عمر مدرسي، مو حديث ولادة"),
        ("progressive respiratory distress", "تدهور تنفسي مستمر"),
        ("after severe pneumonia", "سبب التحفيز هو عدوى رئوية حديثة"),
        ("no improvements still hypoxia", "<bdi>hypoxia</bdi> لا تستجيب للأكسجين"),
        ("echo normal", "الإيكو الطبيعي يستبعد سبب قلبي للـ<bdi>pulmonary edema</bdi>"),
    ],
    "why_correct": [
        "الإيكو الطبيعي يستبعد سبب قلبي، فـ<bdi>hypoxia</bdi> لا تستجيب للأكسجين بعد التهاب رئوي شديد تعطي صورة <bdi>ARDS</bdi>: ضرر حاد خلال أسبوع، <bdi>non-cardiogenic</bdi>، مع ارتشاحات منتشرة.",
        "صورة الصدر بـ<bdi>ARDS</bdi> تُظهر <bdi>bilateral infiltrates</bdi> منتشرة وليست محصورة بفص واحد، وهذا يطابق آلية المرض هنا (ضرر حاد منتشر بالرئتين).",
        "ما فيه ذكر <bdi>wheeze</bdi> أو علامات تضيق مجرى هوائي، فخيارات مثل <bdi>hyperinflation</bdi> أو الصدر النفخي لا تناسب الصورة.",
    ],
    "when_changes": [
        "لو ذكر السؤال <bdi>haemoptysis</bdi> واضح مع علامات أخرى محددة، الصورة تتجه لتشخيص نزفي رئوي مختلف.",
        "لو كان فيه ضيق مع <bdi>wheeze</bdi> صريح، الجواب يتجه للصدر النفخي (<bdi>hyperinflation</bdi>).",
    ],
    "rule": "<bdi>hypoxia</bdi> لا تستجيب للأكسجين بعد ضرر حاد، مع إيكو طبيعي، تعني صورة منتشرة ثنائية الجانب (<bdi>bilateral infiltrates</bdi>) تناسب <bdi>ARDS</bdi>؛ هذا السؤال بلا جواب مؤكد من المصدر فاعتمدنا هذا الاستنتاج الإكلينيكي.",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر نفسه كان متردد بين B و C؛ بالاعتماد على غياب العلامات القلبية (إيكو طبيعي) وصورة الـ<bdi>ARDS</bdi> المنتشرة اخترنا B كأقرب إجابة سريرية.",
},
"AS-0545": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "مولود <bdi>macrosomia</bdi> عنده <bdi>weak moro reflex</bdi>، والسؤال عن الخطوة الجاية.",
    "clues": [
        ("Macrosomia", "خطر <bdi>shoulder dystocia</bdi> أثناء الولادة"),
        ("weak moro reflex", "يرجح إصابة <bdi>brachial plexus</bdi> من جهة واحدة"),
    ],
    "why_correct": [
        "<bdi>macrosomia</bdi> يرفع خطر <bdi>shoulder dystocia</bdi> وإصابة <bdi>brachial plexus</bdi> (<bdi>Erb palsy</bdi>)، واللي تفسر <bdi>weak moro</bdi> من جهة واحدة.",
        "أغلب الحالات تتحسن تلقائياً، فالإدارة الأولى تحفظية: تثبيت الذراع بلطف وعناية داعمة، بعدها علاج طبيعي لمدى الحركة.",
        "الجراحة تُحجز فقط للحالات اللي ما تتحسن بعد عدة أشهر.",
    ],
    "when_changes": [
        "لو ما تحسنت حركة الذراع بعد 3 إلى 6 أشهر، الجواب يتجه لـ<bdi>surgical exploration</bdi>.",
        "لو الصورة كانت <bdi>jitteriness</bdi> عامة بدون ضعف جهة واحدة، نفكر بـ<bdi>hypoglycemia</bdi> أو <bdi>hypocalcemia</bdi> مو إصابة عصبية موضعية.",
    ],
    "rule": "ضعف منعكس من جهة واحدة يعني إصابة موضعية (عصب أو عظم)؛ ضعف منعكسات عام يوجه لسبب استقلابي أو مركزي.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0546": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "مولود <bdi>macrosomic</bdi> من أم سكرية غير منضبطة، بولادة طبيعية، وعنده ضعف بمنعكس <bdi>Moro</bdi> من جهة واحدة.",
    "clues": [
        ("uncontrolled DM", "خطورة أعلى لـ<bdi>shoulder dystocia</bdi>"),
        ("macrosomic baby", "وزن كبير يرفع خطر الإصابة بالولادة"),
        ("week moro reflex on the right side", "إصابة موضعية من جهة واحدة"),
    ],
    "why_correct": [
        "<bdi>macrosomia</bdi> من أم سكرية مع ولادة طبيعية يرفع خطر <bdi>shoulder dystocia</bdi> وإصابة <bdi>Erb palsy</bdi>.",
        "أغلب حالات <bdi>Erb palsy</bdi> تتحسن تلقائياً، فالإدارة الأولى تثبيت لطيف للذراع للراحة بالأيام الأولى، ثم علاج طبيعي لمدى الحركة لمنع التيبس.",
    ],
    "when_changes": [
        "لو ما رجعت حركة ثني المرفق بعد عدة أشهر من العلاج التحفظي، الجواب يصير جراحة.",
        "لو الصورة كانت ضعف عام بالطفل مع رعشة، الجواب يتجه لفحص <bdi>glucose</bdi> أول (خطر <bdi>hypoglycemia</bdi> بطفل أم سكرية).",
    ],
    "rule": "<bdi>Erb palsy</bdi> يدار تحفظياً أول؛ الجراحة فقط لو فشل التحسن بعد شهور.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0548": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "رضيع عمره شهرين عنده نوبات بكاء شديد لمدة 3 ساعات مع رفع الأرجل وغازات، ونموه وتغذيته طبيعية.",
    "clues": [
        ("2-month-old", "عمر نمطي للـ<bdi>colic</bdi>"),
        ("excessive crying, often lasting about 3 hours", "مدة البكاء تطابق قاعدة الـ3"),
        ("raises legs and passes gas", "صورة نمطية للـ<bdi>infantile colic</bdi>"),
        ("normal growth and feeding", "يستبعد سبب عضوي"),
    ],
    "why_correct": [
        "نوبات بكاء متكررة بهذا العمر مع رفع أرجل وغازات، والنمو والتغذية طبيعيين، هذا <bdi>infantile colic</bdi>، حالة حميدة تتحسن تلقائياً بعمر 3 إلى 4 شهور.",
        "الإدارة المناسبة <bdi>reassurance</bdi> للأهل مع نصائح تهدئة، وما يحتاج دواء أو فحوصات طالما الطفل ينمو طبيعي.",
    ],
    "when_changes": [
        "لو ظهرت علامات خطر مثل حمى، تقيؤ، دم بالبراز، أو ضعف بالنمو، الجواب يتغير للتحقيق عن سبب عضوي.",
        "لو السؤال يبي دواء، أي خيار دوائي (مثل <bdi>simethicone</bdi>) يبقى غير مناسب لأن الغاز نتيجة البكاء مو سببه.",
    ],
    "rule": "النمو والتغذية الطبيعية هي القرينة اللي تستبعد سبب عضوي، وأي خيار دوائي يصير مشتت.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0549": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفل عمره 4 سنوات بسعال ليلي متكرر، بعضه مرتبط بـ<bdi>URTI</bdi> وبعضه لا، ويتحسن مع البخاخ، والسؤال عن الخطوة الجاية.",
    "clues": [
        ("nocturnal cough", "سعال ليلي متكرر يرجح <bdi>asthma</bdi>"),
        ("similar episodes of the cough not preceded by URTI", "نوبات مستقلة عن العدوى"),
        ("relieved by inhaler", "استجابة لموسّع القصبات تدعم التشخيص"),
    ],
    "why_correct": [
        "سعال ليلي متكرر، بعضه بلا سبب عدوائي، ويتحسن بالبخاخ، كل هذا صورة <bdi>asthma</bdi> بطفل تحت 5 سنوات.",
        "تحت عمر 5 سنوات التشخيص إكلينيكي ومبني على الاستجابة للعلاج لأن <bdi>spirometry</bdi> غير موثوقة بهذا العمر، فالأعراض المتكررة الليلية تستدعي بدء <bdi>inhaled corticosteroids</bdi> كعلاج ضبط.",
    ],
    "when_changes": [
        "لو عمر الطفل 6 سنوات أو أكبر، الجواب يتجه لـ<bdi>spirometry</bdi> لتأكيد التشخيص.",
        "لو فيه علامات <bdi>foreign body</bdi> أو بؤرة محددة، الجواب يتجه لـ<bdi>chest X-ray</bdi>.",
    ],
    "rule": "العمر يحدد الطريق: طفل تحت 5 سنوات يُعطى تجربة <bdi>ICS</bdi>، وطفل أكبر أو بالغ يحتاج <bdi>spirometry</bdi> أول.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0551": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "طفل بألم بطني مع رفع الأرجل للصدر وبراز «<bdi>red currant jelly</bdi>»، وهذا <bdi>intussusception</bdi>، والسؤال عن أفضل طريقة للوقاية من حدوثه.",
    "clues": [
        ("bringing his legs to chest", "ألم كولكي نمطي"),
        ("red currant jelly stool", "علامة متأخرة لـ<bdi>intussusception</bdi>"),
        ("prevent", "السؤال عن الوقاية الأولية"),
    ],
    "why_correct": [
        "هذا الريكول مفتاحه <bdi>exclusive breastfeeding</bdi> كعامل حماية من <bdi>intussusception</bdi>، لأنه يقلل عدوى الجهاز الهضمي اللي تسبب تضخم لمفاوي معوي (السبب الشائع للحالة الأولية).",
        "من بين الخيارات المطروحة، هو الوحيد المصاغ كوقاية أولية حقيقية بعمر الرضاعة.",
    ],
    "when_changes": [
        "لو خيار <bdi>exclusive breastfeeding</bdi> غاب من الاختيارات، الجواب يتحول إلى تعليم الأهل عن الأعراض المبكرة.",
        "لو السؤال يبي علاج الحالة الحادة نفسها، الجواب يتجه لـ<bdi>ultrasound</bdi> للتشخيص و<bdi>enema reduction</bdi> للعلاج.",
    ],
    "rule": "تحقق من الخيارات المتوفرة: وجود <bdi>exclusive breastfeeding</bdi> يجعله المفتاح؛ غيابه يرجع المفتاح لتعليم الأعراض المبكرة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0552": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "نفس سيناريو <bdi>intussusception</bdi> لكن بدون خيار <bdi>exclusive breastfeeding</bdi>، فالمفتاح يتغير لتعليم الأعراض المبكرة.",
    "clues": [
        ("bringing his legs to chest", "ألم كولكي نمطي"),
        ("red currant jelly stool", "علامة متأخرة"),
        ("prevent", "السؤال عن الوقاية"),
    ],
    "why_correct": [
        "<bdi>intussusception</bdi> غالباً بلا سبب معروف (<bdi>idiopathic</bdi>) وما فيها وقاية أولية حقيقية، فـ«الوقاية» هنا تعني التعرف على الأعراض المبكرة بسرعة.",
        "التعرف المبكر يسمح بعلاج <bdi>enema reduction</bdi> قبل حدوث <bdi>ischaemia</bdi> أو <bdi>perforation</bdi> أو <bdi>shock</bdi>، ويساعد على رصد أي تكرار بسرعة.",
    ],
    "when_changes": [
        "لو ظهر خيار <bdi>exclusive breastfeeding</bdi> بنسخة أخرى من السؤال، يصير هو المفتاح لأنه وقاية أولية أقوى.",
        "لو السؤال عن علاج الحالة الحادة، الجواب يتجه لـ<bdi>ultrasound</bdi> والـ<bdi>enema reduction</bdi>.",
    ],
    "rule": "لما لا يمكن الوقاية من مرض، «الوقاية» بالسؤال تعني تقليل المضاعفات بالتعرف المبكر.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0553": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "حالة <bdi>pyloric stenosis</bdi>، والسؤال عن أهم إجراء وقائي من الأهل.",
    "clues": [
        ("pyloric stenosis", "تضخم عضلة البواب، بلا وقاية أولية حقيقية"),
        ("protective or preventive measures from parents", "السؤال عن دور الأهل"),
    ],
    "why_correct": [
        "<bdi>pyloric stenosis</bdi> تضخم عضلي بلا سبب يمكن الوقاية منه، فأهم إجراء هو تعليم الأهل عن الأعراض المبكرة: تقيؤ <bdi>projectile</bdi> غير صفراوي بعمر 2 إلى 8 أسابيع، وجوع الرضيع بعد التقيؤ، وضعف زيادة الوزن.",
        "التعرف المبكر يسمح بتشخيص سريع بالـ<bdi>ultrasound</bdi> وعلاج بـ<bdi>pyloromyotomy</bdi> قبل حدوث جفاف شديد واضطراب كيميائي.",
    ],
    "when_changes": [
        "لو السؤال عن سبب يمكن الوقاية منه فعلياً، الجواب يختلف لأن <bdi>pyloric stenosis</bdi> ليس له وقاية أولية حقيقية.",
        "لو السؤال عن علاج الحالة الحادة، الجواب يتجه لتصحيح السوائل والكهارل أول ثم الجراحة.",
    ],
    "rule": "تقيؤ <bdi>projectile</bdi> غير صفراوي مع جوع الرضيع يعني <bdi>pyloric stenosis</bdi>؛ تقيؤ هادئ بطفل ينمو طبيعي يعني <bdi>reflux</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0554": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "طفل بـ<bdi>cystic fibrosis</bdi> تسأل أمه عن أمان لعبه مع طفل آخر عنده <bdi>cystic fibrosis</bdi> أيضاً.",
    "clues": [
        ("cystic fibrosis", "خطر انتقال جراثيم بين مرضى CF"),
        ("play with another child who also has cystic fibrosis", "تواصل مباشر بين طفلين CF"),
    ],
    "why_correct": [
        "مرضى <bdi>cystic fibrosis</bdi> يحملون جراثيم مثل <bdi>Pseudomonas aeruginosa</bdi> و<bdi>Burkholderia cepacia</bdi> تنتقل بسهولة بين مرضى CF وتسرّع تدهور الرئة.",
        "لذلك النصيحة المعيارية تجنب التواصل القريب بين مرضى CF (مسافة، عدم مشاركة أدوات أو لعب قريب)، فالجواب هنا لا.",
    ],
    "when_changes": [
        "لو كان الطفل الآخر سليم بلا CF، اللعب معه مسموح مع نظافة يدين جيدة.",
        "لو السؤال عن تقليل العدوى بشكل عام بالمدرسة، الجواب يتجه لـ<bdi>influenza vaccine</bdi>.",
    ],
    "rule": "الخطر هو من مريض CF لمريض CF آخر، مو من طفل CF لطفل سليم.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0555": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفلة عمرها 7 سنوات بـ<bdi>cystic fibrosis</bdi> تلعب مع طفل آخر عنده نفس المرض، والسؤال عن الأنسب.",
    "clues": [
        ("cystic fibrosis", "خطر انتقال جراثيم بين مرضى CF"),
        ("playing with other child with cystic fibrosis", "تواصل مباشر بين مريضين"),
    ],
    "why_correct": [
        "التواصل القريب بين طفلين عندهم <bdi>cystic fibrosis</bdi> يسمح بانتقال جراثيم مثل <bdi>Pseudomonas aeruginosa</bdi> و<bdi>Burkholderia cepacia</bdi> وتسريع ضرر الرئة.",
        "الإجراء المناسب فصلهما والتوصية بتجنب التواصل القريب بين مرضى CF.",
    ],
    "when_changes": [
        "لو السؤال عن طريقة لتقليل العدوى عند دخول المدرسة، الجواب يتجه لـ<bdi>influenza vaccine</bdi>.",
        "لو الطفل الآخر سليم، اللعب مسموح.",
    ],
    "rule": "<bdi>influenza vaccine</bdi> صحيح لتقليل العدوى عموماً، لكنه غلط لما السؤال يكون عن طفلين CF مع بعض؛ الجواب هنا فصل.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0556": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفل بـ<bdi>cystic fibrosis</bdi> عنده عدوى رئوية متكررة رغم العلاج التنظيفي، وبيبدأ المدرسة، والسؤال عن طريقة تقليل تكرار العدوى.",
    "clues": [
        ("cystic fibrosis", "خطر تكرار عدوى رئوية"),
        ("recurrent Pulmonary Infections", "رغم العلاج التنظيفي"),
        ("start to go school", "تعرض أكبر للفيروسات بالمدرسة"),
    ],
    "why_correct": [
        "الذهاب للمدرسة يرفع التعرض للفيروسات التنفسية، والـ<bdi>influenza</bdi> يحرّض نوبات تفاقم بمرضى CF.",
        "<bdi>annual inactivated influenza vaccine</bdi> للطفل وأهل بيته توصية معيارية تقلل هذه العدوى دون تقييد حياته الطبيعية.",
    ],
    "when_changes": [
        "لو السؤال عن طريقة تقليل انتقال الجراثيم بين طفلين CF، الجواب يتجه للفصل بينهم.",
        "لو العدوى مستمرة رغم كل الإجراءات، يراجع نظام العلاج التنظيفي والأدوية الاستنشاقية.",
    ],
    "rule": "تكرار العدوى مع تعرض جديد بالمدرسة يوجه للتلقيح، مو للعزل أو لزيادة نفس العلاج فقط.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0564": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "طفل عمره 9 سنوات بألم متزايد بالساقين مع قلة نشاط خارجي وتعب، وفحصه طبيعي، والتغذية جيدة؛ الصورة توجه لنقص <bdi>vitamin D</bdi>.",
    "clues": [
        ("9-year-old", "عمر مدرسي"),
        ("bilateral leg pain", "ألم عظمي ثنائي متدرج"),
        ("spent less time in outdoor activities", "قلة تعرض للشمس"),
        ("good diet and appetite", "يستبعد سوء تغذية"),
    ],
    "why_correct": [
        "ألم ساقين متزايد مع قلة تعرض للشمس وتعب، وفحص طبيعي، وتغذية جيدة، هذا يرجح نقص <bdi>vitamin D</bdi> بسبب قلة الشمس.",
        "علاج نقص <bdi>vitamin D</bdi> العرضي يكون بإعطاء <bdi>calcium</bdi> مع <bdi>vitamin D</bdi> مع للمساعدة باستعادة التمعدن العظمي، وهذا مفتاح هذا الريكول.",
    ],
    "when_changes": [
        "لو الفحص غير طبيعي (تورم، تشوه)، الجواب يتجه لتحويل عظمي.",
        "لو الألم ليلي فقط مع نشاط نهاري طبيعي وبلا تعب، الجواب يتجه لـ<bdi>growing pains</bdi>.",
    ],
    "rule": "قلة التعرض للشمس هي القرينة الخفية لنقص <bdi>vitamin D</bdi>؛ الفحص الطبيعي مع الألم المتدرج والتعب يبعد السبب العظمي الهيكلي.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0569": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفل عمره 3 سنوات بسوء تغذية و<bdi>hematuria</bdi> مع كتلة بطنية كبيرة وانخفاض دخول الهواء بالصدر، والسؤال عن أهم فحص بتقييم المرض.",
    "clues": [
        ("3-year-old", "عمر نمطي لـ<bdi>Wilms tumor</bdi>"),
        ("hematuria", "يرجح مصدر كلوي"),
        ("large abdominal mass", "كتلة ضخمة بالبطن"),
        ("decreased air entry in multiple areas", "يرجح انتشار رئوي"),
    ],
    "why_correct": [
        "<bdi>hematuria</bdi> مع كتلة بطنية كبيرة بهذا العمر يرجح <bdi>Wilms tumor</bdi>، وانخفاض دخول الهواء يرجح انتشار للرئة.",
        "الـ<bdi>abdominal ultrasound</bdi> هو الفحص الأهم الأول: يأكد إن الكتلة من الكلية، ويفحص الكلية الثانية والوريد الكلوي والـ<bdi>IVC</bdi> لوجود خثرة ورمية، قبل الـ<bdi>CT</bdi> للتدريج.",
    ],
    "when_changes": [
        "لو الكتلة تعبر خط الوسط مع تكلّس، الصورة تتجه لـ<bdi>neuroblastoma</bdi> مو <bdi>Wilms tumor</bdi>.",
        "لو السؤال عن تدريج الانتشار الرئوي بعد تأكيد التشخيص، الجواب يتجه لـ<bdi>chest CT</bdi>.",
    ],
    "rule": "<bdi>hematuria</bdi> مع كتلة بطنية يعني <bdi>Wilms tumor</bdi>: صوّر الكلية أول؛ <bdi>bone marrow aspiration</bdi> يخص <bdi>neuroblastoma</bdi> أو <bdi>leukemia</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
}

WHY_WRONG = {
"AS-0512": {
    "A": "الـ<bdi>MRI</bdi> بديل مقبول للتصوير العرضي (بلا إشعاع، وأفضل لامتداد القناة الشوكية)، لكن الجواب المعتمد للخطوة الجاية هو <bdi>CT</bdi> وهو الأفضل بإظهار التكلّس.",
    "C": "الـ<bdi>biopsy</bdi> يعطي التشخيص النهائي لكنه يجي بعد ما الـ<bdi>CT</bdi> يحدد شكل الكتلة؛ هو الجواب فقط لو غابت كلمة Next.",
},
"AS-0512B": {
    "A": "الـ<bdi>MRI</bdi> بديل بعض المراكز خصوصاً مع امتداد شوكي مشتبه، لكن <bdi>CT</bdi> هو إجابة الامتحان المعتادة للخطوة الجاية.",
    "C": "الـ<bdi>biopsy</bdi> يعطي التشخيص النسيجي لكنه يجي بعد ما الـ<bdi>CT</bdi> يحدد الآفة؛ هو الجواب لو السؤال عن تأكيد التشخيص.",
    "D": "<bdi>bone marrow aspiration</bdi> خطوة <bdi>staging</bdi> لـ<bdi>neuroblastoma</bdi> بعد ما يتوصف الورم الأساسي، مو أول فحص لكتلة <bdi>flank</bdi> لوحدها.",
},
"AS-0513": {
    "A": "الـ<bdi>MRI</bdi> يوصّف الكتلة ويدرّجها لكنه ما يعطي تشخيص نسيجي؛ هو بديل لـ<bdi>CT</bdi> كخطوة تصوير جاية.",
    "B": "<bdi>CT</bdi> هو الجواب الصحيح لو السؤال عن الخطوة الجاية (<bdi>Next</bdi>) بعد الـ<bdi>ultrasound</bdi>؛ هو يوصّف الكتلة بس ما يثبت نوعها.",
},
"AS-0514": {
    "A": "الـ<bdi>MRI</bdi> لوحده مجرد بديل تصوير لـ<bdi>CT</bdi>؛ يوصّف الكتلة بس ما يعطي تشخيص نسيجي، فما يكفي لوحده للوصول للتشخيص.",
},
"AS-0515": {
    "B": "الـ<bdi>biopsy</bdi> ما يعتبر أول فحص تشخيصي لكتلة صغيرة بطفل سليم؛ هو الخطوة اللي تجي بعد التصوير لو كان هناك اشتباه بخباثة.",
    "C": "الـ<bdi>ultrasound</bdi> هو الفحص الأولي النمطي بدون إشعاع للكتلة البطنية عند طفل؛ هو الجواب لو السؤال كان عن الفحص «الأولي».",
    "D": "الـ<bdi>MRI</bdi> بديل لتصوير عرضي يوفر تفصيل بدون إشعاع، لكنه ليس مفتاح هذا الريكول.",
},
"AS-0516": {
    "A": "الـ<bdi>CT</bdi> يحدد مصدر الكتلة وامتدادها وهو الجواب الصحيح للخطوة الجاية بعد التصوير الأولي، لكنه ما يثبت نوع الورم نسيجياً.",
    "B": "الـ<bdi>ultrasound</bdi> يأكد وجود الكتلة ويحدد لو كانت صلبة أو كيسية، وهو الجواب الصحيح لو السؤال عن الفحص الأولي، لكنه ما يؤكد التشخيص.",
},
"AS-0538": {
    "A": "علاج فموي مناسب لـ<bdi>cellulitis</bdi> محدودة بدون حمى؛ الأدوية الموضعية ليس لها دور بـ<bdi>cellulitis</bdi> أصلاً (تخص <bdi>impetigo</bdi> السطحي)، وهنا الحمى والتوسع يحتاجان علاج وريدي.",
    "B": "علاج فموي مع متابعة خارجية يناسب <bdi>cellulitis</bdi> خفيفة بطفل سليم بدون حمى؛ هذا الطفل محموم ومتوسع الالتهاب، فالعلاج الخارجي غير كافٍ.",
},
"AS-0545": {
    "B": "الجراحة (استكشاف أو إصلاح العصب) تُحجز فقط لو ما تحسنت الوظيفة بعد 3 إلى 6 شهور تقريباً، مو كخطوة أولى بمولود.",
    "C": "<bdi>calcium supplements</bdi> تعالج <bdi>neonatal hypocalcemia</bdi> (مثل مولود أم سكرية) اللي تسبب رعشة أو تشنج، مو ضعف منعكس من جهة واحدة.",
    "D": "<bdi>dextrose</bdi> تعالج <bdi>neonatal hypoglycemia</bdi> الشائعة بمواليد <bdi>macrosomic</bdi>، لكنها تعطي رعشة وضعف عام مو ضعف منعكس موضعي.",
},
"AS-0546": {
    "A": "الجراحة تُحجز للحالات اللي ما تتحسن بعد عدة شهور من العلاج التحفظي، مو كخطوة أولى بمولود جديد.",
    "B": "<bdi>IV dextrose</bdi> تعالج <bdi>neonatal hypoglycemia</bdi>، لكنها تعطي صورة رعشة وضعف تغذية عامة متناظرة، مو ضعف منعكس من جهة واحدة.",
},
"AS-0548": {
    "C": "<bdi>simethicone</bdi> ليس له فائدة مؤكدة أكثر من <bdi>placebo</bdi> بالـ<bdi>colic</bdi>؛ الغاز نتيجة البكاء وبلع الهواء مو السبب الأساسي، فالدواء ليس الإدارة الأفضل.",
},
"AS-0549": {
    "A": "<bdi>chest X-ray</bdi> ما يحتاجه <bdi>asthma</bdi> النمطي؛ يستخدم عند اشتباه <bdi>foreign body</bdi> أو <bdi>pneumonia</bdi> أو آفة هيكلية.",
    "B": "<bdi>spirometry</bdi> تؤكد <bdi>asthma</bdi> من عمر 6 سنوات تقريباً فأكبر؛ طفل عمره 4 سنوات غالباً ما يقدر ينفذ المناورة بدقة.",
},
"AS-0551": {
    "A": "تعليم الأعراض المبكرة ما يمنع حدوث <bdi>intussusception</bdi> من الأساس؛ يسمح فقط بتقديم العرض أسرع والعلاج بـ<bdi>enema</bdi> قبل حدوث ضرر، وهو مفتاح النسخة بلا خيار <bdi>breastfeeding</bdi>.",
    "B": "<bdi>high fiber diet</bdi> تمنع الإمساك، لا تمنع <bdi>intussusception</bdi>، وليست ذات صلة بالرضع بهذا العمر.",
    "C": "النشاط الجسدي ما له دور بالوقاية من <bdi>intussusception</bdi>.",
},
"AS-0552": {
    "B": "<bdi>high fiber diet</bdi> تمنع الإمساك، لا تمنع <bdi>intussusception</bdi>، وليست ذات علاقة بالتضخم اللمفاوي المسبب للحالة.",
    "C": "النشاط الجسدي بعمر الرضاعة ما له دور بالوقاية من <bdi>intussusception</bdi> أو مضاعفاتها.",
},
"AS-0553": {
    "B": "زيادة الألياف غير مهمة برضيع صغير وتعالج الإمساك، مو انسداد مخرج المعدة.",
    "C": "أدوية الـ<bdi>reflux</bdi> تعالج <bdi>GERD</bdi> (ارتجاع هادئ بطفل ينمو جيد)، ولا تمنع أو تعالج تضخم عضلة البواب.",
},
"AS-0554": {
    "A": "اللعب الحر يسمح بانتقال الجراثيم بالتلامس وبالرذاذ بين مرضى CF، وهذا عكس المطلوب بإجراءات ضبط العدوى.",
    "C": "وجود المضاد الحيوي لا يُزيل الاستعمار الجرثومي ولا يجعل التواصل آمن؛ الجراثيم المقاومة ممكن تنتقل حتى مع العلاج.",
    "D": "الكمامات تقلل بس ما تمنع الانتقال بالكامل وما تعالج انتقال التلامس؛ التوصية الأساسية تجنب التواصل القريب كلياً.",
},
"AS-0555": {
    "A": "الكمامة تقلل الخطر لكنها لا تزيله، واللعب القريب يسمح بانتقال التلامس؛ التوصية هي الفصل.",
    "B": "<bdi>influenza vaccine</bdi> موصى به سنوياً لكل مرضى CF، لكنه لا يحمي من انتقال جراثيم مثل <bdi>Pseudomonas</bdi> أو <bdi>Burkholderia</bdi> بين الطفلين.",
},
"AS-0556": {
    "A": "منع الطفل من المدرسة غير موصى به؛ أطفال CF يحضرون المدرسة مع نظافة يدين وتلقيح، والتقييد فقط مع مرضى CF آخرين.",
    "B": "السؤال يذكر إن العدوى تتكرر «رغم» العلاج التنظيفي، فمجرد زيادته لا يعالج خطر التعرض الجديد بالمدرسة.",
},
"AS-0564": {
    "A": "تحويل العظمية يخص مشاكل هيكلية أو علامات خطر (عرج، تورم، تشوه، فحص غير طبيعي)؛ الفحص هنا طبيعي.",
    "B": "زيادة النشاط الخارجي وحده نصيحة داعمة فقط ولا يعالج نقص فيتامين راسخ أعطى أعراض لمدة 3 شهور.",
    "C": "التعرض للشمس نصيحة سليمة، لكن الخيار المعتمد بهذا الريكول يجمع <bdi>vitamin D</bdi> مع <bdi>calcium</bdi> لعلاج النقص العرضي حتى مع تغذية ظاهرها جيد.",
},
"AS-0569": {
    "A": "<bdi>chest CT</bdi> يستخدم لتدريج انتشار رئوي بعد تأكيد <bdi>Wilms</bdi>، لكنه لا يوصّف الكتلة البطنية الأساسية.",
    "B": "<bdi>bone marrow aspiration</bdi> خطوة تدريج لـ<bdi>neuroblastoma</bdi> (ينتشر للنخاع والعظم)؛ <bdi>Wilms tumor</bdi> نادراً يصيب النخاع، و<bdi>hematuria</bdi> ترجح مصدر كلوي.",
},
}

HIGHLIGHT_TERMS = {
"AS-0512": ["mass in the abdomen in the left flank", "internal calcification", "Next test"],
"AS-0512B": ["3 year old child", "large mass on his flank", "soft tissue mass with internal calcifications"],
"AS-0513": ["mass in the abdomen in the left flank", "internal calcification", "reach the diagnosis"],
"AS-0514": ["mass in the abdomen in the left flank", "internal calcification", "reach the diagnosis"],
"AS-0515": ["2 cm skin colored painless abdominal mass", "Diagnostic test"],
"AS-0516": ["huge palpable abdominal mass", "CONFIRM"],
"AS-0538": ["fever and irritability", "red warm Painful Tender swelling", "no pus or abscess", "area is Enlarging"],
"AS-0541": ["10-year-old", "progressive respiratory distress", "after severe pneumonia", "no improvements still hypoxia", "echo normal"],
"AS-0545": ["Macrosomia", "weak moro reflux"],
"AS-0546": ["uncontrolled DM", "macrosomic baby", "week moro reflex on the right side"],
"AS-0548": ["2-month-old", "excessive crying, often lasting about 3 hours", "raises legs and passes gas", "normal growth and feeding"],
"AS-0549": ["nocturnal cough", "similar episodes of the cough not preceded by URTI", "relieved by inhaler"],
"AS-0551": ["bringing his legs to chest", "red currant jelly stool", "prevent"],
"AS-0552": ["bringing his legs to chest", "red currant jelly stool", "prevent"],
"AS-0553": ["pyloric stenosis", "protective or preventive measures from parents"],
"AS-0554": ["cystic fibrosis", "play with another child who also has cystic fibrosis"],
"AS-0555": ["cystic fibrosis", "playing with other child with cystic fibrosis"],
"AS-0556": ["cystic fibrosis", "recurrent Pulmonary Infections", "start to go school"],
"AS-0564": ["9-year-old", "bilateral leg pain", "spent less time in outdoor activities", "good diet and appetite"],
"AS-0569": ["3-year-old", "hematuria", "large abdominal mass", "decreased air entry in multiple areas"],
}
