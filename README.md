# 498KeywordExtraction

## Usage
To run this code, run "python KeywordExtraction.py \<dataset-path\> \<stoplist-path\>"

## About
This repo was created by Andrew Chen, Brian Lim, Chris Raveendra, and Matt Kim as a final project for the Natural Language Processing class at the University of Michigan.

The code strives to extract keywords, or words that best capture the main idea, of input text.

Keyword extraction has invaluable uses text mining and information retrieval; it can also be used to tag articles for everyday readers looking to read documents relevant to their interests.

## Methodology
In our project we borrow several research paper methods while adding our own. They are as follows:

1. RAKE
As described in the Rose et al. paper [here](https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents), the RAKE algorithm will seperate a text on stopwords. We use the resulting phrases as keyword candidates for further processing.

2. Part of Speech Tagging
Based on the observation that keywords frequently only contain nouns, verbs, and adjectives, we tag the keyword candidates with a part of speech using a Naive Bayes algorithm and discard candidates that contain non-nouns/verbs/adjectives.

3. Scoring Keywords
We give scores to the keywords by adding the results of the following two algorithms:

  * Co-Occurence Graph
  We then score these filtered keywords using a TextRank algorithm, described in the Mihalcea and Tarau paper [here](http://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf). TextRank builds a graph using the words as vertices and relations to each other as edges. More connected words will be given a high score.
  
  * Forward Frequency
  We calculate what we call the "forward frequency" for each keyword candidate. This is inspired by TF-IDF scores used in information retrieval - it is the product of the frequency of the keyword and the number of paragraphs that contain it. Keywords that appear in more paragraphs are more likely to be the main idea across a paper.

We then pick the 5 keywords that have the highest scores as our observed results. 
