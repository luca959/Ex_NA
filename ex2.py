import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

#import graph
#G = nx.read_edgelist("email-enron-only.mtx", nodetype=int) 

G = nx.karate_club_graph()
x=[]
betwenness={}
closeness={}

print("Node Degree")
for v in G:
    print(f"{v:4} {G.degree(v):6}")
    x.append(G.degree(v))
betwenness=nx.betweenness_centrality(G)
closeness=nx.closeness_centrality(G)
#plot first 10 values of betwenness and closeness
betwenness=sorted(betwenness.items(), key=lambda item: item[1],reverse=True)
closeness=sorted(closeness.items(), key=lambda item: item[1],reverse=True)
print("Node Betwennessness top 10")
for v in range(0,10):
    print(f"{v} {betwenness[v]}")

print("Node Closeness top 10")
for v in range(0,10):
    print(f"{v} {closeness[v]}")

plt.hist(x)
plt.show()

plt.hist(betwenness.values())
plt.show()

plt.hist(closeness.values())
plt.show()


nx.draw_circular(G, with_labels=False)
plt.show()