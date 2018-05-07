#from matplotlib import *
#from matplotlib.lines import Line2D

from hikyuu.interactive.interactive import *
use_draw_engine('echarts')

#创建模拟交易账户进行回测，初始资金30万
my_tm = crtTM(initCash = 300000)

#创建信号指示器（以5日EMA为快线，5日EMA自身的10日EMA最为慢线，快线向上穿越慢线时买入，反之卖出）
my_sg = SG_Flex(OP(EMA(n=5)), slow_n=10)

#固定每次买入1000股
my_mm = MM_FixedCount(1000)

#创建交易系统并运行
sys = SYS_Simple(tm = my_tm, sg = my_sg, mm = my_mm)
sys.run(sm['sz000001'], Query(-150))

#绘制系统信号
sys.plot()

k = sm['sz000001'].getKData(Query(-150))
c = CLOSE(k)
fast = EMA(c, 5)
slow = EMA(fast, 10)

#绘制信号指示器使用两个指标
fast.plot(new=False)
slow.plot(new=False)

#绘制资金收益曲线
x = my_tm.getProfitCurve(k.getDatetimeList(), KQuery.DAY)
x = PRICELIST(x)
x.plot()

#回测统计
from datetime import datetime

per = Performance()
print(per.report(my_tm, Datetime(datetime.today())))

'''
from datetime import datetime

def test_func(stock, query):
    """计算指定stock的系统策略胜率，系统策略为之前的简单双均线交叉系统（每次固定买入100股）
    """
    # 创建模拟交易账户进行回测，初始资金30万
    my_tm = crtTM(initCash=1000000)

    # 创建信号指示器（以5日EMA为快线，5日EMA自身的10日EMA最为慢线，快线向上穿越慢线时买入，反之卖出）
    my_sg = SG_Flex(OP(EMA(n=5)), slow_n=10)

    # 固定每次买入1000股
    my_mm = MM_FixedCount(100)

    # 创建交易系统并运行
    sys = SYS_Simple(tm=my_tm, sg=my_sg, mm=my_mm)
    sys.run(stock, query)

    per = Performance()
    print(per.report(my_tm, Datetime(datetime.today())))
    per.statistics(my_tm, Datetime(datetime.today()))
    return per.get("赢利交易比例%".encode('gb2312'))


def total_func(blk, query):
    """遍历指定板块的所有的股票，计算系统胜率"""
    result = {}
    for s in blk:
        if s.valid and s.type != constant.STOCKTYPE_INDEX:
            result[s.name] = test_func(s, query)
    return result

a = total_func(sm, Query(-500))
len(a)
'''
