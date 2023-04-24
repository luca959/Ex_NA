import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import math
from random import randrange


probability = 0.001
numberOfNodes= 3000
#create random graph
G = nx.erdos_renyi_graph(3000, 0.001)
#Expected number of links = p*N*(N-1)/2
print(f"Expected number of links: {0.001*3000*(3000-1)/2}")
#Regime of the network is connected if p>=ln(N)/N --> Connected ; p>1/N --> Supercritical ; p=1/N --> Critical ; p<1/N --> Subcritical
if probability > math.log(numberOfNodes)/numberOfNodes:
    print("The regime is Connected")
elif probability > 1/numberOfNodes:
    print("The regime is Supercritical")
elif probability == 1/numberOfNodes:
    print("The regime is Critical")
elif probability < 1/numberOfNodes:
    print("The regime is Subcritical")

#Mean degree <k>=p*N
print(f"Mean degree k: {0.001*3000}")
#Diameter <d> =ln N
print(f"Diameter d: {np.log(3000)}")

#Critical point p=1/N
print(f"The probability p so that the network is in a critical point is pc: {1/3000}")

connectedGraph = 2  # not 1 because it is obvious it is gonna be okay
while probability <= math.log(connectedGraph)/connectedGraph:
    connectedGraph += 1
print("The number of nodes so that the network has only one component is: ", connectedGraph)

newG = nx.fast_gnp_random_graph(connectedGraph, probability)
if nx.is_connected(newG):
    randomNode1 = randrange(0, connectedGraph)
    randomNode2 = randrange(0, connectedGraph)
    print("The average degree of node ", randomNode1, " is: ", newG.degree(randomNode1)/connectedGraph)
    print("The average degree of node ", randomNode2, " is: ", newG.degree(randomNode2)/connectedGraph)
    print("The average shortest path is: ", nx.average_shortest_path_length(newG))
    print("The shortest path between the nodes is: ", nx.shortest_path(newG, randomNode1, randomNode2))
else:
    print("Graph is not connected")




