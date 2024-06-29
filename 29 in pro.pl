symptom(john, fever).
symptom(john, cough).
symptom(john, chills).
symptom(john, body_ache).

% Rules: Define when a specific disease can be diagnosed
rule(flu, [fever, chills, body_ache, cough]).
rule(cold, [sneezing, cough, sore_throat, runny_nose]).
rule(covid19, [fever, dry_cough, tiredness, difficulty_breathing]).
rule(allergy, [sneezing, runny_nose, itchy_eyes, headache]).

% Forward chaining mechanism
forward_chaining(Person, Disease) :-
    rule(Disease, Symptoms),
    check_symptoms(Person, Symptoms).

check_symptoms(_, []).
check_symptoms(Person, [Symptom|Rest]) :-
    symptom(Person, Symptom),
    check_symptoms(Person, Rest).

% Add new facts (symptoms) dynamically
add_symptom(Person, Symptom) :-
    assertz(symptom(Person, Symptom)).
