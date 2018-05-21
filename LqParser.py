#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================
import LqFilter as lqf
import os

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

py_str_file = os.getcwd() + "\Policy.log"
print(py_str_file)
fd = fd = open(py_str_file, "w+")
func_name_dict = {}
func_para_dict = {}
py_str = "#FPDF:  function parameters default value\n" \
         "#FPDFL: function parameters default value list\n" \
         "if $$F:[1-3,8]$(FPDF, FPDFL, FPDF) > 10 and $$F:[9,10]$(FPDF, FPDF, FPDF, FPDFL, FPDFL) <= 3000:\n" \
         "    if $$F:[3-6,12]$(FPDF) == True:\n" \
         "        todo\n" \
         "    else:\n" \
         "        todo\n" \
         "else:\n" \
         "    todo\n" \
         "todo\n"

#py_str = "if $$F:[1-5,8]$($$P:1-5,18,100-101, a-c, xyz, TRUE$, $$P:2018$, $$P:8888$) and $$F:[9,10]$($$P:6,100-105,30$):"
#py_str = "if $$F:[1-2,3]$($$P:1-3$, $$P:2018$):"
remain_str = py_str
fd.write("Source Python Code:\n")
fd.write(py_str + '\n')
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
            break
        if pos_f > 0 and pos_p > 0 and pos_f <= pos_p:
            break
        cut_res = lqf.str_cut('$$P:', '$', remain_str)
        if cut_res == -1:
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

fd.write("Functions:" + '\n')
fd.write(str(func_name_dict) + '\n\n')
fd.write("Parameters:" + '\n')
fd.write(str(func_para_dict) + '\n\n')
fd.write("Destination Python code:" + '\n')

import itertools as its

ll = []
for f_key in func_name_dict:
    f_list = func_name_dict[f_key]
    ll.append(f_list)

i = 0
policy_count = 0
replace_str = py_str
for l in its.product(*ll):
    i = 0
    policy_count += 1
    replace_str = py_str
    for f_key in func_name_dict:
        replace_str = replace_str.replace(f_key, l[i])
        i += 1
    fd.write("#===================================================================Policy%03d\n"%policy_count)
    fd.write(replace_str + '\n')
fd.close()
print("OK")
