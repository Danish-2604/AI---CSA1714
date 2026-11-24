
% Best First Search Algorithm

% Graph representation
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).
edge(d, h).
edge(e, h).
edge(f, h).
edge(g, h).

% Heuristic values
h(a, 7).
h(b, 6).
h(c, 4).
h(d, 5).
h(e, 3).
h(f, 2).
h(g, 1).
h(h, 0).

% Best First Search
best_first(Start, Goal, Path) :-
    search([[Start]], Goal, ReversePath),
    reverse(ReversePath, Path).

search([[Goal|Rest]|_], Goal, [Goal|Rest]).

search([ [Node|Path] | Others], Goal, Result) :-
    findall([Next,Node|Path],
            (edge(Node, Next),
             \+ member(Next, [Node|Path])),
            Children),
    append(Others, Children, NewOpen),
    sort_paths(NewOpen, SortedOpen),
    search(SortedOpen, Goal, Result).

% Sort paths based on heuristic value
sort_paths(Paths, Sorted) :-
    map_list_to_pairs(path_heuristic, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

path_heuristic([Node|_], H) :-
    h(Node, H).

% Query
% ?- best_first(a, h, Path).
