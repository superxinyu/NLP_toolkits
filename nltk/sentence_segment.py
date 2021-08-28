"""
    分句
"""

from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg
text=gutenberg.raw("austen-emma.txt")
sentences=sent_tokenize(text)
print(sentences[100])
