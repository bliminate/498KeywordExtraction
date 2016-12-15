from CoOccurrence import CoGraph
from POSTagger import applypostagging
from rake import RAKE
from forward_frequency import forward_freq_calc
import get_stuff
import sys

def sort_keywords(co_occurrence_scores, forfreq_scores):
  keywords = []

  for keyword, score in co_occurrence_scores.iteritems():
    temp_score = score + forfreq_scores[keyword]
    temp_tup = keyword, temp_score
    keywords.append(temp_tup)

  keywords.sort(key=lambda x: x[1], reverse=True)
  return keywords

def print_keywords(keywords):
  num_keys = len(keywords)/3
  for x in xrange(num_keys):
    print(keywords[x])
  return

def get_accuracy(observed, expected):
  global total_correct
  global total
  correct = 0
  for keyword in observed:
    total += 1
    if keyword[0].lower() in expected:
      total_correct += 1
      correct += 1
  return float(correct)/float(len(observed))

if len(sys.argv) == 2:
  #input_data_file = sys.argv[1]
  stopwords_file = sys.argv[1]
else:
  print('Improper Usage: [data file] [stop-word file]')

total_correct = 0
total = 0

input_files = get_stuff.get_input_files()
for input_file in input_files:
  print input_file
  print('Raking...')
  keyword_dict = RAKE(stopwords_file, input_file)
  print('POSing...')
  keyword_sentence_dict = applypostagging(keyword_dict)

  print('Co-Occurrence graphing...')
  co_occurrence = CoGraph()
  co_occurrence.createGraph(keyword_sentence_dict)
  co_occurrence.calcScore()

  print('forward frequency...')
  ffscores = forward_freq_calc(keyword_sentence_dict, input_file)

  print('sorting and printing results...')
  keywords = sort_keywords(co_occurrence.scores, ffscores)
  print_keywords(keywords)
  observed = keywords[:50]
  expected = get_stuff.get_annotations(input_file)
  accuracy = get_accuracy(observed, expected)
  print "accuracy:", accuracy
print "total correct:", total_correct
print "total:", total
print float(total_correct)/float(total)
