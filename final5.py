#
# Design and implement an algorithm that can preprocess a
# graph and then answer the question "is x connected to y in the
# graph" for any x and y in constant time Theta(1).
#

#
# `process_graph` will be called only once on each graph.  If you want,
# you can store whatever information you need for `is_connected` in
# global variables
#
from IPython import embed

# depth first search
def process_graph(G):
    global mydict
    
    def whodat(G, node):
        connected = set()
        left_to_visit = []
        visited = []
        left_to_visit.append(node)

        while left_to_visit:
            current = left_to_visit.pop()
            visited.append(current)
            for neighbor in G[current]:
                connected.add(neighbor)
                if neighbor not in visited:
                    left_to_visit.append(neighbor)

        return connected

    mydict = {}
    for node in G:
        mydict[node] = whodat(G, node)
    return mydict

    #return {1: [2], 2: [1], 3:[3, 4], 5: []}
    

#
# When being graded, `is_connected` will be called
# many times so this routine needs to be quick
#
def is_connected(i, j):
    return j in mydict[i]
    

#######
# Testing
#
def test():
    G = {1:{2:1},
         2:{1:1},
         3:{4:1},
         4:{3:1},
         5:{}}
    process_graph(G)
    assert is_connected(1, 2) == True
    assert is_connected(1, 3) == False

    G = {1:{2:1, 3:1},
         2:{1:1},
         3:{4:1, 1:1},
         4:{3:1},
         5:{}}
    process_graph(G)
    assert is_connected(1, 2) == True
    assert is_connected(1, 3) == True
    assert is_connected(1, 5) == False




