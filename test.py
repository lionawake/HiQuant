
import LqHikyuuIndc as hky
import LqFinance as fa
import LqTalibIndc as ta
import LqAlpha101 as alp101
import LqAlpha191 as alp191
import QUANTAXIS as QA

stocks = ['000001', '000002', '000005']
begin_date = '2018-01-01'
end_date = '2018-06-30'
data = QA.QA_fetch_stock_day_adv(stocks, begin_date, end_date)
close = data.close

#hky.LQ_Hikyuu_AMA(close)
#a = fa.fa_acca_ttm(stocks[0])
#print(a)
a = ta.TALIB_APO(close)
print(a)
a = alp101.alpha_001(stocks, begin_date, end_date)
print(a)
a = alp191.alpha_002(stocks, end_date)
print(a)
