from nltk.corpus import wordnet

syns = wordnet.synsets("bank")  # 返回“bank”的全部词义
print(syns[0].name())  # 查看第一个词义的名称
print(syns[0].definition())  # 查看第一个词义的定义
print(syns[0].examples())  # 查看第一个词义的使用示例
print(syns[0].hypernyms())  # 查看第一个词义的同义词集合

#  比较两个词义的相似度，注意是词义不是单词
dog = wordnet.synset("dog.n.01")
cat = wordnet.synset("cat.n.01")
dog.wup_similarity(cat)
