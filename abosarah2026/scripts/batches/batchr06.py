# -*- coding: utf-8 -*-
# Batch r06 (OBGYN + Medicine recalls, 141 questions)

EXPLANATIONS = {
"AS-2251": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "السؤال يبي <bdi>diagnosis</bdi> حسب <bdi>timing</bdi> الأعراض بالنسبة للدورة: قبل الدورة ولا مع الدورة.",
    "clues": [
        ("headache, anxiety, and mastalgia", "أعراض <bdi>luteal phase</bdi> (صداع، قلق، ألم بالثدي)"),
        ("start 8-10 days before menstruation and improve afterward", "تبدأ قبل الدورة وتتحسن بعدها = النمط المعرّف لـ<bdi>PMS</bdi>"),
    ],
    "why_correct": [
        "الأعراض تبدأ <bdi>8-10 days</bdi> قبل الدورة وتتحسن بعد بدايتها، وهذا هو النمط المعرّف لـ<bdi>Premenstrual Tension Syndrome (PMS)</bdi>: أعراض <bdi>luteal phase</bdi> تروح مع الدورة.",
        "المريضة <bdi>healthy</bdi> والأعراض <bdi>recurrent</bdi> ودوريّة، فـ<bdi>PMS</bdi> يصير <bdi>clinical diagnosis</bdi> يعتمد على التوقيت بدون أي <bdi>lab</bdi> أو <bdi>imaging</bdi>.",
    ],
    "when_changes": [
        "لو الألم يبدأ مع أول يوم من الدورة نفسها (مو قبلها)، الجواب يصير <bdi>primary dysmenorrhea</bdi>.",
        "لو فيه <bdi>dyspareunia</bdi> و<bdi>infertility</bdi> مع الألم، فكر في <bdi>endometriosis</bdi>.",
    ],
    "rule": "الأعراض اللي تبدأ قبل الدورة وتتحسن معها دايمًا تودي لـ<bdi>PMS</bdi>؛ الألم اللي يبدأ مع الدورة يودي لـ<bdi>dysmenorrhea</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2252": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "السؤال تفريق بين <bdi>primary dysmenorrhea</bdi> و<bdi>secondary dysmenorrhea</bdi> و<bdi>PMS</bdi> حسب التوقيت و<bdi>physical exam</bdi>.",
    "clues": [
        ("19-year-old", "<bdi>young patient</bdi> بدون <bdi>pelvic pathology</bdi>"),
        ("beginning with the onset of menses", "الألم يبدأ مع الدورة = مو <bdi>PMS</bdi>"),
        ("no pain between menses", "يدعم <bdi>primary dysmenorrhea</bdi> ويبعد <bdi>secondary</bdi>"),
        ("Physical examination normal", "يبعد أي <bdi>pelvic pathology</bdi>"),
    ],
    "why_correct": [
        "<bdi>crampy pain</bdi> تبدأ <bdi>مع</bdi> الدورة وتستمر يومين-ثلاثة، مع إشعاع للظهر والفخذين وغثيان وتعب وصداع، و<bdi>exam</bdi> <bdi>normal</bdi>: هذا الوصف الكلاسيكي لـ<bdi>primary dysmenorrhea</bdi> (سببها <bdi>prostaglandins</bdi> بدون أي <bdi>pelvic pathology</bdi>).",
        "عمرها <bdi>19</bdi> وما فيه ألم بين الدورات، وهذا يختلف عن <bdi>secondary dysmenorrhea</bdi> اللي يجي بعمر أكبر مع <bdi>abnormal exam</bdi>.",
    ],
    "when_changes": [
        "لو الألم يبدأ قبل الدورة ويتحسن معها، الجواب يصير <bdi>premenstrual syndrome</bdi>.",
        "لو فيه <bdi>dyspareunia</bdi> أو <bdi>abnormal exam</bdi> (مثل <bdi>fixed uterus</bdi>)، الجواب يصير <bdi>endometriosis</bdi> أو <bdi>secondary dysmenorrhea</bdi>.",
    ],
    "rule": "ألم يبدأ مع الدورة + <bdi>exam</bdi> طبيعي + <bdi>young patient</bdi> = <bdi>primary dysmenorrhea</bdi>، والعلاج الأول <bdi>NSAIDs</bdi> ثم <bdi>COCP</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2255": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "السؤال عن أشهر سبب لـ<bdi>secondary amenorrhea</bdi> بعد استبعاد <bdi>ovarian failure</bdi> و<bdi>hyperprolactinemia</bdi>.",
    "clues": [
        ("secondary amenorrhea for 6 month", "انقطاع الدورة لمدة كافية لتشخيص <bdi>secondary amenorrhea</bdi>"),
        ("normal FSH and prolactin", "يستبعد <bdi>ovarian failure</bdi> و<bdi>hyperprolactinemia</bdi>"),
    ],
    "why_correct": [
        "<bdi>normal FSH</bdi> يستبعد <bdi>premature ovarian failure</bdi>، و<bdi>normal prolactin</bdi> يستبعد <bdi>hyperprolactinemia</bdi>.",
        "من اللي تبقى، <bdi>PCOS</bdi> هو أشهر سبب <bdi>endocrine</bdi> لـ<bdi>secondary amenorrhea</bdi> بهذا العمر، وعادة يجي مع <bdi>normal FSH</bdi> (و<bdi>LH</bdi> مرتفع أحيانًا).",
    ],
    "when_changes": [
        "لو ما كان فيه خيار <bdi>PCOS</bdi> بالأسئلة، الجواب يصير <bdi>HPO axis failure</bdi> (<bdi>hypogonadotropic</bdi>).",
        "لو <bdi>FSH</bdi> مرتفع، الجواب يصير <bdi>premature ovarian failure</bdi>.",
    ],
    "rule": "في <bdi>secondary amenorrhea</bdi> بعد استبعاد الحمل: تحقق من <bdi>FSH</bdi> و<bdi>prolactin</bdi> و<bdi>TSH</bdi>؛ طبيعيين = فكر في <bdi>PCOS</bdi> أولًا.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2256": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "<bdi>primary amenorrhea</bdi> مع <bdi>breast development</bdi> طبيعي يعني <bdi>estrogen</bdi> موجود، فالمشكلة في <bdi>outflow tract</bdi> مو بالمبيض.",
    "clues": [
        ("primary amenorrhea", "لم تحصل أي دورة من قبل"),
        ("present breast development and secondary characteristics", "<bdi>estrogen</bdi> طبيعي من المبيض"),
    ],
    "why_correct": [
        "وجود <bdi>breast development</bdi> و<bdi>secondary sexual characteristics</bdi> طبيعية يعني المبيض يصنع <bdi>estrogen</bdi> بشكل طبيعي، فالمشكلة بعد المبيض.",
        "<bdi>Mullerian agenesis (MRKH)</bdi> هي <bdi>46,XX</bdi> بمبايض طبيعية لكن <bdi>absent uterus</bdi> و<bdi>upper vagina</bdi>، وهذا السبب الكلاسيكي لهذا النمط.",
    ],
    "when_changes": [
        "لو <bdi>breast development</bdi> غائب مع <bdi>high FSH</bdi>، الجواب يصير <bdi>gonadal dysgenesis</bdi> (مثل <bdi>Turner</bdi>).",
        "لو فيه <bdi>pubic hair</bdi> قليل مع <bdi>testosterone</bdi> ذكري، الجواب يصير <bdi>androgen insensitivity</bdi> مو <bdi>MRKH</bdi>.",
    ],
    "rule": "<bdi>breasts</bdi> موجودة + <bdi>uterus</bdi> غائب + <bdi>pubic hair</bdi> طبيعي = <bdi>Mullerian agenesis</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2262": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>IUFD</bdi> في <bdi>second trimester</bdi>: السؤال عن الدواء المستخدم لتحفيز الولادة بما إن الرحم ما زال غير حساس للأوكسيتوسين.",
    "clues": [
        ("24 weeks' gestation", "<bdi>mid-trimester</bdi>، الرحم أقل حساسية لـ<bdi>oxytocin receptors</bdi>"),
        ("intrauterine fetal death", "تأكد عدم وجود <bdi>cardiac activity</bdi>"),
        ("induce labor", "السؤال عن <bdi>induction agent</bdi>"),
    ],
    "why_correct": [
        "عند <bdi>24 weeks</bdi> مستقبلات <bdi>oxytocin</bdi> بالرحم قليلة، فـ<bdi>misoprostol</bdi> هو الدواء الرئيسي لأنه ينضّج عنق الرحم ويحفّز التقلصات بفعالية بهذا العمر.",
        "المريضة <bdi>stable</bdi> فالخطة هي <bdi>vaginal delivery</bdi> عن طريق <bdi>medical induction</bdi>.",
    ],
    "when_changes": [
        "لو كانت عند <bdi>term</bdi> (قريب من 40 أسبوع)، <bdi>oxytocin</bdi> يصير فعّال أكثر ويستخدم لتحفيز أو تعزيز الولادة.",
        "لو فيه تاريخ ولادة قيصرية سابقة (<bdi>classical scar</bdi>)، يُتجنب <bdi>misoprostol</bdi> بجرعات عالية بسبب خطر تمزق الرحم.",
    ],
    "rule": "<bdi>mifepristone</bdi> يحضّر الرحم و<bdi>misoprostol</bdi> يحفز الولادة؛ عند السؤال عن دواء التحفيز بعد <bdi>IUFD</bdi> منتصف الحمل، الجواب <bdi>misoprostol</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2270": {
    "correct_letter": "B",
    "self_judged": True,
    "idea": "<bdi>imperforate hymen</bdi> بعد عملية <bdi>hymenotomy</bdi>: السؤال عن الدواء الوقائي بعد الإجراء من بين الخيارات المتاحة.",
    "clues": [
        ("amenorrhea", "<bdi>primary amenorrhea</bdi> بسبب انسداد المخرج"),
        ("mass felt from vagina during DRE", "<bdi>hematocolpos</bdi> محسوس كـ<bdi>mass</bdi>"),
        ("Diagonal incision across the hymen", "علاج <bdi>imperforate hymen</bdi> بـ<bdi>hymenotomy</bdi>"),
    ],
    "why_correct": [
        "بعد تصريف <bdi>hematocolpos</bdi> بواسطة <bdi>hymenotomy</bdi>، الإجراء بسيط ونظيف، وأقرب خيار متاح من ناحية الوقاية من العدوى بعد الإجراء هو <bdi>prophylactic antibiotics post procedure</bdi>.",
        "المصدر نفسه يذكر إن الجواب الحقيقي المفترض (<bdi>topical estrogen</bdi> لمساعدة التئام الفتحة) غير موجود بالخيارات، لذا هذا <bdi>self-judged</bdi> من بين المتاح.",
    ],
    "when_changes": [
        "لو كان الخيار <bdi>topical estrogen</bdi> موجود، هو الأقرب للهدف الحقيقي (الحفاظ على الفتحة مفتوحة أثناء الالتئام).",
        "لو صار <bdi>pyocolpos</bdi> (عدوى) مؤكد، تصير المضادات الحيوية ضرورية فعليًا لا وقائية فقط.",
    ],
    "rule": "<bdi>imperforate hymen</bdi>: العلاج <bdi>hymenotomy</bdi>، والهدف بعد العملية هو إبقاء الفتحة سالكة أثناء الالتئام.",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر لم يعتمد جوابًا مؤكدًا (<bdi>answer_letter</bdi> غير موجود)، والجواب الأصلي المذكور بالمصدر (<bdi>topical estrogen</bdi>) غير مطروح بالخيارات، فاخترنا <bdi>prophylactic antibiotics</bdi> كأقرب خيار متاح.",
},
"AS-2272": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "<bdi>retained placenta</bdi> بعد 30 دقيقة: السؤال عن الدواء الأنسب بين خيارين فقط (<bdi>oxytocin</bdi> مقابل <bdi>ergometrine</bdi>).",
    "clues": [
        ("retained placenta for 30 min", "الوقت الحرج لبدء التدخل الدوائي قبل <bdi>manual removal</bdi>"),
    ],
    "why_correct": [
        "<bdi>IV oxytocin</bdi> يعطي تقلصات منتظمة تساعد على انفصال وطرد المشيمة وتقلل النزيف، وهو الخيار الآمن بين الاثنين.",
        "الهدف من السؤال هو تمييز <bdi>oxytocin</bdi> الآمن عن <bdi>ergometrine</bdi> الخطير بهذا الموقف.",
    ],
    "when_changes": [
        "لو استمرت المشيمة محتجزة بعد التدخل الدوائي، الخطوة التالية <bdi>manual removal</bdi> تحت <bdi>anesthesia</bdi>.",
        "لو فيه <bdi>hypertension</bdi>، <bdi>ergometrine</bdi> يصير <bdi>contraindicated</bdi> بشكل أوضح.",
    ],
    "rule": "في <bdi>retained placenta</bdi>: <bdi>oxytocin</bdi> هو الخيار الآمن؛ <bdi>ergometrine</bdi> يسبب تقلص مستمر بعنق الرحم قد يحبس المشيمة وهو <bdi>contraindicated</bdi> بـ<bdi>hypertension</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2275": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "اختيار الدواء المضاد للدرقية حسب <bdi>trimester</bdi> من الحمل في <bdi>hyperthyroidism</bdi>.",
    "clues": [
        ("9 weeks gestation", "<bdi>first trimester</bdi>، فترة <bdi>organogenesis</bdi>"),
        ("hyperthyroidism", "تحتاج <bdi>antithyroid drug</bdi>"),
    ],
    "why_correct": [
        "عند <bdi>9 weeks</bdi> (<bdi>first trimester</bdi>)، <bdi>PTU</bdi> هو الدواء المفضل لأن <bdi>methimazole</bdi> يحمل خطر أعلى لـ<bdi>embryopathy</bdi> أثناء تكوّن الأعضاء.",
        "<bdi>eye protrusion</bdi> غير موجود لكنه لا يغيّر الاختيار؛ القرار يعتمد فقط على <bdi>trimester</bdi>.",
    ],
    "when_changes": [
        "بعد <bdi>12-13 weeks</bdi> (<bdi>second trimester</bdi> فصاعدًا)، يتم التحويل إلى <bdi>methimazole</bdi> لتجنب سمية الكبد من <bdi>PTU</bdi>.",
        "لو كانت الحالة شديدة ولم تستجب للأدوية أو عدم تحمل، يُنظر بـ<bdi>thyroidectomy</bdi> في <bdi>second trimester</bdi>.",
    ],
    "rule": "قبل حوالي <bdi>12-13 weeks</bdi>: <bdi>PTU</bdi>؛ بعدها: <bdi>methimazole</bdi>؛ <bdi>radioactive iodine</bdi> ممنوع تمامًا بالحمل.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2284": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>PPROM</bdi> مع ظهور <bdi>fever</bdi> و<bdi>abdominal pain</bdi>: السؤال عن التشخيص الأكثر احتمالاً.",
    "clues": [
        ("30 weeks", "عمر حمل <bdi>preterm</bdi>"),
        ("preterm premature rupture of membranes", "مخاطرة عالية لعدوى صاعدة"),
        ("fever and abdominal pain", "علامات <bdi>intrauterine infection</bdi>"),
    ],
    "why_correct": [
        "<bdi>PPROM</bdi> لمدة 3 أيام مع إدارة <bdi>expectant</bdi> هو عامل خطر رئيسي لعدوى صاعدة، وظهور <bdi>fever</bdi> و<bdi>abdominal pain</bdi> يعني <bdi>chorioamnionitis</bdi> حتى يثبت العكس.",
        "علامات داعمة أخرى: <bdi>uterine tenderness</bdi>، إفرازات كريهة، وتسرّع نبض الأم أو الجنين.",
    ],
    "when_changes": [
        "لو فيه ألم وبدون <bdi>fever</bdi> بس مع تقلصات منتظمة، الجواب يصير <bdi>labor</bdi>.",
        "لو فيه نزيف مؤلم مع رحم متشنج، الجواب يصير <bdi>placental abruption</bdi>.",
    ],
    "rule": "<bdi>fever</bdi> بعد <bdi>PPROM</bdi> يحوّل الحالة إلى <bdi>chorioamnionitis</bdi>؛ بدون <bdi>fever</bdi> أو نزيف فكّر بـ<bdi>labor</bdi> فقط.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2284B": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "بعد تشخيص <bdi>chorioamnionitis</bdi>، السؤال عن الخطوة التالية الصحيحة بالعلاج.",
    "clues": [
        ("preterm premature rupture of membranes", "<bdi>chorioamnionitis</bdi> ينهي الإدارة التحفظية"),
        ("fever and abdominal pain", "تشخيص إكلينيكي لـ<bdi>chorioamnionitis</bdi>"),
    ],
    "why_correct": [
        "<bdi>chorioamnionitis</bdi> المؤكدة إكلينيكيًا تعني إنهاء الإدارة التحفظية فورًا: يجب إعطاء <bdi>IV antibiotics</bdi> (<bdi>ampicillin plus gentamicin</bdi>) <bdi>و</bdi> <bdi>delivery</bdi> بغض النظر عن عمر الحمل.",
        "أي خيار يحتفظ بالحمل مع المضادات فقط أو بدون مضادات يُعتبر غير كافٍ لأن العدوى داخل الرحم تهدد الأم والجنين.",
    ],
    "when_changes": [
        "لو ما زالت الحالة <bdi>uncomplicated PPROM</bdi> بدون <bdi>fever</bdi>، تبقى الإدارة تحفظية مع <bdi>latency antibiotics</bdi>.",
        "لو السؤال يفترض سبب آخر غير معروف للحرارة، يصير البحث عن مصدر آخر أولوية، لكن بوجود <bdi>PPROM</bdi> نفترض <bdi>chorioamnionitis</bdi> أولًا.",
    ],
    "rule": "الفخ هو إعطاء مضادات بدون ولادة؛ <bdi>chorioamnionitis</bdi> دايمًا تعني مضادات <bdi>و</bdi> ولادة معًا.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2284C": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "صورة كاملة لـ<bdi>chorioamnionitis</bdi>: <bdi>prolonged PPROM</bdi> مع علامات عدوى واضحة.",
    "clues": [
        ("prelabor premature rupture of membranes for 7 days", "<bdi>prolonged PPROM</bdi> يسمح بعدوى صاعدة"),
        ("rigors, and fever", "علامات جهازية للعدوى"),
        ("purulent, foul-smelling vaginal discharge", "علامة مباشرة على <bdi>intra-amniotic infection</bdi>"),
    ],
    "why_correct": [
        "تمزق الأغشية منذ <bdi>7 days</bdi> يعطي وقت كافٍ لعدوى صاعدة، والآن <bdi>fever</bdi> و<bdi>rigors</bdi> و<bdi>abdominal pain</bdi> مع <bdi>purulent, foul-smelling discharge</bdi> هي الصورة الإكلينيكية الكاملة لـ<bdi>chorioamnionitis</bdi>.",
        "لا يوجد ما يشير لمصدر آخر (<bdi>UTI</bdi>، نزيف، أو جهاز تنفسي).",
    ],
    "when_changes": [
        "لو الإفرازات طبيعية والحرارة فقط موجودة مع أعراض بولية، فكّر بـ<bdi>UTI</bdi> بدلاً من ذلك.",
        "لو فيه نزيف مهبلي بدون إفرازات كريهة، فكّر بـ<bdi>antepartum hemorrhage</bdi>.",
    ],
    "rule": "<bdi>prolonged ROM</bdi> + <bdi>fever</bdi> + إفرازات كريهة = <bdi>chorioamnionitis</bdi> حتى يثبت العكس؛ العلاج <bdi>antibiotics</bdi> <bdi>و</bdi> <bdi>delivery</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2292": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "حامل <bdi>low-risk</bdi> بدون عوامل خطر: السؤال عن الرعاية الروتينية المناسبة لكل الحوامل.",
    "clues": [
        ("Primigravida", "أول حمل"),
        ("no medical history or family history of DM", "لا توجد عوامل خطر لـ<bdi>GDM</bdi>"),
    ],
    "why_correct": [
        "هذه حامل <bdi>low-risk</bdi>: شابة، <bdi>normotensive</bdi>، وبدون تاريخ شخصي أو عائلي لـ<bdi>DM</bdi>، فالتوصية الروتينية لكل حامل هي <bdi>iron</bdi> (مع <bdi>folic acid</bdi>) لأن الحمل يرفع الحاجة للحديد و<bdi>iron deficiency anemia</bdi> هو أشهر <bdi>anemia</bdi> بالحمل.",
        "لا يوجد بالسيناريو أي سبب للخروج عن الرعاية الروتينية.",
    ],
    "when_changes": [
        "لو فيه تاريخ <bdi>previous GDM</bdi> أو <bdi>obesity</bdi> أو <bdi>macrosomia</bdi> سابق، الجواب يصير <bdi>early glucose screening</bdi>.",
        "لو كان <bdi>Hb</bdi> منخفض جدًا ولا يستجيب للحديد، فكّر بـ<bdi>thalassemia trait</bdi>.",
    ],
    "rule": "الحمل منخفض الخطورة = رعاية روتينية؛ <bdi>screening</bdi> مبكر لا يُعطى إلا بوجود عامل خطر واضح بالسؤال.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2293": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "<bdi>twin pregnancy</bdi> عند <bdi>term</bdi>: طريقة الولادة تُحدد حسب وضعية <bdi>twin A</bdi>.",
    "clues": [
        ("38 wkf", "عمر حمل <bdi>term</bdi>"),
        ("twins in vertex position", "كلا الجنينين <bdi>vertex</bdi>"),
        ("ctg was normal", "لا يوجد ضيق جنيني"),
    ],
    "why_correct": [
        "عند <bdi>38 weeks</bdi> مع كلا التوأمين <bdi>vertex</bdi> و<bdi>CTG normal</bdi>، لا يوجد مؤشر لولادة جراحية.",
        "طريقة الولادة في التوائم تُحدد حسب وضعية الجنين الأول (<bdi>presenting twin</bdi>)؛ <bdi>vertex-vertex</bdi> تُولد <bdi>vaginal delivery</bdi> عفوية.",
    ],
    "when_changes": [
        "لو كان <bdi>twin A</bdi> بوضعية <bdi>breech</bdi>، الجواب ينقلب إلى <bdi>cesarean section</bdi>.",
        "لو فيه ضيق جنيني على <bdi>CTG</bdi>، تُنظر الولادة الجراحية حسب الحالة.",
    ],
    "rule": "طريقة ولادة التوائم تُحدد بوضعية <bdi>twin A</bdi> فقط؛ <bdi>vertex-vertex</bdi> = <bdi>vaginal</bdi>، <bdi>twin A breech</bdi> = <bdi>cesarean</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2295": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "اكتشاف <bdi>ovarian cyst</bdi> أثناء <bdi>cesarean section</bdi>: السؤال عن التصرف الأنسب في <bdi>young patient</bdi>.",
    "clues": [
        ("right ovarian cyst measuring 12 cm", "حجم كبير ووُجد أثناء جراحة أخرى"),
    ],
    "why_correct": [
        "<bdi>ovarian cyst</bdi> تُكتشف أثناء جراحة لسبب آخر تُستأصل، وفي <bdi>22-year-old</bdi> العملية التي تحافظ على المبيض هي <bdi>cystectomy</bdi>.",
        "حجم <bdi>12 cm</bdi> (أكبر من 5 سم) سبب إضافي للاستئصال، ويعطي نسيج لفحص <bdi>histology</bdi> ويمنع <bdi>torsion</bdi> أو <bdi>rupture</bdi> لاحقًا.",
    ],
    "when_changes": [
        "لو كانت المريضة أكبر سنًا مع شبهة <bdi>malignancy</bdi> قوية، الجواب يصير <bdi>oophorectomy</bdi>.",
        "لو الكيس بسيط وصغير (≤5 سم) واكتُشف بالتصوير فقط، الخطة <bdi>observation</bdi> لا جراحة.",
    ],
    "rule": "اكتشاف الكيس أثناء جراحة أخرى يعني استئصاله؛ في <bdi>young patient</bdi> يُفضّل <bdi>cystectomy</bdi> على <bdi>oophorectomy</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2309": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "<bdi>teratogenicity</bdi> المرتبطة بـ<bdi>valproic acid</bdi> في الحمل.",
    "clues": [
        ("epilepsy", "تحتاج دواء مضاد للتشنج"),
        ("valproic acid", "أشد الأدوية المضادة للتشنج من ناحية <bdi>teratogenicity</bdi>"),
    ],
    "why_correct": [
        "<bdi>valproic acid</bdi> هو الأكثر تسببًا بالتشوهات بين مضادات التشنج الشائعة، وأثره المميز هو زيادة كبيرة بخطر <bdi>neural tube defects</bdi> (خصوصًا <bdi>spina bifida</bdi>).",
        "التعرض يكون أثناء إغلاق الأنبوب العصبي بالأسابيع الأولى، وعند <bdi>17 weeks</bdi> يُتابع بـ<bdi>anomaly scan</bdi> و<bdi>maternal serum AFP</bdi>.",
    ],
    "when_changes": [
        "لو الدواء <bdi>phenytoin</bdi>، الجواب يصير <bdi>fetal hydantoin syndrome</bdi> (تشوهات وجه وأصابع).",
        "لو الدواء <bdi>lamotrigine</bdi> أو <bdi>levetiracetam</bdi>، فهذه الأدوية أكثر أمانًا بالحمل.",
    ],
    "rule": "<bdi>valproate</bdi> = <bdi>neural tube defects</bdi>؛ خيارات <bdi>amniotic fluid</bdi> بهذا السؤال مجرد مشوشات.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2313": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "توقيت <bdi>anomaly scan</bdi> لا يتغير حتى بوجود تاريخ خسارة سابقة بسبب تشوهات.",
    "clues": [
        ("10 wks", "وقت الحجز، قبل وقت <bdi>anomaly scan</bdi>"),
        ("previous 2 abortion due to congenital anomalies", "تاريخ عالي الخطورة"),
        ("screening for anomalies", "السؤال عن توقيت <bdi>detailed scan</bdi>"),
    ],
    "why_correct": [
        "<bdi>anomaly (morphology) scan</bdi> يتم في <bdi>18-20 weeks</bdi> لأن الأعضاء تكون كبيرة بما يكفي لفحص تشريحي كامل، مع وقت كافٍ لاتخاذ قرارات بعد الكشف.",
        "التاريخ عالي الخطورة يغيّر دقة ومتابعة الفحص لكنه لا يُقدّم توقيته.",
    ],
    "when_changes": [
        "لو السؤال عن <bdi>dating scan</bdi>، التوقيت <bdi>10-12 weeks</bdi>.",
        "لو السؤال عن <bdi>nuchal translucency</bdi>، التوقيت <bdi>12-14 weeks</bdi>.",
    ],
    "rule": "تاريخ عالي الخطورة يغيّر دقة الفحص لكن لا يغيّر توقيت <bdi>anomaly scan</bdi>: يبقى <bdi>18-22 weeks</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2315": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>retraction ring</bdi> (<bdi>Bandl ring</bdi>) هي علامة محددة لـ<bdi>obstructed labor</bdi> مع ضعف تقدم الولادة.",
    "clues": [
        ("regular adequate contractions", "تقلصات كافية لكن الولادة لا تتقدم بشكل طبيعي"),
        ("retraction ring", "علامة <bdi>Bandl ring</bdi> المحددة لـ<bdi>obstructed labor</bdi>"),
    ],
    "why_correct": [
        "تقدم ضعيف من <bdi>5 cm</bdi> إلى <bdi>7 cm</bdi> ومن <bdi>-2</bdi> إلى <bdi>-1</bdi> خلال 6 ساعات رغم تقلصات منتظمة وكافية، مع وجود <bdi>retraction ring</bdi> محسوس بالبطن، يدل بشكل مباشر على <bdi>obstructed labor</bdi> وخطر تمزق الرحم القادم.",
        "<bdi>retraction ring</bdi> يتكوّن بين الجزء العلوي النشط المتقلص والجزء السفلي الممتد والرقيق.",
    ],
    "when_changes": [
        "لو كانت قبل <bdi>37 weeks</bdi>، يصير التشخيص <bdi>preterm labor</bdi> لا <bdi>obstructed labor</bdi>.",
        "لو فيه <bdi>fever</bdi> مع تسرع نبض وإفرازات كريهة، فكّر بـ<bdi>chorioamnionitis</bdi>.",
    ],
    "rule": "<bdi>Bandl ring</bdi> = <bdi>obstructed labor</bdi> حتى يثبت العكس، والعلاج <bdi>urgent cesarean section</bdi> وليس <bdi>oxytocin</bdi> أبدًا.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2317": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سبب موت الجنين يُحدد بالدليل المرضي الموجود (<bdi>placental thrombi</bdi>) مو بعامل الخطر العام (<bdi>diabetes</bdi>).",
    "clues": [
        ("sudden fetal death", "موت مفاجئ بدون تحذير سابق"),
        ("placental sample showed thrombi", "دليل مباشر على سبب الانسداد"),
    ],
    "why_correct": [
        "الدليل الحاسم هو الفحص المرضي: <bdi>placental sample showed thrombi</bdi>، بدون أي تشوه وبحمل <bdi>uneventful</bdi>.",
        "<bdi>placental thrombosis and infarction</bdi> تقطع تدفق الدم بين الأم والجنين وهي سبب مباشر وموثّق لموت الجنين المفاجئ؛ <bdi>diabetes</bdi> عامل خطر بالخلفية فقط.",
    ],
    "when_changes": [
        "لو كان الفحص المرضي طبيعي بدون <bdi>thrombi</bdi>، يصير <bdi>diabetes</bdi> نفسه هو المرشح الأقرب كسبب.",
        "لو كان الوزن أقل بشكل واضح من المتوقع لعمر الحمل مع دليل قصور مشيمي، فكّر بـ<bdi>growth restriction</bdi> كسبب مباشر.",
    ],
    "rule": "سبب الموت هو الدليل المرضي الموجود فعليًا، مو عامل الخطر الذي «سبب السبب».",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2330": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "<bdi>single umbilical artery</bdi>: تحديد عامل الخطر الأقوى بين الخيارات المطروحة.",
    "clues": [
        ("Single umbilical artery", "تشوه بالحبل السري"),
        ("multiple pregnancy", "أقوى عامل خطر مرتبط به من بين الخيارات"),
    ],
    "why_correct": [
        "<bdi>single umbilical artery</bdi> أكثر شيوعًا بوضوح بـ<bdi>multiple pregnancy</bdi>، وهو أقوى الارتباطات المعروفة بين الخيارات المتاحة.",
        "الارتباط الكلاسيكي الآخر (<bdi>maternal diabetes</bdi>) غير مطروح بالخيارات؛ العمر والـ<bdi>parity</bdi> و<bdi>hypothyroidism</bdi> المعالج ارتباطات ضعيفة أو غير معروفة.",
    ],
    "when_changes": [
        "لو كان خيار <bdi>maternal diabetes</bdi> مطروحًا، يصير هو الأقوى.",
        "لو كان العمر ≥40، يصير <bdi>age</bdi> ارتباطًا ضعيفًا إضافيًا، لكنه غالبًا يرتبط بخطر <bdi>aneuploidy</bdi> أكثر.",
    ],
    "rule": "<bdi>single umbilical artery</bdi>: فكّر بـ<bdi>multiple pregnancy</bdi> و<bdi>maternal diabetes</bdi> و<bdi>anomalies</bdi> كأهم الارتباطات.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2332": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نزف خفيف بـ<bdi>second trimester</bdi> مع <bdi>cervical length</bdi> طبيعي: لا يوجد مؤشر لتدخل، فالخطة <bdi>conservative</bdi>.",
    "clues": [
        ("23 weeks", "<bdi>mid-trimester</bdi>، قبل سن قابلية الحياة الجيدة"),
        ("cervical length of 30mm", "أعلى من عتبة الخطر (25 مم)"),
    ],
    "labs": [["Cervical length", "30 mm", ">25 mm = طبيعي"]],
    "why_correct": [
        "<bdi>primigravida</bdi> بدون تاريخ خسارة سابقة، وعنق الرحم <bdi>30 mm</bdi> فوق عتبة <bdi>25 mm</bdi>.",
        "مع <bdi>minimal spotting</bdi> بدون ألم أو تقلصات وجنين <bdi>viable</bdi>، لا يوجد علامة لـ<bdi>preterm labor</bdi> أو <bdi>cervical insufficiency</bdi>، فالخطة هي المتابعة الروتينية (<bdi>conservative management</bdi>).",
    ],
    "when_changes": [
        "لو كان عنق الرحم أقل من <bdi>25 mm</bdi> بدون تاريخ خسارة سابقة، الجواب يصير <bdi>vaginal progesterone</bdi> لا <bdi>cerclage</bdi>.",
        "لو فيه تاريخ خسارة سابقة بمنتصف الحمل، يُنظر بـ<bdi>cerclage</bdi> حسب التوقيت والطول.",
    ],
    "rule": "عنق رحم طويل (>25 مم) بدون تاريخ خسارة سابقة = متابعة تحفظية؛ <bdi>cerclage</bdi> يحتاج تاريخًا سابقًا أو عنقًا قصيرًا جدًا.",
    "comparison": None,
    "guideline_note": None,
},
"AS-2333": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "حساب الحجم المحمي بجرعة <bdi>anti-D</bdi> المعيارية بعد الولادة.",
    "clues": [
        ("300 μg Dose Of Anti-D Immunoglobulin", "الجرعة المعيارية بعد الولادة"),
        ("Volume Of Fetal Blood", "السؤال عن الحجم المحمي بالجرعة"),
    ],
    "labs": [["Standard anti-D dose", "300 micrograms", "يحمي 30 mL دم جنيني كامل ≈ 15 mL خلايا حمراء"]],
    "why_correct": [
        "الأم <bdi>Rh negative</bdi> والجنين <bdi>D-positive</bdi>، فتحتاج <bdi>anti-D</bdi> خلال 72 ساعة لمنع التحسس.",
        "جرعة <bdi>300 micrograms</bdi> المعيارية تُعادل حماية حوالي <bdi>30 mL</bdi> من دم الجنين الكامل (أي حوالي 15 مل خلايا حمراء فقط). زمر <bdi>ABO</bdi> بالسؤال مجرد مشوشات.",
    ],
    "when_changes": [
        "لو كان النزف المشتبه أكبر، يُستخدم فحص <bdi>Kleihauer test</bdi> لتحديد الكمية الحقيقية وتُعطى جرعات إضافية.",
    ],
    "rule": "300 ميكروغرام = 30 مل دم كامل = 15 مل خلايا حمراء؛ الفرق بين الاثنين هو الفخ بهذا السؤال.",
    "comparison": None,
    "guideline_note": None,
},
"AS-2346": {
    "correct_letter": "D",
    "self_judged": True,
    "idea": "<bdi>choriocarcinoma</bdi> مع <bdi>metastasis</bdi> و<bdi>WHO score</bdi> مرتفع: اختيار العلاج المناسب بناءً على شدة المرض.",
    "clues": [
        ("choriocarcinoma + lung mets", "مرض منتشر (<bdi>stage III</bdi>)"),
        ("WHO prognostic score of 10", "درجة خطورة عالية (≥7)"),
    ],
    "why_correct": [
        "<bdi>WHO prognostic score</bdi> بـ<bdi>10</bdi> (أكبر من 7) يعني <bdi>high-risk GTN</bdi>، والعلاج القياسي لهذه الفئة هو <bdi>multi-agent chemotherapy</bdi> (مثل <bdi>EMA-CO</bdi>)، لا <bdi>single-agent</bdi> ولا جراحة أولية.",
        "وجود <bdi>lung metastases</bdi> يحدد <bdi>stage III</bdi> لكن القرار العلاجي يعتمد على <bdi>WHO score</bdi> لا <bdi>stage</bdi> وحده.",
    ],
    "when_changes": [
        "لو كانت الدرجة ≤6، العلاج يصير <bdi>single-agent</bdi> (<bdi>methotrexate</bdi> أو <bdi>actinomycin D</bdi>).",
        "لو فشل العلاج الكيميائي أو احتاجت لتخفيف كتلة موضعية، يُنظر بـ<bdi>hysterectomy</bdi> كمساعد.",
    ],
    "rule": "درجة <bdi>WHO</bdi> هي الفاصل: ≤6 علاج فردي، ≥7 علاج متعدد الأدوية؛ المصدر لم يحدد جوابًا، وهذا استنتاج طبي مباشر.",
    "comparison": None,
    "labs": [["WHO prognostic score", "10", "≤6 منخفض الخطورة / ≥7 مرتفع الخطورة"]],
    "guideline_note": "المصدر لم يعتمد جوابًا (<bdi>answer_letter</bdi> غير موجود)؛ الاختيار هنا حسب مبدأ <bdi>WHO score</bdi> القياسي.",
},
"AS-2376": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "بعد <bdi>20 weeks</bdi> يُسمى موت الجنين <bdi>fetal demise</bdi> لا <bdi>abortion</bdi>.",
    "clues": [
        ("28 weeks", "بعد عتبة <bdi>20 weeks</bdi>، المصطلح يصير <bdi>fetal demise</bdi>"),
        ("fundal height equivalent to 18 weeks", "يدعم موت الجنين منذ عدة أسابيع"),
        ("lack of fetal heart activity", "تأكيد موت الجنين"),
    ],
    "why_correct": [
        "عند <bdi>28 weeks</bdi> مع <bdi>lack of fetal heart activity</bdi> و<bdi>no fetal movement</bdi>، الخسارة بعد عتبة <bdi>20 weeks</bdi>، فالمصطلح الصحيح <bdi>fetal demise</bdi> لا <bdi>abortion</bdi>.",
        "<bdi>fundal height equivalent to 18 weeks</bdi> يتناسب مع جنين توقف نموه منذ أسابيع، متوافق مع النزف قبل أسبوعين.",
    ],
    "when_changes": [
        "لو كانت الخسارة قبل <bdi>20 weeks</bdi> مع نفس الصورة (<bdi>closed os</bdi>، غير قابل للحياة)، الجواب يصير <bdi>missed abortion</bdi>.",
        "لو كان الرحم أكبر من تاريخ الحمل مع <bdi>hCG</bdi> مرتفع جدًا وبدون جنين واضح، فكّر بـ<bdi>molar pregnancy</bdi>.",
    ],
    "rule": "قبل <bdi>20 weeks</bdi> = <bdi>abortion</bdi>؛ عند أو بعد <bdi>20 weeks</bdi> = <bdi>fetal demise</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2385": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>fibroid</bdi> عرضي مع رفض الجراحة وخطورة تخديرية عالية: اختيار الخيار غير الجراحي الفعّال.",
    "clues": [
        ("multiple comorbidities", "خطورة تخديرية مرتفعة"),
        ("uterine fibroids", "سبب <bdi>heavy menstrual bleeding</bdi>"),
        ("completed her family", "لا حاجة للحفاظ على الخصوبة"),
        ("prefers a non-surgical treatment", "تستثني الخيارات الجراحية"),
    ],
    "why_correct": [
        "<bdi>heavy menstrual bleeding</bdi> من <bdi>fibroids</bdi>، أكملت تكوين الأسرة، تفضّل علاجًا غير جراحيًا، وتحمل خطورة تخديرية عالية بسبب <bdi>OSA</bdi> وأمراض أخرى.",
        "<bdi>uterine artery embolization</bdi> هو الخيار الفعّال والدائم لمن ترفض أو غير مؤهلة للجراحة، ويتم تحت تخدير موضعي بدون <bdi>general anesthesia</bdi>.",
    ],
    "when_changes": [
        "لو كانت ترغب بالحمل مستقبلًا، الجواب يصير <bdi>myomectomy</bdi>.",
        "لو كانت مستعدة للجراحة وأكملت تكوين الأسرة، الجواب يصير <bdi>hysterectomy</bdi>.",
    ],
    "rule": "ترغب خصوبة = <bdi>myomectomy</bdi>؛ أكملت الأسرة وتقبل جراحة = <bdi>hysterectomy</bdi>؛ ترفض الجراحة = <bdi>UAE</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2389": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "<bdi>polyhydramnios</bdi> ناتج من ضعف بلع الجنين أو زيادة بوله؛ السؤال عن الحالة المرتبطة بزيادة السائل مو نقصانه.",
    "clues": [
        ("polyhydramnios", "زيادة السائل الأمنيوسي"),
    ],
    "why_correct": [
        "<bdi>polyhydramnios</bdi> ينتج من ضعف بلع الجنين أو زيادة بوله، و<bdi>trisomy 21</bdi> يرتبط بـ<bdi>duodenal atresia</bdi> ومشاكل بلع تمنع الجنين من بلع السائل.",
        "من بين الخيارات، <bdi>trisomy 21</bdi> هو الوحيد المرتبط بزيادة السائل بدل نقصانه.",
    ],
    "when_changes": [
        "لو السؤال عن <bdi>oligohydramnios</bdi>، الجواب يصير <bdi>renal agenesis</bdi> أو <bdi>IUGR</bdi>.",
    ],
    "rule": "«ما يقدر يبلع» أو «بول زايد» = <bdi>polyhydramnios</bdi>؛ «ما فيه كلاوي» أو «مشيمة ضعيفة» = <bdi>oligohydramnios</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2391": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "توقيت <bdi>cleavage</bdi> بعد التبويض يحدد نوع <bdi>chorionicity/amnionicity</bdi> بالتوائم المتماثلة.",
    "clues": [
        ("Dichorionic Diamniotic", "انقسام مبكر جدًا قبل تكوّن <bdi>chorion</bdi>"),
    ],
    "why_correct": [
        "<bdi>DCDA</bdi> من زيجوت واحد يحدث عند انقسام بالفترة <bdi>0-72 hours</bdi> (أيام 0-3)، قبل تمايز <bdi>chorion</bdi>، فيتكوّن لكل جنين <bdi>chorion</bdi> و<bdi>amnion</bdi> خاص به.",
        "(التوائم <bdi>dizygotic</bdi> تكون دايمًا <bdi>DCDA</bdi> أيضًا، لكن السؤال يركز على توقيت الانقسام لدى التوائم <bdi>monozygotic</bdi>.)",
    ],
    "when_changes": [
        "لو كان الانقسام بـ<bdi>4-8 days</bdi>، الجواب يصير <bdi>MCDA</bdi>.",
        "لو كان الانقسام بـ<bdi>9-12 days</bdi>، الجواب يصير <bdi>MCMA</bdi>.",
    ],
    "rule": "كل ما تأخر الانقسام، كل ما زاد التشارك: أولًا <bdi>chorion</bdi> (MCDA)، ثم <bdi>amnion</bdi> (MCMA)، ثم الجسم نفسه (<bdi>conjoined</bdi>).",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2392": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "توقيت <bdi>cleavage</bdi> المرتبط بـ<bdi>Monochorionic Diamniotic</bdi>.",
    "clues": [
        ("Monochorionic Diamniotic", "<bdi>chorion</bdi> مشترك لكن <bdi>amnion</bdi> منفصل"),
    ],
    "why_correct": [
        "<bdi>MCDA</bdi> تنتج من انقسام بـ<bdi>4-8 days</bdi>؛ بهذا الوقت يكون <bdi>chorion</bdi> قد تكوّن (لذلك مشترك) لكن <bdi>amnion</bdi> لم يتكوّن بعد (لذلك كل جنين يأخذ <bdi>amnion</bdi> خاص به).",
    ],
    "when_changes": [
        "لو كان الانقسام بـ<bdi>0-72 hours</bdi>، الجواب يصير <bdi>DCDA</bdi>.",
        "لو كان الانقسام بـ<bdi>9-12 days</bdi>، الجواب يصير <bdi>MCMA</bdi>.",
    ],
    "rule": "<bdi>MCDA</bdi> يعني <bdi>chorion</bdi> مشترك واحد مع <bdi>amnion</bdi>ين، فالانقسام حصل بعد تكوّن <bdi>chorion</bdi> (يوم 4) وقبل <bdi>amnion</bdi> (يوم 8).",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2393": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "توقيت <bdi>cleavage</bdi> المرتبط بـ<bdi>Monochorionic Monoamniotic</bdi>.",
    "clues": [
        ("Monochorionic Monoamniotic", "تشارك كامل بـ<bdi>chorion</bdi> و<bdi>amnion</bdi>"),
    ],
    "why_correct": [
        "بحلول يوم <bdi>9-12</bdi> يكون <bdi>chorion</bdi> و<bdi>amnion</bdi> كلاهما تكوّنا، فينقسم الجنين ويشترك التوأمان بـ<bdi>chorion</bdi> واحد و<bdi>amnion</bdi> واحد: <bdi>monochorionic monoamniotic</bdi>.",
    ],
    "when_changes": [
        "لو الانقسام بعد يوم 12-13، الجواب يصير <bdi>conjoined twins</bdi> (انقسام غير مكتمل).",
        "لو الانقسام بـ<bdi>0-72 hours</bdi>، الجواب يصير <bdi>DCDA</bdi>.",
    ],
    "rule": "كل ما تأخر الانقسام زاد التشارك: الأقصر = لا تشارك، الأطول = تشارك الجسم نفسه (<bdi>conjoined</bdi>).",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2398": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>obese patient</bdi> مع دورات غير منتظمة: الخطوة الأولى دايمًا تعديل نمط الحياة قبل الأدوية.",
    "clues": [
        ("obese", "<bdi>BMI 35</bdi> عامل خطر لـ<bdi>anovulation</bdi>"),
        ("irregular periods", "دورات غير منتظمة (<bdi>anovulatory</bdi>)"),
        ("BMI is 35", "درجة سمنة مرتفعة"),
    ],
    "why_correct": [
        "<bdi>obesity</bdi> مع دورات غير منتظمة غالبًا نتيجة دورات <bdi>anovulatory</bdi> بسبب مقاومة الإنسولين، غالبًا <bdi>PCOS</bdi>.",
        "<bdi>weight reduction and lifestyle modification</bdi> هي الخطوة الأولى لكل مريضة مثل هذه؛ حتى فقدان وزن معتدل قد يعيد <bdi>ovulation</bdi> ويقلل الخطر الاستقلابي.",
    ],
    "when_changes": [
        "لو فشل تعديل نمط الحياة وما ترغب بالحمل، يُضاف <bdi>combined OCP</bdi>.",
        "لو ترغب بالحمل، تُستخدم <bdi>ovulation induction</bdi>.",
    ],
    "rule": "«أنسب نصيحة» بمريضة سمينة مع مشكلة دورة أو <bdi>ovulation</bdi> = فقدان الوزن أولًا؛ الأدوية تأتي بعد ذلك.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2399": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "<bdi>PCOS</bdi> مع رغبة بالحمل: السؤال عن علاج <bdi>infertility</bdi> لا تنظيم الدورة.",
    "clues": [
        ("pCO", "<bdi>PCOS</bdi> كتابة مختصرة"),
        ("trying to conceive", "الهدف هو <bdi>ovulation induction</bdi> لا منع حمل"),
    ],
    "why_correct": [
        "عقم <bdi>PCOS</bdi> سببه <bdi>anovulation</bdi>، فمن تحاول الحمل تحتاج <bdi>ovulation induction</bdi>، ومن بين الخيارات <bdi>clomiphene citrate</bdi> هو مضاد استروجين يرفع إفراز <bdi>FSH</bdi> ويحفّز نمو الجريب.",
        "فقدان الوزن يجب أن يصاحب العلاج بالمريضات ذوات الوزن الزائد.",
    ],
    "when_changes": [
        "لو كانت لا ترغب بالحمل، الجواب يصير <bdi>OCP</bdi> لتنظيم الدورة.",
        "لو فشل <bdi>clomiphene</bdi>، يُضاف <bdi>metformin</bdi> كمساعد أو يُنتقل لـ<bdi>gonadotropins</bdi>.",
    ],
    "rule": "ترغب بالحمل بـ<bdi>PCOS</bdi> = <bdi>ovulation induction</bdi> (<bdi>clomiphene</bdi>)؛ لا ترغب = <bdi>OCP</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2408": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "<bdi>IUFD</bdi> عند <bdi>term</bdi>: الخطة هي <bdi>induction</bdi> لولادة مهبلية آمنة لا جراحة.",
    "clues": [
        ("39 wks", "عمر حمل متقدم جدًا"),
        ("IUFD", "موت جنين مؤكد داخل الرحم"),
    ],
    "why_correct": [
        "بعد تأكيد <bdi>IUFD</bdi> بـ<bdi>39 weeks</bdi> الهدف هو ولادة مهبلية آمنة، فيُحفّز المخاض: <bdi>prostaglandins</bdi> (PGE2 أو misoprostol) لتنضيج عنق الرحم و<bdi>oxytocin</bdi> للتقلصات.",
        "التحفيز يتجنب خطر العدوى و<bdi>DIC</bdi> من بقاء الجنين الميت داخل الرحم لفترة طويلة، ويجنّب الأم عملية جراحية غير ضرورية.",
    ],
    "when_changes": [
        "لو كانت هناك مؤشرات أمومية (مثل <bdi>previous classical scar</bdi> أو وضعية غير طولية)، الجواب يصير <bdi>C/S</bdi>.",
        "لو كانت مستقرة وتفضل الانتظار، يمكن منحها وقتًا قصيرًا قبل التحفيز لكن الخطة الأساسية تبقى <bdi>induction</bdi>.",
    ],
    "rule": "أم مستقرة مع <bdi>IUFD</bdi>: الخطة <bdi>induction</bdi> لا جراحة قيصرية، إلا بوجود سبب أمومي محدد.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2409": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "اللقاحات الحية <bdi>contraindicated</bdi> بالحمل؛ تُعطى بعد الولادة.",
    "clues": [
        ("Second trimester pregnant", "حمل نشط، لقاح حي ممنوع"),
        ("didn't have measles before", "تحتاج مناعة لكن ليس الآن"),
    ],
    "why_correct": [
        "لقاح <bdi>MMR</bdi> هو <bdi>live attenuated vaccine</bdi> و<bdi>contraindicated</bdi> بالحمل بسبب خطر نظري على الجنين.",
        "حامل غير محصّنة تُلقّح <bdi>postpartum</bdi>، قبل الخروج من المستشفى؛ الرضاعة الطبيعية ليست مانعًا.",
    ],
    "when_changes": [
        "لو كان اللقاح غير حي (مثل <bdi>influenza</bdi> أو <bdi>Tdap</bdi>)، يُعطى الآن بالحمل بأمان.",
    ],
    "rule": "أي لقاح حي بالحمل ينقلب الجواب لـ«بعد الولادة»؛ اللقاحات غير الحية (<bdi>flu</bdi>، <bdi>Tdap</bdi>) تُعطى «الآن».",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2410": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "متابعة <bdi>β-hCG</bdi> بعد <bdi>methotrexate</bdi> للحمل خارج الرحم: الحكم على <bdi>trend</bdi> لا على قيمة واحدة.",
    "clues": [
        ("ectopic pregnancy", "سياق متابعة <bdi>MTX</bdi>"),
        ("One dose of methotrexate", "جرعة واحدة أعطيت"),
        ("Day 4: 70 mmol; Day 5: 70 mmol", "انخفاض كبير إجمالي مع ثبات مستوى منخفض"),
    ],
    "labs": [["β-hCG Day 1", "1800", "انخفاض متوقع ≥15% بين اليوم 4 واليوم 7"], ["β-hCG Day 4-5", "70 / 70", "انخفاض إجمالي أكثر من 95% من القيمة الأولى"]],
    "why_correct": [
        "<bdi>β-hCG</bdi> انخفض من <bdi>1800</bdi> إلى <bdi>70</bdi>، أي أكثر من 95%، وهذا تجاوب جيد جدًا يتعدى شرط الانخفاض المطلوب (>15%).",
        "ثبات قصير بين <bdi>70</bdi> و<bdi>70</bdi> بمستوى منخفض لا يُعد فشل علاج؛ الخطة الصحيحة متابعة <bdi>β-hCG</bdi> الأسبوعية حتى تصبح غير مكتشفة مع إرسالها للمنزل.",
    ],
    "when_changes": [
        "لو ارتفع <bdi>β-hCG</bdi> بعد الجرعة، الجواب يصير <bdi>immediate surgical management</bdi>.",
        "لو كان الانخفاض بين اليوم 4 و7 أقل من 15% (ثبات حقيقي)، تُعطى جرعة ثانية من <bdi>methotrexate</bdi>.",
    ],
    "rule": "الحكم يكون على الاتجاه العام لا على زوج أرقام واحد؛ انخفاض كبير إجمالي مع ثبات قصير بمستوى منخفض يبقى استجابة ناجحة.",
    "comparison": None,
    "guideline_note": None,
},
"AS-2411": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "<bdi>preconception counseling</bdi> لمريضة على <bdi>ACE inhibitor</bdi>: يجب التبديل قبل الحمل بسبب <bdi>teratogenicity</bdi>.",
    "clues": [
        ("preconception counseling", "وقت مثالي لمراجعة الأدوية قبل الحمل"),
        ("ACE inhibitors", "دواء <bdi>fetotoxic</bdi> يجب استبداله"),
    ],
    "why_correct": [
        "<bdi>ACE inhibitors</bdi> (و<bdi>ARBs</bdi>) سامة للجنين، تؤثر أساسًا على نمو ووظيفة كلية الجنين (<bdi>renal dysgenesis</bdi>، <bdi>oligohydramnios</bdi>).",
        "يجب التبديل لدواء آمن بالحمل مثل <bdi>labetalol</bdi> أو <bdi>methyldopa</bdi> أو <bdi>nifedipine</bdi>؛ <bdi>preconception counseling</bdi> هو أفضل وقت لمراجعة وتغيير الأدوية.",
    ],
    "when_changes": [
        "لو كان الدواء آمنًا بالحمل (مثل <bdi>hydroxychloroquine</bdi> بـ<bdi>SLE</bdi>)، يُستمر عليه بدون تبديل.",
    ],
    "rule": "حمل + <bdi>ACEi/ARB</bdi> = تبديل، أبدًا لا استمرار؛ الاستمرار فقط للأدوية الآمنة أو غير الممنوعة تمامًا.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
}

WHY_WRONG = {
"AS-2251": {
    "A": "<bdi>endometriosis</bdi> يعطي <bdi>dysmenorrhea</bdi> و<bdi>dyspareunia</bdi> و<bdi>dyschezia</bdi> وعقم؛ ما يسبب أعراض <bdi>luteal</bdi> نفسية وثديّية تروح مع الدورة.",
    "B": "<bdi>perimenopause</bdi> يعطي هبات حرارة ودورات غير منتظمة بعمر أكبر، مو أعراض مرتبطة بأسبوع قبل كل دورة بعمر 34.",
    "C": "<bdi>pelvic congestion syndrome</bdi> يعطي ألم حوضي مزمن يزيد بالوقوف، مو صداع وقلق وألم ثدي دوري.",
},
"AS-2252": {
    "A": "<bdi>secondary dysmenorrhea</bdi> سببها <bdi>pelvic pathology</bdi>، تظهر بعمر أكبر مع ألم خارج الدورة أو <bdi>exam</bdi> غير طبيعي، وهذا غير موجود هنا.",
    "B": "<bdi>premenstrual syndrome</bdi> يبدأ بـ<bdi>luteal phase</bdi> قبل الدورة ويتحسن بأول الدورة؛ هنا الألم يبدأ <bdi>مع</bdi> الدورة بدون ألم قبلها.",
    "D": "<bdi>endometriosis</bdi> يعطي <bdi>secondary dysmenorrhea</bdi> غالبًا مع <bdi>dyspareunia</bdi> و<bdi>fixed uterus</bdi>؛ <bdi>exam</bdi> هنا طبيعي والتوقيت محصور بالدورة.",
},
"AS-2255": {
    "A": "<bdi>premature ovarian failure</bdi> يعطي <bdi>FSH</bdi> و<bdi>LH</bdi> مرتفعين مع <bdi>estrogen</bdi> منخفض؛ <bdi>normal FSH</bdi> يستبعده.",
    "B": "خيار غير محدد طبيًا ولا يفسر الصورة بشكل أفضل من <bdi>PCOS</bdi>.",
    "C": "<bdi>HPO axis failure</bdi> (<bdi>hypogonadotropic</bdi>) يُشير له <bdi>FSH</bdi> و<bdi>LH</bdi> منخفضان مع <bdi>estrogen</bdi> منخفض، وعادة مع إجهاد أو نقص وزن أو رياضة شديدة؛ مع وجود خيار <bdi>PCOS</bdi> يصير هو الأقل احتمالاً.",
},
"AS-2256": {
    "A": "<bdi>gonadal dysgenesis</bdi> (مثل <bdi>Turner</bdi>) يعطي مبايض ضعيفة و<bdi>estrogen</bdi> منخفض مع <bdi>absent</bdi> تطور ثدي و<bdi>FSH</bdi> مرتفع.",
    "B": "<bdi>LH deficiency</bdi> حالة <bdi>hypogonadotropic</bdi> مع <bdi>estrogen</bdi> منخفض، فلن يحصل تطور ثدي طبيعي.",
    "D": "<bdi>pituitary FSH deficiency</bdi> يعطي أيضًا <bdi>estrogen</bdi> منخفض وتطور جنسي ثانوي ضعيف، مو التطور الطبيعي الموصوف.",
},
"AS-2262": {
    "A": "<bdi>oxytocin</bdi> يعمل بشكل ضعيف بـ<bdi>second trimester</bdi> لأن مستقبلاته بالرحم قليلة؛ يُستخدم أكثر قرب <bdi>term</bdi> أو لتعزيز ولادة قائمة.",
    "C": "<bdi>mifepristone</bdi> يُستخدم كـ<bdi>priming agent</bdi> قبل <bdi>misoprostol</bdi> بـ36-48 ساعة؛ يقصّر فترة التحفيز لكنه وحده نادرًا كافٍ لتحفيز الولادة.",
    "D": "<bdi>dinoprostone (PGE2)</bdi> يُستخدم أساسًا لتنضيج عنق الرحم قرب <bdi>term</bdi>؛ <bdi>misoprostol</bdi> هو المفضل للتحفيز بعد وفاة الجنين بمنتصف الحمل.",
},
"AS-2270": {
    "A": "<bdi>OCP</bdi> لمدة 6 أشهر يثبّط الدورة كما يُستخدم في <bdi>endometriosis</bdi>؛ لا يفيد بإبقاء فتحة الغشاء مفتوحة بعد الشق.",
    "C": "<bdi>IUD</bdi> وسيلة منع حمل ولا توضع بمجرى خروج تم شقه حديثًا؛ ما له دور بمنع عودة الانسداد.",
},
"AS-2272": {
    "B": "<bdi>ergometrine</bdi> يسبب تقلص مستمر وقوي حتى بالجزء السفلي وعنق الرحم مما قد يحبس المشيمة بالداخل، وهو أيضًا <bdi>contraindicated</bdi> بـ<bdi>hypertension</bdi>.",
},
"AS-2275": {
    "A": "<bdi>methimazole</bdi> يُفضّل من <bdi>second trimester</bdi> فصاعدًا (للتبديل من <bdi>PTU</bdi> وتجنب سمية كبده)، لكنه يُتجنب بـ<bdi>first trimester</bdi> بسبب خطر التشوه.",
    "C": "<bdi>thyroidectomy</bdi> بالحمل تُحجز لفشل أو عدم تحمل الأدوية المضادة للدرقية أو تضخم ضاغط كبير، وتتم بـ<bdi>second trimester</bdi> لو احتاجت.",
    "D": "<bdi>radioactive iodine</bdi> ممنوع تمامًا بالحمل لأنه يدمر الغدة الدرقية للجنين.",
},
"AS-2284": {
    "A": "<bdi>labor</bdi> يعطي تقلصات مؤلمة بدون <bdi>fever</bdi>؛ الحرارة بعد تمزق طويل الأغشية تدل على عدوى (قد تحفّز الولادة نفسها).",
    "C": "<bdi>placental abruption</bdi> يعطي نزيف مهبلي مؤلم مع رحم متشنج ومؤلم، مو <bdi>fever</bdi>.",
    "D": "<bdi>cervical incompetence</bdi> تعطي توسع غير مؤلم بعنق الرحم بمنتصف الحمل، لا <bdi>fever</bdi> وألم بعد تمزق الأغشية.",
},
"AS-2284B": {
    "A": "<bdi>painkiller</bdi> وحده يتجاهل عدوى داخل الرحم تهدد الأم والجنين وتحتاج مضادات وولادة.",
    "B": "مضادات بدون ولادة غير كافية؛ استمرار الحمل مع <bdi>chorioamnionitis</bdi> يرفع خطر <bdi>sepsis</bdi> للأم وعدوى للجنين.",
    "D": "بوجود <bdi>PPROM</bdi> تُعتبر الحرارة وألم البطن <bdi>chorioamnionitis</bdi> حتى يثبت العكس؛ البحث عن مصدر آخر يؤخر العلاج الضروري.",
},
"AS-2284C": {
    "B": "<bdi>urinary tract infection</bdi> تسبب <bdi>dysuria</bdi> و<bdi>frequency</bdi> أو ألم بالخصر مع حرارة؛ لا تسبب إفرازات مهبلية كريهة بعد تمزق الأغشية.",
    "C": "<bdi>antepartum hemorrhage</bdi> يظهر بنزيف مهبلي (غير مؤلم بـ<bdi>previa</bdi>، مؤلم بـ<bdi>abruption</bdi>)، مو حرارة مع إفرازات كريهة.",
    "D": "<bdi>lower respiratory tract infection</bdi> يعطي سعال وضيق تنفس وعلامات بالصدر، مو ألم بطن مع إفرازات مهبلية كريهة.",
},
"AS-2292": {
    "A": "<bdi>early glucose screening</bdi> يُحجز للحوامل <bdi>high-risk</bdi> (تاريخ <bdi>GDM</bdi> سابق، <bdi>obesity</bdi>، تاريخ عائلي قوي، <bdi>macrosomia</bdi> سابق)؛ هذه المريضة بدون أي منها، فتُفحص بشكل روتيني بـ<bdi>24-28 weeks</bdi>.",
},
"AS-2293": {
    "B": "<bdi>forceps</bdi> ولادة مهبلية بأداة تحتاج سببًا محددًا بالمرحلة الثانية (تأخر أو ضيق جنيني) مع توسع كامل ورأس منخفض؛ لا يوجد سبب هنا.",
    "C": "<bdi>cesarean section</bdi> تُستخدم عند <bdi>twin A</bdi> غير <bdi>vertex</bdi> أو توائم <bdi>monoamniotic</bdi> أو أسباب أخرى؛ ليس لتوائم <bdi>vertex-vertex</bdi> مع <bdi>CTG</bdi> طبيعي.",
},
"AS-2295": {
    "B": "<bdi>oophorectomy</bdi> يفقد المبيض كاملًا بمريضة شابة؛ يُحجز لحالات لا يمكن حفظ المبيض فيها أو شبهة قوية بـ<bdi>malignancy</bdi> بعمر أكبر.",
    "C": "<bdi>no intervention</bdi> يناسب فقط كيس بسيط وبدون أعراض ≤5 سم وُجد بالتصوير؛ كيس <bdi>12 cm</bdi> أثناء جراحة مفتوحة يجب استئصاله.",
    "D": "<bdi>squeeze and rupture</bdi> يسكب محتوى الكيس (قد يكون خبيثًا) بدون فحص <bdi>histology</bdi> ويترك جدار الكيس مما يسمح بعودته.",
},
"AS-2309": {
    "A": "<bdi>oligohydramnios</bdi> سببه <bdi>renal agenesis</bdi> أو انسداد أو قصور مشيمي، مو تعرّض لـ<bdi>valproate</bdi>.",
    "B": "<bdi>polyhydramnios</bdi> يرتبط بسكري الأم وحمل متعدد وضعف بلع الجنين، مو أثر <bdi>valproate</bdi> المباشر.",
    "D": "<bdi>non-immune hydrops</bdi> ينتج من مرض قلبي جنيني أو عدوى أو تشوه كروموسومي أو فقر دم شديد، مو <bdi>valproate</bdi>.",
},
"AS-2313": {
    "A": "<bdi>10-12 weeks</bdi> هو وقت <bdi>dating scan</bdi> (تأكيد عمر الحمل والحيوية وعدد الأجنة)، مبكر جدًا للتشريح التفصيلي.",
    "B": "<bdi>12-14 weeks</bdi> يغطي <bdi>first-trimester aneuploidy screening</bdi> (<bdi>nuchal translucency</bdi>)، مو الفحص التشريحي؛ الأعضاء ما زالت صغيرة.",
    "D": "<bdi>22-26 weeks</bdi> متأخر عن النافذة المعيارية؛ اكتشاف تشوه بهذا الوقت يقلل خيارات التعامل.",
},
"AS-2315": {
    "A": "<bdi>preterm labor</bdi> يحدث قبل <bdi>37 weeks</bdi>؛ هذه المريضة بـ<bdi>term</bdi> (39 أسبوع).",
    "C": "<bdi>chorioamnionitis</bdi> تظهر بـ<bdi>fever</bdi> وتسرع نبض الأم أو الجنين وألم بالرحم أو إفرازات كريهة؛ لا شيء من هذا موجود.",
    "D": "<bdi>abruptio placentae</bdi> يعطي نزيف مهبلي مؤلم مع رحم متشنج ومؤلم وضيق جنيني، مو <bdi>retraction ring</bdi> مع تقدم متوقف.",
},
}

HIGHLIGHT_TERMS = {
"AS-2251": ["headache, anxiety, and mastalgia", "start 8-10 days before menstruation and improve afterward"],
"AS-2252": ["19-year-old", "beginning with the onset of menses", "no pain between menses", "Physical examination normal"],
"AS-2255": ["secondary amenorrhea for 6 month", "normal FSH and prolactin"],
"AS-2256": ["primary amenorrhea", "present breast development and secondary characteristics"],
"AS-2262": ["24 weeks' gestation", "intrauterine fetal death", "induce labor"],
"AS-2270": ["amenorrhea", "mass felt from vagina during DRE", "Diagonal incision across the hymen"],
"AS-2272": ["retained placenta for 30 min"],
"AS-2275": ["9 weeks gestation", "hyperthyroidism"],
"AS-2284": ["30 weeks", "preterm premature rupture of membranes", "fever and abdominal pain"],
"AS-2284B": ["preterm premature rupture of membranes", "fever and abdominal pain"],
"AS-2284C": ["prelabor premature rupture of membranes for 7 days", "rigors, and fever", "purulent, foul-smelling vaginal discharge"],
"AS-2292": ["Primigravida", "no medical history or family history of DM"],
"AS-2293": ["38 wkf", "twins in vertex position", "ctg was normal"],
"AS-2295": ["right ovarian cyst measuring 12 cm"],
"AS-2309": ["epilepsy", "valproic acid"],
"AS-2313": ["10 wks", "previous 2 abortion due to congenital anomalies", "screening for anomalies"],
"AS-2315": ["regular adequate contractions", "retraction ring"],
}
