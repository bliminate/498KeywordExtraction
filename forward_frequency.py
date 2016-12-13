import fileinput
import re
import sys
from sklearn import preprocessing
import hashlib

#takes in keyword_map of keywords w/ frequencies as values & text file as a string
def forward_freq_calc(keyword_map, textfile):
	t = open(textfile, "r")
	line = t.readline()

	ffreq_dict = {}
	paragraphs = 0
	occurred = False

	#grab total # of paragraphs within textfile
	while line:
		#for each class chunk
		while line.strip() != '':
			line = t.readline()
		paragraphs+=1
		line = t.readline()


	#for each key, go through entire textfile and calculate forward frequency
	for key, value in keyword_map.iteritems():
		freq = 0
		ffreq = 0

		t = open(textfile, "r")
		line = t.readline()


		while line:
			#for each class chunk
			while line.strip() != '':
				line = line.strip()
				
				#for word in sentence:
				if line.find(key) != -1:
					#increase frequency once per paragraph if word is found
					if occurred == False:
						freq+=1
						occurred = True

				line = t.readline()

			#at end of a paragraph
			occurred = False

			#get rid of blank line
			line = t.readline()

		#after going through entire doc, calculate forward frequency and store
		ffreq = float(keyword_map[key])*float(freq)/float(paragraphs)

		#add keyword candidate to keyword_map with value of its forward frequency
		ffreq_dict[key] = ffreq



	return ffreq_dict

keyword_map = {
  'Present': 1, 'Scalable Distributed Information Management System (SDIMS)': 1, 'aggregates information': 1,
  'large-scale networked systems': 1, 'large-scale distributed applications': 1,
  'information': 1, 'summary': 1, 'global': 1, 'information': 1
}

#dict = {}
#dict = forward_freq_calc(keyword_map, "testdoc.txt")


#for word in dict:
#	print word
#	print dict[word]

