#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================
import LqFilter as lqf

def get_func_name_list(src):
    s = src.strip('[')
    s = s.strip(']')
    res = []
    l = s.split(',')
    for x in l:
        t = x.split('-')
        if len(t) == 1:
            n = int(t[0])
            res.append(lqf.stock_func_list[n])
        else:
            min = int(t[0])
            max = int(t[1]) + 1
            r = range(min, max)
            for y in r:
                n = int(y)
                res.append(lqf.stock_func_list[n])
    return res

func_name_dict = {}
py_str = "if $$F:[1-5,8]$($$P:100-101$):"

print(py_str)
str_len = len(py_str)
remain_len = str_len
pos_s = 0
pos_e = 0
while (remain_len > 0):
    cut_res = lqf.str_cut('$$F:', '$', py_str[pos_e:])
    if cut_res == -1:
        break
    pos_s = cut_res[0]
    pos_e = cut_res[1]
    func_name = get_func_name_list(py_str[pos_s:pos_e])
    pos_s -= 4
    pos_e += 1
    func_name_dict[py_str[pos_s:pos_e]] = func_name
    remain_len -= pos_e
print(func_name_dict)
