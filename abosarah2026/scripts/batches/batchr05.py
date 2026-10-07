# -*- coding: utf-8 -*-
# Batch r05 — OBGYN slice (AS-1496 .. AS-2247)

EXPLANATIONS = {

"AS-1496": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "السؤال عن <bdi>fertility-sparing</bdi> management لـ<bdi>atypical complex hyperplasia</bdi> بمريضة شابة.",
    "clues": [
        ("25-year-old", "عمر صغير يعني لازم نحافظ على <bdi>fertility</bdi>"),
        ("Atypical complex hyperplasia", "<bdi>premalignant lesion</bdi>، علاجها النهائي <bdi>hysterectomy</bdi> لكن ممكن نأجله"),
    ],
    "why_correct": [
        "<bdi>atypical hyperplasia</bdi> حالة <bdi>premalignant</bdi>، والعلاج النهائي <bdi>hysterectomy</bdi>، لكن المريضة عمرها <bdi>25</bdi> سنة فلازم نحافظ على <bdi>fertility</bdi>.",
        "الحل اللي يحفظ <bdi>fertility</bdi> هو <bdi>oral progesterone</bdi> مع <bdi>follow-up</bdi> قريب و<bdi>repeat endometrial biopsy</bdi> بعدين.",
    ],
    "when_changes": [
        "لو المريضة بعمر 50 أو خلصت <bdi>childbearing</bdi>، الجواب يتغير لـ<bdi>hysterectomy</bdi> لأنه العلاج النهائي والمضمون.",
    ],
    "rule": "<bdi>atypical complex hyperplasia</bdi> + شابة تبي <bdi>fertility</bdi> = <bdi>oral progesterone</bdi> مع <bdi>follow-up biopsy</bdi>؛ نفس الحالة بعمر متقدم = <bdi>hysterectomy</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1498": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "علاج <bdi>genital warts</bdi> بالحمل لازم يكون طريقة لا تمتص جهازيًا حتى لا تأثر على الجنين.",
    "clues": [
        ("pregnant", "الحمل يمنع استخدام الأدوية الكيميائية الممتصة جهازيًا"),
        ("large genital warts", "<bdi>wart</bdi> كبيرة تحتاج علاج فعّال وآمن بنفس الوقت"),
    ],
    "why_correct": [
        "بالحمل أهم شي سلامة الجنين، و<bdi>cryotherapy</bdi> طريقة <bdi>physical ablative</bdi> بدون أي امتصاص جهازي، فهي آمنة بأي مرحلة من الحمل.",
        "أغلب العلاجات الكيميائية والمناعية لـ<bdi>warts</bdi> ممنوعة بالحمل، فالطريقة الفيزيائية البسيطة هي الأولى.",
    ],
    "when_changes": [
        "لو كانت الـ<bdi>wart</bdi> كبيرة جدًا أو ما استجابت، الجواب يصير <bdi>electrocautery</bdi> أو استئصال جراحي.",
        "لو المريضة غير حامل، يصير <bdi>podophyllin</bdi> أو <bdi>interferon</bdi> خيارات مطروحة أيضًا.",
    ],
    "rule": "كلمة <bdi>pregnant</bdi> تشيل <bdi>podophyllin</bdi> و<bdi>interferon</bdi> فورًا؛ بين الطرق الفيزيائية الجواب الأبسط والآمن هو <bdi>cryotherapy</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1500": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "السؤال عن أعلى قيمة <bdi>diagnostic</bdi> لتقييم <bdi>thickened endometrium</bdi> مع <bdi>menorrhagia</bdi> بعمر الخطر.",
    "clues": [
        ("menorrhagia", "<bdi>abnormal uterine bleeding</bdi> لمدة طويلة"),
        ("diabetic and hypertensive", "عوامل خطر لـ<bdi>unopposed estrogen</bdi> و<bdi>hyperplasia</bdi>"),
        ("Thickened endometrial lining", "تضخم واضح بالـ<bdi>endometrium</bdi> يستدعي أخذ نسيج"),
    ],
    "why_correct": [
        "عمرها 45 ومعها <bdi>AUB</bdi> لثمانية أشهر، و<bdi>diabetic and hypertensive</bdi> (عوامل خطر <bdi>unopposed estrogen</bdi>)، مع <bdi>endometrium</bdi> سمكه 23 مم.",
        "<bdi>AUB</bdi> بعمر 45 فأكثر مؤشر لأخذ <bdi>endometrial sampling</bdi> للخوف من <bdi>hyperplasia</bdi> أو <bdi>carcinoma</bdi>.",
        "فقط <bdi>endometrial biopsy</bdi> يعطينا <bdi>histology</bdi>، فهو الأعلى قيمة <bdi>diagnostic</bdi>.",
    ],
    "when_changes": [
        "لو كان السؤال عن تحديد انتشار <bdi>cancer</bdi> بعد التشخيص (<bdi>staging</bdi>)، الجواب يصير <bdi>MRI</bdi> أو <bdi>CT</bdi>.",
    ],
    "rule": "«أعلى قيمة <bdi>diagnostic</bdi>» لأي <bdi>endometrial lesion</bdi> يعني أخذ نسيج (<bdi>biopsy</bdi>)؛ التصوير يجي بعدين لـ<bdi>staging</bdi> فقط.",
    "comparison": None,
    "labs": [["Endometrial thickness", "23 mm", "عادة <5 mm بعد سن الأمل"]],
    "guideline_note": None,
},

"AS-1506": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "جرعة <bdi>folic acid</bdi> بالحمل تختلف حسب خطر <bdi>neural tube defect</bdi>، و<bdi>sickle cell disease</bdi> ترفع الحاجة للـ<bdi>folate</bdi>.",
    "clues": [
        ("pregnant", "تحتاج جرعة <bdi>folic acid</bdi> وقائية طول الحمل"),
        ("sickle cell disease", "<bdi>chronic hemolysis</bdi> تستهلك <bdi>folate</bdi> باستمرار فتحتاج جرعة عالية"),
    ],
    "why_correct": [
        "<bdi>sickle cell disease</bdi> تسبب <bdi>chronic hemolysis</bdi> اللي يستهلك <bdi>folate</bdi> باستمرار، فالحامل المصابة تحتاج جرعة <bdi>high dose</bdi> من <bdi>folic acid</bdi> طول الحمل مو الجرعة العادية (0.4 mg).",
        "من بين الخيارات المعطاة، 2.4 mg هي أعلى جرعة متوفرة، فهي الجواب رغم إن الجرعة النظرية العالية بالكتب تقارب 4-5 mg.",
    ],
    "when_changes": [
        "لو كانت الجرعة العالية الحقيقية (4-5 mg) من بين الخيارات، تكون هي الجواب الأدق.",
        "لو المريضة بدون عوامل خطر إضافية، الجرعة العادية 0.4 mg تكفي.",
    ],
    "rule": "إذا السؤال عن <bdi>folic acid</bdi> بوجود <bdi>sickle cell disease</bdi> أو خطر <bdi>NTD</bdi> عالي، اختار أعلى جرعة <bdi>high dose</bdi> متوفرة بين الخيارات.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1534": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "<bdi>irregular menstrual cycle</bdi> بوجود <bdi>obesity</bdi> والنتائج لسه معلّقة، الخطوة الأولى دايمًا تغيير نمط الحياة.",
    "clues": [
        ("irregular menstrual cycle", "خلل بالـ<bdi>ovulation</bdi> محتمل مثل <bdi>PCOS</bdi>"),
        ("obese and BMI 31", "<bdi>obesity</bdi> سبب شائع لخلل <bdi>ovulation</bdi>"),
    ],
    "why_correct": [
        "مريضة <bdi>obese</bdi> (<bdi>BMI 31</bdi>) مع <bdi>irregular cycle</bdi> والفحوصات لسه معلّقة، السبب الأرجح خلل <bdi>ovulation</bdi> مرتبط بالوزن مثل <bdi>PCOS</bdi>.",
        "<bdi>lifestyle modification</bdi> (نظام غذائي ورياضة) هي الخطوة الأولى لكل هالحالات، حتى قبل تأكيد التشخيص، لأن نزول الوزن ولو قليل يرجّع <bdi>ovulation</bdi>.",
    ],
    "when_changes": [
        "لو تأكد تشخيص <bdi>PCOS</bdi> وما تبي حمل قريب، الجواب يصير <bdi>OCP</bdi> لضبط الدورة.",
        "لو تبي حمل، الجواب يصير تحريض <bdi>ovulation</bdi> بـ<bdi>clomiphene</bdi> أو <bdi>letrozole</bdi>.",
    ],
    "rule": "«فحوصات لسه معلّقة» + <bdi>obesity</bdi> يعني نبدأ بـ<bdi>lifestyle modification</bdi>؛ <bdi>OCP</bdi> يجي بعد تأكيد التشخيص.",
    "comparison": None,
    "labs": [["BMI", "31", "18.5-24.9"]],
    "guideline_note": None,
},

"AS-1549": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "متابعة <bdi>bhCG</bdi> بعد <bdi>methotrexate</bdi> لـ<bdi>ectopic pregnancy</bdi> تعتمد على مقارنة يوم 4 مع يوم 7.",
    "clues": [
        ("bhCG", "متابعة الاستجابة لـ<bdi>methotrexate</bdi> حسب نسبة النزول"),
    ],
    "why_correct": [
        "المقارنة الحاسمة بعد <bdi>methotrexate</bdi> هي بين يوم 4 ويوم 7: هنا نزل من 1000 إلى 800، يعني نزول 20% (أكثر من 15%)، واستمر النزول لحد 500 بيوم 14.",
        "هذا نزول ناجح، فالخطوة التالية تكرار <bdi>bhCG</bdi> أسبوعيًا لحد ما يصير غير مكتشف.",
    ],
    "when_changes": [
        "لو كان النزول من يوم 4 ليوم 7 أقل من 15% أو حصل <bdi>plateau</bdi>، الجواب يصير جرعة ثانية من <bdi>methotrexate</bdi>.",
        "لو ارتفع <bdi>bhCG</bdi> بين يوم 4 و7 أو صار عدم استقرار، الجواب يصير تدخل جراحي فوري.",
    ],
    "rule": "بعد جرعة <bdi>methotrexate</bdi> الواحدة، تجاهل يوم 1 وركّز على التغيّر بين يوم 4 ويوم 7 لتحديد الخطوة التالية.",
    "comparison": {"headers": ["اليوم", "القيمة"], "rows": [["Day 1", "1200 mIU/mL"], ["Day 4", "1000 mIU/mL"], ["Day 7", "800 mIU/mL"], ["Day 14", "500 mIU/mL"]]},
    "labs": None,
    "guideline_note": None,
},

"AS-1560": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "السؤال عن أشيع سبب لـ<bdi>DIC</bdi> بالحمل المصاحب بنزيف غير متحكم فيه.",
    "clues": [
        ("uncontrolled bleeding", "نزيف شديد يستهلك عوامل التخثر"),
        ("DIC", "اعتلال تخثر استهلاكي يحتاج سبب يحرره"),
    ],
    "why_correct": [
        "<bdi>placental abruption</bdi> أشيع سبب لـ<bdi>DIC</bdi> بالحمل، لأن تجمع الدم خلف المشيمة يحرر <bdi>tissue factor</bdi> بالدورة الدموية للأم، فيستهلك عوامل التخثر والصفائح ويسبب نزيف غير متحكم فيه.",
        "الخطر يرتفع مع <bdi>abruption</bdi> الشديد أو المخفي ووفاة الجنين.",
    ],
    "when_changes": [
        "لو كان هناك انهيار مفاجئ مع نقص أكسجين وقت الولادة، الجواب يصير <bdi>amniotic fluid embolism</bdi>.",
        "لو كان النزيف غير مؤلم من الجزء السفلي للرحم، الجواب يصير <bdi>placenta previa</bdi> بدون <bdi>DIC</bdi> عادة.",
    ],
    "rule": "«حمل + <bdi>DIC</bdi>» الجواب الافتراضي <bdi>placental abruption</bdi> إلا لو كان هناك انهيار مفاجئ مع نقص أكسجين فيصير <bdi>amniotic fluid embolism</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1565": {
    "correct_letter": "C",
    "self_judged": True,
    "idea": "<bdi>leiomyoma</bdi> كبير مع <bdi>menorrhagia</bdi> شديد وفقر دم حاد، السؤال عن أولى خطوة قبل علاج الفايبرويد نفسه.",
    "clues": [
        ("large leiomyoma", "<bdi>fibroid</bdi> كبير يسبب نزيف شديد"),
        ("Hb is 70", "فقر دم شديد يهدد استقرار المريضة قبل أي علاج آخر"),
    ],
    "why_correct": [
        "<bdi>Hb</bdi> منخفض جدًا (70) يعني فقر دم شديد يحتاج تصحيح فوري (نقل دم و/أو حديد) قبل التفكير بعلاج الفايبرويد نفسه.",
        "علاج سبب النزيف (<bdi>fibroid</bdi>) يجي بالخطوة التالية بعد استقرار المريضة، سواء دوائي أو جراحي.",
    ],
    "when_changes": [
        "لو لم يذكر فقر دم شديد بالسؤال، الجواب يصير علاج طبي أولي مثل <bdi>OCP</bdi> قبل الجراحة.",
        "لو الفايبرويد كبير جدًا (>7 سم) أو فشل العلاج الطبي، الجواب يصير جراحة (<bdi>myomectomy</bdi>).",
    ],
    "rule": "لما يذكر السؤال <bdi>Hb</bdi> منخفض جدًا مع <bdi>fibroid</bdi>، تصحيح فقر الدم يسبق أي علاج آخر للفايبرويد.",
    "comparison": None,
    "labs": [["Hb", "70 g/L", "120-150 g/L"]],
    "guideline_note": "المصدر لم يحدد جوابًا مؤكدًا لهذا السؤال، لكن سؤال مشابه بنفس السيناريو كان جوابه المؤكد «تصحيح فقر الدم».",
},

"AS-1566": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "نفس سيناريو <bdi>fibroid</bdi> و<bdi>menorrhagia</bdi> بدون خيار تصحيح فقر الدم، فالخطوة التالية علاج طبي قبل الإجراءات.",
    "clues": [
        ("large leiomyoma", "<bdi>fibroid</bdi> كبير يسبب نزيف شديد"),
    ],
    "why_correct": [
        "بهذا النسخة ما فيه خيار لتصحيح فقر الدم، فمن بين المطروح يكون <bdi>OCP</bdi> الخطوة التالية لأن النزيف المصاحب للفايبرويد يعالج طبيًا أولًا قبل <bdi>embolization</bdi> أو الجراحة.",
        "<bdi>OCP</bdi> يقلل النزيف الشهري بينما تتم معالجة فقر الدم بطرق أخرى بالتوازي.",
    ],
    "when_changes": [
        "لو كان هناك خيار لتصحيح فقر الدم بنفس السؤال، هو الجواب الأولى (انظر السؤال الشقيق).",
        "لو فشل العلاج الطبي أو كان الفايبرويد كبير جدًا، الجواب يصير جراحة.",
    ],
    "rule": "نفس السيناريو له جوابين: مع خيار تصحيح فقر الدم يُختار هو؛ بدونه يُختار العلاج الطبي (<bdi>OCP</bdi>) قبل أي إجراء.",
    "comparison": None,
    "labs": [["Hb", "70 g/L", "120-150 g/L"]],
    "guideline_note": None,
},

"AS-1568": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "<bdi>post-menopausal bleeding</bdi> لازم تقييمه بأخذ نسيج من <bdi>endometrium</bdi> حتى لو كان فيه <bdi>fibroid</bdi> ثابت لا يتغير.",
    "clues": [
        ("post-menopausal bleeding", "أي نزيف بعد سن الأمل يعتبر خطر حتى يُستثنى"),
        ("the same size and location", "الفايبرويد ثابت لمدة 5 سنوات فهو غير مسؤول عن النزيف الجديد"),
    ],
    "why_correct": [
        "أي <bdi>post-menopausal bleeding</bdi> لازم تقييمه لاستثناء <bdi>endometrial hyperplasia</bdi> أو <bdi>carcinoma</bdi> بأخذ عينة من <bdi>endometrium</bdi>.",
        "الفايبرويد نفس حجمه ومكانه لمدة 5 سنوات، يعني غير محتمل يكون هو مصدر النزيف الجديد؛ لو كان تضخم بعد سن الأمل كان نشك بـ<bdi>sarcoma</bdi>.",
    ],
    "when_changes": [
        "لو كان الفايبرويد تضخم بوضوح بعد سن الأمل، الجواب يتجه نحو الشك بـ<bdi>leiomyosarcoma</bdi> وتصوير إضافي.",
        "لو تأكد التشخيص بعد الـ<bdi>biopsy</bdi> أن السبب حميد، يتابع العلاج حسب النتيجة.",
    ],
    "rule": "«<bdi>post-menopausal bleeding</bdi> = <bdi>endometrium</bdi> حتى يُستثنى» — لا تدع فايبرويد ثابت يصرف نظرك عن أخذ عينة من الرحم.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1572": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "متابعة الجنين الأمثل بالولادة المنخفضة الخطورة هي بالفحص المتقطع لا المستمر.",
    "clues": [
        ("low risk and uncomplicated", "حمل منخفض الخطورة يناسبه متابعة أبسط"),
    ],
    "why_correct": [
        "بما إن الحمل <bdi>low risk</bdi> وغير معقد، الموصى به هو <bdi>intermittent auscultation</bdi> لنبض الجنين، وهو آمن بنفس درجة <bdi>continuous CTG</bdi> للجنين بدون زيادة تدخلات مثل الولادة الجراحية.",
        "هذا الخيار يغطي متابعة الجنين فعلًا، بعكس باقي الخيارات اللي تتحدث عن الأم أو المخاض بشكل عام.",
    ],
    "when_changes": [
        "لو ظهر عامل خطر (<bdi>FGR</bdi>، <bdi>preeclampsia</bdi>، سكري، ولادة قيصرية سابقة)، الجواب يصير <bdi>continuous CTG</bdi>.",
        "لو كان نبض الجنين غير طبيعي بالفحص المتقطع، نتحول فورًا لـ<bdi>continuous CTG</bdi>.",
    ],
    "rule": "حمل <bdi>low risk</bdi> + «أفضل متابعة» = <bdi>intermittent auscultation</bdi>؛ أي عامل خطر يحول الجواب لـ<bdi>continuous CTG</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1577": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "تحديد نوع <bdi>miscarriage</bdi> يحتاج فحص حالة عنق الرحم (<bdi>os</bdi>) مع تصوير يوضح محتوى الرحم.",
    "clues": [
        ("amenorrhea for the last 8 weeks", "حمل مبكر بعمر 8 أسابيع"),
        ("expelling blood and tissue through the vagina", "علامة على <bdi>miscarriage</bdi> قيد الحدوث"),
    ],
    "why_correct": [
        "8 أسابيع من <bdi>amenorrhea</bdi> مع «خروج دم ونسيج» تعني <bdi>miscarriage</bdi> جارٍ، ونوعه يحدد حسب حالة عنق الرحم (مفتوح أو مغلق) وما تبقى بالرحم.",
        "<bdi>pelvic examination</bdi> يقيّم <bdi>cervical os</bdi> وأي نسيج عنده، و<bdi>ultrasound</bdi> يوضح إذا تبقى نسيج أو الرحم فاضي، فمعًا يحددان نوع <bdi>miscarriage</bdi> ويوجهان العلاج.",
    ],
    "when_changes": [
        "لو كان هناك كتلة بعنق الرحم تحتاج تقييم موضعي، يصير <bdi>punch biopsy</bdi> مناسب لتلك الحالة فقط.",
    ],
    "rule": "<bdi>pelvic examination</bdi> هو اللي يخبرنا إذا <bdi>cervical os</bdi> مفتوح أو مغلق، وهذا هو الفارق بين أنواع <bdi>miscarriage</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1588": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "بعمر حمل أقل من 32 أسبوع، <bdi>MgSO4</bdi> يُعطى لحماية دماغ الجنين مو كـ<bdi>tocolytic</bdi>.",
    "clues": [
        ("31 weeks", "عمر حمل أقل من 32 أسبوع، نافذة الحماية العصبية"),
        ("preterm labor", "مخاض مبكر يحتاج قرار علاجي"),
    ],
    "why_correct": [
        "بعمر 31 أسبوع (أقل من 32)، تُعطى <bdi>magnesium sulfate</bdi> للحماية العصبية للجنين (<bdi>fetal neuroprotection</bdi>)، تقلل خطر <bdi>cerebral palsy</bdi> لو ولدت.",
        "باقي الخيارات مجرد <bdi>tocolytics</bdi> وما تعطي حماية لدماغ الجنين، وتأثير <bdi>MgSO4</bdi> كـ<bdi>tocolytic</bdi> ضعيف وغير موصى به لهذا الغرض.",
    ],
    "when_changes": [
        "لو كان من ضمن الخيارات <bdi>corticosteroids</bdi> لنضج الرئة بعمر أقل من 34 أسبوع، تأخذ الأولوية على <bdi>MgSO4</bdi>.",
        "لو العمر 32 أسبوع فأكثر، الحماية العصبية بـ<bdi>MgSO4</bdi> لا تُعطى، ويركز على <bdi>tocolysis</bdi> والـ<bdi>steroids</bdi>.",
    ],
    "rule": "مخاض مبكر أقل من 32 أسبوع = <bdi>MgSO4</bdi> للحماية العصبية؛ لو كان <bdi>corticosteroids</bdi> مطروح أقل من 34 أسبوع فهو الأولوية.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1607": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "علاج <bdi>severe preeclampsia</bdi> بخافض الضغط هدفه حماية الأم من <bdi>stroke</bdi> لا تحسين حالة الجنين.",
    "clues": [
        ("severe preeclampsia", "ارتفاع ضغط شديد يهدد الأم أكثر من الجنين"),
        ("rationale", "السؤال يبي السبب الأساسي من إعطاء الدواء"),
        ("antihypertensive medications", "دواء خافض للضغط موجه للمضاعفات الأمومية"),
    ],
    "why_correct": [
        "بـ<bdi>severe preeclampsia</bdi> يعالج الضغط الشديد لحماية <bdi>mother</bdi>: ارتفاع الضغط غير المتحكم يسبب <bdi>hemorrhagic stroke</bdi>، وهو من أهم أسباب وفاة الأم بهذه الحالة.",
        "خافضات الضغط لا تغيّر مرض المشيمة نفسه، فلا فائدة مؤكدة للجنين منها؛ الولادة هي العلاج الشافي الوحيد.",
    ],
    "when_changes": [
        "لو كان السؤال عن منع التشنجات، الجواب يصير <bdi>magnesium sulfate</bdi>.",
        "لو كان السؤال عن العلاج الشافي النهائي، الجواب يصير الولادة.",
    ],
    "rule": "خافضات الضغط بـ<bdi>preeclampsia</bdi> هدفها حماية دماغ الأم من <bdi>stroke</bdi>، مو علاج الجنين.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1612": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "<bdi>REDV</bdi> بعمر حمل 32 أسبوع فأكثر يعني ولادة، لكن مع تغطية بـ<bdi>steroids</bdi> لأن المريضة لسه مبكرة.",
    "clues": [
        ("33 weeks'", "عمر حمل 32 فأكثر، فترة الولادة عند REDV"),
        ("small for gestational age", "جنين أصغر من الطبيعي، احتمال قصور مشيمي"),
        ("reversed end-diastolic flow", "أشد نتائج Doppler غير طبيعية"),
    ],
    "why_correct": [
        "جنين <bdi>SGA</bdi> مع <bdi>reversed end-diastolic flow (REDV)</bdi> بعمر 33 أسبوع تجاوز الحد (32 أسبوع) اللي تصبح فيه الولادة واجبة، فلا يجوز الانتظار أكثر.",
        "بما إنها لسه مبكرة، تُعطى <bdi>antenatal corticosteroids</bdi> أولًا متى سمح الوقت، وتخطط الولادة فورًا بعدها.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>CTG</bdi> أو <bdi>BPP</bdi> غير طبيعي بالفعل، الجواب يصير ولادة فورية بدون انتظار الـ<bdi>steroids</bdi>.",
        "لو كان الدوبلر طبيعي، الجواب يصير متابعة أسبوعية فقط.",
    ],
    "rule": "<bdi>REDV</bdi> بعمر 32 أسبوع فأكثر = ولادة؛ إذا لسه مبكرة وما فيه ضيق وقت، تُعطى <bdi>steroids</bdi> أولًا.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1613": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "نفس حالة <bdi>REDV</bdi> بعمر 33 أسبوع، لكن هنا الخيار يحدد نافذة الولادة بـ72 ساعة بعد الـ<bdi>steroids</bdi>.",
    "clues": [
        ("33 weeks'", "عمر حمل 32 فأكثر، فترة الولادة عند REDV"),
        ("small for gestational age", "جنين أصغر من الطبيعي"),
        ("reversed enddiastolic flow", "أشد نتائج Doppler غير طبيعية"),
    ],
    "why_correct": [
        "<bdi>REDV</bdi> هي أشد نتيجة Doppler قبل تدهور الجنين، وبعمر 33 أسبوع (≥32) يجب الولادة مو الاستمرار بالمتابعة.",
        "بما إنها لسه مبكرة (<34 أسبوع)، تُعطى <bdi>corticosteroids</bdi> أولًا لتقليل مشاكل تنفس الوليد، وتخطط الولادة فورًا بعدها (خلال 72 ساعة).",
    ],
    "when_changes": [
        "لو كان الـ<bdi>CTG</bdi> أو <bdi>BPP</bdi> غير مطمئن، تصير الولادة فورية بدون انتظار.",
        "لو كان الدوبلر طبيعي، الجواب يصير متابعة أسبوعية فقط.",
    ],
    "rule": "<bdi>REDV</bdi> بعمر ≥32 أسبوع = ولادة قريبة؛ النقاش الوحيد هل تُعطى <bdi>steroids</bdi> أولًا أو تكون الولادة فورية.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1653": {
    "correct_letter": "C",
    "self_judged": True,
    "idea": "تسمية تمزق الأغشية تعتمد على ترتيب الأحداث: هل جاء التمزق قبل بداية التقلصات أو بعدها.",
    "clues": [
        ("41 WEEKS", "عمر حمل بعد الموعد المتوقع (post-term)"),
        ("IN LABOR", "المخاض بدأ فعلًا قبل التمزق"),
        ("GUSH OF FLUID", "علامة تمزق الأغشية"),
    ],
    "why_correct": [
        "المريضة بـ<bdi>41 weeks</bdi> وهي أصلًا «<bdi>in labor</bdi>» (يعني المخاض بدأ)، وبعدها حصل «<bdi>gush of fluid</bdi>» (تمزق الأغشية).",
        "لما يحصل التمزق بعد بداية المخاض، يسمى <bdi>spontaneous rupture of membranes (SROM)</bdi> بغض النظر عن عمر الحمل.",
    ],
    "when_changes": [
        "لو حصل التمزق قبل بداية المخاض بعمر 37 أسبوع فأكثر، يسمى <bdi>PROM</bdi>.",
        "لو حصل التمزق قبل بداية المخاض بعمر أقل من 37 أسبوع، يسمى <bdi>PPROM</bdi>.",
    ],
    "rule": "التمزق بعد بداية التقلصات = <bdi>SROM</bdi> (بأي عمر حمل)؛ التمزق قبل التقلصات يسمى <bdi>PROM</bdi> أو <bdi>PPROM</bdi> حسب عمر الحمل.",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر لم يحدد جوابًا مؤكدًا لهذا السؤال؛ الجواب مبني على القاعدة الموضحة بملاحظة المصدر نفسها (ترتيب التمزق مقابل التقلصات).",
},

"AS-1687": {
    "correct_letter": "B",
    "self_judged": True,
    "idea": "<bdi>ovarian cancer</bdi> مع انتشار واسع جدًا بالبطن يصعب استئصاله بالكامل جراحيًا، فيبدأ العلاج بـ<bdi>chemotherapy</bdi> أولًا.",
    "clues": [
        ("markedly elevated CA-125", "علامة ورم تدعم تشخيص <bdi>ovarian carcinoma</bdi>"),
        ("high-grade epithelial ovarian carcinoma", "نوع عدواني من سرطان المبيض"),
        ("extensive metastatic spread throughout the abdomen", "انتشار واسع يصعب استئصاله بالكامل جراحيًا"),
    ],
    "why_correct": [
        "وجود «<bdi>extensive metastatic spread throughout the abdomen</bdi>» يعني المرض غير قابل للاستئصال الكامل بسهولة (<bdi>unresectable</bdi>)، فالخيار الأنسب هو بدء <bdi>chemotherapy</bdi> (<bdi>neoadjuvant</bdi>) أولًا ثم إعادة تقييم إمكانية الجراحة.",
        "هذا يسمى <bdi>interval debulking surgery</bdi> بعد استجابة المرض للعلاج الكيميائي، ويقلل مخاطر جراحة كبرى بمرض منتشر جدًا.",
    ],
    "when_changes": [
        "لو كان المرض يبدو قابل للاستئصال الكامل والمريضة مستقرة صحيًا، الجواب يصير جراحة استئصال أولية (<bdi>primary debulking</bdi>) ثم علاج كيميائي.",
        "لو كانت المريضة غير مؤهلة لأي علاج فعّال، الجواب يصير رعاية تلطيفية فقط.",
    ],
    "rule": "كلمات مثل «<bdi>unresectable</bdi>» أو «<bdi>extensive spread</bdi>» تحول الجواب نحو <bdi>chemotherapy</bdi> أولًا؛ كلمة «<bdi>advanced</bdi>» وحدها عادة تبقي الجواب جراحة أولًا.",
    "comparison": None,
    "labs": [["CA-125", "markedly elevated", "<35 U/mL"]],
    "guideline_note": "المصدر لم يحدد جوابًا مؤكدًا لهذا السؤال؛ تم الاختيار حسب المنطق الإكلينيكي الموضح بملاحظة المصدر نفسه (كلمة extensive spread تدفع نحو العلاج الكيميائي أولًا).",
},

"AS-1687B": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>advanced epithelial ovarian cancer</bdi> بدون ذكر عدم قابلية الاستئصال، فالعلاج الأساسي جراحة استئصال كامل ثم علاج كيميائي.",
    "clues": [
        ("solid irregular fixed pelvic mass", "كتلة حوضية مشبوهة بالسرطان"),
        ("multilocular ovarian mass", "كتلة مبيضية معقدة"),
        ("advanced epithelial ovarian cancer", "تشخيص مؤكد بـ<bdi>staging</bdi> و<bdi>histology</bdi>"),
    ],
    "why_correct": [
        "تشخيصها <bdi>advanced epithelial ovarian cancer</bdi> مؤكد بـ<bdi>staging</bdi> و<bdi>histology</bdi>، بدون أي ذكر لعدم قابلية الاستئصال أو عدم لياقتها للجراحة.",
        "العلاج الأساسي هو جراحة استئصال شامل (<bdi>cytoreduction</bdi>: رحم، مبايض، <bdi>omentum</bdi>) ثم علاج كيميائي مساعد، وكمية ما يتبقى من المرض بعد الجراحة هي أهم عامل للبقيا.",
    ],
    "when_changes": [
        "لو كان المرض واسع الانتشار بشكل يصعب استئصاله بالكامل، الجواب يصير علاج كيميائي أولًا (<bdi>neoadjuvant</bdi>).",
        "لو كانت المريضة غير مؤهلة لأي علاج، الجواب يصير رعاية تلطيفية.",
    ],
    "rule": "جراحة استئصال ثم علاج كيميائي هما الثنائي المعياري بـ<bdi>advanced ovarian cancer</bdi> القابل للاستئصال؛ العلاج الكيميائي أولًا محجوز لحالات غير قابلة للاستئصال أو غير مؤهلة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1699": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "حجم الكتلة الـ<bdi>ectopic</bdi> هو العامل الحاسم بين العلاج الدوائي والجراحي.",
    "clues": [
        ("ectopic pregnancy", "حمل خارج الرحم يحتاج قرار علاج"),
        ("4 cm", "يفشل شرط حجم <bdi>methotrexate</bdi> (أقل من 4 سم)"),
    ],
    "why_correct": [
        "كتلة <bdi>ectopic</bdi> بحجم 4 سم تفشل شرط الحجم اللازم لـ<bdi>methotrexate</bdi> (يجب أقل من 4 سم)، وكل شروط <bdi>methotrexate</bdi> لازم تتحقق كلها.",
        "لذلك الخيار المناسب هو العلاج الجراحي، عادة بـ<bdi>laparoscopic salpingectomy</bdi> أو <bdi>salpingostomy</bdi>.",
    ],
    "when_changes": [
        "لو كانت الكتلة أقل من 4 سم مع استقرار المريضة وعدم نشاط قلبي للجنين و<bdi>bhCG</bdi> أقل من 5000، الجواب يصير <bdi>methotrexate</bdi>.",
    ],
    "rule": "فشل أي شرط من شروط <bdi>methotrexate</bdi> (الحجم، <bdi>hCG</bdi>، النشاط القلبي، الاستقرار) يكفي لتحويل الجواب للعلاج الجراحي.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1700": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "<bdi>nodularity</bdi> على <bdi>uterosacral ligament</bdi> علامة فحص كلاسيكية لـ<bdi>endometriosis</bdi>.",
    "clues": [
        ("Dysmenorrhea", "ألم دورة شهرية شديد، من أعراض <bdi>endometriosis</bdi>"),
        ("nodularity on uterosacral ligament", "علامة فحص مباشرة لـ<bdi>endometriosis</bdi> العميق"),
    ],
    "why_correct": [
        "<bdi>dysmenorrhea</bdi> مع <bdi>nodularity</bdi> على <bdi>uterosacral ligaments</bdi> هي علامة الفحص الكلاسيكية لـ<bdi>endometriosis</bdi> (ارتشاح عميق بـ<bdi>pouch of Douglas</bdi>).",
        "النسخة الكاملة تضيف رحم ثابت متجه للخلف وعدم خصوبة، وهذا يكمل صورة الـ3Ds مع <bdi>subfertility</bdi>.",
    ],
    "when_changes": [
        "لو كان الرحم متضخم ومنتشر الألم مع نزيف غزير بسيدة متعددة الولادة، الجواب يصير <bdi>adenomyosis</bdi>.",
        "لو كان الرحم متضخم وغير منتظم مع نزيف غزير، الجواب يصير <bdi>leiomyoma</bdi>.",
    ],
    "rule": "<bdi>nodularity</bdi> على <bdi>uterosacral ligament</bdi> تشير لمرض خارج الرحم (<bdi>endometriosis</bdi>)؛ تضخم الرحم نفسه يشير لـ<bdi>adenomyosis</bdi> أو <bdi>fibroids</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1703": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "من بين الـ<bdi>tocolytics</bdi>، واحد فقط له تأثير مباشر على <bdi>ductus arteriosus</bdi> الجنيني.",
    "clues": [
        ("preterm labor", "حالة تحتاج <bdi>tocolytic</bdi>"),
        ("tocolytics", "نوع الدواء المطلوب تحديد تأثيره"),
        ("patent ductus arteriosus", "تأثير جنيني محدد مرتبط بالبروستاغلاندين"),
    ],
    "why_correct": [
        "<bdi>indomethacin</bdi> من فئة <bdi>NSAID</bdi> (مثبط <bdi>prostaglandin synthesis</bdi>)، والبروستاغلاندين هو ما يحافظ على فتح <bdi>ductus arteriosus</bdi> الجنيني.",
        "لذلك <bdi>indomethacin</bdi> يسبب تضيق مبكر للـ<bdi>ductus</bdi> داخل الرحم مع احتمال <bdi>pulmonary hypertension</bdi> للجنين، ويسبب أيضًا <bdi>oligohydramnios</bdi>، فيُحدد استخدامه لفترة قصيرة قبل 32 أسبوع.",
    ],
    "when_changes": [
        "لو كان السؤال عن أكثر آثار جانبية أمومية (تسرع قلب، وذمة رئوية)، الجواب يصير <bdi>ritodrine</bdi>.",
        "لو كان السؤال عن أقل آثار جانبية، الجواب يصير <bdi>atosiban</bdi>.",
    ],
    "rule": "<bdi>indomethacin</bdi> يغلق <bdi>ductus arteriosus</bdi> بالرحم (ويُستخدم أيضًا لإغلاق <bdi>PDA</bdi> بالمواليد)؛ بروستاغلاندين E1 يفتحه.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1725": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "توقيت انقسام الجنين أحادي الزيجوت يحدد نوع الأغشية المشتركة بين التوأمين.",
    "clues": [
        ("Monochorionic Monoamniotic", "كيس مشيمة واحد وكيس سلى واحد مشترك"),
    ],
    "why_correct": [
        "بالتوائم أحادية الزيجوت، نوع الأغشية يعتمد على وقت انقسام الجنين بعد الإخصاب.",
        "بين يوم 9 و12، يكون <bdi>chorion</bdi> و<bdi>amnion</bdi> كلاهما تكوّن مسبقًا، فيتشارك التوأمان بمشيمة واحدة وكيس سلى واحد: <bdi>monochorionic monoamniotic</bdi>.",
    ],
    "when_changes": [
        "لو كان الانقسام قبل 72 ساعة، يصير كل جنين له مشيمته وكيسه الخاص (<bdi>dichorionic diamniotic</bdi>).",
        "لو كان الانقسام بعد يوم 12، يصير التوأمان <bdi>conjoined twins</bdi>.",
    ],
    "rule": "كل ما تأخر الانقسام، كل ما زاد التشارك: المشيمة أولًا، ثم كيس السلى، ثم الجسم نفسه.",
    "comparison": {"headers": ["وقت الانقسام", "النوع"], "rows": [["0-72 hours", "Dichorionic Diamniotic"], ["4-8 days", "Monochorionic Diamniotic"], ["9-12 days", "Monochorionic Monoamniotic"], [">12 days", "Conjoined twins"]]},
    "labs": None,
    "guideline_note": None,
},

"AS-1735": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "أم <bdi>Rh negative</bdi> غير محسسة (بدون أجسام مضادة) تحتاج وقاية روتينية بـ<bdi>anti-D</bdi>، مو مراقبة.",
    "clues": [
        ("14 weeks", "عمر حمل مبكر، لا حاجة لجرعة إضافية بدون سبب محدد"),
        ("O negative", "أم <bdi>Rh negative</bdi> مع أب <bdi>Rh positive</bdi> يعني خطر تحسس"),
        ("no anti-D antibodies", "غير محسسة حاليًا، تحتاج وقاية مو مراقبة"),
    ],
    "why_correct": [
        "هي <bdi>Rh negative</bdi> وشريكها <bdi>Rh positive</bdi>، والحمل الحالي «بدون <bdi>anti-D antibodies</bdi>»، يعني غير محسسة (<bdi>unsensitized</bdi>) وتحتاج وقاية مو مراقبة.",
        "الوقاية الروتينية هي <bdi>anti-D immunoglobulin</bdi> بالأسبوع 28، ثم جرعة أخرى خلال 72 ساعة بعد الولادة لو كان الطفل <bdi>Rh positive</bdi>.",
    ],
    "when_changes": [
        "لو حصل حدث محسس (نزيف، إجهاض، رضة بطنية، إجراء تداخلي)، تُعطى <bdi>anti-D</bdi> فورًا بذلك الوقت حتى لو قبل 28 أسبوع.",
        "لو كانت محسسة فعلًا (أجسام مضادة موجودة)، <bdi>anti-D</bdi> لا تفيد، والمتابعة تصير بـ<bdi>MCA Doppler</bdi>.",
    ],
    "rule": "<bdi>anti-D</bdi> تمنع التحسس؛ لما توجد أجسام مضادة فعلًا، نتحول للمراقبة (<bdi>titers</bdi>، <bdi>MCA Doppler</bdi>) أبدًا لا للوقاية.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1736": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "عند الجراحة لـ<bdi>tubal ectopic</bdi>، الإجراء المعياري استئصال الأنبوب المصاب فقط.",
    "clues": [
        ("4 cm ectopic pregnancy", "حجم يفشل شرط <bdi>methotrexate</bdi>، يحتاج جراحة"),
        ("scheduled for surgery", "القرار الجراحي محسوم، السؤال عن نوع الإجراء"),
    ],
    "why_correct": [
        "كتلة <bdi>ectopic</bdi> بحجم 4 سم تفشل شرط حجم <bdi>methotrexate</bdi> (أقل من 4 سم)، فالعلاج جراحي، والإجراء المعياري هو <bdi>salpingectomy</bdi> للأنبوب المصاب (الأيمن).",
        "<bdi>salpingectomy</bdi> تزيل كل الـ<bdi>trophoblast</bdi> وتحتاج فقط <bdi>bhCG</bdi> واحد بعد العملية للتأكد من النزول.",
    ],
    "when_changes": [
        "لو كان الأنبوب المقابل مصاب أيضًا (مثل <bdi>hydrosalpinx</bdi> قبل <bdi>IVF</bdi>)، يصير استئصال الأنبوبين مبرر.",
        "لو كانت تبي حفظ الخصوبة والأنبوب المقابل سليم، يُفكر بـ<bdi>salpingostomy</bdi> مع متابعة <bdi>bhCG</bdi> متكررة.",
    ],
    "rule": "استئصال الأنبوبين معًا فقط لو الأنبوب المقابل مريض أيضًا؛ غير ذلك يُستأصل الأنبوب المصاب فقط.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1744": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "تاريخ ولادتين مبكرتين سابقتين مع نزيف حالي يوجه لإعطاء <bdi>progesterone</bdi> لحماية الحمل الحالي.",
    "clues": [
        ("history of 2 preterm delivery", "أعلى فئة خطر لتكرار <bdi>preterm birth</bdi>"),
    ],
    "why_correct": [
        "تاريخ ولادتين مبكرتين سابقتين يضعها بأعلى فئة خطر لتكرار <bdi>spontaneous preterm birth</bdi>، و<bdi>progesterone</bdi> هو الدواء المستخدم لتقليل هذا الخطر.",
        "<bdi>progesterone</bdi> أيضًا يدعم استمرار الحمل عند حدوث <bdi>vaginal spotting</bdi>، وهو هرمون الحفاظ على الحمل.",
    ],
    "when_changes": [
        "لو كان المخاض المبكر فعليًا قد بدأ (أقل من 34 أسبوع)، تتغير الخطة لـ<bdi>steroids</bdi> و<bdi>tocolysis</bdi> و<bdi>MgSO4</bdi> لو أقل من 32 أسبوع.",
    ],
    "rule": "<bdi>progesterone</bdi> يمنع تكرار الولادة المبكرة بالمرأة عالية الخطر؛ هو ليس <bdi>tocolytic</bdi> ولا يوقف مخاض فعلي قائم.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1747": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "<bdi>molar pregnancy</bdi> يُعالج بالإفراغ بالمص (<bdi>suction evacuation</bdi>) لا بالكحت الحاد.",
    "clues": [
        ("fundal height is consistent with 19 weeks", "رحم أكبر من عمر الحمل الحقيقي، علامة مهمة لـ<bdi>molar pregnancy</bdi>"),
        ("molar pregnancy", "تشخيص بالموجات الصوتية"),
    ],
    "why_correct": [
        "نزيف بالثلث الأول مع رحم أكبر من عمر الحمل (19 أسبوع بدل 12) وموجات صوتية متوافقة مع <bdi>molar pregnancy</bdi> تشخص <bdi>hydatidiform mole</bdi>.",
        "العلاج هو <bdi>suction evacuation</bdi> لأنه يُفرّغ الرحم الكبير الطري بالكامل مع أقل خطر ثقب أو نزيف، متبوعًا بمتابعة <bdi>bhCG</bdi> متسلسلة، ويحفظ الخصوبة بعمر 30 سنة.",
    ],
    "when_changes": [
        "لو حصل <bdi>plateau</bdi> أو ارتفاع بـ<bdi>bhCG</bdi> بعد الإفراغ، الجواب يصير علاج كيميائي (<bdi>methotrexate</bdi>) لـ<bdi>GTN</bdi>.",
        "لو اكتملت الخصوبة ورفضت المتابعة، <bdi>hysterectomy</bdi> خيار بديل.",
    ],
    "rule": "<bdi>molar pregnancy</bdi> يُفرّغ بـ<bdi>suction</bdi> مو كحت حاد؛ العلاج الكيميائي يدخل فقط لو فشل نزول <bdi>bhCG</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1753": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "ارتفاع ضغط شديد مفاجئ بالثلث الثالث يُعامل كـ<bdi>preeclampsia</bdi> حتى بدون بروتين بالبول أو أعراض.",
    "clues": [
        ("3rd trimester", "عمر حمل متأخر"),
        ("previous BP f/u were normal", "لا يوجد ارتفاع ضغط مسبق، يستثني <bdi>chronic HTN</bdi>"),
        ("160/100", "ضغط بمستوى شديد (severe-range)"),
        ("No protein in urine", "لا بروتين ظاهر، لكن الضغط الشديد كافٍ"),
    ],
    "why_correct": [
        "ضغط «160/100» جديد بالثلث الثالث بعد أن كانت كل القراءات السابقة «120/70» هو قراءة بمستوى شديد (<bdi>severe-range</bdi>)، وهذا السؤال يعامل الارتفاع الشديد المفاجئ كـ<bdi>preeclampsia</bdi>.",
        "ارتفاع الضغط بمستوى شديد (≥160/110) بالحمل يُدار بنفس طريقة <bdi>preeclampsia with severe features</bdi>، وهذا هو منطق الإجابة.",
    ],
    "when_changes": [
        "لو كان الضغط أقل من المستوى الشديد (مثل 145/90) بدون بروتين أو أعراض، الجواب يصير <bdi>gestational HTN</bdi>.",
        "لو حصلت تشنجات، الجواب يصير <bdi>eclampsia</bdi>.",
    ],
    "rule": "ضغط بمستوى شديد (≥160/110) بالحمل يُدار كـ<bdi>preeclampsia with severe features</bdi> حتى لو غاب البروتين أو الأعراض.",
    "comparison": None,
    "labs": [["Blood pressure", "160/100 mmHg", "<140/90 mmHg"]],
    "guideline_note": "تصنيف هذه الحالة مثار نقاش طبي (ارتفاع ضغط شديد بدون بروتين أو أعراض قد يصنف <bdi>severe gestational HTN</bdi> بدل <bdi>preeclampsia</bdi>)، لكن إجابة المصدر محفوظة هنا.",
},

"AS-1754": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "ارتفاع ضغط جديد بدون بروتين أو أعراض أو خلل بالفحوصات المخبرية يُصنف <bdi>gestational hypertension</bdi>.",
    "clues": [
        ("39 weeks' gestation", "عمر حمل متأخر، بعد 20 أسبوع"),
        ("Urinalysis was negative for protein", "يستثني <bdi>preeclampsia</bdi>"),
        ("160/90", "ضغط جديد بمستوى شديد بالسيستولي"),
        ("Blood pressure 120/70", "كل الزيارات السابقة طبيعية، يستثني <bdi>chronic HTN</bdi>"),
    ],
    "why_correct": [
        "ضغط جديد (160/90) بعد 20 أسبوع (وكل زياراتها السابقة كانت 120/70)، مع بروتين بول سلبي، وبدون صداع أو اضطراب رؤية أو ألم بطن، وصفائح وإنزيمات كبد طبيعية.",
        "ارتفاع ضغط جديد بعد 20 أسبوع بدون بروتين أو خلل بالأعضاء يصنف <bdi>gestational hypertension</bdi>؛ ارتفاع السيستولي الشديد يجعلها <bdi>severe gestational HTN</bdi> مو <bdi>preeclampsia</bdi>.",
    ],
    "when_changes": [
        "لو ظهر بروتين بالبول أو اضطراب بالصفائح أو إنزيمات الكبد، الجواب يصير <bdi>preeclampsia</bdi>.",
        "لو كان الضغط مرتفع قبل 20 أسبوع، الجواب يصير <bdi>chronic hypertension</bdi>.",
    ],
    "rule": "صفائح وإنزيمات كبد طبيعية مع بروتين سلبي تبقي التصنيف <bdi>gestational hypertension</bdi> حتى لو وصل السيستولي 160.",
    "comparison": None,
    "labs": [["Blood pressure", "160/90 mmHg", "<140/90 mmHg"], ["Platelets", "165 x10^9/L", "150-400 x10^9/L"], ["ALT", "12 IU/L", "5-40 IU/L"], ["AST", "22 IU/L", "12-40 IU/L"], ["HCT", "0.34", "0.37-0.48"]],
    "guideline_note": None,
},

"AS-1767": {
    "correct_letter": "C",
    "self_judged": True,
    "idea": "<bdi>secondary amenorrhea</bdi> بعد إجراء رحمي حديث (<bdi>D&C</bdi>) يوجه الشك نحو التصاقات داخل الرحم.",
    "clues": [
        ("secondary amenorrhea", "توقف الدورة بعد وجودها سابقًا"),
        ("D&C 3 month ago", "إجراء رحمي حديث يرفع خطر التصاقات"),
    ],
    "why_correct": [
        "<bdi>D&amp;C</bdi> قبل 3 أشهر يرفع خطر <bdi>intrauterine adhesions (Asherman syndrome)</bdi>، وهذا السبب الأكثر احتمالًا لـ<bdi>secondary amenorrhea</bdi> بعد إجراء رحمي حديث.",
        "<bdi>hysteroscopy</bdi> هو الفحص المباشر الذي يثبت وجود التصاقات داخل الرحم ويسمح بعلاجها.",
    ],
    "when_changes": [
        "لو كان هناك <bdi>galactorrhea</bdi> أو صداع واضطراب رؤية، الجواب يصير <bdi>MRI brain</bdi> للشك بـ<bdi>prolactinoma</bdi>.",
        "لو لم يكن هناك إجراء رحمي حديث، الخطوة الأولى دايمًا اختبار حمل ثم <bdi>TSH</bdi> و<bdi>prolactin</bdi> و<bdi>FSH</bdi>.",
    ],
    "rule": "إجراء رحمي حديث (<bdi>D&amp;C</bdi>) مع <bdi>secondary amenorrhea</bdi> وهرمونات طبيعية يوجه نحو <bdi>hysteroscopy</bdi> لاستثناء <bdi>Asherman syndrome</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر لم يحدد جوابًا مؤكدًا لهذا السؤال؛ الاختيار مبني على القاعدة الإكلينيكية الموضحة بملاحظة المصدر نفسها (تاريخ إجراء رحمي حديث يوجه نحو hysteroscopy).",
},

"AS-1773": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "حمل بوجود <bdi>IUD</bdi> مع رحم فاضي وتجمع سوائل كبير وألم شديد يعني <bdi>ectopic pregnancy</bdi> متمزق.",
    "clues": [
        ("severe generalized abdominal pain", "ألم منتشر شديد يوجه لتمزق داخل البطن"),
        ("intrauterine contraceptive device", "عامل خطر مهم لـ<bdi>ectopic pregnancy</bdi>"),
        ("positive", "حمل مؤكد"),
        ("Fluid collection of approximately 13 x 15 cm", "تجمع دم كبير داخل البطن (<bdi>hemoperitoneum</bdi>)"),
        ("No identified gestational sac", "لا كيس حمل بالرحم، يوجه لحمل خارج الرحم"),
    ],
    "why_correct": [
        "اختبار حمل إيجابي مع عدم وجود كيس حمل بالرحم يعني <bdi>ectopic pregnancy</bdi> حتى يُستثنى، وحدوث الحمل مع وجود <bdi>IUD</bdi> يرفع احتمالية كونه خارج الرحم.",
        "الألم المنتشر الشديد مع تجمع سوائل كبير (13×15 سم، يعني <bdi>hemoperitoneum</bdi>) يدل على أن الحمل الخارجي قد تمزق.",
    ],
    "when_changes": [
        "لو كان الألم خفيف وموضعي مع كتلة بالملحق وبدون سوائل كبيرة، الجواب يصير حمل خارج الرحم سليم (<bdi>intact</bdi>).",
    ],
    "rule": "ألم شديد منتشر مع تجمع سوائل كبير بالبطن يحوّل حمل خارج الرحم من سليم إلى متمزق، ويحتم الجراحة فورًا.",
    "comparison": None,
    "labs": [["Fluid collection", "13 x 15 cm", "لا يوجد طبيعيًا"]],
    "guideline_note": None,
},

"AS-1775": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "لما يكون الفحص السريري غير حاسم لـ<bdi>PPROM</bdi>، يوجد بروتين محدد موجود بالسائل الأمنيوسي يؤكد التمزق.",
    "clues": [
        ("sudden, watery vaginal discharge", "علامة تمزق الأغشية"),
        ("preterm prelabor rupture of membranes (PPROM)", "التشخيص المشتبه به"),
        ("proteins in the vaginal secretions", "اختبار كيميائي مساعد للتشخيص"),
    ],
    "why_correct": [
        "لما نتائج الفحص بالمنظار (تجمع سائل، <bdi>nitrazine</bdi>، <bdi>ferning</bdi>) غير حاسمة، <bdi>PAMG-1</bdi> بروتين موجود بكثرة بالسائل الأمنيوسي وبكمية ضئيلة جدًا بإفرازات المهبل، فوجوده بالإفرازات يدعم تمزق الأغشية.",
        "هو أساس اختبار سريع تجاري يستخدم لتأكيد <bdi>PPROM</bdi> المشتبه به، كحال هذه المريضة بعمر 24 أسبوع مع إفرازات مائية مفاجئة.",
    ],
    "when_changes": [
        "لو كان الفحص بالمنظار واضحًا (تجمع سائل ظاهر مع <bdi>nitrazine</bdi> و<bdi>ferning</bdi> إيجابيين)، لا حاجة لاختبار بروتين إضافي.",
    ],
    "rule": "عند عدم وضوح تمزق الأغشية بالفحص التقليدي، <bdi>PAMG-1</bdi> هو بروتين السائل الأمنيوسي المحدد لتأكيد التشخيص.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1777": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "<bdi>fibroid</bdi> مع نزيف غزير بمريضة لا تبي حمل قريب يُعالج طبيًا أولًا بـ<bdi>OCP</bdi>.",
    "clues": [
        ("leiomyoma", "سبب النزيف"),
        ("heavy menstruation", "عرض يحتاج علاج"),
        ("doesn't want children soon", "لا حاجة لجراحة حافظة للخصوبة فورًا، ولا لإنهاء الخصوبة نهائيًا"),
    ],
    "why_correct": [
        "<bdi>fibroid</bdi> مع نزيف غزير يُعالج طبيًا أولًا قبل الجراحة إلا لو كان كبير جدًا أو فشل العلاج الطبي.",
        "بما إنها «لا تبي حمل قريب» (مو الآن، ومستقبلًا ممكن تبي)، <bdi>OCP</bdi> يناسب لأنه يقلل النزيف ويعطي وسيلة منع حمل، ويحفظ الخصوبة المستقبلية.",
    ],
    "when_changes": [
        "لو كان <bdi>Hb</bdi> منخفض جدًا بالسؤال، يصير تصحيح فقر الدم الأولوية قبل أي علاج آخر.",
        "لو كان الفايبرويد كبير جدًا أو فشل العلاج الطبي، الجواب يصير جراحة.",
    ],
    "rule": "نزيف غزير بسبب فايبرويد يُعالج طبيًا أولًا (<bdi>OCP</bdi>)؛ الجراحة تجي بعد فشل العلاج الطبي أو حجم كبير جدًا.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1778": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "ألم بالخاصرة مع حمى ورجفة وبول قيحي بالحمل يشخص <bdi>pyelonephritis</bdi>.",
    "clues": [
        ("right flank radiating to her groin", "ألم خاصرة يمتد للفخذ، نمط ألم المسالك البولية العلوية"),
        ("rigors and chills", "علامة عدوى جهازية شديدة"),
        ("Numerous pus cells", "دليل مباشر على عدوى بولية"),
    ],
    "why_correct": [
        "ألم خاصرة يمينًا يمتد للفخذ مع رجفة وحمى وكثرة خلايا القيح بالبول هو عدوى مسالك بولية علوية: <bdi>pyelonephritis</bdi>.",
        "الحمل يهيئ لها بسبب توسع الحالب المرتبط بالبروجستيرون وركود البول، وتكون أكثر على اليمين لأن الرحم ينحرف لليمين ويضغط على الحالب الأيمن.",
    ],
    "when_changes": [
        "لو كان الألم بطني بالربع الأيمن السفلي بدون بول قيحي أو رجفة، الجواب يصير <bdi>appendicitis</bdi>.",
    ],
    "rule": "ألم خاصرة + حمى ورجفة + بول قيحي بالحمل يعني <bdi>pyelonephritis</bdi>؛ يحتاج دخول للمستشفى ومضادات حيوية وريدية.",
    "comparison": None,
    "labs": [["Urine", "numerous pus cells", "لا يوجد طبيعيًا"]],
    "guideline_note": None,
},

"AS-1781": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>cervical cancer</bdi> بمرحلة 2B يعني غزو <bdi>parametrium</bdi>، فلازم إجراء يزيله.",
    "clues": [
        ("cervical cancer stage 2B", "مرحلة تتضمن غزو الأنسجة المحيطة بعنق الرحم"),
    ],
    "why_correct": [
        "مرحلة <bdi>2B</bdi> تعني غزو <bdi>parametrium</bdi>، ومن بين الخيارات المطروحة، فقط <bdi>radical hysterectomy</bdi> يستأصل الرحم مع <bdi>parametria</bdi> والجزء العلوي من المهبل، عادة مع استئصال العقد اللمفاوية الحوضية.",
        "<bdi>conization</bdi> و<bdi>simple hysterectomy</bdi> كلاهما لا يزيل <bdi>parametrium</bdi>، فهما غير كافيين لهذه المرحلة.",
    ],
    "when_changes": [
        "لو كانت المرحلة IA1 وتبي حمل، الجواب يصير <bdi>conization</bdi>.",
        "لو كانت المرحلة متقدمة أكثر من 2B (غزو جدار الحوض أو أبعد)، الجواب يصير علاج كيميائي إشعاعي متزامن.",
    ],
    "rule": "أي مرحلة تتضمن غزو <bdi>parametrium</bdi> تحتاج إجراء يزيله؛ <bdi>conization</bdi> و<bdi>simple hysterectomy</bdi> محجوزان فقط للمرحلة المبكرة جدًا (<bdi>IA1</bdi>).",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1798": {
    "correct_letter": "D",
    "self_judged": True,
    "idea": "<bdi>missed abortion</bdi> مع حمى يعني إجهاض مصاب بعدوى (<bdi>septic abortion</bdi>)، يحتاج مضاد حيوي مع إفراغ الرحم.",
    "clues": [
        ("Missed abortion", "إجهاض بدون طرد كامل للنسيج"),
        ("Infected Abortus", "دليل مباشر على وجود عدوى"),
        ("Fever", "علامة أساسية على عدوى جهازية"),
    ],
    "why_correct": [
        "وجود <bdi>fever</bdi> مع <bdi>missed abortion</bdi> يحوّل الحالة إلى <bdi>septic abortion</bdi>، وهذا يحتاج مضاد حيوي واسع المجال وريدي مع إفراغ عاجل للرحم (<bdi>abortifacient with antibiotic</bdi>).",
        "لا يجوز الانتظار بالإدارة التحفظية أو الدوائية فقط مع وجود حمى؛ العدوى تحتاج تغطية مضاد حيوي بالتوازي مع إفراغ الرحم.",
    ],
    "when_changes": [
        "لو لم تكن هناك حمى أو عدوى، الجواب يصير إدارة تحفظية أو <bdi>misoprostol</bdi> فقط بدون مضاد حيوي.",
    ],
    "rule": "كلمة <bdi>fever</bdi> مع إجهاض تحوّله لـ<bdi>septic abortion</bdi>: مضاد حيوي إلزامي مع إفراغ الرحم فورًا.",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر لم يحدد جوابًا مؤكدًا لهذا السؤال (الخياران A و B لم يُذكرا بالمصدر)؛ الاختيار مبني على القاعدة الإكلينيكية الموضحة بملاحظة المصدر نفسها (الحمى تحتم مضاد حيوي مع إفراغ الرحم).",
},

"AS-1805": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "كتلة زرقاء بالمهبل مع ألم دوري وانقطاع دورة أولي تشخص انسداد عند أدنى نقطة بمسار الطمث.",
    "clues": [
        ("1ry amenorrhea", "لم تحدث دورة أبدًا، لكن التبويض يحدث"),
        ("Cyclic pelvic pain", "يدل على أن الدورة تحدث لكن الدم لا يخرج"),
        ("blue mass in vagina", "علامة فحص مباشرة لانسداد عند غشاء البكارة"),
    ],
    "why_correct": [
        "فتاة بـ<bdi>primary amenorrhea</bdi> مع <bdi>cyclic pelvic pain</bdi> وكتلة زرقاء بارزة عند فتحة المهبل تعني دم الطمث محتجز خلف <bdi>imperforate hymen</bdi> (<bdi>hematocolpos</bdi>).",
        "هي تحيض بشكل طبيعي (الألم الدوري يدل على دورات تبويضية)، لكن الانسداد عند أدنى نقطة بمسار الطمث يمنع خروج الدم، فيظهر لونه الداكن خلال الغشاء الرقيق.",
    ],
    "when_changes": [
        "لو لم تكن هناك كتلة زرقاء بارزة عند فتحة المهبل مع وجود جيب مهبلي أعمى، الجواب يصير <bdi>transverse vaginal septum</bdi>.",
    ],
    "rule": "كتلة زرقاء بارزة عند فتحة المهبل مباشرة = <bdi>imperforate hymen</bdi>؛ انسداد بدون بروز خارجي يوجه لمستوى أعلى (<bdi>septum</bdi> أو عدم تكوّن).",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1807": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "انسداد الأنبوبين كليًا يلغي فائدة تحريض التبويض، فالحل هو تجاوز الأنابيب كليًا.",
    "clues": [
        ("B/L tubal block", "انسداد كلا الأنبوبين يمنع لقاء البويضة بالحيوان المنوي بأي طريق"),
    ],
    "why_correct": [
        "مع عامل ذكري طبيعي وانسداد ثنائي بالأنابيب، لا تستطيع البويضة ملاقاة الحيوان المنوي عبر أي أنبوب، فالعلاج هو <bdi>IVF</bdi> الذي يتجاوز الأنابيب كليًا.",
        "تحريض التبويض لا فائدة منه لأن المشكلة ليست بالتبويض بل بالانسداد الكامل.",
    ],
    "when_changes": [
        "لو كان الانسداد بأنبوب واحد فقط (<bdi>unilateral</bdi>) مع سلامة الأنبوب الآخر، الجواب يصير تحريض التبويض بـ<bdi>clomiphene</bdi>.",
        "لو كان الانسداد مكتشف فقط بـ<bdi>HSG</bdi> وغير مؤكد، الخطوة التالية تأكيده بـ<bdi>diagnostic laparoscopy</bdi> ورنين صبغي.",
    ],
    "rule": "انسداد <bdi>HSG</bdi> فقط يحتاج تأكيد بـ<bdi>laparoscopy</bdi>؛ انسداد ثنائي مؤكد يعني <bdi>IVF</bdi> مباشرة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1819": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "عدم خروج المشيمة بعد 30 دقيقة من الولادة يُعرّف <bdi>retained placenta</bdi> ويحتاج إزالة يدوية.",
    "clues": [
        ("30 min later", "تجاوز الحد الطبيعي لخروج المشيمة"),
        ("placenta did not come out", "تعريف مباشر لـ<bdi>retained placenta</bdi>"),
    ],
    "why_correct": [
        "عدم خروج المشيمة بعد 30 دقيقة من ولادة الطفل يُعرّف <bdi>retained placenta</bdi>.",
        "الخطوة التالية هي <bdi>manual removal of the placenta</bdi> تحت تخدير أو تسكين كافٍ مع تغطية مضاد حيوي؛ لو تبقى نسيج أو فشلت الإزالة، يتبعها كحت.",
    ],
    "when_changes": [
        "لو كان النزيف غزير قبل اكتمال 30 دقيقة، تتقدم الإزالة اليدوية فورًا بدون انتظار كامل المدة.",
        "لو كانت المشيمة لم تنزل بسبب <bdi>uterine atony</bdi> بدون احتجاز، الجواب يصير <bdi>IV oxytocin</bdi> لعلاج الرحم المرتخي.",
    ],
    "rule": "عدم خروج المشيمة بعد 30 دقيقة = إزالة يدوية؛ النزيف الغزير يسرّع هذا القرار قبل انتهاء المدة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1820": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "ارتفاع البرولاكتين الثانوي بسبب <bdi>hypothyroidism</bdi> يسبب اضطراب الدورة ثم انقطاعها.",
    "clues": [
        ("every 45 day", "دورة متباعدة (<bdi>oligomenorrhea</bdi>)"),
        ("period stopped for 6 months", "تطور إلى انقطاع كامل للدورة"),
    ],
    "why_correct": [
        "بالسؤال الأصلي كانت نتائج المختبر: <bdi>TSH</bdi> مرتفع، <bdi>FSH</bdi> و<bdi>LH</bdi> طبيعيان، و<bdi>prolactin</bdi> مرتفع.",
        "<bdi>hypothyroidism</bdi> يرفع <bdi>TRH</bdi>، الذي يحرض <bdi>prolactin</bdi>، والذي يثبط نبضات <bdi>GnRH</bdi>، فيسبب <bdi>oligomenorrhea</bdi> (دورة كل 45 يوم) ثم انقطاع كامل؛ ارتفاع البرولاكتين هنا سبب ثانوي مو مرض مستقل.",
    ],
    "when_changes": [
        "لو كان <bdi>TSH</bdi> طبيعي والبرولاكتين مرتفع جدًا، الجواب يصير <bdi>hyperprolactinemia</bdi> الأساسية (<bdi>prolactinoma</bdi>).",
        "لو كان <bdi>FSH</bdi> و<bdi>LH</bdi> منخفضين مع <bdi>TSH</bdi> منخفض أو طبيعي غير مناسب، الجواب يصير <bdi>hypopituitarism</bdi>.",
    ],
    "rule": "ارتفاع برولاكتين مع ارتفاع <bdi>TSH</bdi> يوجه نحو الغدة الدرقية كسبب أساسي؛ دائمًا تحقق من <bdi>TSH</bdi> قبل تسمية الحالة <bdi>hyperprolactinemia</bdi> أساسية.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
}

WHY_WRONG = {
"AS-1496": {
    "A": "<bdi>Tamoxifen</bdi> له تأثير محفز للإستروجين على <bdi>endometrium</bdi> ويسبب <bdi>hyperplasia</bdi>، أبدًا ليس علاج لها.",
    "B": "<bdi>hysterectomy</bdi> علاج <bdi>atypical hyperplasia</bdi> عند اكتمال <bdi>childbearing</bdi> أو بالمريضات الأكبر عمرًا؛ هنا سينهي <bdi>fertility</bdi> بمريضة عمرها 25.",
    "D": "<bdi>endometrial ablation</bdi> لا يعالج الـ<bdi>atypia</bdi>، ويدمر <bdi>fertility</bdi> ويعيق متابعة <bdi>endometrium</bdi> لاحقًا.",
},
"AS-1498": {
    "B": "<bdi>electrocautery</bdi> خيار للـ<bdi>warts</bdi> الكبيرة أو المعاندة، لكنه ليس الجواب هنا لأن <bdi>cryotherapy</bdi> أبسط وآمن بالحمل.",
    "C": "<bdi>podophyllin resin</bdi> يمتص جهازيًا وممنوع بالحمل (<bdi>teratogenic</bdi> وسام).",
    "D": "<bdi>intralesional interferon</bdi> غير موصى به بالحمل ومحجوز للحالات المعاندة بغير الحوامل.",
},
"AS-1500": {
    "B": "<bdi>MRI</bdi> لا يعطي تشخيص نسيجي؛ يستخدم لـ<bdi>staging</bdi> بعد تأكيد السرطان.",
    "C": "<bdi>diagnostic laparoscopy</bdi> يفحص خارج الرحم وداخل البطن، ولا يأخذ عينة من <bdi>endometrium</bdi>.",
    "D": "<bdi>CT</bdi> يستخدم لكشف الانتشار البعيد و<bdi>staging</bdi>، مو لتشخيص آفة بالـ<bdi>endometrium</bdi>.",
},
"AS-1506": {
    "A": "0.2 mg أقل حتى من الجرعة الوقائية العادية، غير كافية لأي حمل.",
    "B": "0.8 mg تقارب جرعة المخاطر العادية (0.4 mg)؛ <bdi>SCD</bdi> تحتاج جرعة عالية لاستهلاك <bdi>folate</bdi> المستمر.",
    "C": "1.4 mg لسه أقل بكثير من نطاق الجرعة العالية الموصى بها.",
},
"AS-1534": {
    "B": "<bdi>OCP</bdi> علاج اضطراب الدورة بعد تأكيد <bdi>PCOS</bdi> وعدم وجود رغبة بالحمل؛ لا يُختار قبل اكتمال الفحوصات، والإستروجين يزيد خطر <bdi>VTE</bdi> بالبدانة.",
},
"AS-1549": {
    "A": "وقف المتابعة خطأ ما زال <bdi>bhCG</bdi> 500؛ لازم المتابعة الأسبوعية لحد عدم الاكتشاف لاستثناء <bdi>persistent trophoblast</bdi>.",
    "B": "التدخل الجراحي الفوري يُختار عند ارتفاع <bdi>bhCG</bdi> بين يوم 4 و7 أو تمزق أو عدم استقرار؛ هنا القيم بنازلة بثبات.",
    "D": "جرعة ثانية من <bdi>methotrexate</bdi> تُعطى عند <bdi>plateau</bdi> أو نزول أقل من 15%؛ هنا النزول أكثر من 15%.",
},
"AS-1560": {
    "A": "<bdi>placenta previa</bdi> يسبب نزيف غزير غير مؤلم من نوع ميكانيكي، ونادرًا يسبب <bdi>DIC</bdi>.",
    "C": "اضطراب تخثر خلقي نادر ولا يعتبر <bdi>consumptive coagulopathy</bdi>.",
    "D": "<bdi>uterine rupture</bdi> يسبب ألم وصدمة مع ارتفاع ارتفاع الجنين، عادة بتاريخ ولادة قيصرية سابقة، وهو أقل شيوعًا من <bdi>abruption</bdi> كسبب لـ<bdi>DIC</bdi>.",
},
"AS-1565": {
    "A": "<bdi>myomectomy</bdi> خطوة علاج الفايبرويد لاحقًا، مو الأولوية الفورية مع فقر دم شديد (<bdi>Hb 70</bdi>).",
    "B": "<bdi>uterine artery embolization</bdi> خيار يجي بعد استقرار المريضة، مو أولوية فورية.",
    "D": "<bdi>OCP</bdi> علاج طبي للنزيف نفسه، لكن استقرار المريضة بتصحيح فقر الدم الشديد يسبقه.",
},
"AS-1566": {
    "A": "<bdi>myomectomy</bdi> جراحة تحافظ على الخصوبة للفايبرويد الكبير أو فشل العلاج الطبي، مو الخطوة الفورية قبل تجربة علاج طبي.",
    "B": "<bdi>uterine artery embolization</bdi> محجوز لمن ترفض الجراحة، مو الخطوة الأولى.",
    "C": "هذا الخيار فارغ بالنسخة الأصلية؛ لو كان «تصحيح فقر الدم» هو الجواب الصحيح (انظر السؤال الشقيق).",
},
"AS-1568": {
    "A": "<bdi>myomectomy</bdi> جراحة تحافظ على الخصوبة لمن تبي حمل؛ غير مناسبة بعمر 60 وتتجاهل تقييم السرطان.",
    "B": "<bdi>hysterectomy</bdi> قد تكون العلاج النهائي بعد معرفة النتيجة النسيجية، لكن الجراحة قبل أخذ عينة تتجاهل الخطوة الأساسية.",
    "C": "<bdi>uterine artery embolization</bdi> لعلاج الفايبرويد عند رفض الجراحة، ولا يستثني خباثة <bdi>endometrium</bdi>.",
},
"AS-1572": {
    "A": "متابعة نبض وضغط الأم لا تخبرنا شي عن حالة الجنين.",
    "B": "متابعة التقلصات تقيّم تقدم المخاض، لكنها لا تخبرنا إذا الجنين يتحمل المخاض.",
    "C": "الكشف المبكر عن المضاعفات هدف المتابعة، مو طريقة متابعة بنفسها.",
},
"AS-1577": {
    "B": "<bdi>punch biopsy</bdi> يستخدم لآفات عنق الرحم الظاهرة، ولا دور له بتشخيص <bdi>miscarriage</bdi>.",
    "C": "الفحص البطني لا يقيّم حالة <bdi>cervical os</bdi>، وهو الفارق بين أنواع <bdi>miscarriage</bdi>.",
    "D": "<bdi>CT</bdi> لا يستخدم لتقييم حمل مبكر؛ يضيف إشعاع ويوضح محتوى الرحم أقل من <bdi>ultrasound</bdi>.",
},
"AS-1588": {
    "A": "<bdi>nifedipine</bdi> أول خيار <bdi>tocolytic</bdi> لكنه لا يعطي حماية عصبية للجنين.",
    "B": "<bdi>terbutaline</bdi> له آثار جانبية أمومية كبيرة، وليس خط أول، ولا يعطي حماية عصبية.",
    "C": "<bdi>indomethacin</bdi> خيار <bdi>tocolytic</bdi> قبل 32 أسبوع لكنه يسبب تضيق <bdi>ductus arteriosus</bdi> وقلة سائل أمنيوسي، ولا يعطي حماية عصبية.",
},
"AS-1607": {
    "A": "خفض الضغط لا يمنع <bdi>oligohydramnios</bdi> الناتج عن قصور المشيمة.",
    "B": "وفاة الجنين سببها مرض المشيمة الأساسي، وخافضات الضغط لا تعالجه؛ الحل الجنيني هو الولادة بالوقت المناسب.",
    "C": "خافضات الضغط لا تقلل <bdi>growth restriction</bdi>، وخفض الضغط بشدة ممكن يقلل تروية المشيمة.",
},
"AS-1612": {
    "A": "تكرار الدوبلر أسبوعيًا مناسب بمتابعة <bdi>FGR</bdi> بنتائج مطمئنة؛ ظهور <bdi>REDV</bdi> بعمر ≥32 أسبوع يجعل الانتظار أسبوع خطر على الجنين.",
    "B": "ولادة فورية بدون <bdi>steroids</bdi> تفوّت فائدة نضج الرئة بعمر 33 أسبوع ما دام الجنين غير متدهور حاليًا؛ تُختار عند <bdi>CTG/BPP</bdi> غير طبيعي فعلًا.",
    "D": "متابعة النمو بعد أسبوعين تتجاهل <bdi>REDV</bdi>، وهي أشد نتيجة دوبلر؛ تناسب <bdi>SGA</bdi> بدوبلر طبيعي.",
},
"AS-1613": {
    "A": "تكرار الدوبلر أسبوعيًا مناسب لمتابعة طبيعية؛ ظهور <bdi>REDV</bdi> بعمر ≥32 أسبوع يجعل الانتظار خطيرًا.",
    "B": "الولادة مطلوبة لكن بعمر 33 أسبوع تُعطى <bdi>steroids</bdi> أولًا إن لم يكن الجنين بضيق حاد؛ القيصرية الفورية بدون <bdi>steroids</bdi> تناسب <bdi>CTG/BPP</bdi> غير مطمئن.",
    "D": "متابعة النمو بعد أسبوعين تتجاهل نتيجة الدوبلر الأشد (<bdi>REDV</bdi>) وتناسب فقط دوبلر طبيعي.",
},
"AS-1653": {
    "A": "<bdi>preterm labor</bdi> يحتاج تقلصات مع تغيّر بعنق الرحم بعمر أقل من 37 أسبوع؛ هنا العمر 41 أسبوع.",
    "B": "<bdi>PPROM</bdi> يعني تمزق قبل بداية التقلصات بعمر أقل من 37 أسبوع؛ هنا العمر 41 أسبوع والتمزق جاء بعد بداية المخاض.",
},
"AS-1687": {
    "A": "جراحة استئصال شاملة مع إزالة كل الانتشارات الظاهرة غير واقعية مع انتشار واسع جدًا بكل البطن؛ تناسب مرض قابل للاستئصال الكامل.",
    "C": "رعاية تلطيفية فقط تحجب علاج فعّال متوفر (كيميائي ± جراحة لاحقة) عن مريضة يبدو أنها قد تستفيد منه.",
    "D": "<bdi>radiotherapy</bdi> ليس خط علاج معياري بسرطان المبيض المنتشر بالبطن.",
},
"AS-1687B": {
    "A": "علاج كيميائي أولًا ثم إعادة تقييم (<bdi>neoadjuvant</bdi>) يُختار عند عدم قابلية الاستئصال الكامل أو عدم لياقة المريضة للجراحة؛ لم يُذكر أي منهما هنا.",
    "C": "<bdi>radiotherapy</bdi> ليس خط علاج معياري بسرطان المبيض المنتشر بالصفاق.",
    "D": "رعاية تلطيفية فقط تحجب علاج فعّال (جراحة + علاج كيميائي) يستجيب له <bdi>advanced ovarian cancer</bdi> غالبًا جيدًا.",
},
"AS-1699": {
    "A": "<bdi>methotrexate</bdi> صحيح فقط عند تحقق كل الشروط معًا (استقرار، <bdi>bhCG</bdi> ≤5000، لا نشاط قلبي، كتلة أقل من 4 سم، متابعة موثوقة)؛ هنا حجم الكتلة 4 سم يفشل الشرط.",
},
"AS-1700": {
    "B": "<bdi>adenomyosis</bdi> يسبب نزيف غزير وألم مع رحم متضخم ومنتظم طري، عادة بسيدة متعددة الولادة؛ لا يسبب <bdi>nodularity</bdi> على <bdi>uterosacral ligaments</bdi>.",
    "C": "<bdi>leiomyoma</bdi> يسبب نزيف غزير مع رحم متضخم وغير منتظم وصلب؛ الـ<bdi>nodularity</bdi> هنا بالرحم نفسه، مو بالـ<bdi>uterosacral ligaments</bdi>.",
},
}

HIGHLIGHT_TERMS = {
"AS-1496": ["25-year-old", "Atypical complex hyperplasia"],
"AS-1498": ["pregnant", "large genital warts"],
"AS-1500": ["menorrhagia", "diabetic and hypertensive", "Thickened endometrial lining"],
"AS-1506": ["pregnant", "sickle cell disease"],
"AS-1534": ["irregular menstrual cycle", "obese and BMI 31"],
"AS-1549": ["bhCG"],
"AS-1560": ["uncontrolled bleeding", "DIC"],
"AS-1565": ["large leiomyoma", "Hb is 70"],
"AS-1566": ["large leiomyoma"],
"AS-1568": ["post-menopausal bleeding", "the same size and location"],
"AS-1572": ["low risk and uncomplicated"],
"AS-1577": ["amenorrhea for the last 8 weeks", "expelling blood and tissue through the vagina"],
"AS-1588": ["31 weeks", "preterm labor"],
"AS-1607": ["severe preeclampsia", "rationale", "antihypertensive medications"],
"AS-1612": ["33 weeks'", "small for gestational age", "reversed end-diastolic flow"],
"AS-1613": ["33 weeks'", "small for gestational age", "reversed enddiastolic flow"],
"AS-1653": ["41 WEEKS", "IN LABOR", "GUSH OF FLUID"],
"AS-1687": ["markedly elevated CA-125", "high-grade epithelial ovarian carcinoma", "extensive metastatic spread throughout the abdomen"],
"AS-1687B": ["solid irregular fixed pelvic mass", "multilocular ovarian mass", "advanced epithelial ovarian cancer"],
"AS-1699": ["ectopic pregnancy", "4 cm"],
"AS-1700": ["Dysmenorrhea", "nodularity on uterosacral ligament"],
}
