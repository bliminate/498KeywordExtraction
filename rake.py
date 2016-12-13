import re
from collections import defaultdict

def get_stopwords(stopwords_file):
    with open(stopwords_file, 'r') as myfile:
        text = myfile.read()
    return text.split('\n')

def build_regex(stopwords_file):
    stopword_list = get_stopwords(stopwords_file)
    stopword_regex_list = []
    for stopword in stopword_list:
        stopword_regex = r'\b' + stopword + r'(?![\w-])'
        stopword_regex_list.append(stopword_regex)
    stop_regex = re.compile('|'.join(stopword_regex_list), re.IGNORECASE)
    return stop_regex

def get_sentences(text_file):
    with open(text_file, 'r') as myfile:
        text = myfile.read()
    punctuation_regex = re.compile('[.,!?:;\n\"\'()-]')
    sentences = punctuation_regex.split(text)
    return sentences

def get_candidate_keywords(stop_regex, sentences):
    candidate_keywords = []
    for sentence in sentences:
        sentence_keywords = stop_regex.split(sentence)
        for keyword in sentence_keywords:
            if keyword != '':
                candidate_keywords.append(keyword.strip())
    return candidate_keywords

def make_keyword_sentences_dict(keywords, sentences):
    keyword_sentences = defaultdict(list)
    for keyword in keywords:
        for sentence in sentences:
            if keyword in sentence:
                keyword_sentences[keyword].append(sentence.strip())
    return keyword_sentences

def RAKE(stoplist_file, text_file):
    stop_regex = build_regex(stoplist_file)
    sentences = get_sentences(text_file)
    candidate_keywords = get_candidate_keywords(stop_regex, sentences)
    keyword_sentences = make_keyword_sentences_dict(candidate_keywords, sentences)
    return keyword_sentences
