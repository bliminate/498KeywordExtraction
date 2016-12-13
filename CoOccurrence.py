
# Vertex class represents a vertex in the Co-Occurrence graph.
# Each vertex contains a word (the vertex), a set of edges,
# or other words that it is connected to, and a number for
# the frequency or number of times the word/vertex occurs.
class Vertex:
  def __init__(self):
    self.word = ''
    self.edges = set()
    self.frequency = 0
    return

  # function to initialize the word of the vertex
  def setWord(self, w):
    self.word = w

  # function to add an edge to a vertex
  def addEdge(self, e):
    self.edges.add(e)

  # function to increment the number of occurrences
  # of a vertex.
  def incFrequency(self):
    self.frequency += 1

Vertex()

# CoGraph represents the Co-Occurrence graph. The graph instance
# variable stores a dictionary representation of the graph. The
# keys of the dictionary are the word or vertex, the values are
# instances of the vertex class for the word.
# The keywords instance variable is a copy of the candidate keyword
# dictionary, extracted from the text files.
# The scores instance variable is a dictionary with the keys being
# the candidate keywords, and the values the graph score for each
# keyword candidate.
class CoGraph:
  def __init__(self):
    self.graph = {}
    self.scores = {}
    self.keywords = {}
    return

  # Member function to create the dictionary representation of the
  # co-occurrence graph.
  def createGraph(self, keyword_map):
    self.keywords = keyword_map
    for key in keyword_map:
      words = key.split()
      for word in words:
        if word in self.graph:
          self.graph[word].incFrequency()
          for w in words:
            if w == word:
              continue
            self.graph[word].addEdge(w)
        else:
          v = Vertex()
          v.setWord(word)
          v.incFrequency()
          for w in words:
            if w == word:
              continue
            v.addEdge(w)
          self.graph[word] = v
    return

  # Member function to create the dictionary containing the candidate
  # keywords, and their respective scores.
  def calcScore(self):
    for key in self.keywords:
      key_score = 0.0
      words = key.split()
      for word in words:
        key_score += float(len(self.graph[word].edges)) / float(self.graph[word].frequency)

      self.scores[key] = key_score
    return
CoGraph()


keyword_map = {
  'Present': 1, 'Scalable Distributed Information Management System (SDIMS)': 1, 'aggregates information': 1,
  'large-scale networked systems':1, 'large-scale distributed applications':1,
  'information':1, 'summary':1, 'global':1, 'information':1
}

#g = CoGraph()
#g.createGraph(keyword_map)
#g.calcScore()

#for key, value in g.scores.iteritems():
#  print(key + ': ' + str(value))
