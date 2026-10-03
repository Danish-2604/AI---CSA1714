from collections import deque

def bfs(a, b, goal):
    q = deque([((0, 0), [])])
    visited = set()

    while q:
        (x, y), path = q.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        if x == goal or y == goal:
            return path

        states = [
            (a, y),              # Fill A
            (x, b),              # Fill B
            (0, y),              # Empty A
            (x, 0),              # Empty B
            (max(0, x-(b-y)), min(b, x+y)),  # A -> B
            (min(a, x+y), max(0, y-(a-x)))   # B -> A
        ]

        for state in states:
            if state not in visited:
                q.append((state, path))

    return None


# Jug capacities
A = 4
B = 3
goal = 2

solution = bfs(A, B, goal)

print("Steps:")
for state in solution:
    print(state)
