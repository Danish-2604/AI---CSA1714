graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    # Visit the current node
    visited.add(node)
    print(node, end=" ")

    # Visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Run DFS starting from node 'A'
print("DFS Traversal:")
dfs(graph, 'A')
