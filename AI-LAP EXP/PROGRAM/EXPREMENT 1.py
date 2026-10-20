from collections import deque

# Goal state
goal = "123456780"

# Possible moves of the blank space
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def solve(start):
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()

        # Check goal
        if state == goal:
            return path + [state]

        # Find blank position
        blank = state.index("0")

        # Generate next states
        for pos in moves[blank]:
            new_state = list(state)
            new_state[blank], new_state[pos] = new_state[pos], new_state[blank]
            new_state = "".join(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    return None


# Input
start = input("Enter the puzzle (use 0 for blank): ")

solution = solve(start)

# Display solution
if solution:
    print("\nSolution:")
    for state in solution:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("No solution exists.")
