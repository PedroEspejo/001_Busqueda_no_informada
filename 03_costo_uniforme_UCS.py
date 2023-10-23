import heapq

def ucs(graph, start, goal):
    queue = [(0, start)]
    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)
        if node == goal:
            return cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, neighbor_cost in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + neighbor_cost, neighbor))

# Ejemplo de uso
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'D': 15, 'E': 20},
    'C': {'E': 10},
    'D': {'F': 5},
    'E': {'F': 10},
    'F': {}
}
start_node = 'A'
goal_node = 'F'
print(ucs(graph, start_node, goal_node))
