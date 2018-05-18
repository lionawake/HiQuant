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

def get_func_para_list(src):
    s = src.strip('[')
    s = s.strip(']')
    res = []
    l = s.split(',')
    for x in l:
        t = x.split('-')
        if len(t) == 1:
            if t[0].isdigit():
                n = int(t[0])
                res.append(n)
            else:
                res.append(x.strip())
        else:
            if t[0].isdigit() and t[1].isdigit():
                min = int(t[0])
                max = int(t[1]) + 1
                r = range(min, max)
                for y in r:
                    n = int(y)
                    res.append(n)
            else:
                res.append(x.strip())
    return res


func_name_dict = {}
func_para_dict = {}
py_str = "if $$F:[1-5,8]$($$P:1-5,18,100-101, a-c, xyz, TRUE$, $$P:2018$, $$P:8888$) and $$F:[9,10]$($$P:6,100-105,30$):"
#py_str = "if $$F:[1-2,3]$($$P:1-3$, $$P:2018$):"
remain_str = py_str
print("Source Python Code:")
print(py_str)
str_len = len(py_str)
remain_len = str_len
pos_s = 0
pos_e = 0
while (remain_len > 0):
    cut_res = lqf.str_cut('$$F:', '$', remain_str)
    if cut_res == -1:
        break
    pos_s = cut_res[0]
    pos_e = cut_res[1]
    func_list = get_func_name_list(remain_str[pos_s:pos_e])
    pos_s -= 4
    pos_e += 1
    func_key = remain_str[pos_s:pos_e]
    func_name_dict[func_key] = func_list
    remain_len -= pos_e
    remain_str = remain_str[pos_e:]

    para_list_list = []
    while (remain_len > 0):
        pos_f = remain_str.find('$$F:')
        pos_p = remain_str.find('$$P:')
        if pos_p < 0:
            #print('b1')
            break
        if pos_f > 0 and pos_p > 0 and pos_f <= pos_p:
            #print('b2')
            break
        cut_res = lqf.str_cut('$$P:', '$', remain_str)
        if cut_res == -1:
            #print('b3')
            break
        pos_s = cut_res[0]
        pos_e = cut_res[1]
        para_list = get_func_para_list(remain_str[pos_s:pos_e])
        para_list_list.append(para_list)
        pos_s -= 4
        pos_e += 1
        remain_len -= pos_e
        remain_str = remain_str[pos_e:]
    func_para_dict[func_key] = para_list_list

print("Functions:")
print(func_name_dict)
print("Parameters:")
print(func_para_dict)
print("Destination Python code:")

#re_str = ""
#for f_key in func_name_dict:
#    f_list = func_name_dict[f_key]
#    for f in f_list:
#        p_n = len(func_para_dict[f_key])
#        i = 0
#        for p_list in func_para_dict[f_key]:
#            p_sz = len(p_list)
#            for p in p_list:
#                print(p)
