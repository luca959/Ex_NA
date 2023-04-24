import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

#import graph
G = nx.read_edgelist("email-enron-only.mtx", nodetype=int) 

#G = nx.karate_club_graph()
x=[]
print("Node Degree")
for v in G:
    print(f"{v:4} {G.degree(v):6}")
    x.append(G.degree(v))


plt.hist(x)
plt.show()

nx.draw_circular(G, with_labels=False)
plt.show()