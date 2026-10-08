# -*- coding: utf-8 -*-
# Proper bilingual rewrite — batch p07 (45 questions, Medicine section).

EXPLANATIONS = {

"AS-1516": {"correct_letter": "C", "self_judged": True,
    "idea": "<bdi>myoclonic seizures</bdi> ما زالت مستمرة رغم <bdi>valproic acid</bdi> بجرعة كافية — الخطوة الثانية بسلم علاج هذا النوع من <bdi>seizures</bdi>.",
    "clues": [("myoclonic seizures", "نوع <bdi>seizure</bdi> له سلم علاج خاص، وبعض الأدوية تسوّئه"),
               ("Valproic acid", "خط أول، لكن فشل هنا رغم الجرعة الكافية")],
    "why_correct": [
        "<bdi>valproic acid</bdi> هو خط أول لـ<bdi>myoclonic seizures</bdi>، ولما يفشل رغم جرعة كافية، الخط الثاني المعتمد هو <bdi>levetiracetam</bdi>.",
        "أدوية حاصرة لقنوات الصوديوم زي <bdi>phenytoin</bdi> و<bdi>carbamazepine</bdi> و<bdi>oxcarbazepine</bdi> وكذلك <bdi>gabapentin</bdi> ممكن تسوّئ <bdi>myoclonus</bdi>، فما تُستخدم.",
        "<bdi>lamotrigine</bdi> كمان ممكن يسوّئ <bdi>myoclonus</bdi> بعض المرات، و<bdi>ethosuximide</bdi> يُستخدم بس لـ<bdi>absence seizures</bdi>، مو <bdi>myoclonic</bdi>."],
    "when_changes": ["لو كان النوع <bdi>absence seizures</bdi> (مو <bdi>myoclonic</bdi>)، الجواب يتحول لـ<bdi>ethosuximide</bdi>."],
    "rule": "<bdi>myoclonic seizures</bdi>: خط أول <bdi>valproate</bdi>، خط ثاني <bdi>levetiracetam</bdi>؛ تجنبي حاصرات قنوات الصوديوم لأنها تسوّئ <bdi>myoclonus</bdi>.",
    "comparison": None, "labs": None,
    "guideline_note": "هذا السؤال ما له جواب مؤكد من المصدر؛ اخترنا <bdi>levetiracetam</bdi> بناءً على سلم العلاج المعروف لـ<bdi>myoclonic seizures</bdi> بعد فشل <bdi>valproate</bdi>."},

"AS-1521": {"correct_letter": "B", "self_judged": False,
    "idea": "<bdi>ACS</bdi> قبل ٥ أيام، الآن هبوط ضغط وتسرع نبض مع نفخة شاملة الانقباض (<bdi>pansystolic murmur</bdi>) تنتشر لحافة القص اليمنى — مضاعفة ميكانيكية محددة بعد الاحتشاء.",
    "clues": [("5 days after", "توقيت كلاسيكي للمضاعفات الميكانيكية بعد الاحتشاء (يوم ٣-٥)"),
               ("hypotension", "صدمة قلبية جديدة"),
               ("pansystolic murmur", "نفخة شاملة الانقباض جديدة"),
               ("right sternal border", "اتجاه الانتشار المميز لهذا السؤال")],
    "why_correct": [
        "نفخة شاملة الانقباض جديدة مع هبوط ضغط وتسرع نبض بعد ٥ أيام من <bdi>MI</bdi> هي مضاعفة ميكانيكية.",
        "النفخة اللي تنتشر من حافة القص اليسرى إلى حافة القص اليمنى هي نفخة <bdi>VSD</bdi> المكتسبة، يعني <bdi>interventricular septal rupture</bdi> (تحويلة من اليسار لليمين تسبب صدمة قلبية)."],
    "when_changes": ["لو كانت النفخة تنتشر للإبط مع وذمة رئة حادة، الجواب يتحول لـ<bdi>papillary muscle rupture</bdi>."],
    "rule": "نفخة تتجه للقص = <bdi>septal rupture</bdi>؛ نفخة تتجه للإبط مع وذمة رئة = <bdi>papillary muscle rupture</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1524": {"correct_letter": "C", "self_judged": False,
    "idea": "مريض بعد احتشاء قديم، ضيق تنفس مترقي وضيق نفس بالاستلقاء حتى بالراحة، كسر قذفي ٢٠٪ — قصور قلب حاد لا معاوض بوذمة رئة.",
    "clues": [("MI two years ago", "مرض قلبي معروف"),
               ("progressive dyspnea and orthopnea at rest", "ضيق تنفس بالراحة = شدة عالية"),
               ("EF 20%", "كسر قذفي منخفض جدًا")],
    "why_correct": [
        "ضيق تنفس بالراحة مع كسر قذفي ٢٠٪ يعني <bdi>acute decompensated heart failure</bdi> مع وذمة رئة، وعلاج الطوارئ هو تفريغ السوائل بـ<bdi>IV furosemide</bdi> مع دعم التنفس.",
        "بوجود ضيق نفس شديد، <bdi>non-invasive ventilation</bdi> (<bdi>CPAP/BiPAP</bdi>) تحسّن الأكسجين وتقلل جهد التنفس والحمل القبلي، وتجنّب التنبيب."],
    "when_changes": ["لو كان المريض خامل الوعي أو مستنفذ أو فشل معه التنفس غير الباضع، الجواب يتحول لـ<bdi>intubation</bdi>."],
    "rule": "ضيق تنفس بالراحة بقصور قلب حاد = <bdi>IV furosemide</bdi> + <bdi>NIV</bdi>؛ التنبيب فقط لو فشل التنفس غير الباضع.",
    "comparison": None, "labs": [["EF", "20%", ">50% طبيعي"]], "guideline_note": None},

"AS-1529": {"correct_letter": "B", "self_judged": False,
    "idea": "مريض قصور كلوي مرحلة نهائية، أصوات قلب مكتومة، انصباب تامور بالصدى، وضغط منخفض فعليًا (٨٦) — دكاك قلبي غير مستقر.",
    "clues": [("end-stage kidney disease", "سبب شائع لانصباب تامور يوريمي"),
               ("muffled heart sounds", "علامة من ثلاثية <bdi>Beck</bdi>"),
               ("pericardial effusion", "مؤكد بالصدى"),
               ("Was Frankly Hypotensive", "المفتاح — عدم الاستقرار الفعلي")],
    "why_correct": [
        "أصوات مكتومة + انصباب مؤكد + ضغط منخفض فعليًا = دكاك قلبي بتأثير هيموديناميكي.",
        "الدكاك غير المستقر يحتاج تصريف فوري، فـ<bdi>pericardiocentesis</bdi> هي الخطوة التالية بغض النظر عن سبب اليوريميا الأساسي."],
    "when_changes": ["لو كان الضغط طبيعي (مستقر)، الجواب يتحول لتكثيف <bdi>hemodialysis</bdi> لعلاج الانصباب اليوريمي."],
    "rule": "انصباب يوريمي مستقر = ديال؛ انصباب مع دكاك غير مستقر (ضغط منخفض) = تصريف فوري.",
    "comparison": None, "labs": [["BP", "86/.. mmHg", "&lt;90 systolic = هبوط ضغط فعلي"]], "guideline_note": None},

"AS-1535": {"correct_letter": "A", "self_judged": False,
    "idea": "رجل ٦٠ سنة سكري وضغط، استسقاء بطني بعد ١٠ سنوات من ارتفاع إنزيمات الكبد بدون كحول — صورة <bdi>NAFLD</bdi> المتقدمة لتشمع، والسؤال عن «الأفضل» مو «الخطوة التالية».",
    "clues": [("HTN and DM", "عوامل خطر <bdi>NAFLD</bdi>"),
               ("no history of alcohol use", "يستبعد السبب الكحولي"),
               ("10 years history of high aminotransferase", "مدة طويلة توحي بتليف متقدم"),
               ("ascites", "علامة تشمع متقدم")],
    "why_correct": [
        "الصورة كلها <bdi>non-alcoholic fatty liver disease</bdi> متطورة لتشمع: ضغط وسكري، بدون كحول، وارتفاع إنزيمات طويل الأمد، والآن استسقاء.",
        "جواب المصدر هنا <bdi>liver biopsy</bdi> لأن السؤال يسأل عن «الأفضل» (<bdi>BEST</bdi>) بمعنى المعيار الذهبي: الخزعة تؤكد <bdi>steatohepatitis</bdi> وتحدد درجة التليف وتستبعد أسباب ثانية لارتفاع الإنزيمات المزمن."],
    "when_changes": ["لو كان السؤال يسأل عن الخطوة الأولى/التالية للتشخيص (مو الأفضل/المعيار الذهبي)، الجواب يتحول لـ<bdi>ultrasound</bdi> كفحص أولي غير باضع."],
    "rule": "«الأفضل/المعيار الذهبي» بتشخيص <bdi>NAFLD</bdi>/تشمع = <bdi>liver biopsy</bdi>؛ «الخطوة الأولى/التالية» = <bdi>ultrasound</bdi>.",
    "comparison": None, "labs": None,
    "guideline_note": "هذا السؤال وصفه المصدر بإنه مختلف عليه؛ أغلب الإرشادات ما تطلب خزعة روتينية (الخزعة نادرًا لازمة لأن التشخيص يصير بالفحوصات والسونار بأكثر من ٩٠٪ من الحالات)، لكن احتفظنا بجواب المصدر <bdi>liver biopsy</bdi> لأنه الموثق ومربوط بكلمة «الأفضل» كمعيار ذهبي."},

"AS-1537": {"correct_letter": "A", "self_judged": False,
    "idea": "<bdi>HFrEF</bdi> من <bdi>dilated cardiomyopathy</bdi>، المريض أصلاً على <bdi>ARB</bdi> وحاصر بيتا و<bdi>MRA</bdi> ومدر — أي إضافة تنفع بدون ما تضر.",
    "clues": [("Heart failure with reduced EF", "يحدد سلم العلاج المطلوب"),
               ("metoprolol", "حاصر بيتا موجود أصلاً — يستبعد إضافة حاصر بيتا ثاني")],
    "why_correct": [
        "المريض متكامل العلاج القياسي (<bdi>ARB</bdi>، حاصر بيتا، <bdi>MRA</bdi>، مدر)، فالإضافة المنطقية لو الأعراض مستمرة بإيقاع جيبي ونبض راحة ٧٠ أو أكثر رغم حاصر البيتا هي <bdi>ivabradine</bdi> (حاصر قناة <bdi>If</bdi>).",
        "<bdi>ivabradine</bdi> يقلل النبض ويقلل دخول المستشفى بقصور القلب بدون أي ضرر إضافي، وهو الخيار الوحيد اللي يضيف فايدة هنا."],
    "when_changes": ["لو كان المريض غير معالج بحاصر بيتا أصلاً، الخطوة الصحيحة تبدأ بإضافة حاصر بيتا (<bdi>bisoprolol</bdi>) أولاً."],
    "rule": "حاصر بيتا موجود + أعراض مستمرة + إيقاع جيبي ونبض ≥٧٠ = أضيفي <bdi>ivabradine</bdi>؛ أبدًا لا تضيفي حاصر بيتا ثاني أو <bdi>verapamil/diltiazem</bdi> بـ<bdi>HFrEF</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1540": {"correct_letter": "D", "self_judged": False,
    "idea": "لمفوما عالية الخطورة على كيماوي، بوتاسيوم مرتفع وكالسيوم منخفض وفوسفات مرتفع — متلازمة تحلل ورم، لكن حمض اليوريك طبيعي، فالإشكال المتبقي هو الفوسفات.",
    "clues": [("Burkitt lymphoma", "ورم عالي الخطورة لمتلازمة تحلل الورم"),
               ("hypocalcemia + hyperphosphatemia", "فوسفات مرتفع هو اللي يسحب الكالسيوم للأسفل"),
               ("Uric acid below 480", "طبيعي — يستبعد الحاجة لعلاج حمض اليوريك")],
    "why_correct": [
        "علاج الكيماوي لورم عالي الخطورة مع بوتاسيوم وفوسفات مرتفعين وكالسيوم منخفض = متلازمة تحلل الورم.",
        "بما إن حمض اليوريك هنا طبيعي (أقل من ٤٨٠) وما فيه ذكر لقلة بول، الخلل المتبقي بين الخيارات هو ارتفاع الفوسفات، اللي هو السبب بترسيب الكالسيوم.",
        "<bdi>sevelamer</bdi> رابط فوسفات يخفضه ويحمي الكلى من ترسب فوسفات الكالسيوم."],
    "when_changes": ["لو كان حمض اليوريك مرتفع فعليًا، الجواب يتحول لـ<bdi>allopurinol</bdi> (وقاية) أو <bdi>rasburicase</bdi> (علاج مؤكد)."],
    "rule": "متلازمة تحلل ورم: بوتاسيوم مرتفع يُعالج بروتوكول فرط البوتاسيوم، حمض يوريك مرتفع = ألوبيورينول/راسبيوريكيز، فوسفات مرتفع = سيفيلامر.",
    "comparison": None, "labs": [["K", "5.3 mmol/L", "3.5-5.1 طبيعي"], ["Uric acid", "&lt;480 µmol/L", "طبيعي تقريبًا"]], "guideline_note": None},

"AS-1541": {"correct_letter": "B", "self_judged": False,
    "idea": "امرأة ٥٠ سنة، ألم بمفاصل أصابع بعيدة وقريبة (<bdi>DIP, PIP</bdi>) ثنائي ٣ سنين، بدون تيبس صباحي واضح، وعقد صلبة غير مؤلمة بمفاصل <bdi>DIP</bdi> — صورة <bdi>osteoarthritis</bdi> الكلاسيكية.",
    "clues": [("distal and proximal interphalangeal joints", "إصابة <bdi>DIP</bdi> تحديدًا تميل لـ<bdi>OA</bdi> مو <bdi>RA</bdi>"),
               ("does not have significant early morning stiffness", "غياب التيبس الطويل يستبعد التهاب مناعي فعّال"),
               ("non-tender hard nodules over some distal interphalangeal", "عقد <bdi>Heberden</bdi> الصلبة"),
               ("Rheumatoid factor 30 (&lt;58 kIU/L)", "طبيعي، يدعم غياب التهاب مناعي")],
    "why_correct": [
        "ألم مزمن ٣ سنين بمفاصل <bdi>DIP</bdi> و<bdi>PIP</bdi> ثنائيًا بدون تيبس صباحي طويل، مع عقد صلبة غير مؤلمة بـ<bdi>DIP</bdi> (<bdi>Heberden nodes</bdi>) هي الصورة الكلاسيكية لـ<bdi>hand osteoarthritis</bdi>.",
        "التحاليل مطمّنة: <bdi>CRP</bdi> و<bdi>ESR</bdi> و<bdi>rheumatoid factor</bdi> كلها طبيعية، يعني ما فيه عملية التهابية تفسر الأعراض."],
    "when_changes": ["لو كان الالتهاب فعّال بمفاصل <bdi>MCP/PIP/wrist</bdi> (<bdi>DIP</bdi> معفى) مع تيبس أطول من ٣٠ دقيقة وإنزيمات مرتفعة، الجواب يتحول لـ<bdi>seronegative rheumatoid arthritis</bdi>."],
    "rule": "إصابة <bdi>DIP</bdi> + عقد صلبة + تحاليل طبيعية = <bdi>osteoarthritis</bdi>؛ <bdi>RA</bdi> تعفي <bdi>DIP</bdi> دايمًا تقريبًا.",
    "comparison": None, "labs": [["CRP", "5", "&lt;8.2 mg/L طبيعي"], ["Rheumatoid factor", "30", "&lt;58 kIU/L طبيعي"], ["ESR", "15", "طبيعي تقريبًا"]], "guideline_note": None},

"AS-1542": {"correct_letter": "B", "self_judged": False,
    "idea": "رجل ٥٢ سنة سكري، ألم وتورم بمفاصل <bdi>DIP, PIP</bdi> مع ألم ركبة ثنائي وتحديد بثني الركبة — توزيع نموذجي لـ<bdi>OA</bdi> (مفاصل أصابع + مفصل حامل وزن).",
    "clues": [("DIP and PIP pain and swelling", "توزيع يميل لـ<bdi>OA</bdi>"),
               ("Rheumatoid factor 55 (normal &lt;58)", "طبيعي بالحدود، لا يدعم <bdi>RA</bdi>")],
    "why_correct": [
        "إصابة <bdi>DIP</bdi> و<bdi>PIP</bdi> مع ألم ركبة وتحديد بالثني هي التوزيع النموذجي لـ<bdi>osteoarthritis</bdi> (مفاصل أصابع + مفصل حامل وزن).",
        "<bdi>RF</bdi> طبيعي (٥٥ وتحت الحد ٥٨) و<bdi>ESR</bdi> بسيط الارتفاع فقط (١٥)، وهذا ما يدعم وجود التهاب مناعي فعلي."],
    "when_changes": ["لو كان الالتهاب يصيب <bdi>MCP</bdi> والرسغ بشكل متماثل مع تيبس أطول من ٣٠ دقيقة وإنزيمات التهاب واضحة الارتفاع، الجواب يتحول لـ<bdi>seronegative RA</bdi>."],
    "rule": "لا تدعي قيمة مخبرية «حد» تسحبك لـ<bdi>seronegative RA</bdi> لما تكون مفاصل <bdi>DIP</bdi> هي المصابة.",
    "comparison": None, "labs": [["Rheumatoid factor", "55", "&lt;58 kIU/L طبيعي"], ["ESR", "15", "&lt;10 طبيعي تقريبًا"]], "guideline_note": None},

"AS-1547": {"correct_letter": "A", "self_judged": True,
    "idea": "رجل ٢٩ سنة بفحص توظيف روتيني، بدون أعراض، نفخة شاملة الانقباض (<bdi>pansystolic murmur</bdi>) تنتشر للإبط — لقطة عرضية بدون أي سياق مرضي ثاني.",
    "clues": [("29-year-old", "عمر صغير، ما فيه تاريخ مرضي قلبي"),
               ("asymptomatic", "لقطة بدون أعراض تمامًا"),
               ("pansystolic murmur that radiated to the axilla", "النفخة الكلاسيكية لـ<bdi>mitral regurgitation</bdi>")],
    "why_correct": [
        "بشاب ٢٩ سنة بدون أي أعراض ولا تاريخ حمى رثوية أو احتشاء، أشيع سبب لنفخة <bdi>MR</bdi> تنكشف صدفة بفحص روتيني هو <bdi>Mitral Valve Prolapse</bdi>، وهو أشيع سبب لـ<bdi>MR</bdi> بالدول المتقدمة بشكل عام وبالشباب الأصحاء تحديدًا."],
    "when_changes": ["لو ذكر السؤال تاريخ حمى رثوية أو منطقة ينتشر فيها هذا المرض، الجواب يتحول لـ<bdi>rheumatic mitral regurgitation</bdi>؛ ولو ذكر تاريخ احتشاء، يتحول لـ<bdi>ischemic MR</bdi>."],
    "rule": "نفخة <bdi>MR</bdi> صدفة بشاب بدون أعراض ولا تاريخ = <bdi>MVP</bdi> هو الأشيع؛ تاريخ حمى رثوية = رثوي؛ تاريخ احتشاء = إقفاري؛ قلب متوسع = وظيفي.",
    "comparison": None, "labs": None,
    "guideline_note": "هذا السؤال ما له جواب مؤكد من المصدر؛ اخترنا <bdi>MVP</bdi> لأنه الأشيع سبب لنفخة <bdi>MR</bdi> تُكتشف صدفة بشاب سليم بدون أي سياق مرضي آخر."},

"AS-1551": {"correct_letter": "D", "self_judged": False,
    "idea": "شاب ١٩ سنة نوبات <bdi>seizure</bdi> متكررة بسرعة (بالإسعاف، وبعدها أثناء الفحص)، توقفت بـ<bdi>lorazepam</bdi> وريدي — هذا تصرف كـ<bdi>status epilepticus</bdi>، نحتاج خط ثاني طويل المفعول.",
    "clues": [("history of seizure", "تاريخ معروف للنوبات"),
               ("generalized tonic-clonic seizure", "نوبة كاملة ثانية بوقت قصير"),
               ("terminates after intravenous lorazepam", "البنزوديازيبين وقف النوبة الحالية بس مفعوله قصير")],
    "why_correct": [
        "نوبات متكررة متتالية (بالإسعاف، وبعدها أثناء الفحص) تتصرف كـ<bdi>status epilepticus</bdi>، و<bdi>lorazepam</bdi> يوقف النوبة الحالية بس مفعوله قصير.",
        "الخطوة التالية هي دواء خط ثاني طويل المفعول يمنع تكرار النوبة، والكلاسيكي هو <bdi>fosphenytoin infusion</bdi>، قبل أي فحص تشخيصي."],
    "when_changes": ["لو كان السيناريو بعد إصابة رأس/رضّة، <bdi>CT brain</bdi> يصير أولوية مباشرة حسب نسخة المصدر الثانية لنفس السؤال."],
    "rule": "بنزوديازيبين يوقف النوبة الحالية، لكن لازم دواء خط ثاني (<bdi>fosphenytoin</bdi>) يمنع التكرار؛ الفحوصات التشخيصية تجي بعد الاستقرار.",
    "comparison": None, "labs": None,
    "guideline_note": "المصدر وضّح جدل حول هذا السؤال: نسخة بدون رضّة = <bdi>fosphenytoin</bdi>؛ نسخة بوجود رضّة رأس (نفس السؤال تقريبًا) = <bdi>CT brain</bdi> أولاً؛ أبقينا جواب المصدر <bdi>fosphenytoin</bdi> لعدم ذكر أي رضّة بهذا النص."},

"AS-1554": {"correct_letter": "B", "self_judged": False,
    "idea": "نقل دم قبل ١٠ سنين، إنزيمات كبد طبيعية، تحاليل التهاب الكبد B: <bdi>HBsAg</bdi> موجب و<bdi>IgG HBc</bdi> موجب و<bdi>IgM HBc</bdi> سالب و<bdi>HBeAg</bdi> موجب — عدوى مزمنة غير نشطة.",
    "clues": [("HBsAg (+)", "عدوى حالية (مزمنة أو حادة)"),
               ("IgG HBc (+)", "التهاب كبد B، مو حادة")],
    "why_correct": [
        "<bdi>HBsAg</bdi> موجب يعني عدوى حالية، و<bdi>IgG anti-HBc</bdi> موجب مع <bdi>IgM</bdi> سالب يعني العدوى غير حادة — يعني التهاب كبد B مزمن.",
        "إنزيمات الكبد الطبيعية وبدون أعراض هي ما تجعل المصدر يصفها بـ«غير نشطة» (<bdi>Chronic inactive HBV</bdi>). (كلمة <bdi>HPV</bdi> بالخيارات خطأ طباعي والمقصود <bdi>HBV</bdi>.)"],
    "when_changes": ["لو كان <bdi>IgM HBc</bdi> موجب مع إنزيمات مرتفعة بشدة، الجواب يتحول لعدوى حادة."],
    "rule": "<bdi>HBsAg</bdi> موجب + <bdi>IgM anti-HBc</bdi> = عدوى حادة؛ <bdi>HBsAg</bdi> موجب + <bdi>IgG anti-HBc</bdi> فقط = عدوى مزمنة.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1556": {"correct_letter": "B", "self_judged": False,
    "idea": "فتاة ١٨ سنة عندها <bdi>WPW</bdi> ودخلت برجفان أذيني، خفقان وضيق تنفس خفيف — السؤال عن دواء ضبط الإيقاع الآمن، مو أي دواء يبطئ العقدة الأذينية البطينية.",
    "clues": [("Wolff-Parkinson-White syndrome and atrial fibrillation", "تركيبة خطيرة — حاصرات العقدة الأذينية البطينية ممنوعة"),
               ("control her rhythm", "السؤال عن ضبط الإيقاع تحديدًا")],
    "why_correct": [
        "بـ<bdi>WPW</bdi> مع رجفان أذيني، حصر العقدة الأذينية البطينية يدفع التوصيل كامل عبر المسار الإضافي، وهذا ممكن يسبب <bdi>ventricular fibrillation</bdi>.",
        "السؤال يسأل عن ضبط «الإيقاع»، و<bdi>amiodarone</bdi> هو الخيار الوحيد اللي يعمل كمضاد اضطراب نظم فعلي (ضبط إيقاع)، مو مجرد حاصر للعقدة الأذينية البطينية."],
    "when_changes": ["لو كانت غير مستقرة هيموديناميكيًا، الجواب يتحول لـ<bdi>synchronized DC cardioversion</bdi> فورًا."],
    "rule": "<bdi>WPW + AF</bdi>: تجنبي كل حاصرات العقدة الأذينية البطينية (<bdi>adenosine, beta-blockers, CCBs, digoxin</bdi>)؛ المستقر يُعالج بـ<bdi>amiodarone</bdi> أو دواء يعمل على المسار الإضافي، وغير المستقر بتحويل كهربائي.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1562": {"correct_letter": "A", "self_judged": False,
    "idea": "صورة مسحة دم فيها خلايا منجلية — السؤال عن الفحص المؤكد، مو مجرد المسحة.",
    "clues": [("sickle cells", "موجودة بالمسحة لكن ما تثبت النمط الجيني"),
               ("confirmatory test", "الفحص المؤكد وليس الأولي")],
    "why_correct": [
        "خلايا منجلية بالمسحة توحي بمرض الخلايا المنجلية، لكن المسحة لوحدها ما تثبت النمط الجيني.",
        "الفحص المؤكد لأي اعتلال هيموغلوبين هو <bdi>Hb electrophoresis</bdi> (أو <bdi>HPLC</bdi>)، اللي يُظهر <bdi>HbS</bdi> مرتفع مع غياب أو نقص شديد بـ<bdi>HbA</bdi>، ويفرّق بين المرض والسمة."],
    "when_changes": ["لو كانت المسحة تظهر خلايا كروية (<bdi>spherocytes</bdi>) بدل منجلية، الفحص المؤكد يتحول لـ<bdi>osmotic fragility</bdi> ثم <bdi>EMA binding</bdi>."],
    "rule": "خلايا منجلية بالمسحة = فحص مؤكد <bdi>Hb electrophoresis</bdi>؛ خلايا كروية = <bdi>osmotic fragility/EMA binding</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1567": {"correct_letter": "D", "self_judged": False,
    "idea": "رجل ٦٦ سنة سكري، سعال وضيق تنفس، تشوش بالمكان والزمان، ضغط منخفض ونبض تنفس سريع ويوريا مرتفعة — حساب درجة <bdi>CURB-65</bdi>.",
    "clues": [("disoriented", "<bdi>Confusion</bdi> = نقطة"),
               ("BP: 80/55", "ضغط منخفض = نقطة"),
               ("RR: 33", "تسرع تنفس شديد = نقطة"),
               ("urea is 12 mmol/L", "يوريا مرتفعة = نقطة")],
    "why_correct": [
        "نحسب كل عنصر: <bdi>Confusion</bdi> (مشوش) = ١، <bdi>Urea</bdi> ١٢ (فوق ٧) = ١، <bdi>RR</bdi> ٣٣ (٣٠ فأكثر) = ١، <bdi>BP</bdi> ٨٠/٥٥ (انقباضي تحت ٩٠) = ١، العمر ٦٦ (٦٥ فأكثر) = ١.",
        "المجموع = <bdi>5</bdi>، أعلى درجة ممكنة، يعني التهاب رئوي شديد يحتاج تنويم مع تقييم العناية المركزة."],
    "when_changes": ["لو كان العمر تحت ٦٥ مع باقي العناصر نفسها، الدرجة تنزل لـ٤."],
    "rule": "<bdi>CURB-65</bdi>: كل عنصر نقطة واحدة (<bdi>Confusion, Urea&gt;7, RR≥30, BP&lt;90/60, Age≥65</bdi>)؛ السكري ليس من ضمن المعيار، مجرد تشتيت بالسؤال.",
    "comparison": None, "labs": [["Urea", "12 mmol/L", "&lt;7 mmol/L طبيعي بالمعيار"], ["RR", "33 /min", "&lt;20 طبيعي"], ["BP", "80/55 mmHg", "≥90 systolic طبيعي بالمعيار"]], "guideline_note": None},

"AS-1569": {"correct_letter": "D", "self_judged": True,
    "idea": "سكري من ١٢ سنة، بروتين كبير بالبول وكرياتينين مرتفع، بدأت <bdi>enalapril</bdi> للضغط لكن قطعته بسبب سعال — السؤال عن أفضل علاج بديل بنفس الفئة الوقائية للكلى.",
    "clues": [("type 2 diabetes", "سكري مزمن مع بروتين بول = حماية كلوية مطلوبة"),
               ("could not tolerate it because of a cough", "سعال من <bdi>ACE inhibitor</bdi>، تأثير فئة كامل"),
               ("24-hour urine protein 1500", "بروتينية واضحة تستدعي حصر <bdi>RAAS</bdi>")],
    "why_correct": [
        "سكري مع بروتينية ١٥٠٠ ملغ باليوم يحتاج حصر محور <bdi>RAAS</bdi> (<bdi>ACE inhibitor</bdi> أو <bdi>ARB</bdi>) لحماية الكلى، بس السعال من <bdi>enalapril</bdi> هو تأثير فئة <bdi>ACE inhibitors</bdi> كاملة بسبب <bdi>bradykinin</bdi>.",
        "الحل الصحيح هو التحويل لـ<bdi>Angiotensin receptor blocker</bdi>، اللي يحافظ على الحماية الكلوية بدون التسبب بنفس السعال."],
    "when_changes": ["لو كان السبب <bdi>angioedema</bdi> (مو سعال فقط)، لازم نحتاط كمان مع <bdi>ARB</bdi> لاحتمال تكرار مشابه."],
    "rule": "سعال <bdi>ACE inhibitor</bdi> = تأثير فئة كامل، حوّلي لـ<bdi>ARB</bdi>، أبدًا لا تحوّلي لـ<bdi>ACE inhibitor</bdi> ثاني ولا تجمعي الفئتين.",
    "comparison": None, "labs": [["Creatinine", "142 µmol/L", "44-115 طبيعي"], ["24h urine protein", "1500 mg/24hr", "0-150 طبيعي"]], "guideline_note": None},

"AS-1570": {"correct_letter": "A", "self_judged": False,
    "idea": "رجل ٣٠ سنة، التهاب مفصل واحد حاد، تحليل السائل الزليلي أثبت وجود بلورات وشُخّص بـ<bdi>gout</bdi> — السؤال عن شكل ولون انكسار هذي البلورات.",
    "clues": [("gout", "التشخيص معطى مباشرة بالسؤال")],
    "why_correct": [
        "بلورات <bdi>gout</bdi> هي <bdi>monosodium urate</bdi>، وشكلها <bdi>needle-shaped</bdi> (إبرية) وانكسارها <bdi>negatively birefringent</bdi> تحت الضوء المستقطب."],
    "when_changes": ["لو كان التشخيص <bdi>pseudogout</bdi> بدل <bdi>gout</bdi>، الجواب يتحول لبلورات معينية الشكل وموجبة ضعيفة الانكسار."],
    "rule": "تذكري: <bdi>gout</bdi> = إبرية وسالبة (الاثنين بحرف <bdi>N</bdi>)؛ <bdi>pseudogout</bdi> = معينية وموجبة ضعيفة.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1571": {"correct_letter": "B", "self_judged": False,
    "idea": "السؤال عن أي نتيجة زرع بول تُعتبر دليل حقيقي على <bdi>UTI</bdi>، مو مجرد وجود بكتيريا.",
    "clues": [("uti", "السؤال عن معيار التشخيص المخبري")],
    "why_correct": [
        "الزرع يكون ذا دلالة لما ينمو <bdi>عضو واحد</bdi> بعدد كبير <bdi>≥10^5 CFU/mL</bdi> من عينة بول نظيفة متوسطة التدفق.",
        "عضو واحد بعدد مرتفع يعكس عدوى مثانة حقيقية، مو تلوث من الجلد أو منطقة العجان."],
    "when_changes": ["لو كان النمو من عينة مأخوذة بقسطرة فوق العانة، أي نمو يُعتبر دليل كافٍ حتى بعدد أقل."],
    "rule": "بكتيريا بول ذات دلالة = عضو واحد بعدد مرتفع (<bdi>≥10^5</bdi>) من عينة نظيفة؛ نمو مختلط يعني تلوث، نعيد العينة.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1573": {"correct_letter": "B", "self_judged": False,
    "idea": "رجل ٥٠ سنة، <bdi>anti-HCV</bdi> موجب لكن <bdi>HCV RNA</bdi> سالب، بدون أي عامل خطر أو أعراض وإنزيمات وسونار طبيعيين — عدوى شُفيت أو إيجابية كاذبة، ما فيه عدوى فعّالة.",
    "clues": [("positive anti-HCV (ELISA)", "يعني تعرّض سابق، مو عدوى حالية بالضرورة"),
               ("Hepatitis C RNA was negative", "المفتاح — ما فيه عدوى فعّالة حاليًا")],
    "why_correct": [
        "<bdi>anti-HCV</bdi> موجب مع <bdi>HCV RNA</bdi> سالب يعني عدوى سابقة شُفيت أو إيجابية كاذبة، مو التهاب كبد C فعّال.",
        "بدون أي عامل خطر أو تعرّض حديث، وبإنزيمات كبد وسونار طبيعيين، المريض يحتاج طمأنة فقط بدون أي فحص إضافي."],
    "when_changes": ["لو كان فيه تعرّض حديث (مثل وخزة إبرة) يحتمل كونه بفترة النافذة، الجواب يتحول لإعادة <bdi>HCV RNA</bdi> بعد عدة أشهر."],
    "rule": "<bdi>Ab+/RNA-</bdi> بدون تعرّض حديث وإنزيمات طبيعية = طمأنة بدون فحوصات إضافية؛ وجود تعرّض حديث = أعيدي <bdi>RNA</bdi> لاحقًا.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1580": {"correct_letter": "C", "self_judged": False,
    "idea": "مريضة بالعناية المركزة بالتهاب رئوي حرج على <bdi>dopamine</bdi>، جلد دافئ وجاف بدون جحوظ عين وغدة طبيعية، <bdi>T3</bdi> منخفض و<bdi>TSH</bdi> منخفض و<bdi>T4</bdi> طبيعي — تغيرات تحاليل الغدة بمريض حرج مو مرض غدة حقيقي.",
    "clues": [("Intensive Care Unit with pneumonia", "مرض حرج شديد"),
               ("dopamine", "دواء يثبّط <bdi>TSH</bdi> ويساهم بالصورة"),
               ("TSH 0.1 (low)", "منخفض بدون أي علامة فرط نشاط فعلي"),
               ("T3 2 (low)", "أول وأشيع تغيّر بمرض حرج")],
    "why_correct": [
        "مريضة حرجة (عناية مركزة، التهاب رئوي، تنبيب، <bdi>dopamine</bdi>) مع <bdi>T3</bdi> منخفض و<bdi>T4</bdi> طبيعي و<bdi>TSH</bdi> منخفض، وغدة طبيعية بدون جحوظ، هذي <bdi>sick euthyroid syndrome</bdi>.",
        "انخفاض <bdi>T3</bdi> هو أشيع وأبكر تغيّر بهذي المتلازمة، و<bdi>dopamine</bdi> (كمان الستيرويدات) يثبّط <bdi>TSH</bdi> فيفسّر انخفاضه بدون فرط نشاط حقيقي."],
    "when_changes": ["لو كان <bdi>T4</bdi> و<bdi>T3</bdi> مرتفعين مع جحوظ عين وغدة متضخمة، الجواب يتحول لـ<bdi>Graves disease</bdi>."],
    "rule": "بمريض حرج بالعناية المركزة، لا تشخّصي فرط نشاط الغدة من <bdi>TSH</bdi> منخفض فقط لو <bdi>T3</bdi> منخفض و<bdi>T4</bdi> غير مرتفع.",
    "comparison": None, "labs": [["TSH", "0.1", "منخفض"], ["T3", "2", "منخفض"], ["T4", "11-14", "طبيعي"]], "guideline_note": None},

"AS-1582": {"correct_letter": "B", "self_judged": False,
    "idea": "امرأة على <bdi>prednisolone 60 mg</bdi> لمدة ٦ أسابيع مع تناقص تدريجي، بس استمرت على نفس الجرعة العالية بالغلط — وجدت ميتة بالحمام. السبب مرتبط باستمرار الجرعة العالية، مو بإيقافها.",
    "clues": [("prednisolone 60 mg", "جرعة عالية جدًا من الستيرويد"),
               ("continued the same dose", "المفتاح — استمرت عالية، ما أوقفت الدواء"),
               ("Found dead in bathroom", "وفاة مفاجئة تحتاج تفسير مباشر")],
    "why_correct": [
        "بما إنها استمرت على الجرعة (ما أوقفتها)، هذا يستبعد <bdi>adrenal crisis</bdi>، واستمرار جرعة عالية لـ٦ أسابيع يسبب احتباس صوديوم وسوائل وارتفاع ضغط.",
        "جواب المصدر يربط هذا بارتفاع ضغط مؤدي لنزيف دماغي مفاجئ (<bdi>hypertensive cerebral hemorrhage</bdi>) يفسر الوفاة المفاجئة."],
    "when_changes": ["لو كانت أوقفت الدواء بغتة بعد استخدام طويل، الجواب يتحول لـ<bdi>adrenal crisis</bdi> (هبوط ضغط وصدمة)."],
    "rule": "استمرار جرعة ستيرويد عالية = مضاعفات فرط الستيرويد (ضغط، سكر، سوائل)؛ إيقاف مفاجئ بعد استخدام طويل = أزمة كظرية.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1586": {"correct_letter": "A", "self_judged": False,
    "idea": "رجل ٣٣ سنة، تعب وحمى وتضخم غدد لمفاوية معمم وسعال لأسبوعين، يسافر كثير للشرق الأقصى، وعنده <bdi>oral candidiasis</bdi> — دلالة ضعف مناعة خلوية بشخص بالغ سليم.",
    "clues": [("generalised lymphadenopathy", "تضخم غدد معمم غير محدد"),
               ("travels frequently to Far East", "عامل خطر تعرّض"),
               ("oral candidiasis", "علامة ضعف مناعة خلوية بشخص بالغ")],
    "why_correct": [
        "شاب بالغ بدون سكري أو ستيرويدات أو مضادات حيوية، عنده <bdi>oral candidiasis</bdi> مع حمى وتعب وتضخم غدد معمم لمدة أسبوعين وتاريخ سفر وتعرّض محتمل — هذي صورة <bdi>HIV</bdi> لحد ما يُنفى.",
        "<bdi>thrush</bdi> بشخص سليم ظاهريًا يدل على ضعف بالمناعة الخلوية، والمرض الحموي غير النوعي مع تضخم الغدد يتناسق مع عدوى <bdi>HIV</bdi>."],
    "when_changes": ["لو كان فيه تاريخ تماس حيواني أو حليب غير مبستر مع حمى متموجة وألم عظمي، الجواب يتحول لـ<bdi>brucellosis</bdi>."],
    "rule": "<bdi>oral candidiasis</bdi> بشخص بالغ سليم بدون سكري أو ستيرويدات = افحصي <bdi>HIV</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1593": {"correct_letter": "B", "self_judged": True,
    "idea": "ضعف طرف علوي يمين بعد تمديد الرقبة، تصوير الرنين للدماغ طبيعي — الخلل تحت الدماغ، بالرقبة نفسها.",
    "clues": [("post neck extension", "حركة محددة فجّرت العرض — توحي بسبب رقبي"),
               ("mri brain normal", "استبعاد السبب الدماغي، الخلل بمكان آخر")],
    "why_correct": [
        "ضعف طرف علوي بعد تمديد الرقبة مع تصوير دماغ طبيعي يوجّه للرقبة نفسها، خصوصًا بوجود تنكس فقري عنقي (<bdi>cervical spondylosis</bdi>) يسبب ضيق قناة شوكية يتفاقم بالتمديد.",
        "<bdi>MRI cervical spine</bdi> هو الفحص اللي يكشف الضغط على الحبل الشوكي أو الجذور العنقية المسؤول عن هذا الضعف."],
    "when_changes": ["لو كان الضعف عابر (دقائق) مع عوامل خطر وعائية، الجواب يتحول لـ<bdi>carotid duplex</bdi> أولاً (اشتباه <bdi>TIA</bdi>)."],
    "rule": "تصوير دماغ طبيعي مع ضعف طرف بعد حركة رقبة = شوفي الرقبة بـ<bdi>MRI cervical spine</bdi>؛ ضعف عابر مع عوامل خطر وعائية = <bdi>carotid duplex</bdi>.",
    "comparison": None, "labs": None,
    "guideline_note": "هذا السؤال ما له جواب مؤكد من المصدر؛ اخترنا <bdi>MRI cervical spine</bdi> بناءً على كون الضعف مرتبط بحركة الرقبة وتصوير الدماغ طبيعي، ما يوجّه لسبب عنقي مو دماغي."},

"AS-1593B": {"correct_letter": "B", "self_judged": False,
    "idea": "رجل ٥٥ سنة، ضعف بالذراع اليسرى بدون ألم استمر ٥ دقائق وزال تمامًا، سكري ودهون مرتفعة، بدون نفخة قلبية وإيقاع جيبي طبيعي — نوبة إقفارية عابرة بمنطقة السباتي، نبحث عن المصدر القابل للعلاج.",
    "clues": [("left arm weakness without pain that lasted 5 minutes", "نوبة إقفارية عابرة كلاسيكية بمنطقة <bdi>carotid</bdi>"),
               ("initial imaging", "السؤال عن الفحص الأولي تحديدًا")],
    "why_correct": [
        "نوبة ضعف ٥ دقائق زالت تمامًا هي <bdi>TIA</bdi> بالدورة الأمامية (السباتي). مع سكري ودهون مرتفعة، تصلب الشرايين الكبيرة هو المصدر الأرجح، والسؤال يؤكد إيقاع جيبي وبدون نفخة، يعني مصدر قلبي أقل احتمالاً.",
        "<bdi>carotid duplex</bdi> هو الفحص الأولي السريع غير الباضع، واكتشاف تضيّق عرضي كبير يغيّر الخطة العلاجية (استئصال بطانة الشريان)."],
    "when_changes": ["لو كان فيه نفخة قلبية أو رجفان أذيني، الجواب يتحول لصدى القلب (<bdi>TTE</bdi> ثم <bdi>TEE</bdi>) بحثًا عن مصدر قلبي."],
    "rule": "أعراض بمنطقة السباتي + عوامل خطر تصلب شرايين + إيقاع جيبي بدون نفخة = <bdi>carotid duplex</bdi> أولاً؛ نفخة أو رجفان أذيني = صدى قلب.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1594": {"correct_letter": "B", "self_judged": False,
    "idea": "رجل ٥٥ سنة، تعب وشحوب لمدة ٣ أشهر بدون تضخم أعضاء — بالسؤال الأصلي فقر دم فقر حديد، ولازم نبحث عن مصدر نزيف هضمي خفي.",
    "clues": [("55-year-old man", "عمر الخطر لسرطان القولون"),
               ("pallor", "علامة فقر دم")],
    "why_correct": [
        "رجل ٥٥ سنة بتعب وشحوب — بالسؤال الأصلي التحاليل تظهر فقر دم فقر حديد (<bdi>MCV</bdi> منخفض، <bdi>ferritin</bdi> منخفض، <bdi>TIBC</bdi> مرتفع).",
        "نقص الحديد برجل أو امرأة بعد سن اليأس يعني نزيف هضمي خفي، ولازم نستبعد سرطان القولون؛ أفضل فحص هو المنظار (أعلى وأسفل)، لكن من الخيارات المتاحة هنا الفحص اللي يبحث عن مصدر النزيف هو <bdi>fecal occult blood</bdi>."],
    "when_changes": ["لو كان المنظار (العلوي والسفلي) من ضمن الخيارات، هو الأفضل دايمًا على فحص الدم الخفي بالبراز."],
    "rule": "فقر حديد برجل بالغ أو امرأة بعد سن اليأس = نزيف هضمي لحد إثبات العكس؛ المنظار هو الأفضل، والدم الخفي بالبراز بديل لو ما فيه منظار بالخيارات.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1595": {"correct_letter": "D", "self_judged": False,
    "idea": "نفس السيناريو السابق بالضبط، لكن هذي المرة خيار المنظار العلوي والسفلي متوفر بالخيارات — فهو الأفضل من فحص الدم الخفي.",
    "clues": [("55-year-old man", "عمر الخطر لسرطان القولون"),
               ("pallor", "علامة فقر دم فقر حديد مفترض")],
    "why_correct": [
        "نفس الرجل بتعب وشحوب — فقر الحديد المفترض بالسؤال الأصلي يعني نزيف هضمي مزمن لحد إثبات العكس، خصوصًا سرطان القولون أو المعدة.",
        "بما إن الخيارات هذي المرة تحتوي <bdi>endoscopy and colonoscopy</bdi> (رؤية مباشرة للجهاز الهضمي كامل)، هو الفحص الأفضل لتحديد مصدر النزيف، أقوى من فحص الدم الخفي."],
    "when_changes": ["لو ما كان المنظار من ضمن الخيارات، فحص الدم الخفي بالبراز يصير أفضل خيار متاح (انظري AS-1594)."],
    "rule": "وجود المنظار بالخيارات = اختاريه دائمًا على فحص الدم الخفي؛ غيابه = فحص الدم الخفي هو البديل.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1604": {"correct_letter": "C", "self_judged": False,
    "idea": "رجل ٨٥ سنة بعد سكتة دماغية كبيرة، ضعف جديد مع وذمة حليمة العصب البصري (<bdi>papilledema</bdi>)، أشعة مقطعية أظهرت تحوّل نزفي — ارتفاع ضغط داخل الجمجمة بتأثير كتلة، والسؤال عن العلاج «الأكثر حسمًا».",
    "clues": [("papilledema", "علامة ارتفاع ضغط داخل الجمجمة"),
               ("Hemorrhagic transformation", "نزيف داخل منطقة الاحتشاء"),
               ("definitive", "المفتاح — يبحث عن العلاج الحاسم مو المؤقت")],
    "why_correct": [
        "سكتة إقفارية كبيرة تحولت لنزفية، والضعف الجديد مع <bdi>papilledema</bdi> يعني تأثير كتلة وارتفاع ضغط داخل الجمجمة.",
        "السؤال يسأل عن العلاج «الأكثر حسمًا»، والعلاج الوحيد اللي يزيل تأثير الكتلة فعليًا هو الجراحة (<bdi>craniotomy and decompression</bdi>)، بينما الإجراءات الطبية الثانية مؤقتة فقط."],
    "when_changes": ["لو كان السؤال يسأل عن الخطوة «الأولية/الفورية» (مو الأكثر حسمًا)، الجواب يتحول لـ<bdi>mannitol</bdi> كجسر مؤقت."],
    "rule": "اقرئي الفعل بالسؤال: «أولي/فوري» = <bdi>mannitol</bdi>؛ «الأكثر حسمًا» = جراحة تفريغ الضغط.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1605": {"correct_letter": "C", "self_judged": False,
    "idea": "امرأة ٣٢ سنة، ألم أسفل ظهر ٣ أشهر مع تيبس صباحي ساعة تقريبًا، ألم بالركبتين والكاحلين ثنائيًا، تحديد بحركة الظهر، وإيلام فوق وتر <bdi>Achilles</bdi> — صورة التهاب مفصل محوري.",
    "clues": [("lower back pain", "ألم ظهر التهابي مزمن"),
               ("morning stiffness", "تيبس صباحي طويل تقريبًا ساعة"),
               ("limited lumbar spine movements", "تحديد حركة قطنية فعلي"),
               ("tenderness over the Achilles tendon", "التهاب وتري (<bdi>enthesitis</bdi>)")],
    "why_correct": [
        "ألم ظهر لـ٣ أشهر مع تيبس صباحي حوالي ساعة هو ألم ظهر التهابي، وإضافة تحديد حركة قطنية والتهاب مفصل طرف سفلي (ركبة وكاحل) وإيلام وتر <bdi>Achilles</bdi> (التهاب وتري) يرسم صورة التهاب مفصل محوري.",
        "غياب الطفح والقرح المخاطية والحمى يستبعد أهم المنافسين، فالتشخيص <bdi>ankylosing spondylitis</bdi>."],
    "when_changes": ["لو سبق الأعراض عدوى هضمية أو بولية مع التهاب ملتحمة، الجواب يتحول لـ<bdi>reactive arthritis</bdi>."],
    "rule": "ألم ظهر التهابي أكثر من ٣ أشهر + التهاب وتري + تحديد حركة قطنية = <bdi>ankylosing spondylitis</bdi>، حتى عند امرأة.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1606": {"correct_letter": "C", "self_judged": False,
    "idea": "امرأة ٣٨ سنة، ضيق تنفس وخفقان وتعب جديد لأسبوع، شحوب وتضخم طحال، والمسحة تظهر خلايا كروية (<bdi>spherocytes</bdi>) — بداية حادة بالغة تميل لسبب مناعي مكتسب مو وراثي.",
    "clues": [("splenomegaly", "تضخم طحال يدعم انحلال دم خارج الأوعية"),
               ("spheroytosis", "خلايا كروية — سببان محتملان، الفيصل هو العمر والبداية")],
    "why_correct": [
        "خلايا كروية بالمسحة لها سببان: <bdi>hereditary spherocytosis</bdi> أو <bdi>warm autoimmune hemolytic anemia</bdi>؛ بداية حادة جديدة عمرها أسبوع واحد بامرأة ٣٨ سنة تميل للسبب المكتسب <bdi>AIHA</bdi> مو المرض الخلقي.",
        "علاج الخط الأول لـ<bdi>warm AIHA</bdi> هو <bdi>corticosteroids</bdi>، يثبّط تدمير الطحال لكريات الدم المرتبط بأجسام <bdi>IgG</bdi> المضادة."],
    "when_changes": ["لو كان فيه تاريخ عائلي وبداية بالطفولة مع يرقان متكرر وحصوات مرارية، الجواب يتحول لـ<bdi>hereditary spherocytosis</bdi> (مو ستيرويد)."],
    "rule": "خلايا كروية ببداية حادة بالغة = <bdi>warm AIHA</bdi> لحد إثبات العكس، علاجها ستيرويد؛ تاريخ عائلي وبداية طفولة = وراثي.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1608": {"correct_letter": "C", "self_judged": False,
    "idea": "امرأة ٣٣ سنة بنوبة ربو حادة — أي علامة تحديدًا تصنف النوبة بإنها «مهددة للحياة» (<bdi>life-threatening</bdi>)، مو مجرد شديدة؟",
    "clues": [("acute exacerbation of asthma", "نوبة ربو حادة"),
               ("life-threatening", "السؤال عن معيار «مهدد للحياة» تحديدًا")],
    "why_correct": [
        "النوبة المهددة للحياة تُعرّف بوجود <bdi>أي واحدة</bdi> من: ذروة تدفق أقل من ٣٣٪ من الأفضل/المتوقع، تشبع أكسجين أقل من ٩٢٪، صدر صامت، زرقة، جهد تنفسي ضعيف، هبوط ضغط، استنفاذ أو تشوش.",
        "<bdi>ذروة تدفق ٣٠٪</bdi> أقل من حد ٣٣٪، فهي وحدها تجعل النوبة مهددة للحياة."],
    "when_changes": ["لو كان تشبع الأكسجين ٩٠٪ بدل ٩٤٪ (أقل من ٩٢٪)، هو كمان معيار مستقل مهدد للحياة."],
    "rule": "«مهدد للحياة»: ذروة تدفق أقل من ٣٣٪ أو تشبع أقل من ٩٢٪ أو صدر صامت أو استنفاذ/تشوش؛ تسرع تنفس ونبض فقط = «شديد» لا «مهدد للحياة».",
    "comparison": None, "labs": [["Peak flow", "30% best/predicted", "&lt;33% = مهدد للحياة"], ["SpO2", "94%", "فوق حد ٩٢٪ المهدد للحياة"]], "guideline_note": None},

"AS-1609": {"correct_letter": "B", "self_judged": False,
    "idea": "رجل ٥٥ سنة، ضعف بالذراع اليسرى بدون ألم استمر ٥ دقائق وزال تمامًا، سكري ودهون مرتفعة، بدون نفخة قلبية وإيقاع جيبي طبيعي — نوبة إقفارية عابرة بمنطقة السباتي، نبحث عن المصدر القابل للعلاج (نفس سؤال AS-1593B).",
    "clues": [("left arm weakness", "ضعف محدد بالذراع — منطقة السباتي"),
               ("lasted 5 minutes", "نوبة عابرة قصيرة"),
               ("asymptomatic", "زال العرض تمامًا"),
               ("initial imaging", "السؤال عن الفحص الأولي تحديدًا")],
    "why_correct": [
        "نوبة ضعف ٥ دقائق زالت تمامًا هي <bdi>TIA</bdi> بالدورة الأمامية (السباتي). مع سكري ودهون مرتفعة، تصلب الشرايين الكبيرة هو المصدر الأرجح، والسؤال يؤكد إيقاع جيبي وبدون نفخة.",
        "<bdi>carotid duplex</bdi> هو الفحص الأولي السريع غير الباضع لاكتشاف تضيّق عرضي يغيّر الخطة العلاجية."],
    "when_changes": ["لو كان فيه نفخة قلبية أو رجفان أذيني، الجواب يتحول لصدى القلب (<bdi>TTE</bdi> ثم <bdi>TEE</bdi>)."],
    "rule": "أعراض بمنطقة السباتي + عوامل خطر تصلب شرايين + إيقاع جيبي بدون نفخة = <bdi>carotid duplex</bdi> أولاً.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1610": {"correct_letter": "B", "self_judged": False,
    "idea": "رجل ٥٨ سنة سكري وضغط ومرض قلب إقفاري، ضيق تنفس مجهودي ٤ أشهر «يعيقه بشغله بس ما يوقفه»، ومرتاح تمامًا بالراحة — تصنيف درجة <bdi>NYHA</bdi>.",
    "clues": [("exertional shortness of breath", "عرض مع المجهود فقط"),
               ("interferes with his job but does not limit him", "تحديد خفيف، يقدر يكمل شغله"),
               ("at rest, he is fine", "مرتاح تمامًا بالراحة")],
    "why_correct": [
        "تصنيف <bdi>NYHA</bdi> يعتمد على مقدار النشاط اللي يسبب الأعراض. عنده ضيق تنفس مع نشاط عادي (شغله كميكانيكي) و«يعيقه بس ما يمنعه»، ومرتاح بالراحة.",
        "نشاط عادي يسبب عرض مع تحديد بسيط فقط وراحة طبيعية = <bdi>NYHA class II</bdi>."],
    "when_changes": ["لو كان النشاط العادي يمنعه تمامًا من إكمال شغله، الجواب يتحول لـ<bdi>class III</bdi>."],
    "rule": "«يقدر يكمل شغله بس يضايقه» = <bdi>II</bdi>؛ «ما يقدر يكمل نشاط عادي» = <bdi>III</bdi>؛ «أعراض بالراحة» = <bdi>IV</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1611": {"correct_letter": "A", "self_judged": False,
    "idea": "رجل ٧٠ سنة، مدخن أكثر من ٥٠ سنة، ضيق تنفس وسعال منتج مترقي ٥ أشهر مع تعب وتعرق ليلي وحمى ونزول وزن ١٠ كيلو خلال ٣ أشهر — صورة مزمنة بأعراض بائية تتجه لورم خبيث.",
    "clues": [("smoker for over 50 years", "تدخين شديد طويل المدة — عامل خطر رئيسي"),
               ("lost 10 kg", "نزول وزن كبير خلال فترة قصيرة نسبيًا")],
    "why_correct": [
        "رجل ٧٠ سنة بتدخين أكثر من ٥٠ سنة، مع ٥ أشهر من ضيق تنفس وسعال منتج مترقي، وأعراض بائية (تعب، تعرق ليلي، حمى) ونزول وزن ١٠ كيلو خلال ٣ أشهر تتناسق مع <bdi>lung carcinoma</bdi>.",
        "المسار الزمني المزمن ونزول الوزن الكبير بمدخن شره مسن يرجّح الورم على أي سبب معدي أو تحسسي."],
    "when_changes": ["لو كان المسار أيام قليلة بحمى حادة وسعال منتج فقط بدون نزول وزن، الجواب يتحول لـ<bdi>pneumonia</bdi>."],
    "rule": "مدخن شره مسن + أشهر من سعال وضيق تنفس + نزول وزن كبير = <bdi>lung carcinoma</bdi> لحد إثبات العكس.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1624": {"correct_letter": "D", "self_judged": False,
    "idea": "رجل مسن بدون تاريخ مرضي، سكتة نزفية عولجت، وبعد أسبوع صار عدم تناسق بالوجه واضطراب كلام مع احتشاء دماغي يسار جديد بالتصوير — مضاعفة متأخرة كلاسيكية بعد نزيف تحت العنكبوتية.",
    "clues": [("hemorrhagic stroke", "النزيف الأصلي"),
               ("after 1 week", "توقيت كلاسيكي لمضاعفة متأخرة"),
               ("left cerebral infarction", "احتشاء جديد، مو تكرار نزيف")],
    "why_correct": [
        "سكتة نزفية وبعدها بأسبوع تقريبًا عجز عصبي جديد مع احتشاء دماغي جديد هو نقص تروية متأخر بسبب تشنج الأوعية (<bdi>vasospasm</bdi>)، أشيع مضاعفة لنزيف تحت العنكبوتية.",
        "تشنج الأوعية يبلغ ذروته حوالي اليوم ٤ إلى ١٤ بعد النزيف ويضيّق الشرايين الدماغية بما يكفي لإحداث احتشاء."],
    "when_changes": ["لو كان العجز الجديد مصحوب بنزيف دماغي طازج بالتصوير (مو احتشاء)، الجواب يتحول لإعادة نزيف (<bdi>rebleeding</bdi>)."],
    "rule": "عجز جديد بعد نزيف تحت العنكبوتية بأيام ٤-١٤ مع احتشاء بالتصوير = تشنج الأوعية؛ مع نزيف طازج = إعادة نزيف.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1625": {"correct_letter": "A", "self_judged": False,
    "idea": "مريض يفهم الكلام تمامًا، لكن ما يقدر يكتب، ما يتذكر الكلمات، وما يميز اليمين من اليسار — مجموعة أعراض تحدد الفص المصاب بدقة.",
    "clues": [("understand what is being told", "الفهم سليم، يستبعد <bdi>Wernicke</bdi>"),
               ("can't write", "<bdi>agraphia</bdi>"),
               ("can't remember words", "صعوبة تسمية (<bdi>anomia</bdi>)"),
               ("can't know left and right", "تشوش يمين-يسار")],
    "why_correct": [
        "الفهم سليم (ليس <bdi>receptive aphasia</bdi>)، و<bdi>agraphia</bdi> (عدم القدرة على الكتابة) مع تشوش يمين-يسار هي علامات أساسية بمتلازمة <bdi>Gerstmann</bdi> (مع <bdi>finger agnosia</bdi> و<bdi>acalculia</bdi>)، وصعوبة تذكر الكلمات (<bdi>anomia</bdi>) تتناسق كمان مع إصابة <bdi>angular gyrus</bdi>.",
        "كل هذي العلامات توضع تشريحيًا بالفص الجداري (<bdi>parietal lobe</bdi>) المسيطر (غالبًا الأيسر)."],
    "when_changes": ["لو كان المريض ما يفهم الكلام المسموع أصلاً، الجواب يتحول للفص الصدغي (<bdi>Wernicke area</bdi>)."],
    "rule": "<bdi>agraphia</bdi> + تشوش يمين-يسار (± <bdi>finger agnosia, acalculia</bdi>) = متلازمة <bdi>Gerstmann</bdi> = الفص الجداري المسيطر.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1632": {"correct_letter": "A", "self_judged": False,
    "idea": "رجل ٢٨ سنة، ألم مفاصل وتيبس صباحي وقرح بالفم لشهرين، التهاب فعّال بالرسغين ومفصل <bdi>PIP</bdi> الثاني، <bdi>ESR</bdi> مرتفع مع <bdi>CRP</bdi> شبه طبيعي و<bdi>C4</bdi> منخفض — صورة <bdi>SLE</bdi>؛ السؤال عن الدواء اللي يقلل النكسات والخطر الوعائي.",
    "clues": [("mouth ulcers", "قرح فموية — من معايير <bdi>SLE</bdi>"),
               ("Complement C4 0.1", "مكمل منخفض يدعم نشاط <bdi>SLE</bdi>"),
               ("remission and vascular risk", "المفتاح — الدواء اللي يفيد الاثنين معًا")],
    "why_correct": [
        "التهاب مفاصل مع قرح فموية و<bdi>ESR</bdi> مرتفع مع <bdi>CRP</bdi> شبه طبيعي و<bdi>C4</bdi> منخفض يوجه لـ<bdi>systemic lupus erythematosus</bdi>.",
        "<bdi>hydroxychloroquine</bdi> هو الدواء الأساسي لكل مريضة <bdi>SLE</bdi> بدون مانع: يقلل النكسات ويساعد على استمرار الهدأة، وكمان يقلل الخطر التخثري والوعائي ويحسّن البقيا — بالضبط ما يسأل عنه السؤال."],
    "when_changes": ["لو ظهر ارتفاع كرياتينين وبروتينية (إصابة كلوية)، الجواب يتحول لـ<bdi>mycophenolate mofetil</bdi> مع ستيرويد."],
    "rule": "كل مريضة <bdi>SLE</bdi> تاخذ <bdi>hydroxychloroquine</bdi> دايمًا — هو الوحيد اللي يقلل الخطر الوعائي ويحسّن البقيا بين هذي الخيارات.",
    "comparison": None, "labs": [["ESR", "55", "2-10 (رجال) طبيعي"], ["CRP", "12", "&lt;8.2 mg/L طبيعي"], ["C4", "0.1", "0.15-0.45 g/L طبيعي"]], "guideline_note": None},

"AS-1633": {"correct_letter": "D", "self_judged": False,
    "idea": "مريض مسن على هيبارين وريدي، جلطة وريدية عميقة جديدة باليوم السادس بعد العملية، وصفائح انخفضت لـ٧٥ — صورة <bdi>HIT</bdi> الكلاسيكية.",
    "clues": [("IV heparin", "الدواء المسبب"),
               ("6 days post-operatively", "توقيت كلاسيكي لـ<bdi>HIT</bdi> (٥-١٠ أيام)"),
               ("Platelet count is 75", "انخفاض صفائح نموذجي لـ<bdi>HIT</bdi>")],
    "why_correct": [
        "جلطة جديدة مع هبوط صفائح لـ٧٥ باليوم السادس من الهيبارين هي <bdi>heparin induced thrombocytopenia</bdi> — حالة تخثرية مناعية رغم انخفاض الصفائح.",
        "العلاج: إيقاف كل أشكال الهيبارين فورًا والبدء بمميع غير هيباريني، وأشيعه <bdi>direct thrombin inhibitor</bdi> (<bdi>argatroban</bdi> أو <bdi>bivalirudin</bdi>)."],
    "when_changes": ["لو كان انخفاض الصفائح خلال أول يوم أو يومين من الهيبارين بدون جلطة جديدة، غالبًا سبب غير مناعي حميد، مو <bdi>HIT</bdi>."],
    "rule": "هبوط صفائح بعد ٥-١٠ أيام من الهيبارين ± جلطة جديدة = <bdi>HIT</bdi>: أوقفي كل الهيبارين وابدئي مميع غير هيباريني (<bdi>direct thrombin inhibitor</bdi>)، بدون نقل صفائح.",
    "comparison": None, "labs": [["Platelets", "75 ×10⁹/L", "150-400 طبيعي"]], "guideline_note": None},

"AS-1657": {"correct_letter": "B", "self_judged": True,
    "idea": "السؤال عن الفحص المؤكد الوحيد لـ<bdi>iron deficiency anemia (IDA)</bdi>، من بين ٣ خيارات فقط.",
    "clues": [("SINGLE CONFIRMATORY TEST", "يبحث عن أفضل فحص دم مفرد يؤكد التشخيص"),
               ("IDA", "التشخيص المطلوب تأكيده")],
    "why_correct": [
        "المعيار الذهبي الحقيقي لتأكيد <bdi>IDA</bdi> هو صبغة الحديد بنخاع العظم (غير متاحة هنا كخيار)، لكن من بين الخيارات المتاحة، <bdi>low ferritin</bdi> هو أقرب فحص دم مفرد لتأكيد التشخيص عمليًا، لأن انخفاضه شبه قاطع لنقص الحديد.",
        "<bdi>high TIBC</bdi> و<bdi>low serum iron</bdi> يساعدان بس أقل تحديدًا من الفيريتين لوحده، لأن حالات ثانية (<bdi>anemia of chronic disease</bdi>) ممكن تغيّر هذي القيم بدون نقص حديد حقيقي."],
    "when_changes": ["لو كان «صبغة الحديد بنخاع العظم» (<bdi>bone marrow iron stain</bdi>) من ضمن الخيارات، هو المعيار الذهبي الحقيقي ويُفضّل دايمًا."],
    "rule": "المعيار الذهبي الحقيقي = نخاع العظم (نادرًا لازم)؛ من بين فحوصات الدم، الفيريتين المنخفض هو الأقرب لتأكيد <bdi>IDA</bdi>.",
    "comparison": None, "labs": None,
    "guideline_note": "هذا السؤال ما له جواب مؤكد من المصدر، والمصدر نفسه يوضح إن المعيار الذهبي الحقيقي (نخاع العظم) غير مذكور بالخيارات؛ اخترنا <bdi>low ferritin</bdi> كأقرب فحص دم متاح لتأكيد التشخيص."},

"AS-1657B": {"correct_letter": "D", "self_judged": False,
    "idea": "فقر دم صغير الكريات (<bdi>microcytic</bdi>)، والسؤال عن الفحص «الأكثر حسمًا» (<bdi>most definitive</bdi>) لتحديد السبب الكامن — صياغة مختلفة عن «الأفضل/الأولي».",
    "clues": [("Most definitive test", "المفتاح — يطلب المعيار الذهبي مو الفحص الأولي"),
               ("microcytic anemia", "فقر دم صغير الكريات، أسبابه متعددة")],
    "why_correct": [
        "السؤال يحدد «الأكثر حسمًا» لتشخيص سبب فقر الدم صغير الكريات، و<bdi>bone marrow</bdi> بصبغة الحديد يُظهر مباشرة غياب مخزون الحديد (نقص حديد)، أو مخزون طبيعي/مرتفع (مرض مزمن)، أو <bdi>ring sideroblasts</bdi> (فقر دم جيبي).",
        "هو المعيار الذهبي رغم كونه باضع ونادر الحاجة عمليًا، لكن «الأكثر حسمًا» يشير له تحديدًا."],
    "when_changes": ["لو كان السؤال يسأل عن الفحص «الأولي/الأفضل» (مو الأكثر حسمًا)، الجواب يتحول لـ<bdi>serum ferritin</bdi>."],
    "rule": "«أولي/أفضل» = فيريتين؛ «الأكثر حسمًا/معيار ذهبي» = نخاع العظم بصبغة الحديد.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1658": {"correct_letter": "B", "self_judged": False,
    "idea": "حالة سريرية مباشرة لمرض الخلايا المنجلية — أي هيموغلوبين لو غاب بتحليل الكهربائي يؤكد التشخيص؟",
    "clues": [("SCD", "التشخيص الأساسي"), ("absent", "المفتاح — غياب أي هيموغلوبين يؤكد المرض")],
    "why_correct": [
        "بمرض الخلايا المنجلية (<bdi>HbSS</bdi>)، جين السلسلة البيتا ينتج <bdi>HbS</bdi> فقط، فـ<bdi>HbA</bdi> الطبيعي البالغ يكون غائبًا تمامًا، مع <bdi>HbS</bdi> هو السائد وأحيانًا ارتفاع بسيط بـ<bdi>HbF</bdi>.",
        "غياب <bdi>HbA</bdi> هو اللي يفرّق المرض عن سمة المرض (<bdi>trait</bdi>) اللي فيها <bdi>HbA</bdi> موجود مع <bdi>HbS</bdi>."],
    "when_changes": ["لو كان الهيموغلوبين الغائب هو <bdi>HbS</bdi> نفسه، هذا يستبعد التشخيص أصلاً."],
    "rule": "وجود <bdi>HbA</bdi> و<bdi>HbS</bdi> معًا = سمة منجلية؛ غياب <bdi>HbA</bdi> تمامًا مع <bdi>HbS</bdi> سائد = مرض الخلايا المنجلية.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1659": {"correct_letter": "C", "self_judged": False,
    "idea": "امرأة ٣٥ سنة، تعب وضعف مفاجئ بدون يرقان أو عدوى أو دواء جديد، بدون تضخم غدد أو طحال، شبكيات مرتفعة وبيليروبين غير مباشر مرتفع و<bdi>haptoglobin</bdi> منخفض وصفائح طبيعية — انحلال دم مكتسب حاد.",
    "clues": [("no jaundice", "ما فيه يرقان ظاهر رغم الانحلال"),
               ("no lymphadenopathy or splenomegaly", "ما فيه تضخم أعضاء يوحي بمرض مزمن"),
               ("Reticulocyte count: Elevated", "نخاع يعوّض بإنتاج خلايا جديدة"),
               ("Haptoglobin: Decreased", "تأكيد انحلال دم داخل الأوعية/خارجها")],
    "why_correct": [
        "انخفاض الهيموغلوبين مع ارتفاع الشبكيات والبيليروبين غير المباشر وانخفاض <bdi>haptoglobin</bdi> يؤكد انحلال دم، والصفائح الطبيعية تستبعد عملية استهلاكية (<bdi>DIC/TTP</bdi>).",
        "بداية مفاجئة بامرأة بالغة سليمة بدون تضخم طحال أو دواء جديد أو عدوى تناسب سبب مناعي مكتسب — <bdi>autoimmune hemolytic anemia</bdi>، وتُؤكد بفحص <bdi>Coombs</bdi> المباشر الموجب."],
    "when_changes": ["لو كان فيه يرقان مزمن وحصوات مرارية متعددة، الجواب يتحول لـ<bdi>hereditary spherocytosis</bdi> (انظري AS-1660)."],
    "rule": "علامات الانحلال (شبكيات مرتفعة، بيليروبين غير مباشر مرتفع، <bdi>haptoglobin</bdi> منخفض) + بداية مفاجئة بدون تضخم طحال = <bdi>AIHA</bdi>؛ صفائح منخفضة = <bdi>DIC/TTP</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1660": {"correct_letter": "B", "self_judged": False,
    "idea": "نفس صورة الانحلال السابقة، لكن هذي المرة مع يرقان وحصوات مرارية متعددة بالسونار — دليل على انحلال دم مزمن طويل الأمد، مو حديث.",
    "clues": [("jaundice", "يرقان ظاهر هذي المرة"),
               ("multiple gallstones", "المفتاح — حصوات صبغية تحتاج سنوات من الانحلال لتتكون")],
    "why_correct": [
        "علامات الانحلال موجودة (شبكيات وبيليروبين مرتفعين، <bdi>haptoglobin</bdi> منخفض) مع صفائح طبيعية.",
        "الدليل الحاسم هو الحصوات المرارية المتعددة مع اليرقان: الحصوات الصبغية تتكون فقط بعد انحلال دم طويل الأمد، وهذا يوجه لخلل خلقي بغشاء الكرية الحمراء (<bdi>hereditary spherocytosis</bdi>) مو عملية مكتسبة حديثة."],
    "when_changes": ["لو ما فيه حصوات مرارية وكانت البداية مفاجئة بدون تاريخ طويل، الجواب يرجع لـ<bdi>AIHA</bdi> (انظري AS-1659)."],
    "rule": "حصوات صفراوية صبغية بشاب = انحلال دم مزمن = فكّري وراثي (<bdi>hereditary spherocytosis</bdi>)؛ أكدي بفحص <bdi>Coombs</bdi> السالب.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1669": {"correct_letter": "A", "self_judged": False,
    "idea": "امرأة ٥٠ سنة، اكتئاب، تبول وعطش مفرط شهرين، عندها نقائل رئوية من سرطان ثدي — صوديوم مرتفع وبول مخفف جدًا = فقدان ماء حر من الكلية.",
    "clues": [("excessive urination and thirst", "عطش وتبول معًا — يوحي بـ<bdi>DI</bdi>"),
               ("lung metastases", "سبب محتمل لتلف الغدة النخامية الخلفية"),
               ("Sodium 150", "صوديوم مرتفع فعليًا"),
               ("Osmolality 110", "بول مخفف جدًا رغم الجفاف")],
    "why_correct": [
        "تبول وعطش مع صوديوم ١٥٠ وبول مخفف جدًا (أسمولالية ١١٠) يعني الكلية تفقد ماء حر كان المفروض تحتفظ فيه — <bdi>diabetes insipidus</bdi>.",
        "تاريخ سرطان ثدي مع نقائل رئوية يوجه لسبب مركزي: نقائل بالغدة النخامية الخلفية أو ساقها توقف إفراز <bdi>ADH</bdi>؛ الثدي والرئة أشيع الأسباب النقيلية لـ<bdi>central DI</bdi>."],
    "when_changes": ["لو كان الصوديوم منخفض أو طبيعي مع بول مخفف، الجواب يتحول لـ<bdi>psychogenic polydipsia</bdi> (الاكتئاب كان تشتيت)."],
    "rule": "بول مخفف + صوديوم مرتفع = <bdi>DI</bdi>؛ بول مخفف + صوديوم منخفض = شرب ماء زائد.",
    "comparison": None, "labs": [["Sodium", "150 mmol/L", "134-146 طبيعي"], ["Urine osmolality", "110 mOsm/kg", "280-910 طبيعي"]], "guideline_note": None},

"AS-1670": {"correct_letter": "D", "self_judged": False,
    "idea": "رجل ٦٠ سنة ضغط، ألم صدر خلف القص مفاجئ وضيق تنفس وخفقان ساعتين، تخطيط قلب يُظهر ارتفاع <bdi>ST</bdi> بالجدار السفلي، وتاريخ سكتة إقفارية قبل شهرين — احتشاء حاد يحتاج إعادة ترويه، لكن التحلل الخثري ممنوع.",
    "clues": [("non-hemorrhagic stroke 2 months ago", "مانع مطلق للتحلل الخثري"),
               ("ST-segment elevation in II, III, aVF", "احتشاء جداري سفلي")],
    "why_correct": [
        "ارتفاع <bdi>ST</bdi> بالمشتقات <bdi>II, III, aVF</bdi> مع ألم صدر ساعتين هو احتشاء سفلي حاد (<bdi>STEMI</bdi>) يحتاج إعادة ترويه عاجلة.",
        "<bdi>PCI</bdi> الأولية هي الخيار المفضل دايمًا، وهنا هي الخيار الوحيد أصلاً لأن السكتة الإقفارية قبل شهرين (خلال ٣ أشهر) مانع مطلق للتحلل الخثري."],
    "when_changes": ["لو ما فيه تاريخ سكتة أو أي مانع، <bdi>PCI</bdi> تبقى الأفضل، والتحلل الخثري يُستخدم بس لو <bdi>PCI</bdi> غير متاحة بالوقت المناسب."],
    "rule": "سكتة إقفارية خلال ٣ أشهر = مانع مطلق للتحلل الخثري؛ الخيار يصير <bdi>PCI</bdi> دايمًا بغض النظر عن التوفر.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-1671": {"correct_letter": "B", "self_judged": False,
    "idea": "بالغ بألم ركبة ورسغ وكاحل لـ٥ أسابيع تقريبًا، بعد عدوى تنفسية علوية قبل أسابيع، الركبة متورمة، والتحاليل وتحليل السائل الزليلي طبيعيان تمامًا — التهاب عقيم بعد عدوى فيروسية، مو عدوى فعلية بالمفصل.",
    "clues": [("history of URTI a few weeks back", "عدوى فيروسية سابقة — تسبق الالتهاب المفصلي"),
               ("Synovial analysis is normal", "المفتاح — يستبعد العدوى الفعلية بالمفصل")],
    "why_correct": [
        "التهاب مفاصل متعدد بعد عدوى تنفسية علوية حديثة مع تحاليل وسائل زليلي طبيعيين تمامًا يناسب التهاب مفصلي عقيم تالٍ للعدوى الفيروسية (<bdi>toxic/reactive synovitis</bdi>)، مو عدوى فعلية بالمفصل.",
        "سائل زليلي طبيعي (عدد كريات بيضاء منخفض) يستبعد <bdi>septic arthritis</bdi> تمامًا، اللي يحتاج عدد كريات بيضاء عالي جدًا وغالبًا مفصل واحد حار أحمر مع حمى."],
    "when_changes": ["لو كان المفصل حار أحمر مع حمى وتحاليل التهاب مرتفعة وسائل زليلي صديدي، الجواب يتحول لـ<bdi>septic arthritis</bdi>."],
    "rule": "تحاليل وسائل زليلي طبيعيان بعد عدوى فيروسية حديثة = التهاب عقيم تالٍ للعدوى، أبدًا لا تشخّصي عدوى فعلية بالمفصل بدون سائل التهابي.",
    "comparison": None, "labs": None, "guideline_note": None},
}

WHY_WRONG = {

"AS-1516": {
    "A": "<bdi>Phenobarbital</bdi> دواء قديم عالي الأعراض الجانبية، ومو الخط الثاني المعتمد لـ<bdi>myoclonic seizures</bdi>.",
    "B": "<bdi>Lamotrigine</bdi> جيد لنوبات <bdi>focal/GTC</bdi>، لكن ممكن يسوّئ <bdi>myoclonus</bdi> بعض المرات، فمو الخيار الآمن هنا.",
    "D": "<bdi>Ethosuximide</bdi> يُستخدم بس لـ<bdi>absence seizures</bdi>، مو لـ<bdi>myoclonic seizures</bdi>."},

"AS-1521": {
    "A": "<bdi>Free wall rupture</bdi> يسبب دكاك قلبي (هبوط ضغط، ارتفاع الوريد الوداجي، أصوات مكتومة، توقف قلب) بدون أي نفخة جديدة.",
    "C": "<bdi>Pseudoaneurysm</bdi> تمزق محدود بالجدار، غالبًا صامت أو بنفخة تردد بالصدى، ما يعطي نفخة شاملة انقباض تتجه لحافة القص اليمنى."},

"AS-1524": {
    "A": "هذي أدوية فموية مزمنة لتعديل المرض؛ حاصر بيتا ما يبدأ أثناء التدهور الحاد، و<bdi>propranolol</bdi> أصلاً مو دواء قصور قلب معتمد.",
    "B": "<bdi>furosemide</bdi> الفموي بطيء وامتصاصه ضعيف بالاحتقان المعوي؛ والموسّع الوريدي المناسب هو النترات لو كان الضغط مرتفع، مو <bdi>hydralazine</bdi>.",
    "D": "التنبيب يكون لو فشل التنفس غير الباضع أو تراجع الوعي أو استنفاذ المريض؛ هنا ما فيه هذي العلامات، فهو مو الخطوة الأولى."},

"AS-1529": {
    "A": "<bdi>furosemide</bdi> يقلل الحمل القبلي اللي القلب المدكوك محتاجه، ويسوّئ الهبوط؛ الدكاك يُدار بالسوائل والتصريف، مو بالمدرات.",
    "C": "تكثيف الديال يعالج الانصباب اليوريمي بمريض مستقر؛ هنا المريض غير مستقر، وسحب السوائل بالديال ممكن يسبب انهيار مفاجئ، فالتصريف أولاً."},

"AS-1535": {
    "B": "<bdi>ultrasound</bdi> هو الفحص الأولي المفضل لتشخيص الكبد الدهني والتشمع والاستسقاء وارتفاع ضغط البوابة، لكن مو المعيار الذهبي اللي يستهدفه الجواب.",
    "C": "<bdi>CT</bdi> البطني يضيف تعرض للإشعاع والصبغة بدون ما يفيد بتشخيص الدهون الكبدية أو التشمع؛ يُستخدم لتوصيف كتلة &gt;١ سم تُكتشف بالسونار."},

"AS-1537": {
    "B": "<bdi>bisoprolol</bdi> حاصر بيتا ثاني، والمريض أصلاً على <bdi>metoprolol</bdi>؛ إضافته تكرار لنفس الفئة، وهو مناسب فقط لو لم يكن على حاصر بيتا أساسًا.",
    "C": "<bdi>verapamil</bdi> حاصر كالسيوم سلبي التقلص يسوّئ <bdi>HFrEF</bdi>، وممنوع بهذا المرض.",
    "D": "<bdi>diltiazem</bdi> كمان حاصر كالسيوم سلبي التقلص من فئة غير <bdi>dihydropyridine</bdi>، ممنوع بكسر قذفي منخفض."},

"AS-1540": {
    "A": "<bdi>Lasix</bdi> يُضاف بمتلازمة تحلل الورم بس بعد ترطيب وريدي كافٍ للحفاظ على إخراج البول أو علاج فرط السوائل؛ ما يصحح الفوسفات، وما فيه قلة بول أو فرط سوائل مذكور هنا.",
    "B": "<bdi>Thiazide</bdi> يخفض الكالسيوم بالبول ويُستخدم لفرط كالسيوم البول والحصوات؛ ما له دور بمتلازمة تحلل الورم وممكن يسوّئ الصورة بإنقاص حجم السوائل.",
    "C": "<bdi>Allopurinol</bdi> يمنع تكوّن حمض يوريك جديد، وهو خيار الوقاية أو فرط حمض اليوريك؛ هنا حمض اليوريك مذكور بوضوح إنه غير مرتفع، فما يعالج الخلل الحالي."},

"AS-1541": {
    "A": "<bdi>seronegative RA</bdi> تعفي مفاصل <bdi>DIP</bdi> وتصيب <bdi>MCP/PIP/wrist</bdi> بتورم زليلي ناعم وتيبس صباحي أطول من ٣٠ دقيقة، غالبًا مع ارتفاع <bdi>ESR/CRP</bdi>؛ ما فيه شي من هذا هنا.",
    "C": "<bdi>Polyarticular gout</bdi> يظهر كنوبات حادة متكررة بمفاصل حمراء ساخنة شديدة الألم مع إنزيمات التهاب مرتفعة وحمض يوريك عالي، والعقد التوفية تجي بعد سنوات نوبات؛ هذا نمط عقد عظمية غير مؤلمة بدون نوبات وبتحاليل طبيعية.",
    "D": "<bdi>Reactive arthritis</bdi> التهاب مفصل حاد غير متماثل غالبًا بالأطراف السفلية بعد عدوى هضمية أو بولية، غالبًا مع التهاب أوتار أو ملتحمة؛ مو نمط <bdi>DIP</bdi> متماثل عمره ٣ سنين."},

"AS-1542": {
    "A": "<bdi>seronegative RA</bdi> تعفي مفاصل <bdi>DIP</bdi> نموذجيًا وتعطي التهاب زليلي متماثل بـ<bdi>MCP/wrist</bdi> مع تيبس صباحي طويل وإنزيمات التهاب واضحة الارتفاع؛ قيمة <bdi>RF</bdi> «حدية» لوحدها ما تحوّل صورة <bdi>OA</bdi> إلى <bdi>RA</bdi>."},

"AS-1547": {
    "B": "<bdi>Ischemic mitral regurgitation</bdi> تصير بمريض أكبر سنًا بعد احتشاء أو مرض شرايين تاجية؛ ما فيه تاريخ احتشاء هنا.",
    "C": "<bdi>Functional mitral regurgitation</bdi> تصير مع توسع البطين الأيسر أو قصور قلب؛ هذا شاب سليم بدون أي مرض قلبي معروف.",
    "D": "<bdi>Rheumatic mitral regurgitation</bdi> تحتاج تاريخ حمى رثوية أو منطقة موبوءة؛ ما فيه ذكر لذلك هنا."},

"AS-1551": {
    "A": "<bdi>MRI brain</bdi> مفيد لاحقًا للبحث عن سبب تشريحي، لكن ما يُطلب قبل ضبط النوبة؛ بالسياق الحاد أو الرضحي، <bdi>CT</bdi> هو فحص التصوير المفضل.",
    "B": "<bdi>Continuous EEG</bdi> يُطلب لو المريض ما رجع وعيه بعد توقف النوبة (اشتباه <bdi>non-convulsive status</bdi>) أو مخدّر/مرخي؛ هنا مو الخطوة قبل دواء الخط الثاني.",
    "C": "<bdi>Lumbar puncture</bdi> صحيح لو فيه حرارة أو تيبس رقبة أو اشتباه عدوى جهاز عصبي مركزي، وبس بعد تصوير يستبعد ارتفاع الضغط داخل الجمجمة؛ ما فيه شي يوحي بعدوى هنا."},

"AS-1554": {
    "A": "عدوى حادة تحتاج <bdi>IgM anti-HBc</bdi> موجب، غالبًا مع إنزيمات مرتفعة بشدة؛ <bdi>IgM</bdi> هنا سالب والإنزيمات طبيعية.",
    "C": "التحصين يعطي <bdi>anti-HBs</bdi> فقط، مع <bdi>HBsAg</bdi> و<bdi>anti-HBc</bdi> سالبين؛ هذا المريض <bdi>HBsAg</bdi> موجب.",
    "D": "الشفاء يتطلب <bdi>HBsAg</bdi> سالب مع <bdi>anti-HBs</bdi> و<bdi>anti-HBc IgG</bdi> موجبين؛ استمرار <bdi>HBsAg</bdi> موجب يستبعد الشفاء."},

"AS-1569": {
    "A": "<bdi>Beta blocker</bdi> لا يملك نفس الحماية الكلوية المباشرة ضد بروتينية السكري، وممكن يخفي أعراض نقص السكر؛ مناسب لو فيه مؤشر قلبي إضافي بس مو الخيار الأول هنا.",
    "B": "<bdi>Thiazide diuretic</bdi> يفيد كإضافة لضبط الضغط لكن ما يستهدف البروتينية ولا يحمي الكلى بنفس آلية حصر <bdi>RAAS</bdi>.",
    "C": "<bdi>Calcium channel blocker</bdi> خيار إضافي جيد لضبط الضغط، لكن ما يقلل البروتينية بنفس فعالية حصر <bdi>RAAS</bdi>، فما يحل محل <bdi>ACEi/ARB</bdi>."},

"AS-1556": {
    "A": "<bdi>Beta-blocker</bdi> يحصر العقدة الأذينية البطينية، وبالرجفان المُسبق الاستثارة (<bdi>pre-excited AF</bdi>) ممكن يشجّع التوصيل عبر المسار الإضافي؛ هو مناسب لضبط النبض برجفان عادي بدون <bdi>WPW</bdi>.",
    "C": "<bdi>Digoxin</bdi> يحصر العقدة الأذينية البطينية وممكن يقصّر فترة استعصاء المسار الإضافي، فهو ممنوع بـ<bdi>WPW</bdi>؛ مناسب لضبط نبض رجفان مع قصور قلب بدون <bdi>WPW</bdi>.",
    "D": "<bdi>Verapamil</bdi> حاصر كالسيوم غير <bdi>dihydropyridine</bdi> (حاصر للعقدة الأذينية البطينية)، ممنوع بـ<bdi>WPW</bdi> مع رجفان لأنه ممكن يسبب <bdi>VF</bdi>؛ مناسب لضبط نبض رجفان عادي أو لـ<bdi>SVT</bdi>."},

"AS-1562": {
    "B": "<bdi>Osmotic fragility test</bdi> هو الفحص الأولي لـ<bdi>hereditary spherocytosis</bdi> (خلايا كروية بالمسحة)، ويُؤكد بـ<bdi>EMA binding</bdi>؛ ما يحدد نوع الهيموغلوبين غير الطبيعي.",
    "C": "<bdi>Bone marrow</bdi> يُستخدم للاشتباه بلوكيميا أو فشل نقي (نقص خلايا شامل أو خلايا بلاستية)؛ باضع وغير مستخدم لتشخيص مرض الخلايا المنجلية."},

"AS-1567": {
    "A": "درجة <bdi>٢</bdi> تعني إن عنصرين فقط موجودين؛ هنا كل العناصر الخمسة موجودة.",
    "B": "درجة <bdi>٣</bdi> تعني غياب عنصرين؛ التشوش واليوريا المرتفعة وتسرع التنفس وانخفاض الضغط والعمر ٦٥ فأكثر كلها موجودة.",
    "C": "درجة <bdi>٤</bdi> تفوّت عنصر واحد، غالبًا العمر (٦٦ يُحسب) أو الضغط (٨٠/٥٥ يُحسب كنقطة واحدة)."},

"AS-1570": {
    "B": "الشكل الإبري يطابق <bdi>urate</bdi>، لكن الانكسار الموجب الضعيف يخص بلورات <bdi>CPPD</bdi> (<bdi>pseudogout</bdi>)، مو <bdi>gout</bdi>.",
    "C": "الشكل المعيني يخص <bdi>CPPD</bdi>، وهي انكسارها موجب ضعيف مو سالب؛ هذا خيار يخلط بين الصفتين.",
    "D": "هذي بلورات <bdi>calcium pyrophosphate</bdi>، وهي الجواب الصحيح لو التشخيص <bdi>pseudogout</bdi>."},

"AS-1571": {
    "A": "نمو بكتيريا مختلطة بالزرع غالبًا يعني تلوث العينة أثناء الأخذ؛ الخطوة الصحيحة إعادة عينة بطريقة صحيحة، مو تشخيص <bdi>UTI</bdi>."},

"AS-1573": {
    "A": "<bdi>Liver fibroscan</bdi> يُستخدم لتقييم درجة التليف بعدوى <bdi>HCV</bdi> مزمنة مؤكدة (<bdi>RNA</bdi> موجب) قبل العلاج؛ ما فيه عدوى فعّالة هنا تحتاج تقييم.",
    "C": "<bdi>Triphasic CT scan</bdi> يُستخدم لتوصيف كتلة كبدية مشتبهة أو سرطان كبد، غالبًا بمريض تشمع؛ كبده طبيعي بالسونار.",
    "D": "إعادة <bdi>HCV RNA</bdi> بعد ٦ أشهر مناسبة لو فيه تعرّض حديث أو خطر مستمر؛ هذا الرجل بدون أي تاريخ تعرّض وإنزيماته طبيعية."},

"AS-1580": {
    "A": "<bdi>Graves disease</bdi> تحتاج <bdi>TSH</bdi> منخفض مع <bdi>T4/T3</bdi> مرتفعين وتضخم غدة منتشر وجحوظ عين؛ هنا <bdi>T3</bdi> منخفض والغدة طبيعية وما فيه جحوظ.",
    "B": "<bdi>Subacute thyroiditis</bdi> تعطي غدة مؤلمة ومتضخمة بعد مرض فيروسي مع <bdi>T4</bdi> مرتفع و<bdi>TSH</bdi> منخفض وارتفاع <bdi>ESR</bdi>؛ هنا الرقبة طبيعية و<bdi>T3</bdi> منخفض.",
    "D": "<bdi>Hashimoto thyroiditis</bdi> هي قصور غدة أساسي بـ<bdi>TSH</bdi> مرتفع و<bdi>T4</bdi> منخفض، غالبًا مع تضخم غدة؛ هنا <bdi>TSH</bdi> منخفض مو مرتفع."},

"AS-1582": {
    "A": "<bdi>Perforated duodenal ulcer</bdi> هو المنافس الرئيسي لأن الستيرويدات تخفي التهاب الصفاق، لكن الانثقاب غالبًا يسبق بألم بطني شديد واضح، مو موت مفاجئ غير مفسّر؛ هو الجواب لو السؤال وصف ألم بطني أو هواء حر بمريض على ستيرويد (غالبًا مع مضادات الالتهاب).",
    "C": "<bdi>Acute Cerebral vasculitis</bdi>: الستيرويدات علاج لالتهاب الأوعية، مو سبب له.",
    "D": "<bdi>Intestinal ischemia with perforation</bdi> تُقترح بمسنة عندها رجفان أذيني أو مرض وعائي مع ألم غير متناسب مع الفحص؛ ليست مضاعفة معروفة لاستمرار البريدنيزولون."},

"AS-1586": {
    "B": "<bdi>Syphilis</bdi> الثانوي يعطي حمى وتضخم غدد وطفح بالراحتين والأخمصين بعد قرحة تناسلية غير مؤلمة؛ ما يسبب <bdi>oral candidiasis</bdi>.",
    "C": "<bdi>Brucellosis</bdi> تُقترح بتاريخ حليب نيء أو تماس حيواني مع حمى متموجة وألم ظهر أو مفصل عجزي حرقفي وتضخم كبد وطحال؛ ما فيه هذا التعرّض أو علامة ضعف مناعي هنا.",
    "D": "<bdi>Toxoplasmosis</bdi> بالبالغ السليم تعطي مرض شبيه بكريات وحيدة خفيف مع تضخم غدد، وبالإيدز تعطي آفات دماغية حلقية التعزيز؛ ما تفسر <bdi>thrush</bdi>."},

"AS-1593": {
    "A": "<bdi>Carotid US</bdi> مناسب لو كان الضعف عابر (دقائق) مع عوامل خطر وعائية (اشتباه <bdi>TIA</bdi>)؛ هنا الضعف مرتبط بحركة الرقبة مباشرة، مو نوبة عابرة.",
    "C": "<bdi>CT cervical spine</bdi> مناسب لو فيه تاريخ رضّة واشتباه كسر؛ ما فيه رضّة مذكورة هنا، والسؤال عن ضعف بعد حركة طبيعية للرقبة.",
    "D": "خيار غير متعلق فعليًا بالتشخيص المطروح هنا."},

"AS-1593B": {
    "A": "<bdi>Transesophageal echocardiography</bdi> مناسب لو فيه اشتباه مصدر قلبي (رجفان أذيني، نفخة، صمام صناعي، أو شاب بدون عوامل خطر وعائية)؛ ليس الفحص الأولي هنا.",
    "C": "<bdi>CT angiography of the neck</bdi> دقيق لكن يحتاج صبغة وإشعاع؛ يُستخدم لتأكيد أو توصيف تضيّق وجده السونار، أو لو السونار غير متاح أو غير قاطع، مو كفحص أولي.",
    "D": "<bdi>MRI of the brain</bdi> جزء من تقييم كامل لـ<bdi>TIA</bdi> لكن السؤال يبي الفحص الأولي للبحث عن المصدر القابل للعلاج، وهو <bdi>carotid duplex</bdi>."},

"AS-1594": {
    "A": "مسحة الدم تصف نوع فقر الدم (صغير الكريات، شاحب) لكن ما تحدد سببه؛ دراسات الحديد أصلاً أثبتت نقص الحديد.",
    "C": "خزعة نخاع العظم باضعة وغير ضرورية لو نقص الحديد مؤكد بالفيريتين؛ تُستخدم لنقص خلايا غير مفسّر أو اشتباه مرض نقي.",
    "D": "فقر حديد غير مفسّر بعمر ٥٥ علامة خطر لسرطان القولون ولازم يُحقق فيه دائمًا، ما نتركه بدون فحص."},

"AS-1595": {
    "A": "مسحة الدم تصف الانحلال أو شكل الخلايا لكن ما تحدد سبب فقدان الدم برجل متوسط العمر.",
    "B": "فحص الدم الخفي بالبراز للفحص بالأشخاص بدون أعراض؛ نتيجة سالبة ما تستبعد سبب هضمي لفقر الدم، فيُختار بس لو المنظار غير متاح بالخيارات.",
    "C": "خزعة نخاع العظم لنقص خلايا غير مفسّر أو اشتباه مرض نقي؛ ليست الفحص التالي لفقر حديد محتمل بدون تضخم أعضاء."},

"AS-1604": {
    "A": "<bdi>Dexamethasone</bdi> يقلل الوذمة الوعائية حول الأورام أو الخراجات؛ ما يفيد بوذمة السكتة أو النزيف الدماغي.",
    "B": "<bdi>Mannitol</bdi> مادة أسمولية تخفض الضغط داخل الجمجمة مؤقتًا كجسر؛ ما تزيل الورم الدموي، فمو علاج حاسم.",
    "D": "فرط التهوية يخفض الضغط داخل الجمجمة مؤقتًا بتضييق الأوعية؛ إجراء إنقاذ مؤقت مو علاج حاسم."},

"AS-1605": {
    "A": "<bdi>Reactive arthritis</bdi> تحتاج عدوى هضمية أو بولية سابقة وغالبًا التهاب ملتحمة أو إحليل، وتكون التهاب مفصل حاد وليست مزمنة محورية؛ ما فيه شي من هذا هنا.",
    "B": "<bdi>Rheumatoid arthritis</bdi> التهاب مفاصل صغيرة متماثل (<bdi>MCP, PIP, wrist</bdi>) يعفي العمود الفقري القطني والمفصل العجزي الحرقفي، وما يسبب التهاب وتر <bdi>Achilles</bdi> نموذجيًا.",
    "D": "التهاب المفاصل البلوري (نقرس، كاذب نقرس) يعطي التهاب حاد نوبي شديد الألم بمفصل أو مفصلين، مو ٣ أشهر من ألم ظهر التهابي مع تحديد حركة."},

"AS-1606": {
    "A": "نقل الدم يرفع الهيموغلوبين فقط بدون إيقاف الانحلال المناعي؛ يُحفظ للحالات الشديدة أو غير المستقرة، وتوافق الدم صعب بـ<bdi>AIHA</bdi>.",
    "B": "<bdi>Hydroxyurea</bdi> يرفع هيموغلوبين جنيني ويُستخدم بمرض الخلايا المنجلية؛ ما له دور بانحلال الدم المناعي.",
    "D": "الانحلال ليس حالة نقص حديد (الحديد يُعاد تدويره)؛ الحديد الوريدي لنقص الحديد الحقيقي بعدم تحمل فموي أو سوء امتصاص أو فقدان مستمر."},

"AS-1608": {
    "A": "فشل الاستجابة لأول جرعة سالبوتامول ليس بذاته معيار «مهدد للحياة»؛ يدفع لتصعيد العلاج (تكرار <bdi>SABA</bdi>، إضافة <bdi>ipratropium</bdi>، ستيرويد، مغنيسيوم).",
    "B": "تشبع أكسجين ٩٤٪ أعلى من الحد المهدد للحياة اللي يتطلب أقل من ٩٢٪.",
    "D": "تسرع تنفس ٢٨ (أكثر من ٢٥) هو علامة نوبة ربو حادة شديدة، مو مهددة للحياة."},

"AS-1610": {
    "A": "درجة <bdi>I</bdi> تعني ما فيه أعراض أبدًا مع نشاط عادي؛ هو يحس بضيق تنفس أثناء شغله العادي.",
    "C": "درجة <bdi>III</bdi> تحديد واضح وأقل من نشاط عادي يسبب أعراض وما يقدر يكمل شغله الطبيعي؛ هو لسا يقدر يكمل شغله.",
    "D": "درجة <bdi>IV</bdi> أعراض بالراحة؛ هو يصرح إنه مرتاح تمامًا بالراحة."},

"AS-1611": {
    "B": "التهاب الرئة مرض حاد يمتد أيام مع حمى وسعال منتج؛ ما يفسر ٥ أشهر من التدهور مع نزول وزن ١٠ كيلو (التهاب رئوي لا يستجيب بمدخن لازم يرفع شك ورم انسدادي).",
    "C": "الربو يعطي أزيز وضيق تنفس نوبي غالبًا من الصغر، بدون حمى أو تعرق ليلي أو نزول وزن.",
    "D": "الانصمام الرئوي يعطي ضيق تنفس مفاجئ وألم جنبي وتسرع نبض، مو مسار ٥ أشهر بسعال منتج وأعراض بائية."},

"AS-1624": {
    "A": "تصلب الشرايين يسبب سكتة تخثرية بمرضى عندهم عوامل خطر وعائية؛ هذا الرجل بدون أي تاريخ مرضي، والتوقيت فور بعد النزيف يوجه لتشنج الأوعية.",
    "B": "الصمة الدماغية تحتاج مصدر زي رجفان أذيني أو مرض صمامي أو مصدر سباتي مع بداية مفاجئة؛ ما فيه شي يوحي بمصدر صمي هنا.",
    "C": "تمزق الأنيوريزم يفسر النزيف الأصلي، لكن إعادة النزيف تظهر كنزيف جديد مفاجئ مع صداع وتراجع وعي، مو احتشاء."},

"AS-1625": {
    "B": "الفص الصدغي المسيطر (<bdi>Wernicke</bdi>) يعطي كلام سليس لكن فهم ضعيف؛ هنا الفهم سليم. كمان يسبب مشاكل ذاكرة وسمع، مو تشوش يمين-يسار.",
    "C": "الفص الجبهي المسيطر (<bdi>Broca</bdi>) يعطي كلام غير سليس وجهد بالنطق مع فهم سليم، غالبًا مع ضعف بالجهة المقابلة؛ ما يفسر تشوش يمين-يسار.",
    "D": "الفص القذالي يسبب عيوب بالمجال البصري (عمى نصفي متماثل بالجهة المقابلة) أو عمى قشري، مو مشاكل كتابة أو توجه مكاني."},

"AS-1632": {
    "B": "<bdi>Azathioprine</bdi> مثبط مناعي موفّر للستيرويد يُستخدم بمرض متوسط أو كصيانة لالتهاب الكلية الذئبي؛ ما يحمل الفايدة الوعائية الخاصة بـ<bdi>hydroxychloroquine</bdi>.",
    "C": "<bdi>Cyclosporine</bdi> مثبط <bdi>calcineurin</bdi> يُحفظ للمرض المعند أو بعض بروتوكولات التهاب الكلية؛ يسبب ضغط وسمية كلوية، فما يقلل الخطر الوعائي.",
    "D": "<bdi>Mycophenolate mofetil</bdi> هو العلاج الأول لالتهاب الكلية الذئبي (كرياتينين مرتفع وبروتينية)؛ هنا الكرياتينين واليوريا طبيعيان وما فيه إصابة عضو كبرى."},

"AS-1633": {
    "A": "<bdi>Warfarin</bdi> ممنوع بداية <bdi>HIT</bdi> الحادة لأن نقص بروتين <bdi>C</bdi> المبكر يسبب غرغرينا وريدية بالأطراف؛ يُبدأ بس بعد تعافي الصفائح مع تداخل مع دواء غير هيباريني.",
    "B": "<bdi>Enoxaparin</bdi> (هيبارين منخفض الوزن) يتفاعل تصالبيًا مع أجسام <bdi>HIT</bdi> المضادة وممنوع؛ يناسب جلطة وريدية بصفائح طبيعية.",
    "C": "<bdi>HIT</bdi> حالة تخثرية مو نزفية؛ نقل الصفائح ممكن يغذي تخثر إضافي ويُحفظ لنزيف فعلي شديد."},

"AS-1657B": {
    "A": "<bdi>Serum Iron</bdi> منخفض بنقص الحديد وبمرض مزمن أيضًا، ويتغير خلال اليوم، فما يحدد السبب بدقة.",
    "B": "<bdi>Serum ferritin</bdi> هو أفضل فحص أولي غير باضع (منخفضه شبه قاطع لنقص الحديد)، لكنه بروتين طور حاد وممكن يكون طبيعي كاذبًا مع التهاب؛ هو الجواب لو السؤال سأل عن الأفضل/الأولي.",
    "C": "<bdi>TIBC</bdi> يساعد يفرّق نقص الحديد (مرتفع) عن مرض مزمن (منخفض) لكنه مؤشر غير مباشر، مو حاسم."},

"AS-1658": {
    "A": "<bdi>HB S</bdi> موجود وسائد بمرض الخلايا المنجلية؛ غيابه يستبعد التشخيص كليًا.",
    "C": "<bdi>HB F</bdi> طبيعي أو مرتفع بمرض الخلايا المنجلية (ومرتفع جدًا بثلاسيميا بيتا الكبرى)؛ ليس غائبًا.",
    "D": "<bdi>HB C</bdi> يظهر فقط بمرض <bdi>HbSC</bdi>؛ غيابه متوقع بـ<bdi>HbSS</bdi> وما يؤكد التشخيص."},

"AS-1659": {
    "A": "<bdi>PNH</bdi> انحلال داخل الأوعية مع بول غامق صباحًا، غالبًا نقص خلايا شامل وجلطات وريدية غير معتادة؛ يُطرح لو ذُكر بول دموي أو جلطة غريبة.",
    "B": "<bdi>Hereditary Spherocytosis</bdi> انحلال مزمن منذ الطفولة مع تاريخ عائلي وتضخم طحال ويرقان وحصوات مرارية؛ بداية مفاجئة بالغة بدون تضخم طحال ما تناسبه.",
    "D": "<bdi>DIC</bdi> يستهلك الصفائح وعوامل التخثر فتكون الصفائح منخفضة مع تطاول زمن التخثر، بمريض خطير (عدوى، رضّة، خباثة)؛ هنا الصفائح طبيعية."},

"AS-1660": {
    "A": "<bdi>PNH</bdi> تعطي بول غامق صباحًا ونقص خلايا وجلطات وريدية غير معتادة، مو حصوات مرارية.",
    "C": "<bdi>AIHA</bdi> سبب مكتسب غالبًا مفاجئ مع <bdi>Coombs</bdi> مباشر موجب؛ الحصوات المرارية تدل على سنوات من الانحلال، ما يناسب عملية مكتسبة حديثة.",
    "D": "<bdi>DIC</bdi> يعطي صفائح منخفضة مع تطاول زمن التخثر بمريض خطير؛ الصفائح الطبيعية تستبعده."},

"AS-1669": {
    "B": "<bdi>Adipsic hypernatremia</bdi> سببه فقدان الشعور بالعطش (تلف مستقبلات الأسمولالية بالهايبوثلامس)، فالمريض ما يشرب أصلاً؛ هذي المرأة عطشها زائد وتتبول كثير.",
    "C": "<bdi>Psychogenic polydipsia</bdi> هو الفخ بسبب الاكتئاب المذكور. شرب الماء الزائد يعطي بول مخفف لكن صوديوم منخفض أو طبيعي منخفض؛ صوديوم ١٥٠ يستبعده."},

"AS-1670": {
    "A": "التحلل الخثري يُستخدم لو <bdi>PCI</bdi> بالوقت المناسب غير متاحة، لكن السكتة الإقفارية خلال ٣ أشهر مانع مطلق له.",
    "B": "الأسبرين يُعطى لكل مريض <bdi>STEMI</bdi> كدواء مساعد، لكنه ليس إعادة ترويه وما يفتح الشريان المسدود.",
    "C": "الهيبارين غير المجزأ مميع مساعد أثناء <bdi>PCI</bdi>؛ لوحده ما يعيد ترويه الشريان المصاب."},

"AS-1671": {
    "A": "<bdi>Septic Arthritis</bdi> تحتاج مفصل واحد حار أحمر حاد مع حمى وإنزيمات التهاب مرتفعة وسائل زليلي صديدي (كريات بيضاء غالبًا فوق ٥٠٠٠٠ مع غلبة عدلات)؛ هنا التحاليل والسائل الزليلي طبيعيان تمامًا."},
}

HIGHLIGHT_TERMS = {
"AS-1516": ["myoclonic seizures", "Valproic acid"],
"AS-1521": ["5 days after", "hypotension", "pansystolic murmur", "right sternal border"],
"AS-1524": ["MI two years ago", "progressive dyspnea and orthopnea at rest", "EF 20%"],
"AS-1529": ["end-stage kidney disease", "muffled heart sounds", "pericardial effusion", "Was Frankly Hypotensive"],
"AS-1535": ["HTN and DM", "no history of alcohol use", "10 years history of high aminotransferase", "ascites"],
"AS-1537": ["Heart failure with reduced EF", "metoprolol"],
"AS-1540": ["Burkitt lymphoma", "hypocalcemia + hyperphosphatemia", "Uric acid below 480"],
"AS-1541": ["50-year-old woman", "distal and proximal interphalangeal joints", "does not have significant early morning stiffness", "non-tender hard nodules over some distal interphalangeal", "Rheumatoid factor 30 (<58 kIU/L)"],
"AS-1542": ["DIP and PIP pain and swelling", "Rheumatoid factor 55 (normal <58)"],
"AS-1547": ["29-year-old", "asymptomatic", "pansystolic murmur that radiated to the axilla"],
"AS-1551": ["history of seizure", "generalized tonic-clonic seizure", "terminates after intravenous lorazepam"],
"AS-1554": ["blood transfusions 10 years ago", "AST and ALT within normal range", "HBsAg (+)", "IgG HBc (+)", "HBeAg (+)"],
"AS-1556": ["Wolff-Parkinson-White syndrome and atrial fibrillation", "control her rhythm"],
"AS-1562": ["sickle cells", "confirmatory test"],
"AS-1567": ["disoriented", "BP: 80/55", "RR: 33", "urea is 12 mmol/L"],
"AS-1569": ["type 2 diabetes", "could not tolerate it because of a cough", "24-hour urine protein 1500"],
"AS-1570": ["gout"],
"AS-1571": ["uti"],
"AS-1573": ["positive anti-HCV (ELISA)", "Hepatitis C RNA was negative"],
"AS-1580": ["Intensive Care Unit with pneumonia", "dopamine", "TSH 0.1 (low)", "T3 2 (low)"],
"AS-1582": ["prednisolone 60 mg", "continued the same dose", "Found dead in bathroom"],
"AS-1586": ["generalised lymphadenopathy", "travels frequently to Far East", "oral candidiasis"],
"AS-1593": ["post neck extension", "mri brain normal"],
"AS-1593B": ["left arm weakness without pain that lasted 5 minutes", "initial imaging"],
"AS-1594": ["55-year-old man", "pallor"],
"AS-1595": ["55-year-old man", "pallor"],
"AS-1604": ["papilledema", "Hemorrhagic transformation", "definitive"],
"AS-1605": ["lower back pain", "morning stiffness", "limited lumbar spine movements", "tenderness over the Achilles tendon"],
"AS-1606": ["splenomegaly", "spheroytosis"],
"AS-1608": ["acute exacerbation of asthma", "life-threatening"],
"AS-1609": ["left arm weakness", "lasted 5 minutes", "asymptomatic", "initial imaging"],
"AS-1610": ["exertional shortness of breath", "interferes with his job but does not limit him", "at rest, he is fine"],
"AS-1611": ["smoker for over 50 years", "lost 10 kg"],
"AS-1624": ["hemorrhagic stroke", "after 1 week", "left cerebral infarction"],
"AS-1625": ["understand what is being told", "can't write", "can't remember words", "can't know left and right"],
"AS-1632": ["mouth ulcers", "Complement C4 0.1", "remission and vascular risk"],
"AS-1633": ["IV heparin", "6 days post-operatively", "Platelet count is 75"],
"AS-1657": ["SINGLE CONFIRMATORY TEST", "IDA"],
"AS-1657B": ["Most definitive test", "microcytic anemia"],
"AS-1658": ["SCD", "absent"],
"AS-1659": ["no jaundice", "no lymphadenopathy or splenomegaly", "Reticulocyte count: Elevated", "Haptoglobin: Decreased"],
"AS-1660": ["jaundice", "multiple gallstones"],
"AS-1669": ["excessive urination and thirst", "lung metastases", "Sodium 150", "Osmolality 110"],
"AS-1670": ["non-hemorrhagic stroke 2 months ago", "ST-segment elevation in II, III, aVF"],
"AS-1671": ["history of URTI a few weeks back", "Synovial analysis is normal"],
}
