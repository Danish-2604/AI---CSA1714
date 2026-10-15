graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

current = 'A'
visited = [current]
cost = 0

while len(visited) < len(graph):
    next_city = min(
        (city for city in graph[current] if city not in visited),
        key=lambda city: graph[current][city]
    )

    cost += graph[current][next_city]
    visited.append(next_city)
    current = next_city

cost += graph[current]['A']
visited.append('A')

print("Route:", " -> ".join(visited))
print("Total Distance:", cost)
