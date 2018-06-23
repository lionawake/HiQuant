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

'''
rep = 'xxxxAMA(1,2,3).xxxxx > xxxxxAMA(a,b)xxx'
print(rep)
s1 = 'AMA(*)'
s2 = 'AMA(*)[0]'
rep = rep.replace(s1, s2)
print(rep)
rep = re.sub('AMA\((.*?)\)', r_replace, rep)
print(rep)

import LqFinance as lqfin
import factors as lqidc
from hikyuu.interactive.interactive import *
from hikyuu.indicator import *

my_sys = SYS_Simple()
data = CLOSE(my_sys.getTO())
lqidc.lqEMA(data,1,2)
'''

import LqIndicator

gFuncList = []
def get_func_list():
    f_l = list(filter(lambda x: callable(getattr(LqIndicator, x)), dir(LqIndicator)))
    print(f_l)
    f_num = len(f_l)
    i = 0
    while (i <= f_num):
        for f in f_l:
            l = getattr(LqIndicator, f).__doc__.split(',')
            f_id = int(l[0])
            if f_id == i:
                gFuncList.append(f)
                break
        pass
        if f_id != i:
            gFuncList.append('NULL')
        i += 1
    pass
#get_func_list()
#print(gFuncList)

def func_p2(a=1, b=2):
    print("func_p2")
    print("a=%d"%a)
    print("b=%d" % b)
    return 100

def func_p5(a=10, b=20, c=30, d=40, e=50):
    print("func_p5")
    print("a=%d" % a)
    print("b=%d" % b)
    print("c=%d" % c)
    print("d=%d" % d)
    print("e=%d" % e)
    return 200

def my_replace(s):
    s0 = s.group(0)
    s1 = s.group(1)
    s2 = s.group(2)
    s3 = s.group(3)
    l = s2.split(',')
    dst = ""
    i = 0
    paraNum = 3
    if len(l) <= paraNum:
        return s0
    for c in l:
        if i >= paraNum:
            break
        dst += c
        i += 1
        if i != paraNum:
            dst += ','

    return s1 + dst + s3

s1 = "if ABC(1,2,3,4,5,6) and CDE(x,y,z):"

print(s1)
s2 = re.sub('(ABC\()(.*?)(\))', my_replace, s1)
print(s2)
