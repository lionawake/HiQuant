#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import pymysql as MySQLdb
from pymongo import MongoClient

class SqlDB():
    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PWD, DB_NAME):
        self.DB_HOST = DB_HOST
        self.DB_PORT = DB_PORT
        self.DB_USER = DB_USER
        self.DB_PWD = DB_PWD
        self.DB_NAME = DB_NAME
        self.lock = threading.Lock()
        self.conn = MySQLdb.Connect(
            host=self.DB_HOST,
            port=self.DB_PORT,
            user=self.DB_USER,
            passwd=self.DB_PWD,
            db=self.DB_NAME,
            charset='utf8'
        )
        self.qa_conn = MongoClient(DB_HOST, 27017)
        self.qa_db = self.qa_conn.quantaxis    #连接quantaxis数据库，没有则自动创建
        self.qa_account = self.qa_db.account   #使用account集合，没有则自动创建
        self.qa_risk = self.qa_db.risk         #使用risk集合，没有则自动创建

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
        code = code.replace("'", "\\\'")
        code = code.replace('"', '\\\"')
        sqlstr = "insert into lq_strategy_pattern"+\
            "(sp_name,author,test_status,task_total,task_finished,code) "+\
            "values ('%s','%s',%d,%ld,%ld,'%s');" % (name, author, status, task_total, task_finished, code)
        self.lock.acquire()
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        self.conn.commit()
        cursor.close()
        self.lock.release()

    def save_strategy(self, sp_id, code, path):
        code = code.replace("'", "\\\'")
        code = code.replace('"', '\\\"')
        sqlstr = "insert into lq_strategy(sp_id,code,data_path) values (%ld,'%s','%s');" % (sp_id, code, path)
        self.lock.acquire()
        cursor = self.conn.cursor()
        cursor.execute(sqlstr)
        self.conn.commit()
        cursor.close()
        self.lock.release()

    def save_strategy_test(self, sp_id, s_id, t_id, stock, path, perf):
        cond = sp_id + s_id + t_id
        data = self.qa_risk.find_one({"account_cookie":cond})
        sqlstr = """insert into lq_strategy_test 
                    (sp_id, s_id, t_id, stock, data_path,
                    net_profit, total_profit, total_loss,
                    trade_lot, profit_ratio, average_profit,
                    average_loss, max_profit, max_loss,
                    average_hold_period, max_fund_use, yield_rate,
                    annual_return, r_square_yield_curve, max_retrace_ratio
                    ) 
                    values
                    """
        self.lock.acquire()
        cursor = self.conn.cursor()
        d1 = data['profit_money'] #perf["已平仓净利润总额".encode('gbk')]
        d2 = 0 #perf["赢利交易赢利总额".encode('gbk')]
        d3 = 0 #perf["亏损交易亏损总额".encode('gbk')]
        d4 = 0 #perf["已平仓交易总数".encode('gbk')]
        d5 = 0 #perf["赢利交易比例%".encode('gbk')]
        d6 = 0 #perf["赢利交易平均赢利".encode('gbk')]
        d7 = 0 #perf["亏损交易平均亏损".encode('gbk')]
        d8 = 0 #perf["最大单笔赢利".encode('gbk')]
        d9 = 0 #perf["最大单笔亏损".encode('gbk')]
        d10 = 0 #perf["赢利交易平均持仓时间".encode('gbk')]
        d11 = 0 #perf["单笔交易最大占用现金比例%".encode('gbk')]
        d12 = data['profit'] #perf["已平仓帐户收益率%".encode('gbk')]
        d13 = data['annualize_return'] #perf["帐户年复合收益率%".encode('gbk')]
        d14 = 0 #perf["R乘数期望值".encode('gbk')]
        d15 = data['max_dropback'] #perf["最大资产回撤值比率".encode('gbk')]
        s = sqlstr + '(%ld,'%sp_id + '%ld,'%s_id + '%ld,'%t_id + '\'%s\','%stock + '\'%s\','%path + '%f,'%d1\
        + '%f,' % d2 + '%f,'%d3 + '%f,'%d4 + '%f,'%d5 + '%f,'%d6 + '%f,'%d7 + '%f,'%d8\
        + '%f,'%d9 + '%f,'%d10 + '%f,'%d11\
        + '%f,' % d12 + '%f,'%d13 + '%f,'%d14 + '%f);'%d15
        print(s)
        cursor.execute(s)
        self.conn.commit()
        cursor.close()
        self.lock.release()

    def update_strategy_perf(self, sp_id, s_id, profit_day, profit_month):
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
                    max(max_retrace_ratio) as avg_hold_ratio 
                    from lq_strategy_test
                    where sp_id = %ld and s_id = %ld;""" % (sp_id,sid)
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
                    r_square_yield_curve = %f, max_retrace_ratio = %f,
                    profit_daily = '%s', profit_monthly = '%s' 
                    where sp_id = %ld and s_id = %ld;""" % (perfs[0],perfs[1],perfs[2],
                       perfs[3],perfs[4],perfs[5],perfs[6],perfs[7],
                       perfs[8],perfs[9],perfs[10],perfs[11],perfs[12],
                       perfs[13],perfs[14],perfs[15],str(profit_day()),str(profit_month()),
                       sp_id,s_id)
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
