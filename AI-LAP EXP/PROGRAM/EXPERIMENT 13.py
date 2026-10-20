
def minimax(tree, maximizing):
    if isinstance(tree, int):
        return tree

    scores = [minimax(child, not maximizing) for child in tree]

    if maximizing:
        return max(scores)
    return min(scores)

game_tree = [
    [3, 5],
    [2, 9],
    [12, 5]
]

best_score = minimax(game_tree, True)

print("Game Tree:", game_tree)
print("Best Score:", best_score)
