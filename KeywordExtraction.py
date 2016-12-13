from CoOccurrence import CoGraph
from POSTagger import applypostagging
from rake import RAKE
from forward_frequency import forward_freq_calc
import sys

def sort_keywords(co_occurrence_scores, forfreq_scores):
  keywords = []

  for keyword, score in co_occurrence_scores.iteritems():
    temp_score = score + forfreq_scores[keyword]
    temp_tup = keyword, temp_score
    keywords.append(temp_tup)

  keywords.sort(key=lambda x: x[0], reverse=True)
  return keywords

def print_keywords(keywords):
  num_keys = len(keywords)/3

  for x in xrange(num_keys):
    print(keywords[x])

  return

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

ffscores = forward_freq_calc(keyword_sentence_dict, input_data_file)

keywords = sort_keywords(co_occurrence.scores, ffscores)
print_keywords(keywords)
