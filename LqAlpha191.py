# -*- coding:utf-8 -*-
# functions which are in common use
try:
    from kuanke.user_space_api import *
except:
    try:
        from kuanke.research.research_api import *
    except:
        try:
            from jqresearch.api import *
        except:
            pass

import pandas as pd
import numpy as np
from numpy import sign, sum, nan
from sklearn.linear_model import LinearRegression
import six


# 版本
def alpha191_version():
    '''
    V1.0 上线
    V1.1 优化 func_decaylinear 函数
    '''
    return 'V1.1 优化 func_decaylinear 函数'

# pandas 0.17.0 --> 0.23.4
def pd_rolling_count(df, win):
    return df.rolling(win).count()

def pd_rolling_sum(df, win):
    return df.rolling(win).sum()

def pd_rolling_mean(df, win):
    return df.rolling(win).mean()

def pd_rolling_median(df, win):
    return df.rolling(win).median()

def pd_rolling_var(df, win):
    return df.rolling(win).var()

def pd_rolling_std(df, win):
    return df.rolling(win).std()

def pd_rolling_min(df, win):
    return df.rolling(win).min()

def pd_rolling_max(df, win):
    return df.rolling(win).max()

def pd_rolling_corr(df1, df2, win):
    rol1 = df1.rolling(win)
    rol2 = df2.rolling(win)
    return rol1.corr(rol2)

def pd_rolling_cov(df1, df2, win):
    rol1 = df1.rolling(win)
    rol2 = df2.rolling(win)
    return rol1.cov(rol2)

def pd_rolling_apply(df, win, func):
    return df.rolling(win).apply(func, raw=True)

def pd_ewma(df, span, adjust=True):
    return df.ewm(span=span, adjust=adjust).mean()

# pandas 0.17.0 --> 0.23.4

def get_price(stock_pool=None, begin_date=None, end_date=None, field=None, tail_count=0, plat_form_type='QA'):
    if plat_form_type != 'QA':
        return None
    if begin_date == None:
        begin_date = '2018-05-01'

    data = QA.QA_fetch_stock_day_adv(stock_pool, begin_date, end_date)
    if field == 'open':
        field_data = data.open
    elif field == 'high':
        field_data = data.high
    elif field == 'low':
        field_data = data.low
    elif field == 'close':
        field_data = data.close
    elif field == 'volume':
        field_data = data.volume
    elif field == 'money':
        field_data = data.money
    elif field == 'avg':
        field_data = data.avg
    elif field == 'factor':
        #field_data = data.factor
        return None
    elif field == 'high_limit':
        field_data = data.high_limit
    elif field == 'low_limit':
        field_data = data.low_limit
    elif field == 'pre_close' or field == 'preclose':
        field_data = data.preclose
    elif field == 'paused':
        #field_data = data.paused
        return None
    else:
        return None

    if tail_count != 0:
        res = field_data.unstack().tail(tail_count)
    else:
        res = field_data.unstack()

    return res

# 开盘价 最高价 最低价 收盘价 平均值 成交量 成交额 指数的开盘价 指数的收盘价
# 返回的都是数据框
def open(code, end_date=None):
    #temp = get_price(code, None, end_date, '1d', ['open'], False, None, 350)['open']
    temp = get_price(code, None, end_date, 'open', 350, plat_form_type='QA')
    return temp


def high(code, end_date=None):
    #temp = get_price(code, None, end_date, '1d', ['high'], False, None, 350)['high']
    temp = get_price(code, None, end_date, 'high', 350, plat_form_type='QA')
    return temp


def low(code, end_date=None):
    #temp = get_price(code, None, end_date, '1d', ['low'], False, None, 350)['low']
    temp = get_price(code, None, end_date, 'low', 350, plat_form_type='QA')
    return temp


def close(code, end_date=None):
    #temp = get_price(code, None, end_date, '1d', ['close'], False, None, 350)['close']
    temp = get_price(code, None, end_date, 'close', 350, plat_form_type='QA')
    return temp


def vwap(code, end_date=None):
    #temp = get_price(code, None, end_date, '1d', ['avg'], False, None, 350)['avg']
    temp = get_price(code, None, end_date, 'avg', 350, plat_form_type='QA')
    return temp


def volume(code, end_date=None):
    #temp = get_price(code, None, end_date, '1d', ['volume'], False, None, 350)['volume']
    temp = get_price(code, None, end_date, 'volume', 350, plat_form_type='QA')
    return temp


def amount(code, end_date=None):
    #temp = get_price(code, None, end_date, '1d', ['money'], False, None, 350)['money']
    temp = get_price(code, None, end_date, 'money', 350, plat_form_type='QA')
    return temp


def benchmark_index_open(code, benchmark, end_date=None):
    output = pd.DataFrame(code)
    #temp = get_price(benchmark, None, end_date, '1d', ['open'], False, None, 350)['open']
    temp = get_price(code, None, end_date, 'open', 350, plat_form_type='QA')
    for stock in code:
        output[stock] = temp
    return output


def benchmark_index_close(code, benchmark, end_date=None):
    output = pd.DataFrame(code)
    #temp = get_price(benchmark, None, end_date, '1d', ['close'], False, None, 350)['close']
    temp = get_price(code, None, end_date, 'close', 350, plat_form_type='QA')
    for stock in code:
        output[stock] = temp
    return output


# 每日收益率
def func_ret(code, end_date=None):
    return close(code, end_date).pct_change()


# sing 符号函数
def func_sign(a):
    result = pd.DataFrame()
    for stock in a.index:
        result[stock] = np.sign(a[stock])
    return result


def func_tsrank(a, n):
    output = pd.DataFrame()
    for stock in a.columns:
        temp = [0] * (len(a) - n)
        for i in range(len(a) - n):
            temp[i] = a[stock][i:i + n].rank(pct=True)[-1]
            output[stock] = temp
    output.index = a.index[n:]
    return output


# 序列A和序列B在过去n天的协方差
def func_coviance(a, b, n):
    output = pd.Series()
    for stock in a.columns:
        output[stock] = float(cov(a[stock][-n:], b[stock][-n:])[0, 1])
    output = pd.DataFrame(output, columns=['coviance'])
    return output


# 序列A过去n天的累乘
def func_prod(a, n):
    output = pd.Series()
    for stock in a.columns:
        output[stock] = cumprod(a[stock][-n:])[-1]
    output = pd.DataFrame(output, columns=['cumprod'])
    return output


# 计算前n期样本A对B做回归所得回归系数
def func_regbeta(a, b, n):
    output = pd.Series()
    for stock in a.columns:
        linreg = LinearRegression()
        model = linreg.fit(a[stock][-n:].values.reshape(n, 1), b[stock][-n:].values.reshape(n, 1))
        output[stock] = float(model.coef_)
        output = pd.DataFrame(output)
    return output


# 前n期样本A对B做回归所得的残差
def func_regresi(a, b, n):
    output = pd.DataFrame()
    for stock in a.columns:
        linreg = LinearRegression()
        model = linreg.fit(a[stock][:n].values.reshape(n, 1), b[stock][:n].values.reshape(n, 1))
        temp = pd.DataFrame(model.predict(a[stock][:n].values.reshape(n, 1)) - b[stock][:n].values.reshape(n, 1), columns=[stock])
        temp_s = pd.Series(temp[stock])
        output[stock] = temp_s
    output.index = a[:n].index
    return output


# 计算A前n期样本加权平均值权重为0.9*i
def func_wma(a, n):
    output = pd.DataFrame()
    for stock in a.columns:
        temp = 0
        for i in range(n):
            temp = a[stock][i] * 0.9 * (i + 1) + temp
        output[stock] = pd.Series(temp)
        output = pd.DataFrame(output)
    return output


def func_dtm(code, end_date=None):
    cond1 = open(code, end_date) <= open(code, end_date).shift()
    data1 = np.maximum(high(code, end_date) - open(code, end_date), open(code, end_date) - open(code, end_date).shift())
    data1[cond1] = 0
    return data1


def func_dbm(code, end_date=None):
    cond1 = open(code, end_date) >= open(code, end_date).shift()
    data1 = np.maximum(open(code, end_date) - low(code, end_date), open(code, end_date) - open(code, end_date).shift())
    data1[cond1] = 0
    return data1


def func_tr(code, end_date=None):
    output_f = pd.DataFrame()
    for stock in code:
        temp_1 = list(high(stock, end_date)['high'] - low(stock, end_date)['low'])
        temp_hdelay = list(abs(high(stock, end_date)['high'] - close(stock, end_date).shift()['close']))
        temp_ldelay = list(abs(low(stock, end_date)['low'] - close(stock, end_date).shift()['close']))
        output = [0] * (len(temp_1) - 1)
        for i in range(1, (len(temp_1) - 1)):
            output[i - 1] = max(max(temp_1[i], temp_hdelay[i]), temp_ldelay[i])
        output_f[stock] = pd.Series(output)
    output_f.index = open(code, end_date)[1:].index
    return output_f


def func_hd(code, end_date=None):
    output = pd.DataFrame()
    for stock in code:
        output[stock] = high(stock, end_date)['high'] - high(stock, end_date).shift()['high']
    return output


def func_ld(code, end_date=None):
    output = pd.DataFrame()
    for stock in code:
        output[stock] = low(stock, end_date).shift()['low'] - low(stock, end_date)['low']
    return output


# 生成1~n的等差序列，间距为1
def func_sequence(n):
    return linspace(1, n, n)


# 对序列A计算移动平均加权，其中权重对应d,d-1....1(权重和为1)
def func_decaylinear(a, d):
    seq1 = np.arange(0, d, 1)
    abc = pd.Series(seq1) / sum(seq1)
    weight1 = np.array(abc)
    part1 = lambda x: sum(x * weight1)
    output = pd_rolling_apply(a, d, part1)
    output = output.iloc[d - 1:, :]
    return output.T


# 计算A前n期时间序列中最大值距离当前时点的间隔
def func_highday(a, n):
    output = pd.DataFrame()
    for stock in a.columns:
        temp = n - a[stock][-n:].values.argmin()
        output[stock] = pd.Series(temp)
    return output.iloc[0, :]

    # LOWDAY 函数


def func_lowday(a, n):
    output = pd.DataFrame()
    for stock in a.columns:
        temp = n - a[stock][-n:].values.argmax()
        output[stock] = pd.Series(temp)
    return output.iloc[0, :]


######################################

def alpha_001(code, end_date=None):
    '''
    公式：
        (-1 * CORR(RANK(DELTA(LOG(VOLUME),1)),RANK(((CLOSE-OPEN)/OPEN)),6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    data1 = volume(code, end_date).diff(1).rank(axis=0, pct=True)
    data2 = ((close(code, end_date) - open(code, end_date)) / open(code, end_date)).rank(axis=0, pct=True)
    alpha = -data1.iloc[-6:, :].corrwith(data2.iloc[-6:, :])
    return alpha


def alpha_002(code, end_date=None):
    '''
    公式：
        -1 * delta((((close-low)-(high-close))/((high-low)),1))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp = ((close(code, end_date) - low(code, end_date)) / (high(code, end_date) - low(code, end_date))).diff(1)
    alpha = temp.iloc[-1, :]
    return alpha * -1


def alpha_003(code, end_date=None):
    '''
    公式：
        SUM((CLOSE=DELAY(CLOSE,1)?0:CLOSE-(CLOSE>DELAY(CLOSE,1)?MIN(LOW,DELAY(CLOSE,1)):MAX(HIGH,DELAY(CLOSE,1)))),6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay1 = close(code, end_date).shift()
    condtion1 = (close(code, end_date) == delay1)
    condition2 = (close(code, end_date) > delay1)
    condition3 = (close(code, end_date) < delay1)

    part2 = (close(code, end_date) - np.minimum(delay1[condition2], low(code, end_date)[condition2])).iloc[-6:,
            :]  # 取最近的6位数据
    part3 = (close(code, end_date) - np.maximum(delay1[condition3], low(code, end_date)[condition3])).iloc[-6:, :]

    result = part2.fillna(0) + part3.fillna(0)
    alpha = result.sum()
    for stock in code:
        if alpha[stock] == 0:
            alpha[stock] = nan
    return alpha


def alpha_004(code, end_date=None):
    '''
    公式：
        ((((SUM(CLOSE,8)/8)+STD(CLOSE,8))<(SUM(CLOSE,2)/2))?(-1*1):(((SUM(CLOSE,2)/2)<((SUM(CLOSE,8)/8)-STD(CLOSE,8)))?1:(((1<(VOLUME/MEAN(VOLUME,20)))||((VOLUME/MEAN(VOLUME,20))==1))?1:(-1*1))))
    Inputs:

        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    condition1 = (pd_rolling_std(close(code, end_date), 8) < pd_rolling_sum(close(code, end_date), 2) / 2)
    condition2 = (pd_rolling_sum(close(code, end_date), 2) / 2 < (
                pd_rolling_sum(close(code, end_date), 8) / 8 - pd_rolling_std(close(code, end_date), 8)))
    condition3 = (1 <= volume(code, end_date) / pd_rolling_mean(volume(code, end_date), 20))
    indicator1 = pd.DataFrame(np.ones(close(code, end_date).shape), index=close(code, end_date).index,
                              columns=close(code, end_date).columns)  # [condition2]
    indicator2 = -pd.DataFrame(np.ones(close(code, end_date).shape), index=close(code, end_date).index,
                               columns=close(code, end_date).columns)  # [condition3]

    part0 = pd_rolling_sum(close(code, end_date), 8) / 8
    part1 = indicator2[condition1].fillna(0)
    part2 = (indicator1[~condition1][condition2]).fillna(0)
    part3 = (indicator1[~condition1][~condition2][condition3]).fillna(0)
    part4 = (indicator2[~condition1][~condition2][~condition3]).fillna(0)

    result = part0 + part1 + part2 + part3 + part4
    alpha = result.iloc[-1, :]
    return alpha


def alpha_005(code, end_date=None):
    '''
    公式：
        (-1*TSMAX(CORR(TSRANK(VOLUME,5),YSRANK(HIGH,5),5),3))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    ts_volume = (volume(code, end_date).iloc[-7:, :]).rank(axis=0, pct=True)
    ts_high = (high(code, end_date).iloc[-7:, :]).rank(axis=0, pct=True)
    corr_ts = pd_rolling_corr(ts_high, ts_volume, 5)
    alpha = corr_ts.max()
    return alpha


def alpha_006(code, end_date=None):
    '''
    公式：
        (RANK(SIGN(DELTA((((OPEN*0.85)+(HIGH*0.15))),4)))*-1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = open(code, end_date) * 0.85 + high(code, end_date) * 0.15
    alpha = -1 * sign(temp_1.diff(4)).rank(axis=0, pct=True)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_007(code, end_date=None):
    '''
    公式：
        ((RANK(MAX((VWAP-CLOSE),3))+RANK(MIN((VWAP-CLOSE),3)))*RANK(DELTA(VOLUME,3)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp = vwap(code, end_date) - close(code, end_date)
    temp_1 = np.maximum(temp, 3).rank(axis=0, pct=True)
    temp_2 = np.minimum(temp, 3).rank(axis=0, pct=True)
    temp_3 = volume(code, end_date).diff(3).rank(axis=0, pct=True)
    alpha = temp_1 + temp_2 + temp_3
    alpha = alpha.ix[-1]
    return alpha


def alpha_008(code, end_date=None):
    '''
    公式：
        RANK(DELTA(((((HIGH+LOW)/2)*0.2)+(VWAP*0.8)),4)*-1
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = ((high(code, end_date) + low(code, end_date)) / 2) * 0.2 + vwap(code, end_date) * 0.8
    temp_2 = temp_1.diff(4) * -1
    alpha = temp_2.rank(axis=0, pct=True)
    alpha = alpha.ix[-1]
    return alpha


def alpha_009(code, end_date=None):
    '''
    公式：
        SMA(((HIGH+LOW)/2-(DELAY(HIGH,1)+DELAY(LOW,1))/*(HIGH-LOW)/VOLUME,7，2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp = (high(code, end_date) + low(code, end_date)) * 0.5 - (
                high(code, end_date).shift() + low(code, end_date).shift()) * 0.5 * (
                       high(code, end_date) - low(code, end_date)) / volume(code, end_date)  # 计算close_{i-1}
    result = pd_ewma(temp, span=6)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_010(code, end_date=None):
    '''
    公式：
        (RANK(MAX(((RET<0)?STD(RET,20):CLOSE)^2),5))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp = close(code, end_date).pct_change()
    condtion = (temp < 0)
    part1 = (pd_rolling_std(temp, 20)[condtion]).fillna(0)
    part2 = (close(code, end_date)[~condtion]).fillna(0)
    part3 = (part1 + part2) ** 2
    cond = part3 == 0
    part3[cond] = nan
    result = np.maximum(part3, 5)
    alpha = result.rank(pct=True)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_011(code, end_date=None):
    '''
    公式：
        SUM(((CLOSE-LOW)-(HIGH-CLOSE))./(HIGH-LOW).*VOLUME,6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = (close(code, end_date) - low(code, end_date)) - (high(code, end_date) - close(code, end_date))
    temp_2 = (high(code, end_date) - low(code, end_date))
    temp = (temp_1 / temp_2) * volume(code, end_date)
    alpha = temp.iloc[-6:, :].sum()
    for stock in code:
        if alpha[stock] == 0:
            alpha[stock] = nan
    return alpha


def alpha_012(code, end_date=None):
    '''
    公式：
        (RANK((OPEN-(SUM(VWAP,10)/10))))*(-1*(RANK(ABS((CLOSE-VWAP)))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp1 = open(code, end_date) - vwap(code, end_date).iloc[-10:, :].sum()
    part1 = temp1.rank(axis=0, pct=True)
    temp2 = (close(code, end_date) - vwap(code, end_date)).abs()
    part2 = -temp2.rank(axis=0, pct=True)
    result = part1 * part2 * -1
    alpha = result.iloc[-1, :]
    return alpha


def alpha_013(code, end_date=None):
    '''
    公式：
        (((HIGH*LOW)^0.5)-VWAP)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    result = ((high(code, end_date) - low(code, end_date)) ** 0.5) - vwap(code, end_date)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_014(code, end_date=None):
    '''
    公式：
        CLOSE-DELAY(CLOSE,5)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp = close(code, end_date) - close(code, end_date).shift(5)
    alpha = temp.iloc[-1, :]
    return alpha


def alpha_015(code, end_date=None):
    '''
    公式：
        OPEN/DELAY(CLOSE,1)-1
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp = open(code, end_date) / close(code, end_date).shift(1) - 1
    alpha = temp.iloc[-1, :]
    return alpha


def alpha_016(code, end_date=None):
    '''
    公式：
        (-1*TSMAX(RANK(CORR(RANK(VOLUME),RANK(VWAP),5)),5))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp1 = volume(code, end_date).rank(axis=0, pct=True)
    temp2 = vwap(code, end_date).rank(axis=0, pct=True)
    part = pd_rolling_corr(temp1, temp2, 5)
    part = part[(part < np.inf) & (part > -np.inf)].rank(axis=0, pct=True)
    result = part.iloc[-5:, :]
    result = result.dropna(axis=0)
    alpha = -result.max()
    return alpha


def alpha_017(code, end_date=None):
    '''
    公式：
        RANK((VWAP-MAX(VWAP,15)))^DELTA(CLOSE,5)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp1 = pd_rolling_max(vwap(code, end_date), 15)
    temp2 = (close(code, end_date) - temp1)
    part1 = temp2.rank(axis=0, pct=True)
    part2 = close(code, end_date).diff(5)
    result = part1 ** part2
    alpha = result.iloc[-1, :]
    return alpha


def alpha_018(code, end_date=None):
    '''
    公式：
        CLOSE/DELAY(CLOSE,5)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay5 = close(code, end_date).shift(5)
    alpha = close(code, end_date) / delay5
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_019(code, end_date=None):
    '''
    公式：
        (CLOSE<DELAY(CLOSE,5)?(CLOSE-DELAY(CLOSE,5))/DELAY(CLOSE,5):(CLOSE=DELAY(CLOSE,5)?0:(CLOSE-DELAY(CLOSE,5))/CLOSE))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay5 = close(code, end_date).shift(5)
    condition1 = (close(code, end_date) < delay5)
    condition3 = (close(code, end_date) > delay5)
    part1 = (close(code, end_date)[condition1] - delay5[condition1]) / delay5[condition1]
    part1 = part1.fillna(0)
    part2 = (close(code, end_date)[condition3] - delay5[condition3]) / close(code, end_date)[condition3]
    part2 = part2.fillna(0)
    result = part1 + part2
    alpha = result.iloc[-1, :]
    for stock in code:
        if alpha[stock] == 0:
            alpha[stock] = nan
    return alpha


def alpha_020(code, end_date=None):
    '''
    公式：
        (CLOSE-DELAY(CLOSE,6))/DELAY(CLOSE,6)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay6 = close(code, end_date).shift(6)
    result = (close(code, end_date) - delay6) * 100 / delay6
    alpha = result.iloc[-1, :]
    return alpha


def alpha_021(code, end_date=None):
    '''
    公式：
        REGBETA(MEAN(CLOSE,6),SEQUENCE(6))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    A = pd_rolling_mean(close(code, end_date), 6).iloc[-6:, :]
    B = np.arange(1, 7)  # 等差Sequence 1:6
    output = pd.Series()
    for stock in code:
        A[stock] = A[stock].fillna(0)
        linreg = LinearRegression()
        model = linreg.fit(A[stock][-6:].values.reshape(6, 1), B[-6:].reshape(6, 1))
        output[stock] = float(model.coef_)
    alpha = output
    for stock in code:
        if alpha[stock] == 0:
            alpha[stock] = nan
    return alpha


def alpha_022(code, end_date=None):
    '''
    公式：
        SMEAN(((CLOSE-MEAN(CLOSE,6))/MEAN(CLOSE,6)-DELAY((CLOSE-MEAN(CLOSE,6))/MEAN(CLOSE,6),3)),12,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part1 = (close(code, end_date) - pd_rolling_mean(close(code, end_date), 6)) / pd_rolling_mean(close(code, end_date),
                                                                                                  6)
    temp = (close(code, end_date) - pd_rolling_mean(close(code, end_date), 6)) / pd_rolling_mean(close(code, end_date),
                                                                                                 6)
    part2 = temp.shift(3)
    result = part1 - part2
    result = pd_ewma(result, span=23)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_023(code, end_date=None):
    '''
    公式：
        SMA((CLOSE>DELAY(CLOSE,1)?STD(CLOSE:20),0),20,1)/(SMA((CLOSE>DELAY(CLOSE,1)?STD(CLOSE,20):0),20,1
        )+SMA((CLOSE<=DELAY(CLOSE,1)?STD(CLOSE,20):0),20,1))*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    condition1 = (close(code, end_date) > close(code, end_date).shift())
    temp1 = pd_rolling_std(close(code, end_date), 20)[condition1]
    temp1 = temp1.fillna(0)
    temp2 = pd_rolling_std(close(code, end_date), 20)[~condition1]
    temp2 = temp2.fillna(0)
    part1 = pd_ewma(temp1, span=39)
    part2 = pd_ewma(temp2, span=39)
    result = part1 * 100 / (part1 + part2)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_024(code, end_date=None):
    '''
    公式：
        SMA(CLOSE-DELAY(CLOSE,5),5,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay5 = close(code, end_date).shift(5)
    result = close(code, end_date) - delay5
    result = pd_ewma(result, span=9)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_025(code, end_date=None):
    '''
    公式：
        ((-1  *  RANK((DELTA(CLOSE,  7)  *  (1 - RANK(DECAYLINEAR((VOLUME  /  MEAN(VOLUME,20)),  9))))))  *  (1  + RANK(SUM(RET, 250))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = close(code, end_date).diff(7)
    temp_2 = 1 - func_decaylinear(volume(code, end_date) / pd_rolling_mean(volume(code, end_date), 20), 9).rank(axis=1,
                                                                                                                pct=True)
    part_1 = (temp_1 * temp_2.T).rank(pct=True)
    part_2 = pd_rolling_sum(func_ret(code, end_date), 250).rank(pct=True)
    alpha = -part_1.iloc[-1, :] * (part_2.iloc[-1, :] + 1)
    for stock in code:
        if alpha[stock] == 0:
            alpha[stock] = nan
    return alpha


def alpha_026(code, end_date=None):
    '''
    公式：
        ((((SUM(CLOSE, 7) / 7)-CLOSE)) + ((CORR(VWAP, DELAY(CLOSE, 5), 230))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part1 = pd_rolling_sum(close(code, end_date), 7) / 7 - close(code, end_date)
    part1 = part1.iloc[-1, :]
    delay5 = close(code, end_date).shift(5)
    part2 = pd_rolling_corr(vwap(code, end_date), delay5, 230)
    part2 = part2.iloc[-1, :]
    alpha = part1 + part2
    return alpha


def alpha_027(code, end_date=None):
    '''
    公式：
        WMA((CLOSE-DELAY(CLOSE,3))/DELAY(CLOSE,3)*100+(CLOSE-DELAY(CLOSE,6))/DELAY(CLOSE,6)*100,12)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = ((close(code, end_date) - close(code, end_date).shift(3)) * 100) / close(code, end_date).shift(3)
    temp_2 = ((close(code, end_date) - close(code, end_date).shift(6)) * 100) / close(code, end_date).shift(6)
    alpha = func_wma(temp_1.iloc[6:, ] + temp_2.iloc[6:, ], 12)
    alpha = alpha.iloc[-1, :]
    for stock in code:
        if alpha[stock] == 0:
            alpha[stock] = nan
    return alpha


def alpha_028(code, end_date=None):
    '''
    公式：
        3*SMA((CLOSE-TSMIN(LOW,9))/(TSMAX(HIGH,9)-TSMIN(LOW,9))*100,3,1)-2*SMA(SMA((CLOSE-TSMIN(LOW,9))/( MAX(HIGH,9)-TSMAX(LOW,9))*100,3,1),3,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp1 = close(code, end_date) - pd_rolling_min(low(code, end_date), 9)
    temp2 = pd_rolling_max(high(code, end_date), 9) - pd_rolling_min(low(code, end_date), 9)
    part1 = 3 * pd_ewma(temp1 * 100 / temp2, span=5)
    temp3 = pd_ewma(temp1 * 100 / temp2, span=5)
    part2 = 2 * pd_ewma(temp3, span=5)
    result = part1 - part2
    alpha = result.iloc[-1, :]  #
    return alpha


# 怀疑后面乘以成交量这里的括号他们没有扩上
def alpha_029(code, end_date=None):
    '''
    公式：
       (CLOSE-DELAY(CLOSE,6))/DELAY(CLOSE,6)*VOLUME
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay6 = close(code, end_date).shift(6)
    result = ((close(code, end_date) - delay6) / delay6) * volume(code, end_date)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_030(code, end_date=None):
    '''
    公式：
        WMA((REGRESI(CLOSE/DELAY(CLOSE)-1,MKT,SMB,HML，60))^2,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    # 表达不清
    return nan


def alpha_031(code, end_date=None):
    '''
    公式：
        LOSE-MEAN(CLOSE,12))/MEAN(CLOSE,12)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    result = (close(code, end_date) - pd_rolling_mean(close(code, end_date), 12)) * 100 / pd_rolling_mean(
        close(code, end_date), 12)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_032(code, end_date=None):
    '''
    公式：
        (-1 * SUM(RANK(CORR(RANK(HIGH), RANK(VOLUME), 3)), 3))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp1 = high(code, end_date).rank(axis=0, pct=True)
    temp2 = volume(code, end_date).rank(axis=0, pct=True)
    temp3 = pd_rolling_corr(temp1, temp2, 3)
    result = (temp3.rank(axis=0, pct=True)).iloc[-3:, :]
    alpha = -result.sum()
    for stock in code:
        if alpha[stock] == 0:
            alpha[stock] = nan
    return alpha


def alpha_033(code, end_date=None):
    '''
    公式：
        ((((-1  *  TSMIN(LOW,  5))  +  DELAY(TSMIN(LOW,  5),  5))  *  RANK(((SUM(RET,  240) - SUM(RET,  20))  /  220)))    * TSRANK(VOLUME, 5))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    ret = close(code, end_date).pct_change()
    temp1 = pd_rolling_min(low(code, end_date), 5)  # TS_MIN
    part1 = temp1.shift(5) - temp1
    part1 = part1.iloc[-1, :]
    temp2 = (pd_rolling_sum(ret, 240) - pd_rolling_sum(ret, 20)) / 220
    part2 = temp2.rank(axis=0, pct=True)
    part2 = part2.iloc[-1, :]
    temp3 = volume(code, end_date).iloc[-5:, :]
    part3 = temp3.rank(axis=0, pct=True)  # TS_RANK
    part3 = part3.iloc[-1, :]
    alpha = part1 + part2 + part3
    return alpha


def alpha_034(code, end_date=None):
    '''
    公式：
        MEAN(CLOSE,12)/CLOSE
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    result = pd_rolling_mean(close(code, end_date), 12) / close(code, end_date)
    alpha = result.iloc[-1, :]
    return alpha


# open*0.65+open*0.35 这个不就是开盘价么...肯定是有一个写错了
def alpha_035(code, end_date=None):
    '''
    公式：
        (MIN(RANK(DECAYLINEAR(DELTA(OPEN,  1),  15)),  RANK(DECAYLINEAR(CORR((VOLUME),  ((OPEN  *  0.65)  + (OPEN *0.35)), 17),7))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = open(code, end_date).diff(1)
    temp_1 = temp_1.fillna(0)
    part_1 = func_decaylinear(temp_1, 15)
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True).iloc[:, -1]
    temp_2 = open(code, end_date) * 0.65 + open(code, end_date) * 0.35
    temp_3 = pd_rolling_corr(volume(code, end_date), temp_2, 17)
    temp_3 = temp_3.fillna(0)
    part_2 = func_decaylinear(temp_3, 7)
    cond2 = part_2 == 0
    part_2[cond2] = nan
    part_2 = part_2.rank(axis=1, pct=True).iloc[:, -1]
    alpha = np.minimum(part_1, part_2)
    return alpha


def alpha_036(code, end_date=None):
    '''
    公式：
        RANK(SUM(CORR(RANK(VOLUME), RANK(VWAP)), 6), 2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp1 = volume(code, end_date).rank(axis=0, pct=True)
    temp2 = vwap(code, end_date).rank(axis=0, pct=True)
    part1 = pd_rolling_corr(temp1, temp2, 6)
    result = pd_rolling_sum(part1, 2)
    result = result.rank(axis=0, pct=True)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_037(code, end_date=None):
    '''
    公式：
        (-1 * RANK(((SUM(OPEN, 5) * SUM(RET, 5))-DELAY((SUM(OPEN, 5) * SUM(RET, 5)), 10))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    ret = close(code, end_date).pct_change()
    temp = pd_rolling_sum(open(code, end_date), 5) * pd_rolling_sum(ret, 5)
    part1 = temp.rank(axis=0, pct=True)
    part2 = temp.shift(10)
    result = -part1 - part2
    alpha = result.iloc[-1, :]
    return alpha


def alpha_038(code, end_date=None):
    '''
    公式：
        (((SUM(HIGH, 20) / 20) < HIGH) ? (-1 * DELTA(HIGH, 2)) : 0)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    sum_20 = pd_rolling_sum(high(code, end_date), 20) / 20
    delta2 = high(code, end_date).diff(2)
    condition = (sum_20 < high(code, end_date))
    result = -delta2[condition].fillna(0)
    alpha = result.iloc[-1, :]
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_039(code, end_date=None):
    '''
    公式：
        ((RANK(DECAYLINEAR(DELTA((CLOSE), 2),8))-RANK(DECAYLINEAR(CORR(((VWAP * 0.3) + (OPEN * 0.7)), SUM(MEAN(VOLUME,180), 37), 14), 12))) * -1
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = func_decaylinear(close(code, end_date).diff(2), 8)
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True)
    temp_1 = vwap(code, end_date) * 0.3 + open(code, end_date) * 0.7
    temp_2 = pd_rolling_sum(pd_rolling_mean(volume(code, end_date), 180), 37)
    part_2 = func_decaylinear(pd_rolling_corr(temp_1, temp_2, 14), 12).rank(axis=1, pct=True)
    result = part_1.iloc[:, -1] - part_2.iloc[:, -1]
    alpha = result
    return alpha


def alpha_040(code, end_date=None):
    '''
    公式：
        SUM((CLOSE>DELAY(CLOSE,1)?VOLUME:0),26)/SUM((CLOSE<=DELAY(CLOSE,1)?VOLUME:0),26)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay1 = close(code, end_date).shift()
    condition = (close(code, end_date) > delay1)
    vol = volume(code, end_date)[condition].fillna(0)
    vol_sum = pd_rolling_sum(vol, 26)
    vol1 = volume(code, end_date)[~condition].fillna(0)
    vol1_sum = pd_rolling_sum(vol1, 26)
    result = 100 * vol_sum / vol1_sum
    result = result.iloc[-1, :]
    alpha = result
    return alpha


def alpha_041(code, end_date=None):
    '''
    公式：
        (RANK(MAX(DELTA((VWAP), 3), 5))* -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delta_avg = vwap(code, end_date).diff(3)
    part = np.maximum(delta_avg, 5)
    result = -part.rank(axis=0, pct=True)
    alpha = result.iloc[-1, :]
    alpha = alpha
    return alpha


def alpha_042(code, end_date=None):
    '''
    公式：
        (-1 * RANK(STD(HIGH, 10))) * CORR(HIGH, VOLUME, 10))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part1 = pd_rolling_corr(high(code, end_date), volume(code, end_date), 10)
    part2 = pd_rolling_std(high(code, end_date), 10)
    part2 = part2.rank(axis=0, pct=True)
    result = -part1 * part2
    alpha = result.iloc[-1, :]
    return alpha


def alpha_043(code, end_date=None):
    '''
    公式：
        SUM((CLOSE>DELAY(CLOSE,1)?VOLUME:(CLOSE<DELAY(CLOSE,1)?-VOLUME:0)),6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay1 = close(code, end_date).shift()
    condition1 = (close(code, end_date) > delay1)
    condition2 = (close(code, end_date) < delay1)
    temp1 = volume(code, end_date)[condition1].fillna(0)
    temp2 = -volume(code, end_date)[condition2].fillna(0)
    result = temp1 + temp2
    result = pd_rolling_sum(result, 6)
    alpha = result.iloc[-1, :]
    cond = alpha == 0
    alpha[cond] = nan
    return alpha


def alpha_044(code, end_date=None):
    '''
    公式：
        (TSRANK(DECAYLINEAR(CORR(((LOW )), MEAN(VOLUME,10), 7), 6),4) + TSRANK(DECAYLINEAR(DELTA((VWAP), 3), 10), 15))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_rolling_corr(low(code, end_date), pd_rolling_mean(volume(code, end_date), 10), 7)
    part_1 = func_decaylinear(temp_1, 6).iloc[:, -4:]
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True)

    temp_2 = func_decaylinear(vwap(code, end_date).diff(3), 10).iloc[:, -15:]
    cond2 = temp_2 == 0
    temp_2[cond2] = nan
    part_2 = temp_2.rank(axis=1, pct=True)
    alpha = part_1 + part_2
    alpha = alpha.iloc[:, -1]
    return alpha


def alpha_045(code, end_date=None):
    '''
    公式：
        (RANK(DELTA((((CLOSE * 0.6) + (OPEN *0.4))), 1)) * RANK(CORR(VWAP, MEAN(VOLUME,150), 15)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp1 = close(code, end_date) * 0.6 + open(code, end_date) * 0.4
    part1 = temp1.diff()
    part1 = part1.rank(axis=0, pct=True)
    temp2 = pd_rolling_mean(volume(code, end_date), 150)
    part2 = pd_rolling_corr(vwap(code, end_date), temp2, 15)
    part2 = part2.rank(axis=0, pct=True)
    result = part1 * part2
    alpha = result.iloc[-1, :]
    return alpha


def alpha_046(code, end_date=None):
    '''
    公式：
        (MEAN(CLOSE,3)+MEAN(CLOSE,6)+MEAN(CLOSE,12)+MEAN(CLOSE,24))/(4*CLOSE)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = pd_rolling_mean(close(code, end_date), 3)
    part_2 = pd_rolling_mean(close(code, end_date), 6)
    part_3 = pd_rolling_mean(close(code, end_date), 12)
    part_4 = pd_rolling_mean(close(code, end_date), 24)
    alpha = (part_1 + part_2 + part_3 + part_4) / (4 * close(code, end_date))
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_047(code, end_date=None):
    '''
    公式：
        SMA((TSMAX(HIGH,6)-CLOSE)/(TSMAX(HIGH,6)-TSMIN(LOW,6))*100,9,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part1 = pd_rolling_max(high(code, end_date), 6) - close(code, end_date)
    part2 = pd_rolling_max(high(code, end_date), 6) - pd_rolling_min(low(code, end_date), 6)
    result = pd_ewma(100 * part1 / part2, span=17)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_048(code, end_date=None):
    '''
    公式：
        (-1*((RANK(((SIGN((CLOSE-DELAY(CLOSE,1)))+SIGN((DELAY(CLOSE,1)-DELAY(CLOSE,2))))+SIGN((DELAY(CLOSE,2)-DELAY(CLOSE,3))))))*SUM(VOLUME,5))/SUM(VOLUME,20))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    condition1 = (close(code, end_date) > close(code, end_date).shift())
    condition2 = (close(code, end_date).shift() > close(code, end_date).shift(2))
    condition3 = (close(code, end_date).shift(2) > close(code, end_date).shift(3))

    indicator1 = pd.DataFrame(np.ones(close(code, end_date).shape), index=close(code, end_date).index,
                              columns=close(code, end_date).columns)[condition1].fillna(0)
    indicator2 = pd.DataFrame(np.ones(close(code, end_date).shape), index=close(code, end_date).index,
                              columns=close(code, end_date).columns)[condition2].fillna(0)
    indicator3 = pd.DataFrame(np.ones(close(code, end_date).shape), index=close(code, end_date).index,
                              columns=close(code, end_date).columns)[condition3].fillna(0)

    indicator11 = -pd.DataFrame(np.ones(close(code, end_date).shape), index=close(code, end_date).index,
                                columns=close(code, end_date).columns)[
        (~condition1) & (close(code, end_date) != close(code, end_date).shift())].fillna(0)
    indicator22 = -pd.DataFrame(np.ones(close(code, end_date).shape), index=close(code, end_date).index,
                                columns=close(code, end_date).columns)[
        (~condition2) & (close(code, end_date).shift() != close(code, end_date).shift(2))].fillna(0)
    indicator33 = -pd.DataFrame(np.ones(close(code, end_date).shape), index=close(code, end_date).index,
                                columns=close(code, end_date).columns)[
        (~condition3) & (close(code, end_date).shift(2) != close(code, end_date).shift(3))].fillna(0)

    summ = indicator1 + indicator2 + indicator3 + indicator11 + indicator22 + indicator33
    result = -summ * pd_rolling_sum(volume(code, end_date), 5) / pd_rolling_sum(volume(code, end_date), 20)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_049(code, end_date=None):
    '''
    公式：
        SUM(((HIGH+LOW)>=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(LOW-DELAY(L OW,1)))),12)/(SUM(((HIGH+LOW)>=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(L OW-DELAY(LOW,1)))),12)+SUM(((HIGH+LOW)<=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HI GH,1)),ABS(LOW-DELAY(LOW,1)))),12))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay_high = high(code, end_date).shift()
    delay_low = low(code, end_date).shift()
    condition1 = (high(code, end_date) + low(code, end_date) >= delay_high + delay_low)
    condition2 = (high(code, end_date) + low(code, end_date) <= delay_high + delay_low)
    part1 = np.maximum(np.abs(high(code, end_date) - delay_high), np.abs(low(code, end_date) - delay_low))
    part1 = part1[~condition1]
    part1 = part1.iloc[-12:, :].sum()

    part2 = np.maximum(np.abs(high(code, end_date) - delay_high), np.abs(low(code, end_date) - delay_low))
    part2 = part2[~condition2]
    part2 = part2.iloc[-12:, :].sum()
    result = part1 / (part1 + part2)
    alpha = result
    return alpha


def alpha_050(code, end_date=None):
    '''
    公式：
        SUM(((HIGH+LOW)<=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(LOW-DELAY(L OW,1)))),12)/(SUM(((HIGH+LOW)<=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(L OW-DELAY(LOW,1)))),12)+SUM(((HIGH+LOW)>=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HI GH,1)),ABS(LOW-DELAY(LOW,1)))),12))-SUM(((HIGH+LOW)>=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(LOW-DELAY(LOW,1)))),12)/(SUM(((HIGH+LOW)>=(DELAY(HIGH,1)+DELAY(LOW,1))?0: MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(LOW-DELAY(LOW,1)))),12)+SUM(((HIGH+LOW)<=(DELAY(HIGH,1)+DELA Y(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(LOW-DELAY(LOW,1)))),12))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    cond1 = (high(code, end_date) + low(code, end_date)) <= (high(code, end_date).shift() + low(code, end_date).shift())
    data1 = np.maximum(abs(high(code, end_date) - high(code, end_date).shift()),
                       abs(low(code, end_date) - low(code, end_date).shift()))
    data1[cond1] = 0
    part1 = pd_rolling_sum(data1, 12)
    data2 = np.maximum(abs(high(code, end_date) - high(code, end_date).shift()),
                       abs(low(code, end_date) - low(code, end_date).shift()))
    data2[~cond1] = 0
    part2 = pd_rolling_sum(data2, 12)
    alpha = part1 / (part1 + part2) - part2 / (part1 + part2)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_051(code, end_date=None):
    '''
    公式：
        SUM(((HIGH+LOW)<=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(LOW-DELAY(L OW,1)))),12)/(SUM(((HIGH+LOW)<=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(L OW-DELAY(LOW,1)))),12)+SUM(((HIGH+LOW)>=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HI GH,1)),ABS(LOW-DELAY(LOW,1)))),12))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    cond1 = (high(code, end_date) + low(code, end_date)) <= (high(code, end_date).shift() + low(code, end_date).shift())
    data1 = np.maximum(abs(high(code, end_date) - high(code, end_date).shift()),
                       abs(low(code, end_date) - low(code, end_date).shift()))
    data1[cond1] = 0
    part1 = pd_rolling_sum(data1, 12)

    data2 = np.maximum(abs(high(code, end_date) - high(code, end_date).shift()),
                       abs(low(code, end_date) - low(code, end_date).shift()))
    data2[~cond1] = 0
    part2 = pd_rolling_sum(data2, 12)
    alpha = part1 / (part1 + part2)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_052(code, end_date=None):
    '''
    公式：
        SUM(MAX(0,HIGH-DELAY((HIGH+LOW+CLOSE)/3,1)),26)/SUM(MAX(0,DELAY((HIGH+LOW+CLOSE)/3,1)-L),26)* 100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay = ((high(code, end_date) + low(code, end_date) + close(code, end_date)) / 3).shift()
    part1 = (np.maximum(high(code, end_date) - delay, 0)).iloc[-26:, :]

    part2 = (np.maximum(delay - low(code, end_date), 0)).iloc[-26:, :]
    alpha = part1.sum() + part2.sum()
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_053(code, end_date=None):
    '''
    公式：
       COUNT(CLOSE>DELAY(CLOSE,1),12)/12*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay = close(code, end_date).shift()
    condition = close(code, end_date) > delay
    result = close(code, end_date)[condition].iloc[-12:, :]
    alpha = result.count() * 100 / 12
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_054(code, end_date=None):
    '''
    公式：
       (-1 * RANK((STD(ABS(CLOSE-OPEN)) + (CLOSE-OPEN)) + CORR(CLOSE, OPEN,10)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part1 = (close(code, end_date) - open(code, end_date)).abs()
    part1 = part1.std()
    part2 = (close(code, end_date) - open(code, end_date)).iloc[-1, :]
    part3 = close(code, end_date).iloc[-10:, :].corrwith(open(code, end_date).iloc[-10:, :])
    result = (part1 + part2 + part3)
    alpha = result.rank(pct=True)
    return alpha


# 公式有误，以自行修正
def alpha_055(code, end_date=None):
    '''
    公式：
        SUM(16*(CLOSE-DELAY(CLOSE,1)+(CLOSE-OPEN)/2+DELAY(CLOSE,1)-DELAY(OPEN,1))/((ABS(HIGH-DELAY(CL OSE,1))>ABS(LOW-DELAY(CLOSE,1))&ABS(HIGH-DELAY(CLOSE,1))>ABS(HIGH-DELAY(LOW,1))?ABS(HIGH-DELAY(CLOSE,1))+ABS(LOW-DELAY(CLOS E,1))/2+ABS(DELAY(CLOSE,1)-DELAY(OPEN,1))/4:(ABS(LOW-DELAY(CLOSE,1))>ABS(HIGH-DELAY(LOW,1))   & ABS(LOW-DELAY(CLOSE,1))>ABS(HIGH-DELAY(CLOSE,1))?ABS(LOW-DELAY(CLOSE,1))+ABS(HIGH-DELAY(CLO SE,1))/2+ABS(DELAY(CLOSE,1)-DELAY(OPEN,1))/4:ABS(HIGH-DELAY(LOW,1))+ABS(DELAY(CLOSE,1)-DELAY(OP EN,1))/4)))*MAX(ABS(HIGH-DELAY(CLOSE,1)),ABS(LOW-DELAY(CLOSE,1))),20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp1 = 16 * (close(code, end_date) - close(code, end_date).shift() + (
                close(code, end_date) - open(code, end_date)) / 2 + close(code, end_date).shift() - open(code,
                                                                                                         end_date).shift())
    temp2 = (abs(high(code, end_date) - close(code, end_date).shift()))
    temp3 = abs(low(code, end_date) - close(code, end_date).shift())
    temp4 = abs(high(code, end_date) - low(code, end_date).shift())
    temp5 = abs(close(code, end_date).shift() - open(code, end_date).shift())
    cond1 = temp1 / temp2 > temp3
    cond2 = temp2 > temp4
    data1 = temp2 + temp3 / 2 + temp5 / 4
    cond3 = temp3 > temp4
    cond4 = temp3 > temp2
    data1[(~(cond1 & cond2)) & (cond3 & cond4)] = temp3 + temp2 / 2 + temp5 / 4
    data1[(~(cond1 & cond2)) & ~(cond3 & cond4)] = temp4 + temp5 / 4
    part1 = abs(data1)
    part2 = np.maximum(temp2, temp3)
    alpha = pd_rolling_sum(part1 * part2, 20)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_056(code, end_date=None):
    '''
    公式：
        (RANK((OPEN-TSMIN(OPEN,12)))<RANK((RANK(CORR(SUM(((HIGH+LOW)/2),19),SUM(MEAN(VOLUME,40),19),13))^5)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part1 = (open(code, end_date) - pd_rolling_min(open(code, end_date), 12)).rank(pct=True)
    temp1 = pd_rolling_sum((high(code, end_date) + low(code, end_date)) / 2, 19)
    temp2 = pd_rolling_sum(pd_rolling_mean(volume(code, end_date), 40), 19)
    temp3 = pd_rolling_corr(temp1, temp2, 13).rank(pct=True)
    part2 = (temp3 ** 5).rank(pct=True)
    alpha = part1 - part2
    alpha = alpha.iloc[-1, :]
    for stock in code:
        if alpha[stock] < 0:
            alpha[stock] = 1
        elif alpha[stock] > 0:
            alpha[stock] = -1
    return alpha


def alpha_057(code, end_date=None):
    '''
    公式：
        SMA((CLOSE-TSMIN(LOW,9))/(TSMAX(HIGH,9)-TSMIN(LOW,9))*100,3,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part1 = close(code, end_date) - pd_rolling_min(low(code, end_date), 9)
    part2 = pd_rolling_max(high(code, end_date), 9) - pd_rolling_min(low(code, end_date), 9)
    result = pd_ewma(100 * part1 / part2, span=5)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_058(code, end_date=None):
    '''
    公式：
        COUNT(CLOSE>DELAY(CLOSE,1),20)/20*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay = close(code, end_date).shift()
    condition = close(code, end_date) > delay
    result = close(code, end_date)[condition].iloc[-20:, :]
    alpha = result.count() * 100 / 20
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_059(code, end_date=None):
    '''
    公式：
        SUM((CLOSE=DELAY(CLOSE,1)?0:CLOSE-(CLOSE>DELAY(CLOSE,1)?MIN(LOW,DELAY(CLOSE,1)):MAX(HIGH,D ELAY(CLOSE,1)))),20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay = close(code, end_date).shift()
    condition1 = (close(code, end_date) > delay)
    condition2 = (close(code, end_date) < delay)
    part1 = np.minimum(low(code, end_date)[condition1], delay[condition1]).fillna(0)
    part2 = np.maximum(high(code, end_date)[condition2], delay[condition2]).fillna(0)
    part1 = part1.iloc[-20:, :]
    part2 = part2.iloc[-20:, :]
    result = close(code, end_date) - part1 - part2
    alpha = result.sum()
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_060(code, end_date=None):
    '''
    公式：
        SUM(((CLOSE-LOW)-(HIGH-CLOSE))./(HIGH-LOW).*VOLUME,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part1 = (close(code, end_date).iloc[-20:, :] - low(code, end_date).iloc[-20:, :]) - (
                high(code, end_date).iloc[-20:, :] - close(code, end_date).iloc[-20:, :])
    part2 = high(code, end_date).iloc[-20:, :] - low(code, end_date).iloc[-20:, :]
    result = volume(code, end_date).iloc[-20:, :] * part1 / part2
    alpha = result.sum()
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_061(code, end_date=None):
    '''
    公式：
        (MAX(RANK(DECAYLINEAR(DELTA(VWAP,   1), 12)),RANK(DECAYLINEAR(RANK(CORR((LOW),MEAN(VOLUME,80), 8)), 17))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = func_decaylinear(vwap(code, end_date).diff(1), 12)
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True)
    temp_1 = pd_rolling_corr(low(code, end_date), pd_rolling_mean(volume(code, end_date), 80), 8).rank(axis=0, pct=True)
    part_2 = func_decaylinear(temp_1, 17)
    cond2 = part_2 == 0
    part_2[cond2] = nan
    part_2 = part_2.rank(axis=1, pct=True)
    alpha = np.maximum(part_1.iloc[:, -1], part_2.iloc[:, -1]) * -1
    return alpha


def alpha_062(code, end_date=None):
    '''
    公式：
        (-1 * CORR(HIGH, RANK(VOLUME), 5))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = volume(code, end_date).rank(axis=0, pct=True)
    alpha = pd_rolling_corr(high(code, end_date), part_1, 5) * -1
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_063(code, end_date=None):
    '''
    公式：
        SMA(MAX(CLOSE-DELAY(CLOSE,1),0),6,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),6,1)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part1 = np.maximum(close(code, end_date) - close(code, end_date).shift(), 0)
    part1 = pd_ewma(part1, span=11)
    part2 = (close(code, end_date) - close(code, end_date).shift()).abs()
    part2 = pd_ewma(part2, span=11)
    result = part1 * 100 / part2
    alpha = result.iloc[-1, :]
    return alpha


def alpha_064(code, end_date=None):
    '''
    公式：
        (MAX(RANK(DECAYLINEAR(CORR(RANK(VWAP),  RANK(VOLUME),   4), 4)),RANK(DECAYLINEAR(MAX(CORR(RANK(CLOSE), RANK(MEAN(VOLUME,60)), 4), 13), 14))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_rolling_corr(vwap(code, end_date).rank(axis=0, pct=True), volume(code, end_date).rank(axis=0, pct=True),
                             4)
    part_1 = func_decaylinear(temp_1, 4)
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True)
    temp_2 = pd_rolling_corr(close(code, end_date).rank(axis=0, pct=True),
                             pd_rolling_mean(volume(code, end_date), 60).rank(axis=0, pct=True), 4)
    temp_3 = np.maximum(temp_2, 13)
    part_2 = func_decaylinear(temp_3, 14).rank(axis=1, pct=True)
    cond2 = part_2 == 0
    part_2[cond2] = nan
    part_2 = part_2.rank(axis=1, pct=True)
    alpha = np.maximum(part_1.iloc[:, -1], part_2.iloc[:, -1]) * -1
    return alpha


def alpha_065(code, end_date=None):
    '''
    公式：
        MEAN(CLOSE,6)/CLOSE
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = pd_rolling_mean(close(code, end_date), 6) / close(code, end_date)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_066(code, end_date=None):
    '''
    公式：
        (CLOSE-MEAN(CLOSE,6))/MEAN(CLOSE,6)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = ((close(code, end_date) - pd_rolling_mean(close(code, end_date), 6)) / pd_rolling_mean(
        close(code, end_date), 6)) * 100
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_067(code, end_date=None):
    '''
    公式：
        SMA(MAX(CLOSE-DELAY(CLOSE,1),0),24,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),24,1)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp1 = close(code, end_date) - close(code, end_date).shift()
    part1 = np.maximum(temp1, 0)
    part1 = pd_ewma(part1, span=47)
    temp2 = temp1.abs()
    part2 = pd_ewma(temp2, span=47)
    result = part1 * 100 / part2
    alpha = result.iloc[-1, :]
    return alpha


def alpha_068(code, end_date=None):
    '''
    公式：
        SMA(((HIGH+LOW)/2-(DELAY(HIGH,1)+DELAY(LOW,1))/2)*(HIGH-LOW)/VOLUME,15,2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part1 = (high(code, end_date) + low(code, end_date)) / 2 - high(code, end_date).shift()
    part2 = 0.5 * low(code, end_date).shift() * (high(code, end_date) - low(code, end_date)) / volume(code, end_date)
    result = (part1 + part2) * 100
    result = pd_ewma(result, span=29)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_069(code, end_date=None):
    '''
    公式：
        (SUM(DTM,20)>SUM(DBM,20)？(SUM(DTM,20)-SUM(DBM,20))/SUM(DTM,20)：(SUM(DTM,20)=SUM(DBM,20)？0：(SUM(DTM,20)-SUM(DBM,20))/SUM(DBM,20)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    condition1 = (pd_rolling_sum(func_dtm(code, end_date), 20) > pd_rolling_sum(func_dbm(code, end_date), 20))
    condition2 = (pd_rolling_sum(func_dtm(code, end_date), 20) < pd_rolling_sum(func_dbm(code, end_date), 20))

    indicator1 = (pd_rolling_sum(func_dtm(code, end_date), 20) - pd_rolling_sum(func_dbm(code, end_date),
                                                                                20)) / pd_rolling_sum(
        func_dtm(code, end_date), 20)
    indicator1[(~condition1) & condition2] = 0
    indicator1[(~condition1) & (-condition2)] = (pd_rolling_sum(func_dtm(code, end_date), 20) - pd_rolling_sum(
        func_dbm(code, end_date), 20)) / pd_rolling_sum(func_dbm(code, end_date), 20)
    alpha = indicator1.iloc[-1, :]
    for stock in code:
        if alpha[stock] == 0:
            alpha[stock] = nan
    return alpha


def alpha_070(code, end_date=None):
    '''
    公式：
        STD(AMOUNT,6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = amount(code, end_date).iloc[-6:, :].std()
    return alpha


def alpha_071(code, end_date=None):
    '''
    公式：
        (CLOSE-MEAN(CLOSE,24))/MEAN(CLOSE,24)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    data = (close(code, end_date) - pd_rolling_mean(close(code, end_date), 24)) / pd_rolling_mean(close(code, end_date),
                                                                                                  24)
    alpha = data.iloc[-1] * 100
    return alpha


def alpha_072(code, end_date=None):
    '''
    公式：
        SMA((TSMAX(HIGH,6)-CLOSE)/(TSMAX(HIGH,6)-TSMIN(LOW,6))*100,15,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    data1 = pd_rolling_max(high(code, end_date), 6) - close(code, end_date)
    data2 = pd_rolling_max(high(code, end_date), 6) - pd_rolling_min(low(code, end_date), 6)
    alpha = pd_ewma(data1 / data2 * 100, span=29).iloc[-1]
    return alpha


def alpha_073(code, end_date=None):
    '''
    公式：
        ((TSRANK(DECAYLINEAR(DECAYLINEAR(CORR((CLOSE),  VOLUME, 10),    16),    4), 5)  -RANK(DECAYLINEAR(CORR(VWAP, MEAN(VOLUME,30), 4),3))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_rolling_corr(close(code, end_date), volume(code, end_date), 10)
    temp_2 = func_decaylinear(temp_1, 16).T
    part_1 = func_decaylinear(temp_2, 4).iloc[:, -5:]
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True)
    temp_3 = pd_rolling_corr(vwap(code, end_date), pd_rolling_mean(volume(code, end_date), 30), 4)
    part_2 = func_decaylinear(temp_3, 3).rank(axis=1, pct=True)
    cond2 = part_2 == 0
    part_2[cond2] = nan
    part_2 = part_2.rank(axis=1, pct=True)
    alpha = (part_1.iloc[:, -1] - part_2.iloc[:, -1]) * -1
    return alpha


def alpha_074(code, end_date=None):
    '''
    公式：
       (RANK(CORR(SUM(((LOW *   0.35)   +   (VWAP   *   0.65)), 20),    SUM(MEAN(VOLUME,40),    20),    7)) +RANK(CORR(RANK(VWAP), RANK(VOLUME), 6)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_rolling_sum(low(code, end_date) * 0.35 + vwap(code, end_date) * 0.65, 20)
    temp_2 = pd_rolling_sum(pd_rolling_mean(volume(code, end_date), 40), 20)
    part_1 = pd_rolling_corr(temp_1, temp_2, 7).rank(axis=0, pct=True)

    temp_3 = vwap(code, end_date).rank(axis=0, pct=True)
    temp_4 = volume(code, end_date).rank(axis=0, pct=True)
    part_2 = pd_rolling_corr(temp_3, temp_4, 6).rank(axis=0, pct=True)
    alpha = part_1.iloc[-1, :] + part_1.iloc[-1, :]
    return alpha


def alpha_075(code, benchmark='000300.XSHG', end_date=None):
    '''
    公式：
       BANCHMARKINDEXCLOSE<BANCHMARKINDEXOPEN,50)/COUNT(BANCHMARKINDEXCLOSE<BANCHMARKIN DEXOPEN,50)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    condition1 = (close(code, end_date)) > (open(code, end_date))
    condition2 = benchmark_index_close(code, benchmark, end_date) > benchmark_index_open(code, benchmark, end_date)
    part_1 = sum(pd.DataFrame(np.ones(close(code, end_date).shape), index=close(code, end_date).index,
                              columns=close(code, end_date).columns)[(condition1) & (condition2)].fillna(0).iloc[-50:,
                 :])

    condition3 = benchmark_index_close(code, benchmark, end_date) < benchmark_index_open(code, benchmark, end_date)
    part_2 = sum(pd.DataFrame(np.ones(close(code, end_date).shape), index=close(code, end_date).index,
                              columns=close(code, end_date).columns)[(condition3)].fillna(0).iloc[-50:, :])
    alpha = part_1 / part_2
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_076(code, end_date=None):
    '''
    公式：
       STD(ABS((CLOSE/DELAY(CLOSE,1)-1))/VOLUME,20)/MEAN(ABS((CLOSE/DELAY(CLOSE,1)-1))/VOLUME,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = pd_rolling_std(abs(close(code, end_date) / close(code, end_date).shift(1) - 1) / volume(code, end_date),
                            20)
    part_2 = pd_rolling_mean(abs(close(code, end_date) / close(code, end_date).shift(1) - 1) / volume(code, end_date),
                             20)
    alpha = (part_1.iloc[-1, :] / part_2.iloc[-1, :])
    return alpha


def alpha_077(code, end_date=None):
    '''
    公式：
       MIN(RANK(DECAYLINEAR(((((HIGH + LOW) / 2) + HIGH) - (VWAP + HIGH)), 20)), RANK(DECAYLINEAR(CORR(((HIGH + LOW) / 2), MEAN(VOLUME,40), 3), 6)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = (high(code, end_date) + low(code, end_date)) / 2 + high(code, end_date) - vwap(code, end_date) - high(code,
                                                                                                                   end_date)
    part_1 = func_decaylinear(temp_1, 20)
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True)
    temp_2 = pd_rolling_corr((high(code, end_date) + low(code, end_date)) / 2,
                             pd_rolling_mean(volume(code, end_date), 40), 3)
    part_2 = func_decaylinear(temp_2, 6)
    cond2 = part_2 == 0
    part_2[cond2] = nan
    part_2 = part_2.rank(axis=1, pct=True)
    alpha = np.minimum(part_1.iloc[:, -1], part_2.iloc[:, -1])
    return alpha


def alpha_078(code, end_date=None):
    '''
    公式：
       ((HIGH+LOW+CLOSE)/3-MA((HIGH+LOW+CLOSE)/3,12))/(0.015*MEAN(ABS(CLOSE-MEAN((HIGH+LOW+CLOSE)/3,12)),12))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = (high(code, end_date) + low(code, end_date) + close(code, end_date)) / 3 - pd_rolling_mean(
        (high(code, end_date) + low(code, end_date) + close(code, end_date)) / 3, 12)
    temp_1 = abs(close(code, end_date) - pd_rolling_mean(
        (high(code, end_date) + low(code, end_date) + close(code, end_date)) / 3, 12))
    part_2 = pd_rolling_mean(temp_1, 12) * 0.015
    alpha = (part_1 / part_2).iloc[-1, :]
    return alpha


def alpha_079(code, end_date=None):
    '''
    公式：
       SMA(MAX(CLOSE-DELAY(CLOSE,1),0),12,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = pd_ewma(np.maximum((close(code, end_date) - close(code, end_date).shift(1)), 0), span=23)
    part_2 = pd_ewma(abs(close(code, end_date) - close(code, end_date).shift(1)), span=23)
    alpha = (part_1 / part_2 * 100).iloc[-1, :]
    return alpha


def alpha_080(code, end_date=None):
    '''
    公式：
       (VOLUME-DELAY(VOLUME,5))/DELAY(VOLUME,5)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = volume(code, end_date) - volume(code, end_date).shift(5)
    part_2 = volume(code, end_date).shift(5)
    alpha = (part_1 / part_2 * 100).iloc[-1, :]
    return alpha


def alpha_081(code, end_date=None):
    '''
    公式：
       SMA(VOLUME,21,2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    result = pd_ewma(volume(code, end_date), span=20)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_082(code, end_date=None):
    '''
    公式：
       SMA((TSMAX(HIGH,6)-CLOSE)/(TSMAX(HIGH,6)-TSMIN(LOW,6))*100,20,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part1 = pd_rolling_max(high(code, end_date), 6) - close(code, end_date)
    part2 = pd_rolling_max(high(code, end_date), 6) - pd_rolling_min(low(code, end_date), 6)
    result = pd_ewma(100 * part1 / part2, span=39)
    alpha = result.iloc[-1, :]
    return alpha


def alpha_083(code, end_date=None):
    '''
    公式：
       (-1 * RANK(COVIANCE(RANK(HIGH), RANK(VOLUME), 5)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part1 = high(code, end_date).rank(axis=0, pct=True)
    part1 = part1.iloc[-5:, :]
    part2 = volume(code, end_date).rank(axis=0, pct=True)
    part2 = part2.iloc[-5:, :]
    result = part1.corrwith(part2)
    alpha = -result
    return alpha


def alpha_084(code, end_date=None):
    '''
    公式：
       SUM((CLOSE>DELAY(CLOSE,1)?VOLUME:(CLOSE<DELAY(CLOSE,1)?-VOLUME:0)),20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    condition1 = (close(code, end_date) > close(code, end_date).shift())
    condition2 = (close(code, end_date) < close(code, end_date).shift())
    part1 = volume(code, end_date)[condition1].fillna(0)
    part2 = -volume(code, end_date)[condition2].fillna(0)
    result = part1.iloc[-20:, :] + part2.iloc[-20:, :]
    alpha = result.sum()
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_085(code, end_date=None):
    '''
    公式：
       (TSRANK((VOLUME / MEAN(VOLUME,20)), 20) * TSRANK((-1 * DELTA(CLOSE, 7)), 8))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = volume(code, end_date) / pd_rolling_mean(volume(code, end_date), 20)
    part_1 = temp_1.iloc[-20:, :].rank(axis=0, pct=True)
    temp_2 = close(code, end_date).diff(7) * -1
    part_2 = temp_2.iloc[-8:, :].rank(axis=0, pct=True)
    alpha = part_1.iloc[-1, :] * part_2.iloc[-1, :]
    return alpha


def alpha_086(code, end_date=None):
    '''
    公式：
       ((0.25 < (((DELAY(CLOSE, 20)-DELAY(CLOSE, 10)) / 10)-((DELAY(CLOSE, 10)-CLOSE) / 10))) ? (-1 * 1) :(((((DELAY(CLOSE, 20)-DELAY(CLOSE, 10)) / 10)-((DELAY(CLOSE, 10)-CLOSE) / 10)) < 0) ? 1 : ((-1 * 1) * (CLOSE-DELAY(CLOSE, 1)))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    delay10 = close(code, end_date).shift(10)
    delay20 = close(code, end_date).shift(20)
    indicator1 = pd.DataFrame(-np.ones(close(code, end_date).shape), index=close(code, end_date).index,
                              columns=close(code, end_date).columns)
    indicator2 = pd.DataFrame(np.ones(close(code, end_date).shape), index=close(code, end_date).index,
                              columns=close(code, end_date).columns)

    temp = (delay20 - delay10) / 10 - (delay10 - close(code, end_date)) / 10
    condition1 = (temp > 0.25)
    condition2 = (temp < 0)
    temp2 = (close(code, end_date) - close(code, end_date).shift()) * indicator1

    part_1 = indicator1[condition1].fillna(0)
    part_2 = indicator2[~condition1][condition2].fillna(0)
    part_3 = temp2[~condition1][~condition2].fillna(0)
    result = part_1 + part_2 + part_3
    alpha = result.iloc[-1, :]
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_087(code, end_date=None):
    '''
    公式：
       ((RANK(DECAYLINEAR(DELTA(VWAP, 4), 7)) + TSRANK(DECAYLINEAR(((((LOW * 0.9) + (LOW * 0.1))-VWAP) / (OPEN-((HIGH + LOW) / 2))), 11), 7)) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = func_decaylinear(vwap(code, end_date).diff(4), 7)
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True)
    temp_1 = low(code, end_date) * 0.9 + low(code, end_date) * 0.9 - vwap(code, end_date)
    temp_2 = open(code, end_date) - (high(code, end_date) + low(code, end_date)) / 2
    part_2 = func_decaylinear(temp_1 / temp_2, 11).iloc[:, -7:]
    cond2 = part_2 == 0
    part_2[cond2] = nan
    part_2 = part_2.rank(axis=1, pct=True)
    alpha = (part_1.iloc[:, -1] + part_2.iloc[:, -1]) * -1
    return alpha


def alpha_088(code, end_date=None):
    '''
    公式：
       (CLOSE-DELAY(CLOSE,20))/DELAY(CLOSE,20)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = (close(code, end_date) - close(code, end_date).shift(20)) / close(code, end_date).shift(20)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_089(code, end_date=None):
    '''
    公式：
       2*(SMA(CLOSE,13,2)-SMA(CLOSE,27,2)-SMA(SMA(CLOSE,13,2)-SMA(CLOSE,27,2),10,2))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    data1 = pd_ewma(close(code, end_date), span=12, adjust=False)
    data2 = pd_ewma(close(code, end_date), span=26, adjust=False)
    data3 = pd_ewma(data1 - data2, span=9, adjust=False)
    alpha = ((data1 - data2 - data3) * 2).iloc[-1, :]
    alpha = alpha
    return alpha


def alpha_090(code, end_date=None):
    '''
    公式：
       ( RANK(CORR(RANK(VWAP), RANK(VOLUME), 5)) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    data1 = vwap(code, end_date).rank(axis=0, pct=True)
    data2 = volume(code, end_date).rank(axis=0, pct=True)
    corr = data1.iloc[-5:, :].corrwith(data2.iloc[-5:, :])
    rank1 = corr.rank(pct=True)
    alpha = rank1 * -1
    return alpha


def alpha_091(code, end_date=None):
    '''
    公式：
       ((RANK((CLOSE-MAX(CLOSE, 5)))*RANK(CORR((MEAN(VOLUME,40)), LOW, 5))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    data1 = close(code, end_date)
    cond = data1 > 5
    data1[~cond] = 5
    rank1 = ((close(code, end_date) - data1).rank(axis=1, pct=True)).iloc[-1, :]
    mean = pd_rolling_mean(volume(code, end_date), 40)
    corr = mean.iloc[-5:, :].corrwith(low(code, end_date).iloc[-5:, :])
    rank2 = corr.rank(pct=True)
    alpha = rank1 * rank2 * (-1)
    return alpha


def alpha_092(code, end_date=None):
    '''
    公式：
       (MAX(RANK(DECAYLINEAR(DELTA(((CLOSE  *   0.35)   +   (VWAP   *0.65)),    2), 3)),TSRANK(DECAYLINEAR(ABS(CORR((MEAN(VOLUME,180)), CLOSE, 13)), 5), 15)) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = close(code, end_date) * 0.35 + vwap(code, end_date) * 0.65
    part_1 = func_decaylinear(temp_1.diff(2), 3)
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True)
    temp_2 = abs(pd_rolling_corr(pd_rolling_mean(volume(code, end_date), 180), close(code, end_date), 13))
    part_2 = func_decaylinear(temp_2, 5).iloc[:, -15:]
    cond2 = part_2 == 0
    part_2[cond2] = nan
    part_2 = part_2.rank(axis=1, pct=True)
    alpha = np.maximum(part_1.iloc[:, -1], part_2.iloc[:, -1]) * -1
    return alpha


def alpha_093(code, end_date=None):
    '''
    公式：
       SUM((OPEN>=DELAY(OPEN,1)?0:MAX((OPEN-LOW),(OPEN-DELAY(OPEN,1)))),20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    cond = open(code, end_date) >= open(code, end_date).shift()
    data1 = open(code, end_date) - low(code, end_date)
    data2 = open(code, end_date) - open(code, end_date).shift()
    cond_max = data1 > data2
    data2[cond_max] = data1[cond_max]
    data2[cond] = 0
    alpha = data2.iloc[-20:, :].sum()
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_094(code, end_date=None):
    '''
    公式：
       SUM((CLOSE>DELAY(CLOSE,1)?VOLUME:(CLOSE<DELAY(CLOSE,1)?-VOLUME:0)),30)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    cond1 = close(code, end_date) > close(code, end_date).shift()
    cond2 = close(code, end_date) < close(code, end_date).shift()
    value = -volume(code, end_date)
    value[~cond2] = 0
    value[cond1] = volume(code, end_date)[cond1]
    alpha = value.iloc[-30:, :].sum()
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_095(code, end_date=None):
    '''
    公式：
       STD(AMOUNT,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = amount(code, end_date).iloc[-20:, :].std(axis=0)
    return alpha


def alpha_096(code, end_date=None):
    '''
    公式：
       SMA(SMA((CLOSE-TSMIN(LOW,9))/(TSMAX(HIGH,9)-TSMIN(LOW,9))*100,3,1),3,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_ewma(100 * (close(code, end_date) - pd_rolling_min(low(code, end_date), 9)) / (
                pd_rolling_max(high(code, end_date), 9) - pd_rolling_min(low(code, end_date), 9)), span=5, adjust=False)
    alpha = pd_ewma(temp_1, span=5, adjust=False).iloc[-1, :]
    return alpha


def alpha_097(code, end_date=None):
    '''
    公式：
       STD(VOLUME,10)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = volume(code, end_date).iloc[-10:, :].std(axis=0)
    return alpha


def alpha_098(code, end_date=None):
    '''
    公式：
       ((((DELTA((SUM(CLOSE, 100) / 100), 100) / DELAY(CLOSE, 100)) < 0.05) || ((DELTA((SUM(CLOSE, 100) / 100), 100) /DELAY(CLOSE, 100)) == 0.05)) ? (-1 * (CLOSE-TSMIN(CLOSE, 100))) : (-1 * DELTA(CLOSE, 3)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    sum_close = pd_rolling_sum(close(code, end_date), 100)
    cond = (sum_close / 100 - (sum_close / 100).shift(100)) / close(code, end_date).shift(100) <= 0.05
    left_value = -(close(code, end_date) - pd_rolling_min(close(code, end_date), 100))
    right_value = -(close(code, end_date) - close(code, end_date).shift(3))
    right_value[cond] = left_value[cond]
    alpha = right_value.iloc[-1, :]
    return alpha


def alpha_099(code, end_date=None):
    '''
    公式：
       (-1 * RANK(COVIANCE(RANK(CLOSE), RANK(VOLUME), 5)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = (-pd_rolling_cov(close(code, end_date).rank(axis=1, pct=True),
                             volume(code, end_date).rank(axis=1, pct=True), 5).rank(axis=0, pct=True)).iloc[-1,
            :]
    return alpha


def alpha_100(code, end_date=None):
    '''
    公式：
       STD(VOLUME,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = volume(code, end_date).iloc[-20:, :].std(axis=0)
    return alpha


def alpha_101(code, end_date=None):
    '''
    公式：
       ((RANK(CORR(CLOSE, SUM(MEAN(VOLUME,30), 37), 15)) < RANK(CORR(RANK(((HIGH * 0.1) + (VWAP * 0.9))),RANK(VOLUME), 11))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_rolling_sum(pd_rolling_mean(volume(code, end_date), 30), 37)
    part_1 = pd_rolling_corr(close(code, end_date), temp_1, 15).rank(axis=0, pct=True)
    temp_2 = (high(code, end_date) * 0.1 + vwap(code, end_date) * 0.9).rank(axis=0, pct=True)
    temp_3 = volume(code, end_date).rank(axis=0, pct=True)
    part_2 = pd_rolling_corr(temp_2, temp_3, 11)
    alpha = part_1 - part_2
    alpha = alpha.iloc[-1, :]
    cond1 = alpha < 0
    cond2 = alpha > 0
    alpha[cond1] = -1
    alpha[cond2] = 1
    return alpha


def alpha_102(code, end_date=None):
    '''
    公式：
       SMA(MAX(VOLUME-DELAY(VOLUME,1),0),6,1)/SMA(ABS(VOLUME-DELAY(VOLUME,1)),6,1)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    max_cond = (volume(code, end_date) - volume(code, end_date).shift()) > 0
    max_data = volume(code, end_date) - volume(code, end_date).shift()
    max_data[~max_cond] = 0
    sma1 = pd_ewma(max_data, span=11, adjust=False)
    sma2 = pd_ewma((volume(code, end_date) - volume(code, end_date).shift()).abs(), span=11, adjust=False)
    alpha = (sma1 / sma2 * 100).iloc[-1, :]
    alpha = alpha
    return alpha


def alpha_103(code, end_date=None):
    '''
    公式：
       ((20-LOWDAY(LOW,20))/20)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = (20 - func_lowday(low(code, end_date), 20)) / 20 * 100
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_104(code, end_date=None):
    '''
    公式：
       (-1 * (DELTA(CORR(HIGH, VOLUME, 5), 5) * RANK(STD(CLOSE, 20))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = pd_rolling_corr(high(code, end_date), volume(code, end_date), 5).diff(5)
    part_2 = pd_rolling_std(close(code, end_date), 20).rank(axis=0, pct=True)
    alpha = -part_1 * part_2
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_105(code, end_date=None):
    '''
    公式：
       (-1 * CORR(RANK(OPEN), RANK(VOLUME), 10))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = -pd_rolling_corr(open(code, end_date).rank(axis=0, pct=True), volume(code, end_date).rank(axis=0, pct=True),
                             10)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_106(code, end_date=None):
    '''
    公式：
       CLOSE-DELAY(CLOSE,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = close(code, end_date) - close(code, end_date).shift(20)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_107(code, end_date=None):
    '''
    公式：
       (((-1 * RANK((OPEN-DELAY(HIGH, 1)))) * RANK((OPEN-DELAY(CLOSE, 1)))) * RANK((OPEN-DELAY(LOW, 1))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    rank1 = -(open(code, end_date) - high(code, end_date).shift()).rank(axis=0, pct=True)
    rank2 = (open(code, end_date) - close(code, end_date).shift()).rank(axis=0, pct=True)
    rank3 = (open(code, end_date) - low(code, end_date).shift()).rank(axis=0, pct=True)
    alpha = (rank1 * rank2 * rank3).iloc[-1, :]
    alpha = alpha
    return alpha


def alpha_108(code, end_date=None):
    '''
    公式：
       ((RANK((HIGH-MIN(HIGH, 2)))^RANK(CORR((VWAP), (MEAN(VOLUME,120)), 6))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = (high(code, end_date) - np.minimum(high(code, end_date), 2)).rank(axis=0, pct=True)
    part_2 = pd_rolling_corr(vwap(code, end_date), pd_rolling_mean(volume(code, end_date), 120), 6).rank(axis=0,
                                                                                                         pct=True)
    alpha = (part_1.iloc[-1, :] ** part_1.iloc[-1, :]) * -1
    alpha = alpha
    return alpha


def alpha_109(code, end_date=None):
    '''
    公式：
       SMA(HIGH-LOW,10,2)/SMA(SMA(HIGH-LOW,10,2),10,2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    data = high(code, end_date) - low(code, end_date)
    sma1 = pd_ewma(data, span=9, adjust=False)
    sma2 = pd_ewma(sma1, span=9, adjust=False)
    alpha = (sma1 / sma2).iloc[-1, :]
    alpha = alpha
    return alpha


def alpha_110(code, end_date=None):
    '''
    公式：
       SUM(MAX(0,HIGH-DELAY(CLOSE,1)),20)/SUM(MAX(0,DELAY(CLOSE,1)-LOW),20)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    data1 = high(code, end_date) - close(code, end_date).shift()
    data2 = close(code, end_date).shift() - low(code, end_date)
    max_cond1 = data1 < 0
    max_cond2 = data2 < 0
    data1[max_cond1] = 0
    data2[max_cond2] = 0
    sum1 = pd_rolling_sum(data1, 20)
    sum2 = pd_rolling_sum(data2, 20)
    alpha = sum1 / sum2 * 100
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_111(code, end_date=None):
    '''
    公式：
       SMA(VOL*((CLOSE-LOW)-(HIGH-CLOSE))/(HIGH-LOW),11,2)-SMA(VOL*((CLOSE-LOW)-(HIGH-CLOSE))/(HIGH-L OW),4,2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    data1 = volume(code, end_date) * (
                (close(code, end_date) - low(code, end_date)) - (high(code, end_date) - close(code, end_date))) / (
                        high(code, end_date) - low(code, end_date))
    x = pd_ewma(data1, span=10)
    y = pd_ewma(data1, span=3)
    alpha = (x - y).iloc[-1, :]
    return alpha


def alpha_112(code, end_date=None):
    '''
    公式：
       (SUM((CLOSE-DELAY(CLOSE,1)>0?CLOSE-DELAY(CLOSE,1):0),12)-SUM((CLOSE-DELAY(CLOSE,1)<0?ABS(CLOS E-DELAY(CLOSE,1)):0),12))/(SUM((CLOSE-DELAY(CLOSE,1)>0?CLOSE-DELAY(CLOSE,1):0),12)+SUM((CLOSE-DE LAY(CLOSE,1)<0?ABS(CLOSE-DELAY(CLOSE,1)):0),12))*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    cond1 = close(code, end_date) > close(code, end_date).shift()
    cond2 = close(code, end_date) < close(code, end_date).shift()
    data1 = close(code, end_date) - close(code, end_date).shift()
    data2 = close(code, end_date) - close(code, end_date).shift()
    data1[~cond1] = 0
    data2[~cond2] = 0
    data2 = data2.abs()
    sum1 = pd_rolling_sum(data1, 12)
    sum2 = pd_rolling_sum(data2, 12)
    alpha = ((sum1 - sum2) / (sum1 + sum2) * 100).iloc[-1, :]
    return alpha


def alpha_113(code, end_date=None):
    '''
    公式：
       (-1 * ((RANK((SUM(DELAY(CLOSE, 5), 20) / 20)) * CORR(CLOSE, VOLUME, 2)) * RANK(CORR(SUM(CLOSE, 5),SUM(CLOSE, 20), 2))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = (pd_rolling_sum(close(code, end_date).shift(5), 20) / 20).rank(axis=0, pct=True)
    part_2 = pd_rolling_corr(close(code, end_date), volume(code, end_date), 2)
    part_3 = pd_rolling_corr(pd_rolling_sum(close(code, end_date), 5), pd_rolling_sum(close(code, end_date), 20),
                             2).rank(axis=0, pct=True)
    alpha = -part_1.iloc[-1, :] * part_2.iloc[-1, :] * part_3.iloc[-1, :]
    return alpha


def alpha_114(code, end_date=None):
    '''
    公式：
       ((RANK(DELAY(((HIGH-LOW) / (SUM(CLOSE, 5) / 5)), 2)) * RANK(RANK(VOLUME))) / (((HIGH-LOW) / (SUM(CLOSE, 5) / 5)) / (VWAP-CLOSE)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = (high(code, end_date) - low(code, end_date)) / (pd_rolling_sum(close(code, end_date), 5) / 5)
    part_1 = (temp_1.shift(2)).rank(axis=0, pct=True).iloc[-1, :]
    part_2 = ((volume(code, end_date).rank(axis=0, pct=True)).rank(axis=0, pct=True)).iloc[-1, :]

    part_3 = (((high(code, end_date) - low(code, end_date)) / (pd_rolling_sum(close(code, end_date), 5) / 5)) / (
                vwap(code, end_date) - close(code, end_date))).iloc[-1, :]
    alpha = (part_1 * part_2) / part_3
    return alpha


def alpha_115(code, end_date=None):
    '''
    公式：
       (RANK(CORR(((HIGH * 0.9) + (CLOSE * 0.1)), MEAN(VOLUME,30), 10))^RANK(CORR(TSRANK(((HIGH + LOW) /  2), 4), TSRANK(VOLUME, 10), 7)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = pd_rolling_corr((high(code, end_date) * 0.9 + close(code, end_date) * 0.1),
                             pd_rolling_mean(volume(code, end_date), 30), 10).rank(axis=0, pct=True)
    temp_1 = func_tsrank((high(code, end_date) + low(code, end_date)) / 2, 4)
    temp_2 = func_tsrank(volume(code, end_date), 10)
    part_2 = pd_rolling_corr(temp_1, temp_2, 7)
    alpha = part_1.iloc[-1, :] ** part_2.iloc[-1, :]
    return alpha


def alpha_116(code, end_date=None):
    '''
    公式：
       REGBETA(CLOSE,SEQUENCE,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    sequence = pd.Series(range(1, 21), index=close(code, end_date).iloc[-20:, ].index)  # 1~20
    corr = close(code, end_date).iloc[-20:, :].corrwith(sequence)
    alpha = corr
    return alpha


def alpha_117(code, end_date=None):
    '''
    公式：
       ((TSRANK(VOLUME, 32) * (1-TSRANK(((CLOSE + HIGH)-LOW), 16))) * (1-TSRANK(RET, 32)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = func_tsrank(volume(code, end_date), 32)
    part_2 = 1 - func_tsrank(close(code, end_date) + high(code, end_date) - low(code, end_date), 16)
    part_3 = 1 - func_tsrank(func_ret(code, end_date), 32)
    alpha = part_1 * part_2 * part_3
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_118(code, end_date=None):
    '''
    公式：
       SUM(HIGH-OPEN,20)/SUM(OPEN-LOW,20)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = pd_rolling_sum(high(code, end_date) - open(code, end_date), 20)
    part_2 = pd_rolling_sum(open(code, end_date) - low(code, end_date), 20)
    alpha = part_1.iloc[-1, :] / part_2.iloc[-1, :] * 100
    return alpha


def alpha_119(code, end_date=None):
    '''
    公式：
       (RANK(DECAYLINEAR(CORR(VWAP, SUM(MEAN(VOLUME,5), 26),    5), 7)) -RANK(DECAYLINEAR(TSRANK(MIN(CORR(RANK(OPEN), RANK(MEAN(VOLUME,15)), 21), 9), 7), 8)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_rolling_corr(vwap(code, end_date), pd_rolling_sum(pd_rolling_mean(volume(code, end_date), 5), 26), 5)
    part_1 = func_decaylinear(temp_1, 7)
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True)
    temp_2 = pd_rolling_corr(open(code, end_date).rank(axis=0, pct=True),
                             pd_rolling_mean(volume(code, end_date), 15).rank(axis=0, pct=True), 21)
    temp_3 = func_tsrank(pd_rolling_min(temp_2, 9), 7)
    part_2 = func_decaylinear(temp_3, 8)
    cond2 = part_2 == 0
    part_2[cond2] = nan
    part_2 = part_2.rank(axis=1, pct=True)
    alpha = part_1.iloc[:, -1] - part_2.iloc[:, -1]
    return alpha


def alpha_120(code, end_date=None):
    '''
    公式：
       (RANK((VWAP-CLOSE)) / RANK((VWAP + CLOSE)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    data1 = (vwap(code, end_date) - close(code, end_date)).rank(axis=0, pct=True)
    data2 = (vwap(code, end_date) + close(code, end_date)).rank(axis=0, pct=True)
    alpha = (data1 / data2).iloc[-1, :]
    return alpha


def alpha_121(code, end_date=None):
    '''
    公式：
       ((RANK((VWAP-MIN(VWAP, 12)))^TSRANK(CORR(TSRANK(VWAP, 20), TSRANK(MEAN(VOLUME,60), 2), 18), 3))  *-1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = (vwap(code, end_date) - pd_rolling_min(vwap(code, end_date), 12)).rank(axis=0, pct=True)
    temp_1 = func_tsrank(vwap(code, end_date), 20)
    temp_2 = func_tsrank(pd_rolling_mean(volume(code, end_date), 60), 2)
    part_2 = func_tsrank(pd_rolling_corr(temp_1, temp_2, 18), 3)
    alpha = part_1 ** part_2 * -1
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_122(code, end_date=None):
    '''
    公式：
       (SMA(SMA(SMA(LOG(CLOSE),13,2),13,2),13,2)-DELAY(SMA(SMA(SMA(LOG(CLOSE),13,2),13,2),13,2),1))/DELAY(SM A(SMA(SMA(LOG(CLOSE),13,2),13,2),13,2),1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    log_close = np.log(close(code, end_date))
    data = pd_ewma(pd_ewma(pd_ewma(np.log(close(code, end_date)), span=12, adjust=False), span=12, adjust=False),
                   span=12, adjust=False)
    alpha = (data.iloc[-1, :] / data.iloc[-2, :]) - 1
    return alpha


def alpha_123(code, end_date=None):
    '''
    公式：
       ((RANK(CORR(SUM(((HIGH + LOW) / 2), 20), SUM(MEAN(VOLUME,60), 20), 9)) < RANK(CORR(LOW, VOLUME,6))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_rolling_sum((high(code, end_date) + low(code, end_date)) / 2, 20)
    temp_2 = pd_rolling_sum(pd_rolling_mean(volume(code, end_date), 60), 20)
    part_1 = pd_rolling_corr(temp_1, temp_2, 9)
    part_2 = pd_rolling_corr(low(code, end_date), volume(code, end_date), 6).rank(axis=0, pct=True)
    alpha = part_1 - part_2
    alpha = alpha.iloc[-1, :]
    cond1 = alpha < 0
    cond2 = alpha > 0
    alpha[cond1] = -1
    alpha[cond2] = 1
    return alpha


def alpha_124(code, end_date=None):
    '''
    公式：
       (CLOSE-VWAP) / DECAYLINEAR(RANK(TSMAX(CLOSE, 30)),2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = close(code, end_date) - vwap(code, end_date)
    temp_1 = pd_rolling_max(close(code, end_date), 30).rank(axis=0, pct=True)
    part_2 = func_decaylinear(temp_1, 2)
    alpha = part_1.iloc[-1, :] / part_2.iloc[:, -1]
    return alpha


def alpha_125(code, end_date=None):
    '''
    公式：
       (RANK(DECAYLINEAR(CORR((VWAP), MEAN(VOLUME,80),17), 20)) / RANK(DECAYLINEAR(DELTA(((CLOSE * 0.5)+ (VWAP * 0.5)), 3), 16)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_rolling_corr(vwap(code, end_date), pd_rolling_mean(volume(code, end_date), 80), 17)
    part_1 = func_decaylinear(temp_1, 20)
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True)
    temp_2 = (close(code, end_date) * 0.5 + vwap(code, end_date) * 0.5).shift(3)
    part_2 = func_decaylinear(temp_2, 16)
    cond2 = part_2 == 0
    part_2[cond2] = nan
    part_2 = part_2.rank(axis=1, pct=True)
    alpha = part_1 / part_2
    alpha = alpha.iloc[:, -1]
    return alpha


def alpha_126(code, end_date=None):
    '''
    公式：
       (CLOSE+HIGH+LOW)/3
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = close(code, end_date) + high(code, end_date) + low(code, end_date)
    alpha = alpha / 3
    alpha = alpha.iloc[-1, :]
    return alpha


# 公式应该是有误
def alpha_127(code, end_date=None):
    '''
    公式：
       (MEAN((100*(CLOSE-MAX(CLOSE,12))/(MAX(CLOSE,12)))^2))^(1/2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = (close(code, end_date) - np.maximum(close(code, end_date), 12)) * 100
    temp_2 = np.maximum(close(code, end_date), 12)
    alpha = (np.mean((temp_1 / temp_2) ** 2)) ** 0.5
    return alpha


def alpha_128(code, end_date=None):
    '''
    公式：
       100-(100/(1+SUM(((HIGH+LOW+CLOSE)/3>DELAY((HIGH+LOW+CLOSE)/3,1)?(HIGH+LOW+CLOSE)/3*VOLUM E:0),14)/SUM(((HIGH+LOW+CLOSE)/3<DELAY((HIGH+LOW+CLOSE)/3,1)?(HIGH+LOW+CLOSE)/3*VOLUME:0), 14)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    cond1 = ((high(code, end_date) + low(code, end_date) + close(code, end_date)) / 3) > (
                (high(code, end_date) + low(code, end_date) + close(code, end_date)) / 3).shift()
    cond2 = ((high(code, end_date) + low(code, end_date) + close(code, end_date)) / 3) < (
                (high(code, end_date) + low(code, end_date) + close(code, end_date)) / 3).shift()
    data1 = ((high(code, end_date) + low(code, end_date) + close(code, end_date)) / 3) * volume(code, end_date)
    data2 = (high(code, end_date) + low(code, end_date) + close(code, end_date) / 3) * volume(code, end_date)
    data1[~cond1] = 0
    data2[~cond2] = 0
    part_1 = pd_rolling_sum(data1, 14) / pd_rolling_sum(data2, 14)
    alpha = 100 - (100 / (1 + part_1))
    alpha = alpha.iloc[-1, :]
    return alpha


# 公式有问题，已经自己修正
def alpha_129(code, end_date=None):
    '''
    公式：
       SUM((CLOSE-DELAY(CLOSE,1)<0?ABS(CLOSE-DELAY(CLOSE,1)):0),12)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    data = close(code, end_date).diff(1)
    data[data >= 0] = 0
    data = abs(data)
    alpha = data.iloc[-12:, :].sum()
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_130(code, end_date=None):
    '''
    公式：
       (RANK(DECAYLINEAR(CORR(((HIGH    +   LOW)    /   2), MEAN(VOLUME,40),    9), 10))    /RANK(DECAYLINEAR(CORR(RANK(VWAP), RANK(VOLUME), 7),3)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_rolling_corr((high(code, end_date) + low(code, end_date)) / 2,
                             pd_rolling_mean(volume(code, end_date), 40), 9)
    part_1 = func_decaylinear(temp_1, 10)
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True)
    temp_2 = pd_rolling_corr(vwap(code, end_date).rank(axis=0, pct=True), volume(code, end_date).rank(axis=0, pct=True),
                             7)
    part_2 = func_decaylinear(temp_2, 3)
    cond2 = part_2 == 0
    part_2[cond2] = nan
    part_2 = part_2.rank(axis=1, pct=True)
    alpha = part_1 / part_2
    alpha = alpha.iloc[:, -1]
    return alpha


def alpha_131(code, end_date=None):
    '''
    公式：
       (RANK(DELAT(VWAP, 1))^TSRANK(CORR(CLOSE,MEAN(VOLUME,50), 18), 18))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = vwap(code, end_date).shift(1).rank(axis=0, pct=True)
    part_2 = func_tsrank(pd_rolling_corr(close(code, end_date), pd_rolling_mean(volume(code, end_date), 50), 18), 18)
    alpha = part_1 / part_2
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_132(code, end_date=None):
    '''
    公式：
       MEAN(AMOUNT,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = pd_rolling_mean(amount(code, end_date), 20)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_133(code, end_date=None):
    '''
    公式：
       ((20-HIGHDAY(HIGH,20))/20)*100-((20-LOWDAY(LOW,20))/20)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = ((20 - func_highday(high(code, end_date), 20)) / 20) * 100
    part_2 = ((20 - func_lowday(low(code, end_date), 20)) / 20) * 100
    alpha = part_1 - part_2
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_134(code, end_date=None):
    '''
    公式：
       (CLOSE-DELAY(CLOSE,12))/DELAY(CLOSE,12)*VOLUME
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = (close(code, end_date) - close(code, end_date).shift(12)) / close(code, end_date).shift(12) * volume(code,
                                                                                                                 end_date)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_135(code, end_date=None):
    '''
    公式：
       SMA(DELAY(CLOSE/DELAY(CLOSE,20),1),20,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = (close(code, end_date) / close(code, end_date).shift(20)).shift(1)
    alpha = pd_ewma(temp_1, span=39, adjust=False)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_136(code, end_date=None):
    '''
    公式：
       ((-1 * RANK(DELTA(RET, 3))) * CORR(OPEN, VOLUME, 10))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = -1 * (func_ret(code, end_date).shift(3).rank(axis=0, pct=True))
    part_2 = pd_rolling_corr(open(code, end_date), volume(code, end_date), 10)
    alpha = part_1 * part_2
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_137(code, end_date=None):
    '''
    公式：
       16*(CLOSE-DELAY(CLOSE,1)+(CLOSE-OPEN)/2+DELAY(CLOSE,1)-DELAY(OPEN,1))/((ABS(HIGH-DELAY(CLOSE,1))>ABS(LOW-DELAY(CLOSE,1)) &ABS(HIGH-DELAY(CLOSE,1))>ABS(HIGH-DELAY(LOW,1))?ABS(HIGH-DELAY(CLOSE,1))+ABS(LOW-DELAY(CLOS E,1))/2+ABS(DELAY(CLOSE,1)-DELAY(OPEN,1))/4:(ABS(LOW-DELAY(CLOSE,1))>ABS(HIGH-DELAY(LOW,1))    & ABS(LOW-DELAY(CLOSE,1))>ABS(HIGH-DELAY(CLOSE,1))?ABS(LOW-DELAY(CLOSE,1))+ABS(HIGH-DELAY(CLO SE,1))/2+ABS(DELAY(CLOSE,1)-DELAY(OPEN,1))/4:ABS(HIGH-DELAY(LOW,1))+ABS(DELAY(CLOSE,1)-DELAY(OP EN,1))/4)))*MAX(ABS(HIGH-DELAY(CLOSE,1)),ABS(LOW-DELAY(CLOSE,1)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = (close(code, end_date) - close(code, end_date).shift() + (
                close(code, end_date) - open(code, end_date)) / 2 + close(code, end_date).shift() - open(code,
                                                                                                         end_date).shift()) * 16
    temp_2 = abs(high(code, end_date) - close(code, end_date).shift())
    temp_3 = abs(low(code, end_date) - close(code, end_date).shift())
    temp_4 = abs(high(code, end_date) - low(code, end_date).shift())
    temp_5 = abs(close(code, end_date).shift() - open(code, end_date).shift())
    cond1 = (temp_1 / temp_2) > temp_3
    cond2 = temp_2 > temp_4
    cond3 = temp_3 > temp_4
    cond4 = temp_3 > temp_2
    data1 = pd.DataFrame(np.ones(close(code, end_date).shape), index=close(code, end_date).index,
                         columns=close(code, end_date).columns)
    data1[cond1 & cond2] = (temp_2 + temp_3) / 2 + abs(close(code, end_date).shift() - open(code, end_date).shift()) / 4
    data1[~(cond1 & cond2)][cond3 & cond4] = (temp_3 + temp_2) / 2 + temp_5 / 4
    data1[~(cond1 & cond2)][~(cond3 & cond4)] = temp_4 + temp_5 / 4
    data2 = np.maximum(temp_2, temp_3)
    alpha = data1 * data2
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_138(code, end_date=None):
    '''
    公式：
       ((RANK(DECAYLINEAR(DELTA((((LOW  *   0.7)    +   (VWAP   *0.3))),    3), 20))    -TSRANK(DECAYLINEAR(TSRANK(CORR(TSRANK(LOW, 8), TSRANK(MEAN(VOLUME,60), 17), 5), 19), 16), 7)) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = (low(code, end_date) * 0.7 + vwap(code, end_date) * 0.3).diff(3)
    part_1 = func_decaylinear(temp_1, 20).rank(axis=1, pct=True)
    temp_2 = pd_rolling_corr(func_tsrank(low(code, end_date), 8),
                             func_tsrank(pd_rolling_mean(volume(code, end_date), 60), 17), 5)
    part_2 = func_tsrank(func_decaylinear(func_tsrank(temp_2, 19), 16), 7)
    alpha = (part_1 - part_2) * -1
    alpha = alpha.iloc[:, -1]
    return alpha


def alpha_139(code, end_date=None):
    '''
    公式：
       (-1 * CORR(OPEN, VOLUME, 10))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = -1 * pd_rolling_corr(open(code, end_date), volume(code, end_date), 10)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_140(code, end_date=None):
    '''
    公式：
       MIN(RANK(DECAYLINEAR(((RANK(OPEN)    +   RANK(LOW)) -  (RANK(HIGH) +   RANK(CLOSE))),  8)), TSRANK(DECAYLINEAR(CORR(TSRANK(CLOSE, 8), TSRANK(MEAN(VOLUME,60), 20), 8), 7), 3))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = (open(code, end_date).rank(pct=True) + low(code, end_date).rank(pct=True) - high(code, end_date).rank(
        pct=True) + close(code, end_date).rank(pct=True))
    part_1 = func_decaylinear(temp_1, 8)
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True).T
    temp_2 = pd_rolling_corr(func_tsrank(close(code, end_date), 8),
                             func_tsrank(pd_rolling_mean(volume(code, end_date), 60), 20), 8)
    temp_2 = func_decaylinear(temp_2, 7).T
    cond2 = temp_2 == 0
    temp_2[cond2] = nan
    part_2 = func_tsrank(temp_2, 3)
    alpha = np.minimum(part_1.iloc[-1, :], part_2.iloc[-1, :])
    return alpha


def alpha_141(code, end_date=None):
    '''
    公式：
       (RANK(CORR(RANK(HIGH), RANK(MEAN(VOLUME,15)), 9))* -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = pd_rolling_corr(high(code, end_date).rank(pct=True),
                            pd_rolling_mean(volume(code, end_date), 15).rank(pct=True), 9).rank(pct=True) * -1
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_142(code, end_date=None):
    '''
    公式：
       (((-1   *   RANK(TSRANK(CLOSE,   10)))   *   RANK(DELTA(DELTA(CLOSE,   1),   1)))   *    RANK(TSRANK((VOLUME/MEAN(VOLUME,20)), 5)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = func_tsrank(close(code, end_date), 10).rank(pct=True) * -1
    part_2 = close(code, end_date).diff().diff().rank(pct=True)
    part_3 = func_tsrank(volume(code, end_date) / pd_rolling_mean(volume(code, end_date), 20), 5).rank(pct=True)
    alpha = part_1 * part_2 * part_3
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_143(code, end_date=None):
    '''
    公式：
       CLOSE>DELAY(CLOSE,1)?(CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)*SELF:SELF
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    # 公式不明
    # 出现了self 不明白意义
    return nan


def alpha_144(code, end_date=None):
    '''
    公式：
       SUMIF(ABS(CLOSE/DELAY(CLOSE,1)-1)/AMOUNT,20,CLOSE<DELAY(CLOSE,1))/COUNT(CLOSE<DELAY(CLOSE, 1),20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    df1 = close(code, end_date) < close(code, end_date).shift()
    sumif = ((abs(close(code, end_date) / close(code, end_date).shift() - 1) / amount(code, end_date)) * df1).iloc[-20:,
            :].sum()
    count = df1.iloc[-20:, :].sum()
    alpha = (sumif / count)
    return alpha


def alpha_145(code, end_date=None):
    '''
    公式：
       (MEAN(VOLUME,9)-MEAN(VOLUME,26))/MEAN(VOLUME,12)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = pd_rolling_mean(volume(code, end_date), 9) - pd_rolling_mean(volume(code, end_date), 26) / pd_rolling_mean(
        volume(code, end_date), 12) * 100
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_146(code, end_date=None):
    '''
    公式：
       MEAN((CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)-SMA((CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1),61,2),20)*(( CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)-SMA((CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1),61,2))/SMA(((CLOS E-DELAY(CLOSE,1))/DELAY(CLOSE,1)-((CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)-SMA((CLOSE-DELAY(CLOSE, 1))/DELAY(CLOSE,1),61,2)))^2,60);
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = (close(code, end_date) - close(code, end_date).shift()) / close(code, end_date).shift()
    part_1 = pd_rolling_mean(temp_1 - pd_ewma(temp_1, span=60, adjust=False), 20)
    part_2 = pd_ewma(temp_1, span=60, adjust=False) / pd_ewma((pd_ewma(temp_1, span=60, adjust=False) ** 2), span=60,
                                                              adjust=False)
    alpha = part_1.iloc[-1, :] * part_2.iloc[-1, :]
    return alpha


def alpha_147(code, end_date=None):
    '''
    公式：
       REGBETA(MEAN(CLOSE,12),SEQUENCE(12))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    sequence = pd.Series(range(1, 13), index=close(code, end_date).iloc[-12:, ].index)
    corr = close(code, end_date).iloc[-12:, :].corrwith(sequence)
    alpha = corr
    return alpha


def alpha_148(code, end_date=None):
    '''
    公式：
       ((RANK(CORR((OPEN), SUM(MEAN(VOLUME,60), 9), 6)) < RANK((OPEN-TSMIN(OPEN, 14)))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = pd_rolling_corr(open(code, end_date), pd_rolling_sum(pd_rolling_mean(volume(code, end_date), 60), 9),
                             6).rank(pct=True)
    part_2 = (open(code, end_date) - pd_rolling_min(open(code, end_date), 14)).rank(pct=True)
    alpha = part_1 - part_2
    alpha = alpha.iloc[-1, :]
    cond1 = alpha < 0
    cond2 = alpha > 0
    alpha[cond1] = -1
    alpha[cond2] = 1
    return alpha


def alpha_149(code, benchmark='000300.XSHG', end_date=None):
    '''
    公式：
       REGBETA(FILTER(CLOSE/DELAY(CLOSE,1)-1,BANCHMARKINDEXCLOSE<DELAY(BANCHMARKINDEXCLOSE,1)),FILTER(BANCHMARKINDEXCLOSE/DELAY(BANCHMARKINDEXCLOSE,1)-1,BANCHMARKINDEXCLOSE<DELA Y(BANCHMARKINDEXCLOSE,1)),252)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp1 = close(code, end_date) / close(code, end_date).shift() - 1
    cond1 = benchmark_index_close(code, benchmark, end_date) < benchmark_index_close(code, benchmark, end_date).shift()
    part1 = temp1[cond1]

    temp2 = benchmark_index_close(code, benchmark, end_date) / benchmark_index_close(code, benchmark,
                                                                                     end_date).shift() - 1
    cond2 = benchmark_index_close(code, benchmark, end_date) < benchmark_index_close(code, benchmark, end_date).shift()
    part2 = temp2[cond2]
    output = pd.Series()
    for stock in code:
        temp_1 = part1[stock].fillna(0)
        temp_2 = part2[stock].fillna(0)
        date = min(len(temp_1), len(temp_2), 252)
        linreg = LinearRegression()
        model = linreg.fit(temp_1[-date:].values.reshape(date, 1), temp_2[-date:].values.reshape(date, 1))
        output[stock] = float(model.coef_)
    cond1 = output == 0
    output[cond1] = nan
    return output


def alpha_150(code, end_date=None):
    '''
    公式：
       (CLOSE+HIGH+LOW)/3*VOLUME
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = (high(code, end_date) + close(code, end_date) + low(code, end_date)) / 3 * volume(code, end_date)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_151(code, end_date=None):
    '''
    公式：
       SMA(CLOSE-DELAY(CLOSE,20),20,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = pd_ewma(close(code, end_date) - close(code, end_date).shift(20), span=39, adjust=False)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_152(code, end_date=None):
    '''
    公式：
       SMA(MEAN(DELAY(SMA(DELAY(CLOSE/DELAY(CLOSE,9),1),9,1),1),12)-MEAN(DELAY(SMA(DELAY(CLOSE/DELAY (CLOSE,9),1),9,1),1),26),9,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_ewma((close(code, end_date) / close(code, end_date).shift(9)).shift(), span=17, adjust=False)
    part_1 = pd_rolling_mean(temp_1, 12)
    part_2 = pd_rolling_mean(temp_1, 26)
    alpha = pd_ewma(part_1 - part_2, span=17)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_153(code, end_date=None):
    '''
    公式：
       (MEAN(CLOSE,3)+MEAN(CLOSE,6)+MEAN(CLOSE,12)+MEAN(CLOSE,24))/4
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = pd_rolling_mean(close(code, end_date), 3)
    part_2 = pd_rolling_mean(close(code, end_date), 6)
    part_3 = pd_rolling_mean(close(code, end_date), 12)
    part_4 = pd_rolling_mean(close(code, end_date), 24)
    alpha = (part_1 + part_2 + part_3 + part_4) / 4
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_154(code, end_date=None):
    '''
    公式：
       (((VWAP-MIN(VWAP, 16))) < (CORR(VWAP, MEAN(VOLUME,180), 18)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = vwap(code, end_date) - np.minimum(vwap(code, end_date), 16)
    part_2 = pd_rolling_corr(vwap(code, end_date), pd_rolling_mean(volume(code, end_date), 180), 18)
    alpha = part_1 - part_2
    alpha = alpha.iloc[-1, :]
    cond1 = alpha < 0
    cond2 = alpha > 0
    alpha[cond1] = 1
    alpha[cond2] = -1
    return alpha


def alpha_155(code, end_date=None):
    '''
    公式：
       SMA(VOLUME,13,2)-SMA(VOLUME,27,2)-SMA(SMA(VOLUME,13,2)-SMA(VOLUME,27,2),10,2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = pd_ewma(volume(code, end_date), span=12)
    part_2 = pd_ewma(volume(code, end_date), span=26)
    part_3 = pd_ewma(part_1 - part_2, span=9)
    alpha = part_1 - part_2 - part_3
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_156(code, end_date=None):
    '''
    公式：
       (MAX(RANK(DECAYLINEAR(DELTA(VWAP, 5), 3)), RANK(DECAYLINEAR(((DELTA(((OPEN * 0.15) + (LOW   *0.85)),2) / ((OPEN * 0.15) + (LOW * 0.85))) * -1), 3))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = func_decaylinear(vwap(code, end_date).diff(5), 3)
    cond1 = part_1 == 0
    part_1[cond1] = nan
    part_1 = part_1.rank(axis=1, pct=True)
    temp_1 = (open(code, end_date) * 0.15 + low(code, end_date) * 0.85).diff(2) / (
                open(code, end_date) * 0.15 + low(code, end_date) * 0.85)
    part_2 = func_decaylinear(temp_1, 3)
    cond2 = part_2 == 0
    part_2[cond2] = nan
    part_2 = part_2.rank(axis=1, pct=True)
    alpha = np.maximum(part_1, part_2) * -1
    alpha = alpha.iloc[:, -1]
    return alpha


def alpha_157(code, end_date=None):
    '''
    公式：
       (MIN(PROD(RANK(RANK(LOG(SUM(TSMIN(RANK(RANK((-1 * RANK(DELTA((CLOSE   -1), 5))))), 2), 1)))), 1), 5) +TSRANK(DELAY((-1 * RET), 6), 5))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = ((close(code, end_date) - 1).diff(5).rank(axis=0, pct=True) * -1).rank(pct=True).rank(pct=True)
    temp_2 = pd_rolling_sum(pd_rolling_min(temp_1, 2), 1)
    temp_3 = np.log(temp_2).rank(axis=0, pct=True).rank(axis=0, pct=True)
    part_1 = np.minimum(temp_3, 5)
    part_2 = func_tsrank((func_ret(code, end_date) * -1).shift(6), 5)
    alpha = part_1 + part_2
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_158(code, end_date=None):
    '''
    公式：
       ((HIGH-SMA(CLOSE,15,2))-(LOW-SMA(CLOSE,15,2)))/CLOSE
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = high(code, end_date) - pd_ewma(close(code, end_date), span=14)
    temp_2 = low(code, end_date) - pd_ewma(close(code, end_date), span=14)
    alpha = (temp_1 - temp_2) / close(code, end_date)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_159(code, end_date=None):
    '''
    公式：
       ((CLOSE-SUM(MIN(LOW,DELAY(CLOSE,1)),6))/SUM(MAX(HGIH,DELAY(CLOSE,1))-MIN(LOW,DELAY(CLOSE,1)),6)*12*24+(CLOSE-SUM(MIN(LOW,DELAY(CLOSE,1)),12))/SUM(MAX(HGIH,DELAY(CLOSE,1))-MIN(LOW,DELAY(CL OSE,1)),12)*6*24+(CLOSE-SUM(MIN(LOW,DELAY(CLOSE,1)),24))/SUM(MAX(HGIH,DELAY(CLOSE,1))-MIN(LOW,D ELAY(CLOSE,1)),24)*6*24)*100/(6*12+6*24+12*24)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    data1 = low(code, end_date)
    data2 = close(code, end_date).shift()
    cond = data1 > data2
    data1[cond] = data2
    data3 = high(code, end_date)
    data4 = close(code, end_date).shift()
    cond = data3 > data4
    data3[~cond] = data4
    x = ((close(code, end_date) - pd_rolling_sum(data1, 6)) / pd_rolling_sum((data2 - data1), 6)) * 12 * 24
    y = ((close(code, end_date) - pd_rolling_sum(data1, 12)) / pd_rolling_sum((data2 - data1), 12)) * 6 * 24
    z = ((close(code, end_date) - pd_rolling_sum(data1, 24)) / pd_rolling_sum((data2 - data1), 24)) * 6 * 24
    data5 = (x + y + z) * (100 / (6 * 12 + 12 * 24 + 6 * 24))
    alpha = data5.iloc[-1, :]
    return alpha


def alpha_160(code, end_date=None):
    '''
    公式：
       SMA((CLOSE<=DELAY(CLOSE,1)?STD(CLOSE,20):0),20,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    cond1 = close(code, end_date) <= close(code, end_date).shift()
    data1 = pd_rolling_std(close(code, end_date), 20)
    data1[~cond1] = 0
    alpha = pd_ewma(data1, span=39)
    alpha = alpha.iloc[-1, :]
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_161(code, end_date=None):
    '''
    公式：
       MEAN(MAX(MAX((HIGH-LOW),ABS(DELAY(CLOSE,1)-HIGH)),ABS(DELAY(CLOSE,1)-LOW)),12)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = high(code, end_date) - low(code, end_date)
    temp_2 = abs(close(code, end_date).shift() - high(code, end_date))
    temp_3 = np.maximum(temp_1, temp_2)
    temp_4 = abs(close(code, end_date).shift() - low(code, end_date))
    temp_5 = np.maximum(temp_3, temp_4)
    alpha = pd_rolling_mean(temp_5, 12)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_162(code, end_date=None):
    '''
    公式：
       (SMA(MAX(CLOSE-DELAY(CLOSE,1),0),12,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100-MIN(SMA(MAX(CLOS E-DELAY(CLOSE,1),0),12,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100,12))/(MAX(SMA(MAX(CLOSE-DELAY(C LOSE,1),0),12,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100,12)-MIN(SMA(MAX(CLOSE-DELAY(CLOSE,1),0),12, 1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100,12))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    data1 = close(code, end_date) - close(code, end_date).shift()
    cond = data1 > 0
    data1[~cond] = 0
    x = pd_ewma(data1, span=23)
    data2 = abs(close(code, end_date) - close(code, end_date).shift())
    y = pd_ewma(data2, span=23)
    z = (x / y) * 100
    cond = z > 12
    z[cond] = 12
    c = (x / y) * 100
    cond = c > 12
    c[~cond] = 12
    data3 = (x / y) * 100 - (z / c) - c
    alpha = data3.iloc[-1, :]
    return alpha


def alpha_163(code, end_date=None):
    '''
    公式：
       RANK(((((-1 * RET) * MEAN(VOLUME,20)) * VWAP) * (HIGH-CLOSE)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = -1 * func_ret(code, end_date) * pd_rolling_mean(volume(code, end_date), 20) * vwap(code, end_date) * (
                high(code, end_date) - low(code, end_date))
    alpha = alpha.rank(pct=True)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_164(code, end_date=None):
    '''
    公式：
       SMA((((CLOSE>DELAY(CLOSE,1))?1/(CLOSE-DELAY(CLOSE,1)):1)-MIN(((CLOSE>DELAY(CLOSE,1))?1/(CLOSE-D ELAY(CLOSE,1)):1),12))/(HIGH-LOW)*100,13,2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    cond1 = close(code, end_date) > close(code, end_date).shift()
    data1 = 1 / (close(code, end_date) - close(code, end_date).shift())
    data1[~cond1] = 1
    data2 = np.minimum(data1, 12)
    alpha = pd_ewma((data1 - data2) / (high(code, end_date) - low(code, end_date)) * 100, span=12)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_165(code, end_date=None):
    '''
    公式：
       MAX(SUMAC(CLOSE-MEAN(CLOSE,48)))-MIN(SUMAC(CLOSE-MEAN(CLOSE,48)))/STD(CLOSE,48)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    # 公式有误
    # 问题1 sumac是计算前n项的累加，然而没有写n
    # 问题2 max里面只有一个参数，无法比较
    return nan


def alpha_166(code, end_date=None):
    '''
    公式：
       -20* （   20-1    ）^1.5*SUM(CLOSE/DELAY(CLOSE,1)-1-MEAN(CLOSE/DELAY(CLOSE,1)-1,20),20)/((20-1)*(20-2)(SUM((CLOSE/DELA Y(CLOSE,1),20)^2,20))^1.5)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part1 = -20 * (19) ** 1.5
    temp = close(code, end_date) / close(code, end_date).shift()
    part2 = pd_rolling_sum(temp - 1 - pd_rolling_mean(temp - 1, 20), 20)
    part3 = 19 * 18 * (pd_rolling_sum(temp, 20)) ** (1.5)
    alpha = part1 * part2 / part3
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_167(code, end_date=None):
    '''
    公式：
       SUM((CLOSE-DELAY(CLOSE,1)>0?CLOSE-DELAY(CLOSE,1):0),12)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    cond1 = (close(code, end_date) - close(code, end_date).shift()) > 0
    data1 = close(code, end_date) - close(code, end_date).shift()
    data1[~cond1] = 0
    alpha = pd_rolling_sum(data1, 12)
    alpha = alpha.iloc[-1, :]
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_168(code, end_date=None):
    '''
    公式：
       (-1*VOLUME/MEAN(VOLUME,20))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = -volume(code, end_date) / pd_rolling_mean(volume(code, end_date), 20)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_169(code, end_date=None):
    '''
    公式：
       SMA(MEAN(DELAY(SMA(CLOSE-DELAY(CLOSE,1),9,1),1),12)-MEAN(DELAY(SMA(CLOSE-DELAY(CLOSE,1),9,1),1), 26),10,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_ewma(close(code, end_date) - close(code, end_date).shift(), span=17).shift()
    alpha = pd_ewma((pd_rolling_mean(temp_1, 12) - pd_rolling_mean(temp_1, 26)), span=19)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_170(code, end_date=None):
    '''
    公式：
       ((((RANK((1 / CLOSE)) * VOLUME) / MEAN(VOLUME,20)) * ((HIGH * RANK((HIGH-CLOSE))) / (SUM(HIGH, 5) / 5)))-RANK((VWAP-DELAY(VWAP, 5))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = ((1 / close(code, end_date)).rank(axis=0, pct=True)) * volume(code, end_date) / pd_rolling_mean(
        volume(code, end_date), 20)
    part_2 = (high(code, end_date) - close(code, end_date)).rank(pct=True) * high(code, end_date)
    part_3 = pd_rolling_sum(high(code, end_date), 5) / 5
    part_4 = (vwap(code, end_date) - vwap(code, end_date).shift(5)).rank(pct=True)
    alpha = part_1 * part_2 / part_3 - part_4
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_171(code, end_date=None):
    '''
    公式：
       ((-1 * ((LOW-CLOSE) * (OPEN^5))) / ((CLOSE-HIGH) * (CLOSE^5)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = (low(code, end_date) - close(code, end_date)) * (open(code, end_date) ** 5) * -1
    part_2 = (close(code, end_date) - high(code, end_date)) * close(code, end_date) ** 5
    alpha = part_1 / part_2
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_172(code, end_date=None):
    '''
    公式：
       MEAN(ABS(SUM((LD>0   &   LD>HD)?LD:0,14)*100/SUM(TR,14)-SUM((HD>0    & HD>LD)?HD:0,14)*100/SUM(TR,14))/(SUM((LD>0 & LD>HD)?LD:0,14)*100/SUM(TR,14)+SUM((HD>0 & HD>LD)?HD:0,14)*100/SUM(TR,14))*100,6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    hd = high(code, end_date) - high(code, end_date).shift()
    ld = low(code, end_date).shift() - low(code, end_date)
    temp1 = high(code, end_date) - low(code, end_date)
    temp2 = (high(code, end_date) - close(code, end_date).shift()).abs()
    cond1 = temp1 > temp2
    temp2[cond1] = temp1[cond1]
    temp3 = (low(code, end_date) - close(code, end_date).shift()).abs()
    cond2 = temp2 > temp3
    temp3[cond2] = temp2[cond2]
    tr = temp3
    sum_tr14 = pd_rolling_sum(tr, 14)
    cond3 = ld > 0
    cond4 = ld > hd
    cond3[~cond4] = False
    data1 = ld
    data1[~cond3] = 0
    sum1 = pd_rolling_sum(data1, 14) * 100 / sum_tr14
    cond5 = hd > 0
    cond6 = hd > ld
    cond5[~cond6] = False
    data2 = hd
    data2[~cond5] = 0
    sum2 = pd_rolling_sum(data2, 14) * 100 / sum_tr14
    alpha = pd_rolling_mean((sum1 - sum2).abs() / (sum1 + sum2) * 100, 6).iloc[-1, :]
    return alpha


def alpha_173(code, end_date=None):
    '''
    公式：
       3*SMA(CLOSE,13,2)-2*SMA(SMA(CLOSE,13,2),13,2)+SMA(SMA(SMA(LOG(CLOSE),13,2),13,2),13,2);
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_ewma(close(code, end_date), span=12)
    part_1 = temp_1 * 3
    part_2 = pd_ewma(temp_1, span=12) * 2
    part_3 = pd_ewma(pd_ewma(pd_ewma(np.log(close(code, end_date)), span=12), span=12), span=12)
    alpha = part_1 - part_2 + part_3
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_174(code, end_date=None):
    '''
    公式：
       SMA((CLOSE>DELAY(CLOSE,1)?STD(CLOSE,20):0),20,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    cond1 = close(code, end_date) < close(code, end_date).shift()
    data1 = pd_rolling_std(close(code, end_date), 20)
    data1[cond1] = 0
    alpha = pd_ewma(data1, span=39)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_175(code, end_date=None):
    '''
    公式：
       MEAN(MAX(MAX((HIGH-LOW),ABS(DELAY(CLOSE,1)-HIGH)),ABS(DELAY(CLOSE,1)-LOW)),6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = np.maximum((high(code, end_date) - low(code, end_date)),
                        abs(close(code, end_date).shift() - high(code, end_date)))
    temp_2 = np.maximum(temp_1, abs(close(code, end_date).shift() - low(code, end_date)))
    alpha = pd_rolling_mean(temp_2, 6)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_176(code, end_date=None):
    '''
    公式：
       CORR(RANK(((CLOSE-TSMIN(LOW, 12)) / (TSMAX(HIGH, 12)-TSMIN(LOW,12)))), RANK(VOLUME), 6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = (close(code, end_date) - pd_rolling_min(low(code, end_date), 12)) / (
                pd_rolling_max(high(code, end_date), 12) - pd_rolling_min(low(code, end_date), 12))
    alpha = pd_rolling_corr(part_1.rank(pct=True), volume(code, end_date).rank(pct=True), 6)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_177(code, end_date=None):
    '''
    公式：
       ((20-HIGHDAY(HIGH,20))/20)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = (20 - func_highday(high(code, end_date), 20)) / 20 * 100
    cond1 = alpha == 0
    alpha[cond1] = nan
    return alpha


def alpha_178(code, end_date=None):
    '''
    公式：
       (CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)*VOLUME
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = (close(code, end_date) - close(code, end_date).shift()) / close(code, end_date).shift() * volume(code,
                                                                                                             end_date)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_179(code, end_date=None):
    '''
    公式：
       (RANK(CORR(VWAP, VOLUME, 4)) *RANK(CORR(RANK(LOW), RANK(MEAN(VOLUME,50)), 12)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = pd_rolling_corr(vwap(code, end_date), volume(code, end_date), 4).rank(pct=True)
    temp_2 = pd_rolling_corr(low(code, end_date).rank(pct=True),
                             pd_rolling_mean(volume(code, end_date), 60).rank(pct=True), 12).rank(pct=True)
    alpha = temp_1 * temp_2
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_180(code, end_date=None):
    '''
    公式：
       ((MEAN(VOLUME,20) < VOLUME) ? ((-1 * TSRANK(ABS(DELTA(CLOSE, 7)), 60)) * SIGN(DELTA(CLOSE, 7)) : (-1 *VOLUME)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    ma = pd_rolling_mean(volume(code, end_date), 20)
    cond = (ma < volume(code, end_date)).iloc[-20:, :]
    sign = delta_close_7 = close(code, end_date).diff(7)
    sign[sign.iloc[:, :] < 0] = -1
    sign[sign.iloc[:, :] > 0] = 1
    sign[sign.iloc[:, :] == 0] = 0
    left = (((close(code, end_date).diff(7).abs()).iloc[-60:, :].rank(axis=0, pct=True) * (-1)).iloc[-20:,
            :] * sign.iloc[-20:, :]).iloc[-20:, :]
    right = volume(code, end_date).iloc[-20:, :] * (-1)
    right[cond] = left[cond]
    alpha = right.iloc[-1, :]
    return alpha


# 公式不符合逻辑，已经补足
def alpha_181(code, benchmark='000300.XSHG', end_date=None):
    '''
    公式：
       SUM(((CLOSE/DELAY(CLOSE,1)-1)-MEAN((CLOSE/DELAY(CLOSE,1)-1),20))-(BANCHMARKINDEXCLOSE-MEAN(B ANCHMARKINDEXCLOSE,20))^2,20)/SUM((BANCHMARKINDEXCLOSE-MEAN(BANCHMARKINDEXCLOSE,20))^3)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp_1 = close(code, end_date) / close(code, end_date).shift()
    temp_2 = benchmark_index_close(code, benchmark, end_date) - pd_rolling_mean(
        benchmark_index_close(code, benchmark, end_date), 20)
    part_1 = pd_rolling_sum((temp_1 - pd_rolling_mean(temp_1, 20) - temp_2) ** 2, 20)
    part_2 = pd_rolling_sum(temp_2 ** 3, 20)
    alpha = part_1 / part_2
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_182(code, benchmark='000300.XSHG', end_date=None):
    '''
    公式：
       COUNT((CLOSE>OPEN    &   BANCHMARKINDEXCLOSE>BANCHMARKINDEXOPEN)OR(CLOSE<OPEN    & BANCHMARKINDEXCLOSE<BANCHMARKINDEXOPEN),20)/20
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    cond1 = close(code, end_date) > open(code, end_date)
    cond2 = benchmark_index_close(code, benchmark, end_date) > benchmark_index_open(code, benchmark, end_date)
    cond3 = close(code, end_date) < open(code, end_date)
    cond4 = benchmark_index_close(code, benchmark, end_date) < benchmark_index_open(code, benchmark, end_date)
    cond5 = (cond1 & cond2) | (cond3 & cond4)
    data1 = close(code, end_date)
    data1[cond5] = 1
    data1[cond5] = 0
    alpha = pd_rolling_sum(data1, 20) / 20
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_183(code, end_date=None):
    '''
    公式：
       MAX(SUMAC(CLOSE-MEAN(CLOSE,24)))-MIN(SUMAC(CLOSE-MEAN(CLOSE,24)))/STD(CLOSE,24)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    # 公式错误
    # 问题1 sumac是计算前n项的累加，然而没有写n
    # 问题2 max里面只有一个参数，无法比较
    return nan


def alpha_184(code, end_date=None):
    '''
    公式：
       (RANK(CORR(DELAY((OPEN-CLOSE), 1), CLOSE, 200)) + RANK((OPEN-CLOSE)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    part_1 = pd_rolling_corr((open(code, end_date) - close(code, end_date)).shift(), close(code, end_date), 200).rank(
        pct=True)
    part_2 = (open(code, end_date) - close(code, end_date)).rank(pct=True)
    alpha = (part_1 + part_2).iloc[-1, :]
    return alpha


def alpha_185(code, end_date=None):
    '''
    公式：
       RANK((-1 * ((1-(OPEN / CLOSE))^2)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = ((1 - (open(code, end_date) / close(code, end_date)) ** 2) * -1).rank(pct=True)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_186(code, end_date=None):
    '''
    公式：
       (MEAN(ABS(SUM((LD>0  &   LD>HD)?LD:0,14)*100/SUM(TR,14)-SUM((HD>0    & HD>LD)?HD:0,14)*100/SUM(TR,14))/(SUM((LD>0 & LD>HD)?LD:0,14)*100/SUM(TR,14)+SUM((HD>0 & HD>LD)?HD:0,14)*100/SUM(TR,14))*100,6)+DELAY(MEAN(ABS(SUM((LD>0   & LD>HD)?LD:0,14)*100/SUM(TR,14)-SUM((HD>0 & HD>LD)?HD:0,14)*100/SUM(TR,14))/(SUM((LD>0 & LD>HD)?LD:0,14)*100/SUM(TR,14)+SUM((HD>0 & HD>LD)?HD:0,14)*100/SUM(TR,14))*100,6),6))/2
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    hd = high(code, end_date) - high(code, end_date).shift()
    ld = low(code, end_date).shift() - low(code, end_date)
    temp1 = high(code, end_date) - low(code, end_date)
    temp2 = (high(code, end_date) - close(code, end_date).shift()).abs()
    cond1 = temp1 > temp2
    temp2[cond1] = temp1[cond1]
    temp3 = (low(code, end_date) - close(code, end_date).shift()).abs()
    cond2 = temp2 > temp3
    temp3[cond2] = temp2[cond2]
    tr = temp3
    sum_tr14 = pd_rolling_sum(tr, 14)
    cond3 = ld > 0
    cond4 = ld > hd
    cond3[~cond4] = False
    data1 = ld
    data1[~cond3] = 0
    sum1 = pd_rolling_sum(data1, 14) * 100 / sum_tr14
    cond5 = hd > 0
    cond6 = hd > ld
    cond5[~cond6] = False
    data2 = hd
    data2[~cond5] = 0
    sum2 = pd_rolling_sum(data2, 14) * 100 / sum_tr14
    mean1 = pd_rolling_mean((sum1 - sum2).abs() / (sum1 + sum2) * 100, 6)
    alpha = ((mean1 + mean1.shift(6)) / 2).iloc[-1, :]
    return alpha


def alpha_187(code, end_date=None):
    '''
    公式：
       SUM((OPEN<=DELAY(OPEN,1)?0:MAX((HIGH-OPEN),(OPEN-DELAY(OPEN,1)))),20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    cond1 = open(code, end_date) <= open(code, end_date).shift()
    data1 = np.maximum(high(code, end_date) - open(code, end_date),
                       (open(code, end_date) - open(code, end_date).shift()))
    data1[cond1] = 0
    alpha = pd_rolling_sum(data1, 20).iloc[-1, :]
    return alpha


def alpha_188(code, end_date=None):
    '''
    公式：
       ((HIGH-LOW–SMA(HIGH-LOW,11,2))/SMA(HIGH-LOW,11,2))*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    temp = high(code, end_date) - low(code, end_date)
    part_1 = temp - pd_ewma(temp, span=10)
    alpha = part_1 / pd_ewma(temp, span=10) * 100
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_189(code, end_date=None):
    '''
    公式：
       MEAN(ABS(CLOSE-MEAN(CLOSE,6)),6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = pd_rolling_mean(abs(close(code, end_date) - pd_rolling_mean(close(code, end_date), 6)), 6)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha_190(code, end_date=None):
    '''
    公式：
       LOG((COUNT(CLOSE/DELAY(CLOSE)-1>((CLOSE/DELAY(CLOSE,19))^(1/20)-1),20)-1)*(SUMIF(((CLOSE/DELAY(C LOSE)-1-(CLOSE/DELAY(CLOSE,19))^(1/20)-1))^2,20,CLOSE/DELAY(CLOSE)-1<(CLOSE/DELAY(CLOSE,19))^(1/20)- 1))/((COUNT((CLOSE/DELAY(CLOSE)-1<(CLOSE/DELAY(CLOSE,19))^(1/20)-1),20))*(SUMIF((CLOSE/DELAY(CLOS E)-1-((CLOSE/DELAY(CLOSE,19))^(1/20)-1))^2,20,CLOSE/DELAY(CLOSE)-1>(CLOSE/DELAY(CLOSE,19))^(1/20)-1))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    # 问题 delay没有写滞后几阶，我默认按1阶处理了
    if isinstance(code, six.string_types):
        code = [code]
    temp1 = close(code, end_date) / close(code, end_date).shift() - 1
    temp2 = (close(code, end_date) / close(code, end_date).shift(19)) ** (1 / 20) - 1
    part1 = (pd_rolling_sum(temp1 > temp2, 20) - 1).iloc[-1, :]

    temp3 = (temp1 - temp2) ** 2
    cond1 = temp1 < temp2
    temp3[~cond1] = 0
    part2 = pd_rolling_sum(temp3, 20).iloc[-1, :]

    part3 = pd_rolling_sum(cond1, 20).iloc[-1, :]
    cond2 = temp1 > temp2
    temp4 = (temp1 - temp2) ** 2
    temp4[~cond2] = 0
    part4 = pd_rolling_sum(temp4, 20).iloc[-1, :]

    alpha = np.log(part1 * part2 / (part3 * part4))
    return alpha


def alpha_191(code, end_date=None):
    '''
    公式：
       ((CORR(MEAN(VOLUME,20),LOW,5)+((HIGH+LOW)/2))-CLOSE)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    '''
    # 修复传入为单只股票的情况
    if isinstance(code, six.string_types):
        code = [code]
    alpha = pd_rolling_corr(pd_rolling_mean(volume(code, end_date), 20), low(code, end_date), 5) + (
                high(code, end_date) + low(code, end_date)) / 2 - close(code, end_date)
    alpha = alpha.iloc[-1, :]
    return alpha


def alpha(code, benchmark='000300.XSHG', end_date=None):
    alpha = pd.DataFrame(alpha_001(code, end_date), columns=['alpha_001'])
    alpha['alpha_002'] = alpha_002(code, end_date)
    alpha['alpha_003'] = alpha_003(code, end_date)
    alpha['alpha_004'] = alpha_004(code, end_date)
    alpha['alpha_005'] = alpha_005(code, end_date)
    alpha['alpha_006'] = alpha_006(code, end_date)
    alpha['alpha_007'] = alpha_007(code, end_date)
    alpha['alpha_008'] = alpha_008(code, end_date)
    alpha['alpha_009'] = alpha_009(code, end_date)
    alpha['alpha_010'] = alpha_010(code, end_date)
    alpha['alpha_011'] = alpha_011(code, end_date)
    alpha['alpha_012'] = alpha_012(code, end_date)
    alpha['alpha_013'] = alpha_013(code, end_date)
    alpha['alpha_014'] = alpha_014(code, end_date)
    alpha['alpha_015'] = alpha_015(code, end_date)
    alpha['alpha_016'] = alpha_016(code, end_date)
    alpha['alpha_017'] = alpha_017(code, end_date)
    alpha['alpha_018'] = alpha_018(code, end_date)
    alpha['alpha_019'] = alpha_019(code, end_date)
    alpha['alpha_020'] = alpha_020(code, end_date)
    alpha['alpha_021'] = alpha_021(code, end_date)
    alpha['alpha_022'] = alpha_022(code, end_date)
    alpha['alpha_023'] = alpha_023(code, end_date)
    alpha['alpha_024'] = alpha_024(code, end_date)
    alpha['alpha_025'] = alpha_025(code, end_date)
    alpha['alpha_026'] = alpha_026(code, end_date)
    alpha['alpha_027'] = alpha_027(code, end_date)
    alpha['alpha_028'] = alpha_028(code, end_date)
    alpha['alpha_029'] = alpha_029(code, end_date)
    alpha['alpha_030'] = alpha_030(code, end_date)
    alpha['alpha_031'] = alpha_031(code, end_date)
    alpha['alpha_032'] = alpha_032(code, end_date)
    alpha['alpha_033'] = alpha_033(code, end_date)
    alpha['alpha_034'] = alpha_034(code, end_date)
    alpha['alpha_035'] = alpha_035(code, end_date)
    alpha['alpha_036'] = alpha_036(code, end_date)
    alpha['alpha_037'] = alpha_037(code, end_date)
    alpha['alpha_038'] = alpha_038(code, end_date)
    alpha['alpha_039'] = alpha_039(code, end_date)
    alpha['alpha_040'] = alpha_040(code, end_date)
    alpha['alpha_041'] = alpha_041(code, end_date)
    alpha['alpha_042'] = alpha_042(code, end_date)
    alpha['alpha_043'] = alpha_043(code, end_date)
    alpha['alpha_044'] = alpha_044(code, end_date)
    alpha['alpha_045'] = alpha_045(code, end_date)
    alpha['alpha_046'] = alpha_046(code, end_date)
    alpha['alpha_047'] = alpha_047(code, end_date)
    alpha['alpha_048'] = alpha_048(code, end_date)
    alpha['alpha_049'] = alpha_049(code, end_date)
    alpha['alpha_050'] = alpha_050(code, end_date)
    alpha['alpha_051'] = alpha_051(code, end_date)
    alpha['alpha_052'] = alpha_052(code, end_date)
    alpha['alpha_053'] = alpha_053(code, end_date)
    alpha['alpha_054'] = alpha_054(code, end_date)
    alpha['alpha_055'] = alpha_055(code, end_date)
    alpha['alpha_056'] = alpha_056(code, end_date)
    alpha['alpha_057'] = alpha_057(code, end_date)
    alpha['alpha_058'] = alpha_058(code, end_date)
    alpha['alpha_059'] = alpha_059(code, end_date)
    alpha['alpha_060'] = alpha_060(code, end_date)
    alpha['alpha_061'] = alpha_061(code, end_date)
    alpha['alpha_062'] = alpha_062(code, end_date)
    alpha['alpha_063'] = alpha_063(code, end_date)
    alpha['alpha_064'] = alpha_064(code, end_date)
    alpha['alpha_065'] = alpha_065(code, end_date)
    alpha['alpha_066'] = alpha_066(code, end_date)
    alpha['alpha_067'] = alpha_067(code, end_date)
    alpha['alpha_068'] = alpha_068(code, end_date)
    alpha['alpha_069'] = alpha_069(code, end_date)
    alpha['alpha_070'] = alpha_070(code, end_date)
    alpha['alpha_071'] = alpha_071(code, end_date)
    alpha['alpha_072'] = alpha_072(code, end_date)
    alpha['alpha_073'] = alpha_073(code, end_date)
    alpha['alpha_074'] = alpha_074(code, end_date)
    #alpha['alpha_075'] = alpha_075(code, benchmark, end_date)
    alpha['alpha_076'] = alpha_076(code, end_date)
    alpha['alpha_077'] = alpha_077(code, end_date)
    alpha['alpha_078'] = alpha_078(code, end_date)
    alpha['alpha_079'] = alpha_079(code, end_date)
    alpha['alpha_080'] = alpha_080(code, end_date)
    alpha['alpha_081'] = alpha_081(code, end_date)
    alpha['alpha_082'] = alpha_082(code, end_date)
    alpha['alpha_083'] = alpha_083(code, end_date)
    alpha['alpha_084'] = alpha_084(code, end_date)
    alpha['alpha_085'] = alpha_085(code, end_date)
    alpha['alpha_086'] = alpha_086(code, end_date)
    alpha['alpha_087'] = alpha_087(code, end_date)
    alpha['alpha_088'] = alpha_088(code, end_date)
    alpha['alpha_089'] = alpha_089(code, end_date)
    alpha['alpha_090'] = alpha_090(code, end_date)
    alpha['alpha_091'] = alpha_091(code, end_date)
    alpha['alpha_092'] = alpha_092(code, end_date)
    alpha['alpha_093'] = alpha_093(code, end_date)
    alpha['alpha_094'] = alpha_094(code, end_date)
    alpha['alpha_095'] = alpha_095(code, end_date)
    alpha['alpha_096'] = alpha_096(code, end_date)
    alpha['alpha_097'] = alpha_097(code, end_date)
    alpha['alpha_098'] = alpha_098(code, end_date)
    alpha['alpha_099'] = alpha_099(code, end_date)
    alpha['alpha_100'] = alpha_100(code, end_date)
    alpha['alpha_101'] = alpha_101(code, end_date)
    alpha['alpha_102'] = alpha_102(code, end_date)
    alpha['alpha_103'] = alpha_103(code, end_date)
    alpha['alpha_104'] = alpha_104(code, end_date)
    alpha['alpha_105'] = alpha_105(code, end_date)
    alpha['alpha_106'] = alpha_106(code, end_date)
    alpha['alpha_107'] = alpha_107(code, end_date)
    alpha['alpha_108'] = alpha_108(code, end_date)
    alpha['alpha_109'] = alpha_109(code, end_date)
    alpha['alpha_110'] = alpha_110(code, end_date)
    alpha['alpha_111'] = alpha_111(code, end_date)
    alpha['alpha_112'] = alpha_112(code, end_date)
    alpha['alpha_113'] = alpha_113(code, end_date)
    alpha['alpha_114'] = alpha_114(code, end_date)
    alpha['alpha_115'] = alpha_115(code, end_date)
    alpha['alpha_116'] = alpha_116(code, end_date)
    alpha['alpha_117'] = alpha_117(code, end_date)
    alpha['alpha_118'] = alpha_118(code, end_date)
    alpha['alpha_119'] = alpha_119(code, end_date)
    alpha['alpha_120'] = alpha_120(code, end_date)
    alpha['alpha_121'] = alpha_121(code, end_date)
    alpha['alpha_122'] = alpha_122(code, end_date)
    alpha['alpha_123'] = alpha_123(code, end_date)
    alpha['alpha_124'] = alpha_124(code, end_date)
    alpha['alpha_125'] = alpha_125(code, end_date)
    alpha['alpha_126'] = alpha_126(code, end_date)
    alpha['alpha_127'] = alpha_127(code, end_date)
    alpha['alpha_128'] = alpha_128(code, end_date)
    alpha['alpha_129'] = alpha_129(code, end_date)
    alpha['alpha_130'] = alpha_130(code, end_date)
    alpha['alpha_131'] = alpha_131(code, end_date)
    alpha['alpha_132'] = alpha_132(code, end_date)
    alpha['alpha_133'] = alpha_133(code, end_date)
    alpha['alpha_134'] = alpha_134(code, end_date)
    alpha['alpha_135'] = alpha_135(code, end_date)
    alpha['alpha_136'] = alpha_136(code, end_date)
    alpha['alpha_137'] = alpha_137(code, end_date)
    alpha['alpha_138'] = alpha_138(code, end_date)
    alpha['alpha_139'] = alpha_139(code, end_date)
    alpha['alpha_140'] = alpha_140(code, end_date)
    alpha['alpha_141'] = alpha_141(code, end_date)
    alpha['alpha_142'] = alpha_142(code, end_date)
    alpha['alpha_143'] = alpha_143(code, end_date)
    alpha['alpha_144'] = alpha_144(code, end_date)
    alpha['alpha_145'] = alpha_145(code, end_date)
    alpha['alpha_146'] = alpha_146(code, end_date)
    alpha['alpha_147'] = alpha_147(code, end_date)
    alpha['alpha_148'] = alpha_148(code, end_date)
    #alpha['alpha_149'] = alpha_149(code, benchmark, end_date)
    alpha['alpha_150'] = alpha_150(code, end_date)
    alpha['alpha_151'] = alpha_151(code, end_date)
    alpha['alpha_152'] = alpha_152(code, end_date)
    alpha['alpha_153'] = alpha_153(code, end_date)
    alpha['alpha_154'] = alpha_154(code, end_date)
    alpha['alpha_155'] = alpha_155(code, end_date)
    alpha['alpha_156'] = alpha_156(code, end_date)
    alpha['alpha_157'] = alpha_157(code, end_date)
    alpha['alpha_158'] = alpha_158(code, end_date)
    alpha['alpha_159'] = alpha_159(code, end_date)
    alpha['alpha_160'] = alpha_160(code, end_date)
    alpha['alpha_161'] = alpha_161(code, end_date)
    alpha['alpha_162'] = alpha_162(code, end_date)
    alpha['alpha_163'] = alpha_163(code, end_date)
    alpha['alpha_164'] = alpha_164(code, end_date)
    alpha['alpha_165'] = alpha_165(code, end_date)
    alpha['alpha_166'] = alpha_166(code, end_date)
    alpha['alpha_167'] = alpha_167(code, end_date)
    alpha['alpha_168'] = alpha_168(code, end_date)
    alpha['alpha_169'] = alpha_169(code, end_date)
    alpha['alpha_170'] = alpha_170(code, end_date)
    alpha['alpha_171'] = alpha_171(code, end_date)
    alpha['alpha_172'] = alpha_172(code, end_date)
    alpha['alpha_173'] = alpha_173(code, end_date)
    alpha['alpha_174'] = alpha_174(code, end_date)
    alpha['alpha_175'] = alpha_175(code, end_date)
    alpha['alpha_176'] = alpha_176(code, end_date)
    alpha['alpha_177'] = alpha_177(code, end_date)
    alpha['alpha_178'] = alpha_178(code, end_date)
    alpha['alpha_179'] = alpha_179(code, end_date)
    alpha['alpha_180'] = alpha_180(code, end_date)
    #alpha['alpha_181'] = alpha_181(code, benchmark, end_date)
    #alpha['alpha_182'] = alpha_182(code, benchmark, end_date)
    alpha['alpha_183'] = alpha_183(code, end_date)
    alpha['alpha_184'] = alpha_184(code, end_date)
    alpha['alpha_185'] = alpha_185(code, end_date)
    alpha['alpha_186'] = alpha_186(code, end_date)
    alpha['alpha_187'] = alpha_187(code, end_date)
    alpha['alpha_188'] = alpha_188(code, end_date)
    alpha['alpha_189'] = alpha_189(code, end_date)
    alpha['alpha_190'] = alpha_190(code, end_date)
    alpha['alpha_191'] = alpha_191(code, end_date)
    return alpha

if __name__ == '__main__':
    import QUANTAXIS as QA
    pool = ['000001', '000002', '000005']
    #res = alpha_001(pool, '2018-06-30')
    #print(res)
    #res = alpha_075(pool, '000300.XSHG', '2018-06-30')
    #print(res)
    #res = alpha_101(pool, '2018-06-30')
    #print(res)
    a = alpha(pool, end_date='2018-06-30')
    print(a)
