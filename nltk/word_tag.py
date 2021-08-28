"""
    词性标注
"""

import nltk.help
from nltk import pos_tag
word_tag=pos_tag(['Mr.', 'Knightley', 'loves', 'to', 'find', 'fault', 'with', 'me', ',', 'you', 'know', '--', 'in', 'a', 'joke', '--', 'it', 'is', 'all', 'a', 'joke', '.'])
print(word_tag)

# 查询tag代表的含义
nltk.help.upenn_tagset('NN')