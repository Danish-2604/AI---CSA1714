from collections import deque

# Define the graph using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    visited.append(start_node)

    while queue:
        # Remove node from front of queue
        current = queue.popleft()
        print(current, end=" ")

        # Check all unvisited neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Run BFS starting from node 'A'
print("BFS Traversal:")
bfs(graph, 'A')
