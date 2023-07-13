import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # Initialize distances to infinity
    distances[start] = 0  # Distance from start node to itself is 0
    queue = [(0, start)]  # Priority queue to keep track of nodes to visit

    while queue:
        current_distance, current_node = heapq.heappop(queue)  # Get node with smallest distance
        if current_distance > distances[current_node]:
            continue  # Skip if we've already found a shorter path

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:  # Found a shorter path
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# Example usage
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4, 'E': 2},
    'C': {'B': 8, 'E': 7},
    'D': {'E': 6, 'F': 3},
    'E': {'F': 1},
    'F': {}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print(f"Shortest distances from node {start_node}:")
for node, distance in distances.items():
    print(f"To node {node}: {distance}")