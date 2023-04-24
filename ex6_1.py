import networkx as nx
import matplotlib.pyplot as plt

# Generate a Barabasi-Albert graph with 100 nodes and initial attachment parameter m=2
G = nx.barabasi_albert_graph(100, 2)  # m=99 avremo 99 nodi di grado 1 e 1 nodo di grado 100

# Compute measures
print("Degree of the most important hubs:", max(nx.degree(G, weight=None), key=lambda x:x[1])[1])
print("Global clustering coefficient:", nx.average_clustering(G))
print("Diameter of the network:", nx.diameter(G))
nx.draw(G, with_labels=True)
plt.show()
# Plot the degree distribution
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degree_count = nx.degree_histogram(G)
plt.hist(degree_sequence, bins='auto', density=True, log=True, label='Degree distribution')
plt.xlabel('Degree')
plt.ylabel('Probability density')
plt.title('Degree distribution of Barabási-Albert network')
plt.legend()
plt.show()
