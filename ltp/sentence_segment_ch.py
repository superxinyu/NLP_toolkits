from ltp import LTP

ltp = LTP()
sentences = ltp.sent_split(["我生病了。我要去医院。", "我是谁？我也不知道。"])
print(sentences)
