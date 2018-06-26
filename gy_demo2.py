from hikyuu.interactive.interactive import *
from datetime import timedelta
import datetime
import time
import talib as tb

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

def TurtleSG(self):
    print('TurtleSG')
    print(self)
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
            # print('_getSellNumber',datetime,part_from, current_num)
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
stk = sm['sh000001']

start_date = Datetime('2018-01-01')
end_date = Datetime()

stk = dofilter(start_date, end_date, stk, max_num)
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

for s in stk:
    print(s)
    my_sys.run(s, q)
