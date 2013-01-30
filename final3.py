#
# In lecture, we took the bipartite Marvel graph,
# where edges went between characters and the comics
# books they appeared in, and created a weighted graph
# with edges between characters where the weight was the
# number of comic books in which they both appeared.
#
# In this assignment, determine the weights between
# comic book characters by giving the probability
# that a randomly chosen comic book containing one of
# the characters will also contain the other
#
from IPython import embed
import cPickle
marvel = cPickle.load(open("smallG.pkl", "rb"))
characters = cPickle.load(open("smallChr.pkl", "rb"))

def create_weighted_graph(bipartiteG, characters):
    G = {}
    def makealist(element, graph):
      # returns a list of books that the char is in
      # or list of chars in a book!
      return [thing for thing in graph[element]]

    for char in characters: # iterate over given list of chars
      booklist = makealist(char, bipartiteG)

      # go through book list to find add'l chars
      for book in booklist:
        charlist = makealist(book, bipartiteG)

        for char2 in charlist:
          book2list = makealist(char2, bipartiteG) # list of books char2 is in
          # now we have booklist, book2list char and char2
          together = booklist + book2list
          uniques = set(together)
          if char in G:
            G[char].update({char2: (len(together) - len(uniques)) / float(len(uniques))})
          else:
            G[char] = {char2: (len(together) - len(uniques)) / float(len(uniques))}
    return G

######
#
# Test

def test():
    bipartiteG = {'charA':{'comicB':1, 'comicC':1},
                  'charB':{'comicB':1, 'comicD':1},
                  'charC':{'comicD':1},
                  'comicB':{'charA':1, 'charB':1},
                  'comicC':{'charA':1},
                  'comicD': {'charC':1, 'charB':1}}
    G = create_weighted_graph(bipartiteG, ['charA', 'charB', 'charC'])
    # three comics contain charA or charB
    # charA and charB are together in one of them
    assert G['charA']['charB'] == 1.0 / 3
    assert G['charA'].get('charA') == None
    assert G['charA'].get('charC') == None

def test2():
    G = create_weighted_graph(marvel, characters)
