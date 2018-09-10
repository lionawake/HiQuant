#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================
from hikyuu.interactive.interactive import *
def dump_profit_day(stocks, q, my_tm, kType=KQuery.DAY):
    """
    导出一个策略的每天净利润数据，需在策略回测完成后调用，策略的资产组合可包含多个股票
    :param stocks: 策略的股票组合
    :param days:   回测的天数
    usage::
    >>> sp = ['sz000002','sz000004','sz000008','sz000010']
    >>> dump_profit_day(sp,500)
    """
    # print(stocks)
    for s in stocks:
        k = s.getKData(q)
        x = my_tm.getProfitCurve(k.getDatetimeList(), kType)
        z = PRICELIST(x)
        break
    d = k.getDatetimeList()
    p = []
    print("len(z)=%d" % len(z))
    for i in range(len(z)):
        t = []
        t.append(d[i].number)
        t.append(z[i])
        p.append(t)
    return str(p)

def dump_profit_month(stocks, q, my_tm, kType=KQuery.DAY):
    """
    导出一个策略的每月净利润数据，需在策略回测完成后调用，策略的资产组合可包含多个股票
    :param stocks: 策略的股票组合
    :param days:   回测的天数
    usage::
    >>> sp = ['sz000002','sz000004','sz000008','sz000010']
    >>> dump_profit_month(sp,500)
    """
    for s in stocks:
        k = s.getKData(q)
        x = my_tm.getProfitCurve(k.getDatetimeList(), kType)
        z = PRICELIST(x)
        break
    d = k.getDatetimeList()
    m = 0
    p = []
    for i in range(len(z)):
        if (d[i].month != m):
            m = d[i].month
            t = []
            t.append(d[i].number)
            t.append(z[i])
            p.append(t)
    return str(p)
