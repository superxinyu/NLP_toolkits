"""
    去除英文停用词
"""

import nltk
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
stopwords = nltk.corpus.stopwords.words('english')
print(stopwords)

emma = [w.lower() for w in emma]
emma_without_stopwords = [w for w in emma if w not in stopwords]
print(emma_without_stopwords)
