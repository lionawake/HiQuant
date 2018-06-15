#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================
import os
import sys
import pickle
from hikyuu.interactive.interactive import *
from hikyuu.indicator import *
cwd = os.getcwd()
sys.path.append(cwd)
import LqDB as lqdb
import LqFinance as lqfin
import factors as lqidc


#账户参数
init_cash = 100000 #账户初始资金
init_date = Datetime('1990-1-1') #账户建立日期

#信号指示器参数
week_n1 = 12
week_n2 = 26
week_n3 = 9
day_n = 20

#选定标的，及测试区间
stk = sm['sz000001']
start_date = Datetime('2018-01-01')  #如果是同一级别K线，可以使用索引号，使用了不同级别的K线数据，建议还是使用日期作为参数
end_date = Datetime()

#创建账户
my_tm = crtTM(datetime=init_date, initCash = init_cash)

#创建系统实例
my_sys = SYS_Simple()

#绑定账户
my_sys.tm = my_tm
data = CLOSE(my_sys.getTO())

#FPDF:  function parameters default value
#FPDFL: function parameters default value list
if lqidc.$$F:[1]$(data,1,2,$$P:[111,222]$) > $$P:[10-11,15]$ and lqidc.$$F:[2,3]$(data) <= $$P:0.1, 0.5, 0.2$:
    #print('if case')
    pass
else:
    if lqidc.$$F:[6]$(data,$$P:[111]$) > $$P:[111]$:
        #print('else if case')
        pass
    #print('else case')
    pass
pass

if lqfin.$$F:[160]$(stk) > 100:
    pass

print(lqfin.$$F:[161]$(stk))

# Database
#per = Performance()
#db = lqdb.SqlDB('127.0.0.1', 3306, 'hikyuu', 'hikyuu', 'hikyuu')
#db.save_strategy_test(1, 1, 'sz000001', cwd, per)
#db.save_strategy_pattern()
#db.save_strategy()
