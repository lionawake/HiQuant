#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================
import os
import time
import datetime
import LqFilter as lqf

print(lqf.stock_func_list)
policy_id = int(time.time() * 1000000)
policy_desc = "policy_%d" % policy_id
py_file = "%s.py" % policy_desc
print(py_file)
py_fd = open(py_file, "w+")

py_str = "from hikyuu.interactive.interactive import *\n" \
         "import LqFilter as lqf\n\n" \
         "stocks=[]\n" \
         "for s in blocka:\n" \
         "    if lqf.StockFilter(s).stock_filter001() >= 100 and lqf.StockFilter(s).stock_filter002() < 1000:\n" \
         "        stocks.append(s)\n" \
         "        #print(s)\n" \
         "print(stocks)\n"

py_fd.write(py_str)
py_fd.close()

#执行通过替换指标函数后的py代码文件
local_dir = os.getcwd()
py_exe = local_dir + "\\venv\Scripts\python.exe"
os.system("%s " % py_exe + "%s" % py_file)
