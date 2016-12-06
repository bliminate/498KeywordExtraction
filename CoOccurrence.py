

class Vertex:
  def __init__(self):
    self.word = ''
    self.edges = set()
    self.frequency = 0
    return

  def setWord(self, w):
    self.word = w

  def addEdge(self, e):
    self.edges.add(e)

  def incFrequency(self):
    self.frequency += 1

Vertex()

class CoGraph:
  def __init__(self):
    self.graph = {}
    self.scores = {}
    self.keywords = {}
    return

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

g = CoGraph()
g.createGraph(keyword_map)
g.calcScore()

for key, value in g.scores.iteritems():
  print(key + ': ' + str(value))
