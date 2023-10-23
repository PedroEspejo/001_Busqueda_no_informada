def dfs(graph, node, goal, path=[]):
    path = path + [node]
    if node == goal:
        return path
    for neighbor in graph[node]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path)
            if new_path:
                return new_path

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start_node = 'A'
goal_node = 'F'
print(dfs(graph, start_node, goal_node))
