
% Medical Diagnosis System

% Symptoms of diseases
symptom(fever, flu).
symptom(cough, flu).
symptom(headache, flu).
symptom(body_pain, flu).

symptom(fever, malaria).
symptom(chills, malaria).
symptom(sweating, malaria).
symptom(headache, malaria).

symptom(cough, cold).
symptom(sneezing, cold).
symptom(runny_nose, cold).
symptom(sore_throat, cold).

% Diagnosis rules
diagnose(Patient, Disease) :-
    has_symptom(Patient, Symptom),
    symptom(Symptom, Disease).

% Patient symptoms
has_symptom(john, fever).
has_symptom(john, cough).
has_symptom(john, headache).
has_symptom(john, body_pain).

% Display diagnosis
medical_diagnosis(Patient, Disease) :-
    diagnose(Patient, Disease),
    write('Patient: '), write(Patient), nl,
    write('Possible Disease: '), write(Disease), nl.
