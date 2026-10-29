% Facts
planet(mercury, 1).
planet(venus, 2).
planet(earth, 3).
planet(mars, 4).
planet(jupiter, 5).
planet(saturn, 6).
planet(uranus, 7).
planet(neptune, 8).

% Query to display planet details
display_planet(Name) :-
    planet(Name, Number),
    write('Planet Name: '), write(Name), nl,
    write('Position from Sun: '), write(Number), nl.

% Query to find planets
find_planet(Number, Name) :-
    planet(Name, Number).