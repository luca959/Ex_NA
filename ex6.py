import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import math
from random import randrange

def measure(G):
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Density:{nx.density(G)}")
    if(nx.is_connected(G)):
        print("Graph is connected")
        print(f"Diameter:{nx.diameter(G)}")
    else:
        print("Graph is not connected")

        
sequence = nx.random_powerlaw_tree_sequence(100, tries=5000)
G = nx.configuration_model(sequence)
#compute measures
measure(G)
actual_degrees = [d for v, d in G.degree()]
#remove self-loops
G.remove_edges_from(nx.selfloop_edges(G))
#remove parallel edges
G = nx.Graph(G)
#print measures
measure(G)
#draw graph
nx.draw(G, with_labels=True)
plt.show()