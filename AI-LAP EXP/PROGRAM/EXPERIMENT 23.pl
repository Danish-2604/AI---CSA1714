can_fly(sparrow).
can_fly(parrot).
can_fly(pigeon).
can_fly(eagle).
can_fly(crow).

cannot_fly(penguin).
cannot_fly(ostrich).
cannot_fly(emu).

bird_can_fly(Bird) :-
    can_fly(Bird),
    write(Bird),
    write(' can fly.').

bird_can_fly(Bird) :-
    cannot_fly(Bird),
    write(Bird),
    write(' cannot fly.').

bird_can_fly(Bird) :-
    \+ can_fly(Bird),
    \+ cannot_fly(Bird),
    write('Bird information not available.').