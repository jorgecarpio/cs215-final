#
# Take a weighted graph representing a social network where the weight
# between two nodes is the "love" between them.  In this "feel the
# love of a path" problem, we want to find the best path from node `i`
# and node `j` where the score for a path is the maximum love of an
# edge on this path. If there is no path from `i` to `j` return
# `None`.  The returned path doesn't need to be simple, ie it can
# contain cycles or repeated vertices.
#
# Devise and implement an algorithm for this problem.
#
from IPython import embed
import random

def feel_the_love(G, i, j):
    path = []
    segments = []
    girl = ''
    boy = ''
    love = 0

    if G[j] == {}: return None # catches lonely dest nodes
    # finds max love
    for node in G:
        for neighbor in G[node]:
            if G[node][neighbor] > love:
                boy = node
                girl = neighbor
                love = G[node][neighbor]

    
    start = i
    path.append(start)
    while path[-1] != j or (((girl, boy) not in segments) and ((boy, girl) not in segments)):
        #walk the path
        next = random.choice(G[start].keys())
        segments.append((start, next))
        path.append(next)
        start = next
        

    return path

#########
#
# Test

def score_of_path(G, path):
    max_love = -float('inf')
    for n1, n2 in zip(path[:-1], path[1:]):
        love = G[n1][n2]
        if love > max_love:
            max_love = love
    return max_love

def test():
    G = {'a':{'c':1},
         'b':{'c':1},
         'c':{'a':1, 'b':1, 'e':1, 'd':1},
         'e':{'c':1, 'd':2},
         'd':{'e':2, 'c':1},
         'f':{}}
    path = feel_the_love(G, 'a', 'b')
    assert score_of_path(G, path) == 2

    path = feel_the_love(G, 'a', 'f')
    assert path == None

test()
