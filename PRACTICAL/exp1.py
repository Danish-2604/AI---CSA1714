from collections import deque

def bfs(start, goal):
    q = deque([(start, [])])
    visited = {start}

    while q:
        state, path = q.popleft()

        if state == goal:
            return path

        zero = state.index(0)

        for move in [-3, 3, -1, 1]:
            new = zero + move

            # Check valid move
            if 0 <= new < 9 and not (zero % 3 == 0 and move == -1) \
                         and not (zero % 3 == 2 and move == 1):

                s = list(state)
                s[zero], s[new] = s[new], s[zero]
                s = tuple(s)

                if s not in visited:
                    visited.add(s)
                    q.append((s, path + [s]))

    return None


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = bfs(start, goal)

for state in solution:
    print(state[:3])
    print(state[3:6])
    print(state[6:])
    print()
