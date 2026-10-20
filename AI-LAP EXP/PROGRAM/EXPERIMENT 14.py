
def alpha_beta(tree, alpha, beta, maximizing):
    if isinstance(tree, int):
        return tree

    if maximizing:
        value = float("-inf")
        for child in tree:
            value = max(
                value,
                alpha_beta(child, alpha, beta, False)
            )
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    else:
        value = float("inf")
        for child in tree:
            value = min(
                value,
                alpha_beta(child, alpha, beta, True)
            )
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

game_tree = [[3, 5], [2, 9], [12, 5]]

result = alpha_beta(
    game_tree, float("-inf"), float("inf"), True
)

print("Optimal Score:", result)
