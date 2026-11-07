# -*- coding: utf-8 -*-
"""Pediatrics systems -> topics for build_dense_merged.py (SPEC=peds).
Same shape as the Medicine SYS list: (system, system regex, [(topic, regex), ..., (last topic, ".")])."""

SYS = [
 ("Neonatology", r"newborn|neonat|preterm|premature|term (baby|infant|neonate)|\d+ ?(weeks|wks) (of )?gestation|gestational|apgar|surfactant|ttn\b|transient tachypnea|meconium|hyaline|respiratory distress syndrome|cephal[oh]?hematoma|caput|erb|klumpke|primitive reflex|moro|rooting|grasp reflex|necrotizing enterocolitis|\bnec\b|umbilical|kernicterus|phototherapy|exchange transfusion|physiological jaundice|breast ?milk jaundice|infant of (a )?diabetic|vitamin k|delivery room|resuscitat\w* (of|the) (newborn|baby)|bronchopulmonary dysplasia|retinopathy of prematurity|\bnicu\b", [
   ("Neonatal jaundice", r"jaundice|bilirubin|phototherapy|exchange transfusion|kernicterus|breast ?milk|coombs|abo|rh\b"),
   ("Neonatal breathing (RDS / TTN / MAS)", r"ttn\b|transient tachypnea|meconium|hyaline|respiratory distress|surfactant|grunting|bronchopulmonary|cpap|apnea"),
   ("Resuscitation / birth injury / reflexes", r"apgar|resuscitat|ventilation|chest compression|erb|klumpke|cephal|caput|clavicle|reflex|moro|rooting|grasp"),
   ("Other neonatal", r".")]),
 ("Growth, development & nutrition", r"milestone|develop|sit|walk|crawl|babbl|words|sentence|smile|social|short stature|stature|height|growth|percentile|failure to thrive|\bftt\b|weight gain|bone age|breast ?feed|formula|feeding|cow'?s milk|solid food|wean|rickets|vitamin d|malnutrition|marasmus|kwashiorkor|obes|bmi", [
   ("Milestones / development", r"milestone|develop|sit|walk|crawl|babbl|words|sentence|smile|social|stack|cubes|copy|draw|pincer|autis|speech|language"),
   ("Growth / short stature / FTT", r"short stature|stature|height|growth|percentile|failure to thrive|\bftt\b|bone age|weight gain|obes|bmi|head circumference"),
   ("Nutrition / feeding / rickets", r"breast ?feed|formula|feeding|cow'?s milk|solid food|wean|rickets|vitamin|malnutrition|marasmus|kwashiorkor|iron supplement|zinc"),
   ("Other growth", r".")]),
 ("Vaccines & infectious disease", r"vaccin|immuni[sz]|mmr|bcg|polio|dtap|hepatitis b|rotavirus|fever|rash|measles|rubella|mumps|varicella|chickenpox|roseola|erythema infectiosum|fifth disease|scarlet|hand,? foot|kawasaki|meningit|lumbar puncture|csf|sepsis|tuberc|\bppd\b|\btb\b|pertussis|whooping|diphtheria|tetanus|rabies|brucell|malaria|typhoid|hiv|infection|antibiotic|impetigo|cellulitis|osteomyel|septic arthritis|abscess|lymphaden|mononucleosis|ebv|cmv|toxoplasm|herpes|hajj|meningococc|prophylaxis", [
   ("Vaccines / prophylaxis", r"vaccin|immuni[sz]|mmr|bcg|polio|dtap|dtp|hepatitis b|rotavirus|pneumococcal|contraindicat|schedule|hajj|prophylaxis|immunoglobulin|catch-?up|rabies|tetanus"),
   ("Rash / exanthems / Kawasaki", r"rash|measles|rubella|varicella|chickenpox|roseola|erythema infectiosum|fifth|slapped|scarlet|hand,? foot|kawasaki|koplik|vesic|impetigo"),
   ("Meningitis / sepsis / fever", r"meningit|lumbar puncture|csf|sepsis|fever without|febrile infant|bacteremia|neck stiff|kernig|brudzinski|ceftriaxone"),
   ("TB / pertussis / other infections", r"tuberc|\bppd\b|\btb\b|pertussis|whooping|diphtheria|brucell|malaria|typhoid|hiv|mononucleosis|ebv|cmv|toxoplasm|parasit|worm"),
   ("Other infections", r".")]),
 ("Respiratory & ENT", r"asthma|wheez|bronchiolitis|croup|stridor|epiglottitis|cough|pneumonia|respiratory|breath|tachypnea|cystic fibrosis|foreign body|aspirat|inhal|oxygen|saturation|salbutamol|nebuli|otitis|ear|tympanic|tonsil|pharyngitis|sore throat|sinusitis|adenoid|nasal|snor|sleep apnea|laryng", [
   ("Asthma / wheeze", r"asthma|wheez|salbutamol|inhaler|steroid|montelukast|spacer|nebuli"),
   ("Bronchiolitis / croup / stridor", r"bronchiolitis|rsv|croup|stridor|barking|epiglottitis|laryng|tracheitis|foreign body|aspirat"),
   ("Pneumonia / CF", r"pneumonia|consolidation|crackles|cystic fibrosis|sweat chloride|effusion|empyema"),
   ("ENT (ear / throat / nose)", r"otitis|ear|tympanic|tonsil|pharyngitis|sore throat|strep|sinusitis|adenoid|nasal|snor|sleep apnea|epistaxis|hearing"),
   ("Other respiratory", r".")]),
 ("Cardiology", r"heart|cardi|murmur|cyanos|cyanotic|vsd|asd|pda|ductus|tetralogy|fallot|coarctation|transposition|tga|valv|stenosis|regurgit|rheumatic fever|syncope|arrhythm|tachycard|svt|ecg|hypertension|blood pressure|chest pain|myocarditis|pericard|endocarditis|tet spell|squatting|prostaglandin|indomethacin|ibuprofen.*duct", [
   ("Congenital heart disease", r"vsd|asd|pda|ductus|tetralogy|fallot|coarctation|transposition|tga|cyanos|cyanotic|tet spell|squatting|prostaglandin|indomethacin|congenital|down|murmur"),
   ("Rheumatic fever / myocarditis / endocarditis", r"rheumatic|jones|myocarditis|pericard|endocarditis|aso"),
   ("Arrhythmia / syncope / BP", r"arrhythm|tachycard|svt|ecg|syncope|adenosine|vagal|hypertension|blood pressure|qt"),
   ("Other cardiology", r".")]),
 ("GI & surgery", r"vomit|diarrh|dehydrat|gastroenteritis|abdominal|abdomen|constipat|stool|bowel|pyloric|intussusception|volvulus|malrotation|bilious|hirschsprung|appendic|hernia|hydrocele|undescended|testi|torsion|reflux|gerd|celiac|crohn|colitis|liver|hepat|biliary atresia|jaundice|gi bleed|rectal bleed|meckel|ors\b|fluid|bolus|intestinal obstruction|esophag|foreign body ingest|swallow|battery|caustic|dysphagia", [
   ("Dehydration / gastroenteritis / fluids", r"dehydrat|gastroenteritis|diarrh|ors\b|fluid|bolus|maintenance|rotavirus|sodium"),
   ("Surgical abdomen (pyloric / intussusception / volvulus)", r"pyloric|intussusception|volvulus|malrotation|bilious|hirschsprung|appendic|meckel|obstruction|duodenal atresia|double bubble|currant|sausage|olive"),
   ("Groin / testis", r"hernia|hydrocele|undescended|testi|torsion|scrot|phimosis|hypospadias|circumcis"),
   ("Liver / jaundice / GI bleed", r"liver|hepat|biliary|jaundice|wilson|gi bleed|rectal bleed|hematochezia|melena|varice"),
   ("Reflux / constipation / malabsorption", r"reflux|gerd|constipat|encopresis|celiac|crohn|colitis|ibd|malabsorption|lactose|cow'?s milk protein|allerg|colic"),
   ("Other GI", r".")]),
 ("Nephrology & urology", r"\buti\b|urinary|urine|urinalysis|dysuria|pyelo|vesicoureteral|vur|vcug|dmsa|renal|kidney|nephrotic|nephritic|proteinuria|hematuria|cola|edema|glomerul|psgn|hus\b|hemolytic uremic|enuresis|bed ?wet|wilms|hydronephrosis|posterior urethral|creatinine|dialysis|potassium|electrolyte|hyponat|hypernat", [
   ("UTI / VUR", r"\buti\b|urinary tract infection|dysuria|pyelo|vesicoureteral|vur|vcug|dmsa|urine culture|cephalexin|renal us|ultrasound"),
   ("Nephrotic / nephritic / HUS", r"nephrotic|nephritic|proteinuria|hematuria|cola|edema|glomerul|psgn|hus\b|hemolytic uremic|albumin|iga|henoch"),
   ("Enuresis / other urology", r"enuresis|bed ?wet|alarm|desmopressin|hydronephrosis|posterior urethral|hypospadias"),
   ("Other renal", r".")]),
 ("Neurology", r"seizure|convuls|epilep|febrile seizure|absence|spasm|eeg|headache|migraine|cerebral palsy|hypotonia|floppy|weakness|duchenne|gower|spinal muscular|guillain|ataxia|hydroceph|head circumference|macroceph|microceph|fontanel|consciousness|gcs|head injury|head trauma|concussion|tic\b|tourette|neural tube|spina bifida|myelomeningocele|squint|strabismus|developmental regression", [
   ("Seizures / febrile seizure", r"seizure|convuls|epilep|absence|spasm|eeg|valpro|phenobarb|levetir|diazepam|midazolam|centrotemporal|rolandic"),
   ("Weakness / hypotonia / CP", r"cerebral palsy|hypotonia|floppy|weakness|duchenne|gower|spinal muscular|guillain|ataxia|myasthenia"),
   ("Head (hydrocephalus / trauma / headache)", r"hydroceph|head circumference|macroceph|microceph|fontanel|head injury|head trauma|concussion|ct\b|headache|migraine|idiopathic intracranial"),
   ("Other neurology", r".")]),
 ("Hematology & oncology", r"anemia|anaemia|hemoglobin|\bhb\b|pallor|pale|iron|ferritin|thalass|sickle|g6pd|hemoly|spherocyt|platelet|itp|bleeding|bruis|petechia|purpura|hemophilia|willebrand|pt\b|ptt|coagul|leukemia|lymphoma|wilms|neuroblastoma|retinoblastoma|tumou?r|mass|cancer|malignan|chemo|neutropeni|transfusion|aldrich|immunodeficien|scid|recurrent infection", [
   ("Anemia (iron / thalassemia / sickle / G6PD)", r"anemia|anaemia|pallor|pale|iron|ferritin|thalass|sickle|g6pd|hemoly|spherocyt|lead|milk|mcv|hemoglobin electrophoresis|dactylitis|vaso-?occlusive"),
   ("Bleeding (ITP / hemophilia / vWD)", r"platelet|itp|bleeding|bruis|petechia|purpura|hemophilia|willebrand|ptt|pt\b|coagul|factor|ivig|hemarthrosis"),
   ("Cancer (leukemia / Wilms / neuroblastoma / retinoblastoma)", r"leukemia|lymphoma|wilms|neuroblastoma|retinoblastoma|tumou?r|mass|cancer|malignan|chemo|white reflex|leukocoria|blast"),
   ("Immunodeficiency", r"aldrich|immunodeficien|scid|recurrent infection|digeorge|agammaglobulin|chronic granulomatous|neutropeni"),
   ("Other hematology", r".")]),
 ("Endocrine, genetics & metabolic", r"diabet|insulin|glucose|dka|ketoacidosis|hypoglyc|thyroid|tsh|hypothyroid|congenital adrenal|cah|ambiguous genitalia|cortisol|puberty|precocious|menarche|breast development|gynecomastia|growth hormone|down syndrome|trisomy|turner|klinefelter|fragile x|noonan|marfan|karyotype|chromosom|genetic|syndrome|galactosemia|phenylketonuria|pku|inborn error|metabolic|ammonia|storage|newborn screening|reducing substance", [
   ("Diabetes / DKA / hypoglycemia", r"diabet|insulin|glucose|dka|ketoacidosis|hypoglyc|polyuria|polydipsia"),
   ("Thyroid / adrenal / puberty", r"thyroid|tsh|hypothyroid|congenital adrenal|cah|ambiguous|cortisol|puberty|precocious|menarche|breast development|thelarche|gynecomastia|growth hormone|salt[- ]wasting|17"),
   ("Genetic syndromes", r"down syndrome|trisomy|turner|klinefelter|fragile x|noonan|marfan|karyotype|chromosom|genetic|prader|angelman|williams|digeorge|edward|patau"),
   ("Inborn errors of metabolism", r"galactosemia|phenylketonuria|pku|inborn error|metabolic|ammonia|storage|newborn screening|reducing substance|maple|urea cycle"),
   ("Other endocrine", r".")]),
 ("Musculoskeletal & rheumatology", r"limp|hip|knee|ankle|joint|arthritis|jia|juvenile idiopathic|henoch|hsp\b|vasculit|lupus|\bsle\b|ddh|developmental dysplasia|barlow|ortolani|perthes|slipped capital|scfe|osgood|scoliosis|club ?foot|talipes|fracture|bone|torticollis|genu|bow ?leg|flat ?foot|nursemaid|elbow|osteogenesis", [
   ("Limp / hip (DDH / Perthes / SCFE / transient synovitis)", r"limp|hip|ddh|developmental dysplasia|barlow|ortolani|perthes|slipped capital|scfe|transient synovitis|septic"),
   ("Arthritis / HSP / vasculitis", r"arthritis|jia|juvenile idiopathic|henoch|hsp\b|vasculit|lupus|\bsle\b|methotrexate|joint"),
   ("Fractures / bones / deformities", r"fracture|bone|scoliosis|club ?foot|talipes|torticollis|genu|bow ?leg|flat ?foot|nursemaid|elbow|osteogenesis|osgood"),
   ("Other MSK", r".")]),
 ("Emergency, poisoning & child abuse", r"poison|ingest|overdose|toxic|paracetamol|acetaminophen|iron tablet|organophosph|kerosene|hydrocarbon|lead|caustic|bleach|button battery|antidote|n-acetylcysteine|charcoal|abuse|non-?accidental|neglect|shaken|retinal hemorrhage|bruises of different|authorities|social service|cpr|cardiac arrest|resuscitation|drowning|burn|anaphyla|epinephrine|bite|dnr|consent|confidential", [
   ("Poisoning", r"poison|ingest|overdose|toxic|paracetamol|acetaminophen|iron|organophosph|kerosene|hydrocarbon|lead|caustic|bleach|battery|antidote|acetylcysteine|charcoal"),
   ("Child abuse / ethics", r"abuse|non-?accidental|neglect|shaken|retinal hemorrhage|authorities|social service|report|consent|confidential|dnr|refus"),
   ("CPR / anaphylaxis / burns / drowning", r"cpr|cardiac arrest|resuscitation|compression|drowning|burn|anaphyla|epinephrine|bite|shock"),
   ("Other emergency", r".")]),
]
SYSORDER = ["Neonatology", "Growth, development & nutrition", "Vaccines & infectious disease", "Respiratory & ENT", "Cardiology",
            "GI & surgery", "Nephrology & urology", "Neurology", "Hematology & oncology", "Endocrine, genetics & metabolic",
            "Musculoskeletal & rheumatology", "Emergency, poisoning & child abuse"]
