from hikyuu.interactive.interactive import *

def func(data, n=10, fast_n=2, slow_n=30):
    print(n)
    print(fast_n)
    print(slow_n)
    return

def LQ_AMA(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
	data = close
	return func(data, n=n1, fast_n=n2, slow_n=n3)

k = sm['sz000001'].getKData(Query(-150))
print(k)
c = CLOSE(k)

x = LQ_AMA(c, n2=111)

print(x)
