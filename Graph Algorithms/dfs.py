#depth first search
def dfs_recursive(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")

            # Push unvisited neighbors onto the stack
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)  # Push unvisited neighbor onto the stack

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['F', 'H'],
    'F': ['A'],
    'G': ['H'],
    'H': ['D']
}

start_vertex = 'A'

print("Depth-First Traversal (Recursive):")
dfs_recursive(graph, start_vertex, set())

print("\nDepth-First Traversal (Stack):")
dfs_stack(graph, start_vertex)


