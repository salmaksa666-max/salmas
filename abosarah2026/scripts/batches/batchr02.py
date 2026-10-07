# -*- coding: utf-8 -*-
# Batch r02: 141 questions.

EXPLANATIONS = {
"AS-2278": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "السؤال يختبر أي <bdi>order</bdi> يصير يتاخذ <bdi>verbally</bdi> بالتلفون، والفكرة إن <bdi>الأدوية</bdi> بالذات الخطيرة لازم تكتب مباشرة من <bdi>prescriber</bdi>.",
    "clues": [
        ("prescribe over the phone", "يبحث عن أكثر <bdi>order</bdi> مسموح يُعطى <bdi>verbally</bdi> (بالتلفون)"),
    ],
    "why_correct": [
        "<bdi>nutrition/feeding order</bdi> هو <bdi>order</bdi> غير دوائي وقليل الخطورة نسبيًا، فهو الأقرب يُقبل كـ<bdi>verbal order</bdi> بالتلفون.",
        "بالمقابل <bdi>drug prescriptions</bdi> المفروض تكتب أو تدخل بالنظام من نفس <bdi>prescriber</bdi>، خصوصًا الأدوية عالية الخطورة.",
    ],
    "when_changes": [
        "لو السؤال يبي دواء منخفض الخطورة فعلاً مسموح بالتلفون أحيانًا (مثل <bdi>paracetamol</bdi>)، فممكن يصير هو الجواب إذا ما كان فيه خيار <bdi>non-drug order</bdi> أقوى.",
        "لو الخيار كان دواء <bdi>chemotherapy</bdi>، فهذا دايمًا ممنوع تمامًا بالتلفون بدون أي استثناء.",
    ],
    "rule": "القاعدة: <bdi>verbal/phone orders</bdi> تتجنب خصوصًا بالأدوية عالية الخطورة، وممنوعة تمامًا مع <bdi>chemotherapy</bdi>؛ <bdi>non-drug orders</bdi> مثل <bdi>nutrition/feeding</bdi> هي الأقرب للقبول.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2296": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "السؤال يختبر مفهوم <bdi>safe prescribing</bdi>: الطبيب يعرف إن <bdi>warfarin</bdi> خطير، بس ما كان يعرف إن المريضة <bdi>pregnant</bdi>، يعني المشكلة بـ<bdi>patient-specific</bdi> لا بمعرفة الدواء.",
    "clues": [
        ("warfarin", "<bdi>teratogenic drug</bdi> معروف خطره، فالمشكلة مو بمعرفة الدواء"),
        ("10 weeks pregnant", "اكتشاف الحمل بعد إعطاء الدواء، يعني فشل بفحص حالة المريضة قبل الوصفة"),
    ],
    "why_correct": [
        "الخطأ هنا إن الطبيب ما سأل عن حالة <bdi>pregnancy</bdi> قبل إعطاء <bdi>teratogen</bdi>، فالحل يصير <bdi>tailoring prescription to the individual patient</bdi>: فحص العمر، الجنس، حالة <bdi>reproductive</bdi>، <bdi>comorbidities</bdi> و<bdi>allergies</bdi> لكل مريضة قبل الوصفة.",
        "يعني لازم يسأل عن <bdi>LMP</bdi> وإمكانية الحمل عند أي امرأة بعمر الإنجاب قبل إعطاء دواء خطير بالحمل.",
    ],
    "when_changes": [
        "لو السؤال يبي السؤال المباشر عن سبب الخطأ نفسه، يصير الجواب عدم معرفة حالة الحمل، مو معرفة الدواء.",
        "لو الدواء نفسه كان غير معروف خطره على الطبيب، يصير الجواب معرفة <bdi>high-risk medications</bdi>.",
    ],
    "rule": "في أسئلة منع تكرار خطأ الوصفة، لازم تحدد وين كانت الفجوة فعليًا: معرفة الدواء ولا معرفة المريضة؛ هنا الفجوة بمعرفة المريضة فالجواب <bdi>tailoring to the individual</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2301": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "السؤال عن قاعدة <bdi>DNR</bdi> بالسعودية لما المريض يتحول من مستشفى ثاني، كم مدة يبقى الـ<bdi>DNR</bdi> القديم ساري.",
    "clues": [
        ("DNR from other hospital", "يسأل عن صلاحية <bdi>DNR order</bdi> صادر من مستشفى آخر بعد التحويل"),
    ],
    "why_correct": [
        "حسب إرشادات <bdi>DNR</bdi> السعودية، لما المريض يتحول من مستشفى آخر (محلي أو دولي)، الـ<bdi>DNR order</bdi> الموقّع من المستشفى المُحوِّل يبقى <bdi>valid</bdi> لمدة <bdi>24 hours</bdi> فقط.",
        "خلال هذي الفترة، الفريق المستقبل لازم يعيد تقييم الحالة ويصدر <bdi>DNR order</bdi> جديد خاص به إذا كان مناسب.",
    ],
    "when_changes": [
        "لو السؤال يبي مين يتخذ قرار الـ<bdi>DNR</bdi> أصلًا، الجواب يصير الطبيب (قرار <bdi>medical</bdi>) مو العائلة.",
        "لو السؤال عن مدة مختلفة (مثل 6 أشهر) فهذا خطأ دايمًا، المدة الصحيحة 24 ساعة بس.",
    ],
    "rule": "<bdi>DNR</bdi> من مستشفى آخر = <bdi>valid</bdi> لمدة 24 ساعة فقط، وبعدها الفريق المستقبل يعيد التقييم ويصدر أمر جديد حسب سياسته.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2302": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نفس فكرة <bdi>DNR</bdi> transfer، بس بصيغة سؤال مباشرة عن المدة الزمنية الصحيحة.",
    "clues": [
        ("transferred to another hospital", "يحدد إن السؤال عن صلاحية <bdi>DNR</bdi> بعد التحويل بين مستشفيات"),
    ],
    "why_correct": [
        "إرشادات <bdi>DNR</bdi> السعودية تنص إن أمر <bdi>DNR</bdi> الموقّع من مستشفى آخر (محلي أو دولي) يبقى <bdi>valid</bdi> لمدة <bdi>24 hours</bdi> فقط عند التحويل.",
        "هذا يحمي قرار المريض خلال فترة الانتقال، لين الفريق المستقبل يعيد التقييم ويصدر أمره الخاص.",
    ],
    "when_changes": [
        "لو ما فيه وقت محدد بالخيارات وكان فيه خيار \"valid\" بدون حد زمني، يبقى الصحيح دايمًا الخيار بـ24 ساعة لأنه الأدق.",
        "لو السؤال يسأل عن مين يراجع الأمر خلال هذي الساعات، الجواب الفريق الطبي المستقبل.",
    ],
    "rule": "احفظ الرقم: <bdi>DNR</bdi> من مستشفى آخر = <bdi>valid for 24 hours</bdi> بالضبط، مو 6 أشهر ومو \"<bdi>invalid</bdi>\" ومو \"<bdi>valid</bdi>\" بدون حد زمني.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2303": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "السؤال عن مين مسؤول عن التحقق من <bdi>DNR status</bdi> عند استقبال مريض محوّل، مو عن مدة الصلاحية.",
    "clues": [
        ("muscular dystrophy", "خلفية مرضية، لكن مو جوهر السؤال"),
        ("transferred from one hospital to a tertiary hospital", "تحويل بين مستشفيات، سياق انتقال <bdi>care</bdi>"),
        ("without knowing about a Do Not Resuscitate (DNR) order", "فشل بالتواصل حول حالة <bdi>code status</bdi> عند الاستقبال"),
    ],
    "why_correct": [
        "التحقق من وجود <bdi>DNR order</bdi> هو مسؤولية <bdi>clinical team</bdi> نفسها، خصوصًا وقت <bdi>handover</bdi> والتحويل بين المستشفيات.",
        "الفريق المُحوِّل لازم ينقل حالة <bdi>code status</bdi> مع ملف المريض، وعضو من الفريق المستقبل لازم يتأكد منها عند الوصول، والمسؤولية ما تنتقل أبدًا للعائلة.",
    ],
    "when_changes": [
        "لو السؤال يبي مدة صلاحية الـ<bdi>DNR</bdi> نفسها، الجواب يصير 24 ساعة.",
        "لو السؤال يبي مين يوافق على قرار <bdi>DNR</bdi> أصلًا، الجواب الطبيب المسؤول، مو أي عضو من الفريق.",
    ],
    "rule": "أي خيار يحوّل مسؤولية التحقق من <bdi>safety item</bdi> (مثل <bdi>DNR</bdi> أو <bdi>consent</bdi> أو <bdi>allergy</bdi>) للعائلة، غالبًا خيار غلط بأسئلة <bdi>ethics</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2339": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طلب <bdi>termination of pregnancy</bdi> لأسباب اجتماعية مع جنين <bdi>viable</bdi>، والسؤال عن تصرف الطبيب الصحيح قانونيًا وأخلاقيًا.",
    "clues": [
        ("termination of pregnancy due to social issues", "سبب الطلب غير مقبول طبيًا أو قانونيًا بالسعودية"),
        ("viable baby at 14 weeks", "الجنين <bdi>viable</bdi>، يرفع مستوى القيد القانوني على الإجهاض"),
    ],
    "why_correct": [
        "بالسعودية إنهاء حمل <bdi>viable</bdi> لأسباب اجتماعية غير مسموح؛ يسمح فقط بأسباب طبية معتمدة عبر الإجراءات الرسمية.",
        "الطبيب ما يسوي <bdi>abortion</bdi>، بس برضو ما يرفض ويسكت: يشرح لها إنه غير قانوني، ويعالج السبب الاجتماعي (مثل دعم اجتماعي)، ويقدم بدائل مسموحة واستمرار الرعاية.",
    ],
    "when_changes": [
        "لو السبب كان طبي معتمد (مثل خطر على حياة الأم)، يصير الجواب المتابعة بإجراءات الإجهاض القانونية المعتمدة.",
        "لو الحمل مو <bdi>viable</bdi> (بمراحل مبكرة جدًا)، القيود تختلف وتتبع لوائح منفصلة.",
    ],
    "rule": "طلب إجراء غير قانوني: الطبيب يرفض تنفيذه بس يستمر بالرعاية ويشرح ويقدم بدائل، وموافقة شخص ثاني (زوج/أب) ما تحوّل إجراء غير قانوني لقانوني.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2340": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "طبيب يحاول إقناع فتاة 16 سنة بعدم الإجهاض بسبب <bdi>personal belief</bdi>، والسؤال عن الموقف الصحيح للطبيب بالاستشارة.",
    "clues": [
        ("Dr is persuading her not to terminate due to personal belief", "الطبيب يفرض رأيه الشخصي على المريضة، وهذا المشكلة بالسؤال"),
    ],
    "why_correct": [
        "الطبيب لازم يقدم معلومة دقيقة ومتوازنة وغير متحيزة (<bdi>non-biased</bdi>)، وما يفرض معتقده الشخصي أو الديني على المريضة.",
        "لو عنده <bdi>conscientious objection</bdi>، يصرّح بها ويحوّل المريضة، مع إعطائها معلومة صحيحة عن الخيارات المتاحة قانونيًا.",
    ],
    "when_changes": [
        "لو الطبيب عنده اعتراض شخصي حقيقي، يصير الجواب الصحيح هو التصريح بالاعتراض والتحويل لطبيب آخر، مو الاستمرار بمحاولة الإقناع.",
        "لو السؤال عن سن المريضة وتأثيره على الموافقة، يصير النقاش عن <bdi>consent</bdi> والسرية لمريضة <bdi>minor</bdi>.",
    ],
    "rule": "الاستشارة بأمور حساسة (<bdi>abortion</bdi>) لازم تكون <bdi>non-directive</bdi> وغير متحيزة؛ رأي الطبيب الشخصي أو الديني مو سبب للتأثير على قرار المريضة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2341": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "<bdi>fetal distress</bdi> تستدعي <bdi>CS</bdi> بس الأم ترفض وتطلب رأي ثاني، والسؤال عن الخطوة التالية الصحيحة.",
    "clues": [
        ("fetal distress", "استعجال طبي، بس ما يبطل حق الأم بالقرار"),
        ("mother refuses the CS and requests a second opinion", "طلب معقول يجب احترامه وتلبيته بسرعة"),
    ],
    "why_correct": [
        "الأم المختصة (<bdi>competent</bdi>) عندها الحق تقبل أو ترفض <bdi>treatment</bdi> حتى لو كان لصالح الجنين، فـ<bdi>autonomy</bdi> المريضة ما تتجاوزها حالة الجنين.",
        "هي ما رفضت نهائيًا، بس طلبت رأي ثاني، وهذا طلب منطقي يجب احترامه وترتيبه بسرعة مع شرح خطورة التأخير والاستمرار بالمراقبة.",
    ],
    "when_changes": [
        "لو كانت الأم فاقدة الوعي أو غير قادرة على القرار، يطبق <bdi>emergency implied consent</bdi> ويتم التدخل فورًا.",
        "لو ظهرت علامات تشكك بقدرتها على فهم القرار (<bdi>capacity</bdi>)، يصير الخيار تقييم <bdi>capacity</bdi> أول شي.",
    ],
    "rule": "<bdi>fetal distress</bdi> تخلي الحالة عاجلة بس ما تبطل حق الأم المختصة بالموافقة أو الرفض؛ لا الزوج ولا أحد غيرها يقرر عنها.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2342": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "نفس فكرة السؤال السابق بصيغة مختلفة: <bdi>obstructed labor</bdi> و<bdi>fetal distress</bdi>، الأم ترفض وتطلب رأي ثاني.",
    "clues": [
        ("She Refuses The Procedure And Requests A Second Opinion", "طلب مشروع من مريضة مختصة، يجب احترامه"),
    ],
    "why_correct": [
        "حتى مع \"<bdi>obstructed labor</bdi> و<bdi>fetal distress</bdi>\"، المريضة المختصة اللي تم شرح الوضع لها لها الحق ترفض <bdi>emergency CS</bdi> وتطلب رأي ثاني.",
        "الصحيح احترام رفضها وترتيب الرأي الثاني فورًا، مع الاستمرار بشرح خطورة التأخير وتوثيق النقاش، مو تجاوز قرارها.",
    ],
    "when_changes": [
        "لو فقدت الوعي أثناء النقاش، ينتقل الوضع لـ<bdi>emergency implied consent</bdi> ويتم التدخل فورًا.",
        "لو الزوج هو من يرفض بس هي موافقة، رأيها هي اللي يُعتمد لأنها المريضة.",
    ],
    "rule": "الاستعجال الطبي يغيّر سرعة الشرح والتصرف، بس ما يغيّر مين يملك حق الموافقة؛ المريضة المختصة هي وحدها.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2343": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "مريضة مجدولة لـ<bdi>elective C-section</bdi> بس أصبحت متردّدة، والسؤال عن التصرف الصحيح بخصوص <bdi>consent</bdi>.",
    "clues": [
        ("elective C-section", "عملية غير عاجلة، فيه وقت للنقاش"),
        ("hesitant", "تردد المريضة يستدعي إيقاف والتحقق من <bdi>consent</bdi> الحالي"),
    ],
    "why_correct": [
        "<bdi>consent</bdi> عملية مستمرة مو توقيع لمرة واحدة، والمريضة تقدر تسحبه في أي وقت قبل الإجراء.",
        "لأنها \"<bdi>hesitant</bdi>\" عن عملية <bdi>elective</bdi>، الصحيح يوقف ويستكشف سبب ترددها، يعيد شرح الفوائد والمخاطر والبدائل، ويكمل العملية فقط بعد <bdi>informed consent</bdi> جديد ومتجدد.",
    ],
    "when_changes": [
        "لو كانت الحالة <bdi>emergency</bdi> وهي فاقدة الوعي، يطبق <bdi>implied consent</bdi> ويتم التدخل فورًا.",
        "لو السبب وراء ترددها مخاوف طبية محددة، يصير الحل معالجة تلك المخاوف بالتحديد ضمن الشرح الجديد.",
    ],
    "rule": "\"<bdi>she signed before</bdi>\" ما يكفي أبدًا؛ <bdi>consent</bdi> السابق ما يبقى صالح إذا عبّرت المريضة عن شك أو تردد، لازم <bdi>consent</bdi> جديد.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2402": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "حالة <bdi>urgent CS</bdi>، الزوج موافق بس المريضة ترفض، والسؤال عن الخيار الصحيح.",
    "clues": [
        ("husband agrees", "موافقة الزوج لا تملك أي قيمة قانونية هنا"),
        ("she refuses", "رفض المريضة المختصة هو الحاسم"),
    ],
    "why_correct": [
        "تم شرح المخاطر والفوائد لها وهي ترفض، وما فيه أي إشارة تدل إنها فاقدة <bdi>capacity</bdi>.",
        "قرار الأم المختصة يتغلب على موافقة الزوج، لأن الموافقة على جراحة بجسمها حق لها حصرًا حتى لو كانت الحالة عاجلة.",
    ],
    "when_changes": [
        "لو فيه علامات واضحة تدل على فقدان <bdi>capacity</bdi> (مثل تشويش بالتفكير أو عدم فهم الوضع)، يصير الخيار تقييم <bdi>capacity</bdi> نفسياً.",
        "لو كانت فاقدة الوعي فعلاً، يطبق <bdi>emergency implied consent</bdi> ويتم التدخل مباشرة.",
    ],
    "rule": "رفض المريضة المختصة <bdi>treatment</bdi> لازم يُحترم حتى مع موافقة الزوج وحتى بوجود استعجال طبي؛ لا ترفض الإحالة النفسية فقط لأنها رفضت علاج.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2403": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>ruptured ectopic pregnancy</bdi> مع <bdi>hypotension</bdi> وفقدان وعي، سؤال عن تطبيق <bdi>emergency consent exception</bdi>.",
    "clues": [
        ("ruptured ectopic pregnancy", "نزيف داخلي يهدد الحياة، يستدعي تدخل فوري"),
        ("hypotensive and unconscious", "المريضة فاقدة الوعي، فما تقدر تعطي <bdi>consent</bdi> بنفسها"),
    ],
    "why_correct": [
        "<bdi>ruptured ectopic</bdi> مع <bdi>hypotension</bdi> هو نزيف مهدد للحياة ومؤشر واضح للجراحة الفورية.",
        "بسبب إنها \"<bdi>unconscious</bdi>\" ما تقدر توافق، فينطبق <bdi>emergency exception</bdi> (<bdi>implied consent</bdi>): المتابعة بالجراحة المنقذة للحياة فورًا بدون انتظار موافقة أحد، مع توثيق الحالة.",
    ],
    "when_changes": [
        "لو كانت واعية ومختصة وترفض الجراحة، يُحترم رفضها حتى مع خطورة الحالة.",
        "لو كان فيه <bdi>advance refusal</bdi> موثق مسبقًا من المريضة بهذا الخصوص، هذا يغيّر القرار ويُحترم.",
    ],
    "rule": "فاقد الوعي + خطر مهدد للحياة = تصرف فورًا بدون انتظار أي موافقة؛ المريضة الواعية المختصة التي ترفض = يُحترم رفضها.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2428": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "سؤال عن تطبيق <bdi>four principles of research ethics</bdi> على مريضة قلقة من الوقوع بمجموعة <bdi>placebo</bdi> ضمن <bdi>clinical trial</bdi>.",
    "clues": [
        ("You Will Receive Standard Care", "التأكيد يعني إنها بتستفيد من علاج فعّال حتى لو كانت بمجموعة <bdi>placebo</bdi>"),
    ],
    "why_correct": [
        "قلقها إنها لو بمجموعة <bdi>placebo</bdi> بتفوت العلاج، وتأكيد الطبيب إنها \"بتاخذ <bdi>standard care</bdi>\" يعني التصميم يضمن إن كل مشارك يستفيد من علاج معتمد.",
        "هذا يُصنّف كـ<bdi>beneficence</bdi>: التصرف لصالح المريضة بضمان استفادتها من <bdi>standard care</bdi> وهي بالتجربة.",
    ],
    "when_changes": [
        "لو كان التركيز على حرية قبولها الاشتراك بالتجربة من الأساس، يصير المبدأ <bdi>autonomy</bdi>.",
        "لو كان السؤال عن طريقة اختيار المشاركين بعدالة، يصير المبدأ <bdi>justice</bdi>.",
    ],
    "rule": "عبارة \"<bdi>will receive</bdi> فائدة\" = <bdi>beneficence</bdi>؛ عبارة عن حرية القرار = <bdi>autonomy</bdi>؛ هذا الفرق هو مفتاح أغلب أسئلة <bdi>ethical principles</bdi>.",
    "comparison": {
        "headers": ["المبدأ", "الفكرة"],
        "rows": [
            ["<bdi>Beneficence</bdi>", "ضمان استفادة المريضة من <bdi>standard care</bdi>"],
            ["<bdi>Autonomy</bdi>", "حرية قرارها بالمشاركة بالتجربة"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},
"AS-2443": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "ممرضة فتحت ملف مريضة بدون صلاحية (صداقة عائلية) والمريضة قدّمت شكوى رسمية، والسؤال عن التصرف الصحيح.",
    "clues": [
        ("opened the patient's file", "دخول غير مخوّل (<bdi>unauthorised access</bdi>) للملف"),
        ("filed a complaint", "شكوى رسمية تستدعي تحقيق"),
    ],
    "why_correct": [
        "الممرضة ما لها دور بعلاج هذه المريضة وفتحت ملفها بدافع شخصي (\"<bdi>to check on her</bdi>\")، وهذا <bdi>unauthorised access</bdi> وخرق <bdi>confidentiality</bdi> حتى لو نيتها حسنة أو كانت صديقة للعائلة.",
        "لأن المريضة قدّمت شكوى رسمية، المستشفى لازم يسوي <bdi>investigation</bdi> ويطبق إجراء تأديبي أو قانوني حسب السياسة والقانون.",
    ],
    "when_changes": [
        "لو ما كان فيه شكوى رسمية وبس فيه خطر مستقبلي، يصير الحل تدريب الطاقم على <bdi>confidentiality</bdi> كإجراء وقائي.",
        "لو السؤال عن كيف تتصرف مباشرة بعد اكتشاف الخرق قبل الشكوى، يصير الخيار إبلاغ المريضة وتوثيق الحالة.",
    ],
    "rule": "خرق <bdi>confidentiality</bdi> ما يُقبل أبدًا لمجرد نية حسنة؛ وجود شكوى رسمية يستدعي <bdi>investigation</bdi> وإجراء تأديبي أو قانوني، مو مجرد توثيق أو تدريب.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2461": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفل عنده <bdi>peanut allergy</bdi> و<bdi>asthma</bdi> استلم أدوية بدون توثيق حساسيته، واكتُشف الخطأ وقت <bdi>nurse handover</bdi>؛ السؤال عن المبدأ الأوسع المختبَر.",
    "clues": [
        ("peanut allergy", "معلومة حرجة ما انتقلت بين الطاقم الطبي"),
        ("without the allergy being documented", "فشل بنقل المعلومة، مو فقط بتوثيقها"),
    ],
    "why_correct": [
        "الخطأ اكتُشف \"وقت <bdi>handover</bdi>\": معلومة <bdi>allergy</bdi> ما انتقلت أو ما تم تسجيلها، فاستلم الطفل أدوية رغم خطرها.",
        "<bdi>handover</bdi> نقطة عالية الخطورة لسوء التواصل، فالمبدأ الأوسع المختبَر هو تحسين <bdi>communication</bdi> بين مزودي الرعاية لضمان سلامة المريض.",
    ],
    "when_changes": [
        "لو السؤال يسأل عن الإجراء المحدد اللي كان ينقص، يصير الجواب <bdi>documentation</bdi> لأنها جزء من التواصل.",
        "لو الخطأ كان بإعطاء الدواء لمريض غلط، يصير المبدأ <bdi>two patient identifiers</bdi>.",
    ],
    "rule": "معلومة حرجة ضاعت وقت <bdi>handover</bdi> بين طاقم طبي = مشكلة <bdi>communication</bdi> الأوسع، حتى لو <bdi>documentation</bdi> جزء من الحل.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2496": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "حامل بالثلث الأخير عندها علامات <bdi>severe pre-eclampsia</bdi> وترفض <bdi>admission</bdi>، والسؤال عن التسلسل الأخلاقي الصحيح للتصرف.",
    "clues": [
        ("refuses the admission and asked to leave the hospital", "رفض مريضة مختصة لعلاج موصى به بشدة"),
    ],
    "labs": [
        ["Blood pressure", "160/95 mmHg", "<140/90 mmHg"],
        ["CTG (fetal heart rate)", "170 bpm", "110-160 bpm"],
    ],
    "why_correct": [
        "الصداع واضطراب الرؤية مع ضغط حوالي 160/95 بالثلث الأخير علامات <bdi>severe pre-eclampsia</bdi>، وزيادة نبض الجنين (<bdi>CTG 170</bdi>) يضيف قلق جنيني، فـ<bdi>admission</bdi> وضبط الضغط والولادة إجراءات واضحة.",
        "بس هي راشدة ولها <bdi>capacity</bdi> وترفض؛ الطبيب يشرح المخاطر المحددة لها وللجنين (<bdi>eclampsia</bdi>، <bdi>stroke</bdi>، <bdi>abruption</bdi>) ويحاول يقنعها، وإذا استمرت على رفضها تُحترم <bdi>autonomy</bdi> وتوقّع <bdi>DAMA</bdi> مع توثيق كامل وبقاء الباب مفتوح للرجوع.",
    ],
    "when_changes": [
        "لو فقدت <bdi>capacity</bdi> (مثل <bdi>eclamptic seizure</bdi>)، يصير التدخل فوري بدون انتظار موافقتها.",
        "لو كانت أعراضها أخف بدون علامات <bdi>severe</bdi>، يختلف مستوى الاستعجال بالشرح بس المبدأ الأخلاقي نفسه.",
    ],
    "rule": "مع مريضة مختصة ترفض علاج ضروري: اشرح المخاطر بالتفصيل وحاول تقنعها، وإذا استمرت على الرفض وثّق ووقّع <bdi>DAMA</bdi>، ما تفرض العلاج ولا تتركها تذهب بدون شرح.",
    "comparison": None,
    "guideline_note": None,
},
"AS-2537": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "بغرفة <bdi>ED</bdi> بعد حادث، الطبيب يسأل عن حالة <bdi>airway</bdi>، <bdi>breathing</bdi>، <bdi>circulation</bdi> والممرضة تجاوب بصوت عالي لكل الفريق، والسؤال عن نوع أداة <bdi>TeamSTEPPS communication</bdi>.",
    "clues": [
        ("communication", "يحدد إن السؤال عن نوع أداة تواصل محددة ضمن <bdi>TeamSTEPPS</bdi>"),
    ],
    "why_correct": [
        "بحالات <bdi>trauma resuscitation</bdi>، القائد يسأل عن حالة كل عنصر حرج والعضو يعلن الحالة بصوت عالي لكل الفريق (\"<bdi>airway patent</bdi>\"، \"<bdi>breathing okay</bdi>\"، حالة <bdi>circulation</bdi>).",
        "هذا هو <bdi>call-out</bdi> ضمن <bdi>TeamSTEPPS</bdi>: استراتيجية لنقل معلومة حرجة أثناء <bdi>emergency</bdi> بحيث يسمعها الجميع بنفس اللحظة ويتوقعون الخطوة التالية.",
    ],
    "when_changes": [
        "لو كان فيه أمر دواء يُعاد تكراره من المستلم ويؤكده المرسل، يصير الجواب <bdi>check-back</bdi> أو <bdi>closed-loop communication</bdi>.",
        "لو السياق كان تسليم مريض بين شفتين بصيغة منظمة (Situation, Background, Assessment, Recommendation)، يصير الجواب <bdi>SBAR</bdi>.",
    ],
    "rule": "إعلان حالة حيوية بصوت عالي لكل الفريق أثناء <bdi>resuscitation</bdi> = <bdi>call-out</bdi>؛ تكرار أمر والتأكد منه = <bdi>check-back/closed-loop</bdi>؛ تسليم منظم = <bdi>SBAR</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0002": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "سؤال حساب <bdi>sensitivity</bdi> لفحص فرز جديد بالمقارنة بـ<bdi>mammogram</bdi> كمرجع، يختبر بناء جدول 2×2 صحيح.",
    "clues": [
        ("200 women", "عدد النساء الإيجابيات حسب المرجع (<bdi>mammogram</bdi>)، هو مقام <bdi>sensitivity</bdi>"),
        ("180", "عدد <bdi>true positives</bdi> اللي اكتشفها الفحص الجديد"),
        ("misses 20", "عدد <bdi>false negatives</bdi>"),
        ("sensitivity", "يحدد المطلوب حسابه بالضبط"),
    ],
    "why_correct": [
        "<bdi>sensitivity</bdi> = <bdi>true positives</bdi> / كل من عنده المرض حقيقةً (حسب المرجع)؛ هنا 200 امرأة إيجابية بـ<bdi>mammogram</bdi>.",
        "الفحص الجديد يكتشف 180 منهم ويفوّت 20 (<bdi>false negatives</bdi>)، فـ<bdi>sensitivity</bdi> = 180 / (180+20) = 180/200 = <bdi>90%</bdi>. الـ50 <bdi>false positive</bdi> بين النساء السالبات تؤثر على <bdi>specificity</bdi> فقط، مو <bdi>sensitivity</bdi>.",
    ],
    "when_changes": [
        "لو السؤال يبي <bdi>positive predictive value</bdi>، يصير الحساب 180/(180+50) ≈ 78%.",
        "لو يبي <bdi>specificity</bdi>، يصير 750/800 ≈ 94%.",
    ],
    "rule": "ابني جدول 2×2 أول (TP, FN, FP, TN)، و<bdi>sensitivity</bdi> و<bdi>specificity</bdi> تُقرآن من عمود الحالة الحقيقية، بينما <bdi>PPV</bdi> و<bdi>NPV</bdi> تُقرآن من صف نتيجة الفحص.",
    "comparison": {
        "headers": ["المؤشر", "القيمة"],
        "rows": [
            ["<bdi>Sensitivity</bdi>", "180/200 = 90%"],
            ["<bdi>Specificity</bdi>", "750/800 ≈ 94%"],
            ["<bdi>PPV</bdi>", "180/230 ≈ 78%"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},
"AS-0007": {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "السؤال عن <bdi>inclusion criteria</bdi> الصحيح لاستخدام <bdi>PSA</bdi> كفحص <bdi>screening</bdi> مع أخذ بالاعتبار إن <bdi>specificity</bdi> منخفضة تسبب <bdi>overtreatment</bdi>.",
    "clues": [
        ("low specificity", "يعني فحوصات إيجابية كثيرة كاذبة تؤدي لـ<bdi>overdiagnosis</bdi>"),
        ("over treatment", "النتيجة السلبية لاستخدام <bdi>PSA</bdi> بشكل واسع بدون استهداف"),
    ],
    "why_correct": [
        "بسبب <bdi>low specificity</bdi>، استخدام <bdi>PSA</bdi> كفحص <bdi>screening</bdi> واسع يسبب كثير <bdi>false positives</bdi> و<bdi>overtreatment</bdi>؛ الحل المنطقي يستهدف المجموعات الأعلى خطورة (<bdi>high risk</bdi> أو <bdi>family history</bdi>) بدل الفحص الجماعي العشوائي.",
        "هذا يرفع <bdi>pre-test probability</bdi> ويقلل نسبة <bdi>false positives</bdi> نسبيًا، ويتماشى مع توصيات <bdi>shared decision making</bdi> للرجال الأعلى خطورة.",
    ],
    "when_changes": [
        "لو كان المريض عنده أعراض فعلية (مثل أعراض بولية)، يصير استخدام <bdi>PSA</bdi> تشخيصي مو <bdi>screening</bdi>، وهذا خيار مختلف تمامًا.",
        "لو السؤال يبي خاصية الفحص المطلوبة أصلًا للـ<bdi>screening</bdi> الجيد (<bdi>sensitivity</bdi> عالية)، يختلف التركيز عن معايير <bdi>inclusion</bdi>.",
    ],
    "rule": "فحص <bdi>screening</bdi> بـ<bdi>low specificity</bdi> يُستخدم بشكل أذكى عند تضييق المجموعة المستهدفة لذوي الخطورة الأعلى، لا بتوسيع الفحص لأكبر عدد من الناس.",
    "comparison": None,
    "labs": None,
    "guideline_note": "الإجابة هنا باجتهادي الطبي لأن المصدر نفسه ما حدد جوابًا مؤكدًا وترك علامة استفهام على الخيارين A و C.",
},
"AS-0105": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "رجل عمره 50 سنة، <bdi>HTN</bdi> متحكم فيه و<bdi>hemorrhagic stroke</bdi> متعافي منه، أخذ <bdi>flu vaccine</bdi> قبل 6 أشهر؛ السؤال عن اللقاح المستحق الآن.",
    "clues": [
        ("50-year-old", "العمر المحدد هو المحرّك الأساسي لقرار اللقاح"),
        ("received the seasonal influenza vaccine 6 months ago", "اللقاح الموسمي أُعطي بالفعل هذا الموسم"),
    ],
    "why_correct": [
        "عمره <bdi>50</bdi> سنة، ولقاح <bdi>recombinant zoster vaccine</bdi> يُوصى به لكل البالغين الأصحاء مناعيًا من عمر 50 فما فوق (جرعتين)، بدون الحاجة لتاريخ سابق لـ<bdi>chickenpox</bdi> أو <bdi>shingles</bdi>.",
        "<bdi>HTN</bdi> و<bdi>recovered hemorrhagic stroke</bdi> ما تُعتبر <bdi>contraindications</bdi>، ولقاح <bdi>influenza</bdi> أخذه هذا الموسم، فاللقاح المستحق الآن هو <bdi>zoster</bdi>.",
    ],
    "when_changes": [
        "لو عمره تحت 50 بدون عوامل خطورة أخرى، ما يكون لقاح <bdi>zoster</bdi> مستحق بعد.",
        "لو ما أخذ <bdi>flu vaccine</bdi> هذا الموسم، يصير اللقاح المستحق هو <bdi>influenza</bdi> العادي (مو <bdi>booster</bdi>).",
    ],
    "rule": "عمر 50 فما فوق = استحقاق <bdi>zoster vaccine</bdi>؛ <bdi>stroke</bdi> و<bdi>HTN</bdi> هنا مجرد تشويش، والعمر هو العلامة الحاسمة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0106": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "نفس فكرة اللقاح عند عمر 50، بس هذي المرة مع <bdi>COPD</bdi> بدل <bdi>stroke</bdi>.",
    "clues": [
        ("50-Year-Old", "العمر هو المحرّك الأساسي لاستحقاق لقاح <bdi>zoster</bdi>"),
    ],
    "why_correct": [
        "عمر <bdi>50</bdi> هو المحرّك: لقاح <bdi>recombinant zoster</bdi> يُوصى به لكل من عمره 50 فما فوق (جرعتين)، و<bdi>COPD</bdi> ليس <bdi>contraindication</bdi> لأنه لقاح غير حي.",
        "الخيارات الأخرى غير مناسبة بذاتها: <bdi>hepatitis A</bdi> بلا مؤشر هنا، ولقاح <bdi>influenza</bdi> بالبالغين ما له \"<bdi>booster</bdi>\".",
    ],
    "when_changes": [
        "لو السؤال ذكر إنه ما أخذ <bdi>flu shot</bdi> هذا الموسم، يصير اللقاح المستحق <bdi>influenza</bdi> الاعتيادي.",
        "لو كان عنده <bdi>immunocompromise</bdi>، قد يحتاج جرعة إضافية أو تقييم مختلف للقاحات.",
    ],
    "rule": "البالغ عمر 50+: <bdi>zoster vaccine</bdi> مستحق دايمًا مهما كانت الحالة المرافقة (ما عدا <bdi>contraindication</bdi> حقيقية)؛ <bdi>COPD</bdi> يرفع أهمية <bdi>influenza</bdi> و<bdi>pneumococcal</bdi> السنوية، بس ما فيه \"<bdi>booster</bdi>\" لـ<bdi>influenza</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0122": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال مفاهيمي: فحص جديد صُمم \"ليشمل حتى الحالات اللي كانت تُفوَّت\"، أي مؤشر يرتفع بهذا التصميم.",
    "clues": [
        ("include the missed cases", "يشير لتقليل <bdi>false negatives</bdi>، وهذا يرفع <bdi>sensitivity</bdi>"),
    ],
    "why_correct": [
        "فحص فرز \"صُمم ليشمل الحالات المفوَّتة\" يهدف لرصد الحالات اللي كان الفحص القديم يفوّتها، يعني تقليل <bdi>false negatives</bdi>.",
        "<bdi>sensitivity</bdi> = TP/(TP+FN)، فتقليل <bdi>false negatives</bdi> يعني ارتفاع <bdi>sensitivity</bdi>، وهذا المطلوب بفحوصات <bdi>screening</bdi> حيث فوات حالة هو أكبر ضرر.",
    ],
    "when_changes": [
        "لو السؤال عن قلة <bdi>false positives</bdi> (تأكيد التشخيص)، يصير المؤشر المطلوب <bdi>specificity</bdi>.",
        "لو السؤال عن احتمال إصابة المريض فعليًا بعد نتيجة إيجابية، يصير المؤشر <bdi>PPV</bdi> ويتأثر بـ<bdi>prevalence</bdi>.",
    ],
    "rule": "كلمات \"<bdi>screening</bdi>\"، \"مو نفوّت حالة\"، \"نشمل الحالات المفوّتة\" = فكر <bdi>high sensitivity</bdi> مباشرة؛ \"نتأكد/نتجنب إيجابي كاذب\" = <bdi>specificity</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0316": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "نسخة مكررة من AS-0105: رجل 50 سنة، <bdi>HTN</bdi> و<bdi>hemorrhagic stroke</bdi> متعافي، واللقاح المستحق الآن.",
    "clues": [
        ("50-year-old", "العمر هو المحرّك لاستحقاق لقاح <bdi>zoster</bdi>"),
        ("received the seasonal influenza vaccine 6 months ago", "لقاح <bdi>influenza</bdi> هذا الموسم مأخوذ بالفعل"),
    ],
    "why_correct": [
        "عمره 50 سنة، فلقاح <bdi>recombinant zoster</bdi> مستحق لكل البالغين من هذا العمر فما فوق (جرعتين)، بدون تأثير من <bdi>HTN</bdi> أو <bdi>stroke</bdi> المتعافي.",
        "لقاح <bdi>influenza</bdi> هذا الموسم مأخوذ، فما يحتاج \"<bdi>booster</bdi>\" (وأصلًا ما فيه <bdi>booster</bdi> لـ<bdi>influenza</bdi> بالبالغين).",
    ],
    "when_changes": [
        "لو كان عمره تحت 50، ما يكون <bdi>zoster</bdi> مستحق.",
        "لو ما أخذ <bdi>flu vaccine</bdi> هذا الموسم، يصير اللقاح المستحق <bdi>influenza</bdi> الاعتيادي.",
    ],
    "rule": "عمر 50 فما فوق = <bdi>zoster vaccine</bdi>، وهذا نفس السؤال بتكرار؛ احفظ العمر كمحرك أساسي للقرار.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0361": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نسخة مكررة من AS-0122: فحص جديد يشمل الحالات المفوَّتة، أي مؤشر يرتفع.",
    "clues": [
        ("even include the missed cases", "تقليل <bdi>false negatives</bdi> يعني رفع <bdi>sensitivity</bdi>"),
    ],
    "why_correct": [
        "فحص فرز جديد \"يشمل الحالات المفوَّتة\" يعني تقليل <bdi>false negatives</bdi>، وبالتالي رفع <bdi>sensitivity</bdi> = TP/(TP+FN).",
        "هذا المؤشر المطلوب بفحوصات <bdi>screening</bdi>، حيث الهدف الأساسي عدم تفويت أي حالة.",
    ],
    "when_changes": [
        "لو كان الهدف تقليل <bdi>false positives</bdi>، يصير المؤشر <bdi>specificity</bdi>.",
        "لو السؤال عن احتمال الإصابة الحقيقية بعد نتيجة إيجابية، يصير المؤشر <bdi>PPV</bdi> المتأثر بـ<bdi>prevalence</bdi>.",
    ],
    "rule": "\"يشمل الحالات المفوَّتة\" = <bdi>high sensitivity</bdi> دايمًا، نفس القاعدة بتكرار.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0365": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال عن تفسير <bdi>incidence</bdi> الصحيح: عدد حالات جديدة ضمن مجموعة محددة بفترة زمنية محددة.",
    "clues": [
        ("1000 people for one year", "المقام (<bdi>population at risk</bdi>) والفترة الزمنية"),
        ("15 of them developed", "المقام (<bdi>new cases</bdi>)، يؤكد إنها <bdi>incidence</bdi> مو <bdi>prevalence</bdi>"),
        ("incidence", "يحدد المصطلح المطلوب تفسيره"),
    ],
    "why_correct": [
        "<bdi>incidence</bdi> هو عدد الحالات <bdi>new</bdi> بمجموعة معرّضة للخطر خلال فترة زمنية محددة.",
        "هنا 15 حالة جديدة بين 1000 شخص بفترة سنة = <bdi>incidence</bdi> 15 لكل 1000 بالسنة (1.5% بالسنة)، والخيار D وحده يحافظ على العدد والمقام والفترة الزمنية معًا.",
    ],
    "when_changes": [
        "لو كان السؤال عن \"يملكون المرض حاليًا\" بدل \"يطورون المرض\"، يصير المفهوم <bdi>prevalence</bdi> مو <bdi>incidence</bdi>.",
        "لو حذفنا الفترة الزمنية من السؤال، ما نقدر نحسب <bdi>incidence rate</bdi> بشكل صحيح.",
    ],
    "rule": "كلمة \"<bdi>have</bdi>\" تشير لـ<bdi>prevalence</bdi> وكلمة \"<bdi>develop</bdi>\" تشير لـ<bdi>incidence</bdi>؛ وبعدها تأكد من المقام والفترة الزمنية.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0424": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال حساب <bdi>odds ratio</bdi> بدراسة <bdi>case-control</bdi> عن علاقة <bdi>cesarean section</bdi> و<bdi>type 1 diabetes</bdi>.",
    "clues": [
        ("case-control study", "يحدد نوع الدراسة والمقياس المناسب (<bdi>odds ratio</bdi> مو <bdi>relative risk</bdi>)"),
        ("80 were delivered by cesarean section and 120 by vaginal delivery", "أرقام مجموعة <bdi>cases</bdi>"),
        ("160 were delivered by cesarean section and 40 by vaginal delivery", "أرقام مجموعة <bdi>controls</bdi>"),
        ("odds ratio", "المطلوب حسابه"),
    ],
    "why_correct": [
        "<bdi>odds ratio</bdi> بدراسة <bdi>case-control</bdi> = (a × d) / (b × c).",
        "مفتاح هذا السؤال (6) يجي من اعتبار <bdi>vaginal delivery</bdi> هو التعرّض: (120 × 160) / (80 × 40) = 19200/3200 = <bdi>6</bdi>.",
    ],
    "when_changes": [
        "لو التعرّض المعتمد هو <bdi>cesarean section</bdi> كما يذكر نص السؤال حرفيًا، يصير الحساب (80×40)/(120×160) = 1/6 ≈ 0.17، وهذا غير متوفر بالخيارات، فيُرجَّح إن الأرقام بالمصدر معكوسة.",
        "لو الدراسة كانت <bdi>cohort</bdi> بدل <bdi>case-control</bdi>، يصير المقياس الصحيح <bdi>relative risk</bdi> مو <bdi>odds ratio</bdi>.",
    ],
    "rule": "<bdi>odds ratio</bdi> = (a×d)/(b×c)؛ عكس تسمية \"من هو المتعرّض\" يعكس النتيجة لمقلوبها (6 تصير 1/6)، فانتبه لجدول 2×2 جيدًا.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0445": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "مريض <bdi>DM</bdi> و<bdi>HTN</bdi> متحكم فيهم بس يفوّت مواعيده كثير، والسؤال عن مبدأ الجودة (<bdi>IOM quality domain</bdi>) المستهدف.",
    "clues": [
        ("missed multiple appointments", "المشكلة مش بالسيطرة الطبية، بل بالالتزام والمتابعة"),
        ("medical value", "يحدد المطلوب أحد مبادئ جودة الرعاية الستة"),
    ],
    "why_correct": [
        "مبادئ الجودة الستة حسب <bdi>IOM</bdi> هي <bdi>safe, effective, patient-centred, timely, efficient, equitable</bdi>؛ ومرضه \"متحكم فيه جيدًا\"، فالمشكلة مو بالنتيجة <bdi>clinical</bdi> بل بـ\"فوّت مواعيد متعددة\".",
        "الطبيب يبي يُشرك المريض، يستكشف عوائقه وتفضيلاته، ويبني الرعاية حول حاجاته ليبقى ملتزم بالمتابعة، وهذا هو مبدأ <bdi>patient centredness</bdi>.",
    ],
    "when_changes": [
        "لو كان القلق عن هدر موارد أو وقت بالعيادة، يصير المبدأ <bdi>efficiency</bdi>.",
        "لو كان القلق عن تأخير بالنظام نفسه بالحصول على موعد، يصير المبدأ <bdi>timeliness</bdi>.",
    ],
    "rule": "تحكم جيد بالمرض + ضعف حضور/التزام المريض = <bdi>patient centredness</bdi> (إشراك المريض)؛ قائمة انتظار بالنظام = <bdi>timeliness</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0478": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "سؤال حساب <bdi>cumulative prevalence</bdi> (= <bdi>existing + new cases</bdi> / <bdi>population</bdi>) بدراسة <bdi>colon cancer</bdi>.",
    "clues": [
        ("100,000", "مقام الحساب (<bdi>population</bdi>)"),
        ("Existing cases: 300, New cases: 75", "مجموع الحالات الموجودة والجديدة يُجمع معًا بـ<bdi>cumulative prevalence</bdi>"),
        ("cumulative prevalence", "يحدد نوع المقياس المطلوب حسابه"),
    ],
    "why_correct": [
        "\"<bdi>cumulative</bdi>\" (أو <bdi>period</bdi>) <bdi>prevalence</bdi> تحسب كل من عنده المرض خلال الفترة: حالات موجودة + حالات جديدة.",
        "(300 + 75) / 100,000 = 375 / 100,000 = <bdi>0.375%</bdi> (أي 3.75 لكل 1000).",
    ],
    "when_changes": [
        "لو السؤال يبي <bdi>point prevalence</bdi> فقط، يُستخدم عدد الحالات الموجودة وحدها (300/100,000 = 0.3%).",
        "لو يبي <bdi>incidence</bdi>، يُستخدم عدد الحالات الجديدة فقط على المجموعة المعرّضة للخطر (75/99,700 تقريبًا).",
    ],
    "rule": "\"<bdi>cumulative</bdi>\" أو \"<bdi>period</bdi>\" <bdi>prevalence</bdi> = أضف الحالات الجديدة للموجودة؛ <bdi>point prevalence</bdi> = الحالات الموجودة وحدها فقط.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0478B": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "سؤال حساب <bdi>prevalence</bdi> للـ<bdi>migraine</bdi> ضمن عيادة محددة، مع فخ لرقم <bdi>population</bdi> أكبر غير مستخدم كمقام.",
    "clues": [
        ("200 adult patients", "المجموعة المدروسة فعلًا، وهي المقام الصحيح"),
        ("75 patients currently have migraine", "المقام (الحالات الموجودة)"),
        ("among these patients", "يحدد إن المقام هو مرضى العيادة لا المجتمع الكامل"),
    ],
    "why_correct": [
        "<bdi>prevalence</bdi> = الحالات الموجودة / المجموعة المدروسة فعليًا، وهنا المجموعة المدروسة هي 200 بالغ بالعيادة، و75 \"عندهم <bdi>migraine</bdi> حاليًا\"، فـ75/200 = 0.375 (37.5%).",
        "الخيار A (0.374) هو الأقرب لهذي القيمة؛ رقم \"<bdi>population</bdi> 100000\" مجرد فخ لأن المقام الصحيح هو المجموعة اللي فعلًا فُحصت.",
    ],
    "when_changes": [
        "لو السؤال يبي <bdi>prevalence</bdi> على مستوى المدينة (100,000)، يصير المقام مختلف تمامًا وتصبح النتيجة أصغر بكثير.",
        "لو السؤال يحدد فترة زمنية ويطلب حالات جديدة فقط، يتحول المفهوم لـ<bdi>incidence</bdi> مو <bdi>prevalence</bdi>.",
    ],
    "rule": "اختر المقام من المجموعة اللي فعلًا دُرست أو فُحصت، لا من أي رقم \"<bdi>population</bdi>\" إضافي مذكور كفخ بالسؤال.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2460": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "سؤال عن القاعدة الصحيحة بكتابة <bdi>prescription</bdi> بدون اختصارات خطيرة (<bdi>error-prone abbreviations</bdi>).",
    "clues": [
        ("vitamin D", "دواء الحالة (<bdi>vitamin D</bdi> للرضيع)"),
        ("best way to write the prescription", "يبحث عن الصيغة الأسلم بالكتابة"),
    ],
    "why_correct": [
        "الكتابة الأفضل تتجنب الاختصارات الخطيرة: \"<bdi>unit</bdi>\" تكتب كاملة (مو \"U\" اللي ممكن تُقرأ 0 أو 4)، و\"<bdi>daily</bdi>\" تكتب كاملة (مو \"OD\" اللي ممكن تُقرأ <bdi>right eye</bdi>).",
        "الخيار C يحقق الاثنين مع بقاء الجرعة بأرقام واضحة، وهذا يطابق قاعدة <bdi>do-not-use abbreviations list</bdi>.",
    ],
    "when_changes": [
        "لو جاء خيار يكتب الجرعة بالكلمات كاملة بدل الأرقام (مثل \"<bdi>four hundred</bdi>\")، هذا غير معياري وقد يُقرأ غلط، فما يكون الأفضل.",
        "لو السؤال عن اختصار آخر خطير (مثل <bdi>trailing zero</bdi>)، القاعدة نفسها: تجنب أي اختصار يسبب لبس.",
    ],
    "rule": "بكتابة <bdi>prescription</bdi> دايمًا اكتب \"<bdi>unit</bdi>\" و\"<bdi>daily</bdi>\" كاملة بدون اختصار، وخلي الجرعة بأرقام واضحة لا بكلمات.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
}

WHY_WRONG = {
"AS-2278": {
    "A": "<bdi>antibiotics</bdi> وصفات دوائية فيها خطر <bdi>allergy</bdi> وجرعة وتفاعلات، فهذا المصدر يتوقع توثيقها من <bdi>prescriber</bdi> مباشرة مو بالتلفون.",
    "B": "<bdi>methotrexate</bdi> دواء <bdi>cytotoxic</bdi> (<bdi>chemotherapy</bdi>)، والأوامر الشفوية لأدوية <bdi>chemotherapy</bdi> ممنوعة تمامًا بإرشادات السلامة.",
    "C": "<bdi>paracetamol</bdi> دواء منخفض الخطورة وبعض المصادر تقبله بالتلفون، لكن هنا الجواب المعتمد يفضّل خيار <bdi>nutrition feeding</bdi> الغير دوائي.",
},
"AS-2296": {
    "A": "الاعتماد على <bdi>memory</bdi> أسلوب معرّض للخطأ، وممارسة <bdi>safe prescribing</bdi> تشجع على الفحص والمراجعة لا الاعتماد على الذاكرة.",
    "C": "معرفة إن <bdi>warfarin</bdi> دواء عالي الخطورة ما كانت الفجوة؛ الطبيب وصفه وهو يعرف خطره، بس ما كان يعرف إن المريضة حامل.",
    "D": "<bdi>generic names</bdi> تساعد بتجنب التكرار واللخبطة بين الأسماء التجارية، بس ما تكشف <bdi>contraindication</bdi> خاصة بهذه المريضة بالذات.",
},
"AS-2301": {
    "A": "الـ<bdi>DNR</bdi> الخارجي ما يُتجاهل عند الوصول؛ يُحترم مؤقتًا لمدة 24 ساعة لتجنب إنعاش غير مرغوب قبل إعادة التقييم من الفريق المستقبل.",
    "C": "بالنظام السعودي، <bdi>DNR</bdi> قرار طبي يوثقه ويصدره الأطباء المؤهلون؛ العائلة تُعلَم بس ما تُوافق أو تتحقق منه.",
    "D": "ما أي عضو بالفريق يقدر يتحقق من <bdi>DNR</bdi>؛ هذا قرار يرجع للطبيب (بقيادة <bdi>consultant</bdi>)، والممرضات وغيرهم يتبعون الأمر الموثق فقط.",
},
"AS-2302": {
    "A": "ستة أشهر مو القاعدة؛ <bdi>DNR</bdi> من مستشفى آخر مجرد جسر مؤقت، والمستشفى المستقبل لازم يعيد التقييم خلال 24 ساعة.",
    "C": "اعتباره <bdi>invalid</bdi> ممكن يؤدي لإنعاش ضد قرار موثق بشكل صحيح أثناء فترة التحويل؛ يُحترم لمدة 24 ساعة.",
    "D": "ما يبقى ساري بدون نهاية؛ بعد 24 ساعة لازم يُراجع ويُستبدل بأمر <bdi>DNR</bdi> جديد من المستشفى المستقبل.",
},
"AS-2303": {
    "A": "قرار <bdi>DNR</bdi> الموثق ما يصبح باطل لمجرد تغيير المستشفى؛ يفترض ينتقل مع ملف التحويل ويُراجع من الفريق المستقبل، مو يُتجاهل.",
    "B": "هذا الخيار يضيف حد زمني غير منطقي ولا يجاوب فعليًا من المسؤول عن التحقق من <bdi>code status</bdi>؛ ما يختبره السؤال هو مسؤولية التحقق عند الوصول.",
    "C": "الأهل ممكن يبلّغوا ويشاركوا بالقرار، بس التحقق من <bdi>code status</bdi> وتحديده مسؤولية مهنية للفريق المعالج، مو واجب العائلة.",
},
"AS-2339": {
    "A": "<bdi>autonomy</bdi> المريضة ما تلزم الطبيب يسوي إجراء غير قانوني؛ الطلب لوحده مو سبب طبي معتمد للإجهاض.",
    "B": "موافقة الأب ما تحوّل إجراء غير قانوني لقانوني؛ موافقة الزوج مهمة فقط ضمن إجراء مسموح طبيًا من الأساس.",
},
"AS-2340": {
    "B": "استخدام الدين يحمّل المريضة رأي الطبيب الديني ويضغط عليها؛ الاستشارة لازم تعتمد على الحقائق الطبية والقانونية مو المعتقد الشخصي.",
    "C": "أخذ موقف الطبيب الشخصي وتوجيه المريضة بعيدًا عن طلبها هو تمامًا التصرف المتحيز والأبوي اللي السؤال ينتقده.",
},
"AS-2341": {
    "B": "الأب ما له أي سلطة يقرر بدل الأم المختصة؛ موافقتها هي الوحيدة المطلوبة لعملية على جسمها.",
    "C": "تنفيذ العملية بدون موافقتها اعتداء (<bdi>battery</bdi>) حتى لو كان السبب طبي لصالح الجنين؛ العملية تتم فقط بعد موافقتها.",
    "D": "موافقة الوالدين معًا غير مطلوبة؛ المرأة المختصة توافق لوحدها، و<bdi>emergency implied consent</bdi> ينطبق فقط إذا كانت فاقدة الوعي.",
},
"AS-2342": {
    "A": "تنفيذ العملية ضد رغبتها اعتداء بغض النظر عن مؤشر الجنين؛ الجنين ما له حق قانوني يتجاوز رفض الأم المختصة.",
    "B": "رأي الأب ما يقدر يتغلب على قرار المريضة المختصة بخصوص جراحة بجسمها.",
    "D": "موافقتها هي الوحيدة المطلوبة؛ طلب موافقة الأب أيضًا يعطيه حق <bdi>veto</bdi> غلط.",
},
"AS-2343": {
    "A": "النموذج الموقّع سابقًا ما يبقى صالح إذا عبّرت عن شك؛ <bdi>consent</bdi> يمكن سحبه بأي وقت ولازم يُعاد تأكيده.",
    "B": "جهوزية غرفة العمليات أو انتظار التخدير أبدًا سبب للمتابعة بدون <bdi>consent</bdi> صحيح، خصوصًا بحالة <bdi>elective</bdi>.",
    "C": "والد الطفل (زوجها) ما يقدر يوافق بدل امرأة مختصة؛ فقط هي تقدر توافق على عمليتها.",
},
"AS-2402": {
    "B": "موافقة الزوج ما لها قيمة قانونية إذا رفضت المريضة المختصة نفسها؛ الزوج ما يقدر يوافق بدلها.",
    "C": "رفض علاج موصى به مو بذاته دليل على فقدان <bdi>capacity</bdi>؛ التقييم النفسي يُطلب فقط إذا فيه علامات حقيقية تشكك بقدرتها على الفهم والقرار.",
    "D": "تنفيذ العملية رغم رفضها اعتداء (<bdi>battery</bdi>) بغض النظر عن الاستعجال أو فائدة الجنين.",
},
"AS-2403": {
    "A": "الانتظار لموافقة العائلة يؤخر جراحة منقذة للحياة بمريضة منخفضة الضغط وتنزف؛ بالحالات العاجلة مع مريض فاقد القدرة ما يُنتظر الأقارب.",
    "C": "أمر المحكمة بطيء جدًا لحالة نزيف حاد وغير مطلوب أصلًا لما تنطبق قاعدة <bdi>emergency doctrine</bdi>.",
},
"AS-2428": {
    "B": "<bdi>non-maleficence</bdi> (تجنب الضرر) قريب بالمعنى، بس المفتاح هنا يركز على تقديم فائدة فعلية (<bdi>standard care</bdi>) مو فقط تجنب الضرر.",
    "C": "<bdi>autonomy</bdi> يُحترم من خلال <bdi>consent</bdi> طوعي ومعلوم للمشاركة بالتجربة؛ العبارة هنا عن نوع العلاج اللي بتستلمه مو عن قرارها.",
    "D": "<bdi>justice</bdi> يتعلق بعدالة اختيار المشاركين وتوزيع المخاطر والفوائد، وهذا مو موضوع الطمأنة هنا.",
},
"AS-2443": {
    "A": "تجاهل وإغلاق قضية خرق <bdi>confidentiality</bdi> مؤكد مع شكوى رسمية غير مقبول أبدًا؛ يفشل بحق المريضة وواجب المستشفى القانوني.",
    "B": "تدريب الطاقم على <bdi>confidentiality</bdi> إجراء وقائي مفيد لاحقًا، بس ما يعالج هذا الخرق والشكوى بالتحديد.",
    "C": "المريضة أصلًا عرفت وقدّمت شكوى؛ التوثيق وحده بدون <bdi>investigation</bdi> ومحاسبة يترك الخرق بدون معالجة حقيقية.",
},
"AS-2461": {
    "A": "توثيق التاريخ المرضي جزء من الحل، بس المصدر يعتمد المبدأ الأوسع للتواصل أثناء <bdi>handover</bdi> كإجابة رئيسية.",
    "B": "<bdi>two patient identifiers</bdi> يمنع إعطاء دواء لمريض غلط؛ هنا المريض الصحيح استلم العلاج بس معلومة الحساسية ما انتقلت.",
    "D": "تعليم المريض أو العائلة مهم لإدارة <bdi>allergy</bdi> و<bdi>asthma</bdi>، بس هذا كان فشل بالتواصل بين الطاقم الطبي، مو فجوة بمعرفة العائلة.",
},
"AS-2496": {
    "A": "فرض <bdi>admission</bdi> يتجاوز <bdi>autonomy</bdi> مريضة راشدة ولها <bdi>capacity</bdi>، ويُعتبر اعتداء؛ العلاج القسري يُطبّق فقط بغياب <bdi>capacity</bdi> أو بحالة <bdi>emergency</bdi> حقيقية بدون قدرة على القرار، وهذا غير موجود هنا.",
    "C": "تركها تذهب ببساطة يتجاهل واجب الإخبار؛ الرفض يكون صحيحًا فقط إذا كان <bdi>informed</bdi>، فلازم تُشرح المخاطر ويُوثّق <bdi>DAMA</bdi>، مو خروج عادي بدون شرح.",
    "D": "خيار غير مكتمل بدون محتوى واضح؛ التسلسل الأخلاقي المتوقع هو الشرح، محاولة الإقناع، ثم احترام الرفض المُعلَم (<bdi>DAMA</bdi>).",
},
"AS-2537": {
    "A": "<bdi>check-back</bdi> يعني إن المستلم يكرر التعليمة والمرسل يتأكد منها؛ هنا ما فيه تكرار أو تأكيد، الممرضة فقط تعلن النتائج.",
    "B": "<bdi>SBAR</bdi> صيغة منظمة للتسليم أو تصعيد مخاوف عن مريض، مو تقارير حالة سريعة أثناء <bdi>primary survey</bdi>.",
    "C": "<bdi>closed-loop communication</bdi> يعني إعطاء أمر، تكراره من المستلم، وتأكيده من المرسل؛ هنا فقط أسئلة وأجوبة تُعلن للفريق بدون حلقة تكرار وتأكيد.",
},
"AS-0002": {
    "A": "70% ما يطابق أي حساب صحيح من هذي الأرقام؛ <bdi>sensitivity</bdi> تستخدم فقط الـ200 امرأة المرجعية الإيجابية.",
    "B": "80% فخ قريب من <bdi>positive predictive value</bdi> (180/(180+50) ≈ 78%)، وهذا يستخدم كل الإيجابيات بالفحص كمقام، مو كل المصابات الحقيقيات.",
    "D": "100% يتطلب صفر <bdi>false negatives</bdi>؛ الفحص فوّت 20 من أصل 200 مصابة حقيقة.",
},
"AS-0105": {
    "B": "لقاح <bdi>hepatitis A</bdi> لمجموعات خطورة محددة (سفر، مرض كبد مزمن، سلوكيات معينة)؛ ما ينطبق أي منها هنا.",
    "C": "لقاح <bdi>influenza</bdi> جرعة واحدة سنويًا بالبالغين؛ ما فيه \"<bdi>booster</bdi>\"، وأصلًا أخذه هذا الموسم قبل 6 أشهر.",
},
"AS-0106": {
    "B": "لقاح <bdi>hepatitis A</bdi> مرتبط بمجموعات خطورة محددة (سفر، مرض كبد، تعرّض معين)؛ <bdi>COPD</bdi> ليس مؤشر لهذا اللقاح.",
    "C": "لقاح <bdi>influenza</bdi> يُعطى جرعة واحدة كل موسم بالبالغين؛ ما فيه \"<bdi>booster</bdi>\"، و<bdi>COPD</bdi> يرفع أهمية اللقاح السنوي بس مو بشكل <bdi>booster</bdi>.",
},
"AS-0122": {
    "A": "<bdi>specificity</bdi> تعكس تحديد الأشخاص السليمين بدقة (قلة <bdi>false positives</bdi>)؛ هذا يُعطى الأولوية بفحوصات التأكيد، مو لرصد الحالات المفوَّتة.",
    "C": "<bdi>PPV</bdi> هو احتمال إصابة المريض فعليًا بعد نتيجة إيجابية، ويعتمد على <bdi>prevalence</bdi> وعادة ينخفض لما يُوسَّع الفحص لرصد حالات أكثر.",
    "D": "<bdi>NPV</bdi> يرتفع فعلًا لما تقل <bdi>false negatives</bdi>، بس يعتمد على <bdi>prevalence</bdi>؛ الخاصية الجوهرية اللي تُعرّف \"عدم فوات الحالات\" هي <bdi>sensitivity</bdi>.",
},
"AS-0316": {
    "B": "لقاح <bdi>hepatitis A</bdi> لمجموعات خطورة محددة؛ ما ينطبق منها شي هنا.",
    "C": "لقاح <bdi>influenza</bdi> جرعة سنوية واحدة بالبالغين؛ ما فيه \"<bdi>booster</bdi>\"، وأصلًا أخذه هذا الموسم.",
},
"AS-0361": {
    "A": "<bdi>specificity</bdi> تهم بالتأكيد وتجنب <bdi>false positives</bdi>، مو برصد الحالات المفوَّتة.",
    "C": "<bdi>PPV</bdi> يتأثر بـ<bdi>prevalence</bdi> وينخفض عادة عند توسيع الفحص.",
    "D": "<bdi>NPV</bdi> يرتفع بس مع تقليل <bdi>false negatives</bdi>، بس الخاصية الجوهرية المطلوبة هي <bdi>sensitivity</bdi>.",
},
"AS-0365": {
    "A": "15/1000 يساوي 1.5%، مو 15%؛ وعبارة \"يملكون المرض\" تصف <bdi>prevalence</bdi> (حالات موجودة) مو <bdi>incidence</bdi> (حالات جديدة).",
    "B": "أي رقم 15% يخطئ بموضع العلامة العشرية؛ 15 من 1000 تساوي 1.5%.",
    "C": "يحذف المقام؛ <bdi>incidence</bdi> بدون ذكر المجموعة المعرّضة للخطر (لكل 1000) ما يمكن تفسيرها أو تعميمها.",
},
"AS-0424": {
    "A": "2.5 ما ينتج من ضرب تقاطعي صحيح لهذي الأرقام بأي اتجاه.",
    "B": "4 هو احتمال <bdi>CS</bdi> بين مجموعة <bdi>controls</bdi> فقط (160/40)، مو نسبة تقارن <bdi>cases</bdi> بـ<bdi>controls</bdi>.",
    "C": "5 ما يطابق الضرب التقاطعي؛ حساب (a×d)/(b×c) يعطي 6 (أو مقلوبها 1/6)، مو 5.",
},
"AS-0445": {
    "A": "<bdi>efficiency</bdi> تعني تجنب هدر الموارد (معدات، وقت، مال)؛ قلق الطبيب هنا عن التزام المريض، مو عن هدر موارد.",
    "B": "<bdi>timeliness</bdi> تعني تقليل التأخير اللي يسببه النظام للمرضى؛ هنا الفجوة من فوات المريض لمواعيده، مو من تأخير بالخدمة.",
},
"AS-0478": {
    "B": "0.45% ما يُستخرج من أي استخدام صحيح لهذي الأرقام؛ إجمالي الحالات 375، مو 450، لكل 100,000.",
    "C": "الأرقام صحيحة بس الوحدة غلط: 375 لكل 100,000 تساوي 3.75 لكل 1000، مو 0.375 لكل 1000 (خطأ بمقدار عشرة أضعاف).",
    "D": "المقام والوحدة غلط معًا؛ 0.45 لكل 1000 يساوي 45 لكل 100,000.",
},
"AS-0478B": {
    "B": "0.375 لكل 1000 أصغر بألف مرة من الصحيح؛ 0.375 (كنسبة) تساوي 375 لكل 1000، مو 0.375 لكل 1000.",
    "C": "0.45 ما يُستخرج من 75/200؛ يحتاج 90 حالة من 200 (و75/100,000 تعطي 0.00075 مو 0.45).",
    "D": "قيمة وحدة خاطئتين معًا؛ لا 75/200 ولا 75/100,000 يعطي 0.45 لكل 1000.",
},
"AS-2460": {
    "A": "تستخدم \"U\" و\"OD\" معًا، وهما أشهر اختصارين ممنوعين بقائمة <bdi>do-not-use abbreviations</bdi>.",
    "B": "\"<bdi>unit</bdi>\" مكتوبة صحيح، بس \"OD\" ممكن تُقرأ خطأ كـ<bdi>right eye</bdi>؛ الصحيح كتابة \"<bdi>daily</bdi>\" كاملة.",
    "D": "تتجنب الاختصارات، بس كتابة الجرعة بالكلمات فقط مو المعيار بوصفة روتينية وممكن تُقرأ خطأ؛ الأفضل أرقام مع كتابة الوحدة كاملة.",
},
}

HIGHLIGHT_TERMS = {
"AS-2461": ["peanut allergy", "without the allergy being documented"],
"AS-2496": ["refuses the admission and asked to leave the hospital"],
"AS-2537": ["communication"],
"AS-0002": ["200 women", "180", "misses 20", "sensitivity"],
"AS-0007": ["low specificity", "over treatment"],
"AS-0105": ["50-year-old", "received the seasonal influenza vaccine 6 months ago"],
"AS-0106": ["50-Year-Old"],
"AS-0122": ["include the missed cases"],
"AS-0316": ["50-year-old", "received the seasonal influenza vaccine 6 months ago"],
"AS-0361": ["even include the missed cases"],
"AS-0365": ["1000 people for one year", "15 of them developed", "incidence"],
"AS-0424": ["case-control study", "80 were delivered by cesarean section and 120 by vaginal delivery", "160 were delivered by cesarean section and 40 by vaginal delivery", "odds ratio"],
"AS-0445": ["missed multiple appointments", "medical value"],
"AS-0478": ["100,000", "Existing cases: 300, New cases: 75", "cumulative prevalence"],
"AS-0478B": ["200 adult patients", "75 patients currently have migraine", "among these patients"],
"AS-2278": ["prescribe over the phone"],
"AS-2296": ["warfarin", "10 weeks pregnant"],
"AS-2301": ["DNR from other hospital"],
"AS-2302": ["transferred to another hospital"],
"AS-2303": ["muscular dystrophy", "transferred from one hospital to a tertiary hospital", "without knowing about a Do Not Resuscitate (DNR) order"],
"AS-2339": ["termination of pregnancy due to social issues", "viable baby at 14 weeks"],
"AS-2340": ["Dr is persuading her not to terminate due to personal belief"],
"AS-2341": ["fetal distress", "mother refuses the CS and requests a second opinion"],
"AS-2342": ["She Refuses The Procedure And Requests A Second Opinion"],
"AS-2343": ["elective C-section", "hesitant"],
"AS-2402": ["husband agrees", "she refuses"],
"AS-2403": ["ruptured ectopic pregnancy", "hypotensive and unconscious"],
"AS-2428": ["You Will Receive Standard Care"],
"AS-2443": ["opened the patient's file", "filed a complaint"],
"AS-2460": ["vitamin D", "best way to write the prescription"],
}
