#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================
import os
import sys
from hikyuu.interactive.interactive import *

cwd = os.getcwd()
sys.path.append(cwd)
import LqDB as lqdb
from LqCommon import StockFilter

def getNextWeekDate(week):
    from datetime import timedelta
    py_week = week.datetime()
    next_week_start = py_week + timedelta(days = 7 - py_week.weekday())
    return Datetime(next_week_start)


def DEMO_SG(self):
    k = self.getTO()
    if (len(k) == 0):
        return

    stk = k.getStock()

    # -----------------------------
    # -----------------------------
    day_c = CLOSE(k)
    day_ma = MA(day_c, self.getParam("day_n"))
    day_x = day_c < day_ma
    for i in range(day_x.discard, len(day_x)):
        if day_x[i] >= 1.0:
            self._addSellSignal(k[i].datetime)

    # -----------------------------
    # -----------------------------
    week_q = QueryByDate(k[0].datetime, k[-1].datetime, kType=Query.WEEK)
    week_k = k.getStock().getKData(week_q)

    n1 = self.getParam("week_macd_n1")
    n2 = self.getParam("week_macd_n2")
    n3 = self.getParam("week_macd_n3")
    m = MACD(CLOSE(week_k), n1, n2, n3)
    fast = m.getResult(0)
    slow = m.getResult(1)

    discard = m.discard if m.discard > 1 else 1
    for i in range(discard, len(m)):
        if (fast[i - 1] < slow[i - 1] and fast[i] > slow[i]):
            self._addBuySignal(getNextWeekDate(week_k[i].datetime))


class DEMO_MM(MoneyManagerBase):
    def __init__(self):
        super(DEMO_MM, self).__init__("MACD_MM")

    def _reset(self):
        pass

    def _clone(self):
        return DEMO_MM()

    def _getBuyNumber(self, datetime, stk, price, risk, part_from):
        tm = self.getTM()
        cash = tm.currentCash

        num = int((cash * 0.3 // price // stk.atom) * stk.atom)
        # print("buy: ", num)
        return num

    def _getSellNumber(self, datetime, stk, price, risk, part_from):
        tm = self.getTM()
        position = tm.getPosition(stk)
        total_num = position.number
        num = total_num * 0.5
        atom_num = (num // stk.atom) * (stk.atom + 1)

        num = int(num if num < atom_num else atom_num)
        # print("sell: ", num)
        return num

init_cash = 100000
init_date = Datetime('1990-1-1')

week_n1 = 12
week_n2 = 26
week_n3 = 9
day_n = 20

stk = sm['sz000001']
start_date = Datetime('2017-01-01')
end_date = Datetime()

my_tm = crtTM(datetime=init_date, initCash = init_cash)

my_sys = SYS_Simple()

my_sys.tm = my_tm

my_sys.sg = crtSG(DEMO_SG,
              {'week_macd_n1': week_n1, 'week_macd_n2': week_n2, 'week_macd_n3': week_n3, 'day_n': day_n},
                'DEMO_SG')

my_sys.mm = DEMO_MM()

q = QueryByDate(start_date, end_date, kType=Query.DAY)
my_sys.run(stk, q)

my_tm.tocsv(sm.tmpdir())

x = my_tm.getProfitCurve(stk.getDatetimeList(q), KQuery.DAY)
#x = my_tm.getFundsCurve(stk.getDatetimeList(q), KQuery.DAY)
x = PRICELIST(x)
x.plot()

per = Performance()
print(per.report(my_tm, Datetime.now()))
db = lqdb.SqlDB('127.0.0.1', 3306, 'hikyuu', 'hikyuu', 'hikyuu')
db.save_strategy_test(1, 1, 'sz000001', cwd, per)

# Database
