# -*- coding: utf-8 -*-
# Batch r13: Surgery (AS-1914 .. AS-2535) + ENT (AS-0008 .. AS-1118)

EXPLANATIONS = {

"AS-1914": {
    "correct_letter": "C",
    "self_judged": True,
    "idea": "<bdi>blunt renal trauma</bdi> والسؤال يفرق بين <bdi>extravasation</bdi> دم ولا بول، والحل يعتمد على <bdi>hemodynamic stability</bdi> أولاً.",
    "clues": [
        ("blunt abdominal trauma", "آلية <bdi>trauma</bdi> تخلينا نفكر بإصابة <bdi>kidney</bdi>"),
        ("Extravasation around the left kidney", "تسرب حول <bdi>kidney</bdi>، لازم نحدد نوعه قبل القرار"),
    ],
    "why_correct": [
        "ما قالوا إن المريض <bdi>unstable</bdi>، وما فيه وصف لـ<bdi>active arterial blush</bdi> واضح، يعني الأقرب إنه <bdi>stable</bdi> بدون نزيف شرياني فعال.",
        "في هالحالة الإدارة الصحيحة هي <bdi>conservative management</bdi>: إعطاء <bdi>IV fluids</bdi> ومراقبة مع متابعة <bdi>Hb</bdi> متسلسلة.",
        "الجراحة أو <bdi>embolization</bdi> تنحفظ لحالات محددة (<bdi>unstable</bdi> أو نزيف شرياني فعال)، وهذا مو وصف السيناريو هنا.",
    ],
    "when_changes": [
        "لو السؤال وصف <bdi>active contrast blush</bdi> على <bdi>CT</bdi> مع مريض <bdi>stable</bdi>، الجواب يتحول إلى <bdi>angioembolization</bdi>.",
        "لو المريض <bdi>unstable</bdi> ومو مستجيب للسوائل، الجواب يصير <bdi>surgical exploration</bdi> (إصلاح أو <bdi>nephrectomy</bdi>).",
    ],
    "rule": "في <bdi>blunt renal trauma</bdi>، <bdi>stability</bdi> هي اللي تقرر: <bdi>stable</bdi> بدون نزيف فعال يعني <bdi>observation</bdi>، مو كل <bdi>extravasation</bdi> يعني تدخل جراحي.",
    "comparison": None,
    "labs": None,
    "guideline_note": "هذا <bdi>qno</bdi> بدون جواب مؤكد من المصدر، فاخترت <bdi>C</bdi> بناءً على إن السيناريو ما ذكر عدم استقرار أو نزيف شرياني فعال، فيكون القرار المعياري <bdi>conservative</bdi>.",
},

"AS-1915": {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "<bdi>axillary mass</bdi> عند امرأة، والسؤال يبي الخطوة الأولى للتقييم مو تشخيص نهائي.",
    "clues": [
        ("axillary mass 3x3", "كتلة جديدة بالإبط لازم تقييم بالتصوير قبل أي قرار"),
        ("soft and movable", "صفات تطمن شوي بس ما تكفي للتطمين المباشر بدون تصوير"),
    ],
    "why_correct": [
        "كتلة <bdi>axillary</bdi> جديدة، حتى لو <bdi>soft and movable</bdi>، تحتاج <bdi>imaging</bdi> قبل أي قرار علاجي.",
        "<bdi>Bilateral mammogram</bdi> هو خطوة التصوير الأولية المعتادة في المرأة لتقييم كتلة بمنطقة الثدي/الإبط، وبعدها حسب النتيجة يتقرر إذا نحتاج <bdi>biopsy</bdi>.",
        "<bdi>Reassurance</bdi> المباشر بدون تصوير غير مناسب لأن ما زال فيه احتمال إنها كتلة متعلقة بنسيج ثدي إضافي أو <bdi>lymph node</bdi> مشتبه.",
    ],
    "when_changes": [
        "لو التصوير رجع بنتيجة مشبوهة (<bdi>solid, irregular</bdi>)، الجواب التالي يصير <bdi>core biopsy</bdi>.",
        "لو الكتلة بوضوح <bdi>lipoma</bdi> بالفحص السريري مع تصوير سابق مطمن، يصير <bdi>reassurance</bdi> مقبول.",
    ],
    "rule": "أي كتلة جديدة بالإبط أو الثدي: <bdi>imaging</bdi> أولاً، ثم <bdi>biopsy</bdi> لو مشبوه، و<bdi>reassurance</bdi> يكون آخر خطوة مو أول خطوة.",
    "comparison": None,
    "labs": None,
    "guideline_note": "هذا السؤال بدون جواب مؤكد من المصدر، فاخترت <bdi>A</bdi> لأن التصوير هو الخطوة المعيارية الأولى قبل <bdi>biopsy</bdi> أو <bdi>reassurance</bdi>.",
},

"AS-1916": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "كتلة بالثدي عند <bdi>pregnant woman</bdi>، والسؤال يبي أول خطوة تصوير آمنة بالحمل.",
    "clues": [
        ("Pregnant", "<bdi>pregnancy</bdi> تغيّر نوع التصوير المفضل (نتجنب الإشعاع)"),
        ("28 weeks", "حمل متقدم، والكتلة موجودة من فترة، فلازم تقييم الآن مو تأجيل"),
        ("breast mass", "كتلة جديدة بالثدي تحتاج تقييم بالتصوير قبل أي قرار"),
    ],
    "why_correct": [
        "كتلة بالثدي عند <bdi>pregnant</bdi> (28 <bdi>weeks</bdi>) موجودة من 4 أشهر، لازم تقييم الآن.",
        "أفضل وأول تصوير بالحمل هو <bdi>ultrasound</bdi> لأنه يفرق بين <bdi>cystic</bdi> و<bdi>solid lesion</bdi> بدون إشعاع.",
        "<bdi>Bilateral US</bdi> يقيم الثديين والإبط، وبعدها لو فيه كتلة <bdi>solid</bdi> مشبوهة تجي خطوة <bdi>core biopsy</bdi>.",
    ],
    "when_changes": [
        "لو المرأة غير <bdi>pregnant</bdi> وعمرها فوق 30، الجواب يتحول إلى <bdi>mammogram</bdi> كتصوير أول.",
        "لو <bdi>US</bdi> أظهرت كتلة <bdi>solid</bdi> مشبوهة، الخطوة التالية تصير <bdi>core biopsy</bdi> مو <bdi>FNA</bdi>.",
    ],
    "rule": "كتلة ثدي بالحمل = <bdi>ultrasound</bdi> أولاً دايمًا، وأبدًا ما نأجل التقييم إلى بعد الولادة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1917": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نفس مبدأ كتلة الثدي بالحمل، بس هنا بوصف <bdi>enlarging mass</bdi> و<bdi>firm movable</bdi>، والسؤال يبي الخطوة التالية.",
    "clues": [
        ("28-week pregnant", "الحمل يحدد نوع التصوير الأول"),
        ("enlarging right breast mass", "كتلة تكبر تحتاج تقييم فوري مو تأجيل"),
        ("firm movable", "صفة <bdi>firm</bdi> ترفع الشك شوي، بس التصوير هو الخطوة الأولى بعدها"),
    ],
    "why_correct": [
        "كتلة <bdi>enlarging</bdi> بثدي <bdi>pregnant</bdi> تحتاج تقييم الآن، والسؤال يبي <bdi>next step</bdi>.",
        "<bdi>Ultrasound</bdi> هو أأمن تصوير أول بالحمل: بدون إشعاع وأدق من <bdi>mammogram</bdi> بالثدي الكثيف وقت الحمل.",
        "<bdi>Bilateral US</bdi> يحدد صفات الكتلة (3x2 <bdi>cm</bdi>) ويفحص الثدي الثاني والإبط قبل أي <bdi>biopsy</bdi>.",
    ],
    "when_changes": [
        "لو المرأة غير حامل وفوق 30 سنة، أول تصوير يصير <bdi>mammogram</bdi>.",
        "بعد <bdi>US</bdi> لو الكتلة <bdi>solid</bdi> مشبوهة، الخطوة التالية <bdi>core biopsy</bdi> مو <bdi>FNA</bdi> مباشرة.",
    ],
    "rule": "الحمل يحوّل أول خطوة تصوير من <bdi>mammogram</bdi> إلى <bdi>ultrasound</bdi>، وكتلة تكبر أبدًا ما تتأجل لبعد الولادة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1918": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "انسداد بالأمعاء (<bdi>bowel obstruction</bdi>) عند شخص بدون أي تاريخ جراحي سابق، والسؤال يبي السبب الأكثر احتمالاً.",
    "clues": [
        ("bowel obstruction", "تشخيص مؤكد، والسؤال يبي السبب"),
        ("no medical or surgical history", "عدم وجود عمليات سابقة يستبعد <bdi>adhesions</bdi> كأكثر سبب شائع"),
    ],
    "why_correct": [
        "<bdi>Adhesions</bdi> هي أشيع سبب لـ<bdi>small bowel obstruction</bdi> بشكل عام، بس لازم يكون فيه تاريخ عملية سابقة بالبطن.",
        "هذا المريض عمره 23 وبدون أي <bdi>surgical history</bdi> (يعني <bdi>virgin abdomen</bdi>)، فأكثر سبب محتمل يصير <bdi>hernia</bdi>.",
        "لازم نفحص المنطقة الإنكبية (<bdi>groin</bdi>) والسرة للبحث عن <bdi>incarcerated hernia</bdi>.",
    ],
    "when_changes": [
        "لو المريض عنده تاريخ عملية بطنية سابقة، الجواب يتحول إلى <bdi>adhesions</bdi>.",
        "لو المريض طفل صغير بدون جراحة سابقة ومعه <bdi>painless rectal bleeding</bdi>، نفكر بـ<bdi>Meckel's diverticulum</bdi>.",
    ],
    "rule": "سبب <bdi>bowel obstruction</bdi> يعتمد على التاريخ الجراحي: فيه عملية سابقة = <bdi>adhesions</bdi>، بدون عملية سابقة (<bdi>virgin abdomen</bdi>) = <bdi>hernia</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1923": {
    "correct_letter": "C",
    "self_judged": True,
    "idea": "مريض <bdi>trauma</bdi> فمه مليان دم، والسؤال يبي أفضل طريقة لتأمين <bdi>airway</bdi>.",
    "clues": [
        ("mouth is full og blood", "<bdi>aspiration risk</bdi> عالي ومؤشر على الحاجة لـ<bdi>definitive airway</bdi>"),
    ],
    "why_correct": [
        "فم مليان دم مع <bdi>loss of consciousness</bdi> وكسور متعددة ونزيف شديد هو مؤشر واضح للحاجة إلى <bdi>definitive airway</bdi> فورًا.",
        "ما فيه ذكر لكسر بالوجه (<bdi>facial fracture</bdi>) يمنع <bdi>intubation</bdi>، فالخيار المعياري هو <bdi>Endotracheal intubation</bdi>.",
        "<bdi>Cricothyroidotomy</bdi> و<bdi>tracheostomy</bdi> تنحفظ لحالات فشل <bdi>intubation</bdi> أو كسور وجه كبيرة تمنع <bdi>oral intubation</bdi>.",
    ],
    "when_changes": [
        "لو السيناريو أضاف كسر وجه كبير (<bdi>maxillofacial fracture</bdi>) يمنع <bdi>intubation</bdi>، الجواب يتحول إلى <bdi>cricothyroidotomy</bdi>.",
        "لو <bdi>intubation</bdi> فشلت فعليًا عدة مرات، الخطوة التالية تصير <bdi>surgical airway</bdi> حسب العمر.",
    ],
    "rule": "فم مليان دم لوحده يعني <bdi>intubate</bdi>؛ ما يصير <bdi>cricothyroidotomy</bdi> إلا لو فيه كسر وجه يمنع <bdi>intubation</bdi> أو فشلت المحاولة.",
    "comparison": None,
    "labs": None,
    "guideline_note": "بدون جواب مؤكد من المصدر، اخترت <bdi>C</bdi> لأن السيناريو ما ذكر كسر وجه يمنع <bdi>intubation</bdi> ولا فشل محاولة سابقة.",
},

"AS-1924": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفل عمره 10 سنوات بإصابة بالوجه و<bdi>intubation</bdi> فشلت عدة مرات، السؤال يبي <bdi>surgical airway</bdi> المناسب حسب العمر.",
    "clues": [
        ("child (10 y.o)", "عمر أقل من 12 سنة يمنع <bdi>surgical cricothyroidotomy</bdi>"),
        ("several hits on his face", "إصابة وجه تزيد خطورة محاولات <bdi>intubation</bdi> المتكررة"),
        ("failure", "فشل <bdi>intubation</bdi> المتكرر يستدعي <bdi>surgical airway</bdi>"),
    ],
    "why_correct": [
        "الطفل عمره 10 سنوات، ومعه إصابة وجه، وفشلت <bdi>intubation</bdi> عدة مرات، فلازم <bdi>surgical airway</bdi>.",
        "<bdi>Surgical cricothyroidotomy</bdi> يُتجنّب تحت عمر 12 سنة تقريبًا لأن <bdi>cricoid</bdi> هو أضيق جزء بمجرى الهواء عند الأطفال، وإصابته تسبب <bdi>subglottic stenosis</bdi>.",
        "لذلك الخيار الجراحي المتبقي هو <bdi>Tracheostomy</bdi>.",
    ],
    "when_changes": [
        "لو نفس السيناريو عند بالغ، الجواب يتحول إلى <bdi>cricothyroidotomy</bdi>.",
        "لو الطفل أقل من 12 سنة ويحتاج <bdi>bridge</bdi> سريع، نستخدم <bdi>needle cricothyroidotomy</bdi> بدل الجراحي.",
    ],
    "rule": "فشل <bdi>intubation</bdi> يعني <bdi>surgical airway</bdi>، والعمر يحدد النوع: بالغ أو طفل ≥12 = <bdi>cricothyroidotomy</bdi>، طفل أصغر = <bdi>tracheostomy</bdi> أو <bdi>needle cricothyroidotomy</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1926": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>reducible inguinal hernia</bdi> عند <bdi>newborn</bdi>، والسؤال يبي العلاج الجراحي المعياري عند الأطفال.",
    "clues": [
        ("newborn", "عمر صغير جدًا يغيّر نوع الجراحة المطلوبة عن البالغين"),
        ("reducible inguinal hernia", "<bdi>inguinal hernia</bdi> لا تُحل تلقائيًا وتحتاج جراحة"),
    ],
    "why_correct": [
        "<bdi>Reducible right inguinal hernia</bdi> عند <bdi>newborn</bdi> تحتاج إصلاح جراحي بـ<bdi>Herniotomy</bdi> (ربط عالي واستئصال الكيس).",
        "<bdi>Inguinal hernia</bdi> عند الأطفال لا تُغلق تلقائيًا، وخطر <bdi>incarceration</bdi> أعلى بمرحلة الرضاعة، فيتم الإصلاح بشكل انتخابي بأقرب وقت.",
        "الجانب الأيسر طبيعي (بدون تورم) فلا يحتاج علاج.",
    ],
    "when_changes": [
        "لو كانت <bdi>umbilical hernia</bdi> بدل <bdi>inguinal</bdi>، الجواب يتحول إلى <bdi>observation</bdi> لأنها تُغلق تلقائيًا بالغالب.",
        "لو المريض بالغ، يصير الإصلاح بـ<bdi>mesh repair</bdi> مو <bdi>herniotomy</bdi>.",
    ],
    "rule": "<bdi>Inguinal hernia</bdi> عند الأطفال = <bdi>herniotomy</bdi> بأقرب وقت، بينما <bdi>umbilical hernia</bdi> فقط تُعطى فرصة للانتظار والمراقبة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1949": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "السؤال يختبر حساب <bdi>GCS</bdi> بعد <bdi>head trauma</bdi> وتصنيف شدة الإصابة.",
    "clues": [
        ("confused", "<bdi>Verbal</bdi> = 4 نقاط"),
        ("opens his eyes to sound", "<bdi>Eye</bdi> = 3 نقاط"),
        ("localizes pain", "<bdi>Motor</bdi> = 5 نقاط"),
    ],
    "why_correct": [
        "نحسب كل مكون: <bdi>Eye</bdi> = 3 (يفتح للصوت)، <bdi>Verbal</bdi> = 4 (<bdi>confused</bdi>)، <bdi>Motor</bdi> = 5 (<bdi>localizes pain</bdi>).",
        "المجموع = 12، و<bdi>GCS</bdi> من 9 إلى 12 يصنف كـ<bdi>Moderate head injury</bdi>.",
    ],
    "when_changes": [
        "لو كان <bdi>GCS</bdi> من 13 إلى 15 (مثلًا يفتح عينه عفويًا أو يطيع الأوامر)، يصير <bdi>Mild</bdi>.",
        "لو <bdi>GCS</bdi> 8 أو أقل، يصير <bdi>Severe</bdi> وهو مؤشر <bdi>intubation</bdi>.",
    ],
    "rule": "<bdi>GCS</bdi>: 13-15 <bdi>Mild</bdi>، 9-12 <bdi>Moderate</bdi>، ≤8 <bdi>Severe</bdi>، واحسب كل مكون (<bdi>Eye/Verbal/Motor</bdi>) بدقة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1954": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "<bdi>bilateral green discharge</bdi> من الحلمة مع <bdi>BI-RADS 2</bdi>، والسؤال يبي الخطوة التالية لإفراز حميد.",
    "clues": [
        ("Bilateral green discharge", "إفراز ثنائي غير دموي، نمط حميد غالبًا"),
        ("dilated ducts", "يتوافق مع <bdi>duct ectasia</bdi>"),
        ("BI RADS 2", "تصنيف حميد مؤكد بالتصوير"),
    ],
    "why_correct": [
        "إفراز <bdi>bilateral green</bdi> (غير دموي) مع <bdi>dilated ducts</bdi> بالتصوير يتوافق مع <bdi>duct ectasia</bdi>، وهي حالة حميدة.",
        "التصوير مصنف <bdi>BI-RADS 2</bdi> (نتيجة حميدة)، فلا يحتاج <bdi>biopsy</bdi>.",
        "الخطوة التالية المناسبة هي <bdi>Reassurance</bdi> مع <bdi>follow-up</bdi> روتيني.",
    ],
    "when_changes": [
        "لو الإفراز كان من جانب واحد ودموي، الجواب يتحول نحو تحقيق إضافي أو <bdi>duct excision</bdi>.",
        "لو <bdi>BI-RADS</bdi> كان 4 أو 5، الخطوة تصير <bdi>core needle biopsy</bdi>.",
    ],
    "rule": "إفراز حلمة <bdi>bilateral</bdi>، متعدد القنوات، غير دموي = حميد؛ أحادي الجانب، قناة واحدة، دموي = يحتاج تحقيق.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1955": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "<bdi>gallbladder polyp</bdi> صغير بس المريضة <bdi>symptomatic</bdi>، والسؤال يبي القرار الصحيح حسب الأعراض لا الحجم فقط.",
    "clues": [
        ("0.8 polyp", "حجم صغير (0.8 <bdi>cm</bdi>) غالبًا يكفي للمراقبة لو ما فيه أعراض"),
        ("bothered by sx", "وجود أعراض يغيّر القرار العلاجي بشكل كامل"),
    ],
    "why_correct": [
        "<bdi>gallbladder polyp</bdi> مع <bdi>recurrent RUQ pain</bdi> والمريضة <bdi>bothered by symptoms</bdi> يعني <bdi>symptomatic polyp</bdi>.",
        "أعراض المرارة غير المفسرة بسبب آخر هي مؤشر لـ<bdi>cholecystectomy</bdi> بغض النظر عن حجم <bdi>polyp</bdi>.",
        "الجراحة تعالج الأعراض وتزيل أي احتمال خباثة مستقبلي.",
    ],
    "when_changes": [
        "لو <bdi>polyp</bdi> بدون أعراض وحجمه صغير، الجواب يتحول إلى <bdi>conservative</bdi> أو <bdi>surveillance US</bdi>.",
        "لو حجم <bdi>polyp</bdi> ≥10 <bdi>mm</bdi> حتى بدون أعراض، يصير <bdi>cholecystectomy</bdi> أيضًا.",
    ],
    "rule": "قاعدة الحجم بـ<bdi>gallbladder polyp</bdi> تنطبق فقط لو المريض بدون أعراض؛ لو فيه أعراض منسوبة للمرارة، العملية هي الحل.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1965": {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "إصابات متعددة بالكبد بعد حادث، والسؤال يبي الإدارة الجراحية المعيارية.",
    "clues": [
        ("multiple liver injuries", "تعدد الإصابات يوجه نحو <bdi>damage control</bdi> لا إصلاح موجه"),
    ],
    "why_correct": [
        "إصابات كبد متعددة بعد حادث، بدون معلومة أكيدة عن الاستقرار، توجه نحو <bdi>damage control surgery</bdi>.",
        "<bdi>Liver packing</bdi> (<bdi>perihepatic packing</bdi>) يضغط على النزيف المنتشر بسرعة ويسمح بتصحيح <bdi>coagulopathy</bdi> قبل عملية ثانية مخططة.",
        "<bdi>Ligation</bdi> الانتقائي يناسب نزيف من وعاء واحد محدد مو إصابات متعددة.",
    ],
    "when_changes": [
        "لو المريض <bdi>stable</bdi> بدون نزيف فعال، الجواب يتحول إلى <bdi>non-operative management</bdi> بالمراقبة.",
        "لو فيه نزيف محدد من وعاء واحد فقط، الخطوة تصير <bdi>selective vessel ligation</bdi>.",
    ],
    "rule": "إصابات كبد <bdi>multiple</bdi> عند مريض يحتاج تدخل جراحي = <bdi>perihepatic packing</bdi> كخطوة <bdi>damage control</bdi> أولى.",
    "comparison": None,
    "labs": None,
    "guideline_note": "بدون جواب مؤكد من المصدر، اخترت <bdi>A</bdi> (<bdi>liver packing</bdi>) لأن تعدد الإصابات هو مؤشر <bdi>damage control</bdi> المعياري.",
},

"AS-1966": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "مريض <bdi>unstable</bdi> بعد <bdi>trauma</bdi> مع إصابات كبد متعددة مؤكدة، والجواب هو إدارة <bdi>damage control</bdi> المعيارية.",
    "clues": [
        ("unstable", "عدم الاستقرار يستدعي <bdi>damage control surgery</bdi> مباشرة"),
        ("mul7ple liver lacera7ons", "تعدد الجروح يمنع الإصلاح النهائي الفوري"),
    ],
    "why_correct": [
        "مريض <bdi>unstable</bdi> مع <bdi>multiple liver lacerations</bdi> يحتاج <bdi>damage control surgery</bdi>.",
        "<bdi>Perihepatic packing</bdi> يضغط على النزيف المنتشر بسرعة، يسمح بالإنعاش وتصحيح <bdi>coagulopathy</bdi>، ويتبعه <bdi>second look</bdi> مخطط.",
        "لو فشل <bdi>packing</bdi>، الخطوة التالية <bdi>angioembolization</bdi> أو استئصال.",
    ],
    "when_changes": [
        "لو المريض <bdi>stable</bdi>، الجواب يتحول إلى <bdi>non-operative management</bdi>.",
        "لو كان الإصابة بوعاء واحد محدد عند مريض <bdi>stable</bdi> يحتمل إصلاح نهائي، يصير <bdi>ligation</bdi> الانتقائي مناسب.",
    ],
    "rule": "إصابة كبد في مريض <bdi>unstable</bdi> = <bdi>laparotomy</bdi> + <bdi>perihepatic packing</bdi>، مو استئصال كبير أو <bdi>ligation</bdi> شرياني وحيد.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1973": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "<bdi>burn</bdi> بنسبة محسوبة بـ<bdi>rule of nines</bdi>، والسؤال يبي تطبيق <bdi>Parkland formula</bdi> بشكل صحيح.",
    "clues": [
        ("2nd degree burn to his both lower limbs", "كل طرف سفلي = 18%، فكلا الطرفين = 36% <bdi>TBSA</bdi>"),
        ("Weight 70 kg", "الوزن يدخل مباشرة بمعادلة <bdi>Parkland</bdi>"),
        ("Parkland formula", "المعادلة: 4 <bdi>ml</bdi> × <bdi>kg</bdi> × %<bdi>TBSA</bdi>"),
    ],
    "why_correct": [
        "كل طرف سفلي = 18% (أمامي 9% + خلفي 9%)، فكلا الطرفين = 36% <bdi>TBSA</bdi>، و<bdi>2nd degree burn</bdi> تُحسب.",
        "<bdi>Parkland</bdi>: 4 <bdi>ml</bdi> × 70 <bdi>kg</bdi> × 36 = حوالي 10 <bdi>L</bdi> من <bdi>Ringer's lactate</bdi> خلال 24 ساعة.",
        "نص الكمية (حوالي 5 <bdi>L</bdi>) تُعطى بالجزء الأول، والنص الآخر خلال باقي 16 ساعة، وهذا يطابق الخيار <bdi>C</bdi>.",
    ],
    "when_changes": [
        "لو كانت الحروق بطرف سفلي واحد فقط، النسبة تصير 18% فقط وتتغير الكمية الكلية إلى النصف تقريبًا.",
        "لو الحرق من الدرجة الأولى (<bdi>superficial</bdi>) فقط، لا يُحسب بمعادلة <bdi>Parkland</bdi> أصلًا.",
    ],
    "rule": "<bdi>Parkland formula</bdi> = 4 <bdi>ml</bdi> × <bdi>kg</bdi> × %<bdi>TBSA</bdi> خلال 24 ساعة، نص الكمية بالثماني ساعات الأولى، والباقي خلال 16 ساعة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1976": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "كيس بـ<bdi>lesser sac</bdi> بعد التعافي من <bdi>severe pancreatitis</bdi>، والسؤال يبي التشخيص الأقرب.",
    "clues": [
        ("recovers from an attack of severe pancreatitis", "التسلسل الزمني يوجه نحو مضاعفة متأخرة لـ<bdi>pancreatitis</bdi>"),
        ("cyst form in lesser sac", "موقع نموذجي لـ<bdi>pancreatic pseudocyst</bdi>"),
    ],
    "why_correct": [
        "كيس في <bdi>lesser sac</bdi> يظهر بعد التعافي من <bdi>severe pancreatitis</bdi> مع <bdi>epigastric fullness</bdi> و<bdi>bloating</bdi> وفقدان شهية يتوافق مع <bdi>pancreatic pseudocyst</bdi>.",
        "<bdi>Pseudocyst</bdi> هو تجمع سوائل محاط بجدار ليفي بدون بطانة طلائية، يتشكل بعد أكثر من 4 أسابيع من <bdi>acute pancreatitis</bdi>.",
        "<bdi>CT</bdi> هو أفضل تصوير لتأكيده.",
    ],
    "when_changes": [
        "لو ظهرت <bdi>fever</bdi> و<bdi>leukocytosis</bdi> وغازات على <bdi>CT</bdi>، التشخيص يتحول إلى <bdi>pancreatic abscess</bdi>.",
        "لو المريض كبير بالسن مع فقدان وزن وبدون قصة <bdi>pancreatitis</bdi> حادة، نفكر بـ<bdi>pancreatic cancer</bdi>.",
    ],
    "rule": "كيس <bdi>lesser sac</bdi> بعد أكثر من 4 أسابيع من <bdi>acute pancreatitis</bdi> = <bdi>pseudocyst</bdi>؛ أضف <bdi>fever</bdi> و<bdi>gas</bdi> ليصير <bdi>abscess</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1979": {
    "correct_letter": "C",
    "self_judged": True,
    "idea": "<bdi>MVA</bdi> مع كسور أضلاع متعددة، مريض كان <bdi>stable</bdi> ثم بدأ يتدهور مع صدر نظيف بالفحص، والسؤال يبي السبب الأرجح.",
    "clues": [
        ("fractured 3 ribs", "كسور أضلاع متعددة ترفع احتمال إصابة رئة تحتها"),
        ("at first stable Then become distressed", "تدهور متأخر يناسب <bdi>pulmonary contusion</bdi> التي تتطور تدريجيًا"),
        ("Chest clear", "عدم وجود علامات موضعية بالفحص يستبعد <bdi>tamponade</bdi> أو <bdi>flail chest</bdi> الواضح"),
    ],
    "why_correct": [
        "<bdi>Pulmonary contusion</bdi> تتميز بتدهور متأخر وتدريجي بالأكسجين بعد <bdi>blunt chest trauma</bdi>، مع صدر قد يبدو نظيف بالفحص السريري الأولي.",
        "كسور الأضلاع المتعددة شائعة كآلية مصاحبة لـ<bdi>pulmonary contusion</bdi> حتى بدون حركة متناقضة واضحة (<bdi>paradoxical movement</bdi>).",
        "غياب علامات <bdi>flail chest</bdi> (حركة متناقضة) أو <bdi>tamponade</bdi> (ارتفاع <bdi>JVP</bdi>) يدعم <bdi>pulmonary contusion</bdi> كتفسير للتدهور.",
    ],
    "when_changes": [
        "لو ذُكرت حركة صدر متناقضة (<bdi>paradoxical movement</bdi>)، الجواب يتحول إلى <bdi>flail chest</bdi>.",
        "لو ذُكر انخفاض ضغط مع ارتفاع <bdi>JVP</bdi> وأصوات قلب مكتومة، الجواب يتحول إلى <bdi>cardiac tamponade</bdi>.",
    ],
    "rule": "تدهور تدريجي بالأكسجين بعد <bdi>blunt chest trauma</bdi> مع صدر نظيف = فكر بـ<bdi>pulmonary contusion</bdi> أولاً.",
    "comparison": None,
    "labs": None,
    "guideline_note": "بدون جواب مؤكد من المصدر، اخترت <bdi>C</bdi> لأن التدهور التدريجي بدون علامات موضعية واضحة (لا حركة متناقضة ولا علامات <bdi>tamponade</bdi>) يناسب <bdi>pulmonary contusion</bdi> أكثر.",
},

"AS-1983": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "عقدة درقية بنتيجة <bdi>FNA</bdi> محددة (<bdi>Bethesda 4</bdi>)، والسؤال يبي الإدارة المناسبة حسب تصنيف <bdi>Bethesda</bdi>.",
    "clues": [
        ("2.3 cm solid hypoechoic nodule", "عقدة <bdi>solid</bdi> بحجم يستدعي تقييم نسيجي"),
        ("Follicular neoplasm, Bethesda 4", "هذا التصنيف لا يُحسم بالخلايا، يحتاج استئصال للتفرقة"),
    ],
    "why_correct": [
        "العلامة الحاسمة هي نتيجة <bdi>FNA</bdi>: «<bdi>follicular neoplasm, Bethesda 4</bdi>».",
        "الخلايا لا تقدر تفرق بين <bdi>follicular adenoma</bdi> و<bdi>follicular carcinoma</bdi> لأن الفرق يحتاج دليل على غزو المحفظة أو الأوعية بالأنسجة، فلازم استئصال الفص: <bdi>Hemithyroidectomy</bdi>.",
        "<bdi>TSH</bdi> و<bdi>free T4</bdi> طبيعيان، يعني العقدة غير فعالة هرمونيًا، فلا حاجة لفحص نووي أو علاج مضاد للدرقية قبل ذلك.",
    ],
    "when_changes": [
        "لو كانت نتيجة <bdi>FNA</bdi> حميدة (<bdi>Bethesda 2</bdi>)، الجواب يتحول إلى مراقبة بـ<bdi>US follow-up</bdi>.",
        "لو <bdi>TSH</bdi> منخفض مع عقدة، الخطوة الأولى تصير فحص نووي (<bdi>isotope scan</bdi>) قبل أي شيء آخر.",
    ],
    "rule": "تصنيف <bdi>Bethesda</bdi> يحدد الإدارة: 4 يعني <bdi>Hemithyroidectomy</bdi>، 2 يعني مراقبة، 6 يعني استئصال كامل أو جزئي حسب الخطورة.",
    "comparison": None,
    "labs": [["TSH", "2.3 pU/mL", "0.4-5.0 pU/mL"], ["Free T4", "11.3 pmol/L", "8.5-15.2 pmol/L"]],
    "guideline_note": None,
},

"AS-1984": {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "مريض حادث سيارة بإصابات وجه و<bdi>desaturating</bdi>، والسؤال يبي الخطوة التالية لتأمين <bdi>airway</bdi>.",
    "clues": [
        ("facial injuries", "إصابة وجه ترفع احتمال صعوبة <bdi>intubation</bdi> بس لا تمنعها دايمًا"),
        ("Desaturating", "انخفاض الأكسجين هو مؤشر واضح للحاجة لـ<bdi>definitive airway</bdi>"),
    ],
    "why_correct": [
        "<bdi>Desaturation</bdi> هي مؤشر مباشر للحاجة إلى <bdi>definitive airway</bdi> فورًا.",
        "ما فيه ذكر لتشوه كبير بالوجه يمنع فتح الفم أو يجعل التنبيب مستحيل، فالخيار المعياري الأول يبقى <bdi>Endotracheal intubation</bdi>.",
        "<bdi>Cricothyroidotomy</bdi> تُحجز لحالات فشل <bdi>intubation</bdi> أو تشوه تشريحي يمنعها تمامًا.",
    ],
    "when_changes": [
        "لو كانت إصابة الوجه شديدة بشكل يمنع فتح الفم أو رؤية الحبال الصوتية، الجواب يتحول إلى <bdi>cricothyroidotomy</bdi>.",
        "لو <bdi>intubation</bdi> حوولت وفشلت، الخطوة التالية تصير <bdi>surgical airway</bdi>.",
    ],
    "rule": "إصابة وجه لا تعني تلقائيًا <bdi>surgical airway</bdi>؛ إلا لو منعت <bdi>oral intubation</bdi> فعليًا أو فشلت المحاولة.",
    "comparison": None,
    "labs": None,
    "guideline_note": "بدون جواب مؤكد من المصدر، اخترت <bdi>A</bdi> لأن السيناريو لم يذكر تشوه وجه يمنع <bdi>intubation</bdi> ولا فشل محاولة سابقة.",
},

"AS-1985": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "حمى بيوم 6-7 بعد عملية مع جرح نظيف بدون إفراز، والسؤال يبي الخطوة المنطقية لعدم وجود هدف موضعي واضح.",
    "clues": [
        ("day 6/7 Post OP", "توقيت متأخر نسبيًا يفتح احتمالات متعددة لحمى ما بعد العملية"),
        ("fever", "الحمى تحتاج تفسير منظم حسب اليوم بعد العملية"),
        ("dry wound", "جرح بدون إفراز يستبعد التهاب الجرح كسبب مباشر"),
    ],
    "why_correct": [
        "حمى بيوم 6-7 بعد العملية مع «<bdi>dry wound</bdi>» لا تعطي هدف موضعي: لا إفراز لنأخذ منه عينة ولا تجمع لنفتحه.",
        "من الخيارات المتاحة، الخطوة المفيدة هي مراجعة قائمة الأدوية (<bdi>review medications</bdi>)، لأن <bdi>drug fever</bdi> (غالبًا من المضادات الحيوية) سبب معروف لحمى متأخرة بعد العملية مع جرح نظيف.",
        "هذا السبب يُعتبر غالبًا تشخيص استبعاد بعد نفي الأسباب الموضعية الأخرى.",
    ],
    "when_changes": [
        "لو الجرح أصبح أحمر ومتوّرم مع إفراز، الجواب يتحول إلى <bdi>wound swab</bdi>.",
        "لو ظهرت أعراض بطنية أو إيجابي بالفحص الشرجي (<bdi>DRE</bdi>)، لازم نفكر بـ<bdi>intra-abdominal abscess</bdi>.",
    ],
    "rule": "حمى ما بعد العملية تُفسر حسب اليوم (<bdi>5 W's</bdi>): يوم 1 رئة منخمصة، أيام 2-3 رئة/بول، أيام 4-5 جرح/<bdi>DVT</bdi>، بعد 5-7 خراج بطني، وأي يوم أدوية.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1985B": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "حمى بيوم 5 بعد <bdi>hysterectomy</bdi> عند مريضة بدون أي شكوى أو علامات موضعية، والسؤال يبي الخطوة المنطقية.",
    "clues": [
        ("5th day post-hysterectomy", "توقيت يفتح احتمالات عدة لحمى ما بعد العملية"),
        ("fever", "الحمى تحتاج تفسير منظم"),
        ("wound is clean", "جرح نظيف يستبعد التهاب الجرح كسبب مباشر"),
    ],
    "why_correct": [
        "المريضة بيوم 5 بحمى بس «<bdi>does not complain of anything</bdi>» والجرح نظيف: لا دليل بولي، صدري، أو جرحي يوجهنا لفحص محدد.",
        "<bdi>Drug fever</bdi> سبب غير جراحي يُنسى غالبًا، ومفيد مراجعته أولاً في مريضة لا تبدو مريضة.",
    ],
    "when_changes": [
        "لو فيه أعراض بولية أو قسطرة، الخطوة تصير <bdi>urinalysis and culture</bdi>.",
        "لو فيه سعال أو ضيق تنفس، الخطوة تصير <bdi>chest X-ray</bdi>.",
    ],
    "rule": "حمى بدون أعراض أو علامات موضعية بعد العملية تبدأ بمراجعة التاريخ والفحص وقائمة الأدوية، قبل الفحوصات العشوائية.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1986": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "حمى بيوم 4 بعد <bdi>sigmoid resection</bdi>، والسؤال يبي الأهم تقييمه مو أبسط خطوة تالية.",
    "clues": [
        ("postoperative day 4", "يوم 4-5 هو نطاق <bdi>surgical site infection</bdi> الكلاسيكي"),
        ("MOST IMPORTANT", "السؤال يبي الفحص الأهم مباشرة مو التسلسل الكامل"),
    ],
    "why_correct": [
        "حمى بيوم «<bdi>postoperative day 4</bdi>» تقع بنطاق أيام 4-5 حيث <bdi>surgical site infection</bdi> هو السبب الكلاسيكي.",
        "فحص الجرح سريريًا هو خطوة بجانب السرير تؤكد أو تستبعد السبب الأشيع مباشرة قبل أي تحليل.",
    ],
    "when_changes": [
        "لو كانت الحمى يوم 1، الأهم تقييمه يصير الصدر (<bdi>atelectasis</bdi>).",
        "لو الجرح نظيف تمامًا بدون أي علامة، الخطوة التالية تصير مراجعة الأدوية.",
    ],
    "rule": "طابق يوم الحمى بالسبب الأرجح: يوم 1 صدر، أيام 2-3 رئة/بول، أيام 4-5 جرح، وفحص الجرح هو الأهم بهذا النطاق.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2010": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "مريضة بـ<bdi>acute pancreatitis</bdi> متأخرة العرض مع <bdi>amylase</bdi> طبيعي بالمصل، والسؤال يبي التحليل الأدق لتأكيد التشخيص.",
    "clues": [
        ("epigastric pain for 6-days, radiating to the back", "ألم مزمن نسبيًا يفتح احتمال أن <bdi>amylase</bdi> المصلي رجع لطبيعي"),
        ("Amylase 149", "طبيعي بالمصل لا يستبعد <bdi>pancreatitis</bdi> المتأخرة"),
    ],
    "why_correct": [
        "ألم لمدة «<bdi>6 days</bdi>» مع حصيات مرارية، <bdi>ileus</bdi>، و<bdi>left pleural effusion</bdi> يقترح <bdi>acute pancreatitis</bdi>، بس <bdi>serum amylase</bdi> (149) طبيعي فعليًا لأنه يرجع طبيعي خلال أيام.",
        "<bdi>Urinary amylase</bdi> يبقى مرتفع لفترة أطول، فهو الطريقة لتأكيد <bdi>pancreatitis</bdi> متأخرة العرض.",
    ],
    "when_changes": [
        "لو التشخيص غير واضح أو نشك بمضاعفات، الخطوة تصير <bdi>CT abdomen</bdi> بعد 48-72 ساعة.",
        "لو العرض مبكر (أول يوم أو يومين)، <bdi>serum amylase</bdi> نفسه يكون كافٍ ومرتفع.",
    ],
    "rule": "<bdi>Acute pancreatitis</bdi> يحتاج 2 من 3: ألم مميز، إنزيمات أعلى من 3 مرات الطبيعي، تصوير مميز؛ <bdi>serum amylase</bdi> يرجع طبيعي بسرعة، فـ<bdi>urinary amylase</bdi> يبقى مرتفع أطول.",
    "comparison": None,
    "labs": [["Amylase (serum)", "149 IU/L", "24-151 IU/L"], ["ALP", "115 IU/L", "39-117 IU/L"], ["Direct bilirubin", "5.6 mol/L", "1.5-6.5 mol/L"], ["Total bilirubin", "15.8 mol/L", "3.5-16.5 mol/L"]],
    "guideline_note": None,
},

"AS-2018": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "حمى شديدة متكررة بيوم 4 بعد <bdi>laparotomy</bdi> لثقب <bdi>diverticular</bdi>، مع جرح وصدر طبيعيين لكن فحص شرجي غير طبيعي، يوجه نحو خراج حوضي.",
    "clues": [
        ("4th post-operative day", "توقيت يناسب التهاب أو تجمع موضعي"),
        ("high-grade fever with chills and multiple spikes", "حمى شديدة متكررة تناسب خراج أو تجمع مُصاب"),
        ("bogginess anteriorly", "علامة فحص شرجي كلاسيكية لـ<bdi>pelvic abscess</bdi>"),
    ],
    "why_correct": [
        "حمى شديدة متكررة بيوم 4 بعد <bdi>laparotomy</bdi> لثقب <bdi>diverticular</bdi>، مع جرح صحي وصدر نظيف، تستبعد الجرح والصدر كسبب.",
        "«<bdi>bogginess anteriorly</bdi>» بالفحص الشرجي (<bdi>DRE</bdi>) يحدد مكان خراج حوضي.",
        "خراج متكون لازم يُصرّف، فالعلاج المناسب هو <bdi>ultrasound guided drainage</bdi> (مع المضادات كمساعد).",
    ],
    "when_changes": [
        "لو كان التجمع صغير (أقل من 4 سم تقريبًا)، العلاج بالمضادات الحيوية فقط قد يكفي.",
        "لو المريض <bdi>unstable</bdi> أو فيه التهاب بريتوني عام، الخطوة تصير <bdi>laparotomy</bdi> لإعادة الفتح.",
    ],
    "rule": "تجمع بطني/حوضي ما بعد العملية بحجم كبير يحتاج تصريف موجه بالتصوير؛ الحجم والاستقرار يحددان الطريقة.",
    "comparison": None,
    "labs": [["Blood pressure", "110/70 mmHg", "90-120/60-80 mmHg"], ["Heart rate", "120/min", "60-100/min"], ["Respiratory rate", "18/min", "12-20/min"], ["Temperature", "38 °C", "36.1-37.2 °C"]],
    "guideline_note": None,
},

"AS-2019": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "تورم رقبي كبير مع <bdi>stridor</bdi> بعد ساعات قليلة من <bdi>total thyroidectomy</bdi>، يستدعي استكشاف فوري عند السرير لتفريغ الدم المضغوط.",
    "clues": [
        ("total thyroidectomy 5 hours ago", "توقيت قريب جدًا يوجه نحو مضاعفة نزفية حادة"),
        ("large neck swelling", "تورم كبير يوحي بتجمع دموي ضاغط"),
        ("stridor", "علامة تهديد مباشر لمجرى الهواء"),
    ],
    "why_correct": [
        "تورم رقبي كبير مع <bdi>stridor</bdi> و<bdi>shortness of breath</bdi> بعد فقط «<bdi>5 hours</bdi>» من <bdi>total thyroidectomy</bdi> هو ورم دموي ضاغط.",
        "أسرع علاج لتخفيف الضغط عن مجرى الهواء هو فتح غرز الجلد والعضلات الحزامية عند السرير لتفريغ الجلطة، ثم الرجوع لغرفة العمليات للسيطرة على النزيف.",
    ],
    "when_changes": [
        "لو كان السبب بحة صوت فقط بدون ضيق تنفس، نفكر بإصابة <bdi>recurrent laryngeal nerve</bdi>.",
        "لو ظهر تنميل حول الفم وتشنج يدوي، نفكر بـ<bdi>hypocalcemia</bdi> لا ورم دموي.",
    ],
    "rule": "تورم رقبي مع <bdi>stridor</bdi> بالساعات الأولى بعد جراحة الدرقية = افتح الجرح فورًا عند السرير، لا تنتظر ولا تنبب أولاً.",
    "comparison": None,
    "labs": [["Blood pressure", "165/90 mmHg", "90-120/60-80 mmHg"], ["Heart rate", "130/min", "60-100/min"], ["Respiratory rate", "24/min", "12-20/min"], ["Temperature", "37 °C", "36.1-37.2 °C"]],
    "guideline_note": None,
},

"AS-2020": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "انسداد بالأمعاء الكبيرة عند مريض مسن بتاريخ إمساك طويل على ملينات، والسؤال يبي موقع الـ<bdi>volvulus</bdi> الأكثر احتمالاً.",
    "clues": [
        ("absolute constipation", "انسداد تام يناسب <bdi>large bowel obstruction</bdi>"),
        ("constipation requiring use of laxatives", "تاريخ إمساك مزمن يناسب <bdi>sigmoid colon</bdi> الطويل والمترهل"),
        ("left lumbar and hypochondrium", "موقع الكتلة يناسب <bdi>sigmoid volvulus</bdi>"),
    ],
    "why_correct": [
        "ألم مع «<bdi>absolute constipation</bdi>» وتقيؤ مع بطن متمدد ومتوتر يعني <bdi>large bowel obstruction</bdi>.",
        "التاريخ الطويل من الإمساك على ملينات (<bdi>sigmoid</bdi> طويل ومترهل) وكتلة بالجانب الأيسر يوجهان نحو <bdi>sigmoid volvulus</bdi>، وهو أشيع <bdi>volvulus</bdi> بالقولون.",
    ],
    "when_changes": [
        "لو المريض أصغر عمرًا بدون تاريخ إمساك مزمن، وكتلة متجهة نحو الجزء العلوي الأيسر أو فوق السرة، نفكر بـ<bdi>caecal volvulus</bdi>.",
        "لو ظهرت علامات التهاب بريتوني أو إقفار، العلاج يتحول إلى <bdi>sigmoid colectomy</bdi> بدل التنظير.",
    ],
    "rule": "<bdi>Sigmoid volvulus</bdi> يناسب المسن بتاريخ إمساك طويل مع كتلة بالجانب الأيسر؛ <bdi>caecal volvulus</bdi> يناسب الأصغر سنًا بدون هذا التاريخ.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2021": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "مريض <bdi>cirrhosis</bdi> يحتاج <bdi>urgent laparotomy</bdi> مع <bdi>INR</bdi> مرتفع، والسؤال يبي أي مشتق دم يصحح الخلل بشكل صحيح قبل العملية.",
    "clues": [
        ("liver cirrhosis", "يسبب نقص تصنيع عوامل التجلط"),
        ("urgent laparotomy", "العملية الطارئة تستدعي تصحيح التجلط أولاً"),
        ("INR 2", "ارتفاع واضح يعكس نقص عوامل تجلط متعددة"),
        ("Prothrombin time 17", "يدعم نفس الخلل بالتجلط"),
    ],
    "why_correct": [
        "المريض يحتاج <bdi>urgent laparotomy</bdi>، والخلل الرئيسي القابل للتصحيح هو اعتلال التجلط: <bdi>INR 2</bdi> و<bdi>PT 17</bdi> يعكسان ضعف تصنيع الكبد لعوامل التجلط.",
        "<bdi>Fresh frozen plasma</bdi> يعوّض نطاقًا واسعًا من عوامل التجلط، فهو المنتج الأنسب قبل العملية.",
    ],
    "when_changes": [
        "لو كان <bdi>fibrinogen</bdi> منخفض بشكل منفصل أو فيه <bdi>DIC</bdi>، نعطي <bdi>cryoprecipitate</bdi>.",
        "لو <bdi>platelets</bdi> أقل من 50 تقريبًا قبل عملية كبيرة، نعطي <bdi>platelets</bdi>.",
    ],
    "rule": "قبل جراحة طارئة بمريض <bdi>cirrhosis</bdi>، صحح <bdi>INR</bdi> المرتفع بـ<bdi>FFP</bdi>، لا تنشغل بـ<bdi>Hb</bdi> أو <bdi>platelets</bdi> الخفيفين.",
    "comparison": None,
    "labs": [["Hb", "90 g/L", "130-170 g/L (M) / 120-160 g/L (F)"], ["Platelets", "90 x10^9/L", "150-400 x10^9/L"], ["INR", "2", "0.8-1.2"], ["Prothrombin time", "17 sec", "10-13 sec"]],
    "guideline_note": None,
},

"AS-2022": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "يرقان تدريجي مع مرارة متمددة وغير مؤلمة (<bdi>Courvoisier sign</bdi>)، والسؤال يبي التشخيص الأكثر احتمالاً.",
    "clues": [
        ("progressive yellowish discoloration", "يرقان يتصاعد يناسب انسداد خبيث"),
        ("weight loss", "فقدان وزن يدعم سبب خبيث"),
        ("palpable, distended non-tender gallbladder", "علامة <bdi>Courvoisier</bdi> توجه نحو انسداد بعيد عن القناة المرارية"),
    ],
    "why_correct": [
        "يرقان تدريجي مع ألم خفيف وبول غامق وفقدان وزن على مدى 3 أشهر عند رجل بعمر 65 يوجه نحو انسداد خبيث.",
        "مرارة متمددة وغير مؤلمة (<bdi>Courvoisier sign</bdi>) تعني الانسداد بعد مفرق <bdi>cystic duct</bdi>، وهذا نطاق <bdi>periampullary tumour</bdi> (رأس البنكرياس، الحليمة، أو القناة الصفراوية البعيدة).",
    ],
    "when_changes": [
        "لو كانت المرارة منكمشة مع توسع داخل الكبد فقط، التشخيص يتحول إلى <bdi>Klatskin tumour</bdi>.",
        "لو كان اليرقان متقطع مع ألم مغصي، التشخيص الأقرب يصير <bdi>common bile duct stone</bdi>.",
    ],
    "rule": "<bdi>Courvoisier sign</bdi> (مرارة متمددة وغير مؤلمة مع يرقان) يوجه نحو انسداد خبيث بعيد، غالبًا <bdi>periampullary</bdi>، ويستبعد الحصيات.",
    "comparison": None,
    "labs": [["ALP", "320 IU/L", "39-117 IU/L"], ["Direct bilirubin", "77 mol/L", "1.5-6.5 mol/L"], ["Total bilirubin", "88 mol/L", "3.5-16.5 mol/L"]],
    "guideline_note": None,
},

"AS-2023": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "يرقان انسدادي شديد مع مرارة متمددة جدًا وتوسع بكل القنوات الصفراوية، والسؤال يبي التشخيص الأكثر احتمالاً.",
    "clues": [
        ("pale stool", "براز فاتح يدعم انسداد صفراوي كامل"),
        ("palpable distended gallbladder", "علامة <bdi>Courvoisier</bdi> تدعم انسداد بعيد"),
        ("Dilated intra and extrahepatic bile ducts with hugely distended gallbladder", "توسع القنوات الداخلية والخارجية معًا يحدد مستوى الانسداد عند <bdi>distal CBD</bdi>"),
    ],
    "why_correct": [
        "يرقان مع بول غامق وبراز فاتح وارتفاع كبير بـ<bdi>ALP</bdi> و<bdi>direct bilirubin</bdi> يعني يرقان انسدادي.",
        "مرارة متمددة (<bdi>Courvoisier</bdi>) وتوسع القنوات الداخلية والخارجية معًا بالتصوير يحدد الانسداد عند <bdi>distal CBD</bdi>، وهو النطاق الكلاسيكي لسرطان رأس البنكرياس عند رجل مسن.",
    ],
    "when_changes": [
        "لو التوسع داخل الكبد فقط مع مرارة منكمشة، التشخيص يتحول إلى <bdi>Klatskin tumour</bdi>.",
        "لو كانت المرارة ملتهبة متقلصة مع حصيات، نفكر بـ<bdi>Mirizzi's syndrome</bdi>.",
    ],
    "rule": "توسع القنوات داخل وخارج الكبد مع مرارة متمددة جدًا = انسداد <bdi>distal CBD</bdi>، غالبًا سرطان رأس البنكرياس.",
    "comparison": None,
    "labs": [["ALP", "421 IU/L", "39-117 IU/L"], ["Direct bilirubin", "122.3 mol/L", "1.5-6.5 mol/L"], ["Total bilirubin", "134.5 umol/L", "3.5-16.5 umol/L"]],
    "guideline_note": None,
},

"AS-2024": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نفس سيناريو AS-2023 تمامًا (سؤال مكرر): يرقان انسدادي شديد مع مرارة متمددة جدًا وتوسع بكل القنوات الصفراوية.",
    "clues": [
        ("pale stool", "براز فاتح يدعم انسداد صفراوي كامل"),
        ("palpable distended gallbladder", "علامة <bdi>Courvoisier</bdi> تدعم انسداد بعيد"),
        ("Dilated intra and extrahepatic bile ducts with hugely distended gallbladder", "توسع القنوات الداخلية والخارجية معًا يحدد مستوى الانسداد عند <bdi>distal CBD</bdi>"),
    ],
    "why_correct": [
        "يرقان مع بول غامق وبراز فاتح وارتفاع كبير بـ<bdi>ALP</bdi> و<bdi>direct bilirubin</bdi> يعني يرقان انسدادي.",
        "مرارة متمددة (<bdi>Courvoisier</bdi>) وتوسع القنوات الداخلية والخارجية معًا بالتصوير يحدد الانسداد عند <bdi>distal CBD</bdi>، وهو النطاق الكلاسيكي لسرطان رأس البنكرياس عند رجل مسن.",
    ],
    "when_changes": [
        "لو التوسع داخل الكبد فقط مع مرارة منكمشة، التشخيص يتحول إلى <bdi>Klatskin tumour</bdi>.",
        "لو كانت المرارة ملتهبة متقلصة مع حصيات، نفكر بـ<bdi>Mirizzi's syndrome</bdi>.",
    ],
    "rule": "توسع القنوات داخل وخارج الكبد مع مرارة متمددة جدًا = انسداد <bdi>distal CBD</bdi>، غالبًا سرطان رأس البنكرياس.",
    "comparison": None,
    "labs": [["ALP", "421 IU/L", "39-117 IU/L"], ["Direct bilirubin", "122.3 mol/L", "1.5-6.5 mol/L"], ["Total bilirubin", "134.5 umol/L", "3.5-16.5 umol/L"]],
    "guideline_note": "هذا السؤال مكرر لـ<bdi>AS-2023</bdi> بنفس السيناريو تمامًا حسب ملاحظة المصدر.",
},

"AS-2025": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "يرقان انسدادي تدريجي مع توسع داخل الكبد فقط ومرارة منكمشة، والسؤال يبي مستوى الانسداد.",
    "clues": [
        ("progressive yellowish discoloration", "يرقان تدريجي يناسب انسداد خبيث"),
        ("Dilated intrahepatic biliary tree", "توسع داخل الكبد فقط يحدد مستوى الانسداد عند الـ<bdi>hilum</bdi>"),
        ("collapsed gallbladder", "مرارة منكمشة تستبعد انسداد <bdi>distal</bdi>"),
    ],
    "why_correct": [
        "يرقان انسدادي تدريجي (بول غامق، <bdi>ALP</bdi> و<bdi>bilirubin</bdi> مرتفعين) مع تصوير يظهر توسع داخل الكبد فقط ومرارة منكمشة يحدد الانسداد عند ملتقى القنوات الكبدية، فوق القناة المرارية.",
        "المرارة فاضية لأن الصفراء لا تقدر توصل إليها، وهذا يناسب <bdi>Klatskin tumour</bdi> (<bdi>hilar cholangiocarcinoma</bdi>).",
    ],
    "when_changes": [
        "لو كانت المرارة ملتهبة مع حصيات، نفكر بـ<bdi>Mirizzi's syndrome</bdi>.",
        "لو كانت المرارة متمددة مع توسع بكل القنوات، التشخيص يتحول إلى <bdi>periampullary tumour</bdi>.",
    ],
    "rule": "مرارة منكمشة مع توسع داخل الكبد فقط = انسداد فوق القناة المرارية (<bdi>Klatskin</bdi>)؛ لا تختار <bdi>periampullary</bdi> فقط لأن المريض مسن ومصفّر.",
    "comparison": None,
    "labs": [["ALP", "312 IU/L", "39-117 IU/L"], ["Direct bilirubin", "87 mol/L", "1.5-6.5 mol/L"], ["Total bilirubin", "97 mol/L", "3.5-16.5 mol/L"]],
    "guideline_note": None,
},

"AS-2026": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نزيف حوضي لا يُسيطر عليه أثناء <bdi>low anterior resection</bdi>، والسؤال يبي الخطوة الأولى الصحيحة.",
    "clues": [
        ("colorectal surgeon", "فريق جراحي متخصص بعملية حوضية"),
        ("low anterior resection", "عملية بمجال عميق وضيق قريب من الضفيرة الوريدية العجزية"),
        ("pelvic bleeding", "نزيف حوضي غالبًا من الضفيرة الوريدية، صعب السيطرة عليه موضعيًا"),
    ],
    "why_correct": [
        "نزيف حوضي غير مسيطر عليه أثناء <bdi>LAR</bdi> غالبًا من الضفيرة الوريدية العجزية بمجال عميق وضيق.",
        "أول خطوة هي حزم الحوض بشكل كثيف (<bdi>heavily pack the pelvis</bdi>) للضغط المباشر، وهذا يضبط النزيف الوريدي ويعطي وقت للتخدير للإنعاش وللفريق لإعادة التنظيم.",
    ],
    "when_changes": [
        "لو فشل الحزم وانخفض الضغط بشدة، الخطوة التالية تصير <bdi>supra celiac aortic clamp</bdi>.",
        "لو النزيف شرياني مستمر بعد سيطرة مؤقتة، نفكر بـ<bdi>on-table angiogram</bdi> مع إنعاش كافٍ.",
    ],
    "rule": "نزيف حوضي أثناء جراحة = حزم أولاً بالضغط المباشر، والأدوات الأخرى (<bdi>clamp</bdi>, <bdi>angiogram</bdi>) تجي فقط لو فشل الحزم.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2027": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "نفس سيناريو النزيف الحوضي لكن بعد الحزم والمريض استمر بانخفاض الضغط، والسؤال يبي الخطوة التالية عند فشل الحزم.",
    "clues": [
        ("low anterior resection", "نفس العملية الحوضية العميقة"),
        ("pelvis was packed", "الحزم تم فعلًا، فالسؤال عن الخطوة التالية بعد فشله الجزئي"),
        ("patient dropped his pressure again", "انخفاض ضغط متكرر يعني نزيف مستمر يهدد الحياة"),
    ],
    "why_correct": [
        "الحوض محزوم فعلًا، ومع ذلك انخفض الضغط مرة أخرى إلى «<bdi>60/40</bdi>»، يعني نزيف مستمر يهدد الحياة.",
        "<bdi>Supraceliac aortic clamp</bdi> يُطبق بسرعة عند الفتحة الحجابية بعيدًا عن المجال الحوضي الملوث بالدم، ويسيطر على كل الدخل الأبهري بينما يستمر الإنعاش.",
    ],
    "when_changes": [
        "لو كان المريض مستقر بعد الحزم بدون انخفاض ضغط متكرر، نكتفي بالحزم والمراقبة.",
        "لو كان الوقت متاح لتصوير الأوعية، نفكر بـ<bdi>on-table angiogram</bdi> مع <bdi>embolization</bdi>.",
    ],
    "rule": "نزيف حوضي أثناء العملية: حزم أولاً، وإذا استمر انخفاض الضغط بعد الحزم، الخطوة التالية هي <bdi>supraceliac aortic clamp</bdi> لا إزالة الحزم.",
    "comparison": None,
    "labs": [["Blood pressure", "60/40 mmHg", "90-120/60-80 mmHg"]],
    "guideline_note": None,
},

"AS-2028": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "كتلة ثدي صلبة مع تاريخ عائلي وعلامات مشبوهة عند امرأة فوق 30، والسؤال يبي الخطوة التالية بالتقييم الثلاثي.",
    "clues": [
        ("family history of breast cancer", "عامل خطورة يرفع الشك بالخباثة"),
        ("hard lump", "صلابة الكتلة تزيد الشك"),
        ("ill-defined edge and skin tethering", "علامات مشبوهة تدعم التقييم الكامل، لكن لا تغيّر تسلسل الفحوصات"),
    ],
    "why_correct": [
        "امرأة بعمر 37 بتاريخ عائلي وكتلة صلبة بحواف غير محددة وتشبث جلدي تحتاج <bdi>triple assessment</bdi>، وبعمر فوق 30 الخطوة التالية هي التصوير.",
        "<bdi>Bilateral mammography</bdi> (مع أو بدون <bdi>US</bdi>) تأتي قبل الخزعة لتوصيف الكتلة وفحص الثدي الآخر.",
    ],
    "when_changes": [
        "لو عمرها أقل من 30، أول تصوير يصير <bdi>ultrasound</bdi> بدل <bdi>mammography</bdi>.",
        "بعد التصوير لو ظهرت نتيجة مشبوهة (<bdi>BI-RADS 4/5</bdi>)، الخطوة التالية تصير <bdi>core needle biopsy</bdi>.",
    ],
    "rule": "علامات خباثة بالفحص السريري لا تقفز بنا فورًا للخزعة؛ بعمر 30 فأكثر، التصوير (<bdi>mammography</bdi>) هو الخطوة الأولى بالتقييم الثلاثي.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2029": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "جرح رقبي مفتوح بعد حادث مع انخفاض تشبع الأكسجين، والمريض لسه واعٍ، والسؤال يبي الخطوة التالية الأولى (<bdi>airway</bdi> أولاً).",
    "clues": [
        ("open wound to the anterior surface of the neck", "جرح رقبي يهدد مجرى الهواء لاحقًا بسبب تورم أو ورم دموي"),
        ("Oxygen saturation 87%", "أقل من 88% هو مؤشر مباشر لـ<bdi>definitive airway</bdi>"),
    ],
    "why_correct": [
        "<bdi>Airway</bdi> أولاً حسب تسلسل <bdi>ABCDE</bdi>. المريض معه جرح رقبي أمامي مفتوح بنسيج ميت، وتسرع تنفس (<bdi>RR 28</bdi>) ونقص أكسجين عند <bdi>SpO2 87%</bdi>، وهذا تحت عتبة 88% المؤشرة لـ<bdi>definitive airway</bdi>.",
        "وهو لسه واعٍ، فالتنبيب الآن (<bdi>endotracheal intubation</bdi>) يؤمن مجرى الهواء قبل أن يزيد التورم أو الورم الدموي ويجعل التنبيب مستحيل.",
    ],
    "when_changes": [
        "لو كان التشبع طبيعي والجرح لا يهدد المجرى، قناع أكسجين يكفي مؤقتًا.",
        "لو فشل التنبيب أو كان مستحيل بسبب تشوه شديد، الخطوة التالية تصير <bdi>cricothyroidotomy</bdi>.",
    ],
    "rule": "وعي المريض لا يعني أمان مجرى الهواء؛ نقص أكسجين مع جرح رقبي يهدد المجرى = تنبيب فورًا.",
    "comparison": None,
    "labs": [["Blood pressure", "100/60 mmHg", "90-120/60-80 mmHg"], ["Heart rate", "104/min", "60-100/min"], ["Respiratory rate", "28/min", "12-20/min"], ["Oxygen saturation", "87%", "≥95%"]],
    "guideline_note": None,
},

"AS-2030": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "حادث سرعة عالية مع مريض واعٍ ومستقر وصورة صدر طبيعية، والسؤال يبي التصوير المناسب لتقييم البطن.",
    "clues": [
        ("conscious, and alert", "علامة على استقرار الدورة الدموية"),
        ("X-ray: Normal", "يستبعد مضاعفات صدرية فورية، لكن لا يستبعد إصابة بطنية"),
    ],
    "why_correct": [
        "رضح شديد بسرعة عالية (130 <bdi>km/h</bdi>) يستدعي تصوير البطن، والمريض «<bdi>conscious and alert</bdi>» يعني <bdi>stable</bdi> مع صورة صدر طبيعية.",
        "مريض <bdi>blunt trauma</bdi> <bdi>stable</bdi> يذهب لـ<bdi>CT abdomen</bdi> (بصبغة) الذي يحدد درجة إصابة الأعضاء الصلبة ويكشف إصابات الأحشاء المجوفة والخلف صفاقية.",
    ],
    "when_changes": [
        "لو كان المريض <bdi>unstable</bdi>، الخطوة الأولى تصير <bdi>FAST US</bdi> بجانب السرير.",
        "لو ظهر التهاب بريتوني أو <bdi>FAST</bdi> إيجابي بمريض <bdi>unstable</bdi>، الخطوة تصير <bdi>exploratory laparotomy</bdi>.",
    ],
    "rule": "الاستقرار يحدد التصوير: <bdi>stable</bdi> يروح لـ<bdi>CT</bdi>، <bdi>unstable</bdi> يحتاج <bdi>FAST</bdi> سريع بجانب السرير.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2034": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "طفلة بشك <bdi>appendicitis</bdi> بعلامات غير نموذجية وفحوصات طبيعية، والسؤال يبي أفضل طريقة لعدم تفويت التشخيص.",
    "clues": [
        ("no fever no anorexia and no rebound tenderness", "صورة منخفضة الاحتمالية لـ<bdi>appendicitis</bdi> حاليًا"),
        ("WBC 9", "عدد كريات دم بيضاء طبيعي لا يستبعد التهاب مبكر"),
    ],
    "why_correct": [
        "ألم بالربع السفلي الأيمن فقط، بدون حمى، أنوركسيا، أو ارتداد، مع <bdi>WBC</bdi> طبيعي (9)، يعطي صورة منخفضة الاحتمالية لـ<bdi>appendicitis</bdi>.",
        "أأمن طريقة لعدم تفويت تطور الحالة هي الملاحظة النشطة: إدخال وفحص متكرر وتحاليل متكررة خلال 6-12 ساعة، حتى تظهر العلامات لو كانت موجودة بدون تعريض الطفلة لإشعاع أو جراحة غير ضرورية.",
    ],
    "when_changes": [
        "لو الصورة غير واضحة بطفلة أو حامل، الخطوة الأولى تصير <bdi>ultrasound</bdi>.",
        "لو ظهرت العلامات الكلاسيكية مع ارتداد وزيادة <bdi>WBC</bdi>، الجواب يتحول إلى استئصال الزائدة مباشرة.",
    ],
    "rule": "احتمالية منخفضة لـ<bdi>appendicitis</bdi> عند طفل = ملاحظة نشطة بالإدخال وفحص متكرر، لا تصوير مؤشّع أو خروج مباشر.",
    "comparison": None,
    "labs": [["WBC", "9 x10^9/L", "4-11 x10^9/L"]],
    "guideline_note": None,
},

}

WHY_WRONG = {

"AS-1914": {
    "A": "<bdi>Nephrectomy</bdi> خطوة جذرية تُحفظ لحالات <bdi>unstable</bdi> لا تستجيب للإنعاش، مو لمريض <bdi>stable</bdi>.",
    "B": "<bdi>Angioembolization</bdi> يُستخدم مع <bdi>active arterial blush</bdi> في مريض <bdi>stable</bdi>؛ السيناريو ما ذكر نزيف شرياني فعال واضح.",
    "D": "لا يوجد خيار كافٍ بهذا الحرف ليُعتبر إجابة.",
},

"AS-1915": {
    "B": "<bdi>Core biopsy</bdi> يأتي بعد التصوير لا قبله، خصوصًا مع كتلة <bdi>soft and movable</bdi> تقل شكوكها.",
    "C": "<bdi>Reassurance</bdi> المباشر بدون تصوير غير كافٍ لكتلة جديدة بالإبط.",
    "D": "عدم تذكر الخيار لا يجعله إجابة صحيحة.",
},

"AS-1916": {
    "A": "<bdi>Mammogram</bdi> هو الخيار الأول بغير الحامل فوق 30، لكن بالحمل نفضّل <bdi>ultrasound</bdi> لتجنب الإشعاع.",
    "C": "<bdi>FNA</bdi> يأتي بعد التصوير، ما يُستخدم كخطوة أولى قبل تحديد طبيعة الكتلة.",
    "D": "تأجيل التقييم لبعد الولادة يحمل خطر تفويت <bdi>pregnancy-associated breast cancer</bdi>.",
},

"AS-1917": {
    "A": "<bdi>Fine needle aspiration</bdi> يأتي بعد التصوير، لا قبله.",
    "C": "<bdi>Diagnostic mammography</bdi> يكون أول خيار بغير الحامل فوق 30، لكن بالحمل <bdi>ultrasound</bdi> أول.",
    "D": "كتلة <bdi>enlarging</bdi> بالحمل لا تُؤجل لبعد الولادة لخطر تفويت <bdi>malignancy</bdi>.",
},

"AS-1918": {
    "B": "<bdi>Adhesions</bdi> تحتاج تاريخ عملية بطنية سابقة أو التهاب بريتوني؛ هذا المريض لا تاريخ له.",
    "C": "<bdi>Meckel's diverticulum</bdi> أقل شيوعًا من <bdi>hernia</bdi> كسبب لـ<bdi>SBO</bdi> وأكثر شيوعًا بالأطفال الصغار.",
    "D": "لم يُذكر هذا الخيار كمحتمل من المصدر أصلًا.",
},

"AS-1923": {
    "A": "<bdi>Tracheostomy</bdi> ليست الخطوة الفورية لتأمين <bdi>airway</bdi> في حالة إسعافية حادة.",
    "B": "<bdi>Cricothyroidotomy</bdi> تُحفظ لحالات كسر وجه يمنع <bdi>intubation</bdi> أو فشل محاولته.",
    "D": "<bdi>Nasopharyngeal airway</bdi> مجرد أداة مساعدة، ليست <bdi>definitive airway</bdi>.",
},

"AS-1924": {
    "A": "<bdi>Orotracheal intubation</bdi> فشلت فعليًا عدة مرات، فتكرارها يضيع وقت ويزيد الرضح.",
    "B": "<bdi>Surgical cricothyrotomy</bdi> يُتجنّب تحت عمر 12 سنة تقريبًا لخطر <bdi>subglottic stenosis</bdi>.",
    "D": "<bdi>Laryngeal airway</bdi> حل مؤقت للأكسجين فقط، ليس <bdi>definitive airway</bdi>، ويضعف أداءه بعد رضح وجهي شديد.",
},

"AS-1926": {
    "A": "<bdi>Observation</bdi> مناسبة لـ<bdi>hydrocele</bdi> أو <bdi>umbilical hernia</bdi>، مو لـ<bdi>inguinal hernia</bdi> المعرضة لـ<bdi>incarceration</bdi>.",
    "C": "<bdi>Mesh repair</bdi> للبالغين حيث الجدار الخلفي ضعيف؛ الأطفال يحتاجون فقط ربط الكيس (<bdi>herniotomy</bdi>).",
    "D": "الانتظار لسنوات ينطبق على <bdi>umbilical hernia</bdi> لا <bdi>inguinal hernia</bdi> التي تُصلح بسرعة.",
},

"AS-1949": {
    "A": "<bdi>Mild</bdi> يحتاج <bdi>GCS</bdi> من 13 إلى 15؛ هذا المريض أقل من ذلك.",
    "C": "<bdi>Severe</bdi> يكون عند <bdi>GCS</bdi> 8 أو أقل؛ درجة 12 أعلى من ذلك بكثير.",
    "D": "<bdi>Minimal</bdi> ليست فئة معيارية ضمن تصنيف <bdi>GCS</bdi> المعتاد.",
},

"AS-1954": {
    "B": "<bdi>Nipple biopsy</bdi> يُحفظ لآفة مشبوهة مثل <bdi>Paget disease</bdi>، مو إفراز حميد مع <bdi>BI-RADS 2</bdi>.",
    "C": "<bdi>CT pelvic</bdi> لا دور له بتقييم إفراز الحلمة أصلًا.",
},

"AS-1955": {
    "B": "<bdi>Conservative management</bdi> تناسب <bdi>polyp</bdi> بدون أعراض فقط؛ هذه المريضة <bdi>symptomatic</bdi>.",
    "C": "<bdi>Surveillance imaging</bdi> يناسب <bdi>polyp</bdi> بدون أعراض؛ الأعراض تُخرجها من مسار المراقبة.",
    "D": "<bdi>HIDA scan</bdi> يفيد عند عدم وجود سبب تركيبي واضح بالتصوير؛ هنا السبب التركيبي موجود والأعراض تكفي لتقرير الجراحة.",
},

"AS-1965": {
    "B": "<bdi>Ligation</bdi> الانتقائي للأوعية الصغيرة لا يكفي للسيطرة على نزيف منتشر من إصابات متعددة.",
    "C": "<bdi>Ligation</bdi> الشريان الكبدي الأيمن قد يسبب نقص تروية ولا يسيطر على نزيف وريدي أو منتشر.",
    "D": "لا يوجد خيار كافٍ بهذا الحرف ليُعتبر إجابة.",
},

"AS-1966": {
    "A": "<bdi>Right hepatectomy</bdi> عملية طويلة بفقد دم كبير لا يتحملها مريض <bdi>unstable</bdi> ومصاب بـ<bdi>coagulopathy</bdi>.",
    "C": "<bdi>Right hepatic artery ligation</bdi> لا يسيطر على نزيف وريدي أو منتشر ويحمل خطر نقص تروية الفص.",
    "D": "<bdi>Individual ligation</bdi> يناسب جرح واحد محدد بمريض <bdi>stable</bdi> يقبل إصلاح نهائي، لا إصابات متعددة بمريض <bdi>unstable</bdi>.",
},

"AS-1973": {
    "A": "200 <bdi>ml/hr</bdi> لمدة 24 ساعة يعطي فقط حوالي 4.8 <bdi>L</bdi>، أقل من نصف الكمية المطلوبة (10 <bdi>L</bdi>).",
    "B": "<bdi>Normal saline</bdi> ليس المحلول المفضل بـ<bdi>Parkland</bdi>، والكمية المحسوبة هنا قليلة جدًا لحرق 36%.",
    "D": "إجمالي 5 <bdi>L</bdi> يطابق نسبة 18% فقط، أي حساب كل طرف سفلي كـ9% بدل 18% — خطأ شائع بـ<bdi>rule of nines</bdi>.",
},

"AS-1976": {
    "A": "<bdi>Pancreatic cancer</bdi> يظهر عادة بمرضى أكبر بالسن مع فقدان وزن، وبدون قصة <bdi>pancreatitis</bdi> حادة واضحة.",
},

}

HIGHLIGHT_TERMS = {
"AS-1914": ["blunt abdominal trauma", "Extravasation around the left kidney"],
"AS-1915": ["axillary mass 3x3", "soft and movable"],
"AS-1916": ["Pregnant", "28 weeks", "breast mass"],
"AS-1917": ["28-week pregnant", "enlarging right breast mass", "firm movable"],
"AS-1918": ["bowel obstruction", "no medical or surgical history"],
"AS-1923": ["mouth is full og blood"],
"AS-1924": ["child (10 y.o)", "several hits on his face", "failure"],
"AS-1926": ["newborn", "reducible inguinal hernia"],
"AS-1949": ["confused", "opens his eyes to sound", "localizes pain"],
"AS-1954": ["Bilateral green discharge", "dilated ducts", "BI RADS 2"],
"AS-1955": ["0.8 polyp", "bothered by sx"],
"AS-1965": ["multiple liver injuries"],
"AS-1966": ["unstable", "mul7ple liver lacera7ons"],
"AS-1973": ["2nd degree burn to his both lower limbs", "Weight 70 kg", "Parkland formula"],
"AS-1976": ["recovers from an attack of severe pancreatitis", "cyst form in lesser sac"],
}
