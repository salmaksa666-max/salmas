# Silent posts 88822-88973 (17 Nov afternoon batch) -> Silent bank section "نوفمبر 17"
G1 = "1) ريكول مكتوب (نصوص سايلنت)"
G2 = "2) صور: أسئلة من ملف التجميعات"
G3 = "3) صور: صفحات الحمراني وغيرها"
# (group, id, stem, options, answer, ok, key note, images)  images: "#N" = compilation page crop, "@path" = scratchpad file
T = [
 (G1, "exo", "A 6-month-old infant presents with exotropia present since birth. Examination reveals an absent red reflex, and the deviation persists on cover-uncover testing. Most appropriate next step?", ["Refer to ophthalmology", "Initiate eye patching"], "A", 1, "Absent red reflex ← urgent ophthalmology (rule out retinoblastoma/cataract).", ["#3445"]),
 (G1, "asd", "18-month-old child, isolated, reduced eye contact, doesn't respond to his own name, significant speech delay, spends a long time organizing his toys in a line. Most likely advice?", ["Hearing test", "Reassure", "Autism spectrum disorder screening"], "C", 0, "⚠ Not in the compilation. Classic red flags ← ASD screening (M-CHAT at 18–24 months).", []),
 (G1, "ptc", "Elderly patient: percutaneous transhepatic cholangiography done, then after 24 hours upper GI bleeding. Investigation?", ["Angiography", "CT abdomen", "Endoscopy", "US"], "A", 1, "Hemobilia after PTC ← angiography.", ["#1565"]),
 (G1, "ocp", "A newly married woman is using oral contraceptive pills and refuses to discontinue them, while her husband requests that she stop. Whose consent should be obtained?", ["The woman's consent only", "The husband's consent is the top priority", "Both the woman's and her husband's consent", "Her consent only if there is a medical reason"], "C", 1, "", ["#4288"]),
 (G1, "catbite", "A child was bitten by a cat (or another animal). Management?", ["Wound cleaning only", "Vaccine only", "Rabies vaccine and immunoglobulin"], "C", 1, "", ["#3456"]),
 (G1, "hb62", "Woman 45 y/o came to ER with 15 days of non-stopping heavy menstruation, Hb 62, she became drowsy and fainted. Most appropriate next step?", ["D&C", "Blood transfusion"], "B", 0, "⚠ Not in the compilation. Unstable + Hb 6.2 ← resuscitate/transfuse first.", []),
 (G1, "wpw", "Girl with WPW presents with palpitations, HR 250 (AF). Treatment?", ["Metoprolol", "Amiodarone", "Digoxin"], "B", 1, "WPW + AF: avoid AV-nodal blockers (BB, CCB, digoxin).", ["#141"]),
 (G1, "antid", "Woman delivered a healthy baby; she is O negative and the baby is O positive.", ["Give anti-D to the mother", "Give anti-D to the mother and baby", "No need to give anti-D"], "A", 0, "⚠ Not in the compilation. Rh-neg mother + Rh-pos baby ← anti-D to mother within 72 h.", []),
 (G1, "spiro", "Patient with liver cirrhosis and lower limb edema. Which drug must be given?", ["Spironolactone", "Furosemide"], "A", 0, "⚠ Not in the compilation. Cirrhotic ascites/edema ← spironolactone first-line.", []),
 (G1, "mtx2100", "Ectopic pregnancy treated with methotrexate. hCG: first 1000, second 900, then suddenly 2100.", ["Surgical intervention", "Second dose of methotrexate", "Observe"], "A", 1, "Rising hCG after MTX ← surgery (file #2244).", ["#2244"]),
 (G1, "ampulla", "Ultrasound shows dilated intra- and extra-hepatic common bile duct. Most likely cause?", ["Ampullary (periampullary) cancer", "Gallbladder cancer", "HCC"], "A", 1, "", ["#1579"]),
 (G1, "rabpreg", "Pregnant woman who didn't receive the rabies vaccine (after exposure). When should she get it?", ["At the clinic now", "Postpartum", "At 28 weeks"], "A", 0, "⚠ Not in the compilation. Rabies is fatal; vaccine is safe in pregnancy ← now.", []),
 (G1, "ogilvie", "Schizophrenic patient with non-mechanical colonic obstruction, 10 cm dilatation (no neostigmine in options).", ["Colonoscopic decompression", "Total colectomy", "Diverting colostomy"], "A", 1, "", ["#1517"]),
 (G1, "axnode", "Enlarged mobile axillary lymph node in a woman. Next step?", ["Bilateral mammography", "Core biopsy"], "A", 0, "⚠ The poster was unsure. Image the breasts first (mammography ± US), then biopsy.", []),
 (G1, "abscess", "Breast abscess on US: thick wall, no septations, 3×3 cm.", ["Aspiration and antibiotics", "Incision and drainage", "Antibiotics only"], "A", 1, "Small unilocular abscess ← needle aspiration + antibiotics.", ["#1442"]),
 (G1, "accreta", "Patient who had myomectomy: what is the risk of developing placenta accreta?", ["Increased", "Decreased", "Not affected"], "C", 1, "GameBoy key: not affected (file #2071).", ["#2071"]),
 (G1, "fluid12", "Pediatric boy going for surgery (testicular torsion), weight 12 kg. Maintenance IV fluid per day?", ["1000 mL", "1100 mL", "1200 mL", "1300 mL"], "B", 1, "100×10 + 50×2 = 1100 mL/day.", ["#3553"]),
 (G1, "epig", "Toxic child with drooling and perioral cyanosis. Next?", ["Laryngoscopy (airway) in the OR", "Admission to general ward"], "A", 0, "⚠ Epiglottitis ← secure airway in the OR.", ["#3123"]),
 (G1, "colon51", "51-year-old woman requests colon cancer screening, no family history, no risk factors.", ["Colonoscopy every five years", "Fecal occult blood test"], "B", 1, "Alhomrani rule: colonoscopy every 5 y (wrong interval) vs annual FOBT ← FOBT.", []),
 (G1, "dmcf", "Diabetic mother asks which risk is the same as the general population.", ["Cystic fibrosis", "Macrosomia", "Pre-eclampsia", "Polyhydramnios"], "A", 1, "", ["#2466"]),
 (G1, "atopic", "Child with itchy rash on trunk, scalp and extensor surfaces.", ["Atopic dermatitis", "Seborrheic dermatitis"], "A", 1, "", ["#3415"]),
 (G1, "ucdx", "How to diagnose ulcerative colitis?", ["Colonoscopy", "CT", "Stool culture"], "A", 0, "⚠ Colonoscopy with biopsy.", []),
 (G1, "psa", "Elderly male with high PSA and back pain.", ["Prostatitis", "BPH", "Prostate cancer"], "C", 0, "⚠ Back pain = bone metastasis.", []),
 (G1, "myco", "14-year-old female, CXR shows bilateral patchy infiltrates. Causative organism?", ["Mycoplasma pneumoniae", "Streptococcus pneumoniae"], "A", 0, "⚠ Adolescent + bilateral patchy (atypical) ← Mycoplasma.", []),
 (G1, "gono", "Male with suspected gonorrhea. Which test establishes the diagnosis?", ["Blood culture", "Urine culture", "Urethral swab"], "C", 1, "", ["#323"]),
 (G1, "mvaair", "Young male after MVA with facial trauma, bloody crust in the nostrils and periorbital ecchymosis. How to secure the airway?", ["Endotracheal (orotracheal) intubation", "Nasotracheal intubation"], "A", 0, "⚠ Suspected base-of-skull fracture ← never nasal tubes.", []),
 (G1, "downthy", "Which disease is associated with Down syndrome?", ["Hypothyroidism", "Hyperthyroidism"], "A", 1, "", ["#3488"]),
 (G1, "mmrfev", "A child has fever of 38.9 °C and came for the MMR vaccine.", ["Administer the vaccine", "Give it without the rubella component", "Defer vaccination until symptoms resolve"], "A", 1, "Alhomrani Nov (MK-NOV-1151, 18 months, 38.9, congested throat, slightly ill) + Athar + file #3875 ← give MMR now. Mild illness even with fever is NOT a reason to delay; defer only if moderate–severe illness.", ["#3875"]),
 (G1, "lambda", "Ultrasound shows the lambda (twin-peak) sign. Which type of twins?", ["Monochorionic diamniotic", "Dichorionic diamniotic", "Monochorionic monoamniotic"], "B", 0, "⚠ Lambda = Di-Di; T-sign = Mono-Di.", []),
]
SO_NUMS = [15, 20, 380, 466, 603, 840, 849, 1028, 1041, 1092, 1214, 1377, 1378, 1395, 1426, 1441, 1448, 1455, 1520, 1716, 1891, 2004, 2232, 2273, 2311, 2446, 2499,
           2535, 2749, 2793, 2838, 2875, 3108, 3136, 3199, 3287, 3542, 3647, 3683, 3691, 3697, 3735, 3752, 3769, 3799, 3889, 3937, 3943, 3988, 4007, 4231, 4535, 4575, 4586, 4658, 4683]
P = "@t17/n2/"
M = [
 (G3, "acs", "X-ray and scenario: pediatric sickle cell disease patient with acute chest syndrome, vitals not improving despite fluids and oxygen. Management?", ["Hydroxyurea", "Exchange transfusion"], "B", 1, "", [P + "88831_5"]),
 (G3, "sarc", "40-year-old woman with progressive dyspnea, dry cough, erythema nodosum, cervical nodes, bilateral hilar lymphadenopathy, PPD negative, non-caseating granuloma. Next best option?", ["Montelukast", "Glucocorticoids", "Anti-tuberculosis", "Salmeterol inhaler"], "B", 1, "", [P + "88831_7"]),
 (G3, "xla", "Child with 5-6 respiratory infections, 3-4 gastroenteritis with giardiasis, greasy foul-smelling stool, small tonsils; younger brother died of similar disease. Diagnosis?", ["X-linked agammaglobulinemia", "Severe combined immunodeficiency", "IgA deficiency", "Hyper IgE syndrome"], "A", 1, "", [P + "88831_8"]),
 (G3, "hemat", "50-year-old with painless hematuria for 3 days, no urinary symptoms. Initial investigation?", ["Urinalysis", "CT KUB", "Cystoscopy"], "A", 1, "", [P + "88895_4"]),
 (G3, "celiac", "8-year-old with chronic abdominal pain and distension, loss of subcutaneous fat, growth plateau. Which nutrient should be avoided?", ["Gluten", "Fat"], "A", 1, "", [P + "88851_1"]),
 (G3, "uti", "20-year-old female with dysuria and suprapubic pain, no fever. Urinalysis: nitrite positive, 10 WBC. Management?", ["No intervention", "Start empiric antibiotics", "Send urine culture + start empiric antibiotics", "Hydration and cranberry juice"], "B", 1, "Simple female cystitis ← no culture needed.", [P + "88851_2"]),
 (G3, "openfx", "RTA with mid-shaft femur fracture and a large contaminated wound with exposed bone, stable vitals. Surgical choice?", ["Primary internal fixation", "Primary wound closure and cast", "Intramedullary fixation with primary closure", "Debridement, external fixation and delayed wound closure"], "D", 1, "", [P + "88851_7"]),
 (G3, "cornab", "27-year-old male feels something in his eye: tearing, photophobia; question mentioned the cornea and no eye protection. Diagnosis?", ["Corneal ulcer", "Corneal abrasion", "Subconjunctival hemorrhage"], "B", 1, "", [P + "88851_9"]),
 (G3, "ida", "Picky-eater girl who drinks a lot of milk; siblings had the same. Low Hb and PCV, reticulocytes 3. Diagnosis?", ["IDA", "SCD", "Hemophilia", "Hemolysis"], "A", 1, "", [P + "88861_1"]),
 (G3, "fascio", "Trauma patient with leg fracture: pain out of proportion, paresthesia, diminished pulse. Next step?", ["Consult ortho for immediate fixation", "Bedside fasciotomy for compartment release", "IV antibiotics"], "B", 1, "", [P + "88885_0"]),
 (G3, "ptx", "After MVA: tracheal deviation and absent breath sounds over the right hemithorax. Next step?", ["IV normal saline", "Endotracheal intubation", "Needle decompression", "Chest tube insertion"], "C", 1, "Alhomrani: resonant (pneumo) ← needle; dull (hemo) ← chest tube.", [P + "88885_2"]),
 (G3, "cta", "Chronic claudication: left femoral pulse present, absent popliteal/distal; right femoral and popliteal present, diminished distal. Investigation?", ["CT angiography", "Ultrasound", "Conventional angiography"], "A", 1, "", [P + "88885_3"]),
 (G3, "spine", "RTA with back pain; spine injury cannot be ruled out, neurosurgery called. Most important until fully assessed?", ["Urgent full spine CT", "Maintain full spine immobilization", "Pelvic binder", "Flexion-extension test"], "B", 1, "", [P + "88885_5"]),
 (G3, "binder", "After MVA with pelvic fracture and significant instability, BP 80/50.", ["Laparotomy", "Pelvic binder", "CT pelvis/abdomen"], "B", 1, "", [P + "88885_7"]),
 (G3, "eschar", "Circumferential right forearm burn; digit saturation 86%, absent pulse.", ["Bedside escharotomy", "Measure intra-compartmental pressure"], "A", 1, "", [P + "88885_8"]),
 (G3, "epist", "Hypertensive patient with right nasal bleed; anterior rhinoscopy fails to identify the source. Next?", ["Facial CT", "Nasal endoscopy", "Refer to cardiology"], "B", 0, "⚠ Answer not shown on the page.", [P + "88885_9"]),
 (G3, "scr50", "50-year-old man for cancer screening. Which cancer is appropriate to screen at this stage?", ["Lung", "Breast", "Prostate", "Colon"], "D", 1, "", [P + "88895_2"]),
 (G3, "tia48", "30 minutes of slurred speech that resolved; carotid stenosis 48%. Best management besides risk-factor control?", ["Observe", "Carotid stenting", "Carotid thrombectomy", "Carotid endarterectomy"], "A", 1, "", [P + "88895_3"]),
 (G3, "atn", "Elderly on lisinopril with vomiting/diarrhea; creatinine 60→160. Urine Na 68, osmolality 220, SG 1.009. Diagnosis?", ["Pre-renal AKI", "Post-renal AKI", "Acute tubular necrosis", "Acute-on-chronic CKD"], "C", 1, "Urine Na >40 + dilute urine ← ATN.", [P + "88895_5"]),
 (G3, "faceair", "20-year-old ejected from a motorcycle with significant facial lacerations and face deformity. Initial airway?", ["Percutaneous tracheostomy", "Surgical cricothyroidotomy", "Endotracheal intubation", "Nasotracheal intubation"], "B", 1, "Bank answer (same stem): major facial injury/deformity ← cricothyroidotomy, never nasal.", [P + "88901_0"]),
 (G3, "squint", "5-year-old at pre-school check with misaligned right eye. Next/initial?", ["Refer to pediatric ophthalmology next day", "Urgent glasses", "Hirschberg corneal reflex test", "Detailed history for possible perinatal trauma"], "D", 1, "Alhomrani: final answer D (back to old answer).", [P + "88905_0"]),
 (G3, "pop80", "80-year-old female with frequency, urgency and dysuria; grade 2 pelvic organ prolapse. Next step?", ["Hysterectomy", "Mid-urethral sling", "Urinalysis", "Anterior and posterior colporrhaphy"], "C", 0, "⚠ Answer not shown; UTI symptoms ← urinalysis first.", [P + "88912_0"]),
 (G3, "hbvhcc", "60-year-old with jaundice for 2 months; US shows liver cirrhosis with 2 lesions. Cause?", ["Aflatoxin", "Lead poisoning", "Wilson disease", "Chronic hepatitis B"], "D", 1, "", [P + "88917_0"]),
 (G3, "sens", "New screening test: 200 positive cases in 1000; the test detects 180 with 20 false negatives. Sensitivity?", ["95%", "90%", "80%", "70%"], "B", 1, "180 / (180+20) = 90%.", [P + "88919_0"]),
 (G3, "mmr", "In 200,000 live births, 450 mothers died. Maternal mortality ratio?", ["225 per 100,000", "450 per 200,000", "450 per 100,000", "0.225 per 100,000"], "A", 1, "", [P + "88921_0"]),
 (G3, "wrongsite", "Surgeon begins operating on the wrong knee; the nurse hesitated to speak up. Best way to prevent this error?", ["Surgical site marking and team verification during time-out", "Allow a single nurse to inform the surgeon", "Prior review of the chart"], "A", 1, "", [P + "88922_0"]),
 (G3, "ino", "Patient looks to the right and can't adduct the left eye, with nystagmus. Lesion?", ["Abducens nerve palsy", "Medial longitudinal fasciculus", "Caudate nucleus", "Hippocampus"], "B", 1, "", [P + "88932_0"]),
 (G3, "dxerr", "Chest pain + SOB assumed acid discomfort, PPI given; 2 days later worse and found to have CHF. How to prevent?", ["Rapidly processing the patient", "First impression of the patient", "Improve doctor-patient communication"], "C", 1, "Athar code version (what error?) ← rapid processing.", [P + "88934_0"]),
 (G3, "uc10", "10-year-old with bloody diarrhea, weight loss and low albumin.", ["Crohn's", "Celiac", "UC"], "C", 1, "Alhomrani: low albumin + bloody ← UC.", [P + "88936_0"]),
 (G3, "asthcoun", "Mother is worried about her son who has asthma. Most appropriate counseling?", ["He will develop chronic lung disorder", "Childhood asthma will disappear later in life", "He will have asthma for the rest of his life", "No correlation between childhood and adult asthma"], "B", 1, "", [P + "88942_3"]),
 (G3, "jdm", "8-year-old girl with 8 weeks rash, weight loss, weakness; heliotrope rash, rash over elbows, truncal weakness, CK 850.", ["SLE", "Scleroderma", "Muscular dystrophy", "Juvenile dermatomyositis"], "D", 1, "", [P + "88942_5"]),
 (G3, "idmjit", "Newborn of a diabetic mother with jitteriness. What to check?", ["Sodium", "Calcium", "Magnesium", "Blood glucose"], "D", 1, "", [P + "88942_6"]),
 (G3, "refuseab", "18 weeks, very high-risk pregnancy that could be fatal to the mother. Both the patient and spouse refuse abortion due to beliefs.", ["Contact the ethics committee", "Go ahead with the abortion", "Transfer to another doctor", "Respect their decision"], "D", 1, "", [P + "88942_7"]),
 (G3, "stepping", "Name of the reflex in the picture (baby 'walks' when feet touch a surface)?", ["Rooting reflex", "Stepping reflex"], "B", 1, "Stepping disappears ~2 months.", [P + "88942_9"]),
 (G3, "sacral", "Child (4–6 y) with chronic constipation; everything normal except a suspected sacral dimple. Next step?", ["MRI of the lumbosacral spine", "Management of chronic constipation"], "A", 0, "⚠ Answer not shown; dimple + bowel/bladder symptoms ← MRI.", [P + "88952_2"]),
 (G3, "measles", "Unvaccinated child with fever, Koplik spots and rash spreading downward. Treatment?", ["Amoxicillin", "Supportive treatment", "Acyclovir"], "B", 1, "", [P + "88952_6"]),
 (G3, "ttn", "Transient tachypnea of the newborn: what is seen on chest X-ray?", ["Fluid in fissures", "Air bronchogram with ground glass", "Hyperinflation with patchy infiltrates"], "A", 1, "", [P + "88952_6"]),
]
# Silent 88974-88978 (15:20-15:37 UTC)
T += [
 (G1, "umbil6", "6-year-old child with umbilical hernia since infancy. No symptoms and it is reducible. Management?", ["Elective surgery", "Observe until adolescence"], "A", 1, "Umbilical hernia persisting beyond 4-5 years ← elective repair.", ["#3619"]),
 (G1, "thyrhem", "After thyroidectomy the patient develops a large neck swelling with stridor. Next step?", ["Tracheostomy", "Close observation", "Percutaneous drainage", "Bedside wound exploration"], "D", 1, "Post-thyroidectomy hematoma with airway compromise ← open the wound at the bedside.", ["#1549"]),
]
M += [
 (G3, "alcliver", "36-year-old asymptomatic man with elevated liver enzymes; smoker, drinks alcohol every weekend. Iron and TIBC mildly high, ferritin given; HCV negative, HBsAg negative with positive anti-HBs. US: enlarged liver, no focal lesion. Underlying liver disease?", ["Hemochromatosis", "Alcoholic hepatitis", "Hepatocellular carcinoma", "Chronic hepatitis B infection"], "B", 1, "Same as file #691.", ["#691"]),
 (G3, "mile15", "Milestones: walks backwards, eats with spoon, 5-6 words, plays with cubes. Age in months?", ["6 months", "9 months", "15 months", "24 months"], "C", 1, "Same idea as file #3215 (walks backwards + spoon ← 15 months).", ["@t17/n3/88976_0", "#3215"]),
]
# Silent 88980-88981
T += [
 (G1, "polyhyd", "Which of the following causes polyhydramnios?", ["Anencephaly", "Post-term pregnancy", "Posterior urethral valve", "Maternal ingestion of NSAIDs"], "A", 1, "If 'uncontrolled maternal diabetes' is offered instead (no anencephaly) ← diabetes (file #2329). PUV, post-term, NSAIDs ← OLIGOhydramnios.", ["#2328"]),
 (G1, "pedas", "Child with valvular aortic stenosis presenting with symptoms. Management?", ["Follow-up 3-6 months", "Reassurance", "Medical symptomatic treatment", "Balloon valvuloplasty/dilatation"], "D", 1, "Symptomatic congenital AS in a child ← transvalvular balloon dilatation (file #3091).", ["#3091"]),
]
# Silent 88982 (recall had no options: "Bluish bulging of the hymen, management")
T += [
 (G1, "hymen", "A 15-year-old girl with primary amenorrhea and cyclic lower abdominal pain. On examination there is a bluish bulging membrane at the vaginal opening. What is the most appropriate management?", ["Hymenotomy (cruciate incision) to drain the hematocolpos", "Combined oral contraceptive pills", "Reassure and observe", "Pelvic MRI then vaginoplasty"], "A", 0,
  "⚠ Silent's recall was only 'bluish bulging of the hymen – management' with no options; I wrote the options. Diagnosis = imperforate hymen (file #1965); treatment = cruciate hymenotomy/hymenectomy (file #2140 is the post-op follow-up of exactly this operation).", ["#1965", "#2140"]),
]
SO_NUMS += [2140]
