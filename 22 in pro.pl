bird(pigeon, small, grey, true).
bird(eagle, large, brown, true).
bird(ostrich, large, black_and_white, false).
bird(penguin, small, black_and_white, false).
bird(sparrow, small, brown, true).

% Predicate to check if a bird can fly
can_fly(Bird) :-
    bird(Bird, _, _, true),
    write(Bird), write(' can fly.'), nl.

can_fly(Bird) :-
    bird(Bird, _, _, false),
    write(Bird), write(' cannot fly.'), nl.
parent(john, mike).
parent(john, sara).
parent(mike, anna).
parent(mike, david).
parent(sara, emma).

% Rules for relationships
father(Father, Child) :- parent(Father, Child), male(Father).
mother(Mother, Child) :- parent(Mother, Child), female(Mother).
child(Child, Parent) :- parent(Parent, Child).
sibling(Sibling1, Sibling2) :- parent(Parent, Sibling1), parent(Parent, Sibling2), Sibling1 \= Sibling2.
brother(Brother, Person) :- sibling(Brother, Person), male(Brother).
sister(Sister, Person) :- sibling(Sister, Person), female(Sister).
