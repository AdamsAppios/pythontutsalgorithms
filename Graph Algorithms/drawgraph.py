import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
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

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Draw the graph
pos = nx.spring_layout(G)  # Layout algorithm for node positions
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black', font_weight='bold')
plt.title("Graph Visualization")
plt.show()