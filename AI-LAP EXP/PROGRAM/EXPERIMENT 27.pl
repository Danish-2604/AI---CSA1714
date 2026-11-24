
% Facts: Fruit and their colors

fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grapes, green).
fruit_color(orange, orange).
fruit_color(mango, yellow).
fruit_color(strawberry, red).
fruit_color(guava, green).

% Rule
fruit(X, Y) :-
    fruit_color(X, Y).
