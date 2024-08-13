import heapq

def dijkstra(graph, start, end):
    # Initialize distances and predecessors
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            path = []
            while current_node:
                path.append(current_node)
                current_node = predecessors[current_node]
            return path[::-1], distances[end]

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return None, float('inf')

# Example usage
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

start = 'A'
end = 'F'

path, distance = dijkstra(graph, start, end)
print(f"Shortest path from {start} to {end}: {' -> '.join(path)}")
print(f"Total distance: {distance}")