import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import math
from random import randrange
def measure(G):
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Density:{nx.density(G)}")
    print(f"Transitivity: {nx.transitivity(G)}")
    print(f"Average Clustering: {nx.average_clustering(G)}")
    print(f"Max Degree: {max(dict(G.degree()).values())}")
    print(f"Min Degree: {min(dict(G.degree()).values())}")
    if(nx.is_connected(G)):
        print("Graph is connected")
        print(f"Diameter:{nx.diameter(G)}")
    else:
        print("Graph is not connected")


G = nx.complete_graph(100)
#draw graph
nx.draw(G, with_labels=False)
plt.show()
measure(G)