#
# Write a function, `bipartite` that
# takes as input a graph, `G` and tries
# to divide G into two sets where 
# there are no edges between elements of the
# the same set - only between elements in
# different sets.
# If two sets exists, return one of them
# or `None` otherwise
# Assume G is connected
#
from IPython import embed

def bipartite(G):
    side1 = set() # should be sets to avoid dupes; check iter
    side2 = set()
    checked = []

    # seed it
    seed = G.iterkeys().next()
    side1.add(seed)
    for neighbor in G[seed]:
        side2.add(neighbor)
    checked.append(seed)
    while len(checked) < len(G):
        # for loop to check side1
        for node in side1: # e.g. 'a'
            if node not in checked:
                for neighbor in G[node]: # e.g. 'd' and 'e'
                    if neighbor in side1:
                        return None
                    side2.add(neighbor)
            checked.append(node)

        # for loop to check side2
        for node in side2:
            if node not in checked:
                for neighbor in G[node]: 
                    if neighbor in side2:
                        return None
                    side1.add(neighbor)
            checked.append(node)
    return side1


    # let's call left with the first node 'a'

    # def left(node):
    #     left.append(node)
    #     for neighbor in G[node]:
    #         # checks to see if neighbor is on same side
    #         if neighbor in left:
    #             return None
    #         right.append(neighbor)
    #     checked.append(node)
    #     for node in right:
    #         if node not in checked:
    #             if right(node) == None:
    #                 return None   

    # def right(node):
    #     for neighbor in G[node]:
    #         if neighbor in right:
    #             return None # how to handle this in callback
    #         left.append(neighbor)
    #     checked.append(node)

    # return None


########
#
# Test

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G


def test():
    edges = [(1, 2), (2, 3), (1, 4), (2, 5),
             (3, 8), (5, 6)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert (g1 == set([1, 3, 5]) or
            g1 == set([2, 4, 6, 8]))
    edges = [(1, 2), (1, 3), (2, 3)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert g1 == None

G = {'a': {'d':1, 'e':1}, 'b': {'d':1, 'e':1}, 'c': {'e': 1, 'f': 1}, 
    'd':{'a':1, 'b':1}, 'e':{'a':1, 'b':1, 'c':1}, 'f':{'c'}}

print test()
