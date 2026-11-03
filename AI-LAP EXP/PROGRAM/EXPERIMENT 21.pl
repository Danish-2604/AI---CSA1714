
% Facts
parent(john, mary).
parent(mary, alice).
parent(john, peter).

% Rules
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Required Queries
% ?- parent(john, mary).
% ?- grandparent(john, alice).
% ?- grandparent(mary, alice).
% ?- grandparent(john, peter).
