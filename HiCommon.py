# -*- coding: UTF-8 -*-
from hikyuu.interactive.interactive import *
from datetime import datetime
import hikyuu.trade_sys._trade_sys

log_file = "D:\Workspace\LQ\hi.log"

class HikyuuArgs:
    i_cash = 0
    func_sg = ''
    func_mm = ''
    list_sg = []
    list_mm = []
    a_stock = []
    o_qry = 0
    id = ''
    id_desc = ''

    def __init__(self, cash, stock, query_list_str, signal, signal_list_str, mmFixed, mm_list_str, tactics):
        self.i_cash = cash
        self.a_stock = stock
        query_list = query_list_str[0].split(',')
        self.o_qry = Query(int(query_list[0]))
        self.func_sg = signal
        self.list_sg = signal_list_str
        self.func_mm = mmFixed
        self.list_mm = mm_list_str
        self.id = tactics[0]
        self.id_desc = tactics[1]
        pass

class HikyuuCommon_old:
    i_cash = 0
    o_tm = 0
    o_sg = 0
    o_mm = 0
    i_ema_n = 0
    i_slow_n = 0
    o_hi_sys = 0
    res_file = 0
    i_count = 0
    func_sg = ''
    func_mm = ''

    def __init__(self, cash, signal, ema, slow, mmFixed, mm):
        self.i_cash = cash
        self.i_ema_n = ema
        self.i_slow_n = slow
        self.func_sg = getattr(hikyuu.trade_sys._trade_sys, signal)
        self.func_mm = getattr(hikyuu.trade_sys._trade_sys, mmFixed)
        print(self.func_sg)
        print(self.func_mm)
        # 创建模拟交易账户进行回测，初始资金
        self.o_tm = crtTM(initCash=cash)
        # 创建信号指示器
        #self.sg = SG_Flex(OP(EMA(n=self.ema_n)), slow_n=self.slow_n)
        self.o_sg = self.func_sg(OP(EMA(n=self.i_ema_n)), slow_n=self.i_slow_n)
        # 固定每次买入
        #self.mm = MM_FixedCount(mm)
        self.o_mm = self.func_mm(mm)
        # 创建交易系统
        self.o_hi_sys  = SYS_Simple(tm=self.o_tm, sg=self.o_sg, mm=self.o_mm)
        self.res_file = open(log_file, 'w+')

    def __del__(self):
        self.res_file.close()

    def __common_func(self, stock, query):
        # 交易系统运行
        self.o_hi_sys.run(stock, query)

        per = Performance()
        self.i_count += 1
        self.res_file.write('%06d++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' % self.i_count + '\n')
        self.res_file.write(per.report(self.o_tm, Datetime(datetime.today())))
        self.res_file.write('\n')
        per.statistics(self.o_tm, Datetime(datetime.today()))
        return per.get("赢利交易比例%".encode('gb2312'))

    def cycle(self, block, query):
        result = {}
        for s in block:
            if s.valid and s.type != constant.STOCKTYPE_INDEX:
                result[s.name] = self.__common_func(s, query)
        return result

class HikyuuCommon:
    i_cash = 0
    o_tm = 0
    o_sg = 0
    o_mm = 0
    i_ema_n = 0
    i_slow_n = 0
    o_hi_sys = 0
    res_file = 0
    i_count = 0
    func_sg = ''
    func_mm = ''
    a_stock = []
    o_qry = 0
    id = ''
    id_desc = ''

    def __init__(self, args):
        if isinstance(args, HikyuuArgs) == False:
            raise ValueError
        self.i_cash = args.i_cash
        self.a_stock = args.a_stock
        self.o_qry = args.o_qry
        self.i_ema_n = int(args.list_sg[0].split(',')[0])
        self.i_slow_n = int(args.list_sg[1].split(',')[0])
        self.func_sg = getattr(hikyuu.trade_sys._trade_sys, args.func_sg)
        self.func_mm = getattr(hikyuu.trade_sys._trade_sys, args.func_mm)
        mm = int(args.list_mm[0].split(',')[0])
        #print(self.func_sg)
        #print(self.func_mm)
        self.id = args.id
        self.id_desc = args.id_desc

        # 创建模拟交易账户进行回测，初始资金
        self.o_tm = crtTM(initCash=self.i_cash)
        # 创建信号指示器
        #self.sg = SG_Flex(OP(EMA(n=self.ema_n)), slow_n=self.slow_n)
        self.o_sg = self.func_sg(OP(EMA(n=self.i_ema_n)), slow_n=self.i_slow_n)
        # 固定每次买入
        #self.mm = MM_FixedCount(mm)
        self.o_mm = self.func_mm(mm)
        # 创建交易系统
        self.o_hi_sys  = SYS_Simple(tm=self.o_tm, sg=self.o_sg, mm=self.o_mm)
        self.res_file = open(log_file, 'w+')

    def __del__(self):
        self.res_file.close()

    def __common_func(self, stock, query):
        # 交易系统运行
        self.o_hi_sys.run(stock, query)

        per = Performance()
        self.i_count += 1
        self.res_file.write('%s'%self.id_desc + '\n')
        self.res_file.write('%06d++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++' % self.i_count + '\n')
        self.res_file.write(per.report(self.o_tm, Datetime(datetime.today())))
        self.res_file.write('\n')
        per.statistics(self.o_tm, Datetime(datetime.today()))
        return per.get("已平仓帐户收益率%".encode('gb2312'))

    def running(self):
        block = self.a_stock
        query = self.o_qry
        result = {}
        for s in block:
            if s.valid and s.type != constant.STOCKTYPE_INDEX:
                self.res_file.write('%s'%s.name+'\n')
                result[s.name] = self.__common_func(s, query)
        return result
