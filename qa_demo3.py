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

def get_stock_day(enddate, code):
    return QA.QA_fetch_stock_day_adv(code, '2018-01-01', enddate)

def get_index_day(enddate, index):
    return QA.QA_fetch_index_day_adv(index, '2018-01-01', enddate)

###################### 共用函数群 ######################

def get_pool(index,enddate=None):

    '''
    Meaning:
        得到成分股的股票代码list

    Inputs:
        index: 股指代码

    Outputs:
        成分股的list
    '''

    #if index == 'all':
    #    return list(get_all_securities(['stock'],date=enddate).index)
    #else:
    #    return get_index_stocks(index,date=enddate)
    if index == 'all':
        return QA.QA_fetch_stock_block_adv().code
    else:
        return QA.QA_fetch_stock_block_adv(code=index).code

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

#import QUANTAXIS as QA

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
        res = field_data.unstack().head(head_count)
    else:
        res = field_data.unstack()

    return res

###################### Alpha函数群 ######################

def alpha_001(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    #pool = get_pool(index,enddate)
    #print(pool)
    #pool = ['000001','000002']
    #pool = ['000001']
    #close = get_price(pool,end_date = enddate,frequency='daily',fields=['close'],count=25)['close']
    #qa_data = QA.QA_fetch_index_day_adv(pool, '2018-01-01', '2018-03-31')
    #c = qa_data.close
    #close = c.unstack().head(25)
    close = get_price(pool, begin_date, end_date, 'close', 25, plat_form_type)
    print(close)
    returns_df = returns(close)
    print(returns_df)
    signedpower_df = pd.DataFrame([],index=range(5),columns=pool)
    print(signedpower_df)
    for stock in pool:
        print(stock)
        for i in range(5):

            if returns_df[stock].iloc[-5+i]<0:
                signedpower_df[stock].loc[i] = signedpower(stddev(returns_df[stock].iloc[i:20+i].to_frame()),2).iloc[0]
            else:
                signedpower_df[stock].loc[i] = signedpower(close[stock].iloc[20+i],2)
            #print(signedpower_df[stock])

    result = rank_pool(ts_argmax(signedpower_df))-0.5

    return result

import os
import sys
#sys.path.append("D:\ProgramData\Anaconda3\Lib\site-packages")

if __name__ == '__main__':
    import QUANTAXIS as QA
    import copy
    #d = QA.QA_fetch_index_day_adv(['000001','000002'], '2018-01-01', '2018-01-31')
    #close = d.close
    #print(close)
    #print(close.index)
    #print(close.values)
    #print(close.unstack())
    #print(type(d))
    #print(type(close))
    #c = close.to_frame()
    #print(c)
    #print(type(c))
    pool = ['000001', '000002']
    res = alpha_001(pool, '2018-01-01', '2018-03-31')
    print(res)
