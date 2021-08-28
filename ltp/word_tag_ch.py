from ltp import LTP

ltp = LTP()
segment, hidden = ltp.seg(["武汉市长江大桥"])
print(hidden)
pos_tags=ltp.pos(hidden)
print(pos_tags)
