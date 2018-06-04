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

import re
def r_replace(s):
    tmp = s.group(0)
    return tmp + '[]'

rep = 'xxxxAMA(1,2,3).xxxxx > xxxxxAMA(a,b)xxx'
print(rep)
s1 = 'AMA(*)'
s2 = 'AMA(*)[0]'
rep = rep.replace(s1, s2)
print(rep)
rep = re.sub('AMA\((.*?)\)', r_replace, rep)
print(rep)

import factors

l = list(filter(lambda x: callable(getattr(factors, x)), dir(factors)))
print(l)
