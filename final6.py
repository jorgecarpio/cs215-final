# 
# In the shortest-path oracle described in Andrew Goldberg's
# interview, each node has a label, which is a list of some other
# nodes in the network and their distance to these nodes.  These lists
# have the property that
#
#  (1) for any pair of nodes (x,y) in the network, their lists will
#  have at least one node z in common
#
#  (2) the shortest path from x to y will go through z.
# 
# Given a graph G that is a balanced binary tree, preprocess the graph to
# create such labels for each node.  Note that the size of the list in
# each label should not be larger than log n for a graph of size n.
#

#
# create_labels takes in a balanced binary tree and the root element
# and returns a dictionary, mapping each node to its label
#
# a label is a dictionary mapping another node and the distance to
# that node
#

# linear time algorithms like Dijkstra not good enough
#sublabeling
#for each vertex it computes labels
# graph is undirected
# label is a set of vertices which we call hubs and and distances to the hubs from the vertex
# each vertex has a label and these labels must have the following property.
# If you take 2 vertices, the set of hubs has to intersect and the intersection mark
# contains a vertex on the shortest path between them.  and why it's important is that for this vertex
# if you sum up the distnaces to the 2 hubs, you will get the shortest path distance.
#  
# so the easiest way to do it is for each vertex all other vertices are at hubs, and then the property
# holds but then your queue at a time is order n, and what you really want is small labels,
# and it turns out that some graphs have more labels,
# and the reason why this works well in road networks is that we can compute labesl
# for, say, the graph of western europe with about 18 million vertices.  We can compute labesl of size 
# about 70.  It's fast.  If you sort these hubs by node id, we have 2 arrays and you just need to intersect
# these2 arrays of size 70 which you can do like a merge sort that is a very good locality.  This time
# become below a microsecond.  
def create_labels(binarytreeG, root):
    labels = {}
    # your code here
    return labels

#######
# Testing
#

def get_distances(G, labels):
    # labels = {a:{b: distance from a to b,
    #              c: distance from a to c}}
    # create a mapping of all distances for
    # all nodes
    distances = {}
    for start in G:
        # get all the labels for my starting node
        label_node = labels[start]
        s_distances = {}
        for destination in G:
            shortest = float('inf')
            # get all the labels for the destination node
            label_dest = labels[destination]
            # and then merge them together, saving the
            # shortest distance
            for intermediate_node, dist in label_node.iteritems():
                # see if intermediate_node is our destination
                # if it is we can stop - we know that is
                # the shortest path
                if intermediate_node == destination:
                    shortest = dist
                    break
                other_dist = label_dest.get(intermediate_node)
                if other_dist is None:
                    continue
                if other_dist + dist < shortest:
                    shortest = other_dist + dist
            s_distances[destination] = shortest
        distances[start] = s_distances
    return distances

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G

def test():
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7),
             (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13)]
    tree = {}
    for n1, n2 in edges:
        make_link(tree, n1, n2)
    labels = create_labels(tree, 1)
    distances = get_distances(tree, labels)
    assert distances[1][2] == 1
    assert distances[1][4] == 2

tree = {1: {2: 1, 3: 1},
 2: {1: 1, 4: 1, 5: 1},
 3: {1: 1, 6: 1, 7: 1},
 4: {2: 1, 8: 1, 9: 1},
 5: {2: 1, 10: 1, 11: 1},
 6: {3: 1, 12: 1, 13: 1},
 7: {3: 1},
 8: {4: 1},
 9: {4: 1},
 10: {5: 1},
 11: {5: 1},
 12: {6: 1},
 13: {6: 1}}