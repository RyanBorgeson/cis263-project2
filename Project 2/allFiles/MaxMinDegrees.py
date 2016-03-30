import numpy as np
import networkx as nx
import networkx.algorithms.approximation as naa
import sys

# Load the adjacency matrix into a numpy array.

a = np.loadtxt(sys.argv[1], dtype=int)

b = nx.from_numpy_matrix(a)

# Code taken from:
# https://networkx.github.io/documentation/latest/_modules/networkx/classes/function.html#degree
# Find the degree of every node in the graph.
# The degree has a strange mathematical property:
# A node connected to itself counts for 2...
degseq = list (b.degree().values())

#print degseq

dmax = 0
for d in degseq:
    if (d-2) > dmax:
        dmax = d-2

dmin = 8
for d in degseq:
    if (d-2) < dmin:
        dmin = d-2

#print (dmin,dmax)

# Other properties that can be
# calculated using methods in the networkx package:

# number_of_connected_components(b)
numberConnectedComponents = nx.number_connected_components(b)



# diameter(b) 
# This will work only for graphs that are connected
diameter = -1
if numberConnectedComponents == 1:
    diameter = nx.diameter(b)

#print(diameter, sizeMaxClique)


# The maximum clique is returned as a set of nodes
# max_clique(b)
maxClique = naa.max_clique(b)
sizeMaxClique = len(maxClique)

print (diameter, sizeMaxClique)

# The dominating set is returned as a set of nodes
# min_weighted_dominating_set(b)
minDominatingSet = naa.min_weighted_dominating_set(b)
sizeMinDominatingSet = len(minDominatingSet)

# The number of maximal cliques in the graph 
# graph_number_of_cliques(b)
numberOfCliques = nx.graph_number_of_cliques(b)


print (numberConnectedComponents,diameter,sizeMaxClique,sizeMinDominatingSet,numberOfCliques)
