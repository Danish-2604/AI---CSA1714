def is_safe(board, row, col):
    for i in range(row):
        # Same column
        if board[i] == col:
            return False

        # Diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row):
    if row == 8:
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col

            if solve(board, row + 1):
                return True

            board[row] = -1

    return False


# Create empty board
board = [-1] * 8

# Solve the problem
if solve(board, 0):
    print("Solution:")
    for row in range(8):
        for col in range(8):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution exists")
