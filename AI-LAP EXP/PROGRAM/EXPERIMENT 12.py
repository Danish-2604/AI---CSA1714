
board = [" "] * 9

def display():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-" * 5)

def winner():
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in lines:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

player = "X"

while " " in board:
    display()
    try:
        pos = int(input(f"Player {player}, enter position (1-9): ")) - 1
        if pos not in range(9) or board[pos] != " ":
            print("Invalid position. Try again.")
            continue
    except ValueError:
        print("Enter a number from 1 to 9.")
        continue

    board[pos] = player

    if winner():
        display()
        print("Player", winner(), "wins!")
        break

    player = "O" if player == "X" else "X"
else:
    display()
    print("Match Draw!")
