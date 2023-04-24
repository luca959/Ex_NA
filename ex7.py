import networkx as nx
import matplotlib.pyplot as plt

# Load or create a network (in this example, we create a random graph)
G = nx.gnm_random_graph(10, 20)

# Compute degree of each node
degrees = dict(G.degree())
print("Degrees:", degrees)

# Compute average degree of neighbors for each node
neighbor_degrees = {}
for node in G.nodes():
    neighbors = list(G.neighbors(node))
    neighbor_degree_sum = sum(degrees[neighbor] for neighbor in neighbors)
    neighbor_degrees[node] = neighbor_degree_sum / len(neighbors) if len(neighbors) > 0 else 0
print("Neighbor degrees:", neighbor_degrees)
nx.draw(G, with_labels=True)
plt.show()
