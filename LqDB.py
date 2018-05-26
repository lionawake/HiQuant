#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql as MySQLdb


class SqlDB():
    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PWD, DB_NAME):
        self.DB_HOST = DB_HOST
        self.DB_PORT = DB_PORT
        self.DB_USER = DB_USER
        self.DB_PWD = DB_PWD
        self.DB_NAME = DB_NAME

        self.conn = MySQLdb.Connect(
            host=self.DB_HOST,
            port=self.DB_PORT,
            user=self.DB_USER,
            passwd=self.DB_PWD,
            db=self.DB_NAME,
            charset='utf8'
        )

    def query(self, sqlstr):
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        returnData = cursor.fetchall()
        cursor.close()
        return returnData

    def update(self, sqlstr):
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        self.conn.commit()
        cursor.close()

    def save_strategy_pattern(self, name, author, status, task_total, task_finished, code):
        sqlstr = """insert into lq_strategy_pattern
            (sp_name,author,test_status,task_total,task_finished,code) 
            values (%s,%s,%d,%ld,%ld,%s);"""
        cursor = self.conn.cursor()
        cursor.execute(sqlstr,name, author, status, task_total, task_finished, code)
        self.conn.commit()
        cursor.close()

    def save_strategy(self, sp_id, code, path):
        sqlstr = "insert into lq_strategy(sp_id,code,data_path) values (%ld,%s,%s);"
        cursor = self.conn.cursor()
        cursor.execute(sqlstr, sp_id, code, path)
        self.conn.commit()
        cursor.close()

    def save_strategy_test(self, sp_id, s_id, stock, path, perf):
        sqlstr = """insert into lq_strategy_test 
                    (sp_id, s_id, stock, data_path,
                    net_profit,
                    total_profit,
                    total_loss,
                    total_profit_loss,
                    trade_lot,
                    profit_ratio,
                    average_profit,
                    average_loss,
                    average_profit_loss,
                    max_profit,
                    max_loss,
                    max_total_profit,
                    max_total_loss,
                    average_hold_period,
                    max_fund_use,
                    yield_rate,
                    annual_return,
                    r_square_yield_curve,
                    hold_period_ratio
                    ) 
                    values
                    """
        cursor = self.conn.cursor()
        d1 = perf["已平仓净利润总额".encode('gbk')]
        d2 = perf["赢利交易赢利总额".encode('gbk')]
        d3 = perf["亏损交易亏损总额".encode('gbk')]
        d4 = perf["已平仓交易总数".encode('gbk')]
        d5 = perf["赢利交易比例%".encode('gbk')]
        d6 = perf["赢利交易平均赢利".encode('gbk')]
        d7 = perf["亏损交易平均亏损".encode('gbk')]
        d8 = perf["最大单笔赢利".encode('gbk')]
        d9 = perf["最大单笔亏损".encode('gbk')]
        d10 = perf["赢利交易平均持仓时间".encode('gbk')]
        d11 = perf["单笔交易最大占用现金比例%".encode('gbk')]
        d12 = perf["已平仓帐户收益率%".encode('gbk')]
        d13 = perf["帐户年复合收益率%".encode('gbk')]
        d14 = perf["R乘数期望值".encode('gbk')]
        d15 = perf["空仓时间/总时间%".encode('gbk')]
        s = sqlstr + '(%ld,'%sp_id + '%ld,'%s_id + '\'%s\','%stock + '\'%s\','%path + '%f,'%d1\
        + '%f,' % d2 + '%f,'%d3 + '0,%f,'%d4 + '%f,'%d5 + '%f,'%d6 + '%f,'%d7 + '0,%f,'%d8\
        + '%f,'%d9 + '0,0,%f,'%d10 + '%f,'%d11\
        + '%f,' % d12 + '%f,'%d13 + '%f,'%d14 + '%f);'%d15
        print(s)
        cursor.execute(s)
        #cursor.execute(sqlstr, (sp_id, s_id, stock, path,
        #               d1,d2,d3,0,int(d4),d5,d6,d7,0,d8,d9,0,
        #               0,int(d10),d11,d12,d13,d14,d15))
        self.conn.commit()
        cursor.close()

    def update_strategy_perf(self, sp_id, s_id, perf):
        sqlstr = """update lq_strategy set 
                    net_profit = %f,
                    total_profit = %f,
                    total_loss = %f,
                    total_profit_loss = %f,
                    trade_lot = %d,
                    profit_ratio = %f,
                    average_profit = %f,
                    average_loss = %f,
                    average_profit_loss = %f,
                    max_profit = %f,
                    max_loss = %f,
                    max_total_profit = %f,
                    max_total_loss = %f,
                    average_hold_period = %d,
                    max_fund_use = %f,
                    yield_rate = %f,
                    annual_return = %f,
                    r_square_yield_curve = %f,
                    hold_period_ratio = %f 
                    where 
                    sp_id = %ld and s_id = %ld;"""
        cursor = self.conn.cursor()
        cursor.execute(sqlstr,
                       perf["已平仓净利润总额"],
                       perf["赢利交易赢利总额"],
                       perf["亏损交易亏损总额"],
                       perf["赢利交易赢利总额"] / perf["亏损交易亏损总额"],
                       perf["已平仓交易总数"],
                       perf["赢利交易比例%"],
                       perf["赢利交易平均赢利"],
                       perf["亏损交易平均亏损"],
                       perf["赢利交易平均赢利"] / perf["亏损交易平均亏损"],
                       perf["最大单笔赢利"],
                       perf["最大单笔亏损"],
                       perf["最大单笔赢利"] / perf["赢利交易赢利总额"],
                       perf["最大单笔亏损"] / perf["亏损交易亏损总额"],
                       perf["赢利交易平均持仓时间"],
                       perf["单笔交易最大占用现金比例"],
                       perf["已平仓帐户收益率"],
                       perf["帐户年复合收益率"],
                       perf["R乘数期望值"],
                       100 - perf["空仓时间/总时间%"],
                       sp_id, s_id)
        self.conn.commit()
        cursor.close()

    def update_task_stat(self, wait, run, over):
        sqlstr = """update lq_task_stat set
                    task_wait = %ld,
                    task_run = %ld,
                    task_over = %ld;"""
        cursor = self.conn.cursor()
        cursor.execute(sqlstr,wait,run,over)
        self.conn.commit()
        cursor.close()

if __name__ == "__main__":
    db = SqlDB('127.0.0.1', 3306, 'hikyuu', 'hikyuu', 'hikyuu')
    print(db.query("show tables;"))
