def limited_cost_search(graph, start, goal, limit):
    stack = [(start, [start])]
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if len(path) < limit:
            for neighbor in graph[node]:
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}
start_node = 'A'
goal_node = 'F'
limit = 3
print(limited_cost_search(graph, start_node, goal_node, limit))
