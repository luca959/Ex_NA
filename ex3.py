import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def measure(G):
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Density:{nx.density(G)}")
    if(nx.is_connected(G)):
        print("Graph is connected")
        print(f"Diameter:{nx.diameter(G)}")
    else:
        print("Graph is not connected")
    for v in G:
        print(f"Node:{v:4} Degree:{G.degree(v):6}")

#create random graph
G = nx.erdos_renyi_graph(100, 0.05)
#plot graph
nx.draw(G, with_labels=False)
plt.show()
#compute measures
measure(G)


