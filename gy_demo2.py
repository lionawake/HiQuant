from hikyuu.interactive.interactive import *
from datetime import datetime,timedelta
import pandas as pd
import numpy as np
import talib as tb

cwd = os.getcwd()
print("Demo:".ljust(15), cwd)
sys.path.append(cwd)

import LqDB as lqdb
import LqFinance as lqfin
import factors as lqidc

sp_id = 202
s_id = 0
if len(sys.argv) >= 2:
    sp_id = int(sys.argv[1])
if len(sys.argv) >= 3:
    s_id = int(sys.argv[2])

def dump_profit_day(stocks,days):
    """
    导出一个策略的每天净利润数据，需在策略回测完成后调用，策略的资产组合可包含多个股票
    :param stocks: 策略的股票组合
    :param days:   回测的天数
    usage::
    >>> sp = ['sz000002','sz000004','sz000008','sz000010']
    >>> dump_profit_day(sp,500)
    """
    for s in stocks:
        k = s.getKData(Query(-days))
        x = my_tm.getProfitCurve(k.getDatetimeList(), KQuery.DAY)
        z = PRICELIST(x)
        z -= z
        break

    for s in stocks:
        k = s.getKData(Query(-days))
        x = my_tm.getProfitCurve(k.getDatetimeList(), KQuery.DAY)
        if (len(x) == days):
            z += PRICELIST(x)
    d = k.getDatetimeList()
    p = []
    for i in range(len(z)):
        t = []
        t.append(d[i].number)
        t.append(z[i])
        p.append(t)
    return str(p)

def dump_profit_month(stocks,days):
    """
    导出一个策略的每月净利润数据，需在策略回测完成后调用，策略的资产组合可包含多个股票
    :param stocks: 策略的股票组合
    :param days:   回测的天数
    usage::
    >>> sp = ['sz000002','sz000004','sz000008','sz000010']
    >>> dump_profit_month(sp,500)
    """
    for s in stocks:
        k = s.getKData(Query(-days))
        x = my_tm.getProfitCurve(k.getDatetimeList(), KQuery.DAY)
        z = PRICELIST(x)
        z -= z
        break

    for s in stocks:
        k = s.getKData(Query(-days))
        x = my_tm.getProfitCurve(k.getDatetimeList(), KQuery.DAY)
        if (len(x) == days):
            z += PRICELIST(x)
    # cal monthly data from daily data
    #k = stocks[0].getKData(Query(-days))
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

#sp = ['sz000002','sz000004','sz000008','sz000010']
#plot_profit_day(sp,500)


def getNextWeekDate(week):
    print('getNextWeekDate')
    py_week = week.datetime()
    next_week_start = py_week + timedelta(days=7 - py_week.weekday())
    next_week_end = next_week_start + timedelta(days=5)
    return getDateRange(Datetime(next_week_start), Datetime(next_week_end))

def dofilter(start_date, end_date, stk, max_num):
    # 按市值升序排列选出最大数量的股票
    print('dofilter')
    '''
    start_date=start_date
    end_date=end_date
    s = stk
    max_num=max_num
    '''
    sMarket = []
    for s in blocka:
        stk = s.getWeight()
        stkValue = s.getMarketValue(end_date, KQuery.KType.DAY)
        sMarket.append((s.market_code, stkValue * stk[len(stk) - 1].totalCount))
    # print(s.code,stkValue*stk[len(stk)-1].totalCount)
    arr1 = np.array(sMarket, dtype=[('stock', np.str_, 8), ('market', int)])
    arr2 = np.sort(arr1, order='market')
    arr2 = arr2[:max_num]
    # 选出的股票代码
    stk = Block()
    # my_block.category='self'
    # my_block.name ='1'
    for stock in arr2['stock']:
        # print(getStock(stock))
        stk.add(getStock(stock))
    # stocks=sm[my_block].getBlock('self','1')

    # print(stk)
    return stk

def TurtleSG(self):
    print('TurtleSG')
    m1 = self.getParam("m1")
    m2 = self.getParam("m2")
    k = self.getTO()
    c = CLOSE(k)
    short = EMA(c, m1)
    long = EMA(c, m2)
    for i in range(0, len(k)):
        if (short[i - 1] >= long[i - 1] and short[i] < long[i]):
            self._addBuySignal(k[i].datetime)
        elif (short[i - 1] <= long[i - 1] and short[i] > long[i]):
            self._addSellSignal(k[i].datetime)

def DEMO_CN(self):
    print('DEMO_CN')
    k = self.getTO()
    if (len(k) <= 1):
        return
    week_q = QueryByDate(k[0].datetime, k[-1].datetime, kType=Query.WEEK, recoverType=Query.FORWARD)
    week_k = k.getStock().getKData(week_q)
    # week_k.plot()
    n1 = self.getParam("week_macd_n1")
    n2 = self.getParam("week_macd_n2")
    n3 = self.getParam("week_macd_n3")
    m = MACD(CLOSE(week_k), n1, n2, n3)

    fast = m.getResult(1)
    slow = m.getResult(2)
    '''
    ax1,ax2 = create_figure(2)
    week_k.plot(axes=ax1)
    ax_draw_macd(ax2,week_k,n1,n2,n3)
    '''
    # x=fast>slow
    # print(len(week_k),len(x))
    for i in range(0, len(m) - 1):
        # print(fast[i],slow[i])
        if (fast[i] > slow[i]):
            date_list = getNextWeekDate(week_k[i].datetime)
            # print(fast[i],slow[i],week_k[i].datetime)
            # print(x[i])
            # print(date_list)
            for d in date_list:
                # print(fast[i],slow[i],d)
                self._addValid(d)  # 系统有效性触发交易

class DEMO_MM(MoneyManagerBase):
    def __init__(self):
        print('_init_')
        super(DEMO_MM, self).__init__('MACD_MM')
        self.setParam('init_position', 1)
        self.next_buy_num = 0

    def _reset(self):
        print('_reset')
        self.next_buy_num = 0

    def _clone(self):
        print('_close')
        mm = DEMO_MM()
        mm.next_buy_num = self.next_buy_num

    def _getBuyNumber(self, datetime, stk, price, risk, part_from):  # 由多个地方触发，这里是信号指示器和系统有效性

        tm = self.getTM()
        cash = tm.currentCash
        if part_from == System.Part.CONDITION:
            num = int(cash * self.getParam('init_position') // price // 100) * 100
            # self.next_buy_num=num
            print('_getBuyNumber', datetime, part_from, num)
            return int(cash * self.getParam('init_position') // price // 100) * 100

        print('_getBuyNumber', datetime, part_from, self.next_buy_num)
        return self.next_buy_num  # 返回的是需要买入股票的证券数量

    def _getSellNumber(self, datetime, stk, price, risk, part_from):  # 这个程序的触发是通过_getBuyNumber函数返回的值来判断的，若是0就不会被触发

        tm = self.getTM()
        position = tm.getPosition(stk)
        current_num = int(position.number)
        if self.next_buy_num == 0:
            print('_getSellNumber',datetime,part_from, current_num)
            self.next_buy_num = current_num

        print('_getSellNumber', datetime, part_from, current_num)
        return current_num  # 返回的是当前持仓股票的证券数量

    def buyNotify(self, trade_record):
        print('buyNotify', trade_record)

    def sellNotify(self, trade_record):
        print('sellNotify', trade_record)


cn_open_position = True

init_cash = 500000
init_date = '1998-1-1'
week_n1 = 12
week_n2 = 26
week_n3 = 9
max_num = 40
stk = [sm['sz000001'], sm['sz000002']]

start_date = Datetime('2018-01-01')
end_date = Datetime.now()

#stk = dofilter(start_date, end_date, stk, max_num)
# 创建模拟交易账户进行回测，初始资金50万
my_tm = crtTM(datetime=Datetime(init_date), initCash=init_cash)

# 创建交易系统并运行
my_sys = SYS_Simple()
my_sys.setParam("cn_open_position", cn_open_position)
my_sys.tm = my_tm

my_sys.cn = crtCN(DEMO_CN, {'week_macd_n1': week_n1, 'week_macd_n2': week_n2, 'week_macd_n3': week_n3},
                  'DEMO_CN')  # 系统有效性
# print(help(OP))
# my_sys.sg=SG_Cross(OP(EMA(n=week_n1)),OP(EMA(n=week_n2)))   #信号指示器触发交易

my_sys.mm = DEMO_MM()
my_sys.sg = crtSG(TurtleSG, {'m1': week_n1, 'm2': week_n2}, 'TurtleSG')

q = QueryByDate(start_date, end_date, kType=Query.DAY, recoverType=Query.FORWARD)
db = lqdb.SqlDB('192.168.54.11', 3306, 'root', 'lq2018', 'lq')
for s in stk:
    my_sys.run(s, q)
    per = Performance()
    per.report(my_tm, Datetime.now())
    db.save_strategy_test(sp_id, s_id, 'sz000001', cwd, per)

day = dump_profit_day(stk, 100)
month = dump_profit_month(stk, 100)
print(day)
print(month)
db.update_strategy_perf(sp_id, s_id, day, month)
