student(john).
student(mary).
student(sam).

teacher(mr_smith).
teacher(mrs_jones).
teacher(mr_brown).

subject(math, 'MATH101').
subject(english, 'ENG201').
subject(science, 'SCI301').

teaches(mr_smith, math).
teaches(mrs_jones, english).
teaches(mr_brown, science).

enrolled(john, math).
enrolled(mary, english).
enrolled(sam, science).
enrolled(john, science).

% Rules
teaches_subject_code(Teacher, Subject, Code) :-
    teaches(Teacher, Subject),
    subject(Subject, Code).

student_enrolled_in_subject(Student, Subject, Code) :-
    enrolled(Student, Subject),
    subject(Subject, Code).

student_taught_by(Student, Teacher) :-
    enrolled(Student, Subject),
    teaches(Teacher, Subject).
