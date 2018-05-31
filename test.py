#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================

'''
#FPDF:  function parameters default value
#FPDFL: function parameters default value list
sf = StockFilter('')
if sf.$$F:[1-2,8]$() > $$P:[10-11,15]$ and sf.$$F:[9,10]$() <= $$P:0.1, 0.5, 0.2$:
    if sf.$$F:[3-5]$() == $$P:8, 10, 2$:
        pass
    else:
        pass
else:
    pass
pass
'''

class test:
    def test_func1(self):
        return 6,7,8

def func1(x=10, y=20, z=['a','b','c']):
    return 1,2,3

a = func1()
b = (1,1,5)
if a < b:
    print('a<b')

print(a)
b = func1()[0]
print(b)

c = test()
d = c.test_func1()[0]
print(d)

print(test().test_func1().__doc__)
print(func1.__defaults__)
print(func1.__code__.co_argcount)
print(func1.__code__)

import LqIndicator

gFuncList = list(filter(lambda x: callable(getattr(LqIndicator, x)), dir(LqIndicator)))
print(gFuncList)
gFuncRetList = []
for f in gFuncList:
    pass