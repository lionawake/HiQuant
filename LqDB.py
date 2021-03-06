#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import pymysql as MySQLdb
import datetime
import os

cwd = os.getcwd()
print("LqDB:".ljust(15), cwd)

class SqlDB():
    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PWD, DB_NAME):
        self.DB_HOST = DB_HOST
        self.DB_PORT = DB_PORT
        self.DB_USER = DB_USER
        self.DB_PWD = DB_PWD
        self.DB_NAME = DB_NAME
        self.lock = threading.Lock()
        try:
            self.conn = MySQLdb.Connect(
                host=self.DB_HOST,
                port=self.DB_PORT,
                user=self.DB_USER,
                passwd=self.DB_PWD,
                db=self.DB_NAME,
                charset='utf8')
        except Exception as e:
            print("DB connect error: ", e)

    def __del__(self):
        self.conn.close()

    def query(self, sqlstr):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sqlstr)
            returnData = cursor.fetchall()
        except Exception as e:
            print("DB query error: ", e)
            print(sqlstr)
        finally:
            cursor.close()
        return returnData

    def update(self, sqlstr):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sqlstr)
            self.conn.commit()
        except Exception as e:
            print("DB update error: ", e)
            print(sqlstr)
            self.conn.rollback()
        finally:
            cursor.close()

    def save_strategy_pattern(self, name, author, status, task_total, task_finished, code):
        time_stamp = datetime.datetime.now()
        code = code.replace("'", "\\\'")
        code = code.replace('"', '\\\"')
        sqlstr = "insert into lq_strategy_pattern"+\
            "(sp_name,author,create_time,test_status,task_total,task_finished,code) "+\
            "values (\"%s\",\"%s\",\"%s\",%d,%ld,%ld,\"%s\");" % (name, author, time_stamp, status, task_total, task_finished, code)
        self.lock.acquire()
        try:
            cursor = self.conn.cursor()
            cursor.execute(sqlstr)
            self.conn.commit()
        except Exception as e:
            print("DB save_strategy_pattern error: ", e)
            print(sqlstr)
            self.conn.rollback()
        finally:
            cursor.close()
            self.lock.release()

    def save_strategy(self, sp_id, s_id, code, path):
        code = code.replace("'", "\\\'")
        code = code.replace('"', '\\\"')
        sqlstr = "insert into lq_strategy(sp_id,s_id,code,data_path) values (%ld,%ld,'%s','%s');" % (sp_id, s_id, code, path)
        self.lock.acquire()
        try:
            cursor = self.conn.cursor()
            cursor.execute(sqlstr)
            self.conn.commit()
        except Exception as e:
            print("DB save_strategy error: ", e)
            print(sqlstr)
            self.conn.rollback()
        finally:
            cursor.close()
            self.lock.release()

    def save_strategy_test(self, sp_id, s_id, stock, path, perf):
        time_stamp = datetime.datetime.now().strftime("%H:%M:%S")
        sqlstr = """insert into lq_strategy_test 
                    (sp_id, s_id, stock, data_path,test_time,
                    net_profit, total_profit, total_loss,
                    trade_lot, profit_ratio, average_profit,
                    average_loss, max_profit, max_loss,
                    average_hold_period, max_fund_use, yield_rate,
                    annual_return, r_square_yield_curve, max_retrace_ratio
                    ) 
                    values
                    """
        self.lock.acquire()
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
        #d15 = perf["最大资产回撤值比率".encode('gbk')]
        d15 = 0
        s = sqlstr + '(%ld,'%sp_id + '%ld,'%s_id + '\'%s\','%stock + '\'%s\','%path + '\'%s\','%time_stamp + '%f,'%d1\
        + '%f,' % d2 + '%f,'%d3 + '%f,'%d4 + '%f,'%d5 + '%f,'%d6 + '%f,'%d7 + '%f,'%d8\
        + '%f,'%d9 + '%f,'%d10 + '%f,'%d11\
        + '%f,' % d12 + '%f,'%d13 + '%f,'%d14 + '%f);'%d15
        #print(s)
        #print(perf)
        try:
            cursor = self.conn.cursor()
            cursor.execute(s)
            self.conn.commit()
        except Exception as e:
            print("DB save_strategy_test error: ", e)
            print(s)
            self.conn.rollback()
        finally:
            cursor.close()
            self.lock.release()

    def update_strategy_perf(self, sp_id, s_id, profit_day, profit_month):
        '''sqlsids = "select distinct(s_id) from lq_strategy_test where sp_id = %d;"%sp_id
        try:
            cursor = self.conn.cursor()
            cursor.execute(sqlsids)
            sids = cursor.fetchall()
            print("sids:",sids)
        except Exception as e:
            print("DB query error: ", e)
            print(sqlsids)
            cursor.close()'''
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
                max(max_retrace_ratio) as max_retrace
                from lq_strategy_test
                where sp_id = %ld and s_id = %ld;""" % (sp_id, s_id)
        #print(sqlperf)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sqlperf)
            results = cursor.fetchall()
            perfs = results[0]
            sqlupd = """update lq_strategy set 
                    net_profit = %f, total_profit = %f, total_loss = %f, trade_lot = %d, profit_ratio = %f, average_profit = %f,
                    average_loss = %f, max_profit = %f, max_loss = %f, average_hold_period = %d, max_fund_use = %f, yield_rate = %f,
                    annual_return = %f, r_square_yield_curve = %f, max_retrace_ratio = %f, profit_daily = '%s', profit_monthly = '%s' 
                    where sp_id = %ld and s_id = %ld;""" % \
                     (perfs[0], perfs[1], perfs[2], perfs[3], perfs[4]/100, perfs[5], perfs[6], perfs[7], perfs[8], perfs[9], perfs[10]/100, perfs[11]/100, perfs[12]/100,
                      perfs[13], perfs[14],
                      profit_day, profit_month,
                      sp_id,
                      s_id)
            cursor.execute(sqlupd)
            #print(sqlupd)
            self.conn.commit()
        except Exception as e:
            print("DB update_strategy_perf error: ", e)
            print(sqlupd)
            self.conn.rollback()
        finally:
            cursor.close()

    def update_task_stat(self, wait, run, over):
        sqlstr = """update lq_task_stat set
                    task_wait = %ld,
                    task_run = %ld,
                    task_over = %ld;""" % (wait,run,over)
        try:
            cursor = self.conn.cursor()
            cursor.execute(sqlstr)
            self.conn.commit()
        except Exception as e:
            print("DB update_task_stat error: ", e)
            print(sqlstr)
            self.conn.rollback()
        finally:
            cursor.close()

if __name__ == "__main__":
    db = SqlDB('192.168.54.11', 3306, 'root', 'lq2018', 'lq')
    print(db.query("show tables;"))
