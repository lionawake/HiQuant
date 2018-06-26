from hikyuu.interactive.interactive import *
from datetime import datetime
import pandas as pd
import numpy as np
import talib as tb

def dofilter(start_date, end_date, stk, max_num):
    # 按市值升序排列选出最大数量的股票
    print('dofilter')
    print(blocka)
    sMarket = []
    for s in blocka:
        print(s)
        stk = s.getWeight()
        stk_len = len(stk)
        if stk_len <= 0:
            continue
        stkValue = s.getMarketValue(end_date, KQuery.KType.DAY)
        sMarket.append((s.market_code, stkValue * stk[stk_len - 1].totalCount))
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

        # 返回类型必须是int
        num = int((cash * 0.3 // price // stk.atom) * stk.atom)
        print("buy: ", num)
        return num

    def _getSellNumber(self, datetime, stk, price, risk, part_from):
        tm = self.getTM()
        position = tm.getPosition(stk)
        total_num = position.number
        num = total_num * 0.5
        atom_num = (num // stk.atom) * (stk.atom + 1)  # 卖多点

        # 返回类型必须是int
        num = int(num if num < atom_num else atom_num)
        print("sell: ", num)
        return num

    def buyNotify(self, trade_record):
        print('buyNotify', trade_record)

    def sellNotify(self, trade_record):
        print('sellNotify', trade_record)

def getNextWeekDate(week):
    """获取指定日期的下一周起始日期"""
    py_week = week.datetime()
    next_week_start = py_week + timedelta(days=7 - py_week.weekday())

    return Datetime(next_week_start)

def DEMO_SG(self):
    """
    买入信号：周线MACD零轴下方底部金叉，即周线的DIF>DEA金叉时买入
    卖出信号：日线级别 跌破 20日均线

    参数：
    week_macd_n1：周线dif窗口
    week_macd_n2: 周线dea窗口
    week_macd_n3: 周线macd平滑窗口
    day_n: 日均线窗口
    """
    k = self.getTO()
    print(k)
    if (len(k) == 0):
        return

    stk = k.getStock()

    # -----------------------------
    # 计算日线级别的卖出信号
    # -----------------------------
    day_c = CLOSE(k)
    day_ma = MA(day_c, self.getParam("day_n"))
    day_x = day_c < day_ma  # 收盘价小于均线
    for i in range(day_x.discard, len(day_x)):
        if day_x[i] >= 1.0:
            print('卖', k[i].datetime)
            self._addSellSignal(k[i].datetime)

    # -----------------------------
    # 计算周线级别的买入信号
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
            # 当周计算的结果，只能作为下周一的信号
            print('买', getNextWeekDate(week_k[i].datetime))
            self._addBuySignal(getNextWeekDate(week_k[i].datetime))

# 账户参数
init_cash = 100000  # 账户初始资金
init_date = Datetime('1990-1-1')  # 账户建立日期

# 信号指示器参数
week_n1 = 12
week_n2 = 26
week_n3 = 9
day_n = 20
max_num = 40
# 选定标的，及测试区间
stk = blocka['sh000001']
start_date = Datetime('2018-01-01')  # 如果是同一级别K线，可以使用索引号，使用了不同级别的K线数据，建议还是使用日期作为参数
end_date = Datetime.now()

q = QueryByDate(start_date, end_date, kType=Query.DAY, recoverType=Query.FORWARD)
stk = dofilter(start_date, end_date, stk, max_num)

# 创建账户
my_tm = crtTM(datetime=init_date, initCash=init_cash)

# 创建系统实例
my_sys = SYS_Simple()

# 绑定账户
my_sys.tm = my_tm

# 绑定信号指示器
my_sys.sg = crtSG(DEMO_SG,
                  {'week_macd_n1': week_n1, 'week_macd_n2': week_n2, 'week_macd_n3': week_n3, 'day_n': day_n},
                  'DEMO_SG')

# 绑定资金管理策略
my_sys.mm = DEMO_MM()

q = QueryByDate(start_date, end_date, kType=Query.DAY)
for s in stk:
    my_sys.run(s, q)
