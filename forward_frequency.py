import fileinput
import re
import sys
import nltk.tokenize
from sklearn import preprocessing
import hashlib

#takes in dictionary of keywords w/ frequencies as values & text file as a string
def forward_freq_calc(dictionary, textfile):
	t = open(textfile, "r")
	line = t.readline()

	ffreq_dict = {}
	paragraphs = 0
	occurred = false

	#get total # of paragraphs within chunk
	while line:
		#for each class chunk
		while line.strip() != '':
			paragraphs+=1
		line = t.readline()


	t = open(textfile, "r")
	line = t.readline()


	#for each key, go through entire textfile and calculate forward frequency
	for key in dictionary.iteritems():
		freq = 0
		ffreq = 0
		while line:
			#for each class chunk
			while line.strip() != '':
				line = line.strip()
				if line == "exit": break
				block = nltk.tokenize.word_tokenize(line)
				
				for blocks in block:
					if key == blocks:
						#increase frequency once per paragraph if word is found
						if occurred == false:
							freq+=1
							occurred = true

				line = t.readline()

			#at end of a paragraph
			occurred = false

			#get rid of blank line
			line = t.readline()

		#after going through entire doc, calculate forward frequency and store
		ffreq = dictionary[key]*freq/paragraphs

		#add keyword candidate to dictionary with value of its forward frequency
		ffreq_dict[key] = ffreq

	return ffreq_dict


