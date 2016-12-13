from CoOccurrence import CoGraph
from POSTagger import applypostagging
from rake import RAKE
import sys

if len(sys.argv) == 3:
  input_data_file = sys.argv[1]
  stopwords_file = sys.argv[2]
else:
  print('Improper Usage: [data file] [stop-word file]')

keyword_dict = RAKE(stopwords_file, input_data_file)
keyword_sentence_dict = applypostagging(keyword_dict)

co_occurrence = CoGraph()
co_occurrence.createGraph(keyword_sentence_dict)
co_occurrence.calcScore()

for key, value in co_occurrence.scores.iteritems():
  print(key + ': ' + str(value))

