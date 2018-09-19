#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#function doc: id, parameter num, return num
#==============================================================================

import talib

def TALIB_AD(close):
    '''00325,1,1'''
    return talib.AD(close)

def TALIB_ADOSC(close, fastperiod=3, slowperiod=10):
    '''00326,3,1'''
    return talib.ADOSC(close, fastperiod, slowperiod)

def TALIB_ADX(close, timeperiod=14):
    '''00327,2,1'''
    return talib.ADX(close, timeperiod)

def TALIB_ADXR(close, timeperiod=14):
    '''00328,2,1'''
    return talib.ADXR(close, timeperiod)

def TALIB_APO(close, fastperiod=12, slowperiod=26, matype=talib.MA_Type.SMA):
    '''00329,4,1'''
    return talib.APO(close, fastperiod, slowperiod, matype)

def TALIB_AROON(close, timeperiod=14):
    '''00330,2,2'''
    return talib.AROON(close, timeperiod)

def TALIB_AROONOSC(close, timeperiod=14):
    '''00331,2,1'''
    return talib.AROONOSC(close, timeperiod)

def TALIB_ATR(close, timeperiod=14):
    '''00332,2,1'''
    return talib.ATR(close, timeperiod)

def TALIB_AVGPRICE(close, timeperiod=14):
    '''00333,2,1'''
    return talib.AVGPRICE(close, timeperiod)

def TALIB_BBANDS(close, timeperiod=14, nbdevup=2, nbdevdn=2, matype=talib.MA_Type.SMA):
    '''00334,5,3'''
    return talib.BBANDS(close, timeperiod, nbdevup, nbdevdn, matype)

def TALIB_BOP(close):
    '''00335,1,1'''
    return talib.BOP(close)

def TALIB_CCI(close, timeperiod=14):
    '''00336,2,1'''
    return talib.CCI(close, timeperiod)

def TALIB_CMO(close, timeperiod=14):
    '''00337,2,1'''
    return talib.CMO(close, timeperiod)

def TALIB_DEMA(close, timeperiod=30):
    '''00338,2,1'''
    return talib.DEMA(close, timeperiod)

def TALIB_DX(close, timeperiod=14):
    '''00339,2,1'''
    return talib.DX(close, timeperiod)

def TALIB_EMA(close, timeperiod=30):
    '''00340,2,1'''
    return talib.EMA(close, timeperiod)

def TALIB_HT_DCPERIOD(close):
    '''00341,1,1'''
    return talib.HT_DCPERIOD(close)

def TALIB_HT_DCPHASE(close):
    '''00342,1,1'''
    return talib.HT_DCPHASE(close)

def TALIB_HT_PHASOR(close):
    '''00343,1,2'''
    return talib.HT_PHASOR(close)

def TALIB_HT_SINE(close):
    '''00344,1,2'''
    return talib.HT_SINE(close)

def TALIB_HT_TRENDLINE(close):
    '''00345,1,1'''
    return talib.HT_TRENDLINE(close)

def TALIB_HT_TRENDMODE(close):
    '''00346,1,1'''
    return talib.HT_TRENDMODE(close)

def TALIB_KAMA(close, timeperiod=30):
    '''00347,2,1'''
    return talib.KAMA(close, timeperiod)

def TALIB_LINEARREG(close, timeperiod=14):
    '''00348,2,1'''
    return talib.LINEARREG(close, timeperiod)

def TALIB_LINEARREG_ANGLE(close, timeperiod=14):
    '''00349,2,1'''
    return talib.LINEARREG_ANGLE(close, timeperiod)

def TALIB_LINEARREG_INTERCEPT(close, timeperiod=14):
    '''00350,2,1'''
    return talib.LINEARREG_INTERCEPT(close, timeperiod)

def TALIB_LINEARREG_SLOPE(close, timeperiod=14):
    '''00351,2,1'''
    return talib.LINEARREG_SLOPE(close, timeperiod)

def TALIB_MA(close, timeperiod=30, matype=talib.MA_Type.SMA):
    '''00352,3,1'''
    return talib.MA(close, timeperiod, matype)

def TALIB_MACD(close, fastperiod=12, slowperiod=26, signalperiod=9):
    '''00353,4,3'''
    return talib.MACD(close, fastperiod, slowperiod, signalperiod)

def TALIB_MACDEXT(close, fastperiod=12, fastmatype=talib.MA_Type.SMA,
                slowperiod=26, slowmatype=talib.MA_Type.SMA,
                signalperiod=9, signalmatype=talib.MA_Type.SMA):
    '''00354,7,3'''
    return talib.MACDEXT(close, fastperiod, fastmatype,
                slowperiod, slowmatype,
                signalperiod, signalmatype)

def TALIB_MACDFIX(close, signalperiod=9):
    '''00355,2,3'''
    return talib.MACDFIX(close, signalperiod)

def TALIB_MAMA(close, fastlimit=0.5, slowlimit=0.05):
    '''00356,3,2'''
    return talib.MAMA(close, fastlimit, slowlimit)

def TALIB_MAX(close, timeperiod=30):
    '''00357,2,1'''
    return talib.MAX(close, timeperiod)

def TALIB_MAXINDEX(close, timeperiod=30):
    '''00358,2,1'''
    return talib.MAXINDEX(close, timeperiod)

def TALIB_MEDPRICE(close):
    '''00359,1,1'''
    return talib.MEDPRICE(close)

def TALIB_MIDPOINT(close, timeperiod=14):
    '''00360,2,1'''
    return talib.MIDPOINT(close, timeperiod)

def TALIB_MIDPRICE(close, timeperiod=14):
    '''00361,2,1'''
    return talib.MIDPRICE(close, timeperiod)

def TALIB_MIN(close, timeperiod=30):
    '''00362,2,1'''
    return talib.MIN(close, timeperiod)

def TALIB_MININDEX(close, timeperiod=30):
    '''00363,2,1'''
    return talib.MININDEX(close, timeperiod)

def TALIB_MINMAX(close, timeperiod=30):
    '''00364,2,2'''
    return talib.MINMAX(close, timeperiod)

def TALIB_MINMAXINDEX(close, timeperiod=30):
    '''00365,2,2'''
    return talib.MINMAXINDEX(close, timeperiod)

def TALIB_MINUS_DI(close, timeperiod=14):
    '''00366,2,1'''
    return talib.MINUS_DI(close, timeperiod)

def TALIB_MINUS_DM(close, timeperiod=14):
    '''00367,2,1'''
    return talib.MINUS_DM(close, timeperiod)

def TALIB_MOM(close, timeperiod=10):
    '''00368,2,1'''
    return talib.MOM(close, timeperiod)

def TALIB_NATR(close, timeperiod=14):
    '''00369,2,1'''
    return talib.NATR(close, timeperiod)

def TALIB_PLUS_DI(close, timeperiod=14):
    '''00370,2,1'''
    return talib.PLUS_DI(close, timeperiod)

def TALIB_PLUS_DM(close, timeperiod=14):
    '''00371,2,1'''
    return talib.PLUS_DM(close, timeperiod)

def TALIB_PPO(close, fastperiod=12, slowperiod=26, matype=talib.MA_Type.SMA):
    '''00372,4,1'''
    return talib.PPO(close, fastperiod, slowperiod, matype)

def TALIB_ROC(close, timeperiod=10):
    '''00373,2,1'''
    return talib.ROC(close, timeperiod)

def TALIB_ROCP(close, timeperiod=10):
    '''00374,2,1'''
    return talib.ROCP(close, timeperiod)

def TALIB_ROCR(close, timeperiod=10):
    '''00375,2,1'''
    return talib.ROCR(close, timeperiod)

def TALIB_ROCR100(close, timeperiod=10):
    '''00376,2,1'''
    return talib.ROCR100(close, timeperiod)

def TALIB_RSI(close, timeperiod=14):
    '''00377,2,1'''
    return talib.RSI(close, timeperiod)

def TALIB_SAR(close, acceleration=0.02, maximum=0.2):
    '''00378,3,1'''
    return talib.SAR(close, acceleration, maximum)

def TALIB_SAREXT(close, startvalue=0,
                 offsetonreverse=0,
                 accelerationinitlong=0.02,
                 accelerationlong=0.02,
                 accelerationmaxlong=0.02,
                 accelerationinitshort=0.02,
                 accelerationshort=0.02,
                 accelerationmaxshort=0.02):
    '''00379,9,1'''
    return talib.SAREXT(close, startvalue,
                 offsetonreverse,
                 accelerationinitlong,
                 accelerationlong,
                 accelerationmaxlong,
                 accelerationinitshort,
                 accelerationshort,
                 accelerationmaxshort)

def TALIB_SMA(close, timeperiod=30):
    '''00380,2,1'''
    return talib.SMA(close, timeperiod)

def TALIB_STDDEV(close, timeperiod=5, nbdev=1):
    '''00381,3,1'''
    return talib.STDDEV(close, timeperiod, nbdev)

def TALIB_STOCH(close, fastk_period=5,
                 slowk_period=3, slowk_matype=talib.MA_Type.SMA,
                 slowd_period=3, slowd_matype=talib.MA_Type.SMA):
    '''00382,6,2'''
    return talib.STOCH(close, fastk_period,
                 slowk_period, slowk_matype,
                 slowd_period, slowd_matype)

def TALIB_STOCHF(close, fastk_period=5, fastd_period=3, fastd_matype=talib.MA_Type.SMA):
    '''00383,4,2'''
    return talib.STOCHF(close, fastk_period, fastd_period, fastd_matype)

def TALIB_STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=talib.MA_Type.SMA):
    '''00384,5,2'''
    return talib.STOCHRSI(close, timeperiod, fastk_period, fastd_period, fastd_matype)

def TALIB_SUM(close, timeperiod=30):
    '''00385,2,1'''
    return talib.SUM(close, timeperiod)

def TALIB_T3(close, timeperiod=5, vfactor=0.7):
    '''00386,3,1'''
    return talib.T3(close, timeperiod, vfactor)

def TALIB_TEMA(close, timeperiod=30):
    '''00387,2,1'''
    return talib.TEMA(close, timeperiod)

def TALIB_TRANGE(close):
    '''00388,1,1'''
    return talib.TRANGE(close)

def TALIB_TRIMA(close, timeperiod=30):
    '''00389,2,1'''
    return talib.TRIMA(close, timeperiod)

def TALIB_TRIX(close, timeperiod=30):
    '''00390,2,1'''
    return talib.TRIX(close, timeperiod)

def TALIB_TSF(close, timeperiod=14):
    '''00391,2,1'''
    return talib.TSF(close, timeperiod)

def TALIB_TYPPRICE(close, timeperiod=14):
    '''00392,2,1'''
    return talib.TYPPRICE(close, timeperiod)

def TALIB_ULTOSC(close, timeperiod1=7, timeperiod2=14, timeperiod3=28):
    '''00393,4,1'''
    return talib.ULTOSC(close, timeperiod1, timeperiod2, timeperiod3)

def TALIB_VAR(close, timeperiod=5, nbdev=1):
    '''00394,3,1'''
    return talib.VAR(close, timeperiod, nbdev)

def TALIB_WCLPRICE(close):
    '''00395,1,1'''
    return talib.WCLPRICE(close)

def TALIB_WILLR(close, timeperiod=14):
    '''00396,2,1'''
    return talib.WILLR(close, timeperiod)

def TALIB_WMA(close, timeperiod=30):
    '''00397,2,1'''
    return talib.WMA(close, timeperiod)

def TALIB_CDL2CROWS(close):
    '''00398,1,1'''
    return talib.CDL2CROWS(close)

def TALIB_CDL3BLACKCROWS(close):
    '''00399,1,1'''
    return talib.CDL3BLACKCROWS(close)

def TALIB_CDL3INSIDE(close):
    '''00400,1,1'''
    return talib.CDL3INSIDE(close)

def TALIB_CDL3LINESTRIKE(close):
    '''00401,1,1'''
    return talib.CDL3LINESTRIKE(close)

def TALIB_CDL3OUTSIDE(close):
    '''00402,1,1'''
    return talib.CDL3OUTSIDE(close)

def TALIB_CDL3STARSINSOUTH(close):
    '''00403,1,1'''
    return talib.CDL3STARSINSOUTH(close)

def TALIB_CDL3WHITESOLDIERS(close):
    '''00404,1,1'''
    return talib.CDL3WHITESOLDIERS(close)

def TALIB_CDLABANDONEDBABY(close, penetration=0.3):
    '''00405,2,1'''
    return talib.CDLABANDONEDBABY(close, penetration)

def TALIB_CDLADVANCEBLOCK(close):
    '''00406,1,1'''
    return talib.CDLADVANCEBLOCK(close)

def TALIB_CDLBELTHOLD(close):
    '''00407,1,1'''
    return talib.CDLBELTHOLD(close)

def TALIB_CDLBREAKAWAY(close):
    '''00408,1,1'''
    return talib.CDLBREAKAWAY(close)

def TALIB_CDLCLOSINGMARUBOZU(close):
    '''00409,1,1'''
    return talib.CDLCLOSINGMARUBOZU(close)

def TALIB_CDLCONCEALBABYSWALL(close):
    '''00410,1,1'''
    return talib.CDLCONCEALBABYSWALL(close)

def TALIB_CDLCOUNTERATTACK(close):
    '''00411,1,1'''
    return talib.CDLCOUNTERATTACK(close)

def TALIB_CDLDARKCLOUDCOVER(close, penetration=0.5):
    '''00412,2,1'''
    return talib.CDLDARKCLOUDCOVER(close, penetration)

def TALIB_CDLDOJI(close):
    '''00413,1,1'''
    return talib.CDLDOJI(close)

def TALIB_CDLDOJISTAR(close):
    '''00414,1,1'''
    return talib.CDLDOJISTAR(close)

def TALIB_CDLDRAGONFLYDOJI(close):
    '''00415,1,1'''
    return talib.CDLDRAGONFLYDOJI(close)

def TALIB_CDLENGULFING(close):
    '''00416,1,1'''
    return talib.CDLENGULFING(close)

def TALIB_CDLEVENINGDOJISTAR(close, penetration=0.3):
    '''00417,2,1'''
    return talib.CDLEVENINGDOJISTAR(close, penetration)

def TALIB_CDLEVENINGSTAR(close, penetration=0.3):
    '''00418,2,1'''
    return talib.CDLEVENINGSTAR(close, penetration)

def TALIB_CDLGAPSIDESIDEWHITE(close):
    '''00419,1,1'''
    return talib.CDLGAPSIDESIDEWHITE(close)

def TALIB_CDLGRAVESTONEDOJI(close):
    '''00420,1,1'''
    return talib.CDLGRAVESTONEDOJI(close)

def TALIB_CDLHAMMER(close):
    '''00421,1,1'''
    return talib.CDLHAMMER(close)

def TALIB_CDLHANGINGMAN(close):
    '''00422,1,1'''
    return talib.CDLHANGINGMAN(close)

def TALIB_CDLHARAMI(close):
    '''00423,1,1'''
    return talib.CDLHARAMI(close)

def TALIB_CDLHARAMICROSS(close):
    '''00424,1,1'''
    return talib.CDLHARAMICROSS(close)

def TALIB_CDLHIGHWAVE(close):
    '''00425,1,1'''
    return talib.CDLHIGHWAVE(close)

def TALIB_CDLHIKKAKE(close):
    '''00426,1,1'''
    return talib.CDLHIKKAKE(close)

def TALIB_CDLHIKKAKEMOD(close):
    '''00427,1,1'''
    return talib.CDLHIKKAKEMOD(close)

def TALIB_CDLHOMINGPIGEON(close):
    '''00428,1,1'''
    return talib.CDLHOMINGPIGEON(close)

def TALIB_CDLIDENTICAL3CROWS(close):
    '''00429,1,1'''
    return talib.CDLIDENTICAL3CROWS(close)

def TALIB_CDLINNECK(close):
    '''00430,1,1'''
    return talib.CDLINNECK(close)

def TALIB_CDLINVERTEDHAMMER(close):
    '''00431,1,1'''
    return talib.CDLINVERTEDHAMMER(close)

def TALIB_CDLKICKING(close):
    '''00432,1,1'''
    return talib.CDLKICKING(close)

def TALIB_CDLKICKINGBYLENGTH(close):
    '''00433,1,1'''
    return talib.CDLKICKINGBYLENGTH(close)

def TALIB_CDLLADDERBOTTOM(close):
    '''00434,1,1'''
    return talib.CDLLADDERBOTTOM(close)

def TALIB_CDLLONGLEGGEDDOJI(close):
    '''00435,1,1'''
    return talib.CDLLONGLEGGEDDOJI(close)

def TALIB_CDLLONGLINE(close):
    '''00436,1,1'''
    return talib.CDLLONGLINE(close)

def TALIB_CDLMARUBOZU(close):
    '''00437,1,1'''
    return talib.CDLMARUBOZU(close)

def TALIB_CDLMATCHINGLOW(close):
    '''00438,1,1'''
    return talib.CDLMATCHINGLOW(close)

def TALIB_CDLMATHOLD(close, penetration=0.5):
    '''00439,1,1'''
    return talib.CDLMATHOLD(close, penetration)

def TALIB_CDLMORNINGDOJISTAR(close, penetration=0.3):
    '''00440,2,1'''
    return talib.CDLMORNINGDOJISTAR(close, penetration)

def TALIB_CDLMORNINGSTAR(close, penetration=0.3):
    '''00441,2,1'''
    return talib.CDLMORNINGSTAR(close, penetration)

def TALIB_CDLONNECK(close):
    '''00442,1,1'''
    return talib.CDLONNECK(close)

def TALIB_CDLPIERCING(close):
    '''00443,1,1'''
    return talib.CDLPIERCING(close)

def TALIB_CDLRICKSHAWMAN(close):
    '''00444,1,1'''
    return talib.CDLRICKSHAWMAN(close)

def TALIB_CDLRISEFALL3METHODS(close):
    '''00445,1,1'''
    return talib.CDLRISEFALL3METHODS(close)

def TALIB_CDLSEPARATINGLINES(close):
    '''00446,1,1'''
    return talib.CDLSEPARATINGLINES(close)

def TALIB_CDLSHOOTINGSTAR(close):
    '''00447,1,1'''
    return talib.CDLSHOOTINGSTAR(close)

def TALIB_CDLSHORTLINE(close):
    '''00448,1,1'''
    return talib.CDLSHORTLINE(close)

def TALIB_CDLSPINNINGTOP(close):
    '''00449,1,1'''
    return talib.CDLSPINNINGTOP(close)

def TALIB_CDLSTALLEDPATTERN(close):
    '''00450,1,1'''
    return talib.CDLSTALLEDPATTERN(close)

def TALIB_CDLSTICKSANDWICH(close):
    '''00451,1,1'''
    return talib.CDLSTICKSANDWICH(close)

def TALIB_CDLTAKURI(close):
    '''00452,1,1'''
    return talib.CDLTAKURI(close)

def TALIB_CDLTASUKIGAP(close):
    '''00453,1,1'''
    return talib.CDLTASUKIGAP(close)

def TALIB_CDLTHRUSTING(close):
    '''00454,1,1'''
    return talib.CDLTHRUSTING(close)

def TALIB_CDLTRISTAR(close):
    '''00455,1,1'''
    return talib.CDLTRISTAR(close)

def TALIB_CDLUNIQUE3RIVER(close):
    '''00456,1,1'''
    return talib.CDLUNIQUE3RIVER(close)

def TALIB_CDLUPSIDEGAP2CROWS(close):
    '''00457,1,1'''
    return talib.CDLUPSIDEGAP2CROWS(close)

def TALIB_CDLXSIDEGAP3METHODS(close):
    '''00458,1,1'''
    return talib.CDLXSIDEGAP3METHODS(close)

def TALIB_BETA(close, timeperiod=5):
    '''00459,2,1'''
    return talib.BETA(close, timeperiod)

def TALIB_CORREL(close, timeperiod=30):
    '''00460,2,1'''
    return talib.CORREL(close, timeperiod)

def TALIB_OBV(close):
    '''00461,1,1'''
    return talib.OBV(close)
