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

    def query(self, sqlString):
        cursor = self.conn.cursor()
        cursor.execute(sqlString)
        returnData = cursor.fetchall()
        cursor.close()
        return returnData

    def update(self, sqlString):
        cursor = self.conn.cursor()
        cursor.execute(sqlString)
        self.conn.commit()
        cursor.close()

    def save_strategy_pattern(self, name, author, status, task_total, task_finished, code):
        sqlstr = """insert into lq_strategy_pattern
            (sp_name,author,test_status,task_total,task_finished,code) 
            values (%s,%s,%d,%ld,%ld,%s);"""
        cursor = self.conn.cursor()
        cursor.execute(sqlString,name, author, status, task_total, task_finished, code)
        self.conn.commit()
        cursor.close()

    def save_strategy(self, sp_id, code, path):
        sqlstr = "insert into lq_strategy(sp_id,code,data_path) values (%ld,%s,%s);"
        cursor = self.conn.cursor()
        cursor.execute(sqlString, sp_id, code, path)
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
                    (%ld,%ld,%s,%s,%f,%f,%f,%f,
                    %d,%f,%f,%f,%f,%f,%f,%f,
                    %f,%d,%f,%f,%f,%f,%f);"""
        cursor = self.conn.cursor()
        cursor.execute(sqlString, sp_id, s_id, stock, path,
                       perf["已平仓净利润总额"],
                       perf["赢利交易赢利总额"],
                       perf["亏损交易亏损总额"],
                       perf["赢利交易赢利总额"]/perf["亏损交易亏损总额"],
                       perf["已平仓交易总数"],
                       perf["赢利交易比例%"],
                       perf["赢利交易平均赢利"],
                       perf["亏损交易平均亏损"],
                       perf["赢利交易平均赢利"]/perf["亏损交易平均亏损"],
                       perf["最大单笔赢利"],
                       perf["最大单笔亏损"],
                       perf["最大单笔赢利"]/perf["赢利交易赢利总额"],
                       perf["最大单笔亏损"]/perf["亏损交易亏损总额"],
                       perf["赢利交易平均持仓时间"],
                       perf["单笔交易最大占用现金比例"],
                       perf["已平仓帐户收益率"],
                       perf["帐户年复合收益率"],
                       perf["R乘数期望值"],
                       100-perf["空仓时间/总时间%"])
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
        cursor.execute(sqlString,
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
        cursor.execute(sqlString,wait,run,over)
        self.conn.commit()
        cursor.close()

if __name__ == "__main__":
    db = SqlDB('127.0.0.1', 3306, 'hikyuu', 'hikyuu', 'hikyuu')
    print(db.query("show tables;"))
