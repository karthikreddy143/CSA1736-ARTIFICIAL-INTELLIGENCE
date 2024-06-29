symptom(flu, fever).
symptom(flu, chills).
symptom(flu, body_ache).
symptom(flu, cough).

symptom(cold, sneezing).
symptom(cold, cough).
symptom(cold, sore_throat).
symptom(cold, runny_nose).

symptom(covid19, fever).
symptom(covid19, dry_cough).
symptom(covid19, tiredness).
symptom(covid19, difficulty_breathing).

symptom(allergy, sneezing).
symptom(allergy, runny_nose).
symptom(allergy, itchy_eyes).
symptom(allergy, headache).

% Rules: Diagnose disease based on symptoms
disease(Disease) :-
    symptom(Disease, Symptom1), symptom(Disease, Symptom2),
    symptom(Disease, Symptom3), symptom(Disease, Symptom4),
    write('Possible disease: '), write(Disease), nl.

% Interactive diagnosis
diagnose :-
    write('Answer the following questions with yes or no.'), nl,
    check_symptom(fever),
    check_symptom(chills),
    check_symptom(body_ache),
    check_symptom(cough),
    check_symptom(sneezing),
    check_symptom(sore_throat),
    check_symptom(runny_nose),
    check_symptom(dry_cough),
    check_symptom(tiredness),
    check_symptom(difficulty_breathing),
    check_symptom(itchy_eyes),
    check_symptom(headache),
    find_disease.

% Check for symptoms
check_symptom(Symptom) :-
    write('Do you have '), write(Symptom), write('? (yes/no): '),
    read(Response),
    ( Response == yes -> assert(user_symptom(Symptom)) ; true ).

% Find possible disease
find_disease :-
    ( disease(Disease),
      symptom(Disease, Symptom1), user_symptom(Symptom1),
      symptom(Disease, Symptom2), user_symptom(Symptom2),
      symptom(Disease, Symptom3), user_symptom(Symptom3),
      symptom(Disease, Symptom4), user_symptom(Symptom4)
    -> write('You may have: '), write(Disease), nl
    ;  write('No diagnosis could be made based on the given symptoms.'), nl
    ).

% Clear user symptoms before new diagnosis
clear_symptoms :-
    retractall(user_symptom(_)).
