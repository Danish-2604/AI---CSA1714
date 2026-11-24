
% Monkey Banana Problem

% Initial state:
% Monkey is at door, box is at window,
% banana is hanging at middle.

% Facts
at(monkey, door).
at(box, window).
at(banana, middle).

% Rules
move(monkey, X, Y) :-
    at(monkey, X),
    X \= Y.

push_box(X, Y) :-
    at(monkey, X),
    at(box, X),
    X \= Y.

climb :-
    at(monkey, middle),
    at(box, middle).

get_banana :-
    climb,
    at(banana, middle).

% Goal condition
can_get_banana :-
    move(monkey, door, window),
    push_box(window, middle),
    climb,
    get_banana.
