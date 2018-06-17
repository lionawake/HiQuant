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
        sqlstr = "insert into lq_strategy_pattern"+
            "(sp_name,author,test_status,task_total,task_finished,code) "+
            "values (%s,%s,%d,%ld,%ld,%s);" % (name, author, status, task_total, task_finished, code)
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        self.conn.commit()
        cursor.close()

    def save_strategy(self, sp_id, code, path):
        sqlstr = "insert into lq_strategy(sp_id,code,data_path) values (%ld,%s,%s);" % （sp_id, code, path）
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        self.conn.commit()
        cursor.close()

    def save_strategy_test(self, sp_id, s_id, stock, path, perf):
        sqlstr = """insert into lq_strategy_test 
                    (sp_id, s_id, stock, data_path,
                    net_profit, total_profit, total_loss,
                    trade_lot, profit_ratio, average_profit,
                    average_loss, max_profit, max_loss,
                    average_hold_period, max_fund_use, yield_rate,
                    annual_return, r_square_yield_curve, hold_period_ratio
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
        + '%f,' % d2 + '%f,'%d3 + '%f,'%d4 + '%f,'%d5 + '%f,'%d6 + '%f,'%d7 + '%f,'%d8\
        + '%f,'%d9 + '%f,'%d10 + '%f,'%d11\
        + '%f,' % d12 + '%f,'%d13 + '%f,'%d14 + '%f);'%d15
        print(s)
        cursor.execute(s)
        self.conn.commit()
        cursor.close()

    def update_strategy_perf(self, sp_id, s_id, perf):
        sqlsids = "select distinct(s_id) from lq_strategy_test;"
        cursor = self.conn.cursor()
        cursor.execute(sqlsids)
        sids = cursor.fetchall()
        for row in sids:
            sid = row[0]
            sqlperf = """select 
                    sum(net_profit) as sum_net_profit,
                    sum(total_profit) as sum_tot_profit,
                    sum(total_loss) as sum_tot_loss,
                    sum(trade_lot) as sum_trade_lot,
                    avg(profit_ratio) as avg_profit_ratio,
                    avg(average_profit) as avg_avg_profit,
                    avg(average_loss) as avg_avg_loss,
                    max(max_profit) as max_max_profit,
                    max(max_loss) as max_max_loss,
                    avg(average_hold_period) as avg_hold_period,
                    max(max_fund_use) as max_max_fund,
                    avg(yield_rate) as avg_yield_rate,
                    avg(annual_return) as avg_ann_ret,
                    avg(r_square_yield_curve) as avg_r_square,
                    avg(hold_period_ratio) as avg_hold_ratio 
                    from lq_strategy_test
                    where s_id = %ld;""" % sid
            cursor = self.conn.cursor()
            cursor.execute(sqlperf)
            results = cursor.fetchall()
            perfs = results[0]

            sqlupd = """update lq_strategy set 
                    net_profit = %f, total_profit = %f, total_loss = %f,
                    trade_lot = %d, profit_ratio = %f, average_profit = %f,
                    average_loss = %f, max_profit = %f, max_loss = %f,
                    average_hold_period = %d, max_fund_use = %f,
                    yield_rate = %f, annual_return = %f,
                    r_square_yield_curve = %f, hold_period_ratio = %f 
                    where s_id = %ld;""" % (perfs[0],perfs[1],perfs[2],
                       perfs[3],perfs[4],perfs[5],perfs[6],perfs[7],
                       perfs[8],perfs[9],perfs[10],perfs[11],perfs[12],
                       perfs[13],perfs[14],perfs[15],s_id)
            cursor = self.conn.cursor()
            cursor.execute(sqlupd)
            self.conn.commit()
        cursor.close()

    def update_task_stat(self, wait, run, over):
        sqlstr = """update lq_task_stat set
                    task_wait = %ld,
                    task_run = %ld,
                    task_over = %ld;""" % (wait,run,over)
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        self.conn.commit()
        cursor.close()

if __name__ == "__main__":
    db = SqlDB('127.0.0.1', 3306, 'hikyuu', 'hikyuu', 'hikyuu')
    print(db.query("show tables;"))
