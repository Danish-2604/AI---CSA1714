
% Facts
fact(rain).
fact(cloudy).

% Rules
rule(wet_ground) :-
    fact(rain).

rule(carry_umbrella) :-
    fact(rain).

rule(possible_rain) :-
    fact(cloudy).

% Forward chaining rules
derive(X) :-
    fact(X), !.

derive(X) :-
    rule(X).

% Required queries
% ?- derive(wet_ground).
% ?- derive(carry_umbrella).
% ?- derive(possible_rain).
% ?- derive(sunny).