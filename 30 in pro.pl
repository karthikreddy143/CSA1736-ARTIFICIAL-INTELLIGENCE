animal(tiger).
animal(lion).
animal(elephant).
animal(rabbit).

characteristic(tiger, carnivorous).
characteristic(lion, carnivorous).
characteristic(elephant, herbivorous).
characteristic(rabbit, herbivorous).

dangerous(tiger).
dangerous(lion).
dangerous_animal(X) :-
    animal(X),
    characteristic(X, carnivorous).
query1 :- dangerous_animal(tiger).
query2 :- dangerous_animal(rabbit).
query3 :- findall(X, dangerous_animal(X), DangerousAnimals).
query4 :- dangerous_animal(cheetah).
