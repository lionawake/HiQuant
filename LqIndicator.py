#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#function doc: id, parameter num, return num
#==============================================================================
#from hikyuu.indicator import *
import talib
import LqWQ101 as LQA101
import LqAlpha191 as LQA191

#import pickle
#findat = pickle.load(open('fin_data.pkl', 'rb'))

#==================Hikyuu functions begin==================
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
#==================Hikyuu functions end==================

#==================finance functions begin==================
def fa_eps_basic(stock):
    '''00158,1,1'''
    return findat.at[stock, 'fa_eps_basic']

def fa_eps_diluted(stock):
    '''00159,1,1'''
    return findat.at[stock, 'fa_eps_diluted']

def fa_bps(stock):
    '''00160,1,1'''
    return findat.at[stock, 'fa_bps']

def fa_grps(stock):
    '''00161,1,1'''
    return findat.at[stock, 'fa_grps']


def fa_orps(stock):
    '''00162,1,1'''
    return findat.at[stock, 'fa_orps']


def fa_opps(stock):
    '''00163,1,1'''
    return findat.at[stock, 'fa_opps']


def fa_capsurpps(stock):
    '''00164,1,1'''
    return findat.at[stock, 'fa_capsurpps']


def fa_spps(stock):
    '''00165,1,1'''
    return findat.at[stock, 'fa_spps']


def fa_undistributedps(stock):
    '''00166,1,1'''
    return findat.at[stock, 'fa_undistributedps']


def fa_retainedps(stock):
    '''00167,1,1'''
    return findat.at[stock, 'fa_retainedps']


def fa_fcffps(stock):
    '''00168,1,1'''
    return findat.at[stock, 'fa_fcffps']


def fa_fcfeps(stock):
    '''00169,1,1'''
    return findat.at[stock, 'fa_fcfeps']


def fa_cceps(stock):
    '''00170,1,1'''
    return findat.at[stock, 'fa_cceps']


def fa_divcover_ttm(stock):
    '''00171,1,1'''
    return findat.at[stock, 'fa_divcover_ttm']


def fa_retainedearn_ttm(stock):
    '''00172,1,1'''
    return findat.at[stock, 'fa_retainedearn_ttm']


def fa_cfps_ttm(stock):
    '''00173,1,1'''
    return findat.at[stock, 'fa_cfps_ttm']


def fa_ocfps_ttm(stock):
    '''00174,1,1'''
    return findat.at[stock, 'fa_ocfps_ttm']


def fa_opps_ttm(stock):
    '''00175,1,1'''
    return findat.at[stock, 'fa_opps_ttm']


def fa_roe_avg(stock):
    '''00176,1,1'''
    return findat.at[stock, 'fa_roe_avg']


def fa_roe_wgt(stock):
    '''00177,1,1'''
    return findat.at[stock, 'fa_roe_wgt']


def fa_roe_diluted(stock):
    '''00178,1,1'''
    return findat.at[stock, 'fa_roe_diluted']


def fa_roe_exbasic(stock):
    '''00179,1,1'''
    return findat.at[stock, 'fa_roe_exbasic']


def fa_roe_exdiluted(stock):
    '''00180,1,1'''
    return findat.at[stock, 'fa_roe_exdiluted']


def fa_roenp_ttm(stock):
    '''00181,1,1'''
    return findat.at[stock, 'fa_roenp_ttm']


def fa_roaebit_ttm(stock):
    '''00182,1,1'''
    return findat.at[stock, 'fa_roaebit_ttm']


def fa_netprofittoassets_ttm(stock):
    '''00183,1,1'''
    return findat.at[stock, 'fa_netprofittoassets_ttm']


def fa_roic_ttm(stock):
    '''00184,1,1'''
    return findat.at[stock, 'fa_roic_ttm']


def fa_roicebit_ttm(stock):
    '''00185,1,1'''
    return findat.at[stock, 'fa_roicebit_ttm']


def fa_roc_ttm(stock):
    '''00186,1,1'''
    return findat.at[stock, 'fa_roc_ttm']


def fa_roa_ttm(stock):
    '''00187,1,1'''
    return findat.at[stock, 'fa_roa_ttm']


def fa_roaavg5y(stock):
    '''00188,1,1'''
    return findat.at[stock, 'fa_roaavg5y']


def fa_roe_ttm(stock):
    '''00189,1,1'''
    return findat.at[stock, 'fa_roe_ttm']


def fa_roeavg5y(stock):
    '''00190,1,1'''
    return findat.at[stock, 'fa_roeavg5y']


def fa_protocost_ttm(stock):
    '''00191,1,1'''
    return findat.at[stock, 'fa_protocost_ttm']


def fa_profittogr_ttm(stock):
    '''00192,1,1'''
    return findat.at[stock, 'fa_profittogr_ttm']


def fa_optoor_ttm(stock):
    '''00193,1,1'''
    return findat.at[stock, 'fa_optoor_ttm']


def fa_optogr_ttm(stock):
    '''00194,1,1'''
    return findat.at[stock, 'fa_optogr_ttm']


def fa_ebittogr_ttm(stock):
    '''00195,1,1'''
    return findat.at[stock, 'fa_ebittogr_ttm']


def fa_sellexpensetogr_ttm(stock):
    '''00196,1,1'''
    return findat.at[stock, 'fa_sellexpensetogr_ttm']


def fa_adminexpensetogr_ttm(stock):
    '''00197,1,1'''
    return findat.at[stock, 'fa_adminexpensetogr_ttm']


def fa_finaexpensetogr_ttm(stock):
    '''00198,1,1'''
    return findat.at[stock, 'fa_finaexpensetogr_ttm']


def fa_impairtogr_ttm(stock):
    '''00199,1,1'''
    return findat.at[stock, 'fa_impairtogr_ttm']


def fa_octogr_ttm(stock):
    '''00200,1,1'''
    return findat.at[stock, 'fa_octogr_ttm']


def fa_netprofittoor_ttm(stock):
    '''00201,1,1'''
    return findat.at[stock, 'fa_netprofittoor_ttm']


def fa_taxtoprofitbt_ttm(stock):
    '''00202,1,1'''
    return findat.at[stock, 'fa_taxtoprofitbt_ttm']


def fa_netprofitmargin_ttm(stock):
    '''00203,1,1'''
    return findat.at[stock, 'fa_netprofitmargin_ttm']


def fa_grossprofitmargin_ttm(stock):
    '''00204,1,1'''
    return findat.at[stock, 'fa_grossprofitmargin_ttm']


def fa_expensetosales_ttm(stock):
    '''00205,1,1'''
    return findat.at[stock, 'fa_expensetosales_ttm']


def fa_salestocost_ttm(stock):
    '''00206,1,1'''
    return findat.at[stock, 'fa_salestocost_ttm']


def fa_taxratio_ttm(stock):
    '''00207,1,1'''
    return findat.at[stock, 'fa_taxratio_ttm']


def fa_acca_ttm(stock):
    '''00208,1,1'''
    return findat.at[stock, 'fa_acca_ttm']


def fa_berryratio_ttm(stock):
    '''00209,1,1'''
    return findat.at[stock, 'fa_berryratio_ttm']


def fa_operincometopbt(stock):
    '''00210,1,1'''
    return findat.at[stock, 'fa_operincometopbt']


def fa_operincometopbt_ttm(stock):
    '''00211,1,1'''
    return findat.at[stock, 'fa_operincometopbt_ttm']


def fa_chgvaluetopbt_ttm(stock):
    '''00212,1,1'''
    return findat.at[stock, 'fa_chgvaluetopbt_ttm']


def fa_nonoperprofittopbt_ttm(stock):
    '''00213,1,1'''
    return findat.at[stock, 'fa_nonoperprofittopbt_ttm']


def fa_optopbt_ttm(stock):
    '''00214,1,1'''
    return findat.at[stock, 'fa_optopbt_ttm']


def fa_pbttoor_ttm(stock):
    '''00215,1,1'''
    return findat.at[stock, 'fa_pbttoor_ttm']


def fa_profittomv_ttm(stock):
    '''00216,1,1'''
    return findat.at[stock, 'fa_profittomv_ttm']


def fa_pttomvavg5y(stock):
    '''00217,1,1'''
    return findat.at[stock, 'fa_pttomvavg5y']


def fa_salescashtoor(stock):
    '''00218,1,1'''
    return findat.at[stock, 'fa_salescashtoor']


def fa_salescashtoor_ttm(stock):
    '''00219,1,1'''
    return findat.at[stock, 'fa_salescashtoor_ttm']


def fa_ocftoor(stock):
    '''00220,1,1'''
    return findat.at[stock, 'fa_ocftoor']


def fa_ocftoor_ttm(stock):
    '''00221,1,1'''
    return findat.at[stock, 'fa_ocftoor_ttm']


def fa_ocftooai_ttm(stock):
    '''00222,1,1'''
    return findat.at[stock, 'fa_ocftooai_ttm']


def fa_ocftoop_ttm(stock):
    '''00223,1,1'''
    return findat.at[stock, 'fa_ocftoop_ttm']


def fa_cashdivcover_ttm(stock):
    '''00224,1,1'''
    return findat.at[stock, 'fa_cashdivcover_ttm']


def fa_cashrecovratio_ttm(stock):
    '''00225,1,1'''
    return findat.at[stock, 'fa_cashrecovratio_ttm']


def fa_noncurassetsratio(stock):
    '''00226,1,1'''
    return findat.at[stock, 'fa_noncurassetsratio']


def fa_curassetsratio(stock):
    '''00227,1,1'''
    return findat.at[stock, 'fa_curassetsratio']


def fa_equitytointerestdebt(stock):
    '''00228,1,1'''
    return findat.at[stock, 'fa_equitytointerestdebt']


def fa_equitytocapital(stock):
    '''00229,1,1'''
    return findat.at[stock, 'fa_equitytocapital']


def fa_current(stock):
    '''00230,1,1'''
    return findat.at[stock, 'fa_current']


def fa_quick(stock):
    '''00231,1,1'''
    return findat.at[stock, 'fa_quick']


def fa_superquick(stock):
    '''00232,1,1'''
    return findat.at[stock, 'fa_superquick']


def fa_tangibleatointerestdebt(stock):
    '''00233,1,1'''
    return findat.at[stock, 'fa_tangibleatointerestdebt']


def fa_tangibleassettonetdebt(stock):
    '''00234,1,1'''
    return findat.at[stock, 'fa_tangibleassettonetdebt']


def fa_debttotangibleafybl(stock):
    '''00235,1,1'''
    return findat.at[stock, 'fa_debttotangibleafybl']


def fa_ocftodebt(stock):
    '''00236,1,1'''
    return findat.at[stock, 'fa_ocftodebt']


def fa_ocftointerestdebt_ttm(stock):
    '''00237,1,1'''
    return findat.at[stock, 'fa_ocftointerestdebt_ttm']


def fa_ocftonetdebt_ttm(stock):
    '''00238,1,1'''
    return findat.at[stock, 'fa_ocftonetdebt_ttm']


def fa_interestdebttocapital(stock):
    '''00239,1,1'''
    return findat.at[stock, 'fa_interestdebttocapital']


def fa_debttoequity(stock):
    '''00240,1,1'''
    return findat.at[stock, 'fa_debttoequity']


def fa_ebittointerest(stock):
    '''00241,1,1'''
    return findat.at[stock, 'fa_ebittointerest']


def fa_uncurdebttoworkcap(stock):
    '''00242,1,1'''
    return findat.at[stock, 'fa_uncurdebttoworkcap']


def fa_blev(stock):
    '''00243,1,1'''
    return findat.at[stock, 'fa_blev']


def fa_cfotocurliabs_ttm(stock):
    '''00244,1,1'''
    return findat.at[stock, 'fa_cfotocurliabs_ttm']


def fa_cashtocurliabs(stock):
    '''00245,1,1'''
    return findat.at[stock, 'fa_cashtocurliabs']


def fa_arturn_ttm(stock):
    '''00246,1,1'''
    return findat.at[stock, 'fa_arturn_ttm']


def fa_apturn_ttm(stock):
    '''00247,1,1'''
    return findat.at[stock, 'fa_apturn_ttm']


def fa_faturn_ttm(stock):
    '''00248,1,1'''
    return findat.at[stock, 'fa_faturn_ttm']


def fa_taturn_ttm(stock):
    '''00249,1,1'''
    return findat.at[stock, 'fa_taturn_ttm']


def fa_turndays_ttm(stock):
    '''00250,1,1'''
    return findat.at[stock, 'fa_turndays_ttm']


def fa_invturndays_ttm(stock):
    '''00251,1,1'''
    return findat.at[stock, 'fa_invturndays_ttm']


def fa_arturndays_ttm(stock):
    '''00252,1,1'''
    return findat.at[stock, 'fa_arturndays_ttm']


def fa_apturndays_ttm(stock):
    '''00253,1,1'''
    return findat.at[stock, 'fa_apturndays_ttm']


def fa_invturn_ttm(stock):
    '''00254,1,1'''
    return findat.at[stock, 'fa_invturn_ttm']


def fa_cashcnvcycle_ttm(stock):
    '''00255,1,1'''
    return findat.at[stock, 'fa_cashcnvcycle_ttm']


def fa_currtassetstrate_ttm(stock):
    '''00256,1,1'''
    return findat.at[stock, 'fa_currtassetstrate_ttm']


def fa_naturn_ttm(stock):
    '''00257,1,1'''
    return findat.at[stock, 'fa_naturn_ttm']


def fa_orgr_ttm(stock):
    '''00258,1,1'''
    return findat.at[stock, 'fa_orgr_ttm']


def fa_ncgr_ttm(stock):
    '''00259,1,1'''
    return findat.at[stock, 'fa_ncgr_ttm']


def fa_tpgr_ttm(stock):
    '''00260,1,1'''
    return findat.at[stock, 'fa_tpgr_ttm']


def fa_oigr_ttm(stock):
    '''00261,1,1'''
    return findat.at[stock, 'fa_oigr_ttm']


def fa_npgr_ttm(stock):
    '''00262,1,1'''
    return findat.at[stock, 'fa_npgr_ttm']


def fa_nppcgr_ttm(stock):
    '''00263,1,1'''
    return findat.at[stock, 'fa_nppcgr_ttm']


def fa_cfogr_ttm(stock):
    '''00264,1,1'''
    return findat.at[stock, 'fa_cfogr_ttm']


def fa_cffgr_ttm(stock):
    '''00265,1,1'''
    return findat.at[stock, 'fa_cffgr_ttm']


def fa_cfigr_ttm(stock):
    '''00266,1,1'''
    return findat.at[stock, 'fa_cfigr_ttm']


def fa_gpmgr_ttm(stock):
    '''00267,1,1'''
    return findat.at[stock, 'fa_gpmgr_ttm']


def fa_tagr(stock):
    '''00268,1,1'''
    return findat.at[stock, 'fa_tagr']


def fa_nagr(stock):
    '''00269,1,1'''
    return findat.at[stock, 'fa_nagr']


def fa_earnmom8qtr(stock):
    '''00270,1,1'''
    return findat.at[stock, 'fa_earnmom8qtr']


def fa_fcff(stock):
    '''00271,1,1'''
    return findat.at[stock, 'fa_fcff']


def fa_fcfe(stock):
    '''00272,1,1'''
    return findat.at[stock, 'fa_fcfe']


def fa_nrgl(stock):
    '''00273,1,1'''
    return findat.at[stock, 'fa_nrgl']


def fa_oaincome(stock):
    '''00274,1,1'''
    return findat.at[stock, 'fa_oaincome']


def fa_workcapital(stock):
    '''00275,1,1'''
    return findat.at[stock, 'fa_workcapital']


def fa_tangibleasset(stock):
    '''00276,1,1'''
    return findat.at[stock, 'fa_tangibleasset']


def fa_retainearn(stock):
    '''00277,1,1'''
    return findat.at[stock, 'fa_retainearn']


def fa_interestdebt(stock):
    '''00278,1,1'''
    return findat.at[stock, 'fa_interestdebt']


def fa_netdebt(stock):
    '''00279,1,1'''
    return findat.at[stock, 'fa_netdebt']


def fa_nicurdebt(stock):
    '''00280,1,1'''
    return findat.at[stock, 'fa_nicurdebt']


def fa_ninocurdebt(stock):
    '''00281,1,1'''
    return findat.at[stock, 'fa_ninocurdebt']


def fa_ebiat(stock):
    '''00282,1,1'''
    return findat.at[stock, 'fa_ebiat']


def fa_da(stock):
    '''00283,1,1'''
    return findat.at[stock, 'fa_da']


def fa_equity(stock):
    '''00284,1,1'''
    return findat.at[stock, 'fa_equity']


def fa_investcapital(stock):
    '''00285,1,1'''
    return findat.at[stock, 'fa_investcapital']


def fa_totassets(stock):
    '''00286,1,1'''
    return findat.at[stock, 'fa_totassets']


def fa_fixassets(stock):
    '''00287,1,1'''
    return findat.at[stock, 'fa_fixassets']


def fa_totliab(stock):
    '''00288,1,1'''
    return findat.at[stock, 'fa_totliab']


def fa_totequity(stock):
    '''00289,1,1'''
    return findat.at[stock, 'fa_totequity']


def fa_cce(stock):
    '''00290,1,1'''
    return findat.at[stock, 'fa_cce']


def fa_gr_ttm(stock):
    '''00291,1,1'''
    return findat.at[stock, 'fa_gr_ttm']


def fa_gc_ttm(stock):
    '''00292,1,1'''
    return findat.at[stock, 'fa_gc_ttm']


def fa_or_ttm(stock):
    '''00293,1,1'''
    return findat.at[stock, 'fa_or_ttm']


def fa_ocnf_ttm(stock):
    '''00294,1,1'''
    return findat.at[stock, 'fa_ocnf_ttm']


def fa_oef_ttm(stock):
    '''00295,1,1'''
    return findat.at[stock, 'fa_oef_ttm']


def fa_gp_ttm(stock):
    '''00296,1,1'''
    return findat.at[stock, 'fa_gp_ttm']


def fa_sellexpense_ttm(stock):
    '''00297,1,1'''
    return findat.at[stock, 'fa_sellexpense_ttm']


def fa_adminexpense_ttm(stock):
    '''00298,1,1'''
    return findat.at[stock, 'fa_adminexpense_ttm']


def fa_finaexpense_ttm(stock):
    '''00299,1,1'''
    return findat.at[stock, 'fa_finaexpense_ttm']


def fa_perexpense_ttm(stock):
    '''00300,1,1'''
    return findat.at[stock, 'fa_perexpense_ttm']


def fa_interestexpense_ttm(stock):
    '''00301,1,1'''
    return findat.at[stock, 'fa_interestexpense_ttm']


def fa_mininterest_ttm(stock):
    '''00302,1,1'''
    return findat.at[stock, 'fa_mininterest_ttm']


def fa_impairloss_ttm(stock):
    '''00303,1,1'''
    return findat.at[stock, 'fa_impairloss_ttm']


def fa_operactincome_ttm(stock):
    '''00304,1,1'''
    return findat.at[stock, 'fa_operactincome_ttm']


def fa_chavalincome_ttm(stock):
    '''00305,1,1'''
    return findat.at[stock, 'fa_chavalincome_ttm']


def fa_op_ttm(stock):
    '''00306,1,1'''
    return findat.at[stock, 'fa_op_ttm']


def fa_nooperprofit_ttm(stock):
    '''00307,1,1'''
    return findat.at[stock, 'fa_nooperprofit_ttm']


def fa_ebitunver_ttm(stock):
    '''00308,1,1'''
    return findat.at[stock, 'fa_ebitunver_ttm']


def fa_tax_ttm(stock):
    '''00309,1,1'''
    return findat.at[stock, 'fa_tax_ttm']


def fa_ebt_ttm(stock):
    '''00310,1,1'''
    return findat.at[stock, 'fa_ebt_ttm']


def fa_profit_ttm(stock):
    '''00311,1,1'''
    return findat.at[stock, 'fa_profit_ttm']


def fa_netprofit_ttm(stock):
    '''00312,1,1'''
    return findat.at[stock, 'fa_netprofit_ttm']


def fa_deductprofit_ttm(stock):
    '''00313,1,1'''
    return findat.at[stock, 'fa_deductprofit_ttm']


def fa_ebit_ttm(stock):
    '''00314,1,1'''
    return findat.at[stock, 'fa_ebit_ttm']


def fa_ebitdainver_ttm(stock):
    '''00315,1,1'''
    return findat.at[stock, 'fa_ebitdainver_ttm']


def fa_ebitda_ttm(stock):
    '''00316,1,1'''
    return findat.at[stock, 'fa_ebitda_ttm']


def fa_salescash_ttm(stock):
    '''00317,1,1'''
    return findat.at[stock, 'fa_salescash_ttm']


def fa_operactcashflow_ttm(stock):
    '''00318,1,1'''
    return findat.at[stock, 'fa_operactcashflow_ttm']


def fa_inveactcashflow_ttm(stock):
    '''00319,1,1'''
    return findat.at[stock, 'fa_inveactcashflow_ttm']


def fa_finaactcashflow_ttm(stock):
    '''00320,1,1'''
    return findat.at[stock, 'fa_finaactcashflow_ttm']

def fa_cashflow_ttm(stock):
    '''00321,1,1'''
    return findat.at[stock, 'fa_cashflow_ttm']

def fa_opertax_ttm(stock):
    '''00322,1,1'''
    return findat.at[stock, 'fa_opertax_ttm']

def total_shares(stock):
    '''00323,1,1'''
    return findat.at[stock, 'total_shares']

def free_float_shares(stock):
    '''00324,1,1'''
    return findat.at[stock, 'free_float_shares']
#==================finance functions end==================

#==================talib functions begin==================

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
#==================talib functions end==================

#==================Alpha 101 functions begin==================
def LQ_alpha101_001(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00462,4,1'''
    return LQA101.alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_002(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00463,4,1'''
    return LQA101.alpha_002(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_003(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00464,4,1'''
    return LQA101.alpha_003(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_004(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00465,4,1'''
    return LQA101.alpha_004(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_005(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00466,4,1'''
    return LQA101.alpha_005(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_006(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00467,4,1'''
    return LQA101.alpha_006(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_007(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00468,4,1'''
    return LQA101.alpha_007(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_008(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00469,4,1'''
    return LQA101.alpha_008(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_009(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00470,4,1'''
    return LQA101.alpha_009(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_010(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00471,4,1'''
    return LQA101.alpha_010(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_011(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00472,4,1'''
    return LQA101.alpha_011(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_012(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00473,4,1'''
    return LQA101.alpha_012(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_013(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00474,4,1'''
    return LQA101.alpha_013(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_014(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00475,4,1'''
    return LQA101.alpha_014(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_015(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00476,4,1'''
    return LQA101.alpha_015(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_016(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00477,4,1'''
    return LQA101.alpha_016(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_017(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00478,4,1'''
    return LQA101.alpha_017(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_018(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00479,4,1'''
    return LQA101.alpha_018(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_019(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00480,4,1'''
    return LQA101.alpha_019(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_020(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00481,4,1'''
    return LQA101.alpha_020(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_021(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00482,4,1'''
    return LQA101.alpha_021(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_022(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00483,4,1'''
    return LQA101.alpha_022(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_023(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00484,4,1'''
    return LQA101.alpha_023(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_024(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00485,4,1'''
    return LQA101.alpha_024(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_025(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00486,4,1'''
    return LQA101.alpha_025(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_026(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00487,4,1'''
    return LQA101.alpha_026(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_027(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00488,4,1'''
    return LQA101.alpha_027(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_028(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00489,4,1'''
    return LQA101.alpha_028(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_029(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00490,4,1'''
    return LQA101.alpha_029(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_030(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00491,4,1'''
    return LQA101.alpha_030(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_031(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00492,4,1'''
    return LQA101.alpha_031(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_032(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00493,4,1'''
    return LQA101.alpha_032(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_033(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00494,4,1'''
    return LQA101.alpha_033(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_034(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00495,4,1'''
    return LQA101.alpha_034(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_035(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00496,4,1'''
    return LQA101.alpha_035(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_036(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00497,4,1'''
    return LQA101.alpha_036(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_037(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00498,4,1'''
    return LQA101.alpha_037(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_038(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00499,4,1'''
    return LQA101.alpha_038(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_039(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00500,4,1'''
    return LQA101.alpha_039(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_040(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00501,4,1'''
    return LQA101.alpha_040(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_041(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00502,4,1'''
    return LQA101.alpha_041(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_042(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00503,4,1'''
    return LQA101.alpha_042(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_043(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00504,4,1'''
    return LQA101.alpha_043(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_044(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00505,4,1'''
    return LQA101.alpha_044(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_045(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00506,4,1'''
    return LQA101.alpha_045(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_046(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00507,4,1'''
    return LQA101.alpha_046(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_047(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00508,4,1'''
    return LQA101.alpha_047(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_048(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00509,4,1'''
    return LQA101.alpha_048(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_049(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00510,4,1'''
    return LQA101.alpha_049(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_050(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00511,4,1'''
    return LQA101.alpha_050(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_051(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00512,4,1'''
    return LQA101.alpha_051(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_052(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00513,4,1'''
    return LQA101.alpha_052(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_053(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00514,4,1'''
    return LQA101.alpha_053(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_054(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00515,4,1'''
    return LQA101.alpha_054(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_055(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00516,4,1'''
    return LQA101.alpha_055(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_056(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00517,4,1'''
    return LQA101.alpha_056(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_057(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00518,4,1'''
    return LQA101.alpha_057(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_058(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00519,4,1'''
    return LQA101.alpha_058(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_059(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00520,4,1'''
    return LQA101.alpha_059(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_060(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00521,4,1'''
    return LQA101.alpha_060(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_061(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00522,4,1'''
    return LQA101.alpha_061(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_062(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00523,4,1'''
    return LQA101.alpha_062(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_063(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00524,4,1'''
    return LQA101.alpha_063(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_064(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00525,4,1'''
    return LQA101.alpha_064(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_065(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00526,4,1'''
    return LQA101.alpha_065(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_066(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00527,4,1'''
    return LQA101.alpha_066(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_067(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00528,4,1'''
    return LQA101.alpha_067(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_068(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00529,4,1'''
    return LQA101.alpha_068(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_069(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00530,4,1'''
    return LQA101.alpha_069(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_070(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00531,4,1'''
    return LQA101.alpha_070(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_071(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00532,4,1'''
    return LQA101.alpha_071(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_072(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00533,4,1'''
    return LQA101.alpha_072(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_073(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00534,4,1'''
    return LQA101.alpha_073(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_074(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00535,4,1'''
    return LQA101.alpha_074(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_075(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00536,4,1'''
    return LQA101.alpha_075(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_076(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00537,4,1'''
    return LQA101.alpha_076(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_077(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00538,4,1'''
    return LQA101.alpha_077(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_078(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00539,4,1'''
    return LQA101.alpha_078(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_079(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00540,4,1'''
    return LQA101.alpha_079(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_080(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00541,4,1'''
    return LQA101.alpha_080(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_081(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00542,4,1'''
    return LQA101.alpha_081(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_082(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00543,4,1'''
    return LQA101.alpha_082(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_083(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00544,4,1'''
    return LQA101.alpha_083(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_084(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00545,4,1'''
    return LQA101.alpha_084(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_085(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00546,4,1'''
    return LQA101.alpha_085(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_086(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00547,4,1'''
    return LQA101.alpha_086(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_087(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00548,4,1'''
    return LQA101.alpha_087(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_088(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00549,4,1'''
    return LQA101.alpha_088(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_089(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00550,4,1'''
    return LQA101.alpha_089(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_090(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00551,4,1'''
    return LQA101.alpha_090(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_091(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00552,4,1'''
    return LQA101.alpha_091(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_092(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00553,4,1'''
    return LQA101.alpha_092(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_093(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00554,4,1'''
    return LQA101.alpha_093(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_094(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00555,4,1'''
    return LQA101.alpha_094(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_095(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00556,4,1'''
    return LQA101.alpha_095(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_096(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00557,4,1'''
    return LQA101.alpha_096(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_097(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00558,4,1'''
    return LQA101.alpha_097(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_098(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00559,4,1'''
    return LQA101.alpha_098(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_099(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00560,4,1'''
    return LQA101.alpha_099(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_100(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00561,4,1'''
    return LQA101.alpha_100(pool, begin_date, end_date, plat_form_type)

def LQ_alpha101_101(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    '''00562,4,1'''
    return LQA101.alpha_101(pool, begin_date, end_date, plat_form_type)
#==================Alpha 101 functions end==================

#==================Alpha 191 functions begin==================
def LQ_alpha191_001(code, end_date=None):
    '''00563,2,1'''
    return LQA191.alpha_001(code, end_date)

def LQ_alpha191_002(code, end_date=None):
    '''00564,2,1'''
    return LQA191.alpha_002(code, end_date)

def LQ_alpha191_003(code, end_date=None):
    '''00565,2,1'''
    return LQA191.alpha_003(code, end_date)

def LQ_alpha191_004(code, end_date=None):
    '''00566,2,1'''
    return LQA191.alpha_004(code, end_date)

def LQ_alpha191_005(code, end_date=None):
    '''00567,2,1'''
    return LQA191.alpha_005(code, end_date)

def LQ_alpha191_006(code, end_date=None):
    '''00568,2,1'''
    return LQA191.alpha_006(code, end_date)

def LQ_alpha191_007(code, end_date=None):
    '''00569,2,1'''
    return LQA191.alpha_007(code, end_date)

def LQ_alpha191_008(code, end_date=None):
    '''00570,2,1'''
    return LQA191.alpha_008(code, end_date)

def LQ_alpha191_009(code, end_date=None):
    '''00571,2,1'''
    return LQA191.alpha_009(code, end_date)

def LQ_alpha191_010(code, end_date=None):
    '''00572,2,1'''
    return LQA191.alpha_010(code, end_date)

def LQ_alpha191_011(code, end_date=None):
    '''00573,2,1'''
    return LQA191.alpha_011(code, end_date)

def LQ_alpha191_012(code, end_date=None):
    '''00574,2,1'''
    return LQA191.alpha_012(code, end_date)

def LQ_alpha191_013(code, end_date=None):
    '''00575,2,1'''
    return LQA191.alpha_013(code, end_date)

def LQ_alpha191_014(code, end_date=None):
    '''00576,2,1'''
    return LQA191.alpha_014(code, end_date)

def LQ_alpha191_015(code, end_date=None):
    '''00577,2,1'''
    return LQA191.alpha_015(code, end_date)

def LQ_alpha191_016(code, end_date=None):
    '''00578,2,1'''
    return LQA191.alpha_016(code, end_date)

def LQ_alpha191_017(code, end_date=None):
    '''00579,2,1'''
    return LQA191.alpha_017(code, end_date)

def LQ_alpha191_018(code, end_date=None):
    '''00580,2,1'''
    return LQA191.alpha_018(code, end_date)

def LQ_alpha191_019(code, end_date=None):
    '''00581,2,1'''
    return LQA191.alpha_019(code, end_date)

def LQ_alpha191_020(code, end_date=None):
    '''00582,2,1'''
    return LQA191.alpha_020(code, end_date)

def LQ_alpha191_021(code, end_date=None):
    '''00583,2,1'''
    return LQA191.alpha_021(code, end_date)

def LQ_alpha191_022(code, end_date=None):
    '''00584,2,1'''
    return LQA191.alpha_022(code, end_date)

def LQ_alpha191_023(code, end_date=None):
    '''00585,2,1'''
    return LQA191.alpha_023(code, end_date)

def LQ_alpha191_024(code, end_date=None):
    '''00586,2,1'''
    return LQA191.alpha_024(code, end_date)

def LQ_alpha191_025(code, end_date=None):
    '''00587,2,1'''
    return LQA191.alpha_025(code, end_date)

def LQ_alpha191_026(code, end_date=None):
    '''00588,2,1'''
    return LQA191.alpha_026(code, end_date)

def LQ_alpha191_027(code, end_date=None):
    '''00589,2,1'''
    return LQA191.alpha_027(code, end_date)

def LQ_alpha191_028(code, end_date=None):
    '''00590,2,1'''
    return LQA191.alpha_028(code, end_date)

def LQ_alpha191_029(code, end_date=None):
    '''00591,2,1'''
    return LQA191.alpha_029(code, end_date)

def LQ_alpha191_030(code, end_date=None):
    '''00592,2,1'''
    return LQA191.alpha_030(code, end_date)

def LQ_alpha191_031(code, end_date=None):
    '''00593,2,1'''
    return LQA191.alpha_031(code, end_date)

def LQ_alpha191_032(code, end_date=None):
    '''00594,2,1'''
    return LQA191.alpha_032(code, end_date)

def LQ_alpha191_033(code, end_date=None):
    '''00595,2,1'''
    return LQA191.alpha_033(code, end_date)

def LQ_alpha191_034(code, end_date=None):
    '''00596,2,1'''
    return LQA191.alpha_034(code, end_date)

def LQ_alpha191_035(code, end_date=None):
    '''00597,2,1'''
    return LQA191.alpha_035(code, end_date)

def LQ_alpha191_036(code, end_date=None):
    '''00598,2,1'''
    return LQA191.alpha_036(code, end_date)

def LQ_alpha191_037(code, end_date=None):
    '''00599,2,1'''
    return LQA191.alpha_037(code, end_date)

def LQ_alpha191_038(code, end_date=None):
    '''00600,2,1'''
    return LQA191.alpha_038(code, end_date)

def LQ_alpha191_039(code, end_date=None):
    '''00601,2,1'''
    return LQA191.alpha_039(code, end_date)

def LQ_alpha191_040(code, end_date=None):
    '''00602,2,1'''
    return LQA191.alpha_040(code, end_date)

def LQ_alpha191_041(code, end_date=None):
    '''00603,2,1'''
    return LQA191.alpha_041(code, end_date)

def LQ_alpha191_042(code, end_date=None):
    '''00604,2,1'''
    return LQA191.alpha_042(code, end_date)

def LQ_alpha191_043(code, end_date=None):
    '''00605,2,1'''
    return LQA191.alpha_043(code, end_date)

def LQ_alpha191_044(code, end_date=None):
    '''00606,2,1'''
    return LQA191.alpha_044(code, end_date)

def LQ_alpha191_045(code, end_date=None):
    '''00607,2,1'''
    return LQA191.alpha_045(code, end_date)

def LQ_alpha191_046(code, end_date=None):
    '''00608,2,1'''
    return LQA191.alpha_046(code, end_date)

def LQ_alpha191_047(code, end_date=None):
    '''00609,2,1'''
    return LQA191.alpha_047(code, end_date)

def LQ_alpha191_048(code, end_date=None):
    '''00610,2,1'''
    return LQA191.alpha_048(code, end_date)

def LQ_alpha191_049(code, end_date=None):
    '''00611,2,1'''
    return LQA191.alpha_049(code, end_date)

def LQ_alpha191_050(code, end_date=None):
    '''00612,2,1'''
    return LQA191.alpha_050(code, end_date)

def LQ_alpha191_051(code, end_date=None):
    '''00613,2,1'''
    return LQA191.alpha_051(code, end_date)

def LQ_alpha191_052(code, end_date=None):
    '''00614,2,1'''
    return LQA191.alpha_052(code, end_date)

def LQ_alpha191_053(code, end_date=None):
    '''00615,2,1'''
    return LQA191.alpha_053(code, end_date)

def LQ_alpha191_054(code, end_date=None):
    '''00616,2,1'''
    return LQA191.alpha_054(code, end_date)

def LQ_alpha191_055(code, end_date=None):
    '''00617,2,1'''
    return LQA191.alpha_055(code, end_date)

def LQ_alpha191_056(code, end_date=None):
    '''00618,2,1'''
    return LQA191.alpha_056(code, end_date)

def LQ_alpha191_057(code, end_date=None):
    '''00619,2,1'''
    return LQA191.alpha_057(code, end_date)

def LQ_alpha191_058(code, end_date=None):
    '''00620,2,1'''
    return LQA191.alpha_058(code, end_date)

def LQ_alpha191_059(code, end_date=None):
    '''00621,2,1'''
    return LQA191.alpha_059(code, end_date)

def LQ_alpha191_060(code, end_date=None):
    '''00622,2,1'''
    return LQA191.alpha_060(code, end_date)

def LQ_alpha191_061(code, end_date=None):
    '''00623,2,1'''
    return LQA191.alpha_061(code, end_date)

def LQ_alpha191_062(code, end_date=None):
    '''00624,2,1'''
    return LQA191.alpha_062(code, end_date)

def LQ_alpha191_063(code, end_date=None):
    '''00625,2,1'''
    return LQA191.alpha_063(code, end_date)

def LQ_alpha191_064(code, end_date=None):
    '''00626,2,1'''
    return LQA191.alpha_064(code, end_date)

def LQ_alpha191_065(code, end_date=None):
    '''00627,2,1'''
    return LQA191.alpha_065(code, end_date)

def LQ_alpha191_066(code, end_date=None):
    '''00628,2,1'''
    return LQA191.alpha_066(code, end_date)

def LQ_alpha191_067(code, end_date=None):
    '''00629,2,1'''
    return LQA191.alpha_067(code, end_date)

def LQ_alpha191_068(code, end_date=None):
    '''00630,2,1'''
    return LQA191.alpha_068(code, end_date)

def LQ_alpha191_069(code, end_date=None):
    '''00631,2,1'''
    return LQA191.alpha_069(code, end_date)

def LQ_alpha191_070(code, end_date=None):
    '''00632,2,1'''
    return LQA191.alpha_070(code, end_date)

def LQ_alpha191_071(code, end_date=None):
    '''00633,2,1'''
    return LQA191.alpha_071(code, end_date)

def LQ_alpha191_072(code, end_date=None):
    '''00634,2,1'''
    return LQA191.alpha_072(code, end_date)

def LQ_alpha191_073(code, end_date=None):
    '''00635,2,1'''
    return LQA191.alpha_073(code, end_date)

def LQ_alpha191_074(code, end_date=None):
    '''00636,2,1'''
    return LQA191.alpha_074(code, end_date)

def LQ_alpha191_075(code, end_date=None):
    '''00637,2,1'''
    return LQA191.alpha_075(code, end_date)

def LQ_alpha191_076(code, end_date=None):
    '''00638,2,1'''
    return LQA191.alpha_076(code, end_date)

def LQ_alpha191_077(code, end_date=None):
    '''00639,2,1'''
    return LQA191.alpha_077(code, end_date)

def LQ_alpha191_078(code, end_date=None):
    '''00640,2,1'''
    return LQA191.alpha_078(code, end_date)

def LQ_alpha191_079(code, end_date=None):
    '''00641,2,1'''
    return LQA191.alpha_079(code, end_date)

def LQ_alpha191_080(code, end_date=None):
    '''00642,2,1'''
    return LQA191.alpha_080(code, end_date)

def LQ_alpha191_081(code, end_date=None):
    '''00643,2,1'''
    return LQA191.alpha_081(code, end_date)

def LQ_alpha191_082(code, end_date=None):
    '''00644,2,1'''
    return LQA191.alpha_082(code, end_date)

def LQ_alpha191_083(code, end_date=None):
    '''00645,2,1'''
    return LQA191.alpha_083(code, end_date)

def LQ_alpha191_084(code, end_date=None):
    '''00646,2,1'''
    return LQA191.alpha_084(code, end_date)

def LQ_alpha191_085(code, end_date=None):
    '''00647,2,1'''
    return LQA191.alpha_085(code, end_date)

def LQ_alpha191_086(code, end_date=None):
    '''00648,2,1'''
    return LQA191.alpha_086(code, end_date)

def LQ_alpha191_087(code, end_date=None):
    '''00649,2,1'''
    return LQA191.alpha_087(code, end_date)

def LQ_alpha191_088(code, end_date=None):
    '''00650,2,1'''
    return LQA191.alpha_088(code, end_date)

def LQ_alpha191_089(code, end_date=None):
    '''00651,2,1'''
    return LQA191.alpha_089(code, end_date)

def LQ_alpha191_090(code, end_date=None):
    '''00652,2,1'''
    return LQA191.alpha_090(code, end_date)

def LQ_alpha191_091(code, end_date=None):
    '''00653,2,1'''
    return LQA191.alpha_091(code, end_date)

def LQ_alpha191_092(code, end_date=None):
    '''00654,2,1'''
    return LQA191.alpha_092(code, end_date)

def LQ_alpha191_093(code, end_date=None):
    '''00655,2,1'''
    return LQA191.alpha_093(code, end_date)

def LQ_alpha191_094(code, end_date=None):
    '''00656,2,1'''
    return LQA191.alpha_094(code, end_date)

def LQ_alpha191_095(code, end_date=None):
    '''00657,2,1'''
    return LQA191.alpha_095(code, end_date)

def LQ_alpha191_096(code, end_date=None):
    '''00658,2,1'''
    return LQA191.alpha_096(code, end_date)

def LQ_alpha191_097(code, end_date=None):
    '''00659,2,1'''
    return LQA191.alpha_097(code, end_date)

def LQ_alpha191_098(code, end_date=None):
    '''00660,2,1'''
    return LQA191.alpha_098(code, end_date)

def LQ_alpha191_099(code, end_date=None):
    '''00661,2,1'''
    return LQA191.alpha_099(code, end_date)

def LQ_alpha191_100(code, end_date=None):
    '''00662,2,1'''
    return LQA191.alpha_100(code, end_date)

def LQ_alpha191_101(code, end_date=None):
    '''00663,2,1'''
    return LQA191.alpha_101(code, end_date)

def LQ_alpha191_102(code, end_date=None):
    '''00664,2,1'''
    return LQA191.alpha_102(code, end_date)

def LQ_alpha191_103(code, end_date=None):
    '''00665,2,1'''
    return LQA191.alpha_103(code, end_date)

def LQ_alpha191_104(code, end_date=None):
    '''00666,2,1'''
    return LQA191.alpha_104(code, end_date)

def LQ_alpha191_105(code, end_date=None):
    '''00667,2,1'''
    return LQA191.alpha_105(code, end_date)

def LQ_alpha191_106(code, end_date=None):
    '''00668,2,1'''
    return LQA191.alpha_106(code, end_date)

def LQ_alpha191_107(code, end_date=None):
    '''00669,2,1'''
    return LQA191.alpha_107(code, end_date)

def LQ_alpha191_108(code, end_date=None):
    '''00670,2,1'''
    return LQA191.alpha_108(code, end_date)

def LQ_alpha191_109(code, end_date=None):
    '''00671,2,1'''
    return LQA191.alpha_109(code, end_date)

def LQ_alpha191_110(code, end_date=None):
    '''00672,2,1'''
    return LQA191.alpha_110(code, end_date)

def LQ_alpha191_111(code, end_date=None):
    '''00673,2,1'''
    return LQA191.alpha_111(code, end_date)

def LQ_alpha191_112(code, end_date=None):
    '''00674,2,1'''
    return LQA191.alpha_112(code, end_date)

def LQ_alpha191_113(code, end_date=None):
    '''00675,2,1'''
    return LQA191.alpha_113(code, end_date)

def LQ_alpha191_114(code, end_date=None):
    '''00676,2,1'''
    return LQA191.alpha_114(code, end_date)

def LQ_alpha191_115(code, end_date=None):
    '''00677,2,1'''
    return LQA191.alpha_115(code, end_date)

def LQ_alpha191_116(code, end_date=None):
    '''00678,2,1'''
    return LQA191.alpha_116(code, end_date)

def LQ_alpha191_117(code, end_date=None):
    '''00679,2,1'''
    return LQA191.alpha_117(code, end_date)

def LQ_alpha191_118(code, end_date=None):
    '''00680,2,1'''
    return LQA191.alpha_118(code, end_date)

def LQ_alpha191_119(code, end_date=None):
    '''00681,2,1'''
    return LQA191.alpha_119(code, end_date)

def LQ_alpha191_120(code, end_date=None):
    '''00682,2,1'''
    return LQA191.alpha_120(code, end_date)

def LQ_alpha191_121(code, end_date=None):
    '''00683,2,1'''
    return LQA191.alpha_121(code, end_date)

def LQ_alpha191_122(code, end_date=None):
    '''00684,2,1'''
    return LQA191.alpha_122(code, end_date)

def LQ_alpha191_123(code, end_date=None):
    '''00685,2,1'''
    return LQA191.alpha_123(code, end_date)

def LQ_alpha191_124(code, end_date=None):
    '''00686,2,1'''
    return LQA191.alpha_124(code, end_date)

def LQ_alpha191_125(code, end_date=None):
    '''00687,2,1'''
    return LQA191.alpha_125(code, end_date)

def LQ_alpha191_126(code, end_date=None):
    '''00688,2,1'''
    return LQA191.alpha_126(code, end_date)

def LQ_alpha191_127(code, end_date=None):
    '''00689,2,1'''
    return LQA191.alpha_127(code, end_date)

def LQ_alpha191_128(code, end_date=None):
    '''00690,2,1'''
    return LQA191.alpha_128(code, end_date)

def LQ_alpha191_129(code, end_date=None):
    '''00691,2,1'''
    return LQA191.alpha_129(code, end_date)

def LQ_alpha191_130(code, end_date=None):
    '''00692,2,1'''
    return LQA191.alpha_130(code, end_date)

def LQ_alpha191_131(code, end_date=None):
    '''00693,2,1'''
    return LQA191.alpha_131(code, end_date)

def LQ_alpha191_132(code, end_date=None):
    '''00694,2,1'''
    return LQA191.alpha_132(code, end_date)

def LQ_alpha191_133(code, end_date=None):
    '''00695,2,1'''
    return LQA191.alpha_133(code, end_date)

def LQ_alpha191_134(code, end_date=None):
    '''00696,2,1'''
    return LQA191.alpha_134(code, end_date)

def LQ_alpha191_135(code, end_date=None):
    '''00697,2,1'''
    return LQA191.alpha_135(code, end_date)

def LQ_alpha191_136(code, end_date=None):
    '''00698,2,1'''
    return LQA191.alpha_136(code, end_date)

def LQ_alpha191_137(code, end_date=None):
    '''00699,2,1'''
    return LQA191.alpha_137(code, end_date)

def LQ_alpha191_138(code, end_date=None):
    '''00700,2,1'''
    return LQA191.alpha_138(code, end_date)

def LQ_alpha191_139(code, end_date=None):
    '''00701,2,1'''
    return LQA191.alpha_139(code, end_date)

def LQ_alpha191_140(code, end_date=None):
    '''00702,2,1'''
    return LQA191.alpha_140(code, end_date)

def LQ_alpha191_141(code, end_date=None):
    '''00703,2,1'''
    return LQA191.alpha_141(code, end_date)

def LQ_alpha191_142(code, end_date=None):
    '''00704,2,1'''
    return LQA191.alpha_142(code, end_date)

def LQ_alpha191_143(code, end_date=None):
    '''00705,2,1'''
    return LQA191.alpha_143(code, end_date)

def LQ_alpha191_144(code, end_date=None):
    '''00706,2,1'''
    return LQA191.alpha_144(code, end_date)

def LQ_alpha191_145(code, end_date=None):
    '''00707,2,1'''
    return LQA191.alpha_145(code, end_date)

def LQ_alpha191_146(code, end_date=None):
    '''00708,2,1'''
    return LQA191.alpha_146(code, end_date)

def LQ_alpha191_147(code, end_date=None):
    '''00709,2,1'''
    return LQA191.alpha_147(code, end_date)

def LQ_alpha191_148(code, end_date=None):
    '''00710,2,1'''
    return LQA191.alpha_148(code, end_date)

def LQ_alpha191_149(code, end_date=None):
    '''00711,2,1'''
    return LQA191.alpha_149(code, end_date)

def LQ_alpha191_150(code, end_date=None):
    '''00712,2,1'''
    return LQA191.alpha_150(code, end_date)

def LQ_alpha191_151(code, end_date=None):
    '''00713,2,1'''
    return LQA191.alpha_151(code, end_date)

def LQ_alpha191_152(code, end_date=None):
    '''00714,2,1'''
    return LQA191.alpha_152(code, end_date)

def LQ_alpha191_153(code, end_date=None):
    '''00715,2,1'''
    return LQA191.alpha_153(code, end_date)

def LQ_alpha191_154(code, end_date=None):
    '''00716,2,1'''
    return LQA191.alpha_154(code, end_date)

def LQ_alpha191_155(code, end_date=None):
    '''00717,2,1'''
    return LQA191.alpha_155(code, end_date)

def LQ_alpha191_156(code, end_date=None):
    '''00718,2,1'''
    return LQA191.alpha_156(code, end_date)

def LQ_alpha191_157(code, end_date=None):
    '''00719,2,1'''
    return LQA191.alpha_157(code, end_date)

def LQ_alpha191_158(code, end_date=None):
    '''00720,2,1'''
    return LQA191.alpha_158(code, end_date)

def LQ_alpha191_159(code, end_date=None):
    '''00721,2,1'''
    return LQA191.alpha_159(code, end_date)

def LQ_alpha191_160(code, end_date=None):
    '''00722,2,1'''
    return LQA191.alpha_160(code, end_date)

def LQ_alpha191_161(code, end_date=None):
    '''00723,2,1'''
    return LQA191.alpha_161(code, end_date)

def LQ_alpha191_162(code, end_date=None):
    '''00724,2,1'''
    return LQA191.alpha_162(code, end_date)

def LQ_alpha191_163(code, end_date=None):
    '''00725,2,1'''
    return LQA191.alpha_163(code, end_date)

def LQ_alpha191_164(code, end_date=None):
    '''00726,2,1'''
    return LQA191.alpha_164(code, end_date)

def LQ_alpha191_165(code, end_date=None):
    '''00727,2,1'''
    return LQA191.alpha_165(code, end_date)

def LQ_alpha191_166(code, end_date=None):
    '''00728,2,1'''
    return LQA191.alpha_166(code, end_date)

def LQ_alpha191_167(code, end_date=None):
    '''00729,2,1'''
    return LQA191.alpha_167(code, end_date)

def LQ_alpha191_168(code, end_date=None):
    '''00730,2,1'''
    return LQA191.alpha_168(code, end_date)

def LQ_alpha191_169(code, end_date=None):
    '''00731,2,1'''
    return LQA191.alpha_169(code, end_date)

def LQ_alpha191_170(code, end_date=None):
    '''00732,2,1'''
    return LQA191.alpha_170(code, end_date)

def LQ_alpha191_171(code, end_date=None):
    '''00733,2,1'''
    return LQA191.alpha_171(code, end_date)

def LQ_alpha191_172(code, end_date=None):
    '''00734,2,1'''
    return LQA191.alpha_172(code, end_date)

def LQ_alpha191_173(code, end_date=None):
    '''00735,2,1'''
    return LQA191.alpha_173(code, end_date)

def LQ_alpha191_174(code, end_date=None):
    '''00736,2,1'''
    return LQA191.alpha_174(code, end_date)

def LQ_alpha191_175(code, end_date=None):
    '''00737,2,1'''
    return LQA191.alpha_175(code, end_date)

def LQ_alpha191_176(code, end_date=None):
    '''00738,2,1'''
    return LQA191.alpha_176(code, end_date)

def LQ_alpha191_177(code, end_date=None):
    '''00739,2,1'''
    return LQA191.alpha_177(code, end_date)

def LQ_alpha191_178(code, end_date=None):
    '''00740,2,1'''
    return LQA191.alpha_178(code, end_date)

def LQ_alpha191_179(code, end_date=None):
    '''00741,2,1'''
    return LQA191.alpha_179(code, end_date)

def LQ_alpha191_180(code, end_date=None):
    '''00742,2,1'''
    return LQA191.alpha_180(code, end_date)

def LQ_alpha191_181(code, end_date=None):
    '''00743,2,1'''
    return LQA191.alpha_181(code, end_date)

def LQ_alpha191_182(code, end_date=None):
    '''00744,2,1'''
    return LQA191.alpha_182(code, end_date)

def LQ_alpha191_183(code, end_date=None):
    '''00745,2,1'''
    return LQA191.alpha_183(code, end_date)

def LQ_alpha191_184(code, end_date=None):
    '''00746,2,1'''
    return LQA191.alpha_184(code, end_date)

def LQ_alpha191_185(code, end_date=None):
    '''00747,2,1'''
    return LQA191.alpha_185(code, end_date)

def LQ_alpha191_186(code, end_date=None):
    '''00748,2,1'''
    return LQA191.alpha_186(code, end_date)

def LQ_alpha191_187(code, end_date=None):
    '''00749,2,1'''
    return LQA191.alpha_187(code, end_date)

def LQ_alpha191_188(code, end_date=None):
    '''00750,2,1'''
    return LQA191.alpha_188(code, end_date)

def LQ_alpha191_189(code, end_date=None):
    '''00751,2,1'''
    return LQA191.alpha_189(code, end_date)

def LQ_alpha191_190(code, end_date=None):
    '''00752,2,1'''
    return LQA191.alpha_190(code, end_date)

def LQ_alpha191_191(code, end_date=None):
    '''00753,2,1'''
    return LQA191.alpha_191(code, end_date)
#==================Alpha 191 functions end==================
