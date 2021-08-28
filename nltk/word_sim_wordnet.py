"""
    用wordnet计算两个词的相似度，计算方法为词义间最大相似度
"""

from nltk.corpus import wordnet
word1 = 'dog'
word2 = 'cat'
word1_synsets = wordnet.synsets(word1)
word2_synsets = wordnet.synsets(word2)
# path_similarity是根据wordnet路径计算相似度的方式
result = max([w1.path_similarity(w2) for w1 in word1_synsets for w2 in word2_synsets])
print(result)