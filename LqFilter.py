#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================
#from hikyuu.interactive.interactive import *
import re

class StockFilter:
    '筛选公共类'
    def __init__(self, stock):
        #print(self.__doc__)
        pass
    def __del__(self):
        pass

    def stock_filter000(self):
        return 1000

    def stock_filter001(self):
        return 1000

    def stock_filter002(self):
        return 100

    def stock_filter003(self):
        pass

    def stock_filter004(self):
        pass

    def stock_filter005(self):
        pass

    def stock_filter006(self):
        pass

    def stock_filter007(self):
        pass

    def stock_filter008(self):
        pass

#获取StockFilter全部筛选函数
stock_func_list = list(filter(lambda x: x.startswith('stock_filter') and callable(getattr(StockFilter,x)), dir(StockFilter)))

def str_cut(start, end, src):
    s = src.find(start)
    if s >= 0:
        s += len(start)
        e = src.find(end, s)
        if e >= 0:
            return [s, e]
    return -1

py_str = "if $$F:2$($$P:A1$) and $$F:5$($$P:B1$, $$P:B2$, $$P:B3$)" \
         "and $$F:8$($$P:C1$, $$P:C2$, $$P:C3$, $$P:C4$, $$P:C5$):"
print(py_str)
str_len = len(py_str)
remain_len = str_len
while (remain_len > 0):
    cut_res = str_cut('$$F:', '$', py_str)
    if cut_res == -1:
        break
    pos_s = cut_res[0]
    pos_e = cut_res[1]
    func_num = int(py_str[pos_s:pos_e])
    func_name = stock_func_list[func_num]
    pos_s -= 4
    pos_e += 1
    new_str = "StockFilter(s).%s" % func_name
    py_str = py_str.replace(py_str[pos_s:pos_e], new_str, 1)
    str_len += (len(new_str) - (pos_e - pos_s))
    remain_len = str_len - pos_e

    #print(func_name)
    #print(cut_res)
    #print(py_str)

    while (remain_len > 0):
        pos_f = py_str.find('$$F:')
        pos_p = py_str.find('$$P:')
        if pos_p < 0:
            #print('b1')
            break
        if pos_f > 0 and pos_p > 0 and pos_f <= pos_p:
            #print('b2')
            break
        cut_res = str_cut('$$P:', '$', py_str)
        if cut_res == -1:
            #print('b3')
            break
        pos_s = cut_res[0]
        pos_e = cut_res[1]
        new_str = py_str[pos_s:pos_e]
        #print(new_str)
        pos_s -= 4
        pos_e += 1
        py_str = py_str.replace(py_str[pos_s:pos_e], new_str, 1)
        str_len += (len(new_str) - (pos_e - pos_s))
        remain_len = str_len - pos_e
        print(py_str)


tmp_str2 = "if $$F:[1-3, 6-9]$($$P:$, $$P:$, $$P:$):"
#res_str2 = str_cut('$$F:', '$', tmp_str2)
#print(res_str2)
