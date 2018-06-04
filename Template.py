#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================
import os
import sys
from hikyuu.interactive.interactive import *
from hikyuu.indicator import *
cwd = os.getcwd()
sys.path.append(cwd)
import LqDB as lqdb
import factors as lqidc

#FPDF:  function parameters default value
#FPDFL: function parameters default value list
if lqidc.$$F:[0]$(1,2,3) > $$P:[10-11,15]$ and lqidc.$$F:[2,3]$() <= $$P:0.1, 0.5, 0.2$:
    #print('if case')
    pass
else:
    if lqidc.$$F:[6]$(888) > $$P:[100]$:
        #print('else if case')
        pass
    #print('else case')
    pass
pass

# Database
#per = Performance()
#db = lqdb.SqlDB('127.0.0.1', 3306, 'hikyuu', 'hikyuu', 'hikyuu')
#db.save_strategy_test(1, 1, 'sz000001', cwd, per)
