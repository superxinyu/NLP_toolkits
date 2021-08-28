from ltp import LTP


#  中文分词
ltp = LTP()
segment, hidden = ltp.seg(["武汉市长江大桥"])
print(segment)
