from collections import deque

# State = (Missionaries on left, Cannibals on left, Boat position)
# Boat position: 0 = Left, 1 = Right

def is_valid(m, c):
    # Number of people cannot be negative or greater than 3
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    # Missionaries should not be outnumbered by cannibals
    if m > 0 and c > m:
        return False

    # Check the right side also
    rm = 3 - m
    rc = 3 - c

    if rm > 0 and rc > rm:
        return False

    return True


def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    # Possible boat movements
    moves = [
        (1, 0),  # 1 missionary
        (2, 0),  # 2 missionaries
        (0, 1),  # 1 cannibal
        (0, 2),  # 2 cannibals
        (1, 1)   # 1 missionary and 1 cannibal
    ]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution:")
            for s in path:
                print(s)
            return

        for dm, dc in moves:

            if boat == 0:
                new_state = (m - dm, c - dc, 1)
            else:
                new_state = (m + dm, c + dc, 0)

            if is_valid(new_state[0], new_state[1]):
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))


solve()
