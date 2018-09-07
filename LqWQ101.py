# -*- coding: utf-8 -*-

# functions which are in common use
from __future__ import division

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
import copy
import numpy as np
import operator
from numpy import mean,math,sum

###################### 共用函数群 ######################

def get_stock_day(begindate, enddate, code):
    return QA.QA_fetch_stock_day_adv(code, begindate, enddate)

def get_index_day(begindate, enddate, index):
    return QA.QA_fetch_index_day_adv(index, begindate, enddate)

def get_price(stock_pool=None, begin_date=None, end_date=None, field=None, head_count=0, plat_form_type='QA'):
    if plat_form_type != 'QA':
        return None

    data = QA.QA_fetch_stock_day_adv(stock_pool, begin_date, end_date)
    if field == 'open':
        field_data = data.open
    elif field == 'high':
        field_data = data.high
    elif field == 'low':
        field_data = data.low
    elif field == 'close':
        field_data = data.close
    else:
        return None

    if head_count != 0:
        res = field_data.unstack().tail(head_count)
    else:
        res = field_data.unstack()

    return res

def get_pool(index,enddate=None):

    '''
    Meaning:
        得到成分股的股票代码list

    Inputs:
        index: 股指代码

    Outputs:
        成分股的list
    '''

    if index == 'all':
        return list(get_all_securities(['stock'],date=enddate).index)
    else:
        return get_index_stocks(index,date=enddate)

    #if index == 'all':
    #    return QA.QA_fetch_stock_block_adv().code
    #else:
    #    return QA.QA_fetch_stock_block_adv(code=index).code

def sign(x):
    # x is a series
    '''
    Meaning:
        判断正负号，正数为1，负数为-1

    Inputs:
        x: 一个Series, index为股票代码，values为需要判断正负号的数值

    Outputs:
        result: 一个Series, index为股票代码，values为+1或-1
    '''
    result = pd.Series([0]*len(x),index=x.index)
    for stock in x.index:
        result[stock] = math.copysign(1,x[stock])

    return result

def correlation(x,y):
    '''
    Meaning:
       correlation value

    Inputs:
       x & y : x,y can be a DataFrame with one column, or lists, x and y have same length

    Outputs:
       相关系数的数值

    '''

    numerator = sum([(x.iloc[i]-mean(x))*(y.iloc[i]-mean(y)) for i in range(len(x))])

    denominator = (sum([(x.iloc[i]-mean(x)) **2 for i in range(len(x))])*sum([(y.iloc[i]-mean(y)) **2 for i in range(len(y))]))**(1/2)

    return numerator/denominator

def rank(series_need_rank,security_or_date):
    '''
    Inputs:
        series_need_rank: 一个需要rank的series，这个series的index为所有股票的代码或者日期
        security_or_date: 对应的需要rank的股票代码-在所有股票中rank这支股票对应值,或者对应的需要rank的date-在所有时间中rank这一天的值

    Outputs:
        第几名-从第一名开始往后从大到小排（最大值为第一名）
    '''
    #？？？没考虑并列情况？？？？？？？？？？？？？？？？？
    b = copy.deepcopy(series_need_rank)
    a = b.dropna()
    if str(pd.__version__) >= '0.17.0':
        a = a.sort_values()
    else:
        a.sort()
    y = pd.DataFrame()
    y['a'] = a
    y['a_rank'] = pd.Series(range(1,len(a)+1),index=a.index)
    vvv = y['a_rank']/len(a)
    df = pd.DataFrame([],index=b.index,columns=['rank_value_boolean'])
    df['rank_value_boolean'] = vvv


    return df['rank_value_boolean'][security_or_date]

def stddev(dataframe):
    '''
    Meaning:
        moving time-series standard deviation over the past d days

    Inputs:
        dataframe: 需要求标准差的dataframe（已经把长度切割好的）,index为时间,columns为股票池

    Outputs:
        标准差series,index为股票代码
    '''
    outputs = pd.Series([0.0]*len(dataframe.columns),index=dataframe.columns)
    length = len(dataframe.index)
    for stock in dataframe.columns:
        outputs[stock] = (sum([(dataframe[stock].iloc[j]-mean(dataframe[stock]))**2 for j in range(length)])/length)**(1/2)
        # temp = 0
        # for j in range(length):
        #     temp += (dataframe[stock].iloc[j]-mean(dataframe[stock]))**2
        # outputs[stock] = (temp/length)**(1/2)
    return outputs

def signedpower(x,a):
    '''
    Meaning:
        signedpower(x,a)=x^a
    Inputs:
        x 是一个series,或者一个int
        a 是一个series,或者一个int,当a为series时，index与x相同
    Outputs:
        x中每个元素的a次方

    '''

    s = x**a

    return s

def returns(close):

    '''
    Meaning:
        求收益率

    Inputs:
        close：closeprice的DataFrame

    Outputs:
        收益率的DataFrame 或者Series（若为单只股票）
    '''

    temp2_01 = (close.diff(1))[1:]
    temp2_02 = copy.deepcopy(temp2_01)
    temp2_01.index = close.index[:-1]
    a = temp2_01/close.ix[:-1]
    a.index = temp2_02.index

    return a

def decay_linear(x):

    '''
    Meaning:
        weighted moving average over the past d days with linearly decaying weights d,d-1,...1, ---rescaled to sum up to 1

    Inputs:
        x: series or list, which length is d

    Outputs:
        value of weighted moving average
    '''
    d = len(x)
    result = 0
    for i in range(1,len(x)+1):
        result += i*2/((1+d)*d)*x[i-1]

    return result

def scale(x,k=1):
    '''
    Meaning:
        rescaled x such that sum(abs(x)) = a (the default is a=1)

    Inputs:
        x: a series, can't be a list

    Outputs:
        value of x
    '''
    return x.mul(k).div(np.abs(x).sum())

def rank_pool(series_need_rank):

    '''
    Inputs:
        series_need_rank: 一个需要rank的series，这个series的index为所有股票的代码或者日期

    Outputs:
        第几名-从第一名开始往后从大到小排（最大值为第一名）的series
    '''

    #？？？没考虑并列情况？？？？？？？？？？？？？？？？？

    b = copy.deepcopy(series_need_rank)
    a = b.dropna()
    if str(pd.__version__) >= '0.17.0':
        a = a.sort_values()
    else:
        a.sort()
    y = pd.DataFrame()
    y['a'] = a
    y['a_rank'] = pd.Series(range(1,len(a)+1),index=a.index)
    vvv = y['a_rank']/len(a)
    df = pd.DataFrame([],index=b.index,columns=['rank_value_boolean'])
    df['rank_value_boolean'] = vvv

    return df['rank_value_boolean']

def ts_argmax(dataframe):
    '''
    Meaning:
        which day ts_max(x,d) occurred on

    Inputs:
       dataframe : 需要进行求值的DataFrame，columns为股票代码，index为时间

    Outputs:
       一个Series，index为股票代码，values为每只股票这几天最大的值对应的序数，（第一天为1，有d天，最后一天为d，若最大值发生在第二天，
       则这只股票对应值为2）
    '''

    ts_argmax_series = pd.Series([0]*len(dataframe.columns),index=dataframe.columns)

    for stock in dataframe.columns:
        max_index, max_value = max(enumerate(dataframe[stock]), key=operator.itemgetter(1))
        ts_argmax_series[stock] = max_index+1


    return ts_argmax_series

def ts_argmin(dataframe):
    '''
    Meaning:
        which day ts_min(x,d) occurred on

    Inputs:
       dataframe : 需要进行求值的DataFrame，columns为股票代码，index为时间

    Outputs:
       一个Series，index为股票代码，values为每只股票这几天最小的值对应的序数，（第一天为1，有d天，最后一天为d，若最大值发生在第二天，
       则这只股票对应值为2）
    '''

    ts_argmin_seires = pd.Series([0]*len(dataframe.columns),index=dataframe.columns)

    for stock in dataframe.columns:
        min_index, min_value = min(enumerate(dataframe[stock]), key=operator.itemgetter(1))
        ts_argmin_seires[stock] = min_index+1


    return ts_argmin_seires

def adv(dataframe_money,d,y):
    '''
    Meaning:
       adv{d}: average daily dollar volume for the past d days

    Inputs:
       dataframe_money:columns为股票代码，index为时间，index的行数应该为d+(y-1)行
       y: value of adv{d} over the past y days

    Outputs:
       一个DataFrame，columns为股票代码，index为时间，从enddate开始之前的y天
    '''

    result_dataframe = pd.DataFrame([],index=dataframe_money.index[-y:],columns=dataframe_money.columns)
    for i in range(y):
        adv_d = mean(dataframe_money.iloc[i:i+d,:])
        result_dataframe.iloc[i,:] = adv_d

    return result_dataframe

def correlation_pool(dataframe1,dataframe2):

    '''
    Meaning:
        correlation value

    Inputs:
       dataframe1 & dataframe2 : 需要进行求相关系数的dataframe，两个dataframe具有相同的index和相同的columns

    Outputs:
       一个series，index为股票代码，values为对应的相关系数的数值

    '''
    output = pd.Series([0.0]*len(dataframe1.columns),index=dataframe1.columns)

    for stock in dataframe1.columns:
        output[stock] = correlation(dataframe1[stock],dataframe2[stock])

    return output

def covariance_pool(dataframe1,dataframe2):
    '''
    Meaning:
        covariance value

    Inputs:
        dataframe1 & dataframe2 : 需要进行covariance的dataframe，两个dataframe具有相同的index和相同的columns

    Outputs:
         一个series，index为股票代码，values为对应的covariance的数值
    '''
    output = pd.Series([0.0]*len(dataframe1.columns),index=dataframe1.columns)
    length = len(dataframe1.index)
    for stock in dataframe1.columns:
        left = sum([dataframe1[stock].iloc[i]*dataframe2[stock].iloc[i] for i in range(length)])/length
        right = (sum(dataframe1[stock])/length)*(sum(dataframe2[stock])/length)
        output[stock] = left-right


    return output

def ts_min(dataframe):
    '''
    Meaning:
       time-series min over the past d days

    Inputs:
       dataframe: 被切割好的DataFrame, index长度为d

    Outputs:
       一个series，index为股票代码，values为min值

    '''
    output = pd.Series([0.0]*len(dataframe.columns),index = dataframe.columns)
    for stock in dataframe.columns:
        a = dataframe[stock]
        b = a.dropna()
        try:
            output[stock] = min(b)
        except:
            output[stock] = np.nan

    return output

def ts_max(dataframe):
    '''
    Meaning:
       time-series max over the past d days

    Inputs:
       dataframe: 被切割好的DataFrame, index长度为d

    Outputs:
       一个series，index为股票代码，values为min值

    '''
    output = pd.Series([0.0]*len(dataframe.columns),index = dataframe.columns)
    for stock in dataframe.columns:
        a = dataframe[stock]
        b = a.dropna()
        try:
            output[stock] = max(b)
        except:
            output[stock] = np.nan

    return output

def decay_linear_pool(dataframe):
    '''
    Meaning:
       weighted moving average over the past d days with linearly decaying weights d,d-1,...1 (rescaled to sum up to 1)

    Inputs:
       dataframe: 被切割好的DataFrame

    Outputs:
       一个series，index为股票代码，values为decay_linear值

    '''
    output = pd.Series([0.0]*len(dataframe.columns),index=dataframe.columns)
    for stock in dataframe.columns:
        a = dataframe[stock]
        b = a.dropna()
        for i in range(1,len(b.index)+1):
            output[stock] += b.iloc[i-1]*2/(1+i)

    return output

def delta(dataframe,d):
    '''
    Meaning:
       delta(x,d):today's value of x minus the value of x d days ago

    Inputs:
       dataframe: 要计算的x已经计算好了, 并且dataframe也已经切割好，dataframe的最后一行为被减数

    Outputs:
       一个series，index为股票代码，values为delta值

    '''
    output = dataframe.iloc[-1,:]-dataframe.iloc[-1-d,:]

    return output

def ts_rank(dataframe):
    '''
    Meaning:
       ts_rank(x,d) = time-series rank in the past d days

    Inputs:
       dataframe: 要计算的x已经计算好了, 并且dataframe也已经切割好，共有d行，dataframe的最后一行为被rank的数

    Outputs:
       一个series，index为股票代码，values为delta值

    '''

    output = pd.Series([0.0]*len(dataframe.columns),index=dataframe.columns)
    for stock in dataframe.columns:
        output[stock] = rank(dataframe[stock],dataframe.index[-1])

    return output


###################### Alpha函数群 ######################

def alpha_001(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):


    '''
    公式：
        rank(Ts_ArgMax(SignedPower(((returns < 0) ? stddev(returns, 20) : close), 2.), 5)) - 0.5
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    #pool = get_pool(index,enddate)
    #close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=25)['close']
    close = get_price(pool, begin_date, end_date, 'close', 25, plat_form_type)
    returns_df = returns(close)
    signedpower_df = pd.DataFrame([],index=range(5),columns=pool)
    for stock in pool:
        for i in range(5):

            if returns_df[stock].iloc[-5+i]<0:

                signedpower_df[stock].loc[i] = signedpower(stddev(returns_df[stock].iloc[i:20+i].to_frame()),2).iloc[0]

            else:
                signedpower_df[stock].loc[i] = signedpower(close[stock].iloc[20+i],2)

#         print(signedpower_df[stock])

    result = rank_pool(ts_argmax(signedpower_df))-0.5

    return result


def alpha_002(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        (-1 * correlation(rank(delta(log(volume), 2)), rank(((close - open) / open)), 6))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    #pool = get_pool(index,enddate)
    #openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=6)['open']
    #close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=6)['close']
    #volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=8)['volume']

    #求rank(    delta(   log(volume)   , 2)   )
    delta_df_01= np.log(volume).diff(2)
    delta_df= delta_df_01[-6:]
    rank_df_01 = pd.DataFrame([],range(6),columns=pool)
    for i in range(6):
        rank_df_01.loc[i] = rank_pool(delta_df.iloc[i,:])


    #求rank((close-open)/open)
    df_02 = (close-openprice)/openprice
    rank_df_02 = pd.DataFrame([],range(6),columns=pool)
    for i in range(6):
        rank_df_02.loc[i] = rank_pool(df_02.iloc[i,:])

    #求correlation
    result = correlation_pool(rank_df_01,rank_df_02)

    return -result


def alpha_003(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        (-1 * correlation(rank(open), rank(volume), 10))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=10)['open']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=10)['volume']

    #求rank(open),rank(volume)
    rank_open = pd.DataFrame([],range(10),columns=pool)
    rank_volume = pd.DataFrame([],range(10),columns=pool)
    for i in range(10):
        rank_open.loc[i] = rank_pool(openprice.iloc[i,:])
        rank_volume.loc[i] = rank_pool(volume.iloc[i,:])

    #求correlation
    result = correlation_pool(rank_open,rank_volume)

    return -result


def alpha_004(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        (-1 * Ts_Rank(rank(low), 9))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=9)['low']

    rank_low = pd.DataFrame([],index=range(9),columns=pool)
    for i in range(9):
        rank_low.loc[i] = rank_pool(low.iloc[i,:])

    result = ts_rank(rank_low)

    return -result


def alpha_005(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        (rank((open - (sum(vwap, 10) / 10))) * (-1 * abs(rank((close - vwap)))))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=10)['avg']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=1)['open']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=1)['close']

    #rank(   open - sum(vwap, 10) / 10   )
    df_01 = openprice-sum(vwap)/10
    rank_df_01 = rank_pool(df_01.iloc[0])

    #abs(  rank(close - vwap)   )
    df_02 = close-vwap.iloc[-1,:]
    rank_df_02 = abs(rank_pool(df_02.iloc[0]))

    result = rank_df_01*(-1)*rank_df_02

    return result


def alpha_006(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
         -1 * correlation(open, volume, 10)
    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''
    pool = get_pool(index,enddate)
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=10)['open']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=10)['volume']

    result = correlation_pool(openprice,volume)

    return -1*result


def alpha_007(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        ((adv20 < volume) ? ((-1 * ts_rank(abs(delta(close, 7)), 60)) * sign(delta(close, 7))) : (-1 * 1))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''
    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=67)['close']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=1)['volume']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=20)['money']

    adv20 = adv(money,20,1)

    #ts_rank(abs(delta(close, 7)), 60)
    abs_df = pd.DataFrame([],index=range(60),columns=pool)
    for i in range(60):
        abs_df.loc[i] = abs(delta(close.iloc[i:i+8,:],7))

    ts_rank_series = ts_rank(abs_df)

    #sign(delta(close, 7))
    sign_series = sign(delta(close.iloc[-8:,:],7))

    result_series = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:

        if adv20[stock].iloc[0]<volume[stock].iloc[0]:
            result_series[stock] = -1*ts_rank_series[stock]*sign_series[stock]

        else:
            result_series[stock] = -1

    return result_series

def alpha_008(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        (-1 * rank(((sum(open, 5) * sum(returns, 5)) - delay((sum(open, 5) * sum(returns, 5)), 10))))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''
    pool = get_pool(index,enddate)

    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=15)['open']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=16)['close']

    returns_df = returns(close)

    #sum(open, 5) * sum(returns, 5)
    series_01 = sum(openprice[-5:])*sum(returns_df[-5:])

    #delay(  sum(open, 5) * sum(returns, 5)   , 10)
    series_02 = sum(openprice[:5])*sum(returns_df[:5])

    result = rank_pool(series_01-series_02)

    return -result


def alpha_009(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
     ((0 < ts_min(delta(close, 1), 5)) ? delta(close, 1) : ((ts_max(delta(close, 1), 5) < 0) ? delta(close, 1) : (-1 * delta(close, 1))))

    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''
    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=6)['close']

    delta_df_01 = pd.DataFrame([],index=range(5),columns=pool)
    for i in range(5):
        delta_df_01.loc[i] = delta(close.iloc[i:i+2,:],1)

    ts_min_series = ts_min(delta_df_01)
    ts_max_series = ts_max(delta_df_01)
    result_series = pd.Series([0.0]*len(pool),index=pool)

    for stock in pool:
        if ts_min_series[stock]>0:
            result_series[stock] = delta_df_01[stock].iloc[-1]
        elif ts_max_series[stock]<0:
            result_series[stock] = delta_df_01[stock].iloc[-1]
        else:
            result_series[stock] = -delta_df_01[stock].iloc[-1]

    return result_series


def alpha_010(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        rank((0 < ts_min(delta(close, 1), 4)) ? delta(close, 1) : ((ts_max(delta(close, 1), 4) < 0) ? delta(close, 1) : (-1 * delta(close, 1))))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=5)['close']

    delta_df_01 = pd.DataFrame([],index=range(4),columns=pool)
    for i in range(4):
        delta_df_01.loc[i] = delta(close.iloc[i:i+2,:],1)

    ts_min_series = ts_min(delta_df_01)
    ts_max_series = ts_max(delta_df_01)

    series_willbe_ranked = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:

        if ts_min_series[stock]>0:
            series_willbe_ranked[stock] = delta_df_01[stock].iloc[-1]

        elif ts_max_series[stock]<0:
            series_willbe_ranked[stock] = delta_df_01[stock].iloc[-1]

        else:
            series_willbe_ranked[stock] = -1*delta_df_01[stock].iloc[-1]

    result = rank_pool(series_willbe_ranked)

    return result



def alpha_011(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        ((rank(ts_max((vwap - close), 3)) + rank(ts_min((vwap - close), 3))) * rank(delta(volume, 3)))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=4)['volume']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=3)['close']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=3)['avg']

    #rank(    ts_max(   vwap - close   , 3)   )
    ts_max_df = ts_max(vwap-close)
    rank_ts_max = rank_pool(ts_max_df)

    #rank(   ts_min(  vwap - close  , 3)  )
    ts_min_df = ts_min(vwap - close)
    rank_ts_min = rank_pool(ts_min_df)

    #rank(   delta(volume, 3)  )
    delta_series = delta(volume,3)
    rank_delta = rank_pool(delta_series)

    result = (rank_ts_max+rank_ts_min)*rank_delta

    return result


def alpha_012(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        sign(delta(volume, 1)) * (-1 * delta(close, 1))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=2)['volume']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=2)['close']

    #sign(delta(volume, 1))
    sign_series = sign(delta(volume,1))

    #delta(close, 1)
    delta_series = delta(close,1)

    return -1*sign_series*delta_series



def alpha_013(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        (-1 * rank(covariance(rank(close), rank(volume), 5)))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=5)['volume']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=5)['close']

    rank_volume_df = pd.DataFrame([],index=range(5),columns=pool)
    rank_close_df = pd.DataFrame([],index=range(5),columns=pool)
    for i in range(5):
        rank_volume_df.loc[i] = rank_pool(volume.iloc[i,:])
        rank_close_df.loc[i] = rank_pool(close.iloc[i,:])

    result = rank_pool(covariance_pool(rank_volume_df,rank_close_df))

    return -1*result


def alpha_014(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        ((-1 * rank(delta(returns, 3))) * correlation(open, volume, 10))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''


    pool = get_pool(index,enddate)

    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=10)['volume']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=5)['close']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=10)['open']

    #rank(   delta(returns, 3)   )
    rank_series = rank_pool(delta(returns(close),3))

    #correlation(open, volume, 10)
    correlation_series = correlation_pool(openprice,volume)

    result = rank_series*correlation_series

    return -1*result


def alpha_015(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        (-1 * sum(rank(correlation(rank(high), rank(volume), 3)), 3))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=5)['volume']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=5)['high']

    rank_volume_df = pd.DataFrame([],index=range(5),columns=pool)
    rank_high_df = pd.DataFrame([],index=range(5),columns=pool)
    for i in range(5):
        rank_volume_df.loc[i] = rank_pool(volume.iloc[i,:])
        rank_high_df.loc[i] = rank_pool(high.iloc[i,:])

    rank_df = pd.DataFrame([],index=range(3),columns=pool)
    for i in range(3):
        rank_df.loc[i] = rank_pool(correlation_pool(rank_volume_df.iloc[i:i+3,:],rank_high_df.iloc[i:i+3,:]))

    result = sum(rank_df)

    return -1*result


def alpha_016(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        (-1 * rank(covariance(rank(high), rank(volume), 5)))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=5)['volume']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=5)['high']

    rank_high = pd.DataFrame([],index=range(5),columns=pool)
    rank_volume = pd.DataFrame([],index=range(5),columns=pool)
    for i in range(5):
        rank_high.loc[i] = rank_pool(high.iloc[i,:])
        rank_volume.loc[i] = rank_pool(volume.iloc[i,:])

    result = rank_pool(covariance_pool(rank_high,rank_volume))

    return -1*result


def alpha_017(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
         (((-1 * rank(ts_rank(close, 10))) * rank(delta(delta(close, 1), 1))) * rank(ts_rank((volume / adv20), 5)))
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=5)['volume']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=10)['close']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=24)['money']

    adv20 = adv(money,20,5)

    #rank(    ts_rank(close, 10)   )
    rank_series1 = rank_pool(ts_rank(close))


    close_ = close.iloc[-3:,:]
    # rank(   delta(    delta(close, 1)   , 1)    )
    delta_df = pd.DataFrame([],index=range(2),columns=pool)
    for i in range(2):
        delta_df.loc[i] = delta(close_.iloc[i:i+2,:],1)

    rank_series2 = rank_pool(delta(delta_df,1))

    # rank(    ts_rank(   volume / adv20    , 5)    )
    division = pd.DataFrame([],index=volume.index,columns=pool)
    null_list = []
    for stock in pool:
        try:
            division[stock] = volume[stock]/adv20[stock]
        except:
            division[stock] = 0
            null_list.append(stock)

    rank_series3 = rank_pool(ts_rank(division))
    rank_series3[null_list] = 0

    return -1*rank_series1*rank_series2*rank_series3


def alpha_018(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
         (-1 * rank(((stddev(abs((close - open)), 5) + (close - open)) + correlation(close, open, 10))))

    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=10)['close']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=10)['open']

    # correlation(   close, open  , 10)
    corre_series = correlation_pool(close,openprice)

    # close - open
    minus_series = close.iloc[-1,:]-openprice.iloc[-1,:]

    #stddev(  abs(close - open)  , 5)
    stddev_series = stddev(abs(close.iloc[-5:,:]-openprice.iloc[-5:,:]))

    result = rank_pool(stddev_series+minus_series+corre_series)

    return -1*result


def alpha_019(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        ((-1 * sign(((close - delay(close, 7)) + delta(close, 7)))) * (1 + rank((1 + sum(returns, 250)))))

    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=251)['close']

    #sign(   close - delay(close, 7) + delta(close, 7)    )
    series1 = sign(close.iloc[-1,:]-close.iloc[-8,:]+delta(close.iloc[-8:,:],7))

    #rank(    1 + sum(returns, 250)   )
    rank_series = rank_pool(1+sum(returns(close)))

    return -1*series1*(rank_series+1)


def alpha_020(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        (((-1 * rank((open - delay(high, 1)))) * rank((open - delay(close, 1)))) * rank((open - delay(low, 1))))

    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=1)['open']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=2)['close']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=2)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=2)['low']

    #rank(   open - delay(high, 1)  )
    series1 = rank_pool(openprice.iloc[-1,:]-high.iloc[-2,:])

    #rank(   open - delay(close, 1)   )
    series2 = rank_pool(openprice.iloc[-1,:]-close.iloc[-2,:])

    #rank(    open - delay(low, 1)   )
    series3 = rank_pool(openprice.iloc[-1,:]-low.iloc[-2,:])

    return -1*series1*series2*series3


def alpha_021(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        ((sum(close, 8) / 8 + stddev(close, 8)) < sum(close, 2) / 2) ? -1 : (sum(close, 2) / 2 < (sum(close, 8) / 8 - stddev(close, 8)) ? 1 : ((1 <= volume / adv20) ? 1 : -1))
    Inputs:
        enddate: 查询日期
        Index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=8)['close']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=1)['volume']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=20)['money']

    adv20 = adv(money,20,1)

    mean_close_8 = mean(close)
    mean_close_2 = mean(close.iloc[-2:,:])
    stddev_series = stddev(close)

    division = pd.Series([0.0]*len(pool),index=pool)
    result = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:
        try:
            division[stock] = volume[stock].iloc[-1]/adv20[stock].iloc[-1]
        except:
            division[stock] = 0

    for stock in pool:
        if mean_close_8[stock] + stddev_series[stock] <  mean_close_2[stock]:
            result[stock] = -1
        elif mean_close_2[stock]< mean_close_8[stock] + stddev_series[stock]:
            result[stock] = 1
        elif division[stock]>=1:
            result[stock] = -1
        else:
            result[stock] = -1

    return result



def alpha_022(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        (-1 * (delta(correlation(high, volume, 5), 5) * rank(stddev(close, 20))))
    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=10)['high']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=20)['close']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=10)['volume']

    #delta(      correlation(high, volume, 5)    , 5)
    correlation_df = pd.DataFrame([],index=range(6),columns=pool)
    for i in range(6):
        correlation_df.loc[i] = correlation_pool(high.iloc[i:i+5,:],volume.iloc[i:i+5,:])
    delta_series = delta(correlation_df,5)

    #rank(    stddev(close, 20)    )
    rank_series = rank_pool(stddev(close))


    return -1*delta_series*rank_series



def alpha_023(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        (((sum(high, 20) / 20) < high) ? (-1 * delta(high, 2)) : 0)
    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=20)['high']

    result_series = pd.Series([0.0]*len(pool),index=pool)
    delta_series = delta(high,2)

    for stock in pool:
        if mean(high[stock]) < high[stock].iloc[-1]:
            result_series[stock] = -1*delta_series[stock]
        else:
            result_series[stock] = 0


    return result_series



def alpha_024(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        ((((delta((sum(close, 100) / 100), 100) / delay(close, 100)) < 0.05) ||
        ((delta((sum(close, 100) / 100), 100) / delay(close, 100)) == 0.05)) ?
        (-1 * (close - ts_min(close, 100))) : (-1 * delta(close, 3)))
    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=200)['close']

    #delta(  sum(close, 100) / 100, 100) / delay(  close, 100) < =0.05
    mean_df = pd.DataFrame([],index=range(101),columns=pool)
    for i in range(101):
        mean_df.loc[i] = mean(close.iloc[i:i+100,:])
    delta_mean_series = delta(mean_df,100)

    delay_series = close.iloc[-101,:]
    ts_min_series = ts_min(close.iloc[-100:,:])
    delta_series_02 = delta(close.iloc[-4:,:],3)

    result_series = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:
        if delta_mean_series[stock]/delay_series[stock]<=0.05:
            result_series[stock] = -1*(close[stock].iloc[-1]-ts_min_series[stock])
        else:
            result_series[stock] = -1*delta_series_02[stock]


    return result_series


def alpha_025(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        rank(((((-1 * returns) * adv20) * vwap) * (high - close)))
    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    high = (get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=1)['high']).iloc[-1,:]
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=2)['close']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=20)['money']
    vwap = (get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=1)['avg']).iloc[-1,:]

    adv20 = (adv(money,20,1)).iloc[-1,:]
    returns_series  = returns(close).iloc[-1,:]

    rank_result = rank_pool(-1*(high-close.iloc[-1,:])*vwap*adv20*returns_series)

    return rank_result


def alpha_026(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        (-1 * ts_max(correlation(ts_rank(volume, 5), ts_rank(high, 5), 5), 3))
    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=11)['high']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=11)['volume']

    #ts_rank(volume, 5), ts_rank(high, 5)
    ts_rank_volume_df = pd.DataFrame([],index=range(7),columns=pool)
    ts_rank_high_df = pd.DataFrame([],index=range(7),columns=pool)
    for i in range(7):
        ts_rank_volume_df.loc[i] = ts_rank(volume.iloc[i:i+5,:])
        ts_rank_high_df.loc[i] = ts_rank(high.iloc[i:i+5,:])

    correlation_df = pd.DataFrame([],index=range(3),columns=pool)
    for i in range(3):
        correlation_df.loc[i] = correlation_pool(ts_rank_volume_df.iloc[i:i+5,:],ts_rank_high_df.iloc[i:i+5,:])

    result = ts_max(correlation_df)

    return -1*result


def alpha_027(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        ((0.5 < rank((sum(correlation(rank(volume), rank(vwap), 6), 2) / 2.0))) ? (-1 * 1) : 1)
    Inputs:
        index: 股票池
        enddate: 查询日期
    Outputs:
        因子的值
    '''


    pool = get_pool(index,enddate)

    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=7)['volume']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=7)['avg']

    #rank(volume), rank(vwap)
    rank_volume_df = pd.DataFrame([],index=range(7),columns=pool)
    rank_vwap_df = pd.DataFrame([],index=range(7),columns=pool)
    for i in range(7):
        rank_volume_df.loc[i] = rank_pool(volume.iloc[i,:])
        rank_vwap_df.loc[i] = rank_pool(vwap.iloc[i,:])

    #correlation(     rank(volume), rank(vwap)    , 6)
    correlation_df = pd.DataFrame([],index=range(2),columns=pool)
    for i in range(2):
        correlation_df.loc[i] = correlation_pool(rank_volume_df.iloc[i:i+6,:],rank_vwap_df.iloc[i:i+6,:])

    compare_series = rank_pool(mean(correlation_df))
    result_series = pd.Series([0]*len(pool),index=pool)
    for stock in pool:
        if compare_series[stock]>0.5:
            result_series[stock] = -1
        else:
            result_series[stock] = 1

    return result_series


def alpha_028(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
        scale(((correlation(adv20, low, 5) + ((high + low) / 2)) - close))
    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=1)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=5)['low']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=1)['close']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=24)['money']

    adv20 = adv(money,20,5)

    #correlation(adv20, low, 5)
    correlation_series = correlation_pool(adv20,low)

    result_series = scale(correlation_series+(high.iloc[0,:]+low.iloc[-1,:])/2-close.iloc[-1,:])

    return result_series


def alpha_029(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (min(product(rank(rank(scale(log(sum(ts_min(rank(rank((-1 * rank(delta((close - 1), 5))))), 2), 1))))), 1), 5)
    + ts_rank(delay((-1 * returns), 6), 5))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=12)['close']

    #ts_min(    rank(    rank(    ts_min(  rank(   rank(   -1 * rank(   delta(close, 5)   )  )  )  , 2)   )   )   , 5)
    #min没有意义，手动改为ts_min
    rank_01_df = pd.DataFrame([],index=range(6),columns=pool)
    for i in range(6):
        rank_01_df.loc[i] = rank_pool(rank_pool(delta(close.iloc[i+1:i+7,:],5))*(-1))

    rank_ts_min_df = pd.DataFrame([],index=range(5),columns=pool)
    for i in range(5):
        rank_ts_min_df.loc[i] = rank_pool(rank_pool(ts_min(rank_01_df.iloc[i:i+2,:])))

    ts_min_series = ts_min(rank_ts_min_df)

    #ts_rank(    delay(    -1 * returns  , 6)     , 5)
    returns_df = returns(close)
    ts_rank_series = ts_rank(returns_df.iloc[i:i+5,:])


    return ts_min_series+ts_rank_series


def alpha_030(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (((1.0 - rank(((sign((close - delay(close, 1))) + sign((delay(close, 1) - delay(close, 2))))
    + sign((delay(close, 2) - delay(close, 3)))))) * sum(volume, 5)) / sum(volume, 20))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=4)['close']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=20)['volume']

    #rank( sign(  close - delay(close, 1)  ) + sign( delay(close, 1) - delay(close, 2) ) + sign(  delay(close, 2) - delay(close, 3) ) )
    rank_series = rank_pool(sign(close.iloc[-1,:]-close.iloc[-2,:])+sign(close.iloc[-2,:]-close.iloc[-3,:])+sign(close.iloc[-3,:]-close.iloc[-4,:]))

    result_series = (1-rank_series)*sum(volume.iloc[-5:,:])/sum(volume)

    return result_series

def alpha_031(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    ((rank(rank(rank(decay_linear((-1 * rank(rank(delta(close, 10)))), 10)))) + rank((-1 * delta(close, 3))))
    + sign(scale(correlation(adv20, low, 12))))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=20)['close']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=12)['low']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=31)['money']

    #rank(     decay_linear(   -1 * rank(   rank(    delta(close, 10)  )   )   , 10)  )
    rank_df = pd.DataFrame([],index=range(10),columns=pool)
    for i in range(10):
        rank_df.loc[i] = -1*rank_pool(rank_pool(delta(close.iloc[i:i+11,:],10)))

    decay_linear_series = decay_linear_pool(rank_df)

    rank_series_01 = rank_pool(decay_linear_series)

    #rank(   -1 * delta(close, 3)  )
    rank_series_02 = rank_pool(-1*delta(close.iloc[-4:,:],3))

    #sign(    correlation(  adv20, low, 12)     )
    adv20 = adv(money,20,12)
    sign_series = sign(correlation_pool(adv20,low))

    return rank_series_01+rank_series_02+sign_series


def alpha_032(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (scale(((sum(close, 7) / 7) - close)) + (20 * scale(correlation(vwap, delay(close, 5), 230))))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=235)['close']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=230)['avg']

    #20 * scale(    correlation(    vwap, delay(close, 5)   , 230)   )
    scale_series_02 = 20*scale(correlation_pool(vwap,close.iloc[:230,:]))

    #scale(   sum(close, 7) / 7 - close   )
    scale_series_01 = scale(mean(close.iloc[-7:,:])-close.iloc[-1,:])

    return scale_series_02+scale_series_01


def alpha_033(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    rank((-1 * ((1 - (open / close))^1)))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=1)['open']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=1)['close']

    rank_series = rank_pool(-1*(1-openprice.iloc[-1,:]/close.iloc[-1,:]))

    return rank_series


def alpha_034(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    rank(((1 - rank((stddev(returns, 2) / stddev(returns, 5)))) + (1 - rank(delta(close, 1)))))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=6)['close']

    returns_df = returns(close)
    rank_series = rank_pool(1-rank_pool(stddev(returns_df.iloc[-2:,:])/stddev(returns_df))+1-rank_pool(delta(close.iloc[-2:,:],1)))

    return rank_series


def alpha_035(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    ((Ts_Rank(volume, 32) * (1 - Ts_Rank(((close + high) - low), 16))) * (1 - Ts_Rank(returns, 32)))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=33)['close']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=16)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=16)['low']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=32)['volume']

    #Ts_Rank(volume, 32)
    ts_rank_series01 = ts_rank(volume)

    #(1 - Ts_Rank(   close + high - low   , 16)   )
    series02 = 1-ts_rank(close.iloc[-16:,:]+high-low)

    #(1 - Ts_Rank(returns, 32)  )
    returns_df = returns(close)
    series03 = 1-ts_rank(returns_df)

    return ts_rank_series01*series02*series03


def alpha_036(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (((((2.21 * rank(correlation((close - open), delay(volume, 1), 15))) + (0.7 * rank((open - close))))
    + (0.73 * rank(Ts_Rank(delay((-1 * returns), 6), 5)))) + rank(abs(correlation(vwap, adv20, 6))))
    + (0.6 * rank((((sum(close, 200) / 200) - open) * (close - open)))))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=200)['close']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=25)['money']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=15)['open']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=16)['volume']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=6)['avg']

    #0.7 * rank(open - close)
    series_02 = 0.7*rank_pool(openprice.iloc[-1,:]-close.iloc[-1,:])

    #rank(    abs(   correlation(vwap, adv20, 6)  )  )
    adv20 = adv(money,20,6)
    series_04 = rank_pool(abs(correlation_pool(vwap,adv20)))

    #0.73 * rank(   Ts_Rank(   delay(-1 * returns, 6)   , 5)   )
    returns_df = (-1*returns(close.iloc[-12:,:])).iloc[:5,:]
    series_03 = 0.73*rank_pool(ts_rank(returns_df))

    #2.21*rank(   correlation(   close - open, delay(volume, 1)   , 15)   )
    df_01 = close.iloc[-15:,:]-openprice
    series_01 = 2.21*rank_pool(correlation_pool(df_01,volume.iloc[:-1,:]))

    #0.6 * rank(   (sum(close, 200) / 200 - open) * (close - open)   )
    series_05 = 0.6*rank_pool((mean(close)-openprice.iloc[-1,:])*(close.iloc[-1,:]*openprice.iloc[-1,:]))


    return series_01+series_02+series_03+series_04+series_05


def alpha_037(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (rank(correlation(delay((open - close), 1), close, 200)) + rank((open - close)))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=201)['close']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=201)['open']

    #rank(open - close)
    rank_series02 = openprice.iloc[-1,:]-close.iloc[-1,:]

    #rank(    correlation(    delay(open - close, 1)  , close, 200)  )
    rank_series01 = rank_pool(correlation_pool((openprice-close).iloc[:-1,:],close.iloc[1:,:]))


    return rank_series01+rank_series02


def alpha_038(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    ((-1 * rank(Ts_Rank(close, 10))) * rank((close / open)))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=10)['close']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=1)['open']

    #rank(  Ts_Rank(close, 10)   )
    rank_series_01 = rank_pool(ts_rank(close))

    #rank(  close / open  )
    rank_series_02 = rank_pool(close.iloc[-1,:]/openprice.iloc[-1,:])


    return -1*rank_series_01*rank_series_02


def alpha_039(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    ((-1 * rank((delta(close, 7) * (1 - rank(decay_linear((volume / adv20), 9)))))) * (1 + rank(sum(returns, 250))))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=251)['close']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=9)['volume']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=28)['money']


    #-1 * rank(    delta(close, 7) * (1 -  rank(   decay_linear(volume / adv20, 9)  )   )  )
    adv20 = adv(money,20,9)

    decay_df = pd.DataFrame([],index=volume.index,columns=pool)
    for stock in pool:
        for i in range(len(volume.index)):
            if adv20[stock].iloc[i] == 0:
                decay_df[stock].iloc[i] = 0
            else:
                decay_df[stock].iloc[i] =volume[stock].iloc[i]/adv20[stock].iloc[i]

    series_02 = -1*rank_pool(delta(close.iloc[-8:,:],7)*(1-rank_pool(decay_linear_pool(decay_df))))

    #1 + rank(   sum(returns, 250)  )
    series_01 = 1 + rank_pool(sum(returns(close)))

    return series_01*series_02


def alpha_040(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    ((-1 * rank(stddev(high, 10))) * correlation(high, volume, 10))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=10)['volume']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=10)['high']

    #-1 * rank(  stddev(high, 10)  )
    series_01 = -1*rank_pool(stddev(high))

    #correlation(high, volume, 10)
    series_02 = correlation_pool(high,volume)

    return series_01*series_02


def alpha_041(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (((high * low)^0.5) - vwap)

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=1)['avg']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=1)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=1)['low']

    result = (high.iloc[0,:]*low.iloc[0,:])**0.5-vwap.iloc[0,:]

    return result


def alpha_042(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (rank((vwap - close)) / rank((vwap + close)))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=1)['avg']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=1)['close']

    result = rank_pool(vwap.iloc[0,:]-close.iloc[0,:])/rank_pool(vwap.iloc[0,:]+close.iloc[0,:])

    return result


def alpha_043(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (ts_rank((volume / adv20), 20) * ts_rank((-1 * delta(close, 7)), 8))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=39)['money']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=15)['close']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=20)['volume']

    #ts_rank(volume / adv20, 20)
    adv20 = adv(money,20,20)

    volume_adv_ratio = pd.DataFrame([],index=volume.index,columns=pool)
    for stock in pool:
        for i in range(len(volume.index)):
            try:
                volume_adv_ratio[stock].iloc[i] = volume[stock].iloc[i]/adv20[stock].iloc[i]
            except:
                volume_adv_ratio[stock].iloc[i] = 0

    series01 = ts_rank(volume_adv_ratio)

    #ts_rank(-1 * delta(close, 7), 8)
    delta_df = pd.DataFrame([],index=range(8),columns=pool)
    for i in range(8):
        delta_df.loc[i] = -1*delta(close.iloc[i:i+8],7)
    series02 = ts_rank(delta_df)

    return series01*series02


def alpha_044(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (-1 * correlation(high, rank(volume), 5))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=5)['high']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=5)['volume']

    rank_volume = pd.DataFrame([],index=range(5),columns=pool)
    for i in range(5):
        rank_volume.loc[i] = rank_pool(volume.iloc[i,:])

    result = -1*correlation_pool(high,rank_volume)


    return result


def alpha_045(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (-1 * ((rank((sum(delay(close, 5), 20) / 20)) * correlation(close, volume, 2))
    * rank(correlation(sum(close, 5), sum(close, 20), 2))))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=25)['close']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=2)['volume']

    #-1 * rank(  sum(   delay(close, 5), 20) / 20  )
    series01 = -1*rank_pool(mean(close.iloc[:20,:]))

    #correlation(close, volume, 2)
    series02 = correlation_pool(close.iloc[-2:,:],volume)

    #rank(     correlation(sum(close, 5), sum(close, 20), 2)   )
    sum_close_5 = pd.DataFrame([],index=range(2),columns=pool)
    sum_close_20 = pd.DataFrame([],index=range(2),columns=pool)
    for i in range(2):
        sum_close_5.loc[i] = sum(close.iloc[19+i:24+i,:])
        sum_close_20.loc[i] = sum(close.iloc[4+i:24+i,:])

    series03 = rank_pool(correlation_pool(sum_close_5,sum_close_20))

    return series01*series02*series03


def alpha_046(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
     ((0.25 < (((delay(close, 20) - delay(close, 10)) / 10) - ((delay(close, 10) - close) / 10)))
     ? (-1 * 1)
     : (((((delay(close, 20) - delay(close, 10)) / 10) - ((delay(close, 10) - close) / 10)) < 0)
     ? 1 : ((-1 * 1) * (close - delay(close, 1)))))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=21)['close']

    result = pd.Series([0.0]*len(pool),index=pool)

    #0.25 < (  delay(close, 20) - delay(close, 10)  ) / 10 - (delay(close, 10) - close) / 10
    for stock in pool:
        if (close[stock].iloc[0]-close[stock].iloc[-11])/10-(close[stock].iloc[-11]-close[stock].iloc[-1])/10>0.25:
            result[stock] = -1
        elif (close[stock].iloc[0]-close[stock].iloc[-11])/10-(close[stock].iloc[-11]-close[stock].iloc[-1])/10<0:
            result[stock] = 1
        else:
            result[stock] = -1*(close[stock].iloc[-1]-close[stock].iloc[-2])

    return result


def alpha_047(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
     ((((rank((1 / close)) * volume) / adv20) * ((high * rank((high - close))) / (sum(high, 5) / 5)))
     - rank((vwap - delay(vwap, 5))))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=1)['close']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=20)['money']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=1)['volume']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=5)['high']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=6)['avg']

    #rank(1 / close) * volume / adv20
    adv20 = adv(money,20,1)

    adv20_reciprocal = pd.Series([0.0]*len(pool),index=pool)
    close_reciprocal = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:
        try:
            close_reciprocal[stock] = 1/close[stock].iloc[-1]
            adv20_reciprocal[stock] = 1/adv20[stock].iloc[0]
        except:
            close_reciprocal[stock] = np.nan
            adv20_reciprocal[stock] = np.nan

    series01 = rank_pool(close_reciprocal)*volume.iloc[0,:]*adv20_reciprocal

    #(high * rank(   high - close  )  ) / (sum(high, 5) / 5)
    series02 = high.iloc[-1,:]*rank_pool(high.iloc[-1,:]-close.iloc[-1,:])/mean(high)

    #rank(  vwap - delay(vwap, 5)  )
    series03 = rank_pool(vwap.iloc[-1,:]-vwap.iloc[0,:])


    return series01*series02-series03


def alpha_049(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
     ((((rank((1 / close)) * volume) / adv20) * ((high * rank((high - close))) / (sum(high, 5) / 5)))
     - rank((vwap - delay(vwap, 5))))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=21)['close']

    #(  delay(close, 20) - delay(close, 10)  ) / 10 - (  delay(close, 10) - close) / 10 < -0.1
    result = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:
        if (close[stock].iloc[0]-close[stock].iloc[-11])/10-(close[stock].iloc[-11]-close[stock].iloc[-1])/10<-0.1:
            result[stock] = 1
        else:
            result[stock] = -1*(close[stock].iloc[-1]-close[stock].iloc[-2])

    return result


def alpha_050(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (-1 * ts_max(rank(correlation(rank(volume), rank(vwap), 5)), 5))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=9)['avg']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=9)['volume']

    #-1 * ts_max(   rank(   correlation(  rank(volume), rank(vwap)  , 5)  )   , 5)
    rank_df_volume = pd.DataFrame([],index=range(9),columns=pool)
    rank_df_vwap = pd.DataFrame([],index=range(9),columns=pool)
    for i in range(9):
        rank_df_volume.loc[i] = rank_pool(volume.iloc[i,:])
        rank_df_vwap.loc[i] = rank_pool(vwap.iloc[i,:])


    rank_df = pd.DataFrame([],index=range(5),columns=pool)
    for i in range(5):
        rank_df.loc[i] = rank_pool(correlation_pool(rank_df_volume.iloc[i:i+5,:],rank_df_vwap.iloc[i:i+5,:]))

    result = -1*ts_max(rank_df)


    return result


def alpha_051(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (((((delay(close, 20) - delay(close, 10)) / 10) - ((delay(close, 10) - close) / 10)) < (-1 * 0.05)) ?
    1 : ((-1 * 1) * (close - delay(close, 1))))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=21)['close']

    #(delay(close, 20) - delay(close, 10)) / 10 - (delay(close, 10) - close) / 10 < -0.05
    result = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:
        if (close[stock].iloc[0]-close[stock].iloc[-11])/10-(close[stock].iloc[-11]-close[stock].iloc[-1])/10<-0.05:
            result[stock] = 1
        else:
            result[stock] = -1*(close[stock].iloc[-1]-close[stock].iloc[-2])


    return result


def alpha_052(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
     ((((-1 * ts_min(low, 5)) + delay(ts_min(low, 5), 5)) * rank(((sum(returns, 240) - sum(returns, 20)) / 220)))
     * ts_rank(volume, 5))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=241)['close']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=10)['low']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=5)['volume']

    # (   -1 * ts_min(low, 5) + delay(   ts_min(low, 5)  , 5)  )
    ts_min_df = pd.DataFrame([],index=range(6),columns=pool)
    for i in range(6):
        ts_min_df.loc[i] = ts_min(low.iloc[i:i+5,:])

    series01 = -1*ts_min_df.iloc[-1,:]+ts_min_df.iloc[0,:]

    #rank(   (  sum(returns, 240) - sum(returns, 20)  ) / 220 )
    returns_df = returns(close)
    series02 = rank_pool((sum(returns_df)-sum(returns_df.iloc[-20:,:]))/220)

    #ts_rank(volume, 5)
    series03 = ts_rank(volume)


    return series01*series02*series03


def alpha_053(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (-1 * delta((((close - low) - (high - close)) / (close - low)), 9))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=10)['close']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=10)['low']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=10)['high']

    #-1 * delta(   (close*2 - low - high) / (close - low)   , 9)
    result = -1*delta((close*2-low-high)/(close-low),9)

    return result


def alpha_054(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    ((-1 * ((low - close) * (open^5))) / ((low - high) * (close^5)))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=1)['close']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=1)['open']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=1)['low']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=1)['high']

    #-1 * (low - close) * (open^5) / (  (low - high) * close^5  )
    result = -1*(low-close)*(openprice**5)/((low-high)*close**5)


    return result.iloc[0,:]


def alpha_055(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (-1 * correlation(rank(((close - ts_min(low, 12)) / (ts_max(high, 12) - ts_min(low, 12)))), rank(volume), 6))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=6)['volume']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=17)['low']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=17)['high']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=6)['close']

    rank_01_df = pd.DataFrame([],index=range(6),columns=pool)
    rank_volume = pd.DataFrame([],index=range(6),columns=pool)
    for i in range(6):
        rank_volume.loc[i] = rank_pool(volume.iloc[i,:])
        rank_01_df.loc[i] = rank_pool((close.iloc[i,:]-ts_min(low.iloc[i:i+12,:]))/(ts_max(high.iloc[i:i+12,:])-ts_min(low.iloc[i:i+12,:])))

    result = -1*correlation_pool(rank_volume,rank_01_df)

    return result


def alpha_056(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
     (0 - (1 * (rank((sum(returns, 10) / sum(sum(returns, 2), 3))) * rank((returns * cap)))))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=11)['close']


    #提取市值数据
    cap_series = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:
        try:
            cap_series[stock] = get_fundamentals(query(valuation.market_cap).filter(valuation.code==stock),date=enddate)['market_cap'].iloc[0]
        except:
            cap_series[stock] = np.nan


    #求 rank(returns * cap)
    returns_df = returns(close)
    series02 = rank_pool(returns_df.iloc[-1,:]*cap_series)


    #求 rank(sum(returns, 10) / sum(sum(returns, 2), 3))
    series01 = rank_pool(sum(returns_df)/sum(returns_df.iloc[-4:,:]))

    return -1*series02*series01


def alpha_057(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    0 - (close - vwap) / decay_linear(rank(ts_argmax(close, 30)), 2)

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=31)['close']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=1)['avg']

    numerator_series = close.ix[-1]-vwap.ix[-1]

    #求 decay_linear(rank(ts_argmax(close, 30)), 2)
    rank_dataframe = pd.DataFrame()
    for i in range(2):
        rank_dataframe = rank_dataframe.append(rank_pool(ts_argmax(close.ix[i:i+30])),ignore_index=True)

    denominator_series = decay_linear_pool(rank_dataframe)

    return -1*numerator_series/denominator_series


def alpha_060(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
     (0 - (1 * ((2 * scale(rank(((((close - low) - (high - close)) / (high - low)) * volume))))
     - scale(rank(ts_argmax(close, 10))))))

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        index成分股对应的因子的值
    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=10)['close']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=1)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=1)['low']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=1)['volume']

    #scale(rank(ts_argmax(close, 10)))
    temp2 = scale(rank_pool(ts_argmax(close)))

    #(  2*close - low - high  ) / (high - low)   * volume
    temp1_01 = (2*close.ix[-1]-low.ix[-1]-high.ix[-1])*volume.ix[-1]/(high.ix[-1]-low.ix[-1])
    temp1 = -2*scale(rank_pool(temp1_01))

    return temp1+temp2


def alpha_061(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (rank((vwap - ts_min(vwap, 16.1219))) < rank(correlation(vwap, adv180, 17.9282)))


    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        符合的股票对应值为1，不符合的股票对应值为-1
    '''

    pool = get_pool(index,enddate)


    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=18)['avg']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=197)['money']

    #获取adv180的DataFrame
    adv180 = adv(money,180,18)

    #求rank(  correlation(vwap, adv180, 18)  )的series
    temp2_series = rank_pool(correlation_pool(vwap,adv180))

    #求rank(  vwap - ts_min(vwap, 16)  )
    temp1_series = rank_pool(vwap.ix[-1]-ts_min(vwap.ix[-16:]))

    stock_series = pd.Series([0]*len(pool),index=pool)
    for stock in temp1_series.index:
        if temp1_series[stock]<temp2_series[stock]:
            stock_series[stock] = 1
        else:
            stock_series[stock] = -1

    return stock_series


def alpha_062(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    ((rank(correlation(vwap, sum(adv20, 22.4101), 9.91009)) < rank(((rank(open) + rank(open))
    < (rank(((high + low) / 2)) + rank(high))))) * -1)

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        符合的股票对应值为-1，不符合的股票对应值为1
    '''

    pool = get_pool(index,enddate)


    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=10)['avg']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=50)['money']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=1)['open']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=1)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=1)['low']

    #求adv20，含22行index
    for i in range(10):
        adv20 = adv(money.ix[i:i+41],20,22)
        money = money.append(sum(adv20.ix[:]),ignore_index=True)
    #求rank( correlation(vwap, sum(adv20, 22), 10) )的series
    temp1 = rank_pool(correlation_pool(vwap,money.ix[-10:]))


    #求rank((high + low) / 2) + rank(high)的series
    temp2_01 = rank_pool((high.ix[-1]+low.ix[-1])/2)+rank_pool(high.ix[-1])
    #求2*rank(open)
    temp2_02 = 2*rank_pool(openprice.ix[-1])

    temp2_series = pd.Series([0]*len(pool),index=pool)
    for stock in pool:
        if temp2_02[stock]<temp2_01[stock]:
            temp2_series[stock] = 1
        else:
            temp2_series[stock] = -1

    temp2 = rank_pool(temp2_series)

    series = pd.Series([0]*len(pool),index=pool)
    for stock in pool:
        if temp1[stock]<temp2[stock]:
            series[stock] = 1
        else:
            series[stock] = -1

    return series*-1


def alpha_064(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    ((rank(correlation(sum(((open * 0.178404) + (low * (1 - 0.178404))), 12.7054), sum(adv120, 12.7054), 16.6208))
    < rank(delta(((((high + low) / 2) * 0.178404) + (vwap * (1 - 0.178404))), 3.69741))) * -1)

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=31)['close']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=5)['avg']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=5)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=29)['low']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=29)['open']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=148)['money']


    #求rank(   delta(        (high + low) / 2 * 0.178404 + vwap * 0.821596        , 4)  )
    dataframe_temp2 = pd.DataFrame([],index=high.index,columns=high.columns)
    dataframe_temp2 = (high+low.ix[-5:])/2*0.178404+vwap*0.821596
    temp2 = rank_pool(delta(dataframe_temp2,4))


    #求rank(  correlation(   sum(    open * 0.178404 + low * 0.821596   ,13), sum(adv120, 13), 17      )     )

    sum_dataframe_17_01 = pd.DataFrame([],index=range(17),columns=high.columns)

    for i in range(17):
        for stock in high.columns:
            sum_dataframe_17_01[stock].ix[i] = sum(openprice[stock].ix[i:i+13])*0.178404+sum(low[stock].ix[i:i+13])*0.821596


    sum_dataframe_17_02 = pd.DataFrame([],index=range(17),columns=high.columns)

    adv120 = adv(money,120,29)
    for i in range(17):
        for stock in pool:
            sum_dataframe_17_02[stock].ix[i] = sum(adv120[stock].ix[i:i+13])

    temp1 = rank_pool(correlation_pool(sum_dataframe_17_01,sum_dataframe_17_02))

    series = pd.Series([0]*len(pool),index=pool)
    for stock in pool:
        if temp1[stock]<temp2[stock]:
            series[stock] = 1
        else:
            series[stock] = -1

    return series*-1


def alpha_065(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    ((rank(correlation(((open * 0.00817205) + (vwap * (1 - 0.00817205))), sum(adv60, 8.6911), 6.40374))
    < rank((open - ts_min(open, 13.635)))) * -1)

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=6)['avg']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=73)['money']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=14)['open']

    #rank(  open - ts_min(open, 14)  )
    temp2 = rank_pool(openprice.ix[-1]-ts_min(openprice))

    #rank(   correlation(   open * 0.00817205 + vwap * 0.99182795, sum(adv60, 9), 6  )  )
    dataframe01 = pd.DataFrame([],index=range(6),columns=vwap.columns)
    for i in range(6):
        dataframe01.ix[i] = openprice.ix[i]*0.00817205+vwap.ix[i]*0.99182795


    adv60 = adv(money,60,14)
    dataframe02 = pd.DataFrame([],index=range(6),columns=vwap.columns)
    for i in range(6):
        for stock in pool:
            dataframe02[stock].ix[i] =sum(adv60[stock].ix[i:i+9])

    temp1 = rank_pool(correlation_pool(dataframe01,dataframe02))

    series = pd.Series([0]*len(pool),index=pool)
    for stock in pool:
        if temp1[stock]<temp2[stock]:
            series[stock] = 1
        else:
            series[stock] = -1

    return series*-1


def alpha_066(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    ((rank(decay_linear(delta(vwap, 3.51013), 7.23052)) + Ts_Rank(decay_linear(((((low * 0.96633)
    + (low * (1 - 0.96633))) - vwap) / (open - ((high + low) / 2))), 11.4157), 6.72611)) * -1)

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=17)['avg']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=17)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=17)['low']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=17)['open']


    #rank(decay_linear(delta(vwap, 4), 7))
    dataframe1 = pd.DataFrame([],index=range(7),columns=pool)
    for i in range(7):
        dataframe1.ix[i] = delta(vwap.ix[6+i:i+11],4)
    temp1 = rank_pool(decay_linear_pool(dataframe1))


    #Ts_Rank(   decay_linear(    (low - vwap) / (open - (high + low) / 2) , 11  )  , 7   )
    dataframe2 = pd.DataFrame([],index=range(7),columns=pool)
    for i in range(7):

        dataframe3 = pd.DataFrame([],index=range(11),columns=pool)
        for j in range(11):
                dataframe3.loc[j] = (low.iloc[i+j,:]-vwap.iloc[i+j,:])/(openprice.iloc[i+j,:]-(high.iloc[i+j,:]+low.iloc[i+j,:])/2)

        dataframe2.loc[i] = decay_linear_pool(dataframe3)
    temp2 = ts_rank(dataframe2)


    return -1*(temp1+temp2)



def alpha_068(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    ((Ts_Rank(correlation(rank(high), rank(adv15), 8.91644), 13.9333)
    < rank(delta(((close * 0.518371) + (low * (1 - 0.518371))), 1.06157))) * -1)

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=36)['money']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=22)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=2)['low']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=2)['close']

    #Ts_Rank(    correlation(  rank(high)  , rank(adv15), 9)   , 14)
    correlation_frame = pd.DataFrame([],index=range(14),columns=high.columns)
    adv15 = adv(money,15,22)
    for i in range(14):

        rank_high_frame = pd.DataFrame([],index=range(9),columns=high.columns)
        rank_adv_frame = pd.DataFrame([],index=range(9),columns=high.columns)
        for j in range(9):
            rank_high_frame.ix[j] = rank_pool(high.ix[i+j])
            rank_adv_frame.ix[j] = rank_pool(adv15.ix[i+j])

        correlation_frame.ix[i] = correlation_pool(rank_high_frame,rank_adv_frame)

    temp1 = ts_rank(correlation_frame)

    #rank(   delta(  (close * 0.518371 + low * (1 - 0.518371))  , 1)    )
    dataframe_2 = pd.DataFrame([],index=range(2),columns=high.columns)
    for i in range(2):
        dataframe_2.ix[i] = close.ix[i]*0.518371+low.ix[i]*(1-0.518371)
    temp2 = rank_pool(delta(dataframe_2,1))

    series = pd.Series([0]*len(pool),index=pool)
    for stock in pool:
        if temp1[stock]<temp2[stock]:
            series[stock] = 1
        else:
            series[stock] = -1

    return -1*series


def alpha_071(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    max(  Ts_Rank(decay_linear(correlation(Ts_Rank(close, 3.43976), Ts_Rank(adv180, 12.0647), 18.0175), 4.20501), 15.6948),
        Ts_Rank(decay_linear((rank(((low + open) - (vwap + vwap)))^2), 16.4662), 4.4388))

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=226)['money']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=19)['open']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=19)['low']
    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=38)['close']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=19)['avg']

    #Ts_Rank(   decay_linear(    rank(   low + open - vwap*2  )^2    , 16)    , 4)
    rank_dataframe = pd.DataFrame([],index=range(19),columns=pool)
    for i in range(19):
        rank_dataframe.iloc[i,:] = rank_pool(low.iloc[i,:]+openprice.iloc[i,:]-vwap.iloc[i,:]*2)**2

    decay_dataframe = pd.DataFrame([],index=range(4),columns=pool)
    for i in range(4):
        decay_dataframe.iloc[i,:] = decay_linear_pool(rank_dataframe.iloc[i:i+16,:])
    temp2 = ts_rank(decay_dataframe)

    #Ts_Rank(  decay_linear(   correlation(    Ts_Rank(close, 3), Ts_Rank(adv180, 12)   , 18)    , 4)   ,16   )
    adv180 = adv(money,180,47)
    ts_rank_close_dataframe = pd.DataFrame([],index=range(36),columns=pool)
    ts_rank_adv180_dataframe = pd.DataFrame([],index=range(36),columns=pool)
    for i in range(36):
        ts_rank_close_dataframe.iloc[i,:] = ts_rank(close.iloc[i:i+3,:])
        ts_rank_adv180_dataframe.iloc[i,:] = ts_rank(adv180.iloc[i:i+12,:])

    correlation_dataframe = pd.DataFrame([],index=range(19),columns=pool)
    for i in range(19):
        correlation_dataframe.loc[i] = correlation_pool(ts_rank_close_dataframe.iloc[i:i+18,:],ts_rank_adv180_dataframe.iloc[i:i+18,:])

    decay_dataframe_01 = pd.DataFrame([],index=range(16),columns=pool)
    for i in range(16):
        decay_dataframe_01.iloc[i,:] = decay_linear_pool(correlation_dataframe.iloc[i:i+4])

    temp1 = ts_rank(decay_dataframe_01)

    result = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:
        result[stock] = max(temp1[stock],temp2[stock])

    return result


def alpha_072(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (rank(decay_linear(correlation(((high + low) / 2), adv40, 8.93345), 10.1519)) /
    rank(decay_linear(correlation(Ts_Rank(vwap, 3.72469), Ts_Rank(volume, 18.5188), 6.86671), 2.95011)))

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=57)['money']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=18)['low']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=18)['high']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=27)['volume']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=12)['avg']

    #rank(       decay_linear(      correlation(   (high + low) / 2, adv40, 9)   , 10)      )
    high_plus_low = (high+low)/2
    adv40 = adv(money,40,18)
    correlation_dataframe = pd.DataFrame([],index=range(10),columns=pool)
    for i in range(10):
        correlation_dataframe.loc[i] = correlation_pool(high_plus_low.iloc[i:i+9,:],adv40.iloc[i:i+9,:])

    temp1 = rank_pool(decay_linear_pool(correlation_dataframe))

    #rank(   decay_linear(      correlation(      Ts_Rank(vwap, 4), Ts_Rank(volume, 19)    , 7)     , 3)    )
    ts_rank_vwap = pd.DataFrame([],index=range(9),columns=pool)
    ts_rank_volume = pd.DataFrame([],index=range(9),columns=pool)
    for i in range(9):
        ts_rank_vwap.loc[i] = ts_rank(vwap.iloc[i:i+4,:])
        ts_rank_volume.loc[i] = ts_rank(volume.iloc[i:i+19,:])

    correlation_dataframe = pd.DataFrame([],index=range(3),columns=pool)
    for i in range(3):
        correlation_dataframe.loc[i] = correlation_pool(ts_rank_vwap.iloc[i:i+7,:],ts_rank_volume.iloc[i:i+7,:])

    temp2 = rank_pool(decay_linear_pool(correlation_dataframe))

    return temp1/temp2


def alpha_073(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (max(rank(decay_linear(delta(vwap, 4.72775), 2.91864)),
    Ts_Rank(decay_linear(((delta(((open * 0.147155) + (low * (1 - 0.147155))), 2.03608) / ((open * 0.147155)
    + (low * (1 - 0.147155)))) * -1), 3.33829), 16.7411)) * -1)

    Inputs:
        enddate: 查询日期
        index: 股票池
    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=21)['open']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=21)['low']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=8)['avg']

    #rank(   decay_linear(  delta(vwap, 5), 3)   ),
    delta_vwap = pd.DataFrame([],index=range(3),columns=pool)
    for i in range(3):
        delta_vwap.loc[i] = delta(vwap.iloc[i:i+6,:],5)

    temp1 = rank_pool(decay_linear_pool(delta_vwap))


    #Ts_Rank(   decay_linear(    (   delta( open * 0.147155 + low * (1 - 0.147155), 2) /
    #(open * 0.147155 + low * (1 - 0.147155))   ) * (-1)   , 3)   , 17)
    delta_dataframe = pd.DataFrame([],index=range(19),columns=pool)
    frame_01 = openprice * 0.147155 + low * (1 - 0.147155)
    for i in range(19):
        delta_dataframe.loc[i] = delta(frame_01.iloc[i:i+3,:],2)

    frame_02 = frame_01.iloc[-19:,:]
    frame_02.index=delta_dataframe.index
    decay_linear_frame = pd.DataFrame([],index=range(17),columns=pool)
    for i in range(17):
        decay_linear_frame.loc[i] = decay_linear_pool(delta_dataframe.iloc[i:i+3,:]/(-1*frame_02.iloc[i:i+3,:]))

    temp2 = ts_rank(decay_linear_frame)

    result = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:
        result[stock] = max(temp1[stock],temp2[stock])*(-1)

    return result


def alpha_074(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
     ((rank(correlation(close, sum(adv30, 37.4843), 15.1365)) <
     rank(correlation(rank(((high * 0.0261661) + (vwap * (1 - 0.0261661)))), rank(volume), 11.4791))) * -1)

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=15)['close']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=11)['high']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=11)['volume']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=80)['money']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=11)['avg']

    #rank(    correlation(close, sum(adv30, 37), 15)     )
    adv30 = adv(money,30,51)
    sum_frame = pd.DataFrame([],index=range(15),columns = pool)
    for i in range(15):
        sum_frame.loc[i] = sum(adv30.iloc[i:i+37,:])
    temp1 = rank_pool(correlation_pool(close,sum_frame))

    #rank(      correlation(   rank(  high * 0.0261661 + vwap * (1 - 0.0261661)   )    , rank(volume)     , 11)    )
    plus_frame = high * 0.0261661 + vwap * (1 - 0.0261661)
    rank_plus_df = pd.DataFrame([],index=range(11),columns = pool)
    rank_volume_df = pd.DataFrame([],index=range(11),columns = pool)
    for i in range(11):
        rank_plus_df.loc[i] = rank_pool(plus_frame.iloc[i,:])
        rank_volume_df.loc[i] = rank_pool(volume.iloc[i,:])

    temp2 = rank_pool(correlation_pool(rank_plus_df,rank_volume_df))

    result = pd.Series([0]*len(pool),index=pool)
    for stock in pool:
        if temp1[stock]<temp2[stock]:
            result[stock] = 1
        else:
            result[stock] = -1

    return -1*result


def alpha_075(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    (rank(correlation(vwap, volume, 4.24304)) < rank(correlation(rank(low), rank(adv50), 12.4413)))

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        一个Series：index为成分股代码，values为1或-1，当满足条件时为1，否则为-1

    '''

    pool = get_pool(index,enddate)

    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=61)['money']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=12)['low']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=4)['avg']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=4)['volume']

    #rank(    correlation(vwap, volume, 4)   )
    temp1 = rank_pool(correlation_pool(vwap,volume))

    #rank(   correlation(    rank(low), rank(adv50)   , 12)   )
    adv50 = adv(money,50,12)
    rank_low_df = pd.DataFrame([],index=range(12),columns=pool)
    rank_adv50_df = pd.DataFrame([],index=range(12),columns=pool)
    for i in range(12):
        rank_low_df.loc[i] = rank_pool(low.iloc[i,:])
        rank_adv50_df.loc[i] = rank_pool(adv50.iloc[i,:])

    temp2 = rank_pool(correlation_pool(rank_low_df,rank_adv50_df))

    result = pd.Series([0]*len(pool),index=pool)
    for stock in pool:
        if temp1[stock]<temp2[stock]:
            result[stock] = 1
        else:
            result[stock] = -1

    return result


def alpha_077(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    min(rank(decay_linear(((((high + low) / 2) + high) - (vwap + high)), 20.0451)),
    rank(decay_linear(correlation(((high + low) / 2), adv40, 3.1614), 5.64125)))

    Inputs:
        enddate: 查询日期
        index:股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=47)['money']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=20)['low']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=20)['high']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=20)['avg']

    #rank(   decay_linear(    (high + low) / 2 + high*2 - vwap , 20)   )
    df_01 = (high+low)/2+2*high-vwap
    temp1 = rank_pool(decay_linear_pool(df_01))

    #rank(    decay_linear(   correlation(  (high + low) / 2, adv40, 3)    , 6)    )
    adv40 = adv(money,40,8)
    df_01 = (high+low)/2
    correlation_df = pd.DataFrame([],index=range(6),columns = pool)
    for i in range(6):
        correlation_df.loc[i] = correlation_pool(adv40.iloc[i:i+3,:],df_01.iloc[-8:,:].iloc[i:i+3,:])
    temp2 = rank_pool(decay_linear_pool(correlation_df))

    result = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:
        result[stock] = min(temp1[stock],temp2[stock])

    return result


def alpha_078(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
     (rank(correlation(sum(((low * 0.352233) + (vwap * (1 - 0.352233))), 19.7428),
     sum(adv40, 19.7428), 6.83313))^rank(correlation(rank(vwap), rank(volume), 5.77492)))

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=65)['money']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=26)['low']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=6)['volume']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=26)['avg']

    #rank(    correlation(   sum(low * 0.352233 + vwap * (1 - 0.352233), 20), sum(adv40, 20)   , 7)   )
    df_01 = low * 0.352233 + vwap * (1 - 0.352233)
    sum_df = pd.DataFrame([],index=range(7),columns=pool)
    for i in range(7):
        sum_df.loc[i] = sum(df_01.iloc[i:i+20,:])

    adv40 = adv(money,40,26)
    sum_df_2= pd.DataFrame([],index=range(7),columns=pool)
    for i in range(7):
        sum_df_2.loc[i] = sum(adv40.iloc[i:i+20,:])

    temp1 = rank_pool(correlation_pool(sum_df_2,sum_df))

    #rank(    correlation(rank(vwap), rank(volume), 6)   )
    rank_vwap_df = pd.DataFrame([],index=range(6),columns=pool)
    rank_volume_df = pd.DataFrame([],index=range(6),columns=pool)
    for i in range(6):
        rank_vwap_df.loc[i] = rank_pool(vwap.iloc[-6:,:].iloc[i,:])
        rank_volume_df.loc[i] = rank_pool(volume.iloc[i,:])

    temp2 = rank_pool(correlation_pool(rank_vwap_df,rank_volume_df))

    result = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:
        result[stock] = temp1[stock]**temp2[stock]

    return result


def alpha_083(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
     ((rank(delay(((high - low) / (sum(close, 5) / 5)), 2)) * rank(rank(volume)))
     / (((high - low) / (sum(close, 5) / 5)) / (vwap - close)))

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=7)['close']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=3)['low']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=3)['high']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=1)['volume']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=1)['avg']

    #rank(rank(volume))
    temp2 = rank_pool(rank_pool(volume.iloc[0,:]))

    #rank(   delay(   (high - low) / mean（close,5)   , 2)    )
    series_1 = high.iloc[0,:]-low.iloc[0,:]
    series_2 = mean(close.iloc[:5,:])
    temp1 = rank_pool(series_1/series_2)

    #(   (high - low) / mean(close,5)  ) / (vwap - close)
    series_1 = high.iloc[-1,:]-low.iloc[-1,:]
    series_2 = mean(close.iloc[-5:,:])
    series_3 = vwap.iloc[-1,:]-close.iloc[-1,:]
    temp3 = series_1/(series_2*series_3)

    return temp1*temp2/temp3


def alpha_084(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：

    SignedPower(Ts_Rank((vwap - ts_max(vwap, 15.3217)), 20.7127), delta(close, 4.96796))

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=6)['close']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=35)['avg']

    # delta(close, 5)
    temp2 = delta(close,5)

    # Ts_Rank(    vwap - ts_max(vwap, 15), 21    )
    minus_df = pd.DataFrame([],index=range(21),columns=pool)
    for i in range(21):
        minus_df.loc[i] = vwap.iloc[i+14,:]-ts_max(vwap.iloc[i:i+15,:])
    temp1 = ts_rank(minus_df)

    result = signedpower(temp1,temp2)

    return result


def alpha_085(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：

    (rank(correlation(((high * 0.876703) + (close * (1 - 0.876703))), adv30, 9.61331))
    ^rank(correlation(Ts_Rank(((high + low) / 2), 3.70596), Ts_Rank(volume, 10.1595), 7.11408)))

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=10)['close']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=10)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=10)['low']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=39)['money']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=16)['volume']

    #rank(     correlation(     high * 0.876703 + close * (1 - 0.876703)   , adv30, 10)     )
    plus_df = high * 0.876703 + close * (1 - 0.876703)
    adv30 = adv(money,30,10)
    temp1 = rank_pool(correlation_pool(plus_df,adv30))

    #rank(     correlation(     Ts_Rank(   (high + low) / 2, 4),   Ts_Rank(volume, 10)     , 7)    )
    df = (high+low)/2
    ts_rank_01_df = pd.DataFrame([],index=range(7),columns=pool)
    ts_rank_02_df = pd.DataFrame([],index=range(7),columns=pool)
    for i in range(7):
        ts_rank_01_df.loc[i] = ts_rank(df.iloc[i:i+4,:])
        ts_rank_02_df.loc[i] = ts_rank(volume.iloc[i:i+10,:])
    temp2 = rank_pool(correlation_pool(ts_rank_01_df,ts_rank_02_df))

    result = signedpower(temp1,temp2)

    return result


def alpha_086(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：

    ((Ts_Rank(correlation(close, sum(adv20, 14.7444), 6.00049), 20.4195) < rank(((open + close) - (vwap + open)))) * -1)

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=25)['close']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=58)['money']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=1)['avg']

    #rank(close - vwap)
    temp2 = rank_pool(close.iloc[-1,:]-vwap.iloc[-1,:])

    #Ts_Rank(    correlation(   close, sum(adv20, 15)   , 6)    , 20   )
    adv20 = adv(money,20,39)
    sum_adv20 = pd.DataFrame([],index=range(25),columns=pool)
    for i in range(25):
        sum_adv20.loc[i] = sum(adv20.iloc[i:i+15,:])

    correlation_df = pd.DataFrame([],index=range(20),columns=pool)
    for i in range(20):
        correlation_df.loc[i] = correlation_pool(close.iloc[i:i+6,:],sum_adv20.iloc[i:i+6,:])

    temp1 = ts_rank(correlation_df)

    result = pd.Series([0]*len(pool),index=pool)
    for stock in pool:
        if temp1[stock]<temp2[stock]:
            result[stock] = 1
        else:
            result[stock] = -1

    return result*-1



def alpha_088(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：

    min(rank(decay_linear(((rank(open) + rank(low)) - (rank(high) + rank(close))),
    8.06882)), Ts_Rank(decay_linear(correlation(Ts_Rank(close, 8.44728), Ts_Rank(adv60, 20.6966), 8.01266), 6.65053), 2.61957))

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=23)['close']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=8)['open']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=8)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=8)['low']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=94)['money']

    #rank(   decay_linear(  rank(open) + rank(low) - rank(high) - rank(close)     , 8)   )
    rank_open_df = pd.DataFrame([],index=range(8),columns=pool)
    rank_low_df = pd.DataFrame([],index=range(8),columns=pool)
    rank_high_df = pd.DataFrame([],index=range(8),columns=pool)
    rank_close_df = pd.DataFrame([],index=range(8),columns=pool)
    for i in range(8):
        rank_open_df.loc[i] = rank_pool(openprice.iloc[i,:])
        rank_low_df.loc[i] = rank_pool(low.iloc[i,:])
        rank_high_df.loc[i] = rank_pool(high.iloc[i,:])
        rank_close_df.loc[i] = rank_pool(close.iloc[-8+i,:])
    temp1 = rank_pool(decay_linear_pool(rank_open_df+rank_low_df-rank_high_df-rank_close_df))

    #Ts_Rank(   decay_linear(    correlation(  Ts_Rank(close, 8), Ts_Rank(adv60, 20), 8)    , 7)   , 3)
    adv60 = adv(money,60,35)
    ts_rank_close_df = pd.DataFrame([],index=range(16),columns=pool)
    ts_rank_adv60_df = pd.DataFrame([],index=range(16),columns=pool)
    for i in range(16):
        ts_rank_close_df.loc[i] = ts_rank(close.iloc[i:i+8,:])
        ts_rank_adv60_df.loc[i] = ts_rank(adv60.iloc[i:i+20,:])

    correlation_df = pd.DataFrame([],index=range(9),columns=pool)
    for i in range(9):
        correlation_df.loc[i] = correlation_pool(ts_rank_close_df.iloc[i:i+8,:],ts_rank_adv60_df.iloc[i:i+8,:])

    decay_linear_df = pd.DataFrame([],index=range(3),columns=pool)
    for i in range(3):
        decay_linear_df.loc[i] = decay_linear_pool(correlation_df.iloc[i:i+7,:])

    temp2 = ts_rank(decay_linear_df)

    result = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:
        result[stock] = min(temp1[stock],temp2[stock])

    return result



def alpha_092(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：

    min(Ts_Rank(decay_linear(((((high + low) / 2) + close) < (low + open)), 14.7221),
    18.8683), Ts_Rank(decay_linear(correlation(rank(low), rank(adv30), 7.58555), 6.94024), 6.80584))

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=33)['close']
    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=33)['open']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=33)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=33)['low']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=49)['money']

    #Ts_Rank(   decay_linear(     (high + low) / 2 + close < low + open    , 15)       , 19   )
    compare_01 = (high+low)/2+close
    compare_02 = low+openprice
    df_01 = pd.DataFrame([],index=range(33),columns=pool)
    for stock in pool:

        for i in range(33):
            if compare_01[stock].iloc[i]<compare_02[stock].iloc[i]:
                df_01[stock].loc[i] = 1
            else:
                df_01[stock].loc[i] = -1

    decay_df = pd.DataFrame([],index=range(19),columns=pool)
    for i in range(19):
        decay_df.loc[i] = decay_linear_pool(df_01.iloc[i:i+15,:])

    temp1 = ts_rank(decay_df)

    #Ts_Rank(      decay_linear(     correlation(rank(low), rank(adv30), 8)     , 7)    , 7)
    adv30 = adv(money,30,20)
    rank_low = pd.DataFrame([],index=range(20),columns=pool)
    rank_adv30 = pd.DataFrame([],index=range(20),columns=pool)
    for i in range(20):
        rank_low.loc[i] = rank_pool(low.iloc[i+13,:])
        rank_adv30.loc[i] = rank_pool(adv30.iloc[i,:])

    correlation_df = pd.DataFrame([],index=range(13),columns=pool)
    for i in range(13):
        correlation_df.loc[i] = correlation_pool(rank_low.iloc[i:i+8,:],rank_adv30.iloc[i:i+8,:])

    decay_df2 = pd.DataFrame([],index=range(7),columns=pool)
    for i in range(7):
        decay_df2.loc[i] = decay_linear_pool(correlation_df.iloc[i:i+7,:])

    temp2 = ts_rank(decay_df2)

    result = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:
        result[stock] = min(temp1[stock],temp2[stock])

    return result


def alpha_094(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：

    ((rank((vwap - ts_min(vwap, 11.5783)))
    ^Ts_Rank(correlation(Ts_Rank(vwap, 19.6462), Ts_Rank(adv60, 4.02992), 18.0926), 2.70756)) * -1)

    Inputs:
        index: 股票池
        enddate: 查询日期

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=39)['avg']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=82)['money']

    #rank(    vwap - ts_min(vwap, 12)   )
    series_01 = vwap.iloc[-1,:]-ts_min(vwap.iloc[-12:,:])
    temp1 = rank_pool(series_01)

    #Ts_Rank(    correlation(     Ts_Rank(vwap, 20), Ts_Rank(adv60, 4)   , 18)     , 3)
    adv60 = adv(money,60,23)
    ts_rank_vwap = pd.DataFrame([],index=range(20),columns=pool)
    ts_rank_adv60 = pd.DataFrame([],index=range(20),columns=pool)
    for i in range(20):
        ts_rank_vwap.loc[i] = ts_rank(vwap.iloc[i:i+20,:])
        ts_rank_adv60.loc[i] = ts_rank(adv60.iloc[i:i+4,:])

    correlation_df = pd.DataFrame([],index=range(3),columns=pool)
    for i in range(3):
        correlation_df.loc[i] = correlation_pool(ts_rank_vwap.iloc[i:i+18,:],ts_rank_adv60.iloc[i:i+18,:])

    temp2 = ts_rank(correlation_df)

    return -1*signedpower(temp1,temp2)


def alpha_095(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：

    (rank((open - ts_min(open, 12.4105))) < Ts_Rank((rank(correlation(sum(((high + low) / 2), 19.1351), sum(adv40, 19.1351), 12.8742))^5), 11.7584))


    Inputs:
        index: 股票池
        enddate: 查询日期

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=12)['open']
    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=42)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=42)['low']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=81)['money']

    #rank(   open - ts_min(open, 12)  )
    series_01 = openprice.iloc[-1,:]-ts_min(openprice)
    temp1 = rank_pool(series_01)

    #Ts_Rank(    rank(    correlation(      sum((high + low) / 2, 19), sum(adv40, 19)    , 13)  )   ^5     , 12)
    adv40 = adv(money,40,42)
    df_01 = (high+low)/2
    sum_df_01 = pd.DataFrame([],index=range(24),columns=pool)
    sum_df_02 = pd.DataFrame([],index=range(24),columns=pool)
    for i in range(24):
        sum_df_01.loc[i] = sum(df_01.iloc[i:i+19,:])
        sum_df_02.loc[i] = sum(adv40.iloc[i:i+19,:])

    rank_df = pd.DataFrame([],index=range(12),columns=pool)
    for i in range(12):
        rank_df.loc[i] = rank_pool(correlation_pool(sum_df_01.iloc[i:i+13,:],sum_df_02.iloc[i:i+13,:]))**5

    temp2 = ts_rank(rank_df)

    result = pd.Series([0]*len(pool),index=pool)
    for stock in pool:
        if temp1[stock]<temp2[stock]:
            result[stock] = 1
        else:
            result[stock] = -1

    return result


def alpha_096(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：

    (max(Ts_Rank(decay_linear(correlation(rank(vwap), rank(volume), 3.83878), 4.16783), 8.38151),
    Ts_Rank(decay_linear(Ts_ArgMax(correlation(Ts_Rank(close, 7.45404), Ts_Rank(adv60, 4.13242), 3.65459), 12.6556), 14.0365), 13.4143)) * -1)

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=47)['close']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=14)['volume']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=103)['money']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=14)['avg']



    #Ts_Rank(      decay_linear(      correlation(rank(vwap), rank(volume), 4)   , 4)   , 8)

    rank_vwap = pd.DataFrame([],index=range(14),columns=pool)
    for i in range(14):
        rank_vwap.loc[i] = rank_pool(vwap.iloc[i,:])

    rank_volume = pd.DataFrame([],index=range(14),columns=pool)
    for i in range(14):
        rank_volume.loc[i] = rank_pool(volume.iloc[i,:])

    correlation_df = pd.DataFrame([],index=range(11),columns=pool)
    for i in range(11):
        correlation_df.loc[i] = correlation_pool(rank_vwap.iloc[i:i+4,:],rank_volume.iloc[i:i+4,:])


    decay_df = pd.DataFrame([],index=range(8),columns=pool)
    for i in range(8):
        decay_df.loc[i] = decay_linear_pool(correlation_df.iloc[i:i+4,:])

    temp1 = ts_rank(decay_df)



    #Ts_Rank(   decay_linear(     Ts_ArgMax(  correlation(    Ts_Rank(close, 7), Ts_Rank(adv60, 4), 4)   , 13)    , 14)     , 13)
    adv60 = adv(money,60,44)

    ts_rank_close = pd.DataFrame([],index=range(41),columns=pool)
    for i in range(41):
        ts_rank_close.loc[i] = ts_rank(close.iloc[i:i+7,:])

    ts_rank_adv60 = pd.DataFrame([],index=range(41),columns=pool)
    for i in range(41):
        ts_rank_adv60.loc[i] = ts_rank(adv60.iloc[i:i+4,:])


    correlation_df_2 = pd.DataFrame([],index=range(38),columns=pool)
    for i in range(38):
        correlation_df_2.loc[i] = correlation_pool(ts_rank_close.iloc[i:i+4,:],ts_rank_adv60.iloc[i:i+4,:])

    ts_argmax_df = pd.DataFrame([],index=range(26),columns=pool)
    for i in range(26):
        ts_argmax_df.loc[i] = ts_argmax(correlation_df_2.iloc[i:i+13,:])

    decay_df_2 = pd.DataFrame([],index=range(13),columns=pool)
    for i in range(13):
        decay_df_2.loc[i] = decay_linear_pool(ts_argmax_df.iloc[i:i+14,:])

    temp2 = ts_rank(decay_df_2)

    result = pd.Series([0.0]*len(pool),index=pool)
    for stock in pool:
        result[stock] = max(temp1[stock],temp2[stock])

    return result*-1


def alpha_098(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：

    (rank(decay_linear(correlation(vwap, sum(adv5, 26.4719), 4.58418), 7.18088)) -
    rank(decay_linear(Ts_Rank(Ts_ArgMin(correlation(rank(open), rank(adv15), 20.8187), 8.62571), 6.95668), 8.07206)))

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=41)['open']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=55)['money']
    vwap = get_price(pool,end_date = enddate,frequency='daily',fields=['avg'],count=11)['avg']



    #rank(     decay_linear(     correlation(vwap, sum(adv5, 26), 5)   , 7)   )
    adv5 = adv(money.iloc[-40:,:],5,36)

    sum_adv5 = pd.DataFrame([],index=range(11),columns=pool)
    for i in range(11):
        sum_adv5.loc[i] = sum(adv5.iloc[i:i+26,:])


    correlation_df = pd.DataFrame([],index=range(7),columns=pool)
    for i in range(7):
        correlation_df.loc[i] = correlation_pool(vwap.iloc[i:i+5,:],sum_adv5.iloc[i:i+5,:])

    temp1 = rank_pool(decay_linear_pool(correlation_df))



    #rank(   decay_linear(   Ts_Rank(    Ts_ArgMin(     correlation(rank(open), rank(adv15), 20)    , 9)    , 7)   , 8)    )
    adv15 = adv(money,15,41)

    rank_open_df = pd.DataFrame([],index=range(41),columns=pool)
    for i in range(41):
        rank_open_df.loc[i] = rank_pool(openprice.iloc[i,:])

    rank_adv15_df = pd.DataFrame([],index=range(41),columns=pool)
    for i in range(41):
        rank_adv15_df.loc[i] = rank_pool(adv15.iloc[i,:])

    correlation_df_2 = pd.DataFrame([],index=range(22),columns=pool)
    for i in range(22):
        correlation_df_2.loc[i] = correlation_pool(rank_open_df.iloc[i:i+20,:],rank_adv15_df.iloc[i:i+20,:])

    ts_argmin_df = pd.DataFrame([],index=range(14),columns=pool)
    for i in range(14):
        ts_argmin_df.loc[i] = ts_argmin(correlation_df_2.iloc[i:i+9,:])

    ts_rank_df = pd.DataFrame([],index=range(8),columns=pool)
    for i in range(8):
        ts_rank_df.loc[i] = ts_rank(ts_argmin_df.iloc[i:i+7,:])
    temp2 = rank_pool(decay_linear_pool(ts_rank_df))

    return temp1-temp2


def alpha_099(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：

    ((rank(correlation(sum(((high + low) / 2), 19.8975), sum(adv60, 19.8975), 8.8136))
    < rank(correlation(low, volume, 6.28259))) * -1)

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    pool = get_pool(index,enddate)

    high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=28)['high']
    low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=28)['low']
    money = get_price(pool,end_date = enddate,frequency='daily',fields=['money'],count=87)['money']
    volume = get_price(pool,end_date = enddate,frequency='daily',fields=['volume'],count=6)['volume']

    #rank(     correlation(    sum((high + low) / 2, 20), sum(adv60, 20)   , 9)   )
    df_01 = (high+low)/2
    adv60 = adv(money,60,28)
    sum_df01 = pd.DataFrame([],index=range(9),columns=pool)
    sum_adv60 = pd.DataFrame([],index=range(9),columns=pool)
    for i in range(9):
        sum_df01.loc[i] = sum(df_01.iloc[i:i+20,:])
        sum_adv60.loc[i] = sum(adv60.iloc[i:i+20,:])

    temp1 = rank_pool(correlation_pool(sum_df01,sum_adv60))

    #rank(    correlation(low, volume, 6)  )
    temp2 = rank_pool(correlation_pool(low.iloc[-6:,:],volume))

    result = pd.Series([0]*len(pool),index=pool)
    for stock in pool:
        if temp1[stock]<temp2[stock]:
            result[stock] = 1
        else:
            result[stock] = -1

    return result*-1


def alpha_101(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):

    '''
    公式：
    ((close - open) / ((high - low) + .001))

    Inputs:
        enddate: 查询日期
        index: 股票池

    Outputs:
        因子的值

    '''

    #pool = get_pool(index,enddate)

    #high = get_price(pool,end_date = enddate,frequency='daily',fields=['high'],count=1)['high']
    #close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=1)['close']
    #low = get_price(pool,end_date = enddate,frequency='daily',fields=['low'],count=1)['low']
    #openprice = get_price(pool,end_date = enddate,frequency='daily',fields=['open'],count=1)['open']

    high = get_price(pool, begin_date, end_date, 'high', 1, plat_form_type)
    close = get_price(pool, begin_date, end_date, 'close', 1, plat_form_type)
    low = get_price(pool, begin_date, end_date, 'low', 1, plat_form_type)
    openprice = get_price(pool, begin_date, end_date, 'open', 1, plat_form_type)

    result = (close-openprice)/((high-low)+.001)

    return result.iloc[0,:]

if __name__ == '__main__':
    import QUANTAXIS as QA
    pool = ['000001', '000002', '000005']
    res = alpha_001(pool, '2018-01-01', '2018-06-30')
    print(res)
    res = alpha_101(pool, '2018-01-01', '2018-06-30')
    print(res)
