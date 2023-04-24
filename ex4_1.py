import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
import math
from random import randrange


def EvaluateRegime(numberOfNodes, probability):
    if probability > math.log(numberOfNodes)/numberOfNodes:
        print("The regime is Connected")
    elif probability > 1/numberOfNodes:
        print("The regime is Supercritical")
    elif probability == 1/numberOfNodes:
        print("The regime is Critical")
    elif probability < 1/numberOfNodes:
        print("The regime is Subcritical")


if __name__ == '__main__':
    numberOfNodes = 3000
    prob = pow(10, (-3))
    print("Probability is: ", prob)
    G = nx.fast_gnp_random_graph(numberOfNodes, prob)
    nx.draw_random(G, node_size=40, alpha=0.5, with_labels=False)

    expNumOfLinks = list(combinations(G.nodes, 2)).__len__()*prob
    # np.random.binomial(G.number_of_nodes(), prob)
    print("Expected number of links is: ", int(expNumOfLinks))

    EvaluateRegime(numberOfNodes, prob)
    print("The probability p so that the network is in a critical point is: ", 1/numberOfNodes)

    connectedGraph = 2  # not 1 because it is obvious it is gonna be okay
    while prob <= math.log(connectedGraph)/connectedGraph:
        connectedGraph += 1
    print("The number of nodes so that the network has only one component is: ", connectedGraph)

    newG = nx.fast_gnp_random_graph(connectedGraph, prob)
    if nx.is_connected(newG):
        randomNode1 = randrange(0, connectedGraph)
        randomNode2 = randrange(0, connectedGraph)
        print("The average degree of node ", randomNode1, " is: ", newG.degree(randomNode1)/connectedGraph)
        print("The average degree of node ", randomNode2, " is: ", newG.degree(randomNode2)/connectedGraph)
        print("The average shortest path is: ", nx.average_shortest_path_length(newG))
        print("The shortest path between the nodes is: ", nx.shortest_path(newG, randomNode1, randomNode2))
    else:
        print("Graph is not connected")

