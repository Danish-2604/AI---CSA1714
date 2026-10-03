def solve(board, row):
    if row == 8:
        print(board)
        return True

    for col in range(8):

        # Check if queen can be placed
        if col not in board and \
           all(abs(row-r) != abs(col-c)
               for r, c in enumerate(board)):

            board.append(col)

            if solve(board, row + 1):
                return True

            board.pop()       # Backtrack

    return False


board = []
solve(board, 0)

print("Queen positions:", board)
