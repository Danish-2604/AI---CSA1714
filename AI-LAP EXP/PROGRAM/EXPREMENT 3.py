from collections import deque

def water_jug(jug1, jug2, target):
    queue = deque([(0, 0)])
    visited = set([(0, 0)])

    while queue:
        a, b = queue.popleft()
        print(a, b)

        if a == target or b == target:
            print("Target reached!")
            return

        states = [
            (jug1, b),  # Fill Jug 1
            (a, jug2),  # Fill Jug 2
            (0, b),     # Empty Jug 1
            (a, 0),     # Empty Jug 2

            # Pour Jug 1 into Jug 2
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),

            # Pour Jug 2 into Jug 1
            (a + min(b, jug1 - a), b - min(b, jug1 - a))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No solution exists.")

# Example: 4-litre and 3-litre jugs, target = 2 litres
water_jug(4, 3, 2)
