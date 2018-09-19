#!/usr/bin/python
# -*- coding: utf8 -*-

from hikyuu.indicator import *
import talib

def LQ_Hikyuu_AMA(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00001,4,2'''
    return AMA(close, n=n1, fast_n=n2, slow_n=n3)

def LQ_Hikyuu_AMO(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00002,1,1'''
    return AMO(close)

def LQ_Hikyuu_CLOSE(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00003,1,1'''
    return CLOSE(close)

def LQ_Hikyuu_CVAL(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00004,4,1'''
    return CVAL(close,value=value,len=len,discard=discard)

def LQ_Hikyuu_DIFF(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00005,1,1'''
    return DIFF(close)

def LQ_Hikyuu_EMA(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00006,2,1'''
    return EMA(close,n=n1)

def LQ_Hikyuu_HHV(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00007,2,1'''
    return HHV(close,n=n1)

def LQ_Hikyuu_HIGH(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00008,1,1'''
    return HIGH(close)

def LQ_Hikyuu_Kclose(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00009,1,1'''
    return Kclose(close)

def LQ_Hikyuu_LLV(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00010,2,1'''
    return LLV(close,n=n1)

def LQ_Hikyuu_LOW(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00011,1,1'''
    return LOW(close)

def LQ_Hikyuu_MA(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00012,3,1'''
    return MA(close,n=n1,type=type)

def LQ_Hikyuu_MACD(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00013,4,3'''
    return MACD(close,n1=n1,n2=n2,n3=n3)

def LQ_Hikyuu_OPEN(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00014,1,1'''
    return OPEN(close)

def LQ_Hikyuu_REF(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00015,2,1'''
    return REF(close,n=n1)

def LQ_Hikyuu_SAFTYLOSS(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00016,4,1'''
    return SAFTYLOSS(close,n1=n1,n2=n2,p=p)

def LQ_Hikyuu_SMA(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00017,2,1'''
    return SMA(close,n=n1)

def LQ_Hikyuu_STDEV(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00018,2,1'''
    return STDEV(close,n=n1)

def LQ_Hikyuu_VIGOR(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00019,2,1'''
    return VIGOR(close,n=n1)

def LQ_Hikyuu_VOL(close, n1=0, n2=0, n3=0, len=0, discard=0, value=0.0, p=0.0, type=""):
    '''00020,1,1'''
    return VOL(close)

def LQ_Hikyuu_TA_AD(ind=None):
    '''00021,1,1'''
    return TA_AD(ind)

def LQ_Hikyuu_TA_ADOSC(ind=None, fastperiod=3, slowperiod=10):
    '''00022,3,1'''
    return TA_ADOSC(ind, fastperiod, slowperiod)

def LQ_Hikyuu_TA_ADX(ind=None, timeperiod=14):
    '''00023,2,1'''
    return TA_ADX(ind, timeperiod)

def LQ_Hikyuu_TA_ADXR(ind=None, timeperiod=14):
    '''00024,2,1'''
    return TA_ADXR(ind, timeperiod)

def LQ_Hikyuu_TA_APO(ind=None, fastperiod=12, slowperiod=26, matype=talib.MA_Type.SMA):
    '''00025,4,1'''
    return TA_APO(ind, fastperiod, slowperiod, matype)

def LQ_Hikyuu_TA_AROON(ind=None, timeperiod=14):
    '''00026,2,2'''
    return TA_AROON(ind, timeperiod)

def LQ_Hikyuu_TA_AROONOSC(ind=None, timeperiod=14):
    '''00027,2,1'''
    return TA_AROONOSC(ind, timeperiod)

def LQ_Hikyuu_TA_ATR(ind=None, timeperiod=14):
    '''00028,2,1'''
    return TA_ATR(ind, timeperiod)

def LQ_Hikyuu_TA_AVGPRICE(ind=None, timeperiod=14):
    '''00029,2,1'''
    return TA_AVGPRICE(ind, timeperiod)

def LQ_Hikyuu_TA_BBANDS(ind=None, timeperiod=14, nbdevup=2, nbdevdn=2, matype=talib.MA_Type.SMA):
    '''00030,5,3'''
    return TA_BBANDS(ind, timeperiod, nbdevup, nbdevdn, matype)

def LQ_Hikyuu_TA_BOP(ind=None):
    '''00031,1,1'''
    return TA_BOP(ind)

def LQ_Hikyuu_TA_CCI(ind=None, timeperiod=14):
    '''00032,2,1'''
    return TA_CCI(ind, timeperiod)

def LQ_Hikyuu_TA_CMO(ind=None, timeperiod=14):
    '''00033,2,1'''
    return TA_CMO(ind, timeperiod)

def LQ_Hikyuu_TA_DEMA(ind=None, timeperiod=30):
    '''00034,2,1'''
    return TA_DEMA(ind, timeperiod)

def LQ_Hikyuu_TA_DX(ind=None, timeperiod=14):
    '''00035,2,1'''
    return TA_DX(ind, timeperiod)

def LQ_Hikyuu_TA_EMA(ind=None, timeperiod=30):
    '''00036,2,1'''
    return TA_EMA(ind, timeperiod)

def LQ_Hikyuu_TA_HT_DCPERIOD(ind=None):
    '''00037,1,1'''
    return TA_HT_DCPERIOD(ind)

def LQ_Hikyuu_TA_HT_DCPHASE(ind=None):
    '''00038,1,1'''
    return TA_HT_DCPHASE(ind)

def LQ_Hikyuu_TA_HT_PHASOR(ind=None):
    '''00039,1,2'''
    return TA_HT_PHASOR(ind)

def LQ_Hikyuu_TA_HT_SINE(ind=None):
    '''00040,1,2'''
    return TA_HT_SINE(ind)

def LQ_Hikyuu_TA_HT_TRENDLINE(ind=None):
    '''00041,1,1'''
    return TA_HT_TRENDLINE(ind)

def LQ_Hikyuu_TA_HT_TRENDMODE(ind=None):
    '''00042,1,1'''
    return TA_HT_TRENDMODE(ind)

def LQ_Hikyuu_TA_KAMA(ind=None, timeperiod=30):
    '''00043,2,1'''
    return TA_KAMA(ind, timeperiod)

def LQ_Hikyuu_TA_LINEARREG(ind=None, timeperiod=14):
    '''00044,2,1'''
    return TA_LINEARREG(ind, timeperiod)

def LQ_Hikyuu_TA_LINEARREG_ANGLE(ind=None, timeperiod=14):
    '''00045,2,1'''
    return TA_LINEARREG_ANGLE(ind, timeperiod)

def LQ_Hikyuu_TA_LINEARREG_INTERCEPT(ind=None, timeperiod=14):
    '''00046,2,1'''
    return TA_LINEARREG_INTERCEPT(ind, timeperiod)

def LQ_Hikyuu_TA_LINEARREG_SLOPE(ind=None, timeperiod=14):
    '''00047,2,1'''
    return TA_LINEARREG_SLOPE(ind, timeperiod)

def LQ_Hikyuu_TA_MA(ind=None, timeperiod=30, matype=talib.MA_Type.SMA):
    '''00048,3,1'''
    return TA_MA(ind, timeperiod, matype)

def LQ_Hikyuu_TA_MACD(ind=None, fastperiod=12, slowperiod=26, signalperiod=9):
    '''00049,4,3'''
    return TA_MACD(ind, fastperiod, slowperiod, signalperiod)

def LQ_Hikyuu_TA_MACDEXT(ind=None, fastperiod=12, fastmatype=talib.MA_Type.SMA,
                slowperiod=26, slowmatype=talib.MA_Type.SMA,
                signalperiod=9, signalmatype=talib.MA_Type.SMA):
    '''00050,7,3'''
    return TA_MACDEXT(ind, fastperiod, fastmatype,
                slowperiod, slowmatype,
                signalperiod, signalmatype)

def LQ_Hikyuu_TA_MACDFIX(ind=None, signalperiod=9):
    '''00051,2,3'''
    return TA_MACDFIX(ind, signalperiod)

def LQ_Hikyuu_TA_MAMA(ind=None, fastlimit=0.5, slowlimit=0.05):
    '''00052,3,2'''
    return TA_MAMA(ind, fastlimit, slowlimit)

def LQ_Hikyuu_TA_MAX(ind=None, timeperiod=30):
    '''00053,2,1'''
    return TA_MAX(ind, timeperiod)

def LQ_Hikyuu_TA_MAXINDEX(ind=None, timeperiod=30):
    '''00054,2,1'''
    return TA_MAXINDEX(ind, timeperiod)

def LQ_Hikyuu_TA_MEDPRICE(ind=None):
    '''00055,1,1'''
    return TA_MEDPRICE(ind)

def LQ_Hikyuu_TA_MIDPOINT(ind=None, timeperiod=14):
    '''00056,2,1'''
    return TA_MIDPOINT(ind, timeperiod)

def LQ_Hikyuu_TA_MIDPRICE(ind=None, timeperiod=14):
    '''00057,2,1'''
    return TA_MIDPRICE(ind, timeperiod)

def LQ_Hikyuu_TA_MIN(ind=None, timeperiod=30):
    '''00058,2,1'''
    return TA_MIN(ind, timeperiod)

def LQ_Hikyuu_TA_MININDEX(ind=None, timeperiod=30):
    '''00059,2,1'''
    return TA_MININDEX(ind, timeperiod)

def LQ_Hikyuu_TA_MINMAX(ind=None, timeperiod=30):
    '''00060,2,2'''
    return TA_MINMAX(ind, timeperiod)

def LQ_Hikyuu_TA_MINMAXINDEX(ind=None, timeperiod=30):
    '''00061,2,2'''
    return TA_MINMAXINDEX(ind, timeperiod)

def LQ_Hikyuu_TA_MINUS_DI(ind=None, timeperiod=14):
    '''00062,2,1'''
    return TA_MINUS_DI(ind, timeperiod)

def LQ_Hikyuu_TA_MINUS_DM(ind=None, timeperiod=14):
    '''00063,2,1'''
    return TA_MINUS_DM(ind, timeperiod)

def LQ_Hikyuu_TA_MOM(ind=None, timeperiod=10):
    '''00064,2,1'''
    return TA_MOM(ind, timeperiod)

def LQ_Hikyuu_TA_NATR(ind=None, timeperiod=14):
    '''00065,2,1'''
    return TA_NATR(ind, timeperiod)

def LQ_Hikyuu_TA_PLUS_DI(ind=None, timeperiod=14):
    '''00066,2,1'''
    return TA_PLUS_DI(ind, timeperiod)

def LQ_Hikyuu_TA_PLUS_DM(ind=None, timeperiod=14):
    '''00067,2,1'''
    return TA_PLUS_DM(ind, timeperiod)

def LQ_Hikyuu_TA_PPO(ind=None, fastperiod=12, slowperiod=26, matype=talib.MA_Type.SMA):
    '''00068,4,1'''
    return TA_PPO(ind, fastperiod, slowperiod, matype)

def LQ_Hikyuu_TA_ROC(ind=None, timeperiod=10):
    '''00069,2,1'''
    return TA_ROC(ind, timeperiod)

def LQ_Hikyuu_TA_ROCP(ind=None, timeperiod=10):
    '''00070,2,1'''
    return TA_ROCP(ind, timeperiod)

def LQ_Hikyuu_TA_ROCR(ind=None, timeperiod=10):
    '''00071,2,1'''
    return TA_ROCR(ind, timeperiod)

def LQ_Hikyuu_TA_ROCR100(ind=None, timeperiod=10):
    '''00072,2,1'''
    return TA_ROCR100(ind, timeperiod)

def LQ_Hikyuu_TA_RSI(ind=None, timeperiod=14):
    '''00073,2,1'''
    return TA_RSI(ind, timeperiod)

def LQ_Hikyuu_TA_SAR(ind=None, acceleration=0.02, maximum=0.2):
    '''00074,3,1'''
    return TA_SAR(ind, acceleration, maximum)

def LQ_Hikyuu_TA_SAREXT(ind=None, startvalue=0,
                 offsetonreverse=0,
                 accelerationinitlong=0.02,
                 accelerationlong=0.02,
                 accelerationmaxlong=0.02,
                 accelerationinitshort=0.02,
                 accelerationshort=0.02,
                 accelerationmaxshort=0.02):
    '''00075,9,1'''
    return TA_SAREXT(ind, startvalue,
                 offsetonreverse,
                 accelerationinitlong,
                 accelerationlong,
                 accelerationmaxlong,
                 accelerationinitshort,
                 accelerationshort,
                 accelerationmaxshort)

def LQ_Hikyuu_TA_SMA(ind=None, timeperiod=30):
    '''00076,2,1'''
    return TA_SMA(ind, timeperiod)

def LQ_Hikyuu_TA_STDDEV(ind=None, timeperiod=5, nbdev=1):
    '''00077,3,1'''
    return TA_STDDEV(ind, timeperiod, nbdev)

def LQ_Hikyuu_TA_STOCH(ind=None, fastk_period=5,
                 slowk_period=3, slowk_matype=talib.MA_Type.SMA,
                 slowd_period=3, slowd_matype=talib.MA_Type.SMA):
    '''00078,6,2'''
    return TA_STOCH(ind, fastk_period,
                 slowk_period, slowk_matype,
                 slowd_period, slowd_matype)

def LQ_Hikyuu_TA_STOCHF(ind=None, fastk_period=5, fastd_period=3, fastd_matype=talib.MA_Type.SMA):
    '''00079,4,2'''
    return TA_STOCHF(ind, fastk_period, fastd_period, fastd_matype)

def LQ_Hikyuu_TA_STOCHRSI(ind=None, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=talib.MA_Type.SMA):
    '''00080,5,2'''
    return TA_STOCHRSI(ind, timeperiod, fastk_period, fastd_period, fastd_matype)

def LQ_Hikyuu_TA_SUM(ind=None, timeperiod=30):
    '''00081,2,1'''
    return TA_SUM(ind, timeperiod)

def LQ_Hikyuu_TA_T3(ind=None, timeperiod=5, vfactor=0.7):
    '''00082,3,1'''
    return TA_T3(ind, timeperiod, vfactor)

def LQ_Hikyuu_TA_TEMA(ind=None, timeperiod=30):
    '''00083,2,1'''
    return TA_TEMA(ind, timeperiod)

def LQ_Hikyuu_TA_TRANGE(ind=None):
    '''00084,1,1'''
    return TA_TRANGE(ind)

def LQ_Hikyuu_TA_TRIMA(ind=None, timeperiod=30):
    '''00085,2,1'''
    return TA_TRIMA(ind, timeperiod)

def LQ_Hikyuu_TA_TRIX(ind=None, timeperiod=30):
    '''00086,2,1'''
    return TA_TRIX(ind, timeperiod)

def LQ_Hikyuu_TA_TSF(ind=None, timeperiod=14):
    '''00087,2,1'''
    return TA_TSF(ind, timeperiod)

def LQ_Hikyuu_TA_TYPPRICE(ind=None, timeperiod=14):
    '''00088,2,1'''
    return TA_TYPPRICE(ind, timeperiod)

def LQ_Hikyuu_TA_ULTOSC(ind=None, timeperiod1=7, timeperiod2=14, timeperiod3=28):
    '''00089,4,1'''
    return TA_ULTOSC(ind, timeperiod1, timeperiod2, timeperiod3)

def LQ_Hikyuu_TA_VAR(ind=None, timeperiod=5, nbdev=1):
    '''00090,3,1'''
    return TA_VAR(ind, timeperiod, nbdev)

def LQ_Hikyuu_TA_WCLPRICE(ind=None):
    '''00091,1,1'''
    return TA_WCLPRICE(ind)

def LQ_Hikyuu_TA_WILLR(ind=None, timeperiod=14):
    '''00092,2,1'''
    return TA_WILLR(ind, timeperiod)

def LQ_Hikyuu_TA_WMA(ind=None, timeperiod=30):
    '''00093,2,1'''
    return TA_WMA(ind, timeperiod)

def LQ_Hikyuu_TA_CDL2CROWS(ind=None):
    '''00094,1,1'''
    return TA_CDL2CROWS(ind)

def LQ_Hikyuu_TA_CDL3BLACKCROWS(ind=None):
    '''00095,1,1'''
    return TA_CDL3BLACKCROWS(ind)

def LQ_Hikyuu_TA_CDL3INSIDE(ind=None):
    '''00096,1,1'''
    return TA_CDL3INSIDE(ind)

def LQ_Hikyuu_TA_CDL3LINESTRIKE(ind=None):
    '''00097,1,1'''
    return TA_CDL3LINESTRIKE(ind)

def LQ_Hikyuu_TA_CDL3OUTSIDE(ind=None):
    '''00098,1,1'''
    return TA_CDL3OUTSIDE(ind)

def LQ_Hikyuu_TA_CDL3STARSINSOUTH(ind=None):
    '''00099,1,1'''
    return TA_CDL3STARSINSOUTH(ind)

def LQ_Hikyuu_TA_CDL3WHITESOLDIERS(ind=None):
    '''00100,1,1'''
    return TA_CDL3WHITESOLDIERS(ind)

def LQ_Hikyuu_TA_CDLABANDONEDBABY(ind=None, penetration=0.3):
    '''00101,2,1'''
    return TA_CDLABANDONEDBABY(ind, penetration)

def LQ_Hikyuu_TA_CDLADVANCEBLOCK(ind=None):
    '''00102,1,1'''
    return TA_CDLADVANCEBLOCK(ind)

def LQ_Hikyuu_TA_CDLBELTHOLD(ind=None):
    '''00103,1,1'''
    return TA_CDLBELTHOLD(ind)

def LQ_Hikyuu_TA_CDLBREAKAWAY(ind=None):
    '''00104,1,1'''
    return TA_CDLBREAKAWAY(ind)

def LQ_Hikyuu_TA_CDLCLOSINGMARUBOZU(ind=None):
    '''00105,1,1'''
    return TA_CDLCLOSINGMARUBOZU(ind)

def LQ_Hikyuu_TA_CDLCONCEALBABYSWALL(ind=None):
    '''00106,1,1'''
    return TA_CDLCONCEALBABYSWALL(ind)

def LQ_Hikyuu_TA_CDLCOUNTERATTACK(ind=None):
    '''00107,1,1'''
    return TA_CDLCOUNTERATTACK(ind)

def LQ_Hikyuu_TA_CDLDARKCLOUDCOVER(ind=None, penetration=0.5):
    '''00108,2,1'''
    return TA_CDLDARKCLOUDCOVER(ind, penetration)

def LQ_Hikyuu_TA_CDLDOJI(ind=None):
    '''00109,1,1'''
    return TA_CDLDOJI(ind)

def LQ_Hikyuu_TA_CDLDOJISTAR(ind=None):
    '''00110,1,1'''
    return TA_CDLDOJISTAR(ind)

def LQ_Hikyuu_TA_CDLDRAGONFLYDOJI(ind=None):
    '''00111,1,1'''
    return TA_CDLDRAGONFLYDOJI(ind)

def LQ_Hikyuu_TA_CDLENGULFING(ind=None):
    '''00112,1,1'''
    return TA_CDLENGULFING(ind)

def LQ_Hikyuu_TA_CDLEVENINGDOJISTAR(ind=None, penetration=0.3):
    '''00113,2,1'''
    return TA_CDLEVENINGDOJISTAR(ind, penetration)

def LQ_Hikyuu_TA_CDLEVENINGSTAR(ind=None, penetration=0.3):
    '''00114,2,1'''
    return TA_CDLEVENINGSTAR(ind, penetration)

def LQ_Hikyuu_TA_CDLGAPSIDESIDEWHITE(ind=None):
    '''00115,1,1'''
    return TA_CDLGAPSIDESIDEWHITE(ind)

def LQ_Hikyuu_TA_CDLGRAVESTONEDOJI(ind=None):
    '''00116,1,1'''
    return TA_CDLGRAVESTONEDOJI(ind)

def LQ_Hikyuu_TA_CDLHAMMER(ind=None):
    '''00117,1,1'''
    return TA_CDLHAMMER(ind)

def LQ_Hikyuu_TA_CDLHANGINGMAN(ind=None):
    '''00118,1,1'''
    return TA_CDLHANGINGMAN(ind)

def LQ_Hikyuu_TA_CDLHARAMI(ind=None):
    '''00119,1,1'''
    return TA_CDLHARAMI(ind)

def LQ_Hikyuu_TA_CDLHARAMICROSS(ind=None):
    '''00120,1,1'''
    return TA_CDLHARAMICROSS(ind)

def LQ_Hikyuu_TA_CDLHIGHWAVE(ind=None):
    '''00121,1,1'''
    return TA_CDLHIGHWAVE(ind)

def LQ_Hikyuu_TA_CDLHIKKAKE(ind=None):
    '''00122,1,1'''
    return TA_CDLHIKKAKE(ind)

def LQ_Hikyuu_TA_CDLHIKKAKEMOD(ind=None):
    '''00123,1,1'''
    return TA_CDLHIKKAKEMOD(ind)

def LQ_Hikyuu_TA_CDLHOMINGPIGEON(ind=None):
    '''00124,1,1'''
    return TA_CDLHOMINGPIGEON(ind)

def LQ_Hikyuu_TA_CDLIDENTICAL3CROWS(ind=None):
    '''00125,1,1'''
    return TA_CDLIDENTICAL3CROWS(ind)

def LQ_Hikyuu_TA_CDLINNECK(ind=None):
    '''00126,1,1'''
    return TA_CDLINNECK(ind)

def LQ_Hikyuu_TA_CDLINVERTEDHAMMER(ind=None):
    '''00127,1,1'''
    return TA_CDLINVERTEDHAMMER(ind)

def LQ_Hikyuu_TA_CDLKICKING(ind=None):
    '''00128,1,1'''
    return TA_CDLKICKING(ind)

def LQ_Hikyuu_TA_CDLKICKINGBYLENGTH(ind=None):
    '''00129,1,1'''
    return TA_CDLKICKINGBYLENGTH(ind)

def LQ_Hikyuu_TA_CDLLADDERBOTTOM(ind=None):
    '''00130,1,1'''
    return TA_CDLLADDERBOTTOM(ind)

def LQ_Hikyuu_TA_CDLLONGLEGGEDDOJI(ind=None):
    '''00131,1,1'''
    return TA_CDLLONGLEGGEDDOJI(ind)

def LQ_Hikyuu_TA_CDLLONGLINE(ind=None):
    '''00132,1,1'''
    return TA_CDLLONGLINE(ind)

def LQ_Hikyuu_TA_CDLMARUBOZU(ind=None):
    '''00133,1,1'''
    return TA_CDLMARUBOZU(ind)

def LQ_Hikyuu_TA_CDLMATCHINGLOW(ind=None):
    '''00134,1,1'''
    return TA_CDLMATCHINGLOW(ind)

def LQ_Hikyuu_TA_CDLMATHOLD(ind=None, penetration=0.5):
    '''00135,1,1'''
    return TA_CDLMATHOLD(ind, penetration)

def LQ_Hikyuu_TA_CDLMORNINGDOJISTAR(ind=None, penetration=0.3):
    '''00136,2,1'''
    return TA_CDLMORNINGDOJISTAR(ind, penetration)

def LQ_Hikyuu_TA_CDLMORNINGSTAR(ind=None, penetration=0.3):
    '''00137,2,1'''
    return TA_CDLMORNINGSTAR(ind, penetration)

def LQ_Hikyuu_TA_CDLONNECK(ind=None):
    '''00138,1,1'''
    return TA_CDLONNECK(ind)

def LQ_Hikyuu_TA_CDLPIERCING(ind=None):
    '''00139,1,1'''
    return TA_CDLPIERCING(ind)

def LQ_Hikyuu_TA_CDLRICKSHAWMAN(ind=None):
    '''00140,1,1'''
    return TA_CDLRICKSHAWMAN(ind)

def LQ_Hikyuu_TA_CDLRISEFALL3METHODS(ind=None):
    '''00141,1,1'''
    return TA_CDLRISEFALL3METHODS(ind)

def LQ_Hikyuu_TA_CDLSEPARATINGLINES(ind=None):
    '''00142,1,1'''
    return TA_CDLSEPARATINGLINES(ind)

def LQ_Hikyuu_TA_CDLSHOOTINGSTAR(ind=None):
    '''00143,1,1'''
    return TA_CDLSHOOTINGSTAR(ind)

def LQ_Hikyuu_TA_CDLSHORTLINE(ind=None):
    '''00144,1,1'''
    return TA_CDLSHORTLINE(ind)

def LQ_Hikyuu_TA_CDLSPINNINGTOP(ind=None):
    '''00145,1,1'''
    return TA_CDLSPINNINGTOP(ind)

def LQ_Hikyuu_TA_CDLSTALLEDPATTERN(ind=None):
    '''00146,1,1'''
    return TA_CDLSTALLEDPATTERN(ind)

def LQ_Hikyuu_TA_CDLSTICKSANDWICH(ind=None):
    '''00147,1,1'''
    return TA_CDLSTICKSANDWICH(ind)

def LQ_Hikyuu_TA_CDLTAKURI(ind=None):
    '''00148,1,1'''
    return TA_CDLTAKURI(ind)

def LQ_Hikyuu_TA_CDLTASUKIGAP(ind=None):
    '''00149,1,1'''
    return TA_CDLTASUKIGAP(ind)

def LQ_Hikyuu_TA_CDLTHRUSTING(ind=None):
    '''00150,1,1'''
    return TA_CDLTHRUSTING(ind)

def LQ_Hikyuu_TA_CDLTRISTAR(ind=None):
    '''00151,1,1'''
    return TA_CDLTRISTAR(ind)

def LQ_Hikyuu_TA_CDLUNIQUE3RIVER(ind=None):
    '''00152,1,1'''
    return TA_CDLUNIQUE3RIVER(ind)

def LQ_Hikyuu_TA_CDLUPSIDEGAP2CROWS(ind=None):
    '''00153,1,1'''
    return TA_CDLUPSIDEGAP2CROWS(ind)

def LQ_Hikyuu_TA_CDLXSIDEGAP3METHODS(ind=None):
    '''00154,1,1'''
    return TA_CDLXSIDEGAP3METHODS(ind)

def LQ_Hikyuu_TA_BETA(ind=None, timeperiod=5):
    '''00155,2,1'''
    return TA_BETA(ind, timeperiod)

def LQ_Hikyuu_TA_CORREL(ind=None, timeperiod=30):
    '''00156,2,1'''
    return TA_CORREL(ind, timeperiod)

def LQ_Hikyuu_TA_OBV(ind=None):
    '''00157,1,1'''
    return TA_OBV(ind)
