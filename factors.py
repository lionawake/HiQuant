#!/usr/bin/python
# -*- coding: utf8 -*-

from hikyuu.indicator import *
import talib
from LqWQ101 import *

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

def lqTA_AD(ind=None):
	'''00021,1,1'''
	return TA_AD(ind)

def lqTA_ADOSC(ind=None, fastperiod=3, slowperiod=10):
	'''00021,3,1'''
	return TA_ADOSC(ind, fastperiod, slowperiod)

def lqTA_ADX(ind=None, timeperiod=14):
	'''00022,2,1'''
	return TA_ADX(ind, timeperiod)

def lqTA_ADXR(ind=None, timeperiod=14):
	'''00023,2,1'''
	return TA_ADXR(ind, timeperiod)

def lqTA_APO(ind=None, fastperiod=12, slowperiod=26, matype=talib.MA_Type.SMA):
	'''00024,4,1'''
	return TA_APO(ind, fastperiod, slowperiod, matype)

def lqTA_AROON(ind=None, timeperiod=14):
	'''00025,2,2'''
	return TA_AROON(ind, timeperiod)

def lqTA_AROONOSC(ind=None, timeperiod=14):
	'''00026,2,1'''
	return TA_AROONOSC(ind, timeperiod)

def lqTA_ATR(ind=None, timeperiod=14):
	'''00027,2,1'''
	return TA_ATR(ind, timeperiod)

def lqTA_AVGPRICE(ind=None, timeperiod=14):
	'''00028,2,1'''
	return TA_AVGPRICE(ind, timeperiod)

def lqTA_BBANDS(ind=None, timeperiod=14, nbdevup=2, nbdevdn=2, matype=talib.MA_Type.SMA):
	'''00029,5,3'''
	return TA_BBANDS(ind, timeperiod, nbdevup, nbdevdn, matype)

def lqTA_BOP(ind=None):
	'''00030,1,1'''
	return TA_BOP(ind)

def lqTA_CCI(ind=None, timeperiod=14):
	'''00031,2,1'''
	return TA_CCI(ind, timeperiod)

def lqTA_CMO(ind=None, timeperiod=14):
	'''00032,2,1'''
	return TA_CMO(ind, timeperiod)

def lqTA_DEMA(ind=None, timeperiod=30):
	'''00033,2,1'''
	return TA_DEMA(ind, timeperiod)

def lqTA_DX(ind=None, timeperiod=14):
	'''00033,2,1'''
	return TA_DX(ind, timeperiod)

def lqTA_EMA(ind=None, timeperiod=30):
	'''00034,2,1'''
	return TA_EMA(ind, timeperiod)

def lqTA_HT_DCPERIOD(ind=None):
	'''00035,1,1'''
	return TA_HT_DCPERIOD(ind)

def lqTA_HT_DCPHASE(ind=None):
	'''00036,1,1'''
	return TA_HT_DCPHASE(ind)

def lqTA_HT_PHASOR(ind=None):
	'''00037,1,2'''
	return TA_HT_PHASOR(ind)

def lqTA_HT_SINE(ind=None):
	'''00038,1,2'''
	return TA_HT_SINE(ind)

def lqTA_HT_TRENDLINE(ind=None):
	'''00039,1,1'''
	return TA_HT_TRENDLINE(ind)

def lqTA_HT_TRENDMODE(ind=None):
	'''00040,1,1'''
	return TA_HT_TRENDMODE(ind)

def lqTA_KAMA(ind=None, timeperiod=30):
	'''00041,2,1'''
	return TA_KAMA(ind, timeperiod)

def lqTA_LINEARREG(ind=None, timeperiod=14):
	'''00042,2,1'''
	return TA_LINEARREG(ind, timeperiod)

def lqTA_LINEARREG_ANGLE(ind=None, timeperiod=14):
	'''00043,2,1'''
	return TA_LINEARREG_ANGLE(ind, timeperiod)

def lqTA_LINEARREG_INTERCEPT(ind=None, timeperiod=14):
	'''00044,2,1'''
	return TA_LINEARREG_INTERCEPT(ind, timeperiod)

def lqTA_LINEARREG_SLOPE(ind=None, timeperiod=14):
	'''00045,2,1'''
	return TA_LINEARREG_SLOPE(ind, timeperiod)

def lqTA_MA(ind=None, timeperiod=30, matype=talib.MA_Type.SMA):
	'''00046,3,1'''
	return TA_MA(ind, timeperiod, matype)

def lqTA_MACD(ind=None, fastperiod=12, slowperiod=26, signalperiod=9):
	'''00047,4,3'''
	return TA_MACD(ind, fastperiod, slowperiod, signalperiod)

def lqTA_MACDEXT(ind=None, fastperiod=12, fastmatype=talib.MA_Type.SMA, 
                slowperiod=26, slowmatype=talib.MA_Type.SMA, 
                signalperiod=9, signalmatype=talib.MA_Type.SMA):
	'''00048,7,3'''
	return TA_MACDEXT(ind, fastperiod, fastmatype, 
                slowperiod, slowmatype, 
                signalperiod, signalmatype)

def lqTA_MACDFIX(ind=None, signalperiod=9):
	'''00049,2,3'''
	return TA_MACDFIX(ind, signalperiod)

def lqTA_MAMA(ind=None, fastlimit=0.5, slowlimit=0.05):
	'''00050,3,2'''
	return TA_MAMA(ind, fastlimit, slowlimit)

def lqTA_MAX(ind=None, timeperiod=30):
	'''00051,2,1'''
	return TA_MAX(ind, timeperiod)

def lqTA_MAXINDEX(ind=None, timeperiod=30):
	'''00052,2,1'''
	return TA_MAXINDEX(ind, timeperiod)

def lqTA_MEDPRICE(ind=None):
	'''00053,1,1'''
	return TA_MEDPRICE(ind)

def lqTA_MIDPOINT(ind=None, timeperiod=14):
	'''00054,2,1'''
	return TA_MIDPOINT(ind, timeperiod)

def lqTA_MIDPRICE(ind=None, timeperiod=14):
	'''00055,2,1'''
	return TA_MIDPRICE(ind, timeperiod)

def lqTA_MIN(ind=None, timeperiod=30):
	'''00056,2,1'''
	return TA_MIN(ind, timeperiod)

def lqTA_MININDEX(ind=None, timeperiod=30):
	'''00057,2,1'''
	return TA_MININDEX(ind, timeperiod)

def lqTA_MINMAX(ind=None, timeperiod=30):
	'''00058,2,2'''
	return TA_MINMAX(ind, timeperiod)

def lqTA_MINMAXINDEX(ind=None, timeperiod=30):
	'''00059,2,2'''
	return TA_MINMAXINDEX(ind, timeperiod)

def lqTA_MINUS_DI(ind=None, timeperiod=14):
	'''00060,2,1'''
	return TA_MINUS_DI(ind, timeperiod)

def lqTA_MINUS_DM(ind=None, timeperiod=14):
	'''00061,2,1'''
	return TA_MINUS_DM(ind, timeperiod)

def lqTA_MOM(ind=None, timeperiod=10):
	'''00062,2,1'''
	return TA_MOM(ind, timeperiod)

def lqTA_NATR(ind=None, timeperiod=14):
	'''00063,2,1'''
	return TA_NATR(ind, timeperiod)

def lqTA_PLUS_DI(ind=None, timeperiod=14):
	'''00064,2,1'''
	return TA_PLUS_DI(ind, timeperiod)

def lqTA_PLUS_DM(ind=None, timeperiod=14):
	'''00065,2,1'''
	return TA_PLUS_DM(ind, timeperiod)

def lqTA_PPO(ind=None, fastperiod=12, slowperiod=26, matype=talib.MA_Type.SMA):
	'''00066,4,1'''
	return TA_PPO(ind, fastperiod, slowperiod, matype)

def lqTA_ROC(ind=None, timeperiod=10):
	'''00067,2,1'''
	return TA_ROC(ind, timeperiod)

def lqTA_ROCP(ind=None, timeperiod=10):
	'''00068,2,1'''
	return TA_ROCP(ind, timeperiod)

def lqTA_ROCR(ind=None, timeperiod=10):
	'''00069,2,1'''
	return TA_ROCR(ind, timeperiod)

def lqTA_ROCR100(ind=None, timeperiod=10):
	'''00070,2,1'''
	return TA_ROCR100(ind, timeperiod)

def lqTA_RSI(ind=None, timeperiod=14):
	'''00071,2,1'''
	return TA_RSI(ind, timeperiod)

def lqTA_SAR(ind=None, acceleration=0.02, maximum=0.2):
	'''00072,3,1'''
	return TA_SAR(ind, acceleration, maximum)

def lqTA_SAREXT(ind=None, startvalue=0, 
                 offsetonreverse=0,
                 accelerationinitlong=0.02,
                 accelerationlong=0.02,
                 accelerationmaxlong=0.02,
                 accelerationinitshort=0.02,
                 accelerationshort=0.02,
                 accelerationmaxshort=0.02):
	'''00073,9,1'''
	return TA_SAREXT(ind, startvalue, 
                 offsetonreverse,
                 accelerationinitlong,
                 accelerationlong,
                 accelerationmaxlong,
                 accelerationinitshort,
                 accelerationshort,
                 accelerationmaxshort)

def lqTA_SMA(ind=None, timeperiod=30):
	'''00074,2,1'''
	return TA_SMA(ind, timeperiod)

def lqTA_STDDEV(ind=None, timeperiod=5, nbdev=1):
	'''00075,3,1'''
	return TA_STDDEV(ind, timeperiod, nbdev)

def lqTA_STOCH(ind=None, fastk_period=5, 
                 slowk_period=3, slowk_matype=talib.MA_Type.SMA,
                 slowd_period=3, slowd_matype=talib.MA_Type.SMA):
	'''00076,6,2'''
	return TA_STOCH(ind, fastk_period, 
                 slowk_period, slowk_matype,
                 slowd_period, slowd_matype)

def lqTA_STOCHF(ind=None, fastk_period=5, fastd_period=3, fastd_matype=talib.MA_Type.SMA):
	'''00077,4,2'''
	return TA_STOCHF(ind, fastk_period, fastd_period, fastd_matype)

def lqTA_STOCHRSI(ind=None, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=talib.MA_Type.SMA):
	'''00078,5,2'''
	return TA_STOCHRSI(ind, timeperiod, fastk_period, fastd_period, fastd_matype)

def lqTA_SUM(ind=None, timeperiod=30):
	'''00079,2,1'''
	return TA_SUM(ind, timeperiod)

def lqTA_T3(ind=None, timeperiod=5, vfactor=0.7):
	'''00080,3,1'''
	return TA_T3(ind, timeperiod, vfactor)

def lqTA_TEMA(ind=None, timeperiod=30):
	'''00081,2,1'''
	return TA_TEMA(ind, timeperiod)

def lqTA_TRANGE(ind=None):
	'''00082,1,1'''
	return TA_TRANGE(ind)

def lqTA_TRIMA(ind=None, timeperiod=30):
	'''00083,2,1'''
	return TA_TRIMA(ind, timeperiod)

def lqTA_TRIX(ind=None, timeperiod=30):
	'''00084,2,1'''
	return TA_TRIX(ind, timeperiod)

def lqTA_TSF(ind=None, timeperiod=14):
	'''00085,2,1'''
	return TA_TSF(ind, timeperiod)

def lqTA_TYPPRICE(ind=None, timeperiod=14):
	'''00086,2,1'''
	return TA_TYPPRICE(ind, timeperiod)

def lqTA_ULTOSC(ind=None, timeperiod1=7, timeperiod2=14, timeperiod3=28):
	'''00087,4,1'''
	return TA_ULTOSC(ind, timeperiod1, timeperiod2, timeperiod3)

def lqTA_VAR(ind=None, timeperiod=5, nbdev=1):
	'''00088,3,1'''
	return TA_VAR(ind, timeperiod, nbdev)

def lqTA_WCLPRICE(ind=None):
	'''00089,1,1'''
	return TA_WCLPRICE(ind)

def lqTA_WILLR(ind=None, timeperiod=14):
	'''00090,2,1'''
	return TA_WILLR(ind, timeperiod)

def lqTA_WMA(ind=None, timeperiod=30):
	'''00091,2,1'''
	return TA_WMA(ind, timeperiod)

def lqTA_CDL2CROWS(ind=None):
	'''00092,1,1'''
	return TA_CDL2CROWS(ind)

def lqTA_CDL3BLACKCROWS(ind=None):
	'''00093,1,1'''
	return TA_CDL3BLACKCROWS(ind)

def lqTA_CDL3INSIDE(ind=None):
	'''00094,1,1'''
	return TA_CDL3INSIDE(ind)

def lqTA_CDL3LINESTRIKE(ind=None):
	'''00095,1,1'''
	return TA_CDL3LINESTRIKE(ind)

def lqTA_CDL3OUTSIDE(ind=None):
	'''00096,1,1'''
	return TA_CDL3OUTSIDE(ind)

def lqTA_CDL3STARSINSOUTH(ind=None):
	'''00097,1,1'''
	return TA_CDL3STARSINSOUTH(ind)

def lqTA_CDL3WHITESOLDIERS(ind=None):
	'''00098,1,1'''
	return TA_CDL3WHITESOLDIERS(ind)

def lqTA_CDLABANDONEDBABY(ind=None, penetration=0.3):
	'''00099,2,1'''
	return TA_CDLABANDONEDBABY(ind, penetration)

def lqTA_CDLADVANCEBLOCK(ind=None):
	'''00100,1,1'''
	return TA_CDLADVANCEBLOCK(ind)

def lqTA_CDLBELTHOLD(ind=None):
	'''00101,1,1'''
	return TA_CDLBELTHOLD(ind)

def lqTA_CDLBREAKAWAY(ind=None):
	'''00102,1,1'''
	return TA_CDLBREAKAWAY(ind)

def lqTA_CDLCLOSINGMARUBOZU(ind=None):
	'''00103,1,1'''
	return TA_CDLCLOSINGMARUBOZU(ind)

def lqTA_CDLCONCEALBABYSWALL(ind=None):
	'''00104,1,1'''
	return TA_CDLCONCEALBABYSWALL(ind)

def lqTA_CDLCOUNTERATTACK(ind=None):
	'''00105,1,1'''
	return TA_CDLCOUNTERATTACK(ind)

def lqTA_CDLDARKCLOUDCOVER(ind=None, penetration=0.5):
	'''00106,2,1'''
	return TA_CDLDARKCLOUDCOVER(ind, penetration)

def lqTA_CDLDOJI(ind=None):
	'''00107,1,1'''
	return TA_CDLDOJI(ind)

def lqTA_CDLDOJISTAR(ind=None):
	'''00108,1,1'''
	return TA_CDLDOJISTAR(ind)

def lqTA_CDLDRAGONFLYDOJI(ind=None):
	'''00109,1,1'''
	return TA_CDLDRAGONFLYDOJI(ind)

def lqTA_CDLENGULFING(ind=None):
	'''00110,1,1'''
	return TA_CDLENGULFING(ind)

def lqTA_CDLEVENINGDOJISTAR(ind=None, penetration=0.3):
	'''00111,2,1'''
	return TA_CDLEVENINGDOJISTAR(ind, penetration)

def lqTA_CDLEVENINGSTAR(ind=None, penetration=0.3):
	'''00112,2,1'''
	return TA_CDLEVENINGSTAR(ind, penetration)

def lqTA_CDLGAPSIDESIDEWHITE(ind=None):
	'''00113,1,1'''
	return TA_CDLGAPSIDESIDEWHITE(ind)

def lqTA_CDLGRAVESTONEDOJI(ind=None):
	'''00114,1,1'''
	return TA_CDLGRAVESTONEDOJI(ind)

def lqTA_CDLHAMMER(ind=None):
	'''00115,1,1'''
	return TA_CDLHAMMER(ind)

def lqTA_CDLHANGINGMAN(ind=None):
	'''00116,1,1'''
	return TA_CDLHANGINGMAN(ind)

def lqTA_CDLHARAMI(ind=None):
	'''00117,1,1'''
	return TA_CDLHARAMI(ind)

def lqTA_CDLHARAMICROSS(ind=None):
	'''00118,1,1'''
	return TA_CDLHARAMICROSS(ind)

def lqTA_CDLHIGHWAVE(ind=None):
	'''00119,1,1'''
	return TA_CDLHIGHWAVE(ind)

def lqTA_CDLHIKKAKE(ind=None):
	'''00120,1,1'''
	return TA_CDLHIKKAKE(ind)

def lqTA_CDLHIKKAKEMOD(ind=None):
	'''00121,1,1'''
	return TA_CDLHIKKAKEMOD(ind)

def lqTA_CDLHOMINGPIGEON(ind=None):
	'''00122,1,1'''
	return TA_CDLHOMINGPIGEON(ind)

def lqTA_CDLIDENTICAL3CROWS(ind=None):
	'''00123,1,1'''
	return TA_CDLIDENTICAL3CROWS(ind)

def lqTA_CDLINNECK(ind=None):
	'''00124,1,1'''
	return TA_CDLINNECK(ind)

def lqTA_CDLINVERTEDHAMMER(ind=None):
	'''00125,1,1'''
	returnTA_CDLINVERTEDHAMMER(ind)

def lqTA_CDLKICKING(ind=None):
	'''00126,1,1'''
	return TA_CDLKICKING(ind)

def lqTA_CDLKICKINGBYLENGTH(ind=None):
	'''00127,1,1'''
	return TA_CDLKICKINGBYLENGTH(ind)

def lqTA_CDLLADDERBOTTOM(ind=None):
	'''00128,1,1'''
	return TA_CDLLADDERBOTTOM(ind)

def lqTA_CDLLONGLEGGEDDOJI(ind=None):
	'''00129,1,1'''
	return TA_CDLLONGLEGGEDDOJI(ind)

def lqTA_CDLLONGLINE(ind=None):
	'''00130,1,1'''
	return TA_CDLLONGLINE(ind)

def lqTA_CDLMARUBOZU(ind=None):
	'''00131,1,1'''
	return TA_CDLMARUBOZU(ind)

def lqTA_CDLMATCHINGLOW(ind=None):
	'''00132,1,1'''
	return TA_CDLMATCHINGLOW(ind)

def lqTA_CDLMATHOLD(ind=None, penetration=0.5):
	'''00133,1,1'''
	return TA_CDLMATHOLD(ind, penetration)

def lqTA_CDLMORNINGDOJISTAR(ind=None, penetration=0.3):
	'''00134,2,1'''
	return TA_CDLMORNINGDOJISTAR(ind, penetration)

def lqTA_CDLMORNINGSTAR(ind=None, penetration=0.3):
	'''00135,2,1'''
	return TA_CDLMORNINGSTAR(ind, penetration)

def lqTA_CDLONNECK(ind=None):
	'''00136,1,1'''
	return TA_CDLONNECK(ind)

def lqTA_CDLPIERCING(ind=None):
	'''00137,1,1'''
	return TA_CDLPIERCING(ind)

def lqTA_CDLRICKSHAWMAN(ind=None):
	'''00138,1,1'''
	return TA_CDLRICKSHAWMAN(ind)

def lqTA_CDLRISEFALL3METHODS(ind=None):
	'''00139,1,1'''
	return TA_CDLRISEFALL3METHODS(ind)

def lqTA_CDLSEPARATINGLINES(ind=None):
	'''00140,1,1'''
	return TA_CDLSEPARATINGLINES(ind)

def lqTA_CDLSHOOTINGSTAR(ind=None):
	'''00141,1,1'''
	return TA_CDLSHOOTINGSTAR(ind)

def lqTA_CDLSHORTLINE(ind=None):
	'''00142,1,1'''
	return TA_CDLSHORTLINE(ind)

def lqTA_CDLSPINNINGTOP(ind=None):
	'''00143,1,1'''
	return TA_CDLSPINNINGTOP(ind)

def lqTA_CDLSTALLEDPATTERN(ind=None):
	'''00144,1,1'''
	return TA_CDLSTALLEDPATTERN(ind)

def lqTA_CDLSTICKSANDWICH(ind=None):
	'''00145,1,1'''
	return TA_CDLSTICKSANDWICH(ind)

def lqTA_CDLTAKURI(ind=None):
	'''00146,1,1'''
	return TA_CDLTAKURI(ind)

def lqTA_CDLTASUKIGAP(ind=None):
	'''00147,1,1'''
	return TA_CDLTASUKIGAP(ind)

def lqTA_CDLTHRUSTING(ind=None):
	'''00148,1,1'''
	return TA_CDLTHRUSTING(ind)

def lqTA_CDLTRISTAR(ind=None):
	'''00149,1,1'''
	return TA_CDLTRISTAR(ind)

def lqTA_CDLUNIQUE3RIVER(ind=None):
	'''00150,1,1'''
	return TA_CDLUNIQUE3RIVER(ind)

def lqTA_CDLUPSIDEGAP2CROWS(ind=None):
	'''00151,1,1'''
	return TA_CDLUPSIDEGAP2CROWS(ind)

def lqTA_CDLXSIDEGAP3METHODS(ind=None):
	'''00152,1,1'''
	return TA_CDLXSIDEGAP3METHODS(ind)

def lqTA_BETA(ind=None, timeperiod=5):
	'''00153,2,1'''
	return TA_BETA(ind, timeperiod)

def lqTA_CORREL(ind=None, timeperiod=30):
	'''00154,2,1'''
	return TA_CORREL(ind, timeperiod)

def lqTA_OBV(ind=None):
	'''00155,1,1'''
	return TA_OBV(ind)


def LQ_WQ_alpha_001(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00501,2,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_002(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00502,2,1"""
    return alpha_002(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_003(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00503,2,1"""
    return alpha_003(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_004(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00504,2,1"""
    return alpha_004(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_005(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00505,2,1"""
    return alpha_005(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_006(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00506,2,1"""
    return alpha_006(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_007(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00507,2,1"""
    return alpha_007(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_008(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00508,2,1"""
    return alpha_008(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_009(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00509,2,1"""
    return alpha_009(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_010(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00510,2,1"""
    return alpha_010(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_011(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00511,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_012(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00512,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_013(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00513,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_014(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00514,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_015(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00515,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_016(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00516,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_017(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00517,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_018(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00518,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_019(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00519,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_020(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00520,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_021(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00521,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_022(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00522,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_023(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00523,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_024(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00524,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_025(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00525,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_026(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00526,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_027(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00527,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_028(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00528,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_029(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00529,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_030(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00530,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_031(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00531,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_032(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00532,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_033(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00533,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_034(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00534,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_035(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00535,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_036(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00536,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_037(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00537,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_038(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00538,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_039(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00539,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_040(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00540,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_041(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00541,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_042(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00542,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_043(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00543,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_044(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00544,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_045(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00545,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_046(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00546,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_047(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00547,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_048(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00548,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_049(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00549,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_050(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00550,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_051(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00551,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_052(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00552,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_053(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00553,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_054(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00554,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_055(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00555,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_056(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00556,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_057(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00557,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_058(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00558,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_059(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00559,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_060(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00560,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_061(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00561,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_062(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00562,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_063(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00563,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_064(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00564,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_065(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00565,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_066(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00566,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_067(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00567,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_068(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00568,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_069(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00569,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_070(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00570,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_071(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00571,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_072(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00572,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_073(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00573,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_074(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00574,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_075(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00575,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_076(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00576,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_077(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00577,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_078(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00578,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_079(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00579,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_080(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00580,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_081(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00581,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_082(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00582,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_083(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00583,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_084(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00584,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_085(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00585,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_086(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00586,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_087(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00587,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_088(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00588,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_089(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00589,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_090(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00590,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_091(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00591,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_092(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00592,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_093(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00593,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_094(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00594,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_095(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00595,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_096(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00596,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_097(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00597,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_098(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00598,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_099(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00599,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_100(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00600,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)

def LQ_WQ_alpha_101(pool=None, begin_date=None, end_date=None, plat_form_type='QA'):
    """00601,4,1"""
    return alpha_001(pool, begin_date, end_date, plat_form_type)
