"""
    根据情感词典计算情感得分
"""

import nltk

sentence = ['welcome', 'to', 'harbin', 'institute', 'of', 'technology']

sentence_tag = nltk.pos_tag(sentence)

tag_map = {'NN': 'n', 'NNP': 'n', 'NNPS': 'n', 'NNS': 'n', 'UH': 'n', \
           'VB': 'v', 'VBD': 'v', 'VBG': 'v', 'VBN': 'v', 'VBP': 'v', 'VBZ': 'v', \
           'JJ': 'a', 'JJR': 'a', 'JJS': 'a', \
           'RB': 'r', 'RBR': 'r', 'RBS': 'r', 'RP': 'r', 'WRB': 'r'}

sentence_tag = [(t[0], tag_map[t[1]]) if t[1] in tag_map else (t[0], '') for t in sentence_tag]

# sentiwordnet情感词典
sentiment_synsets = [list(nltk.corpus.sentiwordnet.senti_synsets(t[0], t[1])) for t
                     in sentence_tag]

score = sum(sum([x.pos_score() - x.neg_score() for x in s]) / len(s) for s in sentiment_synsets if len(s) != 0)

print(score)
# result: 0.3125
