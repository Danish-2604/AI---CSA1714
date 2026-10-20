from collections import deque

def is_safe(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False

    if m_left > 0 and m_left < c_left:
        return False

    if m_right > 0 and m_right < c_right:
        return False

    return True


def solve():
    # State: (missionaries_left, cannibals_left, boat_side)
    # boat_side: 0 = left, 1 = right

    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            for step in path + [state]:
                print(step)
            return

        # Possible boat movements
        moves = [(1, 0), (2, 0), (0, 1),
                 (0, 2), (1, 1)]

        for dm, dc in moves:
            if boat == 0:
                new_m = m - dm
                new_c = c - dc
                new_boat = 1
            else:
                new_m = m + dm
                new_c = c + dc
                new_boat = 0

            m_right = 3 - new_m
            c_right = 3 - new_c

            if is_safe(new_m, new_c, m_right, c_right):
                new_state = (new_m, new_c, new_boat)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append(
                        (new_state, path + [state])
                    )

    print("No solution exists.")


solve()
