#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================
'''/**
 * 佩里.J 考夫曼（Perry J.Kaufman）自适应移动平均，参见《精明交易者》（2006年 广东经济出版社）
 * @param n 计算均值的周期窗口，必须为大于2的整数，默认为10天
 * @param fast_n 对应快速周期N，默认为2
 * @param slow_n 对应慢速EMA线的N值，默认为30，不过当超过60左右该指标会收敛不会有太大的影响
 * @ingroup Indicator 具有2个结果集，result(0)为AMA，result(1)为ER
 */'''
def AMA(n = 10, fast_n = 2, slow_n = 30):
    pass

'''/**
 * 平均真实波幅(Average True Range)
 * @param n 计算均值的周期窗口，必须为大于1的整数
 * @ingroup Indicator
 */'''
def ATR(n = 14):
    pass

'''/**
 * 创建一个指定长度的常数指标
 * @param value 常量
 * @param len 长度
 * @param discard 抛弃数量，默认0
 * @ingroup Indicator
 */'''
def CVAL(value=0.0, len=0, discard=0):
    pass

'''/**
 * 差分指标，即data[i] - data[i-1]
 * @ingroup Indicator
 */'''
def DIFF():
    pass

'''/**
 * 指数移动平均线(Exponential Moving Average)
 * @param n 计算均值的周期窗口，必须为大于0的整数
 * @ingroup Indicator
 */'''
def EMA(n = 22):
    pass

'''/**
 * N日内最高价
 * @param n N日时间窗口
 */'''
def HHV(n = 20):
    pass

'''/**
 * N日内最低价
 * @param n N日时间窗口
 */'''
def LLV(n = 20):
    pass
