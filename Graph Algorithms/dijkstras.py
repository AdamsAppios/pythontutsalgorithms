import heapq

def dijkstra(graph, source):
    # Initialize distances and priority queue
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if the current distance is greater than the recorded distance
        if current_distance > distances[current_vertex]:
            continue

        # Update distances for neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

source_vertex = 'A'
shortest_distances = dijkstra(graph, source_vertex)

print("Shortest distances from vertex", source_vertex, "to all other vertices:")
print(shortest_distances)