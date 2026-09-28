# -*- coding: utf-8 -*-
# Explanations for questions 402-498 (topic: Cardiology)

TOPICS = {n: "Cardiology" for n in range(402, 499)}

EXPLANATIONS = {
402: {
    "idea": "السؤال يبي أثر جانبي حقيقي وموثق لدواء <bdi>furosemide</bdi> بمرضى <bdi>heart failure</bdi>، مو بس أشيع أثر معروف.",
    "clues": [
        ("furosemide", "مدر بولي من نوع <bdi>loop diuretic</bdi> مشتق من مركبات السلفا"),
        ("congestive heart failure", "السياق السريري المعتاد لاستخدام هالدواء"),
    ],
    "why_correct": [
        "بما إن <bdi>furosemide</bdi> مشتق من مجموعة السلفوناميد، فهو مسجل له أثر جانبي دموي نادر لكنه موثق وهو <bdi>haemolytic anaemia</bdi> بآلية مناعية.",
        "هالأثر أقل شيوعًا من نقص البوتاسيوم لكنه من الآثار المعترف فيها رسميًا بنشرة الدواء، وهذا هو المقصود بكلمة recognized بالسؤال.",
        "الخيارات الثانية مو من الآثار الموثقة لهالدواء بنفس الدرجة بهالسياق.",
    ],
    "when_changes": [
        "لو السؤال يبي أشيع أثر جانبي عمليًا (مو الأندر توثيقًا)، يصير نقص البوتاسيوم هو الأقرب.",
        "لو الـ<bdi>patient</bdi> عنده حساسية سلفا معروفة، يرتفع احتمال حدوث تفاعلات دموية مناعية زي هذي مع الـ<bdi>furosemide</bdi>.",
    ],
    "rule": "دايمًا تذكر إن <bdi>furosemide</bdi> مشتق سلفا وممكن يسبب تفاعلات دموية مناعية نادرة زي <bdi>haemolytic anaemia</bdi> إلى جانب أثره المعروف على البوتاسيوم.",
    "comparison": None,
    "guideline_note": None,
},
403: {
    "idea": "الـ<bdi>patient</bdi> عندها غثيان وألم بطن مع اضطراب بصري (اصفرار الرؤية)، وهذي <bdi>sign</bdi> كلاسيكية جدًا لتسمم <bdi>digoxin</bdi>.",
    "clues": [
        ("does not know her medications", "احتمال تناول دواء بجرعة زايدة بدون معرفة دقيقة"),
        ("vision has been slightly yellow tinged", "اضطراب رؤية الألوان (xanthopsia)، <bdi>sign</bdi> كلاسيكية لتسمم الـ<bdi>digoxin</bdi>"),
        ("Heart rate 60", "نبض بطيء نسبيًا، متوافق مع أثر الـ<bdi>digoxin</bdi> على القلب"),
    ],
    "why_correct": [
        "اصفرار الرؤية أو رؤية الألوان بشكل غير <bdi>normal</bdi> من أشهر الـ<bdi>signs</bdi> النوعية لتسمم <bdi>digoxin</bdi>.",
        "الغثيان وألم البطن من الـ<bdi>symptoms</bdi> الهضمية الشائعة بتسمم الـ<bdi>digoxin</bdi>، ومع بطء النبض النسبي تكتمل الصورة.",
        "ما فيه بالسؤال أي دليل تخطيط قلب يدعم احتشاء أو انخفاض حرارة يفسر الـ<bdi>symptoms</bdi>.",
    ],
    "when_changes": [
        "لو ظهر تخطيط قلب فيه رفع segment بالجدار الأمامي الوحشي، يصير الـ<bdi>diagnosis</bdi> احتشاء قلبي بدل تسمم دوائي.",
        "لو البوتاسيوم طلع <bdi>low</bdi> جدًا بالتحاليل بدون <bdi>symptoms</bdi> بصرية، يصير التركيز على نقص البوتاسيوم نفسه.",
    ],
    "rule": "اضطراب رؤية الألوان (اصفرار أو اخضرار الرؤية) <bdi>symptom</bdi> كلاسيكي يدل على تسمم <bdi>digoxin</bdi> ولازم يفكر فيه دايمًا.",
    "comparison": None,
    "guideline_note": None,
},
404: {
    "idea": "السؤال يبي دواء يتفاعل مع <bdi>adenosine</bdi> ويخلّي لازم تقليل جرعته عند إعطائه.",
    "clues": [
        ("regular narrow complex tachycardia", "نوع تسرع القلب اللي يستخدم فيه الأدينوسين"),
        ("IV adenosine", "الدواء المطلوب معرفة تفاعلاته"),
    ],
    "why_correct": [
        "<bdi>Dipyridamole</bdi> يمنع تكسير الأدينوسين بالجسم (يثبط إعادة امتصاصه الخلوي)، فيرفع تركيزه وتأثيره، فلازم تقليل الجرعة.",
        "استخدام الجرعة العادية مع وجود dipyridamole ممكن يسبب بطء قلب <bdi>severe</bdi> أو توقف مؤقت ب<bdi>cause</bdi> زيادة التأثير.",
        "باقي الخيارات ما تزيد تأثير الأدينوسين بنفس الآلية المباشرة.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> ياخذ theophylline بدل dipyridamole، الموضوع بالعكس تمامًا ويحتاج زيادة الجرعة لأنه يضاد تأثير الأدينوسين.",
        "لو فيه قصور كلوي <bdi>chronic</bdi> بس بدون دواء يتفاعل، ما يوجد <bdi>cause</bdi> مباشر لتغيير جرعة الأدينوسين لأجله.",
    ],
    "rule": "<bdi>Dipyridamole</bdi> يقوي تأثير <bdi>adenosine</bdi> ويحتاج تقليل الجرعة، بينما <bdi>theophylline</bdi> يضاده ويحتاج زيادتها.",
    "comparison": {
        "headers": ["الدواء", "تأثيره على الأدينوسين", "التعديل المطلوب"],
        "rows": [
            ["<bdi>Dipyridamole</bdi>", "يقوي تأثيره", "تقليل الجرعة"],
            ["<bdi>Theophylline</bdi>", "يضاد تأثيره", "زيادة الجرعة"],
        ],
    },
    "guideline_note": None,
},
405: {
    "idea": "السؤال يبي دواء من أدوية <bdi>heart failure</bdi> الـ<bdi>chronic</bdi> ثبت إنه يقلل الوفيات على المدى الطويل، مو بس يحسّن الـ<bdi>symptoms</bdi>.",
    "clues": [
        ("chronic heart failure", "السياق المرضي المطلوب"),
        ("increase survival", "يبي دواء يقلل الوفيات تحديدًا"),
    ],
    "why_correct": [
        "<bdi>Enalapril</bdi> من مثبطات <bdi>ACE</bdi> وثبتت بدراسات كبيرة (زي SOLVD) إنه يقلل الوفيات بمرضى <bdi>heart failure</bdi> الـ<bdi>chronic</bdi>.",
        "<bdi>Digoxin</bdi> يحسّن الـ<bdi>symptoms</bdi> ويقلل دخول المستشفى بس ما يثبت له أثر على تقليل الوفيات.",
        "<bdi>Furosemide</bdi> يخفف الـ<bdi>congestion</bdi> والـ<bdi>symptoms</bdi> بسرعة، لكنه <bdi>treatment</bdi> عرضي وما يقلل الوفيات على المدى البعيد.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> ما يتحمل مثبطات <bdi>ACE</bdi>، يصير <bdi>hydralazine</bdi> مع نترات بديل يقلل الوفيات أيضًا خصوصًا بمرضى معينين.",
        "لو السؤال يبي دواء يحسن الـ<bdi>symptoms</bdi> بس بدون أثر على البقاء، يصير الجواب <bdi>furosemide</bdi> أو <bdi>digoxin</bdi>.",
    ],
    "rule": "مثبطات <bdi>ACE</bdi> زي <bdi>enalapril</bdi> من الأدوية الأساسية اللي تقلل الوفيات ب<bdi>heart failure</bdi> الـ<bdi>chronic</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
406: {
    "idea": "رجل عنده حمى غير مفسرة بعد حمى روماتيزمية وخلع أسنان حديث، مع <bdi>murmur</bdi> قلبية وطحال متضخم وبول فيه دم مجهري، وهذي صورة كلاسيكية ل<bdi>infective endocarditis</bdi>.",
    "clues": [
        ("unexplained fever", "حمى مستمرة بدون <bdi>cause</bdi> واضح، من أهم <bdi>signs</bdi> <bdi>endocarditis</bdi>"),
        ("teeth have been extracted", "بوابة دخول للبكتيريا للدم (bacteremia) عند خلع الأسنان"),
        ("systolic murmur and splenomegaly", "<bdi>sign</bdi> إصابة صمام قلبي مع تضخم طحال، متوافق مع <bdi>endocarditis</bdi> تحت الـ<bdi>acute</bdi>"),
        ("Erythrocytes 25", "دم بالبول (بيلة دموية مجهرية) من <bdi>complications</bdi> <bdi>endocarditis</bdi> الكلوية"),
    ],
    "why_correct": [
        "الحمى المستمرة بعد <bdi>procedure</bdi> سني (خلع أسنان) مع <bdi>murmur</bdi> قلبية جديدة وطحال متضخم تطابق تمامًا صورة <bdi>infective endocarditis</bdi>.",
        "خلع الأسنان بوابة معروفة لدخول البكتيريا للدم خصوصًا لمن عنده صمام متضرر من الحمى الروماتيزمية السابقة.",
        "بيلة الدم المجهرية تدعم الانتشار الجهازي أو التهاب كبيبي مناعي المرتبط ب<bdi>endocarditis</bdi>.",
    ],
    "when_changes": [
        "لو الحمى ظهرت مباشرة بعد نوبة الروماتيزم القلبي بدون <bdi>procedure</bdi> سني، يصير احتمال تكرار الروماتيزم نفسه أقوى.",
        "لو فيه ألم صدري <bdi>acute</bdi> مع تغيرات تخطيط قلب واضحة، يتحول التركيز ل<bdi>myocardial infarction</bdi>.",
    ],
    "rule": "حمى مستمرة بعد <bdi>procedure</bdi> سني ب<bdi>patient</bdi> عنده صمام متضرر من قبل تدفعنا نفكر أول شي بـ<bdi>infective endocarditis</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
407: {
    "idea": "الألم الصدري تغيّر بطبيعته: صار أطول مدة وأشد ويحصل حتى بالراحة، وهذا يدل على تحوّله من ذبحة مستقرة إلى ذبحة غير مستقرة.",
    "clues": [
        ("become much worse over the last 3 weeks", "تغيّر حديث بنمط الذبحة يدل على عدم استقرارها"),
        ("occurs even while he is sitting in a chair or in bed", "الألم صار يحصل بالراحة، مو بس بالمجهود"),
    ],
    "why_correct": [
        "الذبحة غير المستقرة (<bdi>unstable angina</bdi>) تتميز بألم يحصل بالراحة أو يزداد شدته وتكراره ومدته حديثًا.",
        "وصف الألم بأنه أطول من قبل ويحصل بدون مجهود يستبعد الذبحة المستقرة (اللي ترتبط دايمًا بالمجهود فقط).",
        "ما فيه بالسؤال وصف لألم يحصل بأوقات محددة بالراحة بدون <bdi>cause</bdi> مع رفع segment عابر يميز <bdi>Prinzmetal angina</bdi>.",
    ],
    "when_changes": [
        "لو الألم يحصل فقط بالمجهود ويزول بالراحة بنفس الدرجة كل مرة، يصير الـ<bdi>diagnosis</bdi> ذبحة مستقرة (<bdi>exertional</bdi>).",
        "لو الألم يحصل بالراحة بأوقات محددة (غالبًا ليلًا) مع تشنج شرياني موثق، يصير الـ<bdi>diagnosis</bdi> <bdi>Prinzmetal angina</bdi>.",
    ],
    "rule": "أي <bdi>angina</bdi> تزيد بالشدة والمدة وتبدأ تحصل بالراحة تعتبر ذبحة غير مستقرة وتحتاج <bdi>assessment</bdi> عاجل.",
    "comparison": None,
    "guideline_note": None,
},
408: {
    "idea": "<bdi>patient</bdi> ضغطه غير مضبوط رغم جرعة كاملة من مدر بولي واحد، والسؤال يبي أفضل تعديل بالـ<bdi>treatment</bdi>.",
    "clues": [
        ("hydrochlorothiazide 25 mg/day", "<bdi>treatment</bdi> ضغط حالي بجرعة كاملة تقريبًا وما زال الضغط <bdi>elevated</bdi>"),
        ("Blood pressure 155/101", "ضغط غير مضبوط رغم الـ<bdi>treatment</bdi> الحالي"),
        ("Glucose, fasting 7.3", "سكر صائم <bdi>elevated</bdi> قليلًا، من الآثار الجانبية المعروفة لمدرات الثيازيد بجرعات عالية"),
    ],
    "why_correct": [
        "إضافة دواء من مجموعة ثانية (<bdi>ACE inhibitor</bdi>) أفضل من رفع جرعة نفس الدواء لأن رفع جرعة الثيازيد يزيد الآثار الجانبية الأيضية بدون فايدة إضافية كبيرة بالضغط.",
        "السكر الصائم الـ<bdi>elevated</bdi> بالفعل يدعم تجنّب زيادة جرعة الثيازيد لأنها تزيد سوء التحكم بالسكر أكثر.",
        "إضافة دواء من آلية مختلفة (مثبط ACE) يعطي تحكم أفضل بالضغط مع حماية إضافية كلوية وقلبية.",
    ],
    "when_changes": [
        "لو السكر والبوتاسيوم كانوا طبيعيين تمامًا، ممكن يفكر برفع جرعة الثيازيد كخيار مقبول أيضًا.",
        "لو الـ<bdi>patient</bdi> عنده قصور كلوي واضح، يفضّل تجنّب مثبطات ACE بالبداية والانتقال لخيار ثاني بحذر مع <bdi>follow-up</bdi> الكرياتينين.",
    ],
    "rule": "لما يفشل دواء ضغط واحد بجرعة كافية، الأفضل إضافة دواء من آلية مختلفة مو رفع جرعة نفس الدواء.",
    "comparison": None,
    "guideline_note": None,
},
409: {
    "idea": "مدمن مخدرات وريدي عنده حمى و<bdi>symptoms</bdi> جهازية مع <bdi>signs</bdi> جلدية وعينية كلاسيكية (آفات جانواي، بقع روث، نزيف تحت الأظافر)، وهذي صورة <bdi>infective endocarditis</bdi>.",
    "clues": [
        ("intravenous drug user", "<bdi>factor</bdi> <bdi>risk</bdi> رئيسي ل<bdi>endocarditis</bdi> بالصمام الثلاثي غالبًا"),
        ("painless erythematous lesions noted on the palms", "آفات جانواي (Janeway lesions)، <bdi>sign</bdi> جلدية ل<bdi>endocarditis</bdi>"),
        ("round erythematous lesions and central clearing noted in the retina", "بقع روث (Roth spots) بالشبكية"),
        ("splinter haemorrhage under the fingernails", "نزيف خطي تحت الأظافر، <bdi>sign</bdi> كلاسيكية ثالثة ل<bdi>endocarditis</bdi>"),
    ],
    "why_correct": [
        "تجمع الحمى وتعاطي المخدرات الوريدي مع ثلاث <bdi>signs</bdi> كلاسيكية (جانواي، روث سبوتس، نزيف تحت الأظافر) يشخص <bdi>infective endocarditis</bdi> بشكل شبه مؤكد.",
        "استخدام المخدرات الوريدي <bdi>factor</bdi> <bdi>risk</bdi> رئيسي لدخول البكتيريا للدم مباشرة وإصابة صمامات القلب.",
        "باقي الـ<bdi>diseases</bdi> المذكورة ما تفسر هالتجمع الكامل من الـ<bdi>signs</bdi> الجلدية والعينية معًا.",
    ],
    "when_changes": [
        "لو كانت الآفات الجلدية مؤلمة بدل غير مؤلمة، يصير التفكير بـ Osler nodes بدل جانواي، لكن الـ<bdi>diagnosis</bdi> العام يبقى نفسه.",
        "لو ما فيه تاريخ تعاطي مخدرات وريدي وكانت الـ<bdi>symptoms</bdi> أكثر تناسلية، يصير التركيز على الزهري.",
    ],
    "rule": "متعاطي المخدرات الوريدي مع حمى و<bdi>signs</bdi> جلدية-عينية كلاسيكية يدفعنا مباشرة للتفكير بـ<bdi>infective endocarditis</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
410: {
    "idea": "السؤال يبي دواء ثبت أنه يقلل الوفيات بمرضى <bdi>congestive heart failure</bdi>، وحسب مفتاح إجابة هالملف الجواب المعتمد هو <bdi>furosemide</bdi>.",
    "clues": [
        ("congestive heart failure", "السياق المرضي المطلوب"),
        ("reduce mortality", "يبي دواء يقلل الوفيات تحديدًا مو بس الـ<bdi>symptoms</bdi>"),
    ],
    "why_correct": [
        "بحسب الإجابة المعتمدة بهالملف، <bdi>furosemide</bdi> هو الخيار المطلوب هنا كمدر بولي أساسي ب<bdi>treatment</bdi> <bdi>congestive heart failure</bdi>.",
        "<bdi>Digitalis</bdi> يحسّن الـ<bdi>symptoms</bdi> ويقلل دخول المستشفى بس بدون إثبات واضح لتقليل الوفيات.",
        "<bdi>Procainamide</bdi> دواء ل<bdi>treatment</bdi> اضطراب النظم مو ل<bdi>treatment</bdi> <bdi>heart failure</bdi> أصلًا، فهو بعيد عن السياق تمامًا.",
    ],
    "when_changes": [
        "لو السؤال يذكر مثبط <bdi>ACE</bdi> زي enalapril ضمن الخيارات، فهو الدواء اللي أثبتته الدراسات الكبرى (SOLVD) بتقليل الوفيات فعليًا.",
        "لو الهدف تحسين الـ<bdi>symptoms</bdi> والـ<bdi>congestion</bdi> بسرعة بدون التركيز على البقاء طويل المدى، يبقى المدر البولي الخيار العملي الأول.",
    ],
    "rule": "لاحظ إن الدليل الطبي الراسخ يثبت مثبطات <bdi>ACE</bdi> (زي enalapril) هي من تقلل الوفيات ب<bdi>heart failure</bdi> الـ<bdi>chronic</bdi> على المدى الطويل.",
    "comparison": None,
    "guideline_note": "الدليل الطبي الراسخ من دراسات كبرى مثل SOLVD يثبت إن مثبطات <bdi>ACE</bdi> هي من تقلل الوفيات ب<bdi>heart failure</bdi> الـ<bdi>chronic</bdi>، بينما <bdi>furosemide</bdi> <bdi>treatment</bdi> عرضي لل<bdi>congestion</bdi> بدون إثبات لتقليل الوفيات؛ ومع ذلك الجواب المعتمد على البطاقة هنا يبقى حسب مفتاح هالملف.",
},
411: {
    "idea": "نفس فكرة السؤال 402: يبي أثر جانبي حقيقي وموثق لدواء <bdi>furosemide</bdi> بمرضى <bdi>heart failure</bdi>.",
    "clues": [
        ("furosemide", "مدر بولي من نوع <bdi>loop diuretic</bdi> مشتق من مركبات السلفا"),
        ("congestive heart failure", "السياق السريري المعتاد لاستخدام هالدواء"),
    ],
    "why_correct": [
        "بما إن <bdi>furosemide</bdi> مشتق سلفوناميد، فهو مسجل له أثر جانبي دموي نادر لكنه موثق وهو <bdi>haemolytic anaemia</bdi> بآلية مناعية.",
        "هالأثر مذكور رسميًا بنشرة الدواء ضمن التفاعلات الدموية النادرة المرتبطة بمشتقات السلفا.",
        "باقي الخيارات مو من الآثار الموثقة رسميًا لهالدواء بنفس الدرجة بهالسياق.",
    ],
    "when_changes": [
        "لو السؤال يبي أشيع أثر جانبي عمليًا بدل الأندر توثيقًا، يصير نقص البوتاسيوم هو الأقرب.",
        "لو الـ<bdi>patient</bdi> عنده حساسية سلفا موثقة، يرتفع احتمال حدوث تفاعل دموي مناعي زي هذا مع الـ<bdi>furosemide</bdi>.",
    ],
    "rule": "تذكر إن <bdi>furosemide</bdi> مشتق سلفا وممكن يسبب تفاعلات دموية مناعية نادرة زي <bdi>haemolytic anaemia</bdi> بجانب أثره المعروف على البوتاسيوم.",
    "comparison": None,
    "guideline_note": None,
},
412: {
    "idea": "<bdi>patient</bdi> تسمم بجرعة زايدة من <bdi>atenolol</bdi> (حاصر بيتا) وصار عنده بطء قلب وهبوط ضغط <bdi>severe</bdi>، والسؤال يبي أفضل ترياق إضافي.",
    "clues": [
        ("accidental ingestion of a higher dose of atenolol", "تسمم بحاصر بيتا هو <bdi>cause</bdi> الـ<bdi>case</bdi>"),
        ("Heart rate 46", "بطء قلب <bdi>severe</bdi> ناتج عن <bdi>block</bdi> مستقبلات بيتا"),
        ("Blood pressure 70/40", "هبوط ضغط <bdi>severe</bdi> مصاحب للتسمم"),
    ],
    "why_correct": [
        "<bdi>Glucagon</bdi> هو الترياق النوعي لتسمم حاصرات بيتا لأنه يرفع cAMP داخل خلايا القلب بآلية مستقلة عن مستقبلات بيتا، فيرجع قوة وسرعة انقباض القلب.",
        "هالآلية البديلة مهمة جدًا لأن مستقبلات بيتا نفسها محصورة بالدواء، فأي <bdi>treatment</bdi> يعتمد عليها ما يفيد بنفس الدرجة.",
        "السوائل الوريدية وحدها ما تكفي لتصحيح بطء القلب وهبوط الانقباض الناتج عن <bdi>block</bdi> بيتا الـ<bdi>severe</bdi>.",
    ],
    "when_changes": [
        "لو التسمم كان بحاصرات قنوات الكالسيوم بدل بيتا، يصير الترياق الأساسي كالسيوم وريدي أو <bdi>insulin</bdi> بجرعات عالية.",
        "لو ما استجاب الـ<bdi>patient</bdi> على الجلوكاجون، الـ<bdi>step</bdi> التالية تصير منشطات قلبية أو منظم ضربات مؤقت.",
    ],
    "rule": "<bdi>Glucagon</bdi> هو الترياق النوعي لتسمم حاصرات بيتا لأنه يرفع قوة القلب بآلية لا تعتمد على مستقبلات بيتا.",
    "comparison": None,
    "guideline_note": None,
},
413: {
    "idea": "<bdi>patient</bdi> ذبحة مستقرة ما زال يعاني من الألم رغم <bdi>treatment</bdi> مضاد للصفائح و<bdi>statin</bdi> ونترات، والسؤال يبي أفضل دواء إضافي يناسب حالته الوعائية المصاحبة.",
    "clues": [
        ("intermittent claudication", "<bdi>disease</bdi> شرايين طرفية مصاحب، <bdi>factor</bdi> مهم بالاختيار"),
        ("still gets angina with moderate exercise", "الذبحة ما زالت غير مسيطر عليها رغم الـ<bdi>treatment</bdi> الحالي"),
    ],
    "why_correct": [
        "<bdi>Diltiazem</bdi> حاصر قنوات كالسيوم غير <bdi>bilateral</bdi> هيدروبيريدين، مناسب ل<bdi>treatment</bdi> الذبحة الإضافي بدون الأثر السلبي لحاصرات بيتا على الدورة الطرفية.",
        "حاصرات البيتا (زي <bdi>metoprolol</bdi>) ممكن تزيد سوء <bdi>symptoms</bdi> العرج المتقطع لأنها تقلل تروية العضلات الطرفية أثناء المجهود.",
        "<bdi>Diltiazem</bdi> يعطي تأثير مشابه بتقليل الطلب على الأكسجين للقلب بدون هالمشكلة الطرفية.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> ما عنده <bdi>disease</bdi> شرايين طرفية أصلًا، يصير حاصر بيتا زي metoprolol خيار أول مقبول ل<bdi>treatment</bdi> الذبحة.",
        "لو عنده انخفاض <bdi>severe</bdi> بوظيفة البطين الأيسر، يفضّل تجنّب diltiazem لأنه يضعف انقباض القلب أكثر.",
    ],
    "rule": "بمرضى الذبحة اللي عندهم أيضًا <bdi>disease</bdi> شرايين طرفية، حاصرات قنوات الكالسيوم غير <bdi>bilateral</bdi> الهيدروبيريدين (زي diltiazem) أفضل من حاصرات البيتا.",
    "comparison": {
        "headers": ["الدواء", "أثره على العرج المتقطع"],
        "rows": [
            ["<bdi>Diltiazem</bdi>", "آمن، لا يسوء الدورة الطرفية"],
            ["<bdi>Metoprolol</bdi>", "قد يسوء <bdi>symptoms</bdi> العرج المتقطع"],
        ],
    },
    "guideline_note": None,
},
414: {
    "idea": "شابة صحيحة عندها <bdi>palpitations</bdi> مفاجئ وتسرع قلب منتظم وسريع (150) مع ضغط مستقر نسبيًا، وهذا يوجه لتسرع قلب فوق بطيني، والـ<bdi>step</bdi> الأولى <bdi>procedures</bdi> بسيطة قبل الأدوية.",
    "clues": [
        ("palpitations for 2-hours", "بداية مفاجئة ل<bdi>palpitations</bdi>، يوجه لتسرع قلب فوق بطيني نوبي"),
        ("Heart rate 150", "تسرع قلب منتظم وسريع"),
        ("Blood pressure 135/80", "استقرار الدورة الدموية رغم التسرع"),
        ("Thyroid-Stimulating Hormone 3.2", "<bdi>normal</bdi>، يستبعد <bdi>hyperthyroidism</bdi> ك<bdi>cause</bdi>"),
    ],
    "why_correct": [
        "الـ<bdi>patient</bdi> مستقرة الدورة الدموية، فالـ<bdi>step</bdi> الأولى المناسبة هي <bdi>procedure</bdi> غير دوائي بسيط زي <bdi>carotid sinus massage</bdi> (مناورة مبهمية) قبل أي دواء.",
        "هالمناورة ممكن توقف تسرع القلب فوق البطيني نفسه بدون أي عقار، وهي آمنة وسريعة ب<bdi>patient</bdi> مستقرة.",
        "الأدينوسين الوريدي أو تقويم النظم الكهربائي يستخدمون لو فشلت المناورات المبهمية أو صارت الـ<bdi>patient</bdi> غير مستقرة.",
    ],
    "when_changes": [
        "لو فشلت مناورة carotid sinus massage بإيقاف التسرع، الـ<bdi>step</bdi> التالية تصير <bdi>IV adenosine</bdi>.",
        "لو صارت الـ<bdi>patient</bdi> غير مستقرة (هبوط ضغط <bdi>severe</bdi> أو فقدان وعي)، يصير تقويم النظم الكهربائي الفوري هو الخيار الصحيح.",
    ],
    "rule": "بتسرع القلب فوق البطيني ب<bdi>patient</bdi> مستقر، أول <bdi>step</bdi> مناورات مبهمية بسيطة زي carotid sinus massage قبل أي دواء.",
    "comparison": None,
    "guideline_note": None,
},
415: {
    "idea": "<bdi>patient</bdi> احتشاء قلبي معالج بالتحلل الخثري (streptokinase) صار عنده نزيف هضمي <bdi>severe</bdi>، والسؤال يبي دواء يوقف تأثير التحلل الخثري.",
    "clues": [
        ("streptokinase infusion", "الدواء المسبب ل<bdi>case</bdi> النزيف الحالية"),
        ("massive hematemesis", "نزيف هضمي <bdi>severe</bdi> يحتاج عكس تأثير الدواء المحلل لل<bdi>thrombus</bdi> بسرعة"),
    ],
    "why_correct": [
        "<bdi>Aminocaproic acid</bdi> دواء مضاد لانحلال الفيبرين، يعكس مباشرة تأثير الأدوية المحللة لل<bdi>thrombus</bdi> زي streptokinase.",
        "استخدامه بحالات النزيف الـ<bdi>severe</bdi> بعد التحلل الخثري يوقف استمرار تكسير الخثرات ويساعد بالسيطرة على النزيف.",
        "باقي الخيارات ترياقات لأدوية ثانية (فيتامين K لمضادات فيتامين K، بروتامين لل<bdi>heparin</bdi>، <bdi>factor</bdi> ثامن للهيموفيليا) وما لها علاقة بعكس تأثير التحلل الخثري.",
    ],
    "when_changes": [
        "لو النزيف ب<bdi>cause</bdi> جرعة زايدة من الـ<bdi>heparin</bdi>، يصير الترياق المناسب <bdi>protamine sulfate</bdi> بدل aminocaproic acid.",
        "لو النزيف ب<bdi>cause</bdi> مضاد فيتامين K (<bdi>warfarin</bdi>)، يصير الترياق <bdi>vitamin K</bdi> مع مركزات <bdi>factor</bdi> التخثر عند الحاجة.",
    ],
    "rule": "<bdi>Aminocaproic acid</bdi> هو الترياق النوعي لعكس تأثير الأدوية المحللة لل<bdi>thrombus</bdi> مثل streptokinase عند حدوث نزيف <bdi>severe</bdi>.",
    "comparison": {
        "headers": ["الدواء المسبب", "الترياق المناسب"],
        "rows": [
            ["<bdi>Streptokinase</bdi> / محللات الـ<bdi>thrombus</bdi>", "<bdi>Aminocaproic acid</bdi>"],
            ["<bdi>Heparin</bdi>", "<bdi>Protamine</bdi>"],
            ["<bdi>Warfarin</bdi>", "<bdi>Vitamin K</bdi>"],
        ],
    },
    "guideline_note": None,
},
416: {
    "idea": "السؤال يبي طريقة صحيحة وأخلاقية بتوعية <bdi>patient</bdi> احتشاء قلبي رافض للإقلاع عن التدخين، بدون تهديد أو إجبار.",
    "clues": [
        ("advised to quit smoking", "الـ<bdi>patient</bdi> بحاجة توعية صحية عن التدخين"),
        ("unwilling to do so", "الـ<bdi>patient</bdi> رافض حاليًا، يحتاج أسلوب توعوي مو إجباري"),
    ],
    "why_correct": [
        "أفضل أسلوب طبي هو إعطاء معلومة صحية موضوعية عن العواقب الطبية الحقيقية (زيادة <bdi>risk</bdi> الـ<bdi>complications</bdi>) بدون تهديد مباشر أو إلقاء لوم.",
        "هالأسلوب يحترم استقلالية الـ<bdi>patient</bdi> بقراره ويعطيه معلومة واقعية تساعده يقرر بنفسه لاحقًا.",
        "التهديد المباشر بالموت أو وصفه بعدم التعاون أساليب تكسر الثقة بين الطبيب والـ<bdi>patient</bdi> ونادرًا ما تنجح بتغيير السلوك.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> كان متردد بس متقبل للنقاش، ممكن نضيف نصيحة بإشراك الأسرة كدعم إضافي، مو كأسلوب أساسي بديل.",
        "لو الـ<bdi>patient</bdi> عنده استعداد فعلي للتغيير، الـ<bdi>step</bdi> التالية تصير تحويله لبرنامج دعم للإقلاع عن التدخين.",
    ],
    "rule": "بتوعية الـ<bdi>patient</bdi> عن عادة ضارة، أفضل أسلوب إعطاء معلومة طبية واقعية عن المخاطر بدون تهديد أو إلقاء لوم.",
    "comparison": None,
    "guideline_note": None,
},
417: {
    "idea": "<bdi>patient</bdi> احتشاء قلبي غير معقد راح يطلع من المستشفى، والسؤال يبي النصيحة الصحيحة عن نمط الحياة والنشاط اليومي بعد الخروج.",
    "clues": [
        ("7-day admission for acute myocardial infarction", "دخول قياسي بدون <bdi>complications</bdi> كبيرة مذكورة"),
        ("given 5 different drugs", "<bdi>treatment</bdi> دوائي قياسي بعد الاحتشاء، يدعم استقرار حالته"),
    ],
    "why_correct": [
        "بعد احتشاء قلبي غير معقد، ينصح الـ<bdi>patient</bdi> يبدأ تمارين هوائية <bdi>mild</bdi> (زي المشي) بشكل تدريجي من الأسبوع الأول تقريبًا لتحسين اللياقة القلبية.",
        "النشاط الـ<bdi>mild</bdi> المبكر آمن ويساعد بالتعافي، بعكس الراحة التامة الطويلة اللي تزيد <bdi>risk</bdi> ضعف اللياقة والجلطات.",
        "قيادة السيارة بعد يومين فقط والامتناع عن النشاط الجنسي لمدة 3 أشهر توصيات أشد من اللازم ومو مبنية على إرشادات التعافي القياسية.",
    ],
    "when_changes": [
        "لو الاحتشاء كان معقدًا بقصور قلب أو اضطراب نظم خطير، تطول فترة الراحة قبل السماح بالتمارين وقيادة السيارة.",
        "لو الـ<bdi>patient</bdi> يشتغل بوظيفة تتطلب مجهود بدني عالي جدًا، ممكن ينصح بتعديل مؤقت بمهام العمل، مو تغيير الوظيفة كليًا.",
    ],
    "rule": "بعد احتشاء قلبي غير معقد، يبدأ الـ<bdi>patient</bdi> تمارين هوائية <bdi>mild</bdi> تدريجيًا خلال أسبوع تقريبًا كجزء من إعادة التأهيل القلبي.",
    "comparison": None,
    "guideline_note": None,
},
418: {
    "idea": "<bdi>patient</bdi> قصور قلب متقدم مرشح لزراعة قلب، والسؤال يبي الأسلوب الصحيح لإخباره بخبر صعب زي هذا (breaking bad news).",
    "clues": [
        ("5th time during the past 2 months", "دخول متكرر يدل على شدة وتدهور الـ<bdi>case</bdi>"),
        ("refractory heart failure", "فشل الاستجابة لل<bdi>treatment</bdi> المعتاد، <bdi>cause</bdi> النظر بزراعة القلب"),
        ("After setting the scene, how would you break the news", "السؤال محدد عن طريقة إيصال الخبر"),
    ],
    "why_correct": [
        "الأسلوب الصحيح بإيصال خبر صعب هو إعطاء تحذير تمهيدي (warning shot) ثم إيصال المعلومة تدريجيًا بخطوات صغيرة يتحملها الـ<bdi>patient</bdi>.",
        "هالطريقة تعطي الـ<bdi>patient</bdi> وقت يستوعب ويهيأ نفسيًا قبل التفاصيل الكاملة، وتقلل الصدمة النفسية.",
        "إخباره مباشرة بدون تمهيد أو تجاوز مشاعره يعتبر أسلوب غير مناسب بالتواصل الطبي الحساس.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> نفسه طلب صراحة معرفة كل التفاصيل مباشرة وبسرعة، ممكن نعدل الأسلوب حسب رغبته الصريحة.",
        "بعد إيصال الخبر بالتدريج، لازم نتعامل مع مخاوفه ونعبر عن التعاطف ك<bdi>step</bdi> تالية مكملة مو بديلة.",
    ],
    "rule": "بإيصال خبر طبي صعب، الأسلوب الصحيح دايمًا تمهيد (warning shot) ثم إعطاء المعلومة تدريجيًا بخطوات صغيرة.",
    "comparison": None,
    "guideline_note": None,
},
419: {
    "idea": "<bdi>patient</bdi> التهاب شغاف على مضاد حيوي، والسؤال يبي أبسط طريقة ل<bdi>follow-up</bdi> استجابته لل<bdi>treatment</bdi>، مو أدق طريقة تشخيصية.",
    "clues": [
        ("infective endocarditis started on antibiotics", "السياق العلاجي المطلوب متابعته"),
        ("simplest way in monitoring antibiotics response", "يبي الطريقة الأبسط تحديدًا مو الأشمل"),
    ],
    "why_correct": [
        "<bdi>Serum C-reactive protein</bdi> فحص دم بسيط وسريع وغير مكلف، وانخفاضه التدريجي يعكس استجابة الالتهاب لل<bdi>treatment</bdi> بشكل عملي.",
        "هالفحص يمكن إعادته بسهولة كل يوم أو كل يومين ل<bdi>follow-up</bdi> الاتجاه العام للاستجابة دون تعقيد.",
        "مزرعة الدم والـ<bdi>echo</bdi> المتكرر فحوصات أدق بس أعقد وأبطأ وأغلى، مو الخيار الأبسط لل<bdi>follow-up</bdi> الروتينية.",
    ],
    "when_changes": [
        "لو الهدف تأكيد زوال البكتيريا من الدم فعليًا مو مجرد <bdi>follow-up</bdi> الالتهاب، يصير Blood culture متكرر هو الأنسب.",
        "لو فيه اشتباه ب<bdi>complication</bdi> تشريحية زي خراج بالصمام، يصير Serial echocardiography ضروري رغم تعقيده.",
    ],
    "rule": "ل<bdi>follow-up</bdi> استجابة الـ<bdi>treatment</bdi> ب<bdi>endocarditis</bdi> بأبسط طريقة عملية، <bdi>CRP</bdi> المتسلسل خيار سريع وموثوق ل<bdi>follow-up</bdi> اتجاه الالتهاب.",
    "comparison": None,
    "guideline_note": None,
},
420: {
    "idea": "<bdi>patient</bdi> احتشاء سفلي معالج بالتحلل الخثري صار عنده <bdi>block</bdi> قلبي من الدرجة الثانية (2:1) مع هبوط ضغط <bdi>severe</bdi> وبطء قلب ما استجاب للأتروبين، فيحتاج تدخل ميكانيكي فوري.",
    "clues": [
        ("2:1 AV block", "<bdi>block</bdi> قلبي يمنع وصول نبضات كافية للبطينين"),
        ("IV atropine given with no effect", "فشل الـ<bdi>treatment</bdi> الدوائي الأولي بتحسين النبض"),
        ("Blood pressure 80/45", "هبوط ضغط <bdi>severe</bdi> يهدد استقرار الـ<bdi>patient</bdi>"),
    ],
    "why_correct": [
        "لما يفشل الأتروبين بتحسين <bdi>block</bdi> قلبي مصحوب بعدم استقرار الدورة الدموية، الـ<bdi>step</bdi> التالية المناسبة هي <bdi>temporary pacemaker</bdi> لتثبيت النبض فورًا.",
        "منظم الضربات المؤقت يعطي تحكم مباشر وموثوق بمعدل ضربات القلب بعكس الأدوية اللي قد تكون غير كافية أو لها <bdi>symptoms</bdi> جانبية.",
        "الأدوية الوريدية زي الـ<bdi>dopamine</bdi> أو الإيزوبرينالين ممكن تستخدم كجسر مؤقت لحين تركيب المنظم، لكنها مو الحل النهائي المطلوب هنا.",
    ],
    "when_changes": [
        "لو استجاب الـ<bdi>patient</bdi> جيدًا على الأتروبين وتحسن الضغط والنبض، ما يحتاج ننتقل مباشرة لمنظم ضربات.",
        "لو الـ<bdi>block</bdi> كان من الدرجة الأولى البسيطة بدون <bdi>symptoms</bdi>، الـ<bdi>follow-up</bdi> وحدها كافية بدون أي تدخل.",
    ],
    "rule": "<bdi>block</bdi> قلبي مصحوب بعدم استقرار الدورة الدموية وما استجاب على الأتروبين يحتاج <bdi>temporary pacemaker</bdi> بأسرع وقت.",
    "comparison": None,
    "guideline_note": None,
},
421: {
    "idea": "نفس سيناريو <bdi>patient</bdi> الاحتشاء السفلي المعالج بالتحلل الخثري وصار عنده دوخة وبطء قلب <bdi>severe</bdi>، والسؤال هنا يبي تحديد نوع الـ<bdi>block</bdi> القلبي بالضبط من صورة تخطيط القلب.",
    "clues": [
        ("inferior MI and received thromolytic therapy", "احتشاء سفلي، منطقة معروفة بارتباطها بحصارات العقدة الأذينية البطينية"),
        ("Heart rate 41", "بطء قلب <bdi>severe</bdi> يدل على درجة <bdi>block</bdi> عالية"),
        ("ECG is done (see image)", "الـ<bdi>diagnosis</bdi> يعتمد على قراءة الصورة المرفقة بالسؤال"),
    ],
    "why_correct": [
        "احتشاء الجدار السفلي يرتبط بشكل مباشر بإصابة الشريان التاجي الأيمن اللي يغذي العقدة الأذينية البطينية، فيسبب غالبًا <bdi>block</bdi> من الدرجة الثانية.",
        "درجة البطء الـ<bdi>severe</bdi> بالنبض (41) مع الصورة المرفقة تدعم <bdi>diagnosis</bdi> <bdi>block</bdi> درجة ثانية أكثر من <bdi>block</bdi> <bdi>mild</bdi> من الدرجة الأولى.",
        "لا يوجد تصنيف طبي معترف به باسم 'الدرجة الرابعة' ل<bdi>block</bdi> القلب، فهذا الخيار غير حقيقي أصلًا.",
    ],
    "when_changes": [
        "لو التخطيط أظهر تطاول بسيط بالـPR فقط بدون سقوط أي نبضة، يصير الـ<bdi>diagnosis</bdi> <bdi>block</bdi> من الدرجة الأولى.",
        "لو ما فيه أي علاقة بين موجات P والمركبات البطينية إطلاقًا، يصير الـ<bdi>diagnosis</bdi> <bdi>block</bdi> كامل من الدرجة الثالثة.",
    ],
    "rule": "احتشاء الجدار السفلي من أشهر <bdi>causes</bdi> <bdi>block</bdi> العقدة الأذينية البطينية من الدرجة الثانية ب<bdi>cause</bdi> قرب الشريان التاجي الأيمن من العقدة.",
    "comparison": None,
    "guideline_note": None,
},
422: {
    "idea": "<bdi>patient</bdi> عندها <bdi>mitral stenosis</bdi> مع ارتفاع ضغط رئوي وتخطط للحمل بدون علم زوجها، والسؤال يبي الأسلوب الأخلاقي الصحيح بالتعامل مع رغبتها بالحمل رغم الخطورة.",
    "clues": [
        ("mitral stenosis with pulmonary hypertension", "<bdi>case</bdi> قلبية عالية الخطورة أثناء الحمل"),
        ("planning to get pregnant", "قرار مهم يحتاج معلومات كافية قبل اتخاذه"),
        ("hiding the diagnosis from her husband", "قرار سري يخص الـ<bdi>patient</bdi> وحدها من ناحية الخصوصية الطبية"),
    ],
    "why_correct": [
        "الأسلوب الصحيح هو توعية الـ<bdi>patient</bdi> نفسها عن الخطورة الحقيقية للحمل بحالتها (زيادة <bdi>risk</bdi> <bdi>heart failure</bdi> والوفاة) قبل أي قرار.",
        "احترام خصوصية الـ<bdi>patient</bdi> يمنعنا من مخاطبة الزوج مباشرة بدون إذنها، فهذا انتهاك لسرية المعلومات الطبية.",
        "مجرد الـ<bdi>follow-up</bdi> بدون توعية واضحة عن المخاطر ما يكفي ل<bdi>patient</bdi> ب<bdi>case</bdi> عالية الخطورة تخطط لقرار مصيري كالحمل.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> نفسها طلبت إشراك زوجها بالمعلومات، يصير التواصل معه بموافقتها مقبول ومناسب.",
        "لو كانت حالتها القلبية بسيطة بدون ارتفاع ضغط رئوي، تقل درجة الخطورة وتصير الاستشارة أخف حدة.",
    ],
    "rule": "بأي قرار طبي مصيري كالحمل مع <bdi>disease</bdi> قلبي خطير، الأولوية توعية الـ<bdi>patient</bdi> نفسها بالمخاطر مع الحفاظ على سرية معلوماتها.",
    "comparison": None,
    "guideline_note": None,
},
423: {
    "idea": "<bdi>patient</bdi> عنده <bdi>signs</bdi> قصور قلب مع نبض مرتد (collapsing pulse) وفرق ضغط واسع و<bdi>murmur</bdi> انبساطية مبكرة وصوت طلقة مسدس بالفخذ، وهذي صورة كلاسيكية جدًا ل<bdi>aortic regurgitation</bdi>.",
    "clues": [
        ("collapsing pulse and wide pulse pressure", "<bdi>signs</bdi> كلاسيكية ل<bdi>aortic regurgitation</bdi> الـ<bdi>chronic</bdi>"),
        ("Early diastolic murmur over left sternal border", "<bdi>murmur</bdi> انبساطية مبكرة، موقعها النموذجي ل<bdi>aortic regurgitation</bdi>"),
        ("pistol-shot sound heard over femoral arteries", "<bdi>sign</bdi> Traube's sign الكلاسيكية ل<bdi>aortic regurgitation</bdi> الـ<bdi>severe</bdi>"),
    ],
    "why_correct": [
        "الـ<bdi>murmur</bdi> الانبساطية المبكرة عند الحافة القصية اليسرى هي الـ<bdi>sign</bdi> السمعية المميزة لـ<bdi>aortic regurgitation</bdi>.",
        "النبض المرتد وفرق الضغط الواسع وصوت طلقة المسدس بالفخذ كلها <bdi>signs</bdi> محيطية كلاسيكية مصاحبة ل<bdi>aortic regurgitation</bdi> الـ<bdi>chronic</bdi>.",
        "<bdi>symptoms</bdi> <bdi>heart failure</bdi> (ضيق نفس واستلقاء ونوبات ليلية) تتوافق مع حمل حجمي <bdi>chronic</bdi> على البطين الأيسر ب<bdi>cause</bdi> الـ<bdi>aortic regurgitation</bdi>.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>murmur</bdi> انقباضية <bdi>severe</bdi> تنتقل للرقبة مع نبض بطيء الارتفاع، يصير الـ<bdi>diagnosis</bdi> <bdi>aortic stenosis</bdi> بدل قصوره.",
        "لو ظهر فرق ضغط بين الذراعين مع <bdi>murmur</bdi> انقباضية بالظهر، يصير التفكير بتضيق برزخ الأبهر أقوى.",
    ],
    "rule": "النبض المرتد وفرق الضغط الواسع مع <bdi>murmur</bdi> انبساطية مبكرة عند الحافة القصية اليسرى تشخص <bdi>aortic regurgitation</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
424: {
    "idea": "<bdi>patient</bdi> ضغط على مثبط ACE (captopril) وظهرت له موجات T مدببة عالية بتخطيط القلب، وهذا يوجه مباشرة لاحتمال فرط بوتاسيوم الدم كأثر جانبي معروف للدواء.",
    "clues": [
        ("hypertensive and on captopril", "مثبطات ACE من أشهر <bdi>causes</bdi> رفع البوتاسيوم دوائيًا"),
        ("tall, tented T waves", "<bdi>sign</bdi> تخطيط قلب كلاسيكية لفرط بوتاسيوم الدم"),
    ],
    "why_correct": [
        "الموجات T المدببة والعالية <bdi>sign</bdi> تخطيط قلب كلاسيكية مبكرة لفرط بوتاسيوم الدم، ولازم تأكيدها بفحص مستوى البوتاسيوم فورًا.",
        "مثبطات ACE زي captopril تقلل إفراز البوتاسيوم بالكلى وترفع مستواه بالدم، وهذا يفسر التغير بتخطيط القلب.",
        "قبل أي تدخل ثاني، لازم نتأكد من مستوى البوتاسيوم الفعلي لأنه الـ<bdi>treatment</bdi> بعدها يعتمد مباشرة عليه.",
    ],
    "when_changes": [
        "لو تأكد ارتفاع البوتاسيوم بشدة مع تغيرات تخطيط أخطر (اتساع QRS)، يصير الـ<bdi>treatment</bdi> الفوري بكالسيوم وريدي وإنسولين-جلوكوز ضروري.",
        "لو طلع البوتاسيوم <bdi>normal</bdi> رغم التغير بالتخطيط، يعاد النظر ب<bdi>causes</bdi> ثانية للتغيرات الكهربائية.",
    ],
    "rule": "أي <bdi>patient</bdi> على مثبط <bdi>ACE</bdi> تظهر له موجات T مدببة، أول <bdi>step</bdi> فحص مستوى البوتاسيوم مباشرة.",
    "comparison": None,
    "guideline_note": None,
},
425: {
    "idea": "<bdi>patient</bdi> قصور قلب <bdi>chronic</bdi> جاتها نوبة <bdi>acute</bdi> من ضيق النفس مع <bdi>congestion</bdi> رئوي واضح (JVP <bdi>elevated</bdi> و<bdi>crepitations</bdi> بالرئتين وS3) ونقص أكسجين، والسؤال يبي أفضل <bdi>step</bdi> علاجية فورية.",
    "clues": [
        ("high JVP with bilateral basal crackles", "<bdi>congestion</bdi> رئوي وجهازي واضح، يدل على حمل سوائل زايد"),
        ("S3 was heard at the apex", "<bdi>sign</bdi> قصور قلب انقباضي مع زيادة حجم البطين"),
        ("Oxygen saturation 88", "نقص أكسجين واضح يحتاج تدخل فوري"),
    ],
    "why_correct": [
        "الـ<bdi>step</bdi> الأولى بوذمة رئوية <bdi>acute</bdi> ناتجة عن قصور قلب هي إعطاء <bdi>IV furosemide</bdi> لتخفيف الحمل السوائلي بسرعة.",
        "المدر البولي الوريدي يعمل بسرعة أكبر من الفموي ويخفف الـ<bdi>congestion</bdi> الرئوي والـ<bdi>symptoms</bdi> خلال دقائق لساعات.",
        "الأكسجين وحده يحسّن التأكسج بس ما يعالج الـ<bdi>cause</bdi> الأساسي (<bdi>congestion</bdi> السوائل)، والـ<bdi>echo</bdi> مهم بس مو الـ<bdi>step</bdi> الفورية الأولى ب<bdi>case</bdi> <bdi>acute</bdi>.",
    ],
    "when_changes": [
        "لو ما استجابت على الـ<bdi>furosemide</bdi> وحده، يضاف مدر ثانوي زي <bdi>metolazone</bdi> لتقوية التأثير.",
        "لو التأكسج ما تحسن رغم المدر البولي، يصير إعطاء الأكسجين المكثف أو الدعم التنفسي ضروري بالتوازي.",
    ],
    "rule": "بالوذمة الرئوية الـ<bdi>acute</bdi> الناتجة عن <bdi>heart failure</bdi>، <bdi>IV furosemide</bdi> هو الـ<bdi>step</bdi> العلاجية الفورية الأولى.",
    "comparison": None,
    "guideline_note": None,
},
426: {
    "idea": "نفس صورة <bdi>patient</bdi> <bdi>heart failure</bdi> الـ<bdi>acute</bdi> (ضيق نفس واستلقاء ونوبات ليلية مع <bdi>congestion</bdi> رئوي وS3)، والسؤال هنا يبي الـ<bdi>diagnosis</bdi> السريري المباشر لهالصورة الـ<bdi>acute</bdi>.",
    "clues": [
        ("paroxysmal nocturnal dyspnea and orthopnea", "<bdi>symptoms</bdi> كلاسيكية ل<bdi>congestion</bdi> رئوي <bdi>acute</bdi> ب<bdi>heart failure</bdi>"),
        ("high JVP with bilateral basal crackles", "<bdi>signs</bdi> <bdi>congestion</bdi> جهازي ورئوي معًا"),
        ("S3 was heard at the apex", "<bdi>sign</bdi> قصور انقباضي بالبطين الأيسر"),
    ],
    "why_correct": [
        "تجمع الـ<bdi>symptoms</bdi> والـ<bdi>signs</bdi> هذي يصف مباشرة <bdi>case</bdi> <bdi>pulmonary oedema</bdi> الناتجة عن تدهور <bdi>acute</bdi> ب<bdi>heart failure</bdi> الـ<bdi>chronic</bdi>.",
        "<bdi>crepitations</bdi> الرئتين الـ<bdi>bilateral</bdi> مع S3 ونقص الأكسجين كلها <bdi>signs</bdi> تراكم سوائل بالحويصلات الهوائية <bdi>result</bdi> ضعف ضخ البطين الأيسر.",
        "ما فيه بالسؤال دليل مباشر على احتشاء <bdi>acute</bdi> جديد أو قصور يمين معزول أو <bdi>mitral regurgitation</bdi> <bdi>acute</bdi> يفسر الصورة بشكل أدق.",
    ],
    "when_changes": [
        "لو ظهر ألم صدري <bdi>acute</bdi> مع تغيرات تخطيط قلب جديدة، يصير الـ<bdi>diagnosis</bdi> احتشاء قلبي <bdi>acute</bdi> هو الـ<bdi>cause</bdi> المباشر.",
        "لو كان الـ<bdi>congestion</bdi> بالأطراف السفلية بس بدون <bdi>crepitations</bdi> رئوية، يميل الـ<bdi>diagnosis</bdi> أكثر ل<bdi>heart failure</bdi> الأيمن المعزول.",
    ],
    "rule": "ضيق نفس واستلقاء ونوبات ليلية مع <bdi>crepitations</bdi> رئوية وS3 يشخصون <bdi>pulmonary oedema</bdi> الناتج عن تدهور <bdi>heart failure</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
427: {
    "idea": "رياضي شاب سليم عنده بطء قلب جيبي بدون <bdi>symptoms</bdi> وبفحوصات <bdi>normal</bdi>، وهذا وضع فسيولوجي <bdi>normal</bdi> معروف عند الرياضيين ولا يحتاج <bdi>anxiety</bdi> أو تدخل.",
    "clues": [
        ("24-year-old athlete man", "الرياضة تسبب بطء قلب فسيولوجي ب<bdi>cause</bdi> زيادة نشاط العصب المبهم"),
        ("asymptomatic", "غياب الـ<bdi>symptoms</bdi> يدعم كونه وضع <bdi>normal</bdi> مو مرضي"),
        ("Normal CBC, renal function, LFT, and TSH", "استبعاد الـ<bdi>causes</bdi> الثانوية لبطء القلب"),
        ("ECG normal only sinus bradycardia", "تأكيد إن بطء القلب جيبي وبدون أي تشوه كهربائي آخر"),
    ],
    "why_correct": [
        "بطء القلب الجيبي عند الرياضيين المدربين <bdi>case</bdi> فسيولوجية <bdi>normal</bdi> <bdi>result</bdi> زيادة نشاط الجهاز العصبي المبهم وتحسن كفاءة القلب.",
        "غياب الـ<bdi>symptoms</bdi> مع تخطيط قلب وفحوصات <bdi>normal</bdi> بالكامل يستبعد أي <bdi>cause</bdi> مرضي خفي يحتاج تدخل.",
        "أفضل تصرف هنا هو الطمأنة فقط، لأن أي تدخل إضافي غير مبرر طبيًا بهالصورة الـ<bdi>normal</bdi> تمامًا.",
    ],
    "when_changes": [
        "لو ظهرت <bdi>symptoms</bdi> زي دوخة أو إغماء مصاحبة لبطء القلب، يصير الـ<bdi>assessment</bdi> الإضافي (زي الـ<bdi>echo</bdi> أو مراقبة هولتر) ضروري.",
        "لو التخطيط أظهر أي اضطراب نظم إضافي غير بطء القلب الجيبي البسيط، يتغير التوجه لل<bdi>assessment</bdi> القلبي الكامل.",
    ],
    "rule": "بطء القلب الجيبي بدون <bdi>symptoms</bdi> عند رياضي سليم بفحوصات <bdi>normal</bdi> يعتبر وضع فسيولوجي <bdi>normal</bdi> ولا يحتاج إلا الطمأنة.",
    "comparison": None,
    "guideline_note": None,
},
428: {
    "idea": "<bdi>patient</bdi> قصور قلب مسيطر عليها بمدر بولي ومثبط ACE، والسؤال يبي دواء إضافي يقلل الوفيات على المدى الطويل مو بس يحسّن الـ<bdi>symptoms</bdi>.",
    "clues": [
        ("treated with loop diuretic and ACE inhibitor", "<bdi>treatment</bdi> أساسي حالي ل<bdi>heart failure</bdi>"),
        ("good control of her symptoms", "الـ<bdi>symptoms</bdi> مسيطر عليها، فالهدف الآن تحسين البقاء طويل المدى"),
    ],
    "why_correct": [
        "<bdi>Spironolactone</bdi> مضاد لمستقبلات الـ<bdi>aldosterone</bdi>، وثبت بدراسات كبرى (RALES) إنه يقلل الوفيات عند إضافته ل<bdi>treatment</bdi> <bdi>heart failure</bdi> الأساسي.",
        "إضافته لمدر بولي ومثبط ACE تكمل الـ<bdi>block</bdi> على المحور الهرموني المسؤول عن تفاقم <bdi>heart failure</bdi> (RAAS) وتحسن البقاء.",
        "<bdi>Digoxin</bdi> و<bdi>amiodarone</bdi> يحسّنون الـ<bdi>symptoms</bdi> أو يتحكمون باضطراب النظم بس ما يثبت لهم تقليل واضح بالوفيات.",
    ],
    "when_changes": [
        "لو البوتاسيوم <bdi>elevated</bdi> أصلًا أو وظائف الكلى ضعيفة جدًا، لازم حذر <bdi>severe</bdi> أو تجنّب spironolactone ب<bdi>cause</bdi> <bdi>risk</bdi> فرط بوتاسيوم الدم.",
        "لو الـ<bdi>patient</bdi> عندها <bdi>atrial fibrillation</bdi> مصاحب، يصير digoxin مفيد للتحكم بمعدل ضربات القلب بجانب الـ<bdi>treatment</bdi> الأساسي مو بديل عنه.",
    ],
    "rule": "إضافة <bdi>spironolactone</bdi> ل<bdi>treatment</bdi> <bdi>heart failure</bdi> الأساسي (مدر ومثبط ACE) ثبت أنها تقلل الوفيات على المدى الطويل.",
    "comparison": None,
    "guideline_note": None,
},
429: {
    "idea": "<bdi>patient</bdi> <bdi>atrial fibrillation</bdi> مسكري متردد يبدأ مضاد تخثر خوفًا من النزيف، والسؤال يبي أهم <bdi>factor</bdi> يوجه القرار الطبي الصحيح.",
    "clues": [
        ("diabetic patient with atrial fibrillation", "<bdi>factors</bdi> <bdi>risk</bdi> تزيد احتمال الجلطات الدماغية"),
        ("hesitant to start anti-coagulant due to its risk of inducing bleeding", "<bdi>anxiety</bdi> الـ<bdi>patient</bdi> من النزيف مقابل فايدة منع الجلطات"),
    ],
    "why_correct": [
        "القرار الطبي الصحيح يعتمد على مقارنة <bdi>risk</bdi> الجلطات الدماغية مقابل <bdi>risk</bdi> النزيف الفعلي لهالمريض بالذات، مو مجرد الخوف العام من النزيف.",
        "بوجود <bdi>disease</bdi> <bdi>diabetes</bdi> ك<bdi>factor</bdi> <bdi>risk</bdi> إضافي (ضمن معايير CHADS2/CHA2DS2-VASc)، يكون <bdi>risk</bdi> الجلطات عادة أعلى من <bdi>risk</bdi> النزيف عند أغلب المرضى المشابهين.",
        "إذا كان <bdi>risk</bdi> الجلطات أعلى من <bdi>risk</bdi> النزيف، فمضاد التخثر يعطي فايدة صافية لل<bdi>patient</bdi> رغم وجود بعض <bdi>risk</bdi> النزيف.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> عنده تاريخ نزيف <bdi>severe</bdi> سابق أو <bdi>risk</bdi> نزيف عالي جدًا موثق، ممكن يميل الميزان لصالح تجنّب مضاد التخثر أو استخدام بديل أخف.",
        "لو كان <bdi>risk</bdi> الجلطات <bdi>low</bdi> جدًا (نقاط CHA2DS2-VASc صفر تقريبًا)، ممكن تجنّب مضاد التخثر يكون القرار الأنسب.",
    ],
    "rule": "قرار بدء مضاد التخثر ب<bdi>atrial fibrillation</bdi> يعتمد دايمًا على موازنة <bdi>risk</bdi> الجلطات مقابل <bdi>risk</bdi> النزيف لكل <bdi>patient</bdi> على حدة.",
    "comparison": None,
    "guideline_note": None,
},
430: {
    "idea": "<bdi>patient</bdi> قلقة من <bdi>complications</bdi> <bdi>procedure</bdi> تدخلي (قسطرة قلبية)، والسؤال يبي أفضل أسلوب تواصل يحترم استقلاليتها ويعطيها موافقة مستنيرة كاملة.",
    "clues": [
        ("admitted to the hospital for cardiac catheterization", "<bdi>procedure</bdi> تدخلي له مخاطر حقيقية تستحق شرح واضح"),
        ("concerned about its complications", "<bdi>anxiety</bdi> حقيقي يحتاج معالجة مباشرة ومفصلة"),
    ],
    "why_correct": [
        "أفضل أسلوب هو الاستماع الفعلي لمخاوفها، شرح الـ<bdi>complications</bdi> المتوقعة بصدق، وأيضًا ذكر البدائل المتاحة لها لتاخذ قرار مستنير كامل.",
        "هالأسلوب يحقق الموافقة المستنيرة الحقيقية لأنه يغطي كل عناصرها: الفهم، المخاطر، والبدائل، مو بس طمأنة سطحية.",
        "تجاهل مخاوفها أو التقليل منها (بقول إنها نادرة وما تحتاج <bdi>anxiety</bdi>) لا يحترم حقها بالمعرفة الكاملة قبل الـ<bdi>procedure</bdi>.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> رفضت الـ<bdi>procedure</bdi> تمامًا بعد الشرح الكامل، يحترم قرارها ويناقش خطة بديلة معها.",
        "لو كانت فاقدة الأهلية لاتخاذ القرار، يصير الحديث مع وليها الشرعي هو المسار الصحيح، مو الزوج تلقائيًا بدون <bdi>cause</bdi> طبي واضح.",
    ],
    "rule": "الموافقة المستنيرة الكاملة تشمل الاستماع للمخاوف، شرح المخاطر الحقيقية، وذكر البدائل المتاحة لل<bdi>patient</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
431: {
    "idea": "<bdi>patient</bdi> <bdi>asthma</bdi> وقصور قلب و<bdi>peptic ulcer</bdi> جالس على عدة أدوية، وصار عنده نقص <bdi>severe</bdi> بالبوتاسيوم بعد بدء <bdi>treatment</bdi> جديد، والسؤال يبي أكثر دواء يفسر هالنقص.",
    "clues": [
        ("nebulized salbutamol", "منبه بيتا استنشاقي يسبب دخول البوتاسيوم للخلايا"),
        ("Spironolactone", "دواء يحتفظ بالبوتاسيوم عادة، مو يخفضه"),
        ("serum potassium is noted to be 2.8", "نقص <bdi>severe</bdi> بالبوتاسيوم يحتاج تفسير دوائي مباشر"),
    ],
    "why_correct": [
        "<bdi>Salbutamol</bdi> منبه لمستقبلات بيتا-2 يحفز مضخة الصوديوم-بوتاسيوم ويدخل البوتاسيوم داخل الخلايا، فيخفض مستواه بالدم بسرعة خصوصًا بالجرعات المتكررة أو العالية.",
        "هالأثر معروف جدًا خصوصًا مع البخاخات المتكررة ل<bdi>treatment</bdi> تفاقم <bdi>asthma</bdi> الـ<bdi>acute</bdi>، ويفسر النقص الـ<bdi>acute</bdi> خلال 24 ساعة.",
        "<bdi>Spironolactone</bdi> بالعكس يرفع البوتاسيوم لأنه مدر بولي حافظ للبوتاسيوم، فهو غير مسؤول عن هالنقص إطلاقًا.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> على مدر بولي من نوع الثيازيد أو الحلقي بجرعة عالية بدون سالبوتامول، يصير المدر البولي هو الـ<bdi>cause</bdi> الأرجح للنقص.",
        "لو توقف البخاخ وبقي النقص مستمرًا، لازم البحث عن <bdi>cause</bdi> ثاني زي فقدان هضمي أو كلوي.",
    ],
    "rule": "منبهات بيتا-2 الاستنشاقية زي <bdi>salbutamol</bdi> تسبب نقص بوتاسيوم <bdi>acute</bdi> بتحريك البوتاسيوم لداخل الخلايا، خصوصًا بالجرعات المتكررة.",
    "comparison": None,
    "guideline_note": None,
},
432: {
    "idea": "<bdi>patient</bdi> عندها متلازمة وولف-<bdi>Parkinson's disease</bdi>-وايت (WPW) مع نوبات إغماء متكررة وما استجابت على حاصر بيتا، والسؤال يبي الـ<bdi>treatment</bdi> النهائي الفعال لحالتها.",
    "clues": [
        ("short PR interval", "<bdi>sign</bdi> تخطيط قلب كلاسيكية لمتلازمة WPW (مسار توصيل إضافي)"),
        ("diagnosed as Wolf-Parkinson-White (WPW) syndrome", "الـ<bdi>diagnosis</bdi> مؤكد مسبقًا"),
        ("given atenolol with no response", "فشل الـ<bdi>treatment</bdi> الدوائي الأولي بالتحكم بالـ<bdi>symptoms</bdi>"),
    ],
    "why_correct": [
        "<bdi>Radiofrequency ablation</bdi> هو الـ<bdi>treatment</bdi> النهائي الشافي لمتلازمة WPW لأنه يزيل المسار التوصيلي الإضافي المسبب لاضطراب النظم مباشرة.",
        "بعد فشل الـ<bdi>treatment</bdi> الدوائي (حاصر بيتا) بالتحكم بالنوبات المتكررة والإغماء، يصير الاستئصال بالترددات الراديوية الخيار الأنسب لمنع النوبات نهائيًا.",
        "زيادة جرعة الحاصر أو إضافة أدوية ثانية زي الـ<bdi>digoxin</bdi> قد تكون غير كافية وحتى خطرة أحيانًا بمرضى WPW لأنها ممكن تسرع التوصيل بالمسار الإضافي.",
    ],
    "when_changes": [
        "لو استجابت الـ<bdi>symptoms</bdi> جيدًا على حاصر بيتا من البداية، ممكن الاكتفاء بالـ<bdi>treatment</bdi> الدوائي بدون تدخل جراحي.",
        "لو كانت النوبات نادرة جدًا و<bdi>mild</bdi> بدون إغماء، ممكن يكتفى بالمراقبة والـ<bdi>treatment</bdi> الدوائي البسيط.",
    ],
    "rule": "بفشل الـ<bdi>treatment</bdi> الدوائي بمتلازمة WPW العرضية، <bdi>radiofrequency ablation</bdi> هو الـ<bdi>treatment</bdi> النهائي الفعال.",
    "comparison": None,
    "guideline_note": None,
},
433: {
    "idea": "<bdi>patient</bdi> ألم صدري متقطع مع تسرع قلب وتعرق، والسؤال يبي قراءة صورة تخطيط القلب المرفقة لتحديد نوع التشوه الكهربائي الظاهر.",
    "clues": [
        ("intermittent chest pains", "<bdi>symptoms</bdi> تدعم مشكلة قلبية <bdi>acute</bdi> محتملة"),
        ("ECG is done (see image)", "الـ<bdi>diagnosis</bdi> يعتمد مباشرة على قراءة الصورة المرفقة"),
        ("tachycardic and sweaty", "<bdi>signs</bdi> جهاز عصبي ودي متفعل، يدعم <bdi>case</bdi> قلبية <bdi>acute</bdi>"),
    ],
    "why_correct": [
        "الصورة المرفقة بالسؤال تظهر نمط <bdi>left bundle branch block</bdi>، وهو تشوه بتوصيل الإشارة الكهربائية بالبطين الأيسر.",
        "ب<bdi>patient</bdi> عنده ألم صدري حديث ونمط LBBB جديد، هذا يعتبر مؤشر مهم يوجب التعامل معه كاحتشاء قلبي <bdi>acute</bdi> محتمل لحين إثبات العكس.",
        "الأنماط الثانية (<bdi>block</bdi> الحزمة اليمنى أو تسرع بطيني) لها معالم تخطيطية مختلفة عن الموصوف بصورة السؤال.",
    ],
    "when_changes": [
        "لو الصورة أظهرت QRS واسع منتظم بمعدل سريع جدًا بدون موجات P واضحة، يصير الـ<bdi>diagnosis</bdi> تسرع بطيني بدل LBBB.",
        "لو الاحتشاء كان بالجدار الخلفي فقط بدون <bdi>block</bdi> توصيل، تظهر تغيرات مختلفة (ارتفاع ST بالخلف مع انخفاضه الانعكاسي بـV1-V2).",
    ],
    "rule": "ظهور <bdi>left bundle branch block</bdi> جديد ب<bdi>patient</bdi> عنده ألم صدري يعامل كاحتشاء قلبي <bdi>acute</bdi> لحين إثبات العكس.",
    "comparison": None,
    "guideline_note": None,
},
434: {
    "idea": "<bdi>patient</bdi> عنده <bdi>factors</bdi> <bdi>risk</bdi> قلبية (ضغط <bdi>chronic</bdi> وتدخين طويل) وبدأ يعاني ضيق نفس حديث مع <bdi>crepitations</bdi> <bdi>mild</bdi>، والسؤال يبي أفضل فحص يكشف خلل بوظيفة البطين الأيسر.",
    "clues": [
        ("dyspnoea on exertion", "<bdi>symptom</bdi> يوجه لاحتمال بداية قصور قلب"),
        ("long standing hypertension", "<bdi>factor</bdi> <bdi>risk</bdi> رئيسي لخلل وظيفة البطين الأيسر"),
        ("rare crackles at the bases of the lungs", "<bdi>sign</bdi> مبكرة محتملة ل<bdi>congestion</bdi> رئوي <bdi>mild</bdi>"),
    ],
    "why_correct": [
        "<bdi>B-type natriuretic peptide (BNP)</bdi> يفرز من عضلة القلب استجابة لزيادة الضغط والحمل على البطين، فارتفاعه يكشف خلل وظيفة البطين الأيسر بدقة عالية.",
        "هالفحص حساس جدًا لاستبعاد أو تأكيد <bdi>heart failure</bdi> ك<bdi>cause</bdi> لضيق النفس، خصوصًا بمرضى عندهم <bdi>factors</bdi> <bdi>risk</bdi> <bdi>chronic</bdi> زي هذا الـ<bdi>patient</bdi>.",
        "التروبونين وCK وCRP فحوصات لتلف عضلة القلب الـ<bdi>acute</bdi> أو الالتهاب، مو ل<bdi>assessment</bdi> الوظيفة الانقباضية الـ<bdi>chronic</bdi> للبطين.",
    ],
    "when_changes": [
        "لو كان الهدف تأكيد احتشاء قلبي <bdi>acute</bdi> بدل <bdi>assessment</bdi> وظيفة البطين الـ<bdi>chronic</bdi>، يصير Troponin T هو الفحص الأنسب.",
        "لو ارتفع BNP بشكل واضح، الـ<bdi>step</bdi> التالية المنطقية تصير عمل <bdi>echo</bdi> قلب لتأكيد وتحديد درجة الخلل.",
    ],
    "rule": "<bdi>BNP</bdi> هو الفحص الأنسب للكشف عن خلل وظيفة البطين الأيسر عند الاشتباه بقصور قلب مبكر.",
    "comparison": None,
    "guideline_note": None,
},
435: {
    "idea": "<bdi>patient</bdi> <bdi>atrial fibrillation</bdi> على <bdi>warfarin</bdi> خضع لقسطرة وتدخل تاجي حديث، والسؤال يبي أفضل نظام مضاد تخثر بعد الـ<bdi>procedure</bdi> يوازن بين منع الـ<bdi>thrombus</bdi> الدماغية ومنع <bdi>thrombus</bdi> الدعامة.",
    "clues": [
        ("history of atrial fibrillation", "يحتاج مضاد تخثر مستمر لمنع الـ<bdi>thrombus</bdi> الدماغية"),
        ("percutaneous coronary intervention", "يحتاج مضادات صفائح لمنع <bdi>thrombus</bdi> الدعامة الحديثة"),
        ("Antithrombotic therapy immediately given after his event", "يبي النظام الأنسب مباشرة بعد الـ<bdi>procedure</bdi>"),
    ],
    "why_correct": [
        "ب<bdi>patient</bdi> <bdi>atrial fibrillation</bdi> خضع لتدخل تاجي وتركيب دعامة، الأنسب هو الاستمرار بمضاد التخثر (<bdi>warfarin</bdi>) لل<bdi>thrombus</bdi> الدماغية مع إضافة مضادين للصفائح لحماية الدعامة لفترة محددة.",
        "هالنظام الثلاثي (triple therapy) يغطي الخطرين معًا: <bdi>risk</bdi> الـ<bdi>thrombus</bdi> الدماغية من الرجفان و<bdi>risk</bdi> <bdi>thrombus</bdi> الدعامة الحديثة.",
        "إيقاف الـ<bdi>warfarin</bdi> تمامًا يترك الـ<bdi>patient</bdi> معرض ل<bdi>risk</bdi> <bdi>thrombus</bdi> دماغية ب<bdi>cause</bdi> <bdi>atrial fibrillation</bdi> المستمر رغم <bdi>treatment</bdi> التاجية.",
    ],
    "when_changes": [
        "لو مر وقت كافي بعد تركيب الدعامة بدون <bdi>complications</bdi>، يقلل عدد الأدوية تدريجيًا حسب بروتوكولات معينة لتقليل <bdi>risk</bdi> النزيف.",
        "لو كان <bdi>risk</bdi> النزيف عالي جدًا عند الـ<bdi>patient</bdi>، يميل الأطباء لتقصير مدة الـ<bdi>treatment</bdi> الثلاثي واستخدام مضاد صفائح واحد بدل اثنين بشكل أبكر.",
    ],
    "rule": "ب<bdi>patient</bdi> <bdi>atrial fibrillation</bdi> بعد تدخل تاجي حديث، يستمر مضاد التخثر مع إضافة مضادات الصفائح مؤقتًا لتغطية <bdi>risk</bdi> الـ<bdi>thrombus</bdi> الدماغية و<bdi>thrombus</bdi> الدعامة معًا.",
    "comparison": None,
    "guideline_note": None,
},
436: {
    "idea": "<bdi>patient</bdi> احتشاء سابق تحلل بالـ<bdi>thrombus</bdi>، صار عنده تورم باللسان والوجه بعد أسابيع، وهذا تفاعل تحسسي معروف (وذمة وعائية) مرتبط بأحد أدويته الحالية.",
    "clues": [
        ("marked tongue and facial swelling", "صورة كلاسيكية لـ<bdi>angioedema</bdi>"),
        ("vital signs are within the normal limits", "استبعاد صدمة تحسسية <bdi>severe</bdi> أو انسداد مجرى هوائي فوري"),
    ],
    "why_correct": [
        "<bdi>Ramipril</bdi> من مثبطات ACE، وهذي المجموعة معروفة بتسببها بوذمة وعائية (angioedema) بتورم الوجه واللسان كأثر جانبي نادر لكن خطير.",
        "الآلية سببها تراكم مادة bradykinin <bdi>result</bdi> تثبيط إنزيم ACE، وممكن تحصل حتى بعد استخدام الدواء لفترة من الوقت.",
        "باقي الأدوية المذكورة (<bdi>aspirin</bdi>، أتورفاستاتين، <bdi>atenolol</bdi>) ما ترتبط بشكل مباشر بهالنوع من التورم الوجهي واللساني.",
    ],
    "when_changes": [
        "لو التورم صاحبه انتشار طفح جلدي وحكة <bdi>severe</bdi> بدون تورم لساني، ممكن يفكر بتحسس دوائي عام ثاني بدل الوذمة الوعائية النوعية.",
        "بعد تأكيد الـ<bdi>diagnosis</bdi>، الـ<bdi>step</bdi> العلاجية الصحيحة تصير إيقاف مثبط ACE فورًا وتجنّبه مستقبلًا نهائيًا.",
    ],
    "rule": "مثبطات <bdi>ACE</bdi> زي <bdi>ramipril</bdi> من أشهر <bdi>causes</bdi> <bdi>angioedema</bdi> الدوائي، وممكن تحصل حتى بعد أسابيع من بدء الـ<bdi>treatment</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
437: {
    "idea": "<bdi>patient</bdi> ضغط غير مسيطر عليه رغم دواءين من مجموعتين مختلفتين، والسؤال يبي أفضل دواء ثالث يضاف حسب الفحوصات الـ<bdi>normal</bdi> عنده.",
    "clues": [
        ("losartan and amlodipine", "<bdi>treatment</bdi> <bdi>bilateral</bdi> حالي من مجموعتين مختلفتين"),
        ("blood test and renal function profile were within the normal limits", "لا يوجد مانع كلوي من إضافة مدر بولي"),
    ],
    "why_correct": [
        "الـ<bdi>step</bdi> الثالثة المعتادة بضغط غير مسيطر عليه رغم دواءين هي إضافة مدر بولي من نوع الثيازيد أو شبيه الثيازيد زي <bdi>indapamide</bdi>.",
        "وظائف الكلى الـ<bdi>normal</bdi> تدعم أمان استخدام هالمدر البولي بدون <bdi>anxiety</bdi> من تراكم أو أثر جانبي كلوي.",
        "إضافة حاصر بيتا أو ألفا (زي doxazosin) عادة تكون خطوات لاحقة بعد المدر البولي، مو الـ<bdi>step</bdi> الثالثة المعتادة أولًا.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> عنده قصور كلوي واضح يمنع استخدام الثيازيد بفعالية، يصير مدر بولي حلقي أو خيار ثاني هو الأنسب.",
        "لو ظهر بوتاسيوم <bdi>low</bdi> مع الدواءين الحاليين، يصير المدر البولي فرصة إضافية لتصحيح ذلك عند اختيار النوع المناسب.",
    ],
    "rule": "بضغط الدم غير المضبوط رغم دواءين من مجموعتين مختلفتين، الـ<bdi>step</bdi> الثالثة المعتادة إضافة مدر بولي شبيه بالثيازيد.",
    "comparison": None,
    "guideline_note": None,
},
438: {
    "idea": "<bdi>patient</bdi> على clopidogrel للوقاية الثانوية من <bdi>disease</bdi> القلب الإقفاري، والسؤال يبي دواء يضعف تأثيره العلاجي ب<bdi>cause</bdi> تداخل دوائي معروف.",
    "clues": [
        ("intolerant of aspirin", "<bdi>cause</bdi> استخدام كلوبيدوجريل بدل الـ<bdi>aspirin</bdi>"),
        ("make clopidogrel less effective", "يبي دواء يقلل فعالية كلوبيدوجريل تحديدًا"),
    ],
    "why_correct": [
        "<bdi>Clopidogrel</bdi> دواء غير فعال أصلًا ويحتاج تفعيل بإنزيم كبدي (CYP2C19)، وبعض مثبطات مضخة البروتون زي <bdi>omeprazole</bdi> تثبط هالإنزيم وتقلل تحويله للشكل الفعال.",
        "هالتداخل يقلل فعالية كلوبيدوجريل المضادة للصفائح ويزيد <bdi>risk</bdi> تكون جلطات رغم استخدام الدواء بانتظام.",
        "باقي الأدوية المذكورة (<bdi>warfarin</bdi>، حاصرات بيتا، SSRIs) ما تتداخل بنفس الآلية المباشرة مع تفعيل كلوبيدوجريل.",
    ],
    "when_changes": [
        "لو احتاج الـ<bdi>patient</bdi> مثبط مضخة بروتون فعليًا، يفضّل اختيار نوع أقل تداخلًا زي <bdi>pantoprazole</bdi> بدل الأوميبرازول.",
        "لو كان الـ<bdi>patient</bdi> على <bdi>warfarin</bdi> مع كلوبيدوجريل، المشكلة تصير زيادة <bdi>risk</bdi> النزيف مو إضعاف فعالية كلوبيدوجريل نفسه.",
    ],
    "rule": "<bdi>Omeprazole</bdi> يثبط تفعيل <bdi>clopidogrel</bdi> الكبدي ويقلل فعاليته المضادة للصفائح.",
    "comparison": None,
    "guideline_note": None,
},
439: {
    "idea": "<bdi>patient</bdi> مشتبه بقصور قلب طلع عنده BNP <bdi>elevated</bdi> قليلًا، والسؤال يبي <bdi>factor</bdi> يرفع BNP بشكل كاذب بدون وجود قصور قلب حقيقي.",
    "clues": [
        ("suspected left ventricular heart failure", "السياق المرضي لطلب فحص BNP"),
        ("slightly elevated", "ارتفاع بسيط يثير التساؤل عن <bdi>causes</bdi> مؤثرة ثانية غير <bdi>heart failure</bdi> نفسه"),
    ],
    "why_correct": [
        "<bdi>disease</bdi> <bdi>COPD</bdi> يسبب ارتفاع ضغط بالدورة الرئوية وإجهاد على البطين الأيمن، وهذا يرفع مستوى BNP حتى بدون قصور قلب أيسر حقيقي.",
        "هالارتفاع يعتبر كاذب نسبيًا بالنسبة ل<bdi>diagnosis</bdi> <bdi>heart failure</bdi> الأيسر تحديدًا، رغم إنه يعكس إجهاد قلبي رئوي حقيقي بآلية مختلفة.",
        "من المهم معرفة هالعامل المربك عشان ما نشخص قصور قلب أيسر بالخطأ ب<bdi>patient</bdi> عنده <bdi>disease</bdi> رئوي <bdi>chronic</bdi> فقط.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عنده سمنة مفرطة بدل <bdi>disease</bdi> رئوي، الأثر يكون بالعكس (BNP كاذب <bdi>low</bdi>) مو <bdi>elevated</bdi>.",
        "لو كان الـ<bdi>patient</bdi> على مثبط ACE، هذا الـ<bdi>treatment</bdi> يخفض BNP قليلًا <bdi>result</bdi> تحسن وظيفة القلب، مو يرفعه كذبًا.",
    ],
    "rule": "<bdi>diseases</bdi> الرئة الـ<bdi>chronic</bdi> زي <bdi>COPD</bdi> ممكن ترفع BNP بشكل كاذب ب<bdi>cause</bdi> إجهادها على البطين الأيمن، حتى بدون قصور قلب أيسر حقيقي.",
    "comparison": {
        "headers": ["الـ<bdi>factor</bdi>", "أثره على BNP"],
        "rows": [
            ["<bdi>COPD</bdi> / ارتفاع ضغط رئوي", "يرفعه كذبًا"],
            ["السمنة", "يخفضه كذبًا"],
            ["مثبطات ACE", "يخفضه فعليًا مع تحسن الـ<bdi>case</bdi>"],
        ],
    },
    "guideline_note": None,
},
440: {
    "idea": "<bdi>patient</bdi> عندها تاريخ إصلاح جراحي لرباعية فالو منذ الطفولة، وظهرت <bdi>murmur</bdi> انبساطية متناقصة تزيد بالشهيق عند الحافة القصية اليسرى، وهذي صورة كلاسيكية لقصور الصمام الرئوي ك<bdi>complication</bdi> متأخرة للجراحة.",
    "clues": [
        ("history of Fallot tetralogy repair", "تاريخ جراحي يفسر <bdi>complications</bdi> لاحقة بالصمام الرئوي"),
        ("S1 is single with grade 2/4 decrescendo diastolic murmur that increases with inspiration", "<bdi>murmur</bdi> انبساطية يمينية تزيد بالشهيق، مميزة لقصور الصمام الرئوي"),
        ("Oxygen saturation 92", "نقص أكسجين <bdi>mild</bdi> متوافق مع <bdi>complications</bdi> قلبية يمينية <bdi>chronic</bdi>"),
    ],
    "why_correct": [
        "قصور الصمام الرئوي (<bdi>pulmonary regurgitation</bdi>) من أشهر الـ<bdi>complications</bdi> طويلة المدى بعد جراحة إصلاح رباعية فالو ب<bdi>cause</bdi> توسيع مجرى خروج البطين الأيمن أثناء الجراحة.",
        "الـ<bdi>murmur</bdi> الانبساطية المتناقصة اللي تزيد بالشهيق تتوافق مع <bdi>murmurs</bdi> الجانب الأيمن من القلب، وتحديدًا قصور الصمام الرئوي هنا.",
        "الاندفاع القصي الأيسر يدعم تضخم البطين الأيمن الـ<bdi>chronic</bdi> <bdi>result</bdi> الحمل الحجمي الزايد من قصور الصمام الرئوي.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>murmur</bdi> انقباضية بدل انبساطية عند نفس الموقع، يصير التفكير بتضيق متبقي بالصمام الرئوي أو الفتحة البطينية بدل القصور.",
        "لو ما فيه تاريخ جراحي لرباعية فالو أصلًا، تقل احتمالية قصور الصمام الرئوي ك<bdi>cause</bdi> أساسي لل<bdi>murmur</bdi>.",
    ],
    "rule": "قصور الصمام الرئوي <bdi>complication</bdi> متأخرة شائعة بعد إصلاح رباعية فالو، وتظهر ك<bdi>murmur</bdi> انبساطية تزيد بالشهيق عند الحافة القصية اليسرى.",
    "comparison": None,
    "guideline_note": None,
},
441: {
    "idea": "شابة عندها تعب وحمى مستمرة تزداد سوء مع التهاب مفاصل وبقع نمشية وتاريخ سابق لخلع أسنان و<bdi>murmur</bdi> قلبية جديدة، وهذي صورة كلاسيكية ل<bdi>endocarditis</bdi> تحت الـ<bdi>acute</bdi>.",
    "clues": [
        ("dental extraction 2 months ago", "بوابة دخول بكتيرية سابقة للدم"),
        ("petechia over lower limb", "<bdi>sign</bdi> جلدية شائعة ب<bdi>endocarditis</bdi> تحت الـ<bdi>acute</bdi>"),
        ("3/6 holosystolic murmur that radiates to axilla and mild splenomegaly", "<bdi>murmur</bdi> قلبية جديدة مع تضخم طحال، يدعم <bdi>endocarditis</bdi>"),
        ("mild proteinuna and microscopic hematuria", "التهاب كبيبي مناعي مصاحب ل<bdi>endocarditis</bdi>"),
    ],
    "why_correct": [
        "تجمع الحمى المتصاعدة مع التهاب المفاصل والنمشيات والـ<bdi>murmur</bdi> الجديدة وتضخم الطحال بعد خلع أسنان يشخص <bdi>infective endocarditis</bdi> تحت الـ<bdi>acute</bdi>.",
        "خلل وظائف الكلى (بروتين ودم بالبول) يعكس التهاب كبيبي مناعي مصاحب، وهو من الـ<bdi>complications</bdi> المعروفة ل<bdi>endocarditis</bdi> الـ<bdi>chronic</bdi>.",
        "خلع الأسنان قبل شهرين وفّر بوابة دخول بكتيرية كافية لتسبب التهاب شغاف تحت <bdi>acute</bdi> يتطور بشكل تدريجي على أسابيع.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>symptoms</bdi> أشد وأسرع (خلال أيام) مع <bdi>murmur</bdi> قلبية جديدة <bdi>acute</bdi> ودليل قوي على مصدر بكتيري جهازي، يصير التفكير بالتهاب شغاف <bdi>acute</bdi> بدل تحت <bdi>acute</bdi>.",
        "لو غابت الـ<bdi>signs</bdi> القلبية (الـ<bdi>murmur</bdi>) تمامًا مع وجود ألم مفاصل متعدد وطفح جلدي مميز، يصير <bdi>lupus</bdi> احتمال أقوى.",
    ],
    "rule": "حمى متصاعدة مع <bdi>murmur</bdi> قلبية جديدة ونمشيات بعد <bdi>procedure</bdi> سني حديث تدفع للتفكير أولًا بـ<bdi>infective endocarditis</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
442: {
    "idea": "<bdi>patient</bdi> صارت عندها <bdi>symptoms</bdi> قصور قلب واضحة (ضيق نفس واستلقاء ونوبات ليلية) خلال أيام قليلة بعد الولادة، وهذا يوجه مباشرة ل<bdi>cardiomyopathy</bdi> حول الولادة.",
    "clues": [
        ("3 days post vaginal delivery", "توقيت الـ<bdi>symptoms</bdi> قريب جدًا من الولادة، مميز لهالحالة"),
        ("apex was displaced down with pan-systolic murmur at the apex radiating to axilla and S3 gallop", "<bdi>signs</bdi> توسع البطين الأيسر مع <bdi>mitral regurgitation</bdi> وظيفي ثانوي"),
        ("no significant medical history", "استبعاد <bdi>diseases</bdi> قلبية سابقة تفسر الـ<bdi>symptoms</bdi>"),
    ],
    "why_correct": [
        "ظهور <bdi>symptoms</bdi> قصور قلب واضحة خلال الأيام الأولى بعد الولادة بدون تاريخ مرضي سابق يشخص <bdi>peri-partum cardiomyopathy</bdi>.",
        "توسع البطين الأيسر و<bdi>shift</bdi> النبض القمي مع S3 يدعمون ضعف انقباض عضلة القلب حديث الحدوث مرتبط بفترة الحمل والولادة.",
        "الـ<bdi>murmur</bdi> الانقباضية الشاملة (pan-systolic) هنا ثانوية لتوسع البطين وليست <bdi>cause</bdi> أساسي لل<bdi>case</bdi>.",
    ],
    "when_changes": [
        "لو صاحبت الـ<bdi>symptoms</bdi> حمى واضحة مع دليل مخبري على عدوى، يصير التفكير بالإنتان النفاسي (puerperium sepsis) أقوى بدل <bdi>cardiomyopathy</bdi>.",
        "لو ظهرت <bdi>murmur</bdi> قلبية جديدة موضعية مع <bdi>signs</bdi> عدوى جهازية بدون توسع بطيني واضح، يصير <bdi>endocarditis</bdi> احتمال يستحق الاستبعاد.",
    ],
    "rule": "<bdi>symptoms</bdi> قصور قلب <bdi>acute</bdi> خلال الشهر الأخير من الحمل حتى 5 أشهر بعد الولادة بدون <bdi>cause</bdi> آخر تشخص <bdi>peripartum cardiomyopathy</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
443: {
    "idea": "نفس الـ<bdi>patient</bdi> ب<bdi>cardiomyopathy</bdi> حول الولادة، لكن هذا السؤال يبي الـ<bdi>step</bdi> التالية الأنسب لتأكيد الـ<bdi>diagnosis</bdi> و<bdi>assessment</bdi> شدة الـ<bdi>case</bdi>.",
    "clues": [
        ("apex was displaced down with pan-systolic murmur at the apex radiating to axilla and S3 gallop", "<bdi>signs</bdi> سريرية قوية لضعف انقباض واتساع البطين الأيسر"),
        ("Oxygen saturation 90", "نقص أكسجين يدعم شدة الـ<bdi>congestion</bdi> الرئوي الحالي"),
    ],
    "why_correct": [
        "<bdi>Echocardiography</bdi> هو الفحص الأساسي لتأكيد <bdi>diagnosis</bdi> <bdi>cardiomyopathy</bdi> حول الولادة وتحديد نسبة الضخ ودرجة توسع البطين.",
        "هالفحص غير جراحي وسريع ومتاح بالطوارئ، ويعطي معلومات كافية توجه الـ<bdi>treatment</bdi> فورًا بدون تأخير.",
        "اختبار الإجهاد بالثاليوم أو الرنين المغناطيسي القلبي <bdi>procedures</bdi> غير مناسبة أو غير عاجلة ب<bdi>case</bdi> <bdi>acute</bdi> ومهددة زي هذي.",
    ],
    "when_changes": [
        "بعد تأكيد الـ<bdi>diagnosis</bdi> بالـ<bdi>echo</bdi>، لو احتاج تفاصيل تشريحية أدق ل<bdi>cause</bdi> نادر مصاحب، ممكن يفكر بالرنين المغناطيسي لاحقًا ك<bdi>step</bdi> مكملة.",
        "لو كان هدف السؤال استبعاد <bdi>cause</bdi> إقفاري لل<bdi>symptoms</bdi>، يصير تخطيط القلب وقياس التروبونين <bdi>step</bdi> أولية مهمة أيضًا لكن مو الأهم هنا.",
    ],
    "rule": "الـ<bdi>echo</bdi> القلبي هو الفحص الأول والأهم لتأكيد و<bdi>assessment</bdi> شدة <bdi>cardiomyopathy</bdi> حول الولادة.",
    "comparison": None,
    "guideline_note": None,
},
444: {
    "idea": "<bdi>patient</bdi> صمام أبهري ميكانيكي مستقر وبدون <bdi>symptoms</bdi>، مقبل على عملية جراحية بسيطة (فتق)، والسؤال يبي هل يحتاج مضاد حيوي وقائي ل<bdi>endocarditis</bdi> قبل العملية.",
    "clues": [
        ("mechanical aortic valve replacement 4 years ago", "صمام صناعي، <bdi>factor</bdi> <bdi>risk</bdi> ل<bdi>endocarditis</bdi> بشكل عام"),
        ("elective hernia repair surgery", "<bdi>procedure</bdi> جراحي نظيف لا يخترق أغشية مخاطية فموية أو تنفسية"),
    ],
    "why_correct": [
        "حسب الإرشادات الحديثة، الوقاية بالمضاد الحيوي ل<bdi>endocarditis</bdi> تقتصر على <bdi>procedures</bdi> معينة (أسنان أو جهاز تنفسي مخترق)، مو الجراحات الجلدية النظيفة زي إصلاح الفتق.",
        "إصلاح الفتق <bdi>procedure</bdi> نظيف لا يخترق أغشية مخاطية ولا يسبب دخول بكتيريا فموية أو تنفسية للدم، فما يستدعي وقاية.",
        "إعطاء مضاد حيوي وقائي بدون داعي يعرض الـ<bdi>patient</bdi> لآثار جانبية و<bdi>risk</bdi> مقاومة بكتيرية بدون فايدة حقيقية.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>procedure</bdi> المخطط له خلع سن أو عملية باللثة، يصير إعطاء مضاد حيوي وقائي (زي أموكسيسيلين) ضروري لوجود صمام صناعي.",
        "لو كان الـ<bdi>procedure</bdi> بجهاز تنفسي يخترق الغشاء المخاطي، تنطبق نفس قاعدة الوقاية بمرضى الصمام الصناعي.",
    ],
    "rule": "الوقاية من <bdi>endocarditis</bdi> بالمضاد الحيوي تقتصر على <bdi>procedures</bdi> الأسنان أو الجهاز التنفسي المخترقة، مو كل عملية جراحية ب<bdi>patient</bdi> صمام صناعي.",
    "comparison": None,
    "guideline_note": None,
},
445: {
    "idea": "السؤال يبي حساب درجة CHADS2 ل<bdi>patient</bdi> عنده <bdi>atrial fibrillation</bdi> مع عدة <bdi>factors</bdi> <bdi>risk</bdi> مذكورة صراحة بالسؤال.",
    "clues": [
        ("diabetic mellitus", "<bdi>factor</bdi> <bdi>risk</bdi> واحد بمقياس CHADS2"),
        ("hypertension", "<bdi>factor</bdi> <bdi>risk</bdi> ثاني بمقياس CHADS2"),
        ("history of stroke", "<bdi>factor</bdi> <bdi>risk</bdi> يحسب بنقطتين بمقياس CHADS2"),
        ("Atrial fibrillation on ECG", "الـ<bdi>disease</bdi> الأساسي المطلوب <bdi>assessment</bdi> خطره"),
    ],
    "why_correct": [
        "مقياس CHADS2 يحسب نقطة لكل من: <bdi>heart failure</bdi>، الضغط، العمر 75 فأكثر، <bdi>diabetes</bdi>، ونقطتين للسكتة الدماغية السابقة.",
        "هالمريض عنده: قصور قلب (S3 و<bdi>crepitations</bdi>، نقطة)، ضغط (نقطة)، <bdi>diabetes</bdi> (نقطة)، وسكتة دماغية سابقة (نقطتين)، فالمجموع يصير 5 نقاط.",
        "هالنقاط العالية تعني <bdi>risk</bdi> عالي جدًا لل<bdi>thrombus</bdi> الدماغية، وتوجب بدء مضاد تخثر فموي فورًا.",
    ],
    "when_changes": [
        "لو ما كان عنده تاريخ سكتة دماغية سابقة، تنقص النقاط لتصير 3 فقط.",
        "لو كان عمره أقل من 75 وما عنده أي <bdi>factor</bdi> من الـ<bdi>factors</bdi> المذكورة، تكون النقاط أقل بكثير ويحتاج <bdi>assessment</bdi> مختلف لمضاد التخثر.",
    ],
    "rule": "مقياس CHADS2 يجمع نقاط <bdi>heart failure</bdi> والضغط والعمر و<bdi>diabetes</bdi> (نقطة لكل واحد) و<bdi>stroke</bdi> السابقة (نقطتين) لتقدير <bdi>risk</bdi> الـ<bdi>thrombus</bdi> ب<bdi>atrial fibrillation</bdi>.",
    "comparison": {
        "headers": ["الـ<bdi>factor</bdi>", "النقاط"],
        "rows": [
            ["<bdi>heart failure</bdi>", "1"],
            ["ضغط الدم", "1"],
            ["<bdi>diabetes</bdi>", "1"],
            ["سكتة دماغية سابقة", "2"],
            ["المجموع", "5"],
        ],
    },
    "guideline_note": None,
},
446: {
    "idea": "<bdi>patient</bdi> عنده <bdi>angina</bdi> مجهودية بدون <bdi>factors</bdi> <bdi>risk</bdi> مذكورة وفحص وتخطيط قلب طبيعيين بالراحة، والسؤال يبي أفضل <bdi>step</bdi> تشخيصية تالية لتأكيد الإقفار.",
    "clues": [
        ("occurs mainly after heavy physical exertion", "نمط الألم يوحي بذبحة مجهودية نموذجية"),
        ("Clinical examination and baseline ECG were normal", "لا يوجد دليل إقفار بالراحة، يحتاج اختبار بالمجهود لإظهاره"),
    ],
    "why_correct": [
        "<bdi>Exercise ECG</bdi> هو الفحص الأولي المناسب ل<bdi>patient</bdi> ذبحة مجهودية بتخطيط قلب <bdi>normal</bdi> بالراحة، لأنه يكشف التغيرات الإقفارية اللي تظهر فقط أثناء المجهود.",
        "هالفحص غير جراحي وأقل تكلفة من القسطرة، ومناسب ك<bdi>step</bdi> أولى ب<bdi>patient</bdi> <bdi>low</bdi> إلى متوسط الخطورة.",
        "تصوير الشرايين التاجية (القسطرة) <bdi>procedure</bdi> أكثر تدخلًا يحجز عادة لو كان الاختبار المجهودي إيجابيًا أو الخطورة عالية جدًا من البداية.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> غير قادر على المشي بالمجهود (مشاكل مفصلية مثلًا)، يصير فحص الإجهاد الدوائي (زي adenosine) بديل مناسب.",
        "لو كانت الـ<bdi>symptoms</bdi> <bdi>severe</bdi> جدًا أو غير مستقرة، يصير التوجه المباشر لتصوير الشرايين التاجية أنسب من اختبار المجهود.",
    ],
    "rule": "بذبحة مجهودية مع تخطيط قلب <bdi>normal</bdi> بالراحة وخطورة <bdi>low</bdi> إلى متوسطة، اختبار المجهود بتخطيط القلب هو الـ<bdi>step</bdi> التشخيصية الأولى.",
    "comparison": None,
    "guideline_note": None,
},
447: {
    "idea": "شاب بدأ برنامج تمارين حديثًا وصار عنده ألم صدري موضعي <bdi>acute</bdi> يزيد بالحركة، وهذا نمط ألم عضلي هيكلي مو قلبي، والـ<bdi>treatment</bdi> المناسب مسكن بسيط.",
    "clues": [
        ("sharp and constant in intensity", "طبيعة الألم <bdi>acute</bdi> وموضعي، مو ضاغط منتشر كالذبحة"),
        ("increase in seventy with movement", "الألم يتأثر بالحركة، يوجه ل<bdi>cause</bdi> عضلي هيكلي مو قلبي"),
        ("started active exercise program a week prior", "<bdi>cause</bdi> واضح لإجهاد عضلي حديث بجدار الصدر"),
    ],
    "why_correct": [
        "طبيعة الألم الـ<bdi>acute</bdi> الموضعي المرتبط بالحركة بعد بدء تمارين حديثة يوجه لألم عضلي هيكلي بجدار الصدر (costochondritis أو إجهاد عضلي)، مو ذبحة قلبية.",
        "<bdi>Ibuprofen</bdi> مسكن ومضاد التهاب مناسب ل<bdi>treatment</bdi> الألم العضلي الهيكلي وتخفيف الالتهاب الموضعي المصاحب.",
        "الـ<bdi>signs</bdi> الحيوية <bdi>normal</bdi> تمامًا بدون أي مؤشر إقفار قلبي، فما يستدعي <bdi>treatment</bdi> قلبي زي النتروجليسرين أو الحاصرات.",
    ],
    "when_changes": [
        "لو كان الألم ضاغط منتشر للذراع أو الفك ويزيد بالمجهود القلبي مو بالحركة الموضعية، يصير التفكير ب<bdi>angina</bdi> حقيقية أقوى.",
        "لو استمر الألم رغم المسكنات لأكثر من أسبوعين، يستحق إعادة <bdi>assessment</bdi> لاستبعاد <bdi>causes</bdi> أخرى.",
    ],
    "rule": "ألم صدري <bdi>acute</bdi> موضعي يزيد بالحركة بعد مجهود عضلي حديث يوجه ل<bdi>cause</bdi> عضلي هيكلي، وعلاجه مسكن بسيط مثل <bdi>ibuprofen</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
448: {
    "idea": "<bdi>patient</bdi> عندها <bdi>murmur</bdi> انقباضية قاسية تنتشر للرقبة (تشير ل<bdi>aortic stenosis</bdi>)، والسؤال يبي أهم <bdi>factor</bdi> يحدد توقيت الجراحة ل<bdi>aortic stenosis</bdi>.",
    "clues": [
        ("harsh ejection systolic murmur, which propagated to the neck", "<bdi>murmur</bdi> كلاسيكية ل<bdi>aortic stenosis</bdi>"),
    ],
    "why_correct": [
        "ظهور <bdi>symptoms</bdi> الـ<bdi>patient</bdi> (ضيق نفس، ذبحة، إغماء) هو الـ<bdi>factor</bdi> الأهم والحاسم بتحديد توقيت التدخل الجراحي ب<bdi>aortic stenosis</bdi>، بغض النظر عن شدة الـ<bdi>murmur</bdi> وحدها.",
        "المرضى عديمو الـ<bdi>symptoms</bdi> عادة يتابعون بدون جراحة فورية حتى لو كان التضيق <bdi>severe</bdi> بالفحوصات، لأن الجراحة المبكرة بدون <bdi>symptoms</bdi> ما تحسن الـ<bdi>results</bdi> بشكل واضح.",
        "شدة الـ<bdi>murmur</bdi> أو تضخم البطين الأيسر مؤشرات مساعدة بس ما تعتبر الـ<bdi>factor</bdi> الحاسم وحدها لتحديد توقيت الجراحة.",
    ],
    "when_changes": [
        "لو ظهرت <bdi>signs</bdi> ضعف <bdi>severe</bdi> بوظيفة البطين الأيسر حتى بدون <bdi>symptoms</bdi> واضحة، ممكن تصير الجراحة مبررة أبكر من المعتاد.",
        "لو كانت الـ<bdi>patient</bdi> عديمة الـ<bdi>symptoms</bdi> تمامًا مع تضيق <bdi>mild</bdi> إلى متوسط، تكتفي بالـ<bdi>follow-up</bdi> الدورية بدون جراحة.",
    ],
    "rule": "ظهور الـ<bdi>symptoms</bdi> هو الـ<bdi>factor</bdi> الأهم بتحديد توقيت جراحة <bdi>aortic stenosis</bdi>، مو شدة الـ<bdi>murmur</bdi> أو درجة <bdi>cardiomegaly</bdi> وحدهم.",
    "comparison": None,
    "guideline_note": None,
},
449: {
    "idea": "<bdi>patient</bdi> <bdi>aortic stenosis</bdi> بدون أي <bdi>symptoms</bdi> ووظيفة بطين أيسر <bdi>normal</bdi> ودرجة تضيق <bdi>mild</bdi> إلى متوسطة (تدرج 40)، والسؤال يبي أنسب تصرف بهالمرحلة المبكرة.",
    "clues": [
        ("no history of chest pain, shortness of breath nor syncope", "الـ<bdi>patient</bdi> عديم الـ<bdi>symptoms</bdi> تمامًا"),
        ("good left ventricular systolic function", "وظيفة القلب سليمة، تدعم تأجيل التدخل"),
        ("Aortic valve gradient of 40 mmH", "درجة تضيق متوسطة تقريبًا، مو <bdi>severe</bdi> جدًا"),
    ],
    "why_correct": [
        "ب<bdi>patient</bdi> عديم الـ<bdi>symptoms</bdi> ووظيفة بطين أيسر <bdi>normal</bdi> ودرجة تضيق متوسطة، الأنسب هو الـ<bdi>follow-up</bdi> الدورية (follow-up) بدون تدخل فوري.",
        "الجراحة المبكرة بدون <bdi>symptoms</bdi> أو ضعف وظيفي ما تحسن الـ<bdi>results</bdi> على المدى الطويل مقارنة بالـ<bdi>follow-up</bdi> المنتظمة بالفحص والـ<bdi>echo</bdi>.",
        "استبدال الصمام أو رأب الصمام يحجزون لحالات الـ<bdi>symptoms</bdi> الواضحة أو التضيق الـ<bdi>severe</bdi> جدًا أو ضعف وظيفة البطين.",
    ],
    "when_changes": [
        "لو ظهرت <bdi>symptoms</bdi> جديدة (ذبحة، ضيق نفس، إغماء) أثناء الـ<bdi>follow-up</bdi>، يصير استبدال الصمام الجراحي هو الـ<bdi>step</bdi> التالية المناسبة.",
        "لو تدهورت وظيفة البطين الأيسر أثناء الـ<bdi>follow-up</bdi> رغم غياب الـ<bdi>symptoms</bdi>، يصير التدخل الجراحي مبررًا أيضًا.",
    ],
    "rule": "<bdi>aortic stenosis</bdi> الـ<bdi>mild</bdi> إلى المتوسط بدون <bdi>symptoms</bdi> ووظيفة بطين <bdi>normal</bdi> يتابع دوريًا بدون تدخل فوري.",
    "comparison": None,
    "guideline_note": None,
},
450: {
    "idea": "<bdi>patient</bdi> ضغط جاء ب<bdi>palpitations</bdi> <bdi>acute</bdi> وتسرع قلب سريع جدًا (170) وضغط دم مستقر نسبيًا، مع نبض غير منتظم يوحي ب<bdi>atrial fibrillation</bdi> حديث، والسؤال يبي أفضل <bdi>treatment</bdi> فوري.",
    "clues": [
        ("pulse rate of 170/min", "تسرع قلب <bdi>severe</bdi> يحتاج تحكم سريع"),
        ("irregular pulse with normal cardiac and chest examinations", "نبض غير منتظم يوجه ل<bdi>atrial fibrillation</bdi>"),
        ("Oxygen saturation 91", "نقص أكسجين <bdi>mild</bdi> يدعم الحاجة ل<bdi>treatment</bdi> فوري بدون تأخير"),
    ],
    "why_correct": [
        "<bdi>Amiodarone</bdi> خيار فعال وآمن نسبيًا للتحكم بمعدل ضربات القلب وحتى إعادة النظم بمرضى <bdi>atrial fibrillation</bdi> الـ<bdi>acute</bdi> السريع، خصوصًا بوجود <bdi>diseases</bdi> قلبية مصاحبة.",
        "الـ<bdi>patient</bdi> مستقر نسبيًا من ناحية الضغط، فما يحتاج تقويم نظم كهربائي طارئ فورًا، لكن السرعة الـ<bdi>severe</bdi> تستدعي <bdi>treatment</bdi> دوائي فعال بسرعة.",
        "المراقبة وحدها (observation) غير كافية بمعدل ضربات قلب <bdi>elevated</bdi> جدًا (170) مع نقص أكسجين مصاحب.",
    ],
    "when_changes": [
        "لو صار الـ<bdi>patient</bdi> غير مستقر (هبوط ضغط <bdi>severe</bdi> أو فقدان وعي)، يصير تقويم النظم الكهربائي الفوري (cardioversion) هو الخيار الصحيح.",
        "لو كان التسرع منتظم بدل غير منتظم، يصير أدينوسين خيار تشخيصي وعلاجي مناسب أولًا.",
    ],
    "rule": "ب<bdi>atrial fibrillation</bdi> سريع ب<bdi>patient</bdi> مستقر نسبيًا، <bdi>amiodarone</bdi> خيار فعال للتحكم بمعدل ضربات القلب أو إعادة النظم.",
    "comparison": None,
    "guideline_note": None,
},
451: {
    "idea": "<bdi>patient</bdi> عنده تاريخ <bdi>tuberculosis</bdi> قديم وضيق نفس تدريجي مع ارتفاع الضغط الوريدي الذي يزيد بالشهيق (<bdi>sign</bdi> كوسماول) بدون <bdi>murmurs</bdi> قلبية، وهذي صورة كلاسيكية ل<bdi>pericarditis</bdi> المضيق.",
    "clues": [
        ("past history of old tuberculosis", "<bdi>factor</bdi> <bdi>risk</bdi> رئيسي ل<bdi>pericarditis</bdi> المضيق الـ<bdi>chronic</bdi>"),
        ("JVP was elevated and rises further on inspiration", "<bdi>sign</bdi> كوسماول الكلاسيكية ل<bdi>pericarditis</bdi> المضيق"),
        ("Cardiac examination was normal with no murmurs", "استبعاد <bdi>diseases</bdi> الصمامات ك<bdi>cause</bdi> لل<bdi>symptoms</bdi>"),
    ],
    "why_correct": [
        "التاريخ المرضي لل<bdi>tuberculosis</bdi> من أشهر <bdi>causes</bdi> <bdi>pericarditis</bdi> الـ<bdi>chronic</bdi> اللي يتطور لتليف وتضيق التامور (constrictive pericarditis) بعد سنوات.",
        "ارتفاع الضغط الوريدي الذي يزيد بالشهيق (<bdi>sign</bdi> كوسماول) <bdi>sign</bdi> مميزة لتضيق التامور ب<bdi>cause</bdi> عدم قدرة القلب على التمدد بحرية.",
        "غياب الـ<bdi>murmurs</bdi> القلبية يستبعد <bdi>diseases</bdi> الصمامات، ويدعم كون المشكلة ميكانيكية بالتامور المحيط بالقلب مو بعضلة القلب أو صماماته.",
    ],
    "when_changes": [
        "لو كان الضغط الوريدي ينخفض بالشهيق بشكل <bdi>normal</bdi> بدل الارتفاع، يستبعد تضيق التامور ويوجه ل<bdi>diagnosis</bdi> ثاني.",
        "لو ظهرت <bdi>murmur</bdi> قلبية واضحة مع تضخم قلب عام بدون تاريخ <bdi>tuberculosis</bdi>، يصير <bdi>cardiomyopathy</bdi> احتمال أقوى.",
    ],
    "rule": "تاريخ <bdi>tuberculosis</bdi> قديم مع ارتفاع الضغط الوريدي الذي يزيد بالشهيق (<bdi>sign</bdi> كوسماول) وغياب الـ<bdi>murmurs</bdi> يشخص <bdi>constrictive pericarditis</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
452: {
    "idea": "السؤال يبي المعيار الرقمي المعتمد لاعتبار <bdi>mitral stenosis</bdi> <bdi>case</bdi> حرجة (critical) حسب مساحة فتحة الصمام.",
    "clues": [
        ("mitral valve orifice measurement is consider critical", "يبي القيمة الرقمية المحددة للتضيق الحرج"),
    ],
    "why_correct": [
        "تعتبر مساحة فتحة الصمام التاجي أقل من 1 سم² هي الحد المعتمد لتصنيف <bdi>mitral stenosis</bdi> على أنه حرج (critical mitral stenosis).",
        "بهالدرجة من التضيق، تكون الـ<bdi>symptoms</bdi> عادة <bdi>severe</bdi> جدًا حتى بالراحة، ويحتاج الـ<bdi>patient</bdi> تدخل عاجل غالبًا.",
        "القيم الأكبر (أقل من 2 أو 3 أو 4 سم) تمثل درجات أخف من التضيق، وما توصف عادة بأنها حرجة.",
    ],
    "when_changes": [
        "لو كانت مساحة الفتحة بين 1 و1.5 سم²، يصنف التضيق <bdi>severe</bdi> لكن مو بالضرورة حرج بنفس الدرجة.",
        "لو كانت المساحة أكبر من 1.5 سم²، يعتبر التضيق <bdi>mild</bdi> إلى متوسط وغالبًا يكتفى بالـ<bdi>follow-up</bdi>.",
    ],
    "rule": "مساحة فتحة الصمام التاجي أقل من 1 سم² هي الحد المعتمد لتصنيف <bdi>mitral stenosis</bdi> على أنه حرج.",
    "comparison": None,
    "guideline_note": None,
},
453: {
    "idea": "<bdi>patient</bdi> احتشاء سفلي عولج بالتحلل الخثري وصار بعد يومين تدهور <bdi>acute</bdi> مع <bdi>murmur</bdi> انقباضية جديدة تنتشر للإبط و<bdi>congestion</bdi> رئوي <bdi>severe</bdi>، وهذي صورة كلاسيكية لتمزق العضلة الحليمية.",
    "clues": [
        ("2 days later acutely unwell with sever dyspnea", "تدهور مفاجئ بعد أيام من الاحتشاء، يوجه ل<bdi>complication</bdi> ميكانيكية"),
        ("loud systolic murmur at the apex, which radiates to the axilla", "<bdi>murmur</bdi> <bdi>mitral regurgitation</bdi> <bdi>acute</bdi> جديدة، مميزة لتمزق العضلة الحليمية"),
        ("bilateral crackles at the base of the lungs", "وذمة رئوية <bdi>acute</bdi> <bdi>result</bdi> القصور التاجي الـ<bdi>acute</bdi> المفاجئ"),
    ],
    "why_correct": [
        "تمزق العضلة الحليمية <bdi>complication</bdi> ميكانيكية معروفة تحصل بعد أيام من الاحتشاء السفلي (ب<bdi>cause</bdi> إصابة الشريان التاجي الأيمن المغذي للعضلة الحليمية الخلفية الإنسية).",
        "الـ<bdi>murmur</bdi> الانقباضية الجديدة الصاخبة عند القمة المنتشرة للإبط مع تدهور <bdi>acute</bdi> وذمة رئوية تطابق تمامًا هالصورة السريرية.",
        "التدهور السريع خلال يومين فقط بعد الاحتشاء يميز هالمضاعفة الميكانيكية الـ<bdi>acute</bdi> عن باقي التفسيرات الأبطأ تطورًا.",
    ],
    "when_changes": [
        "لو كان التدهور بدون <bdi>murmur</bdi> قلبية جديدة واضحة مع انخفاض ضغط <bdi>severe</bdi> فقط، يصير الـ<bdi>diagnosis</bdi> أقرب لصدمة قلبية عامة بدون <bdi>cause</bdi> ميكانيكي محدد.",
        "لو كانت الـ<bdi>murmur</bdi> موجودة قبل الاحتشاء أصلًا بدون تغير مفاجئ، يستبعد تمزق العضلة الحليمية الـ<bdi>acute</bdi>.",
    ],
    "rule": "<bdi>murmur</bdi> انقباضية جديدة صاخبة مع وذمة رئوية <bdi>acute</bdi> بعد أيام من احتشاء سفلي تشخص <bdi>rupture of papillary muscle</bdi> لحين إثبات العكس.",
    "comparison": None,
    "guideline_note": None,
},
454: {
    "idea": "<bdi>patient</bdi> قصور قلب محتاج تحكم بمعدل ضربات القلب ب<bdi>cause</bdi> <bdi>atrial fibrillation</bdi> مصاحب، والسؤال يبي أفضل دواء يحقق هالهدف بأمان بوجود ضعف القلب.",
    "clues": [
        ("heart failure requires rate control", "الهدف تحديدًا تحكم بمعدل ضربات القلب بوجود ضعف وظيفة القلب"),
        ("coexisting atrial fibrillation", "الـ<bdi>disease</bdi> الأساسي المطلوب علاجه"),
    ],
    "why_correct": [
        "<bdi>Digoxin</bdi> خيار مناسب للتحكم بمعدل ضربات القلب ب<bdi>atrial fibrillation</bdi> بمرضى <bdi>heart failure</bdi>، لأنه ما يضعف قوة انقباض القلب بعكس بعض الأدوية الأخرى.",
        "بالإضافة لدوره بالتحكم بالمعدل، الـ<bdi>digoxin</bdi> له أثر إيجابي بسيط على قوة انقباض القلب، وهذا مفيد بوجود ضعف قلب أصلًا.",
        "أدينوسين ونتروجليسرين ما يستخدمون للتحكم الـ<bdi>chronic</bdi> بمعدل ضربات القلب ب<bdi>atrial fibrillation</bdi>، والليدوكايين دواء لاضطراب نظم بطيني مو أذيني.",
    ],
    "when_changes": [
        "لو كانت وظيفة القلب <bdi>normal</bdi> بدون قصور قلب، يصير حاصر بيتا أو حاصر قنوات كالسيوم خيار أول أفضل للتحكم بالمعدل.",
        "لو كان الـ<bdi>patient</bdi> غير مستقر أو الـ<bdi>symptoms</bdi> <bdi>severe</bdi> جدًا، يصير التفكير بتقويم النظم الكهربائي أو استراتيجية إعادة النظم بدل التحكم بالمعدل فقط.",
    ],
    "rule": "بمرضى <bdi>heart failure</bdi> مع <bdi>atrial fibrillation</bdi>، <bdi>digoxin</bdi> خيار آمن وفعال للتحكم بمعدل ضربات القلب بدون إضعاف انقباض القلب.",
    "comparison": None,
    "guideline_note": None,
},
455: {
    "idea": "شابة سليمة تمامًا وجدوا عندها <bdi>murmur</bdi> انبساطية متوسطة الشدة عند القمة صدفة، والسؤال يبي أفضل فحص تالي لتوضيح <bdi>cause</bdi> الـ<bdi>murmur</bdi> وتقييمها.",
    "clues": [
        ("Asymptomatic healthy 24-year-old woman", "غياب الـ<bdi>symptoms</bdi> يدعم كون الـ<bdi>assessment</bdi> أولي غير طارئ"),
        ("grade II mid-diastolic murmur over the apex", "<bdi>murmur</bdi> انبساطية تحتاج <bdi>assessment</bdi> تركيبي دقيق للصمام"),
    ],
    "why_correct": [
        "<bdi>Echocardiography</bdi> هو الفحص الأنسب والأول ل<bdi>assessment</bdi> أي <bdi>murmur</bdi> قلبية جديدة، لأنه يوضح تركيب الصمامات وحركتها وشدة أي تضيق أو قصور بدقة وبدون تدخل جراحي.",
        "هالفحص غير جراحي وآمن ومتاح، ويعطي <bdi>diagnosis</bdi> واضح ل<bdi>cause</bdi> الـ<bdi>murmur</bdi> الانبساطية (زي <bdi>mitral stenosis</bdi> <bdi>mild</bdi>) ب<bdi>step</bdi> واحدة.",
        "قسطرة القلب والرنين المغناطيسي <bdi>procedures</bdi> أكثر تعقيدًا وتكلفة، تحجز لحالات محددة بعد <bdi>results</bdi> الـ<bdi>echo</bdi> غير الحاسمة.",
    ],
    "when_changes": [
        "لو كان فيه تاريخ حمى روماتيزمية أو التهاب حلق سابق موثق، يصير فحص Antistreptolysin O مفيد كدليل مساعد بجانب الـ<bdi>echo</bdi>.",
        "لو كانت الـ<bdi>murmur</bdi> انقباضية بسيطة عند نفس الـ<bdi>patient</bdi> السليمة، ممكن تكون <bdi>murmur</bdi> وظيفية بريئة لا تحتاج تصوير إضافي.",
    ],
    "rule": "أي <bdi>murmur</bdi> قلبية جديدة، أول <bdi>step</bdi> تقييمها هي <bdi>echocardiography</bdi> لتوضيح التركيب والوظيفة.",
    "comparison": None,
    "guideline_note": None,
},
456: {
    "idea": "<bdi>patient</bdi> قصور قلب مستقر على <bdi>treatment</bdi> أساسي (مثبط ACE ومدر بولي)، والسؤال يبي دواء إضافي يحسّن البقاء طويل المدى بمرحلة استقرار الـ<bdi>symptoms</bdi>.",
    "clues": [
        ("poor left ventricular function", "قصور قلب انقباضي مؤكد بالـ<bdi>echo</bdi>"),
        ("good control of his symptoms", "الـ<bdi>patient</bdi> مستقر حاليًا، مناسب لإضافة دواء يحسن البقاء طويل المدى"),
    ],
    "why_correct": [
        "<bdi>Carvedilol</bdi> حاصر بيتا مثبت بدراسات كبرى إنه يقلل الوفيات ب<bdi>heart failure</bdi> الانقباضي الـ<bdi>chronic</bdi> لما يضاف بعد استقرار الـ<bdi>patient</bdi> على الـ<bdi>treatment</bdi> الأساسي.",
        "يبدأ حاصر البيتا بجرعة <bdi>low</bdi> جدًا ويرفع تدريجيًا فقط بعد التأكد من استقرار <bdi>case</bdi> الـ<bdi>patient</bdi> (بدون <bdi>congestion</bdi> <bdi>acute</bdi>)، وهذا متحقق هنا.",
        "<bdi>Digoxin</bdi> ونيفيديبين وهيدرالازين ما يعتبرون الـ<bdi>step</bdi> القياسية التالية ب<bdi>patient</bdi> مستقر جاهز لإضافة حاصر بيتا.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> غير مستقر ب<bdi>symptoms</bdi> <bdi>congestion</bdi> <bdi>acute</bdi>، لازم تأجيل بدء حاصر البيتا لحين الاستقرار أولًا.",
        "لو ما تحمّل حاصر البيتا ل<bdi>cause</bdi> معين (<bdi>asthma</bdi> <bdi>severe</bdi> مثلًا)، يصير التفكير بخيارات بديلة زي hydralazine مع نترات.",
    ],
    "rule": "بعد استقرار <bdi>patient</bdi> <bdi>heart failure</bdi> على الـ<bdi>treatment</bdi> الأساسي، يضاف حاصر بيتا (زي carvedilol) تدريجيًا لتحسين البقاء طويل المدى.",
    "comparison": None,
    "guideline_note": None,
},
457: {
    "idea": "<bdi>patient</bdi> بدون <bdi>factors</bdi> <bdi>risk</bdi> واضحة وخطورة قلبية متوسطة حسب معادلة Pooled Cohort، والسؤال يبي فحص إضافي يساعد يعيد تصنيف الخطورة بدقة أكبر.",
    "clues": [
        ("no chronic health issues and takes no medications", "خطورة أساسية <bdi>low</bdi> نسبيًا من ناحية التاريخ المرضي"),
        ("intermediate risk of myocardial infarction", "درجة خطورة متوسطة تحتاج فحص إضافي لتوضيح القرار العلاجي"),
    ],
    "why_correct": [
        "<bdi>High-sensitivity C-reactive protein</bdi> فحص دم بسيط يستخدم لإعادة تصنيف الخطورة القلبية عند المرضى متوسطي الخطورة لمساعدة القرار بشأن بدء <bdi>treatment</bdi> وقائي (زي الـ<bdi>statin</bdi>).",
        "هالفحص غير جراحي وغير مكلف ومناسب ك<bdi>step</bdi> أولى إضافية قبل التفكير بفحوصات تصويرية أكثر تعقيدًا.",
        "فحوصات التصوير (تصوير الشرايين بالأشعة المقطعية أو الرنين المغناطيسي) أكثر تعقيدًا وتكلفة، وتحجز عادة لحالات أعلى خطورة أو بعد <bdi>results</bdi> غير حاسمة.",
    ],
    "when_changes": [
        "لو كانت الخطورة عالية من البداية (أكثر من 20%)، يبدأ الـ<bdi>treatment</bdi> الوقائي مباشرة بدون حاجة لفحوصات إعادة تصنيف إضافية.",
        "لو طلع الـhs-CRP <bdi>elevated</bdi>، هذا يدعم بدء <bdi>treatment</bdi> وقائي بالـ<bdi>statin</bdi> حتى لو كانت الخطورة الأساسية متوسطة فقط.",
    ],
    "rule": "عند خطورة قلبية متوسطة بمعادلة المخاطر، يستخدم hs-CRP كفحص بسيط يساعد في إعادة تصنيف القرار العلاجي.",
    "comparison": None,
    "guideline_note": None,
},
458: {
    "idea": "<bdi>patient</bdi> بدون <bdi>symptoms</bdi> قلبية طلع عندها بالصدفة <bdi>murmur</bdi> انبساطية <bdi>mild</bdi> عند القمة، والسؤال يبي أفضل فحص تالي لتوضيح <bdi>cause</bdi> هالـ<bdi>murmur</bdi>.",
    "clues": [
        ("grade 2/6 diastolic murmur heard best over the apex", "<bdi>murmur</bdi> انبساطية تحتاج <bdi>assessment</bdi> تركيبي بالـ<bdi>echo</bdi>"),
        ("Peripheral pulses are normal", "استبعاد <bdi>causes</bdi> ثانية مؤثرة على النبض الطرفي"),
    ],
    "why_correct": [
        "<bdi>Transthoracic echocardiography</bdi> هو الفحص الأول والأنسب ل<bdi>assessment</bdi> أي <bdi>murmur</bdi> قلبية جديدة مكتشفة بالصدفة، لتوضيح تركيب الصمامات وحركتها.",
        "هالفحص غير جراحي وآمن تمامًا، ويعطي معلومات كافية لتحديد <bdi>cause</bdi> الـ<bdi>murmur</bdi> الانبساطية دون الحاجة ل<bdi>procedure</bdi> أكثر تعقيدًا.",
        "الـ<bdi>echo</bdi> عبر المريء والأشعة المقطعية للشرايين <bdi>procedures</bdi> أكثر تدخلًا تحجز لحالات محددة بعد <bdi>results</bdi> غير حاسمة من الـ<bdi>echo</bdi> العادي.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>echo</bdi> العادي غير واضح ب<bdi>cause</bdi> صعوبة تقنية (سمنة مثلًا)، يصير الـ<bdi>echo</bdi> عبر المريء الـ<bdi>step</bdi> التالية المناسبة.",
        "لو كانت الـ<bdi>murmur</bdi> <bdi>mild</bdi> جدًا (درجة 1) بدون أي <bdi>symptoms</bdi> أو تغيرات بتخطيط القلب، ممكن يكتفى بالـ<bdi>follow-up</bdi> السريرية فقط بدون تصوير.",
    ],
    "rule": "أي <bdi>murmur</bdi> قلبية مكتشفة بالصدفة، الـ<bdi>step</bdi> الأولى تقييمها هي <bdi>transthoracic echocardiography</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
459: {
    "idea": "<bdi>patient</bdi> <bdi>atrial fibrillation</bdi> سابق حاليًا بنظم جيبي <bdi>normal</bdi> ومستقرة، عندها أيضًا تاريخ سكتة دماغية عابرة وضغط، والسؤال يبي القرار الصحيح بشأن استمرار مضاد التخثر.",
    "clues": [
        ("transient ischemic attack and hypertension", "<bdi>factors</bdi> <bdi>risk</bdi> إضافية ترفع احتمال تكرار الـ<bdi>thrombus</bdi> الدماغية"),
        ("most recent electrocardiogram shows normal sinus rhythm", "عودة النظم الـ<bdi>normal</bdi> حاليًا بس ما يلغي <bdi>risk</bdi> تكرار الرجفان مستقبلًا"),
    ],
    "why_correct": [
        "رغم عودة النظم الـ<bdi>normal</bdi> حاليًا، الـ<bdi>patient</bdi> عندها <bdi>factors</bdi> <bdi>risk</bdi> عالية (تاريخ سكتة دماغية وضغط) تجعل <bdi>risk</bdi> تكرار الرجفان والـ<bdi>thrombus</bdi> الدماغية <bdi>elevated</bdi>، فالاستمرار على <bdi>warfarin</bdi> هو القرار الأصح.",
        "<bdi>atrial fibrillation</bdi> غالبًا يتكرر حتى لو رجع النظم <bdi>normal</bdi> لفترة، خصوصًا بوجود <bdi>factors</bdi> <bdi>risk</bdi> قلبية وعائية مصاحبة.",
        "إيقاف مضاد التخثر ب<bdi>patient</bdi> عالية الخطورة يعرضها ل<bdi>risk</bdi> <bdi>thrombus</bdi> دماغية جديدة رغم استقرار النظم مؤقتًا.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>patient</bdi> <bdi>low</bdi> الخطورة تمامًا (بدون تاريخ سكتة أو ضغط) وبقي النظم <bdi>normal</bdi> لفترة طويلة موثقة، ممكن يفكر بإيقاف مضاد التخثر تدريجيًا.",
        "لو تكرر <bdi>atrial fibrillation</bdi> فعليًا أثناء الـ<bdi>follow-up</bdi>، يتأكد أكثر ضرورة الاستمرار على مضاد التخثر طويل المدى.",
    ],
    "rule": "ب<bdi>patient</bdi> <bdi>atrial fibrillation</bdi> عالي الخطورة (تاريخ سكتة دماغية وضغط)، يستمر مضاد التخثر حتى لو عاد النظم الجيبي الـ<bdi>normal</bdi> مؤقتًا.",
    "comparison": None,
    "guideline_note": None,
},
460: {
    "idea": "<bdi>patient</bdi> قصور قلب <bdi>acute</bdi> مع <bdi>congestion</bdi> رئوي وبي إن بي <bdi>elevated</bdi> بشدة، ووظيفة الضخ محفوظة (EF 60%) والصمامات <bdi>normal</bdi>، والسؤال يبي أفضل <bdi>step</bdi> علاجية فورية لتخفيف الـ<bdi>congestion</bdi>.",
    "clues": [
        ("raised central venous pressure, fine crackles at lung bases and hepatomegaly", "<bdi>congestion</bdi> جهازي ورئوي واضح"),
        ("left ventricular ejection fraction of 60% and normal valves", "قصور قلب بوظيفة ضخ محفوظة، مو انقباضي"),
        ("Brain natriuretic peptide 900", "ارتفاع واضح يؤكد الـ<bdi>diagnosis</bdi> ويعكس شدة الـ<bdi>congestion</bdi>"),
    ],
    "why_correct": [
        "بغض النظر عن نوع <bdi>heart failure</bdi> (انقباضي أو بوظيفة محفوظة)، الـ<bdi>step</bdi> العلاجية الفورية لتخفيف الـ<bdi>congestion</bdi> الـ<bdi>acute</bdi> هي <bdi>furosemide</bdi> لطرح السوائل الزايدة بسرعة.",
        "المدر البولي يخفف الـ<bdi>congestion</bdi> الرئوي والجهازي بشكل مباشر وسريع، وهو الـ<bdi>treatment</bdi> العرضي الأساسي بغض النظر عن الـ<bdi>cause</bdi> الأساسي طالما ما فيه مانع.",
        "حاصرات القنوات الكالسيومية والبيتا واسبيرونولاكتون ما تعتبر الـ<bdi>step</bdi> الفورية لتخفيف <bdi>congestion</bdi> <bdi>acute</bdi>، رغم إنها قد تفيد لاحقًا حسب الـ<bdi>cause</bdi>.",
    ],
    "when_changes": [
        "لو تكرر <bdi>heart failure</bdi> بوظيفة محفوظة بشكل متكرر، يصير التحكم الدقيق بضغط الدم و<bdi>treatment</bdi> الـ<bdi>cause</bdi> الأساسي (زي الضغط الـ<bdi>chronic</bdi>) هو الأولوية طويلة المدى.",
        "لو صاحب الـ<bdi>congestion</bdi> انخفاض بوظيفة الضخ (EF <bdi>low</bdi>)، يضاف مثبط ACE وحاصر بيتا لاحقًا بعد استقرار الـ<bdi>congestion</bdi> الـ<bdi>acute</bdi>.",
    ],
    "rule": "بأي <bdi>congestion</bdi> رئوي <bdi>acute</bdi> ناتج عن قصور قلب، بغض النظر عن نوعه، المدر البولي الوريدي هو الـ<bdi>step</bdi> العلاجية الفورية الأولى.",
    "comparison": None,
    "guideline_note": None,
},
461: {
    "idea": "حامل عندها <bdi>murmur</bdi> انقباضية عند الحافة القصية العلوية اليمنى تنتشر للرقبة، وموقع الانتشار هذا تحديدًا يوجه الملف لاعتبارها <bdi>aortic stenosis</bdi> مو مجرد <bdi>murmur</bdi> حمل بريئة.",
    "clues": [
        ("30th week of pregnancy", "زيادة حجم الدم المتداول تزيد حدة أي <bdi>murmur</bdi> موجودة مسبقًا أثناء الحمل"),
        ("mid-systolic ejection murmur at the right upper sternal border", "موقع الـ<bdi>murmur</bdi> الكلاسيكي ل<bdi>aortic stenosis</bdi>"),
        ("The murmur radiates to carotids", "انتشار الـ<bdi>murmur</bdi> للرقبة سمة مميزة ل<bdi>aortic stenosis</bdi> الحقيقي"),
    ],
    "why_correct": [
        "الـ<bdi>murmur</bdi> الانقباضية عند الحافة القصية العلوية اليمنى المنتشرة للرقبة توافق الموقع والانتشار الكلاسيكي ل<bdi>murmur</bdi> <bdi>aortic stenosis</bdi>.",
        "انتشار الـ<bdi>murmur</bdi> للرقبة تحديدًا هو ما يميزها عن <bdi>murmur</bdi> الحمل الوظيفية البريئة البسيطة، والملف هنا يعتمد هالتفصيل بالـ<bdi>diagnosis</bdi>.",
        "زيادة حجم الدم وسرعة تدفقه أثناء الحمل تزيد شدة أي <bdi>murmur</bdi> صمامية موجودة أصلًا وتجعلها أوضح بالفحص.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>murmur</bdi> <bdi>mild</bdi> (درجة 1-2) بدون انتشار للرقبة وبدون <bdi>murmur</bdi> انبساطية، يصير الـ<bdi>diagnosis</bdi> الأقرب فسيولوجيًا <bdi>murmur</bdi> الحمل البريئة.",
        "لو صاحبت الـ<bdi>murmur</bdi> <bdi>symptoms</bdi> واضحة (ضيق نفس <bdi>severe</bdi> أو إغماء)، يستحق <bdi>assessment</bdi> عاجل بالـ<bdi>echo</bdi> لتحديد شدة التضيق وأثره على الحمل.",
    ],
    "rule": "<bdi>murmur</bdi> انقباضية عند الحافة العلوية اليمنى تنتشر للرقبة تدفع للتفكير بـ<bdi>aortic stenosis</bdi> الحقيقي مو مجرد <bdi>murmur</bdi> حمل بريئة.",
    "comparison": None,
    "guideline_note": "أغلب الـ<bdi>murmurs</bdi> الانقباضية الـ<bdi>mild</bdi> اللي تظهر أثناء الحمل تكون <bdi>murmur</bdi> حمل فسيولوجية بريئة، خصوصًا لو ما انتشرت للرقبة؛ لكن جواب هالملف يعتمد على أن الانتشار للرقبة هنا يميل بالـ<bdi>diagnosis</bdi> نحو <bdi>aortic stenosis</bdi> حقيقي يستحق الـ<bdi>follow-up</bdi>.",
},
462: {
    "idea": "شاب عنده ألم صدري مستمر يزيد بالانحناء للأمام مع صوت <bdi>pericardial friction rub</bdi> وتغيرات تخطيطية منتشرة (ارتفاع ST مقعر مع انخفاض PR)، وهذي صورة كلاسيكية ل<bdi>pericarditis</bdi> الـ<bdi>acute</bdi>.",
    "clues": [
        ("exacerbated when leaning forward", "<bdi>sign</bdi> كلاسيكية لألم <bdi>pericarditis</bdi>"),
        ("friction rub at the left lower sternal border", "صوت <bdi>pericardial friction rub</bdi>، دليل مباشر على <bdi>pericarditis</bdi>"),
        ("diffuse, concave upward ST-segment elevations and PR-segment depression", "نمط تخطيطي كلاسيكي ل<bdi>pericarditis</bdi> الـ<bdi>acute</bdi>"),
    ],
    "why_correct": [
        "<bdi>Ibuprofen</bdi> من مضادات الالتهاب غير الستيرويدية، وهو الـ<bdi>treatment</bdi> الأساسي الأول ل<bdi>pericarditis</bdi> الـ<bdi>acute</bdi> غير المضاعف لتخفيف الألم والالتهاب.",
        "صوت الـ<bdi>pericardial friction rub</bdi> مع نمط تخطيط القلب المنتشر (ارتفاع ST مقعر مع انخفاض PR بعدة اتجاهات) يؤكد الـ<bdi>diagnosis</bdi> بشكل شبه قاطع.",
        "الستيرويدات تحجز للحالات المقاومة أو المتكررة، والنتروجليسرين يعالج الذبحة القلبية مو <bdi>pericarditis</bdi>، والـ<bdi>warfarin</bdi> غير مناسب أصلًا وقد يزيد <bdi>risk</bdi> نزيف تاموري.",
    ],
    "when_changes": [
        "لو ما استجاب الألم على مضادات الالتهاب غير الستيرويدية أو تكرر الالتهاب، يضاف <bdi>colchicine</bdi> ك<bdi>treatment</bdi> مساعد قياسي.",
        "لو ما استجاب على الـ<bdi>treatment</bdi> المزدوج أو تكرر بشكل متكرر جدًا، يصير التفكير بالستيرويدات كخط <bdi>treatment</bdi> لاحق.",
    ],
    "rule": "<bdi>pericarditis</bdi> الـ<bdi>acute</bdi> غير المضاعف يعالج أولًا بمضادات الالتهاب غير الستيرويدية زي <bdi>ibuprofen</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
463: {
    "idea": "<bdi>patient</bdi> قلبية خارجة من المستشفى بعد احتشاء وتسأل عن الوقاية الثانوية الصحيحة طويلة المدى، والسؤال يبي العبارة الطبية الصحيحة من بين خيارات فيها معلومات خاطئة شائعة.",
    "clues": [
        ("secondary prevention of infarction", "الموضوع المطلوب توضيحه لل<bdi>patient</bdi>"),
    ],
    "why_correct": [
        "مثبطات <bdi>ACE</bdi> ثبت إنها تستخدم إلى أجل غير مسمى (indefinitely) بمرضى معينين بعد الاحتشاء (خصوصًا بضعف وظيفة البطين) لتقليل <bdi>risk</bdi> الأحداث القلبية المستقبلية والوفيات.",
        "مضادات الصفائح مثل الـ<bdi>aspirin</bdi> تستمر طويل المدى وليس لفترة قصيرة فقط، فالعبارة التي تحدد فترة قصيرة غير صحيحة.",
        "الـ<bdi>treatment</bdi> الهرموني التعويضي للنساء بعد سن اليأس ثبت أنه لا يقي من <bdi>diseases</bdi> القلب التاجية، بل قد يزيد بعض المخاطر، فهذا خيار خاطئ طبيًا.",
    ],
    "when_changes": [
        "لو كانت وظيفة البطين <bdi>normal</bdi> تمامًا بدون <bdi>factors</bdi> <bdi>risk</bdi> إضافية، ممكن تقل مدة أو ضرورة استمرار بعض الأدوية حسب <bdi>assessment</bdi> الطبيب المختص.",
        "لو كانت الـ<bdi>patient</bdi> لا تتحمل مثبطات ACE، يستبدل بحاصر مستقبلات الأنجيوتنسين كبديل طويل المدى مشابه بالفائدة.",
    ],
    "rule": "مثبطات <bdi>ACE</bdi> ومضادات الصفائح تستخدم لأجل غير مسمى للوقاية الثانوية بعد احتشاء القلب، بينما الـ<bdi>treatment</bdi> الهرموني التعويضي لا يقي من <bdi>diseases</bdi> القلب.",
    "comparison": None,
    "guideline_note": None,
},
464: {
    "idea": "<bdi>patient</bdi> قصور قلب انقباضي <bdi>chronic</bdi> مستقر مع انخفاض واضح بنسبة الضخ (25%)، والسؤال يبي أهم دواء أساسي يبدأ به علاجها طويل المدى.",
    "clues": [
        ("non-decompensated systolic heart failure", "قصور قلب انقباضي مستقر، مناسب لبدء <bdi>treatment</bdi> أساسي طويل المدى"),
        ("ejection fraction of 25%", "انخفاض <bdi>severe</bdi> بوظيفة الضخ، يؤكد الحاجة ل<bdi>treatment</bdi> معدل للوفيات"),
    ],
    "why_correct": [
        "<bdi>Lisinopril</bdi> من مثبطات ACE، وهو من الأدوية الأساسية اللي تقلل الوفيات وتحسن البقاء بمرضى <bdi>heart failure</bdi> الانقباضي الـ<bdi>chronic</bdi> بغض النظر عن وجود <bdi>symptoms</bdi> <bdi>acute</bdi>.",
        "بدء الـ<bdi>treatment</bdi> بمثبط ACE أساسي بكل مرضى <bdi>heart failure</bdi> الانقباضي المستقرين، ويعتبر حجر الأساس بالـ<bdi>treatment</bdi> طويل المدى.",
        "<bdi>amlodipine</bdi> و<bdi>furosemide</bdi> واسبيرونولاكتون لهم أدوار مختلفة (تحكم بالضغط، تخفيف <bdi>congestion</bdi>، أو إضافة لاحقة)، لكن مثبط ACE هو نقطة البداية الأساسية.",
    ],
    "when_changes": [
        "لو ما تحمّلت الـ<bdi>patient</bdi> مثبط ACE (سعال مزعج مثلًا)، يستبدل بحاصر مستقبلات الأنجيوتنسين.",
        "لو استمرت الـ<bdi>symptoms</bdi> رغم مثبط ACE وحاصر بيتا بجرعات كافية، تضاف اسبيرونولاكتون ك<bdi>step</bdi> تالية لتحسين البقاء أكثر.",
    ],
    "rule": "ب<bdi>heart failure</bdi> الانقباضي الـ<bdi>chronic</bdi>، مثبط <bdi>ACE</bdi> هو الدواء الأساسي الأول اللي يبدأ فيه الـ<bdi>treatment</bdi> طويل المدى.",
    "comparison": None,
    "guideline_note": None,
},
465: {
    "idea": "<bdi>patient</bdi> عندها <bdi>mitral regurgitation</bdi> معروف صار عندها تدهور تدريجي بضيق النفس على مدى 3 أسابيع، والسؤال يبي فحص تصويري دقيق يوضح تشريح الصمام وشدة القصور بأعلى دقة ممكنة.",
    "clues": [
        ("moderate mitral regurgitation", "<bdi>disease</bdi> صمامي معروف مسبقًا يحتاج إعادة <bdi>assessment</bdi> دقيق"),
        ("grade 3/6 holosystolic murmur radiating to the axilla", "<bdi>murmur</bdi> <bdi>mitral regurgitation</bdi> أعلى شدة من المعروفة سابقًا، تدعم تفاقم الـ<bdi>case</bdi>"),
        ("Lungs are clear to auscultation", "لا يوجد <bdi>congestion</bdi> رئوي <bdi>acute</bdi> بعد، يدعم كون الـ<bdi>assessment</bdi> غير طارئ لكنه ضروري"),
    ],
    "why_correct": [
        "بحسب إجابة هالملف، <bdi>Transesophageal echocardiogram (TEE)</bdi> هو الفحص المعتمد هنا لإعطاء صورة أدق وأوضح لتشريح الصمام التاجي وشدة القصور مقارنة بالـ<bdi>echo</bdi> العادي عبر جدار الصدر.",
        "زيادة شدة الـ<bdi>murmur</bdi> إلى درجة 3/6 مع تفاقم الـ<bdi>symptoms</bdi> تستدعي <bdi>assessment</bdi> دقيق جدًا لدرجة القصور قبل اتخاذ قرار علاجي أو جراحي.",
        "قياس التنفس والتصوير المقطعي الحلزوني للصدر ما يقيّمون الصمام القلبي نفسه، فهما بعيدان عن الهدف الأساسي من الفحص هنا.",
    ],
    "when_changes": [
        "بالممارسة السريرية المعتادة، الـ<bdi>step</bdi> الأولى القياسية ل<bdi>assessment</bdi> <bdi>murmur</bdi> قلبية متفاقمة عادة تكون <bdi>transthoracic echocardiogram</bdi> غير الجراحي أولًا، وينتقل لل<bdi>echo</bdi> عبر المريء لو كانت الصورة غير واضحة.",
        "لو كان ضيق النفس مرتبط بنوبات <bdi>asthma</bdi> متكررة بدون تغيّر بشدة الـ<bdi>murmur</bdi>، يصير قياس التنفس (spirometry) مفيد ل<bdi>assessment</bdi> <bdi>asthma</bdi> نفسه.",
    ],
    "rule": "ل<bdi>assessment</bdi> دقيق لشدة القصور التاجي وتشريح الصمام، الـ<bdi>echo</bdi> عبر المريء (<bdi>TEE</bdi>) يعطي تفاصيل أوضح من الـ<bdi>echo</bdi> العادي عبر جدار الصدر.",
    "comparison": None,
    "guideline_note": "بالممارسة السريرية القياسية، الـ<bdi>echo</bdi> عبر جدار الصدر (TTE) غير الجراحي هو الـ<bdi>step</bdi> الأولى المعتادة ل<bdi>assessment</bdi> أي <bdi>murmur</bdi> قلبية متفاقمة، وينتقل لل<bdi>echo</bdi> عبر المريء (TEE) فقط لو كانت صورة TTE غير واضحة أو احتيج تفاصيل تشريحية أدق؛ ومع ذلك الجواب المعتمد على البطاقة هنا يبقى TEE حسب مفتاح هالملف.",
},
466: {
    "idea": "<bdi>patient</bdi> <bdi>aortic stenosis</bdi> عرضي (إغماء مجهودي وضيق نفس ووذمة رئوية) مع <bdi>murmur</bdi> كلاسيكية، والسؤال يبي العبارة الصحيحة طبيًا عن هالحالة من بين خيارات فيها معلومات خاطئة.",
    "clues": [
        ("exertional syncope and progressive shortness of breath", "<bdi>symptoms</bdi> <bdi>aortic stenosis</bdi> <bdi>severe</bdi> عرضي"),
        ("mid-systolic murmur at right upper sternal boarder that radiated to carotids", "<bdi>murmur</bdi> كلاسيكية ل<bdi>aortic stenosis</bdi>"),
        ("clear evidence of pulmonary edema", "دليل على قصور قلب مصاحب بمرحلة متقدمة"),
    ],
    "why_correct": [
        "ظهور <bdi>symptoms</bdi> <bdi>congestive heart failure</bdi> (زي الوذمة الرئوية) ب<bdi>patient</bdi> <bdi>aortic stenosis</bdi> يعتبر مؤشر إنذار سيء جدًا ويرتبط بارتفاع <bdi>risk</bdi> الوفاة إذا ما تم التدخل الجراحي بسرعة.",
        "بمجرد ظهور <bdi>symptoms</bdi> قصور قلب واضحة ب<bdi>aortic stenosis</bdi> الـ<bdi>severe</bdi>، يصبح متوسط البقاء بدون جراحة قصير جدًا (أشهر قليلة تقريبًا)، وهذا <bdi>cause</bdi> أهمية التدخل العاجل.",
        "الـ<bdi>treatment</bdi> الأساسي ل<bdi>aortic stenosis</bdi> العرضي هو استبدال الصمام الجراحي مو المدرات وحدها، والمدرات ممكن تستخدم بحذر <bdi>severe</bdi> فقط ك<bdi>treatment</bdi> مساعد مؤقت.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> عديم الـ<bdi>symptoms</bdi> تمامًا رغم وجود تضيق <bdi>severe</bdi> بالـ<bdi>echo</bdi>، يتغير التوجه لل<bdi>follow-up</bdi> الدورية بدل التأكيد على سوء الإنذار الفوري.",
        "لو كانت الـ<bdi>murmur</bdi> تقل بالوقوف بدل ثباتها، يصير التفكير ب<bdi>murmur</bdi> <bdi>cardiomyopathy</bdi> الضخامي الانسدادي بدل <bdi>aortic stenosis</bdi> الحقيقي.",
    ],
    "rule": "ظهور <bdi>symptoms</bdi> <bdi>heart failure</bdi> ب<bdi>patient</bdi> <bdi>aortic stenosis</bdi> <bdi>severe</bdi> مؤشر إنذار سيء جدًا ويستدعي تدخل جراحي عاجل.",
    "comparison": None,
    "guideline_note": None,
},
467: {
    "idea": "<bdi>patient</bdi> ألم صدري ليلي متكرر يزول بسرعة بالنترات مع قسطرة <bdi>normal</bdi> واختبار إرجونوفين إيجابي، وهذي صورة كلاسيكية لذبحة برينزميتال (التشنج الوعائي التاجي).",
    "clues": [
        ("recurrent severe nocturnal chest pain", "توقيت ليلي متكرر، مميز لذبحة برينزميتال"),
        ("normal cardiac catheterization", "غياب انسداد تاجي تشريحي حقيقي"),
        ("positive ergonovine echocardiography testing", "اختبار تحريضي إيجابي يؤكد التشنج الوعائي"),
    ],
    "why_correct": [
        "<bdi>Nifedipine</bdi> حاصر قنوات كالسيوم فعال جدًا بمنع التشنج الوعائي التاجي المسبب لذبحة برينزميتال، وهو الـ<bdi>treatment</bdi> طويل المدى المفضل كدواء واحد.",
        "قسطرة القلب الـ<bdi>normal</bdi> مع اختبار الإرجونوفين الإيجابي يؤكدان إن المشكلة تشنج وعائي وظيفي مو انسداد تصلبي حقيقي، وهذا يوجه لل<bdi>treatment</bdi> بحاصرات الكالسيوم.",
        "حاصرات بيتا (مثل carvedilol) قد تزيد سوء التشنج الوعائي التاجي أحيانًا، فهي أقل ملاءمة هنا مقارنة بحاصرات الكالسيوم.",
    ],
    "when_changes": [
        "لو كانت القسطرة تظهر انسداد تصلبي حقيقي بدل التشنج الوعائي، يصير الـ<bdi>treatment</bdi> الأساسي مختلف تمامًا (توسيع الشريان أو جراحة).",
        "لو ما استجابت الـ<bdi>symptoms</bdi> على حاصر كالسيوم واحد، يضاف نترات طويلة المفعول ك<bdi>treatment</bdi> مساعد ثاني.",
    ],
    "rule": "ذبحة برينزميتال (التشنج الوعائي التاجي) تعالج بحاصرات قنوات الكالسيوم مثل <bdi>nifedipine</bdi> ك<bdi>treatment</bdi> أساسي طويل المدى.",
    "comparison": None,
    "guideline_note": None,
},
468: {
    "idea": "<bdi>patient</bdi> <bdi>aortic stenosis</bdi> عرضي (ضيق نفس مع إغماء) و<bdi>murmur</bdi> كلاسيكية وتضخم قلب وتضخم بطين أيسر بالتخطيط، والسؤال يبي الـ<bdi>treatment</bdi> النهائي المناسب ل<bdi>aortic stenosis</bdi> عرضي و<bdi>severe</bdi>.",
    "clues": [
        ("progressive exertional shortness of breath that associated with syncope", "<bdi>symptoms</bdi> <bdi>aortic stenosis</bdi> <bdi>severe</bdi> وعرضي"),
        ("mid-systolic murmur at right upper sternal boarder that radiates to carotids", "<bdi>murmur</bdi> كلاسيكية ل<bdi>aortic stenosis</bdi>"),
        ("ECG reveals left ventricular hypertrophy", "تضخم بطين أيسر <bdi>result</bdi> مقاومة التضيق الـ<bdi>chronic</bdi>"),
    ],
    "why_correct": [
        "ب<bdi>patient</bdi> <bdi>aortic stenosis</bdi> عرضي (إغماء وضيق نفس)، الـ<bdi>treatment</bdi> النهائي المطلوب هو <bdi>surgical valvular replacement</bdi>، لأن الأدوية لا تعالج التضيق التشريحي نفسه.",
        "الـ<bdi>symptoms</bdi> العرضية ب<bdi>aortic stenosis</bdi> الـ<bdi>severe</bdi> مؤشر واضح على ضرورة التدخل الجراحي العاجل، لأن التأخير يزيد <bdi>risk</bdi> الوفاة المفاجئة.",
        "خفض الضغط بقوة أو استخدام موسعات وعائية أو مدرات ب<bdi>aortic stenosis</bdi> <bdi>severe</bdi> قد يكون <bdi>risk</bdi> لأنه يقلل التروية التاجية والدماغية بشكل مفاجئ.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> عالي الخطورة جراحيًا وغير مرشح للجراحة المفتوحة، يصير <bdi>TAVI</bdi> (استبدال الصمام عبر القسطرة) بديل مناسب.",
        "لو كان الـ<bdi>patient</bdi> عديم الـ<bdi>symptoms</bdi> تمامًا رغم التضيق الـ<bdi>severe</bdi>، يكتفى بالـ<bdi>follow-up</bdi> الدورية بدل الجراحة الفورية.",
    ],
    "rule": "<bdi>aortic stenosis</bdi> الـ<bdi>severe</bdi> العرضي يعالج جراحيًا باستبدال الصمام، ولا تكفي الأدوية وحدها ل<bdi>treatment</bdi> التضيق التشريحي.",
    "comparison": None,
    "guideline_note": None,
},
469: {
    "idea": "شاب عنده ألم صدري مفاجئ يخف بالانحناء للأمام مع صوت <bdi>pericardial friction rub</bdi> وارتفاع منتشر بتخطيط القلب، وأنزيمات القلب <bdi>normal</bdi>، وهذي صورة <bdi>pericarditis</bdi> الـ<bdi>acute</bdi> بدون التهاب عضلة قلب مصاحب.",
    "clues": [
        ("chest pain that reduced with sitting forward", "<bdi>sign</bdi> كلاسيكية لألم <bdi>pericarditis</bdi>"),
        ("friction rub", "دليل مباشر على <bdi>pericarditis</bdi>"),
        ("cardiac enzymes are within normal range", "استبعاد إصابة عضلة القلب المصاحبة (التهاب عضلة قلب أو احتشاء)"),
        ("ECG shows diffuse ST segment elevation", "نمط تخطيطي كلاسيكي منتشر ل<bdi>pericarditis</bdi>"),
    ],
    "why_correct": [
        "أنزيمات القلب الـ<bdi>normal</bdi> مع صوت الـ<bdi>friction rub</bdi> والتخطيط الكلاسيكي تؤكد التهاب تامور <bdi>acute</bdi> بدون إصابة عضلة قلب مصاحبة، والـ<bdi>treatment</bdi> الأساسي مضاد التهاب غير ستيرويدي.",
        "<bdi>NSAID</bdi> يخفف الألم والالتهاب بسرعة وفعالية بالغالبية العظمى من حالات <bdi>pericarditis</bdi> الفيروسي أو مجهول الـ<bdi>cause</bdi>.",
        "المضاد الحيوي غير مناسب بدون دليل عدوى جرثومية واضحة، والستيرويدات تحجز للحالات المقاومة، ومضاد التخثر قد يزيد <bdi>risk</bdi> نزيف تاموري.",
    ],
    "when_changes": [
        "لو ارتفعت أنزيمات القلب مع نفس الـ<bdi>symptoms</bdi>، يصير الـ<bdi>diagnosis</bdi> التهاب عضلة قلب مصاحب (myopericarditis) ويحتاج مراقبة أدق.",
        "لو تكرر الالتهاب بعد الـ<bdi>treatment</bdi> الأولي، يضاف <bdi>colchicine</bdi> لتقليل <bdi>risk</bdi> التكرار.",
    ],
    "rule": "<bdi>pericarditis</bdi> الـ<bdi>acute</bdi> بأنزيمات قلب <bdi>normal</bdi> يعالج بمضادات الالتهاب غير الستيرويدية كخط أول.",
    "comparison": None,
    "guideline_note": None,
},
470: {
    "idea": "<bdi>patient</bdi> قصور قلب <bdi>chronic</bdi> على عدة أدوية، والسؤال يبي أي دواء من مجموعة أدويته يثبت أنه يقلل معدل الوفيات على المدى الطويل.",
    "clues": [
        ("congestive heart failure on multiple treatments", "<bdi>treatment</bdi> متعدد يحتاج تمييز أي جزء منه يقلل الوفيات فعليًا"),
        ("reduced mortality rate in congestive heart failure", "يبي دواء يقلل الوفيات تحديدًا"),
    ],
    "why_correct": [
        "مثبطات <bdi>ACE</bdi> من الأدوية الأساسية المثبتة بدراسات كبرى (SOLVD وغيرها) بتقليل الوفيات ب<bdi>heart failure</bdi> الـ<bdi>chronic</bdi>.",
        "الـ<bdi>digoxin</bdi> يحسّن الـ<bdi>symptoms</bdi> ويقلل دخول المستشفى، والمدرات تخفف الـ<bdi>congestion</bdi>، ومضادات التخثر تمنع الجلطات، لكن ولا واحد منهم يثبت له تقليل مباشر للوفيات مثل مثبطات ACE.",
        "أهمية التزام الـ<bdi>patient</bdi> بمثبط ACE بالذات تكمن بأثره على تقليل تدهور <bdi>heart failure</bdi> وتحسين البقاء طويل المدى.",
    ],
    "when_changes": [
        "لو أضيف حاصر بيتا أو اسبيرونولاكتون لعلاجه لاحقًا، يصيران أيضًا من الأدوية اللي تثبت تقليل الوفيات، مو بديل عن مثبط ACE بل إضافة له.",
        "لو كان الـ<bdi>patient</bdi> عنده <bdi>atrial fibrillation</bdi> مصاحب، مضادات التخثر تمنع الجلطات الدماغية لكن هذا هدف مختلف عن تقليل وفيات <bdi>heart failure</bdi> نفسه.",
    ],
    "rule": "مثبطات <bdi>ACE</bdi> من الأدوية الأساسية المثبتة بتقليل الوفيات ب<bdi>heart failure</bdi> الـ<bdi>chronic</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
471: {
    "idea": "شاب سليم عنده <bdi>murmur</bdi> انقباضية عند القمة تزيد بقبضة اليد المستمرة وتقل بمناورة فالسالفا، وهذا نمط كلاسيكي يميز <bdi>mitral regurgitation</bdi> عن الاعتلال الضخامي الانسدادي.",
    "clues": [
        ("systolic murmur that heard at the apex", "موقع الـ<bdi>murmur</bdi> عند القمة، متوافق مع الصمام التاجي"),
        ("augmented with sustained handgrip and reduced with Valsalva manoeuvre", "نمط استجابة الـ<bdi>murmur</bdi> للمناورات يحدد نوع الآفة الصمامية"),
    ],
    "why_correct": [
        "قبضة اليد المستمرة ترفع مقاومة الشرايين الطرفية وتزيد ارتجاع الدم للخلف بالصمام التاجي، فتقوي <bdi>murmur</bdi> <bdi>mitral regurgitation</bdi>.",
        "مناورة فالسالفا تقلل الحجم داخل القلب وتقلل شدة <bdi>murmur</bdi> قصور التاجي، بعكس <bdi>murmur</bdi> الاعتلال الضخامي الانسدادي اللي تزيد بفالسالفا.",
        "هالنمط المعاكس بالضبط (يزيد بفالسالفا ويقل بقبضة اليد) هو المميز ل<bdi>cardiomyopathy</bdi> الضخامي الانسدادي، وهذا عكس ما وصف بالسؤال.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>murmur</bdi> تزيد بالوقوف المفاجئ وتقل بالقرفصاء، يصير الـ<bdi>diagnosis</bdi> أقرب ل<bdi>cardiomyopathy</bdi> الضخامي الانسدادي بدل قصور التاجي.",
        "لو كانت الـ<bdi>murmur</bdi> انبساطية بدل انقباضية بنفس الموقع، يستبعد قصور التاجي ويوجه ل<bdi>mitral stenosis</bdi> بدلًا منه.",
    ],
    "rule": "<bdi>murmur</bdi> تزيد بقبضة اليد المستمرة وتقل بفالسالفا تشخص <bdi>mitral regurgitation</bdi>، والنمط المعاكس يشخص الاعتلال الضخامي الانسدادي.",
    "comparison": {
        "headers": ["المناورة", "قصور التاجي (MR)", "الاعتلال الضخامي الانسدادي (HOCM)"],
        "rows": [
            ["قبضة اليد المستمرة", "تزيد الـ<bdi>murmur</bdi>", "تقل الـ<bdi>murmur</bdi>"],
            ["فالسالفا", "تقل الـ<bdi>murmur</bdi>", "تزيد الـ<bdi>murmur</bdi>"],
        ],
    },
    "guideline_note": None,
},
472: {
    "idea": "رجل مدخن وضغطه <bdi>elevated</bdi> عنده ألم صدري خلفي <bdi>acute</bdi> مفاجئ وفقدان وعي وهبوط ضغط، وهذي صورة كلاسيكية لتسلخ الأبهر (تمزق البطانة الداخلية).",
    "clues": [
        ("sudden severe retrosternal chest pain that radiates to his back", "ألم مفاجئ <bdi>severe</bdi> ينتشر للظهر، <bdi>sign</bdi> كلاسيكية لتسلخ الأبهر"),
        ("heavy smoker and has history of hypertension", "<bdi>factors</bdi> <bdi>risk</bdi> رئيسية لتسلخ الأبهر"),
        ("Blood pressure 85/56", "هبوط ضغط <bdi>severe</bdi> يوحي ب<bdi>complication</bdi> خطيرة (نزيف داخلي أو <bdi>tamponade</bdi> قلبي)"),
    ],
    "why_correct": [
        "الألم الصدري الـ<bdi>acute</bdi> الذي ينتشر للظهر مع فقدان وعي مفاجئ وهبوط ضغط <bdi>severe</bdi> ب<bdi>patient</bdi> مدخن وضاغط يشخص <bdi>tear in the aortic intima</bdi> (تسلخ الأبهر).",
        "هبوط الضغط الـ<bdi>severe</bdi> قد يكون <bdi>result</bdi> نزيف داخلي أو <bdi>tamponade</bdi> قلبي ثانوي للتسلخ، وهو <bdi>complication</bdi> مهددة للحياة تحتاج تدخل عاجل.",
        "انتشار الألم للظهر تحديدًا يميز هالحالة عن الاحتشاء القلبي المعتاد اللي ينتشر عادة للذراع أو الفك.",
    ],
    "when_changes": [
        "لو انتشر الألم للذراع الأيسر بدل الظهر مع تغيرات تخطيطية إقفارية واضحة، يصير احتشاء القلب الـ<bdi>acute</bdi> الـ<bdi>diagnosis</bdi> الأقرب.",
        "لو كان الفقدان المفاجئ للوعي بدون ألم صدري أصلًا وبضغط <bdi>normal</bdi>، يصير نوبة وعائية مبهمية (vasovagal) احتمال أقوى.",
    ],
    "rule": "ألم صدري <bdi>acute</bdi> ينتشر للظهر مع هبوط ضغط مفاجئ ب<bdi>patient</bdi> مدخن وضاغط يوجه فورًا للتفكير بتسلخ الأبهر.",
    "comparison": None,
    "guideline_note": None,
},
473: {
    "idea": "شاب رياضي عنده نوبات إغماء وألم صدري متكرر بالمجهود مع <bdi>murmur</bdi> انقباضية قوية ونبض كاروتيدي متقطع الشدة، وهذي صورة كلاسيكية ل<bdi>cardiomyopathy</bdi> الضخامي الانسدادي.",
    "clues": [
        ("chest pain, breathlessness and felt as he was going to faint", "<bdi>symptoms</bdi> كلاسيكية ل<bdi>cardiomyopathy</bdi> الضخامي الانسدادي أثناء المجهود"),
        ("harsh ejection systolic murmur with a palpable systolic thrill at the left steal edge", "<bdi>murmur</bdi> انقباضية قوية مع <bdi>tremor</bdi>، متوافقة مع انسداد مجرى خروج البطين"),
        ("jerky carotid pulse", "نبض كاروتيدي متقطع مميز ل<bdi>cardiomyopathy</bdi> الضخامي الانسدادي"),
    ],
    "why_correct": [
        "النبض الكاروتيدي المتقطع (jerky) مع الـ<bdi>murmur</bdi> الانقباضية القوية والـ<bdi>tremor</bdi> الجدارية يطابق تمامًا صورة <bdi>hypertrophic obstructive cardiomyopathy</bdi>.",
        "نوبات الإغماء أثناء الرياضة عند الشباب من أخطر <bdi>signs</bdi> هالمرض لأنها قد تنذر ب<bdi>risk</bdi> الموت القلبي المفاجئ أثناء المجهود.",
        "الـ<bdi>symptoms</bdi> المتكررة أثناء المجهود الرياضي تحديدًا (مو بالراحة) تدعم كون الـ<bdi>cause</bdi> انسدادي ديناميكي يزداد سوء بزيادة قوة انقباض القلب أثناء التمرين.",
    ],
    "when_changes": [
        "لو كانت النوبات مصحوبة ب<bdi>palpitations</bdi> سريع منتظم مع تخطيط يظهر موجة دلتا وPR قصير، يصير التفكير بمتلازمة WPW بدل الاعتلال الضخامي.",
        "لو كان تخطيط القلب يظهر تطاول واضح بفترة QT، يصير الـ<bdi>diagnosis</bdi> متلازمة QT الطويل بدل الاعتلال الضخامي.",
    ],
    "rule": "نبض كاروتيدي متقطع مع <bdi>murmur</bdi> انقباضية و<bdi>tremor</bdi> عند شاب رياضي يعاني إغماء مجهودي يشخص <bdi>hypertrophic obstructive cardiomyopathy</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
474: {
    "idea": "<bdi>patient</bdi> قصور قلب انقباضي مستقر تمامًا على <bdi>treatment</bdi> أساسي (مثبط ACE ومدر بولي) بدون <bdi>symptoms</bdi> <bdi>congestion</bdi>، والسؤال يبي الـ<bdi>step</bdi> التالية المنطقية لتحسين بقاءه طويل المدى.",
    "clues": [
        ("enalopril 10 mg OD, simvastatin 40 mg OD, furosemide 40 mg OD", "<bdi>treatment</bdi> أساسي حالي ل<bdi>heart failure</bdi>"),
        ("chest is clear and heart sounds are normal. There is no peripheral edema", "الـ<bdi>patient</bdi> مستقر تمامًا بدون <bdi>congestion</bdi> حالي"),
    ],
    "why_correct": [
        "بعد استقرار الـ<bdi>patient</bdi> على مثبط ACE ومدر بولي، الـ<bdi>step</bdi> التالية القياسية هي إضافة حاصر بيتا زي <bdi>bisoprolol</bdi> لتحسين البقاء طويل المدى.",
        "حاصرات البيتا تضاف تدريجيًا بجرعة <bdi>low</bdi> فقط بعد التأكد من استقرار الـ<bdi>patient</bdi> (بدون <bdi>congestion</bdi> <bdi>acute</bdi>)، وهذا متحقق تمامًا هنا.",
        "الـ<bdi>digoxin</bdi> ولوسارتان خيارات لاحقة أو بديلة تستخدم بحالات معينة، لكن حاصر البيتا هو الـ<bdi>step</bdi> القياسية الأولى بعد مثبط ACE والمدر البولي.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> غير مستقر ب<bdi>symptoms</bdi> <bdi>congestion</bdi> <bdi>acute</bdi>، لازم تأجيل بدء حاصر البيتا لحين الاستقرار أولًا.",
        "لو ما تحمّل مثبط ACE أصلًا (سعال مزعج)، يستبدل بلوسارتان قبل التفكير بإضافة حاصر بيتا.",
    ],
    "rule": "بعد استقرار <bdi>patient</bdi> <bdi>heart failure</bdi> الانقباضي على مثبط ACE ومدر بولي، تضاف حاصرات البيتا تدريجيًا لتحسين البقاء طويل المدى.",
    "comparison": None,
    "guideline_note": None,
},
475: {
    "idea": "<bdi>patient</bdi> قصور قلب انقباضي مستقر على <bdi>aspirin</bdi> و<bdi>statin</bdi> ومدر بولي فقط بدون مثبط ACE أصلًا، والسؤال يبي الدواء الأساسي الناقص اللي لازم يبدأ فيه.",
    "clues": [
        ("aspirin 75 mg OD, simvastatin 40 mg OD and furosemide 40 mg OD", "<bdi>treatment</bdi> ناقص أساس <bdi>heart failure</bdi> (لا يوجد مثبط ACE)"),
        ("heart sounds are normal, his chest is clear and there is no peripheral edema", "الـ<bdi>patient</bdi> مستقر ومناسب لبدء <bdi>treatment</bdi> أساسي جديد"),
    ],
    "why_correct": [
        "<bdi>Enalapril</bdi> من مثبطات ACE، وهو الدواء الأساسي الناقص من <bdi>treatment</bdi> الـ<bdi>patient</bdi> حاليًا واللي يثبت تقليل الوفيات ب<bdi>heart failure</bdi> الانقباضي الـ<bdi>chronic</bdi>.",
        "بدء مثبط ACE أهم أولوية بهالمرحلة لأنه حجر الأساس ب<bdi>treatment</bdi> <bdi>heart failure</bdi> طويل المدى، قبل التفكير بأي إضافات ثانية.",
        "الـ<bdi>digoxin</bdi> والهيدرالازين واسبيرونولاكتون أدوية إضافية تستخدم لاحقًا أو بحالات معينة، لكنها لا تحل محل مثبط ACE ك<bdi>step</bdi> أولى أساسية.",
    ],
    "when_changes": [
        "لو ما تحمّل الـ<bdi>patient</bdi> مثبطات ACE (سعال أو وذمة وعائية)، يستبدل بحاصر مستقبلات الأنجيوتنسين.",
        "لو استمرت الـ<bdi>symptoms</bdi> رغم مثبط ACE وحاصر بيتا بجرعات كافية، تضاف اسبيرونولاكتون ك<bdi>step</bdi> تالية.",
    ],
    "rule": "أي <bdi>patient</bdi> قصور قلب انقباضي بدون مثبط ACE بعلاجه، أولوية إضافته فورًا لأنه حجر الأساس بالـ<bdi>treatment</bdi> طويل المدى.",
    "comparison": None,
    "guideline_note": None,
},
476: {
    "idea": "<bdi>patient</bdi> <bdi>angina</bdi> بعد احتشاء سابق، والسؤال يبي <bdi>factor</bdi> <bdi>risk</bdi> يمكن تعديله فعليًا للحد من تفاقم <bdi>disease</bdi> القلب الإقفاري.",
    "clues": [
        ("previous history of myocardial infarction", "<bdi>disease</bdi> قلب إقفاري مؤكد يحتاج تعديل <bdi>factors</bdi> الـ<bdi>risk</bdi>"),
        ("modifiable risk factors", "يبي <bdi>factor</bdi> يمكن تغييره فعليًا مو <bdi>factor</bdi> ثابت"),
    ],
    "why_correct": [
        "<bdi>Smoking</bdi> من أهم <bdi>factors</bdi> الـ<bdi>risk</bdi> القابلة للتعديل الكامل ب<bdi>disease</bdi> القلب الإقفاري، والإقلاع عنه يقلل <bdi>risk</bdi> الأحداث القلبية المستقبلية بشكل كبير وموثق.",
        "التدخين يسرّع <bdi>atherosclerosis</bdi> ويزيد تخثر الدم ويقلل الأكسجين الواصل للقلب، فالإقلاع عنه يعالج عدة آليات مسببة لل<bdi>disease</bdi> مرة واحدة.",
        "التاريخ العائلي والجنس والعمر <bdi>factors</bdi> <bdi>risk</bdi> ثابتة لا يمكن تغييرها، بعكس التدخين اللي يعتبر <bdi>factor</bdi> سلوكي قابل للتعديل الكامل.",
    ],
    "when_changes": [
        "لو كان السؤال يبي <bdi>factor</bdi> <bdi>risk</bdi> غير قابل للتعديل، يصير التاريخ العائلي أو الجنس هو الجواب الصحيح بدل التدخين.",
        "لو كان الـ<bdi>patient</bdi> غير مدخن أصلًا، يصير التركيز على <bdi>factors</bdi> قابلة للتعديل ثانية زي الضغط و<bdi>diabetes</bdi> والكوليسترول.",
    ],
    "rule": "<bdi>Smoking</bdi> من أهم <bdi>factors</bdi> الـ<bdi>risk</bdi> القابلة للتعديل الكامل ب<bdi>disease</bdi> القلب الإقفاري، ويجب التركيز على الإقلاع عنه دايمًا.",
    "comparison": None,
    "guideline_note": None,
},
477: {
    "idea": "<bdi>patient</bdi> مسنة عندها إغماء مجهودي مع نبض كاروتيدي بطيء الارتفاع و<bdi>murmur</bdi> انقباضية قاسية تنتشر للرقبة، وهذي صورة كلاسيكية ل<bdi>aortic stenosis</bdi>.",
    "clues": [
        ("exertional syncope", "<bdi>symptom</bdi> كلاسيكي ل<bdi>aortic stenosis</bdi> <bdi>severe</bdi>"),
        ("slow rising carotid pulse", "<bdi>sign</bdi> كلاسيكية (pulsus parvus et tardus) ل<bdi>aortic stenosis</bdi>"),
        ("loud ejection systolic murmur at the upper right sternal edge, radiating to the carotids", "<bdi>murmur</bdi> كلاسيكية ل<bdi>aortic stenosis</bdi> بموقعها وانتشارها"),
    ],
    "why_correct": [
        "النبض الكاروتيدي البطيء الارتفاع (pulsus parvus et tardus) مع الـ<bdi>murmur</bdi> الانقباضية القاسية المنتشرة للرقبة يشخصان <bdi>aortic stenosis</bdi> بشكل كلاسيكي.",
        "الإغماء المجهودي <bdi>symptom</bdi> خطير يدل على شدة التضيق وعدم قدرة القلب على زيادة النتاج القلبي بشكل كافي أثناء المجهود.",
        "باقي الـ<bdi>diseases</bdi> المذكورة (<bdi>mitral stenosis</bdi>، <bdi>mitral valve prolapse</bdi>، قصور ثلاثي الشرف) لها <bdi>murmurs</bdi> مختلفة الموقع والانتشار ولا تتوافق مع هالوصف.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>murmur</bdi> انبساطية عند القمة بدل انقباضية عند الحافة اليمنى، يصير الـ<bdi>diagnosis</bdi> <bdi>mitral stenosis</bdi> بدل <bdi>aortic stenosis</bdi>.",
        "لو كانت الـ<bdi>murmur</bdi> تزيد بالوقوف وتقل بالقرفصاء، يصير التفكير ب<bdi>cardiomyopathy</bdi> الضخامي الانسدادي بدل <bdi>aortic stenosis</bdi> الحقيقي.",
    ],
    "rule": "نبض بطيء الارتفاع مع <bdi>murmur</bdi> انقباضية قاسية تنتشر للرقبة يشخصان <bdi>aortic stenosis</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
478: {
    "idea": "رجل سليم ظاهريًا قلقان من <bdi>disease</bdi> القلب، والسؤال يبي أقوى <bdi>factor</bdi> <bdi>risk</bdi> من بين القيم المذكورة لتطور <bdi>disease</bdi> القلب الإقفاري.",
    "clues": [
        ("2 separate fasting plasma glucose of 8.2 and 8.3 mmol/L", "قيمتان مرتفعتان تؤكدان <bdi>diagnosis</bdi> <bdi>diabetes</bdi>"),
    ],
    "why_correct": [
        "قياسان منفصلان لسكر صائم فوق 7 مليمول/لتر يشخصان <bdi>diabetes mellitus</bdi> فعليًا، وهو من أقوى <bdi>factors</bdi> الـ<bdi>risk</bdi> المستقلة ل<bdi>disease</bdi> القلب الإقفاري.",
        "<bdi>diabetes</bdi> يسرّع <bdi>atherosclerosis</bdi> بعدة آليات (التهاب وأكسدة وخلل بالدهون) ويرفع <bdi>risk</bdi> الاحتشاء بشكل أكبر من زيادة الوزن أو ارتفاع الضغط الـ<bdi>mild</bdi> وحدهم.",
        "قيم BMI ومحيط الخصر والضغط المذكورة بالسؤال <bdi>elevated</bdi> بشكل بسيط فقط ولا ترقى ل<bdi>diagnosis</bdi> مرضي مؤكد بعكس قيم السكر الصريحة.",
    ],
    "when_changes": [
        "لو كانت قيمة الضغط أعلى بكثير (زي 170/100) وتشخص ضغط <bdi>chronic</bdi> حقيقي، يصير <bdi>factor</bdi> <bdi>risk</bdi> مهم أيضًا لكن يبقى <bdi>diabetes</bdi> المشخص أقوى بالمقارنة هنا.",
        "لو كانت قراءة السكر مرة واحدة فقط وغير مؤكدة بقياس ثاني، يقل يقين <bdi>diagnosis</bdi> <bdi>diabetes</bdi> ك<bdi>factor</bdi> <bdi>risk</bdi> مؤكد.",
    ],
    "rule": "<bdi>diabetes</bdi> المشخص من أقوى <bdi>factors</bdi> الـ<bdi>risk</bdi> المستقلة ل<bdi>disease</bdi> القلب الإقفاري، ويتفوق على درجات <bdi>mild</bdi> من السمنة أو ارتفاع الضغط.",
    "comparison": None,
    "guideline_note": None,
},
479: {
    "idea": "<bdi>patient</bdi> عنده نوبة إقفار دماغي عابر (تحسن كامل خلال دقائق) مع <bdi>atrial fibrillation</bdi> مكتشف حديثًا، والسؤال يبي أفضل <bdi>treatment</bdi> وقائي طويل المدى من تكرار الـ<bdi>thrombus</bdi> الدماغية.",
    "clues": [
        ("right-sided weakness that lasted 10 minutes and fully resolved", "نوبة إقفار عابر (TIA) تستدعي وقاية ثانوية فورية"),
        ("he is in atrial fibrillation", "<bdi>cause</bdi> واضح ل<bdi>risk</bdi> الـ<bdi>thrombus</bdi> الدماغية يحتاج مضاد تخثر"),
    ],
    "why_correct": [
        "ب<bdi>patient</bdi> <bdi>atrial fibrillation</bdi> تعرض لنوبة إقفار دماغي عابر، مضاد التخثر الفموي (<bdi>warfarin</bdi>) بمعدل INR بين 2 و3 هو الـ<bdi>treatment</bdi> الوقائي القياسي طويل المدى.",
        "هالمدى العلاجي (2-3) يعطي حماية جيدة من الجلطات الدماغية بدون زيادة <bdi>risk</bdi> النزيف بشكل مبالغ فيه.",
        "الـ<bdi>aspirin</bdi> وحده أقل فعالية بكثير من مضاد التخثر الفموي بمنع الـ<bdi>thrombus</bdi> الدماغية المرتبطة ب<bdi>atrial fibrillation</bdi> تحديدًا.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> عنده صمام ميكانيكي بدل <bdi>atrial fibrillation</bdi> بسيط، يصير المدى المستهدف أعلى (INR 3-4) ب<bdi>cause</bdi> زيادة <bdi>risk</bdi> التجلط على الصمام الصناعي.",
        "لو كان الـ<bdi>patient</bdi> غير مناسب لمضادات التخثر الفموية ل<bdi>cause</bdi> طبي، يصير الـ<bdi>aspirin</bdi> بديل أضعف يستخدم عند الضرورة فقط.",
    ],
    "rule": "ب<bdi>patient</bdi> <bdi>atrial fibrillation</bdi> تعرض لنوبة إقفار دماغي عابر، مضاد التخثر الفموي بمدى INR بين 2 و3 هو الوقاية القياسية طويلة المدى.",
    "comparison": None,
    "guideline_note": None,
},
480: {
    "idea": "<bdi>patient</bdi> احتشاء سفلي ب<bdi>treatment</bdi> قياسي مع <bdi>crepitations</bdi> رئوية <bdi>bilateral</bdi> تدل على بداية <bdi>congestion</bdi> <bdi>mild</bdi>، والسؤال يبي دواء إضافي مناسب يحسّن البقاء ويتحمل حالته الحالية.",
    "clues": [
        ("acute inferior myocardial infarction", "احتشاء قلبي حديث يحتاج <bdi>treatment</bdi> وقائي ثانوي شامل"),
        ("bilateral basal crackles on auscultation of the chest", "<bdi>sign</bdi> <bdi>congestion</bdi> رئوي <bdi>mild</bdi> يحتاج مراعاة عند اختيار الدواء"),
    ],
    "why_correct": [
        "<bdi>Bisoprolol</bdi> حاصر بيتا من الأدوية الأساسية اللي تضاف بعد الاحتشاء القلبي لتحسين البقاء وتقليل <bdi>risk</bdi> تكرار الأحداث القلبية.",
        "رغم وجود <bdi>crepitations</bdi> <bdi>mild</bdi>، حاصر بيتا يبدأ بحذر وبجرعة <bdi>low</bdi> تدريجيًا لأن فوائده على المدى الطويل بعد الاحتشاء تفوق الـ<bdi>risk</bdi> لو أعطي بحذر مناسب.",
        "<bdi>amlodipine</bdi> ولوسارتان ما يعتبران الـ<bdi>step</bdi> القياسية الإضافية الأولى بعد الاحتشاء مقارنة بحاصر بيتا، والـ<bdi>warfarin</bdi> غير مناسب بدون <bdi>cause</bdi> واضح مثل <bdi>atrial fibrillation</bdi> أو <bdi>thrombus</bdi> بالبطين.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>congestion</bdi> الرئوي <bdi>severe</bdi> وواضح (وذمة رئوية <bdi>acute</bdi>)، لازم تأجيل بدء حاصر البيتا لحين استقرار <bdi>case</bdi> القلب أولًا.",
        "لو ما تحمّل الـ<bdi>patient</bdi> حاصر البيتا (<bdi>asthma</bdi> <bdi>severe</bdi> مثلًا)، يصير التفكير بحاصر قنوات كالسيوم غير <bdi>bilateral</bdi> الهيدروبيريدين كبديل جزئي.",
    ],
    "rule": "بعد الاحتشاء القلبي، حاصر البيتا من الأدوية الأساسية المضافة لتحسين البقاء طويل المدى، ويبدأ بحذر حتى مع <bdi>congestion</bdi> <bdi>mild</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
481: {
    "idea": "<bdi>patient</bdi> <bdi>palpitations</bdi> وفقدان وزن مع نبض غير منتظم ورعاش <bdi>mild</bdi>، والسؤال يبي الفحص التالي الأنسب لكشف الـ<bdi>cause</bdi> الهرموني المحتمل وراء <bdi>atrial fibrillation</bdi>.",
    "clues": [
        ("weight loss over the last 2 months", "<bdi>symptom</bdi> جهازي يوجه لاحتمال <bdi>hyperthyroidism</bdi>"),
        ("irregularly irregular pulse and a fine tremor", "<bdi>signs</bdi> مصاحبة كلاسيكية ل<bdi>hyperthyroidism</bdi> مع <bdi>atrial fibrillation</bdi>"),
    ],
    "why_correct": [
        "فقدان الوزن مع الرعاش الـ<bdi>mild</bdi> و<bdi>atrial fibrillation</bdi> يوجهون بقوة لاحتمال <bdi>hyperthyroidism</bdi> ك<bdi>cause</bdi> أساسي، فيصير <bdi>thyroid function tests</bdi> الفحص التالي الأهم.",
        "<bdi>hyperthyroidism</bdi> <bdi>cause</bdi> شائع وقابل لل<bdi>treatment</bdi> للرجفان الأذيني، وتشخيصه يغير خطة الـ<bdi>treatment</bdi> بشكل كامل (<bdi>treatment</bdi> الـ<bdi>cause</bdi> الأساسي مو بس التحكم بالنظم).",
        "باقي الفحوصات (سونار سباتي، اختبار مجهود، مراقبة هولتر) لا تكشف الـ<bdi>cause</bdi> الهرموني المحتمل وراء الـ<bdi>symptoms</bdi> المذكورة.",
    ],
    "when_changes": [
        "لو ما فيه فقدان وزن أو رعاش مصاحب للرجفان الأذيني، يقل احتمال <bdi>hyperthyroidism</bdi> ك<bdi>cause</bdi> ويصير الـ<bdi>assessment</bdi> القلبي المباشر أولوية أكبر.",
        "لو تأكد <bdi>hyperthyroidism</bdi>، يصير <bdi>treatment</bdi> الـ<bdi>cause</bdi> الهرموني نفسه جزء أساسي من خطة <bdi>treatment</bdi> <bdi>atrial fibrillation</bdi>.",
    ],
    "rule": "<bdi>atrial fibrillation</bdi> مع فقدان وزن ورعاش يستدعي فحص وظائف الغدة الدرقية لاستبعاد فرط نشاطها ك<bdi>cause</bdi> علاجي قابل للتصحيح.",
    "comparison": None,
    "guideline_note": None,
},
482: {
    "idea": "<bdi>patient</bdi> ضغط <bdi>chronic</bdi> صار عنده تدهور تدريجي بالقدرة على المشي مع <bdi>congestion</bdi> رئوي <bdi>mild</bdi> ووذمة طرفية، وضغطه غير مضبوط جدًا رغم دواءين، فيحتاج تعديل علاجي يخدم الهدفين معًا.",
    "clues": [
        ("Blood pressure 188/96", "ضغط غير مضبوط بشدة رغم الـ<bdi>treatment</bdi> الحالي"),
        ("bilateral basal crackles and mild pitting ankle edema", "<bdi>signs</bdi> بداية <bdi>congestion</bdi> قلبي مصاحب"),
        ("Creatinine 133", "ارتفاع <bdi>mild</bdi> بالكرياتينين يحتاج مراعاة عند اختيار الدواء المضاف"),
    ],
    "why_correct": [
        "إضافة <bdi>lisinopril</bdi> (مثبط ACE) تخدم هدفين مهمين معًا: تحسين التحكم بالضغط الـ<bdi>severe</bdi> الارتفاع، وحماية القلب والكلى ب<bdi>case</bdi> بداية قصور قلب و<bdi>congestion</bdi>.",
        "مثبطات ACE مفيدة بشكل خاص بمرضى الضغط المصاحب لبداية <bdi>symptoms</bdi> قلبية (<bdi>crepitations</bdi> ووذمة)، لأنها تقلل الحمل على القلب وتبطئ تقدم أي خلل كلوي مصاحب.",
        "زيادة <bdi>amlodipine</bdi> أو إضافة اسبيرونولاكتون أو بيسوبرولول بمفردهم ما يعالجون الصورة الكاملة (ضغط <bdi>severe</bdi> الارتفاع مع بداية <bdi>congestion</bdi> قلبي) بنفس فعالية مثبط ACE هنا.",
    ],
    "when_changes": [
        "لو كان الكرياتينين <bdi>elevated</bdi> بشدة أو البوتاسيوم <bdi>elevated</bdi> أصلًا، لازم حذر أكبر أو تأجيل مثبط ACE لحين إعادة <bdi>assessment</bdi> وظائف الكلى.",
        "لو تحسن الضغط بشكل كافي بمثبط ACE بس استمر الـ<bdi>congestion</bdi>، يضاف مدر بولي مثل furosemide ك<bdi>step</bdi> تالية.",
    ],
    "rule": "ب<bdi>patient</bdi> ضغط <bdi>severe</bdi> الارتفاع مع بداية <bdi>symptoms</bdi> <bdi>congestion</bdi> قلبي، إضافة مثبط ACE تخدم التحكم بالضغط وحماية القلب معًا.",
    "comparison": None,
    "guideline_note": None,
},
483: {
    "idea": "<bdi>patient</bdi> عنده <bdi>murmur</bdi> انبساطية عند الحافة القصية اليسرى مع اندفاع قمي منزاح للخارج، وهذا نمط كلاسيكي يشخص <bdi>aortic regurgitation</bdi>.",
    "clues": [
        ("diastolic murmur best heard at the left steal edge", "موقع الـ<bdi>murmur</bdi> الكلاسيكي ل<bdi>aortic regurgitation</bdi>"),
        ("apex beat is displaced outwards", "<bdi>sign</bdi> توسع البطين الأيسر الـ<bdi>chronic</bdi> <bdi>result</bdi> الحمل الحجمي ب<bdi>aortic regurgitation</bdi>"),
    ],
    "why_correct": [
        "الـ<bdi>murmur</bdi> الانبساطية عند الحافة القصية اليسرى مع اندفاع قمي منزاح للخارج (<bdi>result</bdi> توسع البطين الأيسر) تشخصان <bdi>aortic regurgitation</bdi> بشكل كلاسيكي.",
        "<bdi>aortic regurgitation</bdi> يسبب حمل حجمي <bdi>chronic</bdi> على البطين الأيسر يؤدي لتوسعه و<bdi>shift</bdi> النبض القمي للخارج تدريجيًا مع الوقت.",
        "باقي الـ<bdi>diseases</bdi> المذكورة (تضيق برزخ الأبهر، <bdi>mitral regurgitation</bdi>، <bdi>aortic stenosis</bdi>) لها مواقع <bdi>murmur</bdi> أو توقيت مختلف (انقباضي بدل انبساطي هنا).",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>murmur</bdi> انقباضية بدل انبساطية بنفس الموقع تقريبًا، يصير التفكير ب<bdi>aortic stenosis</bdi> بدل قصوره.",
        "لو كانت الـ<bdi>murmur</bdi> انبساطية عند القمة بدل الحافة اليسرى، يصير الـ<bdi>diagnosis</bdi> <bdi>mitral stenosis</bdi> بدل <bdi>aortic regurgitation</bdi>.",
    ],
    "rule": "<bdi>murmur</bdi> انبساطية عند الحافة القصية اليسرى مع اتساع البطين الأيسر تشخصان <bdi>aortic regurgitation</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
484: {
    "idea": "<bdi>patient</bdi> <bdi>atrial fibrillation</bdi> مستمر بدون موانع لمضادات التخثر، والسؤال يبي الـ<bdi>treatment</bdi> المضاد للتخثر الأنسب كخط أول لمنع الـ<bdi>thrombus</bdi> الدماغية.",
    "clues": [
        ("persistent atrial fibrillation", "الـ<bdi>disease</bdi> الأساسي المطلوب علاجه وقائيًا"),
        ("no contraindications to any antithrombotic treatments", "لا يوجد مانع يمنع استخدام أفضل خيار علاجي"),
    ],
    "why_correct": [
        "<bdi>Warfarin</bdi> (أو مضاد تخثر فموي مشابه) هو الخط الأول المعتمد للوقاية من الـ<bdi>thrombus</bdi> الدماغية بمرضى <bdi>atrial fibrillation</bdi> ذوي <bdi>factors</bdi> الـ<bdi>risk</bdi> (ضغط و<bdi>diabetes</bdi> هنا).",
        "مضادات التخثر الفموية أثبتت فعالية أعلى بكثير من مضادات الصفائح (<bdi>aspirin</bdi> أو كلوبيدوجريل) بمنع الجلطات الدماغية المرتبطة ب<bdi>atrial fibrillation</bdi>.",
        "بوجود عاملي <bdi>risk</bdi> (ضغط و<bdi>diabetes</bdi>) بدون أي مانع لمضاد التخثر، يكون استخدام الـ<bdi>aspirin</bdi> وحده أو مضادات الصفائح غير كافٍ للحماية المطلوبة.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> عنده مانع حقيقي لمضاد التخثر الفموي (نزيف نشط مثلًا)، يصير الـ<bdi>aspirin</bdi> أو الكلوبيدوجريل بديل أضعف يستخدم بحذر.",
        "لو كانت نقاط <bdi>risk</bdi> الـ<bdi>thrombus</bdi> صفر تقريبًا (بدون أي <bdi>factor</bdi> <bdi>risk</bdi> إضافي)، ممكن عدم استخدام أي مضاد تخثر أصلًا يكون خيار مقبول.",
    ],
    "rule": "ب<bdi>patient</bdi> <bdi>atrial fibrillation</bdi> بدون موانع، مضاد التخثر الفموي (<bdi>warfarin</bdi>) هو الخط الأول للوقاية من الـ<bdi>thrombus</bdi> الدماغية.",
    "comparison": None,
    "guideline_note": None,
},
485: {
    "idea": "<bdi>patient</bdi> مسنة <bdi>atrial fibrillation</bdi> مستمر بدون <bdi>symptoms</bdi>، تاخذ أدوية لل<bdi>asthma</bdi> و<bdi>migraine</bdi>، والسؤال يبي أفضل <bdi>treatment</bdi> وقائي أول من الـ<bdi>thrombus</bdi> الدماغية.",
    "clues": [
        ("persistent atrial fibrillation", "الـ<bdi>disease</bdi> الأساسي المطلوب علاجه وقائيًا"),
        ("completely asymptomatic", "غياب الـ<bdi>symptoms</bdi> لا يقلل <bdi>risk</bdi> الـ<bdi>thrombus</bdi> الدماغية المرتبط ب<bdi>atrial fibrillation</bdi> نفسه"),
    ],
    "why_correct": [
        "<bdi>Oral anticoagulation</bdi> هو الخط الأول القياسي للوقاية من الـ<bdi>thrombus</bdi> الدماغية بمرضى <bdi>atrial fibrillation</bdi> المستمر خصوصًا بوجود <bdi>factors</bdi> <bdi>risk</bdi> (السن المتقدم هنا).",
        "عمر الـ<bdi>patient</bdi> (77 سنة) <bdi>factor</bdi> <bdi>risk</bdi> مستقل يزيد احتمال الـ<bdi>thrombus</bdi> الدماغية بشكل كبير بغض النظر عن وجود <bdi>symptoms</bdi> أو عدمه.",
        "الـ<bdi>aspirin</bdi> وحده أو مع دايبيريدامول أقل فعالية بكثير من مضاد التخثر الفموي بالوقاية من الـ<bdi>thrombus</bdi> الدماغية المرتبطة ب<bdi>atrial fibrillation</bdi>.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>patient</bdi> شابة تمامًا بدون أي <bdi>factor</bdi> <bdi>risk</bdi> إضافي (نقاط <bdi>risk</bdi> <bdi>low</bdi> جدًا)، ممكن عدم استخدام أي مضاد تخثر يكون كافي.",
        "لو كان فيه مانع حقيقي لمضاد التخثر الفموي (نزيف نشط)، يصير الـ<bdi>aspirin</bdi> بديل أضعف يستخدم بحذر فقط.",
    ],
    "rule": "ب<bdi>patient</bdi> <bdi>atrial fibrillation</bdi> مستمر مع <bdi>factor</bdi> <bdi>risk</bdi> مثل السن المتقدم، مضاد التخثر الفموي هو الخط الأول للوقاية من الـ<bdi>thrombus</bdi> الدماغية.",
    "comparison": None,
    "guideline_note": None,
},
486: {
    "idea": "<bdi>patient</bdi> مدخن عنده ألم ساق بالمجهود يزول بالراحة مع ضعف نبض ومؤشر ضغط كاحل-عضد <bdi>low</bdi> نسبيًا، وهذا يشخص <bdi>disease</bdi> الشرايين الطرفية بدرجته الحقيقية حسب القيمة المعطاة.",
    "clues": [
        ("pain in his left leg, which is exacerbated by exercise and relieved by rest", "<bdi>symptom</bdi> كلاسيكي للعرج المتقطع ب<bdi>disease</bdi> الشرايين الطرفية"),
        ("weak pulses in the left leg compared to the right", "<bdi>sign</bdi> فحص سريري تدعم نقص التروية الشريانية بالطرف المصاب"),
        ("ankle brachial pressure Index is 0.84", "قيمة تشخص <bdi>disease</bdi> شرايين طرفية <bdi>mild</bdi> إلى متوسط"),
    ],
    "why_correct": [
        "مؤشر الضغط كاحل-عضد 0.84 يقع ضمن نطاق <bdi>diagnosis</bdi> <bdi>peripheral arterial disease</bdi> (المعدل الـ<bdi>normal</bdi> بين 0.9 و1.3 تقريبًا)، بس بدون الوصول لدرجة الإقفار الحرج.",
        "العرج المتقطع (ألم بالمجهود يزول بالراحة) مع ضعف النبض يدعمان الـ<bdi>diagnosis</bdi> السريري، وقيمة المؤشر تؤكده بشكل موضوعي.",
        "الإقفار الحرج يحتاج مؤشر أقل بكثير (عادة أقل من 0.4) مصحوب بألم بالراحة أو تقرحات، وهذا غير موجود هنا.",
    ],
    "when_changes": [
        "لو كان المؤشر أقل من 0.4 مع ألم مستمر بالراحة أو تقرح بالقدم، يصير الـ<bdi>diagnosis</bdi> إقفار حرج يحتاج تدخل عاجل.",
        "لو كان المؤشر أعلى من 1.3 (أوعية غير قابلة للانضغاط)، يصير التفسير مختلف ويحتاج فحص إضافي زي دوبلر الشرايين.",
    ],
    "rule": "مؤشر الضغط كاحل-عضد بين 0.4 و0.9 تقريبًا مع عرج متقطع يشخص <bdi>peripheral arterial disease</bdi> بدون إقفار حرج.",
    "comparison": {
        "headers": ["قيمة المؤشر", "التفسير"],
        "rows": [
            ["أكبر من 0.9", "<bdi>normal</bdi> تقريبًا"],
            ["0.4 - 0.9", "<bdi>disease</bdi> شرايين طرفية"],
            ["أقل من 0.4", "إقفار حرج"],
        ],
    },
    "guideline_note": None,
},
487: {
    "idea": "<bdi>patient</bdi> احتشاء واسع بعد تدخل تاجي ناجح على <bdi>treatment</bdi> قياسي، وكوليسترول LDL عنده عند الحد الأعلى المسموح تقريبًا، والسؤال يبي الدواء الإضافي المناسب لتقليل <bdi>risk</bdi> الأحداث القلبية المستقبلية.",
    "clues": [
        ("extensive anterior ST elevation myocardial infarction", "احتشاء واسع يحتاج وقاية ثانوية شاملة"),
        ("Cholesterol (LDL) 3.36", "قيمة عند الحد الأعلى للمعدل المستهدف عمومًا، لكن بعد احتشاء يحتاج هدف أكثر صرامة"),
    ],
    "why_correct": [
        "<bdi>Atorvastatin</bdi> بجرعة عالية يوصى به لجميع مرضى الاحتشاء القلبي الـ<bdi>acute</bdi> كوقاية ثانوية، بغض النظر عن مستوى الكوليسترول الأساسي، لتقليل <bdi>risk</bdi> الأحداث المستقبلية.",
        "الستاتينات لها فوائد إضافية غير خفض الكوليسترول فقط (تثبيت اللويحة التصلبية وتقليل الالتهاب)، وهذا يبرر استخدامها الروتيني بعد كل احتشاء.",
        "الفينوفايبرات والنياسين ليسا الـ<bdi>treatment</bdi> القياسي الأول للوقاية الثانوية بعد الاحتشاء، ويحجزان لحالات معينة من اضطراب الدهون الـ<bdi>severe</bdi>.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> على <bdi>statin</bdi> بجرعة عالية أصلًا وما زال LDL <bdi>elevated</bdi> جدًا رغمها، يضاف دواء ثاني زي ezetimibe ك<bdi>step</bdi> تالية.",
        "لو كان الـ<bdi>patient</bdi> لا يتحمل الستاتينات إطلاقًا، يصير التفكير بأدوية بديلة أخرى بعد استشارة مختص دهون.",
    ],
    "rule": "بعد أي احتشاء قلبي <bdi>acute</bdi>، يبدأ <bdi>statin</bdi> بجرعة عالية زي <bdi>atorvastatin</bdi> كوقاية ثانوية بغض النظر عن مستوى الكوليسترول الأساسي.",
    "comparison": None,
    "guideline_note": None,
},
488: {
    "idea": "<bdi>patient</bdi> <bdi>diabetes</bdi> عنده ألم صدري مبهم بالمجهود لمدة شهرين مع تخطيط قلب <bdi>normal</bdi> بالراحة، والسؤال يبي أفضل <bdi>step</bdi> تشخيصية تالية ل<bdi>assessment</bdi> احتمال الإقفار القلبي.",
    "clues": [
        ("vague chest pain with exertion for 2 months", "نمط ألم <bdi>chronic</bdi> بالمجهود يوجه لاحتمال <bdi>angina</bdi>"),
        ("Electrocardiogram: Normal", "لا يوجد دليل إقفار بالراحة، يحتاج اختبار بالمجهود لإظهاره"),
    ],
    "why_correct": [
        "<bdi>Exercise ECG testing</bdi> هو الـ<bdi>step</bdi> الأولى المناسبة ل<bdi>assessment</bdi> ألم صدري مجهودي <bdi>chronic</bdi> ب<bdi>patient</bdi> تخطيطه <bdi>normal</bdi> بالراحة، لكشف تغيرات إقفارية أثناء المجهود.",
        "هالفحص غير جراحي وأقل تكلفة من القسطرة أو التصوير النووي، ومناسب ك<bdi>step</bdi> أولى قبل التفكير ب<bdi>procedures</bdi> أكثر تعقيدًا.",
        "القسطرة والتصوير النووي بالأدينوسين <bdi>procedures</bdi> أكثر تدخلًا تحجز عادة لو كان اختبار المجهود إيجابي أو الـ<bdi>patient</bdi> غير قادر على أداء المجهود.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> غير قادر على المشي بالمجهود (اعتلال عصبي <bdi>diabetes</bdi> <bdi>severe</bdi> مثلًا)، يصير فحص الإجهاد الدوائي بديل مناسب.",
        "لو كان اختبار المجهود إيجابي بوضوح، الـ<bdi>step</bdi> التالية المنطقية تصير تصوير الشرايين التاجية بالقسطرة.",
    ],
    "rule": "بألم صدري مجهودي <bdi>chronic</bdi> مع تخطيط <bdi>normal</bdi> بالراحة، اختبار المجهود بتخطيط القلب هو الـ<bdi>step</bdi> التشخيصية الأولى.",
    "comparison": None,
    "guideline_note": None,
},
489: {
    "idea": "<bdi>patient</bdi> ضغط <bdi>chronic</bdi> غير مضبوط عنده ضيق نفس مجهودي وS4 مع تضخم بطين أيسر متحدد المركز ووظيفة ضخ <bdi>normal</bdi>، وهذي صورة كلاسيكية لخلل الوظيفة الانبساطية ب<bdi>cause</bdi> الضغط الـ<bdi>chronic</bdi>.",
    "clues": [
        ("poorly controlled hypertension", "<bdi>cause</bdi> رئيسي لتضخم وتيبس البطين الأيسر مع الوقت"),
        ("loud A2 and left ventricular S4, no murmur", "<bdi>signs</bdi> كلاسيكية لتيبس البطين الأيسر بدون <bdi>disease</bdi> صمامي"),
        ("concentric left ventricular hypertrophy and normal left ventricular ejection fraction", "تضخم متحدد المركز مع وظيفة ضخ محفوظة، يشخص خلل انبساطي"),
    ],
    "why_correct": [
        "تضخم البطين الأيسر المتحدد المركز مع وظيفة ضخ <bdi>normal</bdi> (EF محفوظة) وS4 يشخصون <bdi>left ventricular diastolic dysfunction</bdi> الناتج عن الضغط الـ<bdi>chronic</bdi> غير المضبوط.",
        "صوت S4 يعكس تقلص الأذين بقوة ضد بطين متيبس وأقل مرونة، وهذا نموذجي لخلل الوظيفة الانبساطية.",
        "غياب الـ<bdi>murmur</bdi> القلبية يستبعد <bdi>disease</bdi> صمامي واضح ك<bdi>cause</bdi> لل<bdi>symptoms</bdi>، ويدعم كون المشكلة بالتيبس العضلي للبطين نفسه.",
    ],
    "when_changes": [
        "لو كانت وظيفة الضخ <bdi>low</bdi> بدل محفوظة، يصير الـ<bdi>diagnosis</bdi> قصور قلب انقباضي بدل خلل انبساطي.",
        "لو ظهرت <bdi>signs</bdi> ضغط وريدي <bdi>elevated</bdi> يزيد بالشهيق بدون تضخم بطيني، يصير التفكير ب<bdi>pericarditis</bdi> المضيق بدل خلل الوظيفة الانبساطية.",
    ],
    "rule": "تضخم بطين أيسر متحدد المركز مع S4 ووظيفة ضخ محفوظة ب<bdi>patient</bdi> ضغط <bdi>chronic</bdi> يشخص <bdi>left ventricular diastolic dysfunction</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
490: {
    "idea": "شاب سليم بدون <bdi>symptoms</bdi> طلع عنده تضخم قلب صدفة، والـ<bdi>echo</bdi> أظهر توسع بالبطين الأيسر مع انخفاض واضح بنسبة الضخ (40%)، وهذا يشخص اعتلال عضلة قلب توسعي مبكر بدون <bdi>symptoms</bdi> بعد، والـ<bdi>treatment</bdi> يبدأ فورًا رغم غياب الـ<bdi>symptoms</bdi>.",
    "clues": [
        ("denies chest pain, dyspnea, orthopnea or PND", "غياب الـ<bdi>symptoms</bdi> حاليًا رغم وجود خلل تشريحي بالقلب"),
        ("Dilated left ventricle with ejection fraction of 40%", "انخفاض واضح بوظيفة الضخ يستدعي <bdi>treatment</bdi> فوري بغض النظر عن الـ<bdi>symptoms</bdi>"),
    ],
    "why_correct": [
        "مثبط ACE زي <bdi>lisinopril</bdi> يبدأ فورًا حتى بغياب الـ<bdi>symptoms</bdi> لأن انخفاض نسبة الضخ (EF 40%) وحده كافٍ لبدء <bdi>treatment</bdi> يحسن البقاء ويبطئ تدهور القلب.",
        "بدء الـ<bdi>treatment</bdi> مبكرًا قبل ظهور الـ<bdi>symptoms</bdi> يقلل <bdi>risk</bdi> تطور الـ<bdi>disease</bdi> لقصور قلب عرضي كامل مستقبلًا.",
        "الـ<bdi>digoxin</bdi> والمدر البولي يستخدمون ل<bdi>treatment</bdi> <bdi>symptoms</bdi> <bdi>congestion</bdi> فعلية، وهي غير موجودة هنا، والاكتفاء ب<bdi>follow-up</bdi> الـ<bdi>echo</bdi> فقط بدون <bdi>treatment</bdi> يفوت فرصة علاجية مهمة.",
    ],
    "when_changes": [
        "لو كانت نسبة الضخ <bdi>normal</bdi> تمامًا بدون أي خلل تشريحي، يكتفى بالـ<bdi>follow-up</bdi> الدورية بدون <bdi>treatment</bdi> دوائي.",
        "لو ظهرت <bdi>symptoms</bdi> <bdi>congestion</bdi> لاحقًا أثناء الـ<bdi>follow-up</bdi>، يضاف مدر بولي وحاصر بيتا تدريجيًا فوق مثبط ACE.",
    ],
    "rule": "انخفاض نسبة الضخ حتى بدون <bdi>symptoms</bdi> يستدعي بدء مثبط ACE فورًا لتحسين البقاء وإبطاء تدهور القلب.",
    "comparison": None,
    "guideline_note": None,
},
491: {
    "idea": "<bdi>patient</bdi> <bdi>mitral regurgitation</bdi> روماتيزمي <bdi>severe</bdi> ب<bdi>symptoms</bdi> مستمرة رغم <bdi>treatment</bdi> دوائي كامل، والسؤال يبي الـ<bdi>step</bdi> النهائية المناسبة ل<bdi>treatment</bdi> المشكلة التشريحية الأساسية.",
    "clues": [
        ("severe rheumatic mitral regurgitation", "<bdi>mitral regurgitation</bdi> <bdi>severe</bdi> تشريحيًا، مصدر الـ<bdi>symptoms</bdi> الأساسي"),
        ("symptoms improved with furosemide, spironolactone, enalapril and carvedilol", "تحسن جزئي بالـ<bdi>treatment</bdi> الدوائي بس المشكلة التشريحية باقية"),
    ],
    "why_correct": [
        "بوجود <bdi>mitral regurgitation</bdi> <bdi>severe</bdi> مع <bdi>symptoms</bdi> مستمرة، الـ<bdi>treatment</bdi> النهائي هو <bdi>mitral valve replacement</bdi> لتصحيح المشكلة التشريحية نفسها، مو الاكتفاء بالـ<bdi>treatment</bdi> الدوائي.",
        "الـ<bdi>patient</bdi> عرضي (<bdi>symptoms</bdi> قصور قلب فعلية) وهذا وحده كافٍ لتبرير التدخل الجراحي بغض النظر عن قيمة نسبة الضخ الحالية.",
        "الـ<bdi>digoxin</bdi> ولوسارتان أو مجرد الـ<bdi>follow-up</bdi> لن يعالجوا المشكلة التشريحية الأساسية (تسرب الصمام التاجي الـ<bdi>severe</bdi>) اللي تحتاج تصحيح جراحي.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>patient</bdi> عديم الـ<bdi>symptoms</bdi> تمامًا مع <bdi>mitral regurgitation</bdi> <bdi>mild</bdi> إلى متوسط، تكتفي بالـ<bdi>follow-up</bdi> الدورية بدون جراحة.",
        "لو كانت نسبة الضخ <bdi>low</bdi> جدًا بشكل حرج مع <bdi>symptoms</bdi> متأخرة جدًا، يزيد <bdi>risk</bdi> الجراحة لكنها تبقى الخيار العلاجي الأساسي.",
    ],
    "rule": "<bdi>mitral regurgitation</bdi> <bdi>severe</bdi> مع <bdi>symptoms</bdi> مستمرة رغم الـ<bdi>treatment</bdi> الدوائي يستدعي تصحيح جراحي للصمام (إصلاح أو استبدال) بغض النظر عن نسبة الضخ.",
    "comparison": None,
    "guideline_note": None,
},
492: {
    "idea": "مسن طلع عنده <bdi>aortic stenosis</bdi> <bdi>severe</bdi> بالـ<bdi>echo</bdi> صدفة بدون أي <bdi>symptoms</bdi>، ووظيفة الضخ <bdi>normal</bdi>، والسؤال يبي أنسب تصرف بهالمرحلة المبكرة العرضية.",
    "clues": [
        ("denied symptoms of dyspnea, chest pain or syncope", "الـ<bdi>patient</bdi> عديم الـ<bdi>symptoms</bdi> تمامًا"),
        ("severely stenosed aortic valve", "درجة تضيق <bdi>severe</bdi> تشريحيًا رغم غياب الـ<bdi>symptoms</bdi>"),
        ("normal ejection fraction", "وظيفة القلب سليمة، تدعم تأجيل التدخل الجراحي حاليًا"),
    ],
    "why_correct": [
        "ب<bdi>patient</bdi> <bdi>aortic stenosis</bdi> <bdi>severe</bdi> لكن عديم الـ<bdi>symptoms</bdi> ووظيفة ضخ <bdi>normal</bdi>، الأنسب هو الـ<bdi>follow-up</bdi> الدورية القريبة (كل 6 أشهر تقريبًا) بدون تدخل جراحي فوري.",
        "الجراحة المبكرة بدون <bdi>symptoms</bdi> أو ضعف وظيفي ما تثبت لها فايدة واضحة تفوق مخاطرها مقارنة بالـ<bdi>follow-up</bdi> المنتظمة عند هالفئة من المرضى.",
        "استبدال الصمام يحجز لحالات ظهور الـ<bdi>symptoms</bdi> أو تدهور وظيفة البطين، وهذا غير موجود هنا حاليًا.",
    ],
    "when_changes": [
        "لو ظهرت <bdi>symptoms</bdi> جديدة (ذبحة، ضيق نفس، إغماء) أثناء الـ<bdi>follow-up</bdi>، يصير استبدال الصمام الجراحي هو الـ<bdi>step</bdi> التالية المناسبة فورًا.",
        "لو تدهورت وظيفة البطين الأيسر أثناء الـ<bdi>follow-up</bdi> رغم غياب الـ<bdi>symptoms</bdi>، يصير التدخل الجراحي مبررًا أيضًا حتى بدون <bdi>symptoms</bdi>.",
    ],
    "rule": "<bdi>aortic stenosis</bdi> الـ<bdi>severe</bdi> بدون <bdi>symptoms</bdi> ووظيفة بطين <bdi>normal</bdi> يتابع دوريًا بفترات قريبة بدون تدخل فوري.",
    "comparison": None,
    "guideline_note": None,
},
493: {
    "idea": "شابة عندها تاريخ حمى روماتيزمية منذ الطفولة، وصار عندها ضيق نفس مجهودي مع <bdi>signs</bdi> <bdi>congestion</bdi> (JVP <bdi>elevated</bdi> وS1 صاخب وP2 صاخب و<bdi>murmur</bdi> انبساطية متدحرجة عند القمة)، وهذي صورة كلاسيكية ل<bdi>mitral stenosis</bdi>.",
    "clues": [
        ("history of rheumatic heart disease since childhood", "<bdi>factor</bdi> <bdi>risk</bdi> رئيسي ل<bdi>mitral stenosis</bdi> المكتسب"),
        ("loud S1, loud P2 and mid diastolic rumbling murmur in the apex", "<bdi>signs</bdi> سمعية كلاسيكية ل<bdi>mitral stenosis</bdi> مع ارتفاع ضغط رئوي مصاحب"),
        ("JVP of 5 cm above sternal angle", "<bdi>sign</bdi> <bdi>congestion</bdi> جهازي مصاحب لتفاقم الـ<bdi>case</bdi>"),
    ],
    "why_correct": [
        "الـ<bdi>murmur</bdi> الانبساطية المتدحرجة عند القمة مع S1 صاخب وP2 صاخب (يعكس ارتفاع ضغط رئوي) تشخص <bdi>mitral stenosis</bdi> بشكل كلاسيكي.",
        "التاريخ المرضي للحمى الروماتيزمية منذ الطفولة يفسر التندب والتضيق التدريجي بالصمام التاجي على مدى سنوات طويلة.",
        "الـ<bdi>crepitations</bdi> القاعدية بالرئتين تعكس <bdi>congestion</bdi> رئوي ثانوي لارتفاع الضغط خلف الصمام التاجي المتضيق.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>murmur</bdi> انقباضية بدل انبساطية بنفس الموقع تقريبًا، يصير التفكير ب<bdi>aortic stenosis</bdi> أو <bdi>mitral regurgitation</bdi> بدل <bdi>mitral stenosis</bdi>.",
        "لو كانت الـ<bdi>murmur</bdi> تسمع أفضل عند الحافة القصية اليمنى مع <bdi>signs</bdi> <bdi>congestion</bdi> يميني معزول، يصير تضيق الصمام الثلاثي احتمال أقوى.",
    ],
    "rule": "<bdi>murmur</bdi> انبساطية متدحرجة عند القمة مع S1 وP2 صاخبين ب<bdi>patient</bdi> حمى روماتيزمية سابقة تشخص <bdi>mitral stenosis</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
494: {
    "idea": "<bdi>patient</bdi> عنده صورة قصور قلب يميني بارز (ارتفاع JVP لا يهبط بالشهيق، وذمة ضخمة، استسقاء بطني) مع <bdi>echo</bdi> يظهر توسع الأذينين فقط بدون مشكلة بالبطينين أو الصمامات، وهذا يوجه ل<bdi>disease</bdi> بالتامور أو تليف يقيّد امتلاء القلب، والفحص الأدق لتوضيح الـ<bdi>cause</bdi> هو تصوير مباشر لبنية القلب.",
    "clues": [
        ("JVP is markedly elevated and fails to descend during inspiration", "<bdi>sign</bdi> كوسماول، مميزة ل<bdi>diseases</bdi> تقييدية بالقلب"),
        ("Both atria are dilated. Left and right ventricles are normal in size and LVEF is 60%. No valve lesions", "استبعاد <bdi>diseases</bdi> الصمامات وضعف الانقباض ك<bdi>cause</bdi>، يوجه ل<bdi>disease</bdi> تقييدي أو بالتامور"),
        ("positive shifting dullness", "استسقاء بطني يعكس <bdi>congestion</bdi> وريدي جهازي <bdi>severe</bdi>"),
    ],
    "why_correct": [
        "بوجود صورة قصور قلب يميني بارز مع <bdi>sign</bdi> كوسماول ووظيفة ضخ <bdi>normal</bdi> بدون <bdi>disease</bdi> صمامي، الـ<bdi>cause</bdi> الأرجح <bdi>disease</bdi> بالتامور (تضيقي) أو اعتلال قلب تقييدي، والفحص الأدق لتوضيح هالتشريح هو <bdi>cardiac CT scan</bdi>.",
        "التصوير المقطعي يوضح سماكة التامور وتكلسه إن وجد بدقة عالية، وهذا يساعد يميز بين <bdi>pericarditis</bdi> المضيق و<bdi>cardiomyopathy</bdi> التقييدي.",
        "مراقبة هولتر وتصوير الشرايين واختبار المجهود لا تفيد ب<bdi>diagnosis</bdi> مشكلة تشريحية بالتامور أو عضلة القلب التقييدية زي هذي الـ<bdi>case</bdi>.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>echo</bdi> يظهر سماكة واضحة بجدران البطينين مع خلل بالاسترخاء، يصير <bdi>cardiomyopathy</bdi> التقييدي الـ<bdi>diagnosis</bdi> الأرجح بدل <bdi>disease</bdi> تامور.",
        "لو ظهر <bdi>calcification</bdi> واضح بالتامور بالأشعة العادية من البداية، يقوى احتمال <bdi>pericarditis</bdi> المضيق مباشرة.",
    ],
    "rule": "قصور قلب يميني مع <bdi>sign</bdi> كوسماول ووظيفة ضخ <bdi>normal</bdi> يوجه ل<bdi>disease</bdi> تامور تقييدي، والتصوير المقطعي يوضح التشريح بدقة.",
    "comparison": None,
    "guideline_note": None,
},
495: {
    "idea": "شاب عنده إغماء متكرر بالمجهود مع نبض كاروتيدي متقطع واندفاع قمي قوي و<bdi>murmur</bdi> انقباضية تزيد بالوقوف وتقل بقبضة اليد، وهذا نمط كلاسيكي معاكس يشخص <bdi>cardiomyopathy</bdi> الضخامي الانسدادي.",
    "clues": [
        ("jerky carotid pulsations and thrusting apex", "<bdi>signs</bdi> كلاسيكية ل<bdi>cardiomyopathy</bdi> الضخامي الانسدادي"),
        ("increases in intensity with standing and reduced during handgrip", "نمط استجابة الـ<bdi>murmur</bdi> المعاكس المميز لهالمرض تحديدًا"),
        ("left ventricular hypertrophy", "تضخم عضلة القلب المسبب للانسداد الديناميكي"),
    ],
    "why_correct": [
        "الـ<bdi>murmur</bdi> اللي تزيد بالوقوف (يقل الحجم داخل القلب فيزيد الانسداد) وتقل بقبضة اليد (يزيد الحجم فيقل الانسداد) نمط عكسي مميز جدًا لـ<bdi>hypertrophic obstructive cardiomyopathy</bdi>.",
        "النبض الكاروتيدي المتقطع والاندفاع القمي القوي مع تضخم البطين الأيسر بالتخطيط يدعمون نفس الـ<bdi>diagnosis</bdi>.",
        "الإغماء المتكرر بالمجهود عند شاب من أخطر <bdi>signs</bdi> هالمرض لأنه ينذر ب<bdi>risk</bdi> الموت القلبي المفاجئ.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>murmur</bdi> تزيد بقبضة اليد وتقل بفالسالفا (نمط معاكس)، يصير الـ<bdi>diagnosis</bdi> <bdi>mitral regurgitation</bdi> بدل الاعتلال الضخامي الانسدادي.",
        "لو كانت الـ<bdi>murmur</bdi> انقباضية بسيطة عند الحافة العلوية اليمنى تنتشر للرقبة مع نبض بطيء الارتفاع، يصير <bdi>aortic stenosis</bdi> حقيقي هو الـ<bdi>diagnosis</bdi>.",
    ],
    "rule": "<bdi>murmur</bdi> تزيد بالوقوف وتقل بقبضة اليد المستمرة تشخص <bdi>hypertrophic obstructive cardiomyopathy</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
496: {
    "idea": "شاب مصاب ب<bdi>cardiomyopathy</bdi> الضخامي عنده ألم صدري وإغماء متكرر بالمجهود، والسؤال يبي أفضل <bdi>treatment</bdi> دوائي أولي يقلل الانسداد الديناميكي ويمنع الـ<bdi>symptoms</bdi>.",
    "clues": [
        ("hypertrophic cardiomyopathy", "الـ<bdi>diagnosis</bdi> الأساسي معروف مسبقًا"),
        ("recurrent exertional chest pain and syncope", "<bdi>symptoms</bdi> انسداد ديناميكي <bdi>severe</bdi> بالمجهود يحتاج <bdi>treatment</bdi> دوائي فعال"),
    ],
    "why_correct": [
        "حاصرات البيتا زي <bdi>metoprolol</bdi> هي خط الـ<bdi>treatment</bdi> الدوائي الأول ب<bdi>cardiomyopathy</bdi> الضخامي الانسدادي العرضي، لأنها تبطئ معدل القلب وتقلل قوة الانقباض فتقلل شدة الانسداد.",
        "تقليل سرعة وقوة انقباض القلب يعطي وقت أطول لامتلاء البطين ويقلل تفاقم الانسداد الديناميكي أثناء المجهود.",
        "نيفيديبين ونيتروجليسرين وهيدرالازين من الموسعات الوعائية اللي تقلل مقاومة الشرايين الطرفية، وهذا فعليًا يزيد شدة الانسداد ويسوء الـ<bdi>symptoms</bdi> بهالمرض تحديدًا.",
    ],
    "when_changes": [
        "لو ما استجاب الـ<bdi>patient</bdi> على حاصر بيتا وحده أو ما تحمله، يصير حاصر قنوات كالسيوم من نوع verapamil الخط الثاني المناسب.",
        "لو استمرت الـ<bdi>symptoms</bdi> الـ<bdi>severe</bdi> رغم الـ<bdi>treatment</bdi> الدوائي الأمثل، يصير التفكير بخيارات تدخلية (استئصال العضلة أو تركيب منظم ضربات) ضروري.",
    ],
    "rule": "حاصرات البيتا هي خط الـ<bdi>treatment</bdi> الدوائي الأول ب<bdi>cardiomyopathy</bdi> الضخامي الانسدادي العرضي، وتجنّب الموسعات الوعائية لأنها تزيد الانسداد.",
    "comparison": None,
    "guideline_note": None,
},
497: {
    "idea": "<bdi>patient</bdi> <bdi>diabetes</bdi> وضغط عندها ألم صدري بالراحة مع تروبونين <bdi>elevated</bdi> بشدة وتغير تخطيطي (انقلاب موجة T) بدون ارتفاع segment، وهذا يشخص احتشاء قلبي بدون ارتفاع segment.",
    "clues": [
        ("retrosternal chest pain at rest for 3 hours", "ألم بالراحة لمدة ساعات، يوجه لمتلازمة تاجية <bdi>acute</bdi>"),
        ("Troponin 10", "ارتفاع واضح جدًا بالتروبونين، يؤكد تلف عضلة قلب حقيقي"),
        ("T-wave inversion in leads V2-V5", "تغير تخطيطي إقفاري بدون ارتفاع segment"),
    ],
    "why_correct": [
        "ارتفاع التروبونين بشدة مع ألم صدري بالراحة وتغير تخطيطي إقفاري (انقلاب T) بدون ارتفاع segment يشخص <bdi>non-ST elevation myocardial infarction</bdi>.",
        "ارتفاع التروبونين تحديدًا هو الفيصل بين الذبحة غير المستقرة (تروبونين <bdi>normal</bdi>) واحتشاء بدون ارتفاع segment (تروبونين <bdi>elevated</bdi>)، وهنا <bdi>elevated</bdi> جدًا.",
        "غياب ارتفاع segment بالتخطيط يستبعد احتشاء بارتفاع segment، وثبات الألم بالراحة يستبعد الذبحة المستقرة العادية.",
    ],
    "when_changes": [
        "لو كان التروبونين <bdi>normal</bdi> تمامًا رغم نفس الـ<bdi>symptoms</bdi> والتغيرات التخطيطية، يصير الـ<bdi>diagnosis</bdi> ذبحة غير مستقرة بدل احتشاء فعلي.",
        "لو ظهر ارتفاع واضح بـsegment ST بالتخطيط، يصير الـ<bdi>diagnosis</bdi> احتشاء بارتفاع segment (STEMI) بدل NSTEMI.",
    ],
    "rule": "ألم صدري بالراحة مع تروبونين <bdi>elevated</bdi> وتغيرات تخطيطية بدون ارتفاع segment يشخص <bdi>NSTEMI</bdi>.",
    "comparison": {
        "headers": ["الـ<bdi>case</bdi>", "التروبونين", "ارتفاع ST"],
        "rows": [
            ["ذبحة غير مستقرة", "<bdi>normal</bdi>", "لا"],
            ["NSTEMI", "<bdi>elevated</bdi>", "لا"],
            ["STEMI", "<bdi>elevated</bdi>", "نعم"],
        ],
    },
    "guideline_note": None,
},
498: {
    "idea": "<bdi>patient</bdi> <bdi>diabetes</bdi> وضغط دخل بذبحة غير مستقرة على <bdi>treatment</bdi> قياسي كامل (<bdi>aspirin</bdi> وحاصر بيتا و<bdi>heparin</bdi> <bdi>low</bdi> الوزن و<bdi>statin</bdi> ونترات)، والتروبونين <bdi>normal</bdi> وتخطيط القلب يظهر انخفاض segment، والسؤال يبي دواء إضافي مهم ناقص من الـ<bdi>treatment</bdi> القياسي.",
    "clues": [
        ("diagnosis of unstable angina", "الـ<bdi>diagnosis</bdi> الأساسي مؤكد"),
        ("Aspirin, bisoprolol, enoxaparn, atorvastatin and nitrate are started", "<bdi>treatment</bdi> قياسي شامل لكن ناقص عنصر مهم"),
        ("Troponin .001", "تروبونين <bdi>normal</bdi>، يدعم <bdi>diagnosis</bdi> الذبحة غير المستقرة مو احتشاء فعلي"),
    ],
    "why_correct": [
        "إضافة <bdi>clopidogrel</bdi> (مضاد صفائح ثاني) لل<bdi>treatment</bdi> القياسي بالذبحة غير المستقرة يعتبر معيار علاجي أساسي (الـ<bdi>treatment</bdi> المزدوج المضاد للصفائح) لتقليل <bdi>risk</bdi> تكرار الأحداث القلبية.",
        "الـ<bdi>treatment</bdi> المزدوج (<bdi>aspirin</bdi> مع كلوبيدوجريل) أثبت فعالية أعلى من الـ<bdi>aspirin</bdi> وحده بتقليل <bdi>risk</bdi> الاحتشاء أو الوفاة بالمتلازمة التاجية الـ<bdi>acute</bdi>.",
        "كانديسارتان واسبيرونولاكتون ما يعتبران جزء من الـ<bdi>treatment</bdi> القياسي الفوري للذبحة غير المستقرة، والستربتوكينيز (تحلل <bdi>thrombus</bdi>) غير مناسب هنا لأنه يستخدم فقط بوجود ارتفاع segment وليس انخفاضه.",
    ],
    "when_changes": [
        "لو كان تخطيط القلب يظهر ارتفاع segment بدل انخفاضه، يصير التفكير بتحلل الـ<bdi>thrombus</bdi> أو القسطرة العاجلة مناسب بدل الـ<bdi>treatment</bdi> المحافظ وحده.",
        "لو كان الـ<bdi>patient</bdi> عالي الخطورة جدًا (تروبونين <bdi>elevated</bdi> أو عدم استقرار مستمر)، يصير التوجه لقسطرة قلبية مبكرة أولوية أعلى من مجرد إضافة دواء.",
    ],
    "rule": "بالذبحة غير المستقرة، الـ<bdi>treatment</bdi> المزدوج المضاد للصفائح (<bdi>aspirin</bdi> مع <bdi>clopidogrel</bdi>) جزء أساسي من الـ<bdi>treatment</bdi> القياسي.",
    "comparison": None,
    "guideline_note": None,
},
# INSERT_EXPLANATIONS
}

WHY_WRONG = {
402: {
    "A": "نقص البوتاسيوم أثر معروف جدًا لكنه ليس المطلوب هنا حسب مفتاح الإجابة.",
    "B": "تشنج القصبات أثر نادر جدًا وأقل توثيقًا من التفاعل الدموي المطلوب هنا.",
    "C": "الـ<bdi>furosemide</bdi> يرفع السكر أحيانًا بجرعات عالية، لكن نقص السكر ليس أثر جانبي معروف له.",
},
403: {
    "A": "احتشاء الجدار الأمامي الوحشي يعطي ألم صدري وتغيرات تخطيطية، مو اضطراب رؤية ألوان.",
    "C": "نقص البوتاسيوم يسبب ضعف عضلي و<bdi>palpitations</bdi>، لكنه لا يفسر اصفرار الرؤية.",
    "D": "انخفاض حرارة الجسم يسبب بطء نبض وارتباك، لكن لا يفسر اضطراب رؤية الألوان النوعي.",
},
404: {
    "A": "الثيوفيلين يضاد تأثير الأدينوسين ويحتاج زيادة الجرعة، عكس المطلوب بالسؤال.",
    "C": "<bdi>renal failure</bdi> الـ<bdi>chronic</bdi> لا يغير آلية استقلاب الأدينوسين بشكل مباشر يستدعي تعديل الجرعة.",
    "D": "<bdi>mitral regurgitation</bdi> لا يؤثر على استقلاب أو فعالية الأدينوسين.",
},
405: {
    "A": "الـ<bdi>digoxin</bdi> يحسّن الـ<bdi>symptoms</bdi> ويقلل دخول المستشفى لكن بدون إثبات تقليل الوفيات.",
    "C": "الـ<bdi>furosemide</bdi> <bdi>treatment</bdi> عرضي لل<bdi>congestion</bdi> بدون أثر مثبت على تقليل الوفيات طويل المدى.",
    "D": "الهيدرالازين مفيد بحالات معينة (مع نترات) لكنه ليس الخيار الأقوى بالإثبات هنا.",
},
406: {
    "A": "الصمام التاجي المترهل لا يسبب حمى مستمرة بعد <bdi>procedure</bdi> سني بهذا الشكل الـ<bdi>acute</bdi>.",
    "C": "<bdi>myocardial infarction</bdi> يعطي ألم صدري <bdi>acute</bdi> وتغيرات تخطيطية، مو حمى مستمرة مع تضخم طحال.",
    "D": "تكرار الروماتيزم القلبي لا يفسر عادة تضخم الطحال وبيلة الدم المجهرية بنفس الدرجة.",
},
407: {
    "B": "عقيدات هيبردن آفات بالمفاصل مرتبطة بخشونة اليدين، ولا علاقة لها ب<bdi>angina</bdi>.",
    "C": "الذبحة المستقرة ترتبط بالمجهود فقط وتزول بالراحة، وهذا يخالف وصف الألم بالسؤال.",
    "D": "ذبحة برينزميتال ترتبط بتشنج وعائي بأوقات محددة غالبًا ليلًا، مو تدهور تدريجي بالشدة والمدة كما وصف هنا.",
},
408: {
    "A": "حاصر بيتا قد يزيد سوء التحكم بالسكر أكثر من مثبط ACE بهالسياق.",
    "B": "حاصر قنوات الكالسيوم خيار مقبول لاحقًا لكن مثبط ACE أفضل بوجود سكر <bdi>elevated</bdi> بسيط.",
    "C": "رفع جرعة الثيازيد يزيد الآثار الجانبية الأيضية (سكر وبوتاسيوم) بدون فايدة إضافية كبيرة بالضغط.",
},
409: {
    "A": "الزهري يسبب آفات جلدية مختلفة الشكل والتوزيع، ولا يفسر تجمع الـ<bdi>signs</bdi> الثلاث هنا معًا.",
    "B": "عدوى فيروس نقص المناعة قد تكون <bdi>factor</bdi> <bdi>risk</bdi> مصاحب لكنها لا تفسر مباشرة هالعلامات الثلاث الكلاسيكية.",
    "C": "<bdi>hepatitis</bdi> المعدي يعطي <bdi>symptoms</bdi> هضمية وكبدية، ولا يفسر الـ<bdi>murmur</bdi> أو الآفات العينية والجلدية المذكورة.",
},
410: {
    "A": "الديجيتاليس يحسّن الـ<bdi>symptoms</bdi> ويقلل دخول المستشفى بدون إثبات تقليل الوفيات.",
    "B": "إينالابريل هو الدواء اللي أثبتته الدراسات الكبرى بتقليل الوفيات فعليًا، لكنه ليس إجابة هذا السؤال حسب مفتاح الملف.",
    "D": "بروكيناميد دواء لاضطراب النظم وليس ل<bdi>treatment</bdi> <bdi>heart failure</bdi> أصلًا، ولا علاقة له بتقليل الوفيات هنا.",
},
411: {
    "A": "نقص البوتاسيوم أثر معروف جدًا لكنه ليس المطلوب هنا حسب مفتاح الإجابة.",
    "B": "تشنج القصبات أثر نادر جدًا وأقل توثيقًا من التفاعل الدموي المطلوب هنا.",
    "C": "الـ<bdi>furosemide</bdi> يرفع السكر أحيانًا بجرعات عالية، لكن نقص السكر ليس أثر جانبي معروف له.",
},
412: {
    "A": "نيفيديبين موسع وعائي يخفض الضغط أكثر ويزيد سوء الـ<bdi>case</bdi> بدل تحسينها.",
    "C": "بخاخ السالبوتامول يحفز مستقبلات بيتا بس ما يعتبر ترياق نوعي فعال لتسمم حاصرات بيتا بنفس درجة الجلوكاجون.",
    "D": "الأمينوفيلين ليس الترياق المعتمد لتسمم حاصرات بيتا وله مخاطر جانبية عالية بجرعات علاجية.",
},
413: {
    "B": "نيفيديبين حاصر كالسيوم <bdi>bilateral</bdi> هيدروبيريدين قصير المفعول، أقل ملاءمة كإضافة أولى للذبحة مقارنة بديلتيازيم.",
    "C": "<bdi>amlodipine</bdi> حاصر كالسيوم طويل المفعول لكنه أيضًا <bdi>bilateral</bdi> هيدروبيريدين، أقل استهدافًا لتقليل معدل القلب مقارنة بديلتيازيم.",
    "D": "ميتوبرولول حاصر بيتا قد يسوء <bdi>symptoms</bdi> العرج المتقطع الموجود عند الـ<bdi>patient</bdi>.",
},
414: {
    "A": "الـ<bdi>amiodarone</bdi> الفموي بطيء المفعول ولا يناسب <bdi>case</bdi> <bdi>acute</bdi> تحتاج تدخل سريع.",
    "C": "الأدينوسين خيار جيد لكنه يأتي بعد فشل المناورات المبهمية البسيطة، مو ك<bdi>step</bdi> أولى مباشرة.",
    "D": "تقويم النظم الكهربائي يحجز لو صارت الـ<bdi>patient</bdi> غير مستقرة، وهي حاليًا مستقرة الدورة الدموية.",
},
415: {
    "A": "<bdi>factor</bdi> ثامن ترياق لنقص <bdi>factor</bdi> التخثر الثامن (الهيموفيليا)، ولا علاقة له بعكس تأثير التحلل الخثري.",
    "C": "بروتامين ترياق نوعي لل<bdi>heparin</bdi>، ولا يعكس تأثير الأدوية المحللة لل<bdi>thrombus</bdi> زي streptokinase.",
    "D": "فيتامين K ترياق لمضادات فيتامين K (الـ<bdi>warfarin</bdi>)، ولا علاقة له بعكس تأثير التحلل الخثري.",
},
416: {
    "A": "وصف الـ<bdi>patient</bdi> بعدم التعاون أسلوب يلوم الـ<bdi>patient</bdi> ويكسر الثقة بدل توعيته.",
    "B": "إشراك الأسرة بدون إذن الـ<bdi>patient</bdi> أو ك<bdi>step</bdi> أولى يتجاوز استقلاليته بالقرار.",
    "C": "التهديد المباشر بالموت أسلوب غير أخلاقي ونادرًا ما ينجح بتغيير السلوك.",
},
417: {
    "A": "تغيير الوظيفة نصيحة متطرفة غير مبررة بمعلومات السؤال عن طبيعة عمله كموظف بنك.",
    "B": "قيادة السيارة بعد يومين فقط مبكرة جدًا وغير آمنة بعد احتشاء حديث.",
    "C": "الامتناع عن النشاط الجنسي لمدة 3 أشهر كاملة توصية أشد من اللازم لاحتشاء غير معقد.",
},
418: {
    "B": "إخباره مباشرة بدون تمهيد أسلوب قاسي وغير مراعٍ لل<bdi>case</bdi> النفسية بخبر بهالحساسية.",
    "C": "التعاطف مع مخاوفه <bdi>step</bdi> مهمة لاحقة بس مو بديل عن التمهيد الصحيح بإيصال الخبر نفسه.",
    "D": "مناقشة القرار مع الابن بدل الـ<bdi>patient</bdi> نفسه يتجاوز حق الـ<bdi>patient</bdi> بمعرفة حالته أولًا ما لم يطلب هو ذلك.",
},
419: {
    "A": "مزرعة الدم فحص مهم لل<bdi>diagnosis</bdi> الأولي بس أبطأ وأعقد لل<bdi>follow-up</bdi> اليومية المتكررة.",
    "B": "فحص الدم الكامل اليومي لا يعكس بدقة استجابة الالتهاب مقارنة بـCRP.",
    "C": "الـ<bdi>echo</bdi> المتكرر <bdi>procedure</bdi> مهم لكشف الـ<bdi>complications</bdi> لكنه أعقد وأبطأ من فحص دم بسيط لل<bdi>follow-up</bdi> الروتينية.",
},
420: {
    "A": "السوائل الوريدية تفيد بحالات نقص الحجم لكنها لا تعالج <bdi>block</bdi> كهربائي بالقلب.",
    "B": "الـ<bdi>dopamine</bdi> ممكن يستخدم كجسر مؤقت بس مو الحل النهائي ل<bdi>block</bdi> قلبي غير مستجيب للأتروبين.",
    "C": "الإيزوبرينالين خيار مؤقت أيضًا بس أقل أمانًا ويحمل <bdi>risk</bdi> اضطراب نظم إضافي مقارنة بالمنظم المؤقت.",
},
421: {
    "A": "الـ<bdi>block</bdi> من الدرجة الأولى بسيط ولا يسبب عادة بطء قلب <bdi>severe</bdi> بهالدرجة (41) وهبوط ضغط ملحوظ.",
    "C": "الـ<bdi>block</bdi> الكامل من الدرجة الثالثة ممكن لكن الصورة السريرية المرفقة بالصورة توافق درجة ثانية أكثر تحديدًا.",
    "D": "لا يوجد تصنيف طبي حقيقي باسم <bdi>block</bdi> من الدرجة الرابعة، فهذا خيار غير موجود أصلًا بالتصنيف الطبي.",
},
422: {
    "A": "المراقبة والـ<bdi>follow-up</bdi> وحدها غير كافية بدون توعية واضحة عن مخاطر الحمل بحالتها الخطيرة.",
    "B": "السماح لها بالمضي قدمًا بدون توعية كافية بالمخاطر يعرضها ل<bdi>risk</bdi> حقيقي غير مدروس.",
    "C": "الاتصال بالزوج مباشرة بدون إذن الـ<bdi>patient</bdi> ينتهك خصوصية معلوماتها الطبية.",
},
423: {
    "A": "تضيق برزخ الأبهر يعطي فرق ضغط بين الذراعين و<bdi>murmur</bdi> بالظهر، مو <bdi>murmur</bdi> انبساطية بالحافة القصية اليسرى بهالوصف.",
    "C": "<bdi>tamponade</bdi> القلب يسبب هبوط ضغط وأصوات قلب مكتومة، مو <bdi>murmur</bdi> انبساطية ونبض مرتد.",
    "D": "الفتحة البطينية تعطي <bdi>murmur</bdi> انقباضية شاملة، مو <bdi>murmur</bdi> انبساطية مبكرة بهالوصف.",
},
424: {
    "A": "الطمأنة وحدها غير كافية أمام تغير تخطيطي يوحي بفرط بوتاسيوم محتمل خطير.",
    "B": "طلب أنزيم القلب مناسب لو كان الاشتباه احتشاء، مو التغير الوصفي هنا الأقرب لفرط البوتاسيوم.",
    "D": "الإدخال والـ<bdi>echo</bdi> العاجل <bdi>step</bdi> مبكرة جدًا قبل التأكد من الـ<bdi>cause</bdi> البسيط والمباشر (فحص البوتاسيوم).",
},
425: {
    "A": "الأكسجين وحده يحسّن التأكسج لكنه لا يعالج <bdi>cause</bdi> الـ<bdi>congestion</bdi> (زيادة السوائل) بشكل مباشر.",
    "B": "ميتولازون مدر بولي إضافي يستخدم لو ما استجاب الـ<bdi>furosemide</bdi> وحده، مو ك<bdi>step</bdi> أولى بديلة عنه.",
    "D": "طلب <bdi>echo</bdi> عاجل مفيد ل<bdi>assessment</bdi> الـ<bdi>cause</bdi> لاحقًا لكنه ليس الـ<bdi>step</bdi> العلاجية الفورية ل<bdi>case</bdi> حرجة كهذي.",
},
426: {
    "A": "<bdi>myocardial infarction</bdi> يحتاج دليل مباشر (ألم صدري وتغير تخطيطي)، وغير مذكور صراحة بهالسؤال.",
    "C": "<bdi>heart failure</bdi> الأيمن المعزول يعطي <bdi>congestion</bdi> جهازي بدون <bdi>crepitations</bdi> رئوية بارزة بهالدرجة.",
    "D": "<bdi>mitral regurgitation</bdi> <bdi>acute</bdi> يحتاج دليل <bdi>murmur</bdi> جديدة صريحة بالفحص، وغير مذكور هنا.",
},
427: {
    "B": "طلب <bdi>echo</bdi> عاجل غير ضروري بوجود فحص سريري وتخطيط طبيعيين تمامًا بدون أي دليل مرضي.",
    "C": "الاستشارة الوراثية غير مبررة لبطء قلب فسيولوجي بسيط عند رياضي سليم.",
    "D": "تكرار التخطيط كل 3 أشهر <bdi>procedure</bdi> زائد غير مبرر ل<bdi>case</bdi> فسيولوجية <bdi>normal</bdi> تمامًا.",
},
428: {
    "A": "الـ<bdi>digoxin</bdi> يحسّن الـ<bdi>symptoms</bdi> بدون إثبات واضح لتقليل الوفيات.",
    "B": "نيفيديبين لا يعتبر من أدوية <bdi>heart failure</bdi> القياسية المثبتة لتقليل الوفيات.",
    "C": "<bdi>amiodarone</bdi> دواء لاضطراب النظم وليس <bdi>treatment</bdi> قياسي مثبت لتقليل الوفيات ب<bdi>heart failure</bdi>.",
},
429: {
    "A": "القول إن الـ<bdi>patient</bdi> بلا <bdi>risk</bdi> نزيف مطلق غير دقيق طبيًا، فكل مضاد تخثر يحمل بعض الـ<bdi>risk</bdi>.",
    "B": "<bdi>risk</bdi> الـ<bdi>thrombus</bdi> الـ<bdi>mild</bdi> وحده لا يعتبر الـ<bdi>factor</bdi> الحاسم بالمقارنة مع <bdi>risk</bdi> النزيف الفعلي.",
    "C": "القول إن <bdi>risk</bdi> النزيف أعلى من <bdi>risk</bdi> الـ<bdi>thrombus</bdi> عكس الواقع الشائع ب<bdi>patient</bdi> <bdi>diabetes</bdi> و<bdi>atrial fibrillation</bdi> بدون بيانات تدعم ذلك.",
},
430: {
    "A": "القول إنها نادرة وما تحتاج <bdi>anxiety</bdi> يقلل من مخاوفها الحقيقية ولا يعطيها معلومة كافية.",
    "B": "إخبارها بأن زوجها سيوقع الموافقة يتجاوز حقها الشخصي بالموافقة المستنيرة على <bdi>procedure</bdi> يخص جسدها.",
    "C": "شرح الـ<bdi>complications</bdi> وحده جيد لكن ناقص البدائل المتاحة، وهذا جزء أساسي من الموافقة المستنيرة الكاملة.",
},
431: {
    "A": "الـ<bdi>digoxin</bdi> لا يسبب نقص بوتاسيوم بشكل مباشر، بل خطره يزيد مع نقص البوتاسيوم.",
    "B": "الرانيتيدين مضاد حموضة ولا يؤثر على مستوى البوتاسيوم بالدم.",
    "D": "الاسبيرونولاكتون مدر بولي حافظ للبوتاسيوم، يرفعه عادة مو يخفضه.",
},
432: {
    "A": "الـ<bdi>digoxin</bdi> قد يسرّع التوصيل بالمسار الإضافي بمرضى WPW ويزيد خطورة الاضطراب.",
    "B": "الـ<bdi>amiodarone</bdi> خيار دوائي ممكن لكنه مو الـ<bdi>treatment</bdi> النهائي الشافي مقارنة بالاستئصال.",
    "C": "زيادة جرعة الـ<bdi>atenolol</bdi> فشلت أصلًا بالتحكم بالـ<bdi>symptoms</bdi> من البداية، فزيادتها غير كافية.",
},
433: {
    "A": "احتشاء الجدار الخلفي له معالم تخطيطية مختلفة (انخفاض ST بـV1-V2) عن نمط LBBB الموصوف.",
    "B": "<bdi>block</bdi> الحزمة اليمنى له نمط تخطيطي مختلف تمامًا عن <bdi>block</bdi> الحزمة اليسرى الموصوف بالصورة.",
    "C": "التسرع البطيني يعطي نمط QRS واسع منتظم سريع جدًا بدون علاقة بموجات P، مختلف عن نمط LBBB الموصوف.",
},
434: {
    "B": "CRP فحص التهاب عام غير نوعي لخلل وظيفة القلب.",
    "C": "CK فحص تلف عضلي عام (قلبي أو هيكلي) وليس نوعي لوظيفة البطين الأيسر.",
    "D": "التروبونين T فحص نوعي لتلف عضلة القلب الـ<bdi>acute</bdi>، مو ل<bdi>assessment</bdi> الوظيفة الانقباضية الـ<bdi>chronic</bdi>.",
},
435: {
    "B": "إيقاف الـ<bdi>warfarin</bdi> تمامًا مع البدء بثلاث مضادات صفائح يترك <bdi>risk</bdi> <bdi>thrombus</bdi> دماغية بدون تغطية كافية ويزيد <bdi>risk</bdi> نزيف غير ضروري بثلاثة أدوية معًا.",
    "C": "إيقاف الـ<bdi>warfarin</bdi> يترك الـ<bdi>patient</bdi> معرض ل<bdi>risk</bdi> <bdi>thrombus</bdi> دماغية ب<bdi>cause</bdi> <bdi>atrial fibrillation</bdi> المستمر.",
    "D": "الـ<bdi>warfarin</bdi> وحده بدون مضادات صفائح غير كافٍ لحماية الدعامة الحديثة من التجلط.",
},
436: {
    "A": "<bdi>atenolol</bdi> حاصر بيتا لا يرتبط عادة بوذمة وعائية بالوجه واللسان.",
    "C": "الـ<bdi>aspirin</bdi> قد يسبب تحسس جلدي أو <bdi>asthma</bdi> تحسسي لكن ليس التورم الوجهي واللساني النوعي هذا.",
    "D": "أتورفاستاتين قد يسبب آلام عضلية أو ارتفاع إنزيمات كبدية، ولا يرتبط بوذمة وعائية بهذا الشكل.",
},
437: {
    "A": "رامبريل مثبط ACE مشابه بالآلية لدواء اللوسارتان الحالي عند الـ<bdi>patient</bdi> تقريبًا (كلاهما يستهدف محور RAAS)، فإضافته أقل منطقية من مدر بولي بآلية مختلفة.",
    "B": "حاصر بيتا <bdi>step</bdi> لاحقة عادة بعد المدر البولي، مو الـ<bdi>step</bdi> الثالثة المعتادة أولًا.",
    "C": "حاصر ألفا (دوكسازوسين) يستخدم ك<bdi>step</bdi> متأخرة أكثر، وليس الإضافة الثالثة المعتادة.",
},
438: {
    "A": "الـ<bdi>warfarin</bdi> مضاد تخثر مختلف الآلية عن كلوبيدوجريل ولا يتداخل مع تفعيله الكبدي.",
    "C": "حاصرات البيتا لا تتداخل مع استقلاب أو تفعيل كلوبيدوجريل.",
    "D": "مثبطات استرداد الـ<bdi>serotonin</bdi> الانتقائية قد ترفع <bdi>risk</bdi> النزيف قليلًا لكنها لا تضعف فعالية كلوبيدوجريل نفسه.",
},
439: {
    "A": "مثبطات ACE تخفض BNP قليلًا مع تحسن <bdi>case</bdi> القلب، مو ترفعه كذبًا.",
    "B": "الـ<bdi>furosemide</bdi> يخفض BNP مع تحسن الـ<bdi>congestion</bdi>، ولا يرفعه بشكل كاذب.",
    "C": "السمنة ترتبط بانخفاض كاذب بمستوى BNP، عكس الارتفاع المطلوب بالسؤال.",
},
440: {
    "A": "<bdi>mitral stenosis</bdi> يعطي <bdi>murmur</bdi> انبساطية عند القمة، مو عند الحافة القصية اليسرى بهذا الوصف.",
    "B": "الفتحة البطينية تعطي <bdi>murmur</bdi> انقباضية شاملة، مو انبساطية متناقصة.",
    "C": "قصور الصمام ثلاثي الشرف يعطي <bdi>murmur</bdi> انقباضية عند الحافة السفلية اليسرى، مو <bdi>murmur</bdi> انبساطية بهذا الوصف.",
},
441: {
    "A": "اللمفوما قد تسبب حمى وتعب لكنها لا تفسر الـ<bdi>murmur</bdi> القلبية الجديدة والنمشيات بشكل مباشر.",
    "C": "عدوى العقدية المجموعة أ <bdi>cause</bdi> أولي محتمل للحمى الروماتيزمية لكن الصورة الحالية بعد فترة كامنة تدعم <bdi>endocarditis</bdi> تحت الـ<bdi>acute</bdi> أكثر.",
    "D": "<bdi>lupus</bdi> الجهازية تسبب <bdi>symptoms</bdi> مشابهة لكنها لا تفسر بشكل مباشر الـ<bdi>murmur</bdi> القلبية الجديدة بعد <bdi>procedure</bdi> سني حديث.",
},
442: {
    "A": "التهاب عضلة القلب الفيروسي ممكن لكنه أقل ارتباطًا بتوقيت الولادة المباشر مقارنة ب<bdi>cardiomyopathy</bdi> حول الولادة.",
    "B": "الإنتان النفاسي يحتاج دليل حمى وعدوى واضح، وغير مذكور بالسؤال بشكل كافٍ.",
    "C": "<bdi>endocarditis</bdi> يحتاج دليل حمى وعدوى و<bdi>murmur</bdi> قلبية جديدة مرتبطة بمصدر بكتيري، وغير مدعوم هنا.",
},
443: {
    "B": "اختبار الإجهاد بالثاليوم <bdi>procedure</bdi> غير عاجل وغير مناسب ب<bdi>case</bdi> <bdi>acute</bdi> ومهددة زي هذي.",
    "C": "تخطيط القلب والأشعة السينية مفيدان ك<bdi>step</bdi> أولية مساندة لكن لا يعطيان <bdi>diagnosis</bdi> تركيبي دقيق كالـ<bdi>echo</bdi>.",
    "D": "الرنين المغناطيسي القلبي واختبار وظائف الرئة <bdi>procedures</bdi> أبطأ وأعقد وغير مناسبة ك<bdi>step</bdi> أولى عاجلة.",
},
444: {
    "A": "الأموكسيسيلين مضاد حيوي وقائي يستخدم فقط لو كان الـ<bdi>procedure</bdi> يستدعي وقاية فعلية، وهذا غير منطبق هنا.",
    "B": "أوجمنتين أيضًا غير مطلوب لأن الـ<bdi>procedure</bdi> الجراحي هنا لا يستدعي وقاية من <bdi>endocarditis</bdi> أصلًا.",
    "C": "سيفوروكسيم كذلك غير مبرر لنفس الـ<bdi>cause</bdi>، فالـ<bdi>procedure</bdi> الجراحي النظيف لا يحتاج وقاية مضاد حيوي.",
},
445: {
    "A": "نقطتان فقط لا تعكس كل <bdi>factors</bdi> الـ<bdi>risk</bdi> المذكورة صراحة بالسؤال (قصور قلب وضغط و<bdi>diabetes</bdi> وسكتة سابقة).",
    "B": "ثلاث نقاط تنقص <bdi>factor</bdi> واحد على الأقل من الـ<bdi>factors</bdi> الأربعة المذكورة بوضوح بالسؤال.",
    "C": "أربع نقاط ما زالت تنقص نقطة واحدة، لأن <bdi>stroke</bdi> السابقة تحسب بنقطتين لا بنقطة واحدة.",
},
446: {
    "B": "الـ<bdi>echo</bdi> مفيد ل<bdi>assessment</bdi> وظيفة القلب البنيوية لكنه لا يكشف بشكل مباشر إقفار عضلة القلب أثناء المجهود.",
    "C": "تصوير الشرايين التاجية <bdi>procedure</bdi> تدخلي يحجز لحالات أعلى خطورة أو بعد <bdi>result</bdi> إيجابية باختبار أقل تدخلًا.",
    "D": "التصوير النووي بالمجهود خيار متقدم يستخدم عادة لو كان اختبار المجهود البسيط غير حاسم أو الـ<bdi>patient</bdi> غير قادر عليه.",
},
447: {
    "A": "<bdi>atenolol</bdi> حاصر بيتا لا يعالج الألم العضلي الهيكلي، وقد يبطئ القلب بدون داعٍ هنا.",
    "C": "النتروجليسرين <bdi>treatment</bdi> للذبحة القلبية، ولا فائدة منه بألم عضلي هيكلي غير قلبي.",
    "D": "الاكتفاء بالطمأنة بدون <bdi>treatment</bdi> مسكن يترك الـ<bdi>patient</bdi> يعاني من ألم يمكن تخفيفه بسهولة.",
},
448: {
    "A": "انخفاض ضغط النبض <bdi>sign</bdi> مساعدة لشدة التضيق لكنها ليست الـ<bdi>factor</bdi> الحاسم لتوقيت الجراحة.",
    "B": "شدة الـ<bdi>murmur</bdi> لا ترتبط دايمًا بدقة مع شدة التضيق الفعلية أو الحاجة للجراحة.",
    "D": "تضخم البطين الأيسر مؤشر مساعد على شدة الـ<bdi>disease</bdi> لكنه ليس الـ<bdi>factor</bdi> الأهم لتحديد توقيت الجراحة مقارنة بظهور الـ<bdi>symptoms</bdi>.",
},
449: {
    "B": "مضادات التخثر لا تستخدم ل<bdi>treatment</bdi> <bdi>aortic stenosis</bdi> نفسه بدون <bdi>cause</bdi> آخر مثل <bdi>atrial fibrillation</bdi>.",
    "C": "رأب الصمام بالبالون <bdi>procedure</bdi> يستخدم بحالات محددة (أطفال أو مرضى غير مرشحين للجراحة)، وليس خيار روتيني هنا.",
    "D": "الاستبدال الجراحي يحجز للحالات العرضية أو التضيق الـ<bdi>severe</bdi> جدًا، وهذا الـ<bdi>patient</bdi> عديم الـ<bdi>symptoms</bdi> بتضيق متوسط.",
},
450: {
    "A": "تقويم النظم الكهربائي يحجز ل<bdi>case</bdi> عدم الاستقرار، والـ<bdi>patient</bdi> هنا مستقر نسبيًا.",
    "B": "الأدينوسين يستخدم للتسرع المنتظم فوق البطيني، مو للرجفان الأذيني غير المنتظم.",
    "D": "المراقبة وحدها غير كافية بمعدل ضربات قلب <bdi>elevated</bdi> جدًا (170) مع نقص أكسجين مصاحب.",
},
451: {
    "A": "التهاب عضلة القلب يعطي ضعف انقباض عام بالـ<bdi>echo</bdi>، مو صورة تقييدية بالضغط الوريدي فقط.",
    "B": "القلب الرئوي يرتبط ب<bdi>disease</bdi> رئوي <bdi>chronic</bdi> مباشر يسبب ارتفاع ضغط رئوي، لكن <bdi>sign</bdi> كوسماول هنا أكثر توافقًا مع مشكلة تامورية.",
    "C": "<bdi>cardiomyopathy</bdi> يعطي عادة <bdi>murmur</bdi> أو ضعف انقباض واضح بالفحص، وهذا غير مذكور هنا.",
},
452: {
    "B": "أقل من 2 سم يمثل تضيق <bdi>severe</bdi> لكنه ليس الحد المعتمد للتصنيف الحرج تحديدًا.",
    "C": "أقل من 3 سم يمثل درجة أخف من التضيق ولا يعتبر <bdi>severe</bdi> أو حرجًا.",
    "D": "أقل من 4 سم قريب من الحد الـ<bdi>normal</bdi> تقريبًا ولا يمثل تضيق حرج إطلاقًا.",
},
453: {
    "A": "التهاب عضلة القلب لا يسبب <bdi>murmur</bdi> انقباضية جديدة صاخبة بهذا الشكل المفاجئ بعد احتشاء.",
    "B": "<bdi>cardiogenic shock</bdi> <bdi>diagnosis</bdi> عام لهبوط الدورة الدموية، لكنه لا يفسر مصدر الـ<bdi>murmur</bdi> الجديدة تحديدًا.",
    "D": "<bdi>heart failure</bdi> الأيمن الـ<bdi>acute</bdi> لا يعطي عادة <bdi>murmur</bdi> قمية صاخبة تنتشر للإبط بهذا الوصف.",
},
454: {
    "B": "الأدينوسين يستخدم للتسرع فوق البطيني المنتظم، مو للتحكم الـ<bdi>chronic</bdi> بمعدل <bdi>atrial fibrillation</bdi>.",
    "C": "الليدوكايين دواء لاضطراب النظم البطيني وليس للتحكم بمعدل <bdi>atrial fibrillation</bdi>.",
    "D": "النتروجليسرين موسع وعائي ل<bdi>treatment</bdi> الذبحة، ولا دور له بالتحكم بمعدل ضربات القلب.",
},
455: {
    "A": "الرنين المغناطيسي القلبي <bdi>procedure</bdi> متقدم وغير ضروري ك<bdi>step</bdi> أولى ل<bdi>assessment</bdi> <bdi>murmur</bdi> جديدة.",
    "C": "قسطرة القلب <bdi>procedure</bdi> تدخلي يحجز لحالات محددة بعد <bdi>results</bdi> الـ<bdi>echo</bdi> غير الحاسمة.",
    "D": "فحص Antistreptolysin O يفيد لو كان فيه اشتباه سابق بحمى روماتيزمية موثقة، وليس الـ<bdi>step</bdi> الأولى العامة ل<bdi>assessment</bdi> الـ<bdi>murmur</bdi>.",
},
456: {
    "A": "الـ<bdi>digoxin</bdi> خيار لاحق للتحكم بالـ<bdi>symptoms</bdi> أو بمعدل ضربات القلب، مو الـ<bdi>step</bdi> القياسية التالية هنا.",
    "C": "نيفيديبين لا يعتبر من أدوية <bdi>heart failure</bdi> المثبتة لتحسين البقاء.",
    "D": "الهيدرالازين بديل يستخدم لو ما تحمل الـ<bdi>patient</bdi> مثبط ACE أو حاصر بيتا، مو الـ<bdi>step</bdi> الأولى المعتادة هنا.",
},
457: {
    "A": "تصوير الشرايين بالأشعة المقطعية <bdi>procedure</bdi> أكثر تعقيدًا يحجز لحالات أعلى خطورة أو <bdi>results</bdi> غير حاسمة.",
    "B": "الـ<bdi>echo</bdi> بالإجهاد <bdi>procedure</bdi> تشخيصي أكثر تعقيدًا يستخدم عادة بعد <bdi>results</bdi> غير حاسمة من فحوصات أبسط.",
    "D": "الرنين المغناطيسي القلبي <bdi>procedure</bdi> متقدم وغير ضروري ك<bdi>step</bdi> أولى ب<bdi>patient</bdi> متوسط الخطورة بدون <bdi>symptoms</bdi>.",
},
458: {
    "B": "الأشعة المقطعية للشرايين التاجية لا تقيّم الصمامات القلبية، وغير مناسبة ل<bdi>assessment</bdi> <bdi>murmur</bdi> انبساطية.",
    "C": "الـ<bdi>echo</bdi> عبر المريء <bdi>procedure</bdi> أكثر تدخلًا يحجز لحالات غير واضحة بالـ<bdi>echo</bdi> العادي.",
    "D": "عدم <bdi>procedure</bdi> أي فحص إضافي يفوت فرصة <bdi>diagnosis</bdi> <bdi>cause</bdi> الـ<bdi>murmur</bdi> الجديدة المكتشفة.",
},
459: {
    "B": "إيقاف الـ<bdi>warfarin</bdi> يترك الـ<bdi>patient</bdi> عرضة ل<bdi>risk</bdi> تكرار الـ<bdi>thrombus</bdi> الدماغية بوجود <bdi>factors</bdi> <bdi>risk</bdi> عالية.",
    "C": "إضافة الـ<bdi>aspirin</bdi> لا تضيف حماية كافية وتزيد <bdi>risk</bdi> النزيف بدون فائدة واضحة إضافية.",
    "D": "الكلوبيدوجريل وحده أقل فعالية من مضاد التخثر الفموي بمنع الـ<bdi>thrombus</bdi> الدماغية المرتبطة ب<bdi>atrial fibrillation</bdi>.",
},
460: {
    "A": "حاصر قنوات الكالسيوم لا يعالج الـ<bdi>congestion</bdi> الـ<bdi>acute</bdi> ولا يعتبر الـ<bdi>step</bdi> الفورية المناسبة هنا.",
    "B": "حاصر البيتا غير مناسب ك<bdi>step</bdi> فورية ب<bdi>case</bdi> <bdi>congestion</bdi> <bdi>acute</bdi> غير مستقرة بعد.",
    "C": "الاسبيرونولاكتون دواء يضاف لاحقًا لتحسين البقاء، مو لتخفيف الـ<bdi>congestion</bdi> الـ<bdi>acute</bdi> الفوري.",
},
461: {
    "B": "<bdi>mitral stenosis</bdi> يعطي <bdi>murmur</bdi> انبساطية عند القمة، مو انقباضية بالحافة العلوية اليمنى.",
    "C": "تضيق الصمام ثلاثي الشرف نادر جدًا ويعطي <bdi>murmur</bdi> مختلفة الموقع، وغير متوافق مع الوصف هنا.",
    "D": "رغم إن <bdi>murmur</bdi> الحمل الفسيولوجية شائعة جدًا، انتشار الـ<bdi>murmur</bdi> هنا للرقبة تحديدًا يجعل الملف يعتمد <bdi>diagnosis</bdi> <bdi>aortic stenosis</bdi> حقيقي بدلًا منها.",
},
462: {
    "A": "الستيرويدات تحجز للحالات المقاومة أو المتكررة، مو ك<bdi>treatment</bdi> أول لالتهاب تامور غير معقد.",
    "B": "النتروجليسرين <bdi>treatment</bdi> للذبحة القلبية، ولا دور له ب<bdi>treatment</bdi> <bdi>pericarditis</bdi>.",
    "C": "الـ<bdi>warfarin</bdi> غير مناسب أصلًا وقد يزيد <bdi>risk</bdi> نزيف تاموري خطير.",
},
463: {
    "A": "مضادات الصفائح تستمر طويل المدى وليس لفترة قصيرة فقط بعد الاحتشاء.",
    "B": "حاصرات قنوات الكالسيوم ليست خط الوقاية الثانوية الأساسي المثبت بعد الاحتشاء.",
    "C": "الـ<bdi>treatment</bdi> الهرموني التعويضي لا يقي من <bdi>diseases</bdi> القلب التاجية وقد يزيد بعض المخاطر.",
},
464: {
    "B": "<bdi>amlodipine</bdi> لا يعتبر من الأدوية الأساسية المثبتة لتحسين البقاء ب<bdi>heart failure</bdi> الانقباضي.",
    "C": "الـ<bdi>furosemide</bdi> يعالج الـ<bdi>congestion</bdi> بس لا يثبت له أثر على تحسين البقاء طويل المدى.",
    "D": "الاسبيرونولاكتون دواء إضافي مهم لاحقًا، لكن مثبط ACE هو نقطة البداية الأساسية أولًا.",
},
465: {
    "A": "قياس التنفس يقيّم وظيفة الرئة و<bdi>asthma</bdi>، ولا يقيّم الصمام القلبي المسؤول عن الـ<bdi>symptoms</bdi> هنا.",
    "B": "الـ<bdi>echo</bdi> عبر جدار الصدر فحص أولي جيد بالممارسة المعتادة، لكن حسب هالملف الـ<bdi>echo</bdi> عبر المريء هو المعتمد لإعطاء تفاصيل أدق ب<bdi>case</bdi> التفاقم هذي.",
    "D": "التصوير المقطعي الحلزوني للصدر يفيد ل<bdi>diagnosis</bdi> <bdi>pulmonary embolism</bdi>، ولا يقيّم الصمام التاجي.",
},
466: {
    "A": "<bdi>murmur</bdi> <bdi>aortic stenosis</bdi> لا تتأثر بشكل مميز بالوقوف، بعكس <bdi>murmur</bdi> الاعتلال الضخامي الانسدادي.",
    "B": "الـ<bdi>treatment</bdi> الأساسي ل<bdi>aortic stenosis</bdi> الـ<bdi>severe</bdi> العرضي هو الجراحة، مو المدرات ك<bdi>treatment</bdi> أساسي.",
    "C": "<bdi>aortic stenosis</bdi> لا يرتبط بشكل مباشر ب<bdi>block</bdi> الحزمة اليمنى ك<bdi>sign</bdi> تخطيطية مميزة.",
},
467: {
    "A": "ليسينوبريل مثبط ACE لا يعالج التشنج الوعائي التاجي المسبب لل<bdi>symptoms</bdi> هنا.",
    "B": "كارفيديلول حاصر بيتا قد يزيد سوء التشنج الوعائي التاجي أحيانًا.",
    "D": "الـ<bdi>aspirin</bdi> مضاد صفائح لا يعالج آلية التشنج الوعائي المسببة لهالنوع من الذبحة.",
},
468: {
    "A": "خفض الضغط بقوة ب<bdi>aortic stenosis</bdi> <bdi>severe</bdi> قد يقلل التروية التاجية والدماغية بشكل خطير.",
    "C": "الموسعات الوعائية خطرة ب<bdi>aortic stenosis</bdi> <bdi>severe</bdi> لأنها تقلل مقاومة الأوعية دون تحسين تدفق عبر الصمام الضيق.",
    "D": "المدرات وحدها لا تعالج المشكلة التشريحية الأساسية وقد تقلل التروية أكثر ب<bdi>patient</bdi> معتمد على حجم كافٍ لعبور الصمام الضيق.",
},
469: {
    "A": "المضاد الحيوي غير مناسب بدون دليل عدوى جرثومية واضحة هنا.",
    "B": "الستيرويدات تحجز للحالات المقاومة لمضادات الالتهاب غير الستيرويدية، مو كخط أول.",
    "C": "مضاد التخثر قد يزيد <bdi>risk</bdi> نزيف تاموري خطير ب<bdi>pericarditis</bdi> الـ<bdi>acute</bdi>.",
},
470: {
    "A": "الـ<bdi>digoxin</bdi> يحسّن الـ<bdi>symptoms</bdi> ويقلل دخول المستشفى بدون إثبات تقليل مباشر للوفيات.",
    "B": "المدرات تخفف الـ<bdi>congestion</bdi> والـ<bdi>symptoms</bdi> بدون إثبات تقليل مباشر للوفيات.",
    "C": "مضادات التخثر تمنع الجلطات بحالات محددة (<bdi>atrial fibrillation</bdi> مثلًا) لكنها لا تقلل وفيات <bdi>heart failure</bdi> نفسه بشكل عام.",
},
471: {
    "B": "<bdi>aortic regurgitation</bdi> يعطي <bdi>murmur</bdi> انبساطية عند الحافة القصية اليسرى، مو انقباضية عند القمة.",
    "C": "<bdi>mitral stenosis</bdi> يعطي <bdi>murmur</bdi> انبساطية عند القمة، مو انقباضية.",
    "D": "<bdi>aortic stenosis</bdi> يعطي <bdi>murmur</bdi> انقباضية عند الحافة العلوية اليمنى تنتشر للرقبة، مو عند القمة.",
},
472: {
    "A": "نوبة الوعائي المبهمي لا تسبب ألم صدري <bdi>acute</bdi> ينتشر للظهر ولا ترتبط ب<bdi>factors</bdi> <bdi>risk</bdi> التسلخ.",
    "B": "<bdi>pulmonary embolism</bdi> يسبب ضيق نفس وألم صدري جنبي، مو ألم ظهري منتشر بهذا الشكل المفاجئ.",
    "D": "<bdi>myocardial infarction</bdi> ممكن لكنه لا يفسر بشكل مباشر انتشار الألم للظهر بهذا الشكل الكلاسيكي.",
},
473: {
    "B": "متلازمة WPW تعطي <bdi>palpitations</bdi> مع تخطيط مختلف (موجة دلتا وPR قصير) بدون النبض الكاروتيدي المتقطع والـ<bdi>murmur</bdi> الموصوفة.",
    "C": "متلازمة بروجادا تسبب اضطراب نظم بطيني مفاجئ بدون <bdi>murmur</bdi> قلبية أو نبض كاروتيدي مميز.",
    "D": "متلازمة QT الطويل تسبب اضطراب نظم بطيني خطير لكن بدون الـ<bdi>murmur</bdi> والـ<bdi>tremor</bdi> الجدارية الموصوفة هنا.",
},
474: {
    "A": "الـ<bdi>digoxin</bdi> خيار إضافي لاحق أو لحالات <bdi>atrial fibrillation</bdi> مصاحب، مو الـ<bdi>step</bdi> القياسية التالية هنا.",
    "B": "لوسارتان بديل لمثبط ACE لو ما تحمّله الـ<bdi>patient</bdi>، مو إضافة روتينية فوقه.",
    "D": "عدم إضافة أي <bdi>treatment</bdi> يفوت فرصة تحسين البقاء طويل المدى بإضافة حاصر بيتا.",
},
475: {
    "A": "الـ<bdi>digoxin</bdi> خيار إضافي لاحق، مو الدواء الأساسي الناقص هنا.",
    "C": "الهيدرالازين بديل يستخدم لو ما تحمل الـ<bdi>patient</bdi> مثبط ACE، مو الخيار الأول.",
    "D": "الاسبيرونولاكتون تضاف لاحقًا بعد تأسيس الـ<bdi>treatment</bdi> الأساسي بمثبط ACE وحاصر بيتا أولًا.",
},
476: {
    "A": "التاريخ العائلي <bdi>factor</bdi> <bdi>risk</bdi> ثابت غير قابل للتعديل.",
    "C": "الجنس <bdi>factor</bdi> <bdi>risk</bdi> ثابت لا يمكن تغييره.",
    "D": "مؤشر كتلة الجسم قابل للتعديل جزئيًا لكنه أقل تأثيرًا مباشرًا ووضوحًا من التدخين ب<bdi>disease</bdi> القلب الإقفاري.",
},
477: {
    "A": "<bdi>mitral stenosis</bdi> يعطي <bdi>murmur</bdi> انبساطية عند القمة، مو انقباضية تنتشر للرقبة.",
    "C": "<bdi>mitral valve prolapse</bdi> يعطي نقرة انقباضية مع <bdi>murmur</bdi> متأخرة عند القمة، مختلف عن الوصف هنا.",
    "D": "قصور الصمام ثلاثي الشرف يعطي <bdi>murmur</bdi> عند الحافة السفلية اليسرى تزيد بالشهيق، مختلف عن الوصف هنا.",
},
478: {
    "A": "مؤشر كتلة جسم 31.2 يعتبر سمنة <bdi>mild</bdi> لكنه أقل خطورة من <bdi>diagnosis</bdi> <bdi>diabetes</bdi> مؤكد.",
    "B": "محيط خصر 103 سم <bdi>factor</bdi> <bdi>risk</bdi> لمتلازمة أيضية لكنه أقل قوة من <bdi>diagnosis</bdi> <bdi>diabetes</bdi> مؤكد بقيمتين.",
    "C": "ضغط 132/82 قريب من الـ<bdi>normal</bdi> وليس <bdi>diagnosis</bdi> ضغط <bdi>chronic</bdi> مؤكد بعد.",
},
479: {
    "A": "الـ<bdi>aspirin</bdi> وحده أقل فعالية بكثير من مضاد التخثر الفموي بمنع الـ<bdi>thrombus</bdi> الدماغية ب<bdi>atrial fibrillation</bdi>.",
    "B": "مدى INR بين 3 و4 أعلى من اللازم ويزيد <bdi>risk</bdi> النزيف بدون داعٍ ب<bdi>patient</bdi> <bdi>atrial fibrillation</bdi> بسيط.",
    "D": "عدم إضافة أي <bdi>treatment</bdi> وقائي يترك الـ<bdi>patient</bdi> عرضة لتكرار الـ<bdi>thrombus</bdi> الدماغية بشكل واضح.",
},
480: {
    "B": "<bdi>amlodipine</bdi> لا يعتبر الإضافة القياسية الأولى بعد الاحتشاء مقارنة بحاصر بيتا.",
    "C": "لوسارتان بديل لمثبط ACE لو ما تحمله الـ<bdi>patient</bdi>، مو إضافة قياسية أولى هنا.",
    "D": "الـ<bdi>warfarin</bdi> غير مناسب بدون <bdi>cause</bdi> واضح مثل <bdi>atrial fibrillation</bdi> أو <bdi>thrombus</bdi> بالبطين.",
},
481: {
    "A": "سونار الشرايين السباتية يفيد ل<bdi>assessment</bdi> <bdi>risk</bdi> <bdi>stroke</bdi>، لا يكشف <bdi>cause</bdi> هرموني للرجفان.",
    "C": "اختبار المجهود يقيّم الإقفار القلبي، ولا يكشف الـ<bdi>cause</bdi> الهرموني المحتمل هنا.",
    "D": "مراقبة هولتر تفيد لتوثيق اضطراب النظم، لكنها لا تكشف الـ<bdi>cause</bdi> الهرموني وراء الـ<bdi>symptoms</bdi> الجهازية.",
},
482: {
    "A": "الاسبيرونولاكتون خيار إضافي لاحق، ولا يعالج الضغط الـ<bdi>severe</bdi> الارتفاع بشكل كافٍ وحده هنا.",
    "B": "الـ<bdi>furosemide</bdi> يخفف الـ<bdi>congestion</bdi> لكنه لا يعالج الضغط الـ<bdi>severe</bdi> الارتفاع بنفس فعالية مثبط ACE.",
    "C": "بيسوبرولول قد يساعد لاحقًا بس لا يعالج الضغط الـ<bdi>severe</bdi> الارتفاع بنفس الفعالية والحماية الكلوية لمثبط ACE هنا.",
},
483: {
    "A": "تضيق برزخ الأبهر يعطي فرق ضغط بين الذراعين و<bdi>murmur</bdi> بالظهر، مختلف عن الوصف هنا.",
    "C": "<bdi>mitral regurgitation</bdi> يعطي <bdi>murmur</bdi> انقباضية عند القمة، مو انبساطية عند الحافة اليسرى.",
    "D": "<bdi>aortic stenosis</bdi> يعطي <bdi>murmur</bdi> انقباضية، مو انبساطية كما وصف هنا.",
},
484: {
    "A": "الجمع بين مضادي صفائح أقل فعالية من مضاد التخثر الفموي بمنع الـ<bdi>thrombus</bdi> الدماغية ب<bdi>atrial fibrillation</bdi>.",
    "B": "الكلوبيدوجريل وحده أقل فعالية من مضاد التخثر الفموي بهالسياق.",
    "D": "الـ<bdi>aspirin</bdi> وحده أضعف بكثير من مضاد التخثر الفموي بمنع الـ<bdi>thrombus</bdi> الدماغية المرتبطة ب<bdi>atrial fibrillation</bdi>.",
},
485: {
    "A": "الـ<bdi>aspirin</bdi> وحده أقل فعالية من مضاد التخثر الفموي بمنع الـ<bdi>thrombus</bdi> الدماغية بوجود <bdi>factor</bdi> <bdi>risk</bdi> السن.",
    "B": "الكلوبيدوجريل وحده أيضًا أقل فعالية من مضاد التخثر الفموي بهالسياق.",
    "C": "الـ<bdi>aspirin</bdi> مع دايبيريدامول أقل فعالية من مضاد التخثر الفموي بمنع الـ<bdi>thrombus</bdi> الدماغية ب<bdi>atrial fibrillation</bdi>.",
},
486: {
    "A": "الإقفار الحرج يحتاج مؤشر أقل بكثير (أقل من 0.4) مع ألم بالراحة أو تقرحات، وهذا غير موجود هنا.",
    "B": "المؤشر 0.84 غير <bdi>normal</bdi> فعليًا ويقع ضمن نطاق <bdi>disease</bdi> الشرايين الطرفية، فوصفه بالـ<bdi>normal</bdi> غير صحيح.",
    "D": "الأوعية غير القابلة للانضغاط تعطي مؤشر <bdi>elevated</bdi> جدًا (أكبر من 1.3)، عكس القيمة الـ<bdi>low</bdi> هنا.",
},
487: {
    "A": "عدم إضافة <bdi>treatment</bdi> يفوت فرصة الوقاية الثانوية المهمة بالـ<bdi>statin</bdi> بعد الاحتشاء.",
    "C": "الفينوفايبرات ليس الـ<bdi>treatment</bdi> القياسي الأول للوقاية الثانوية بعد الاحتشاء مقارنة بالـ<bdi>statin</bdi>.",
    "D": "النياسين ليس أيضًا الـ<bdi>treatment</bdi> القياسي الأول هنا، وله آثار جانبية أكثر مقارنة بالـ<bdi>statin</bdi>.",
},
488: {
    "A": "الطمأنة وحدها غير كافية بوجود ألم صدري مجهودي مستمر ب<bdi>patient</bdi> <bdi>diabetes</bdi> يحتاج <bdi>assessment</bdi> إقفاري.",
    "C": "القسطرة <bdi>procedure</bdi> تدخلي يحجز لحالات أعلى خطورة أو بعد <bdi>result</bdi> إيجابية باختبار أقل تدخلًا.",
    "D": "التصوير النووي بالأدينوسين خيار متقدم يستخدم عادة لو كان اختبار المجهود غير ممكن أو غير حاسم.",
},
489: {
    "B": "<bdi>cardiomyopathy</bdi> التقييدي يعطي عادة سماكة جدارية أو خلل بالـ<bdi>echo</bdi> أوضح من مجرد تضخم متحدد المركز بضغط <bdi>chronic</bdi>.",
    "C": "الإقفار الصامت يحتاج دليل إقفاري (تغيرات تخطيطية أو اختبار مجهود إيجابي)، وغير مذكور هنا.",
    "D": "<bdi>pericarditis</bdi> المضيق يعطي <bdi>sign</bdi> كوسماول وضغط وريدي <bdi>elevated</bdi> لا يهبط بالشهيق، وهذا غير موصوف هنا.",
},
490: {
    "A": "الـ<bdi>digoxin</bdi> يستخدم ل<bdi>treatment</bdi> <bdi>symptoms</bdi> <bdi>congestion</bdi> فعلية، وهي غير موجودة هنا.",
    "C": "الـ<bdi>furosemide</bdi> يعالج <bdi>congestion</bdi> فعلي، والـ<bdi>patient</bdi> هنا بدون <bdi>symptoms</bdi> <bdi>congestion</bdi> حاليًا.",
    "D": "الاكتفاء ب<bdi>follow-up</bdi> الـ<bdi>echo</bdi> بدون <bdi>treatment</bdi> يفوت فرصة علاجية مهمة تحسن البقاء رغم غياب الـ<bdi>symptoms</bdi>.",
},
491: {
    "A": "الـ<bdi>digoxin</bdi> يحسّن الـ<bdi>symptoms</bdi> بس لا يعالج المشكلة التشريحية الأساسية (القصور التاجي الـ<bdi>severe</bdi>).",
    "B": "لوسارتان بديل دوائي لمثبط ACE، ولا يعالج المشكلة التشريحية الأساسية أيضًا.",
    "C": "الـ<bdi>follow-up</bdi> لمدة 6 أشهر تأخير غير مبرر ب<bdi>patient</bdi> عرضي ب<bdi>mitral regurgitation</bdi> <bdi>severe</bdi> يحتاج تدخل جراحي.",
},
492: {
    "A": "الاستبدال الجراحي يحجز لحالات ظهور الـ<bdi>symptoms</bdi> أو تدهور وظيفة البطين، وهذا غير موجود حاليًا.",
    "C": "الـ<bdi>furosemide</bdi> يعالج <bdi>congestion</bdi> فعلي، وهو غير موجود عند <bdi>patient</bdi> عديم الـ<bdi>symptoms</bdi> هنا.",
    "D": "مثبط ACE لا يعالج المشكلة التشريحية لل<bdi>aortic stenosis</bdi> ولا يعتبر الـ<bdi>step</bdi> المناسبة بهالمرحلة.",
},
493: {
    "B": "<bdi>aortic stenosis</bdi> يعطي <bdi>murmur</bdi> انقباضية تنتشر للرقبة، مو انبساطية عند القمة.",
    "C": "تضيق الصمام ثلاثي الشرف يعطي <bdi>murmur</bdi> عند الحافة السفلية اليسرى تزيد بالشهيق، مختلف عن الوصف هنا.",
    "D": "تضيق الصمام الرئوي يعطي <bdi>murmur</bdi> انقباضية عند الحافة العلوية اليسرى، مو انبساطية عند القمة.",
},
494: {
    "A": "مراقبة هولتر تفيد لتوثيق اضطراب نظم، ولا تكشف مشكلة تشريحية بالتامور أو عضلة القلب.",
    "C": "تصوير الشرايين التاجية يقيّم انسداد الشرايين، ولا يفيد ب<bdi>diagnosis</bdi> مشكلة تامورية أو تقييدية.",
    "D": "اختبار المجهود يقيّم الإقفار القلبي، ولا يفيد بتوضيح مشكلة تشريحية بالتامور.",
},
495: {
    "A": "<bdi>aortic stenosis</bdi> يعطي نبض بطيء الارتفاع، مو نبض متقطع قوي كما وصف هنا.",
    "B": "تضيق الصمام الرئوي يعطي <bdi>murmur</bdi> تختلف استجابتها للمناورات عن النمط المعاكس المميز هنا.",
    "C": "الفتحة البطينية تعطي <bdi>murmur</bdi> انقباضية شاملة ثابتة، ولا تتأثر بنفس النمط بالوقوف وقبضة اليد.",
},
496: {
    "A": "نيفيديبين موسع وعائي يزيد شدة الانسداد الديناميكي ويسوء الـ<bdi>symptoms</bdi> بهالمرض.",
    "C": "الهيدرالازين موسع وعائي أيضًا يزيد الانسداد الديناميكي بدل تقليله.",
    "D": "النتروجليسرين موسع وعائي يقلل الحمل على القلب لكنه يزيد شدة الانسداد بهالمرض تحديدًا.",
},
497: {
    "A": "الذبحة المستقرة ترتبط بالمجهود فقط وتزول بالراحة، ولا ترتبط بتروبونين <bdi>elevated</bdi>.",
    "B": "الذبحة غير المستقرة تترافق مع تروبونين <bdi>normal</bdi> عادة، بعكس الارتفاع الواضح هنا.",
    "C": "احتشاء بارتفاع segment يحتاج دليل ارتفاع واضح بتخطيط القلب، وهذا غير موجود هنا (انقلاب T فقط).",
},
498: {
    "B": "كانديسارتان دواء ضغط ولا يعتبر جزء من الـ<bdi>treatment</bdi> القياسي الفوري للذبحة غير المستقرة.",
    "C": "الستربتوكينيز يستخدم فقط بوجود ارتفاع segment، وهنا التخطيط يظهر انخفاض segment.",
    "D": "الاسبيرونولاكتون دواء ل<bdi>heart failure</bdi> وليس جزء من الـ<bdi>treatment</bdi> القياسي الفوري للذبحة غير المستقرة.",
},
# INSERT_WHY_WRONG
}

# exact substrings (verbatim from the stem) to wrap in <mark> on the front of the card.
# these must literally appear in the stem and must not span a <br> line break.
HIGHLIGHT_TERMS = {
402: ["furosemide", "congestive heart failure"],
403: ["slightly yellow tinged", "Blood pressure 90/50", "Heart rate 60"],
404: ["regular narrow", "complex tachycardia", "IV adenosine", "previous ischemic stroke"],
405: ["chronic heart failure", "increase survival"],
406: ["unexplained fever 19 days", "teeth have been extracted", "systolic murmur and splenomegaly"],
407: ["become much worse over the last 3 weeks", "sitting in a chair or in bed at night reading"],
408: ["hydrochlorothiazide 25 mg/day", "Blood pressure 155/101", "Glucose, fasting 7.3"],
409: ["intravenous drug user", "painless erythematous lesions noted on the palms", "haemorrhage under the fingernails"],
410: ["reduce mortality", "congestive heart"],
411: ["furosemide", "congestive heart failure"],
412: ["accidental ingestion of a higher dose of atenolol", "Heart rate 46"],
413: ["intermittent claudication", "still gets angina with moderate exercise"],
414: ["palpitations for 2-hours", "Heart rate 150", "Thyroid-Stimulating Hormone 3.2"],
415: ["massive hematemesis", "streptokinase infusion"],
416: ["advised to quit smoking", "he is unwilling to do"],
417: ["7-day admission for", "given 5 different drugs"],
418: ["refractory heart failure", "consider him for heart transplantation", "After setting the scene"],
419: ["infective endocardits started on antibiotics", "simplest way in monitoring"],
420: ["2:1 AV block", "IV atropine given with no effect", "Blood pressure 80/45"],
421: ["inferior MI and received thromolytic therapy", "Blood pressure 80/50", "Heart rate 41"],
422: ["mitral stenosis with pulmonary hypertension", "hiding the diagnosis from her husband"],
423: ["collapsing pulse and wide pulse pressure", "pistol-shot sound heard over femoral arteries"],
424: ["hypertensive and on captopril", "tented T waves"],
425: ["high", "bilateral basal crackles at both lungs", "S3 was heard at the apex", "Oxygen saturation 88"],
426: ["paroxysmal nocturnal", "S3 was heard at the apex", "Oxygen saturation 88"],
427: ["resting pulse of 47 beat/min", "Normal CBC, renal function, LFT, and TSH"],
428: ["treated with loop diuretic and ACE", "good control of her symptoms"],
429: ["hesitant to start anti-coagulant due to its risk"],
430: ["admitted to the hospital for cardiac catheterization", "concerned about"],
431: ["nebulized", "Spironolactone", "serum potassium is noted to be 2.8"],
432: ["short PR interval", "Wolf-", "given atenolol with no response"],
433: ["intermittent chest pains for the past 2 days", "tachycardic and sweaty"],
434: ["long", "standing hypertension", "rare crackles at the bases of the lungs"],
435: ["percutaneous coronary intervention", "warfarin, paracetamol and allopurinol"],
436: ["tongue and facial swelling", "thrombolysed for a myocardial infarction"],
437: ["losartan and amlodipine", "blood test and renal function profile were within the normal limits"],
438: ["intolerant of aspirin", "make clopidogrel less effective"],
439: ["suspected left ventricular heart failure", "slightly elevated"],
440: ["tetralogy repair", "decrescendo diastolic murmur that increases with inspiration"],
441: ["dental extraction 2 months ago", "petechia over lower limb", "mild proteinuna and microscopic hematuria"],
442: ["post vaginal", "displaced down with pan-systolic murmur", "S3 gallop"],
443: ["post vaginal", "Oxygen saturation 90"],
444: ["aortic valve and mechanical aortic valve replacement", "grade 1/6 ejection systolic murmur at aortic area"],
445: ["diabetic mellitus, hypertension and hyperlipidaemia", "with history", "Atrial fibrillation on ECG"],
446: ["mainly after heavy physical exertion", "examination and baseline ECG were normal"],
447: ["program a week prior to the onset", "increase in seventy with movement"],
448: ["murmur, which propagated to the neck"],
449: ["ventricular systolic function", "Aortic valve gradient of 40"],
450: ["pulse rate of 170/min", "normal cardiac and chest examinations"],
451: ["past history of old", "rises further on inspiration", "normal with no murmurs"],
452: ["mitral valve orifice measurement is consider critical"],
453: ["acutely unwell with sever dyspnea", "radiates to the axilla and bilateral"],
454: ["heart failure requires rate control", "coexisting atrial fibrillation"],
455: ["Asymptomatic healthy 24-year-old woman", "grade II mid-"],
456: ["function so furosemide was added", "good control of his symptoms"],
457: ["Pooled Cohort", "intermediate risk of myocardial infarction"],
458: ["grade 2/6 diastolic murmur heard best", "Peripheral pulses are normal"],
459: ["ischemic attack and hypertension", "normal sinus"],
460: ["raised central venous pressure, fine crackles at lung bases and hepatomegaly", "Brain natriuretic peptide 900"],
461: ["30th week of pregnancy", "mid-systolic ejection murmur at"],
462: ["exacerbated when leaning forward", "diffuse, concave upward ST-segment elevations"],
463: ["secondary prevention of infarction"],
464: ["non-decompensated systolic heart failure", "ejection fraction of 25%"],
465: ["moderate mitral regurgitation", "grade 3/6 holosystolic murmur radiating to the axilla"],
466: ["exertional syncope and progressive", "clear evidence of pulmonary edema"],
467: ["recurrent severe nocturnal chest pain", "normal cardiac", "positive ergonovine echocardiography testing"],
468: ["progressive exertional shortness of breath that", "shows cardiomegaly"],
469: ["reduced with sitting forward", "friction rub", "cardiac enzymes are within normal"],
470: ["reduced mortality rate in congestive"],
471: ["with sustained handgrip and reduced with Valsalva"],
472: ["radiates to his back", "heavy smoker and has history of hypertension", "pressure 85/56"],
473: ["harsh ejection systolic murmur with a palpable systolic thrill", "jerky carotid pulse"],
474: ["enalopril 10 mg OD, simvastatin 40 mg OD, furosemide 40 mg OD", "chest is clear and heart sounds are normal"],
475: ["aspirin 75 mg OD, simvastatin 40 mg OD and furosemide 40 mg OD", "there is no peripheral edema"],
476: ["previous history", "modifiable risk factors"],
477: ["slow rising", "upper right sternal edge, radiating to the"],
478: ["43-year-old healthy man concerned about heart disease"],
479: ["right-sided weakness that lasted 10 minutes and", "in atrial fibrillation"],
480: ["bilateral basal crackles on auscultation of", "acute inferior"],
481: ["weight loss over the last 2 months", "irregularly irregular pulse and"],
482: ["unable to walk more than 200-300 meters", "Creatinine 133"],
483: ["diastolic murmur best heard at the left steal edge", "apex beat is displaced outwards"],
484: ["persistent atrial fibrillation", "no contraindications to any antithrombotic treatments"],
485: ["completely", "asthma and on salbutamol PRN"],
486: ["exacerbated by exercise and", "brachial pressure Index is 0.84"],
487: ["Cholesterol (HDL) 1.0", "Cholesterol (LDL) 3.36"],
488: ["vague chest pain with", "Electrocardiogram: Normal."],
489: ["loud A2 and left ventricular S4, no murmur", "concentric left ventricular hypertrophy"],
490: ["cardiomegaly on chest X-ray during pre-employment check", "Dilated left ventricle with ejection fraction of 40%"],
491: ["symptoms improved with furosemide, spironolactone,", "mildly dilated left ventricle, LVEF 45%"],
492: ["slow raising carotid pulsation", "severely stenosed aortic valve"],
493: ["loud S1, loud P2 and mid diastolic rumbling murmur", "JVP of 5 cm above sternal angle"],
494: ["fails to descend during inspiration", "Both atria are dilated"],
495: ["jerky carotid pulsations and thrusting apex", "increases in intensity with standing and reduced during"],
496: ["hypertrophic cardiomyopathy", "recurrent exertional"],
497: ["chest pain at rest", "T-wave inversion in leads V2-V5"],
498: ["diagnosis of unstable angina", "Troponin .001"],
}
