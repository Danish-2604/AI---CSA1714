graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2},
    'C': {'D': 1},
    'D': {}
}

h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

open_list = [(h['A'], 0, 'A')]
path = []

while open_list:
    open_list.sort()
    f, cost, node = open_list.pop(0)

    if node in path:
        continue

    path.append(node)

    if node == 'D':
        print("Path:", path)
        print("Cost:", cost)
        break

    for next_node in graph[node]:
        new_cost = cost + graph[node][next_node]
        open_list.append(
            (new_cost + h[next_node], new_cost, next_node)
        )
