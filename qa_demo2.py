# coding=utf-8
#
# The MIT License (MIT)
#
# Copyright (c) 2016-2018 yutiansut/QUANTAXIS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import sys
#sys.path.append("C:/Users/fu/quantaxis/")

from QUANTAXIS.QAARP.QARisk import QA_Risk
from QUANTAXIS.QAARP.QAUser import QA_User
from QUANTAXIS.QABacktest.QABacktest import QA_Backtest
from QUANTAXIS.QAUtil.QALogs import QA_util_log_info
from QUANTAXIS.QAUtil.QAParameter import FREQUENCE, MARKET_TYPE
from test_backtest.minstrategy import MAMINStrategy
from test_backtest.strategy import MAStrategy

cwd = os.getcwd()
print("Demo:".ljust(15), cwd)
sys.path.append(cwd)

import LqDB_QA as lqdb

sp_id = 1000
s_id = 0
if len(sys.argv) >= 2:
    sp_id = int(sys.argv[1])
if len(sys.argv) >= 3:
    s_id = int(sys.argv[2])


class Backtest(QA_Backtest):
    '''
    多线程模式回测示例

    '''

    def __init__(self, market_type, frequence, start, end, code_list, commission_fee):
        super().__init__(market_type,  frequence, start, end, code_list, commission_fee)
        self.user = QA_User()
        mastrategy = MAStrategy()
        maminstrategy = MAMINStrategy()
        # maminstrategy.reset_assets(1000)
        # self.portfolio, self.account = self.user.register_account(mastrategy)
        self.user = QA_User(user_cookie='user_admin')
        self.portfolio = self.user.new_portfolio('folio_admin')
        self.portfolio, self.account = self.user.register_account(mastrategy)

    def after_success(self):
        QA_util_log_info(self.account.history_table)
        risk = QA_Risk(self.account, benchmark_code='000300',
                       benchmark_type=MARKET_TYPE.INDEX_CN)

        print(risk().T)
        risk.plot_assets_curve()
        risk.plot_dailyhold()
        risk.plot_signal()
        self.account.save()
        risk.save()


def run_daybacktest():
    #sys.path.append("C:/Users/fu/quantaxis/")
    import QUANTAXIS as QA
    backtest = Backtest(market_type=MARKET_TYPE.STOCK_CN,
                        frequence=FREQUENCE.DAY,
                        start='2017-01-01',
                        end='2017-02-10',
                        code_list=QA.QA_fetch_stock_block_adv().code[0:5],
                        commission_fee=0.00015)
    backtest.start_market()

    backtest.run()
    backtest.stop()
    db = lqdb.SqlDB('192.168.54.11', 3306, 'root', 'lq2018', 'lq')
    code = QA.QA_fetch_stock_block_adv().code[0]
    db.save_strategy_test(sp_id, s_id, 0, code, cwd, 0)
    #day = dump_profit_day(stk, q)
    #month = dump_profit_month(stk, q)
    #db.update_strategy_perf(sp_id, s_id, day, month)


def run_minbacktest():
    #sys.path.append("C:/Users/fu/quantaxis/")
    import QUANTAXIS as QA
    backtest = Backtest(market_type=MARKET_TYPE.STOCK_CN,
                        frequence=FREQUENCE.FIFTEEN_MIN,
                        start='2017-11-01',
                        end='2017-11-10',
                        code_list=QA.QA_fetch_stock_block_adv().code[0:5],
                        commission_fee=0.00015)
    backtest.start_market()

    backtest.run()
    backtest.stop()


if __name__ == '__main__':
    run_daybacktest()
    #run_minbacktest()

