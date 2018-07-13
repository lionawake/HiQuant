#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#function doc: id, parameter num, return num
#==============================================================================

import talib

def lqAMA(data, n=10, fast_n=2, slow_n=30):
    '''00001,4,2'''
    return AMA(data, n=10, fast_n=2, slow_n=30)

def lqAMO(data):
	'''00002,1,1'''
	return AMO(data)

def lqCLOSE(data):
	'''00003,1,1'''
	return CLOSE(data)

def lqCVAL(data, value=0.0, len=0, discard=0):
	'''00004,4,1'''
	return CVAL(data,value,len,discard)

def lqDIFF(data):
	'''00005,1,1'''
	return DIFF(data)

def lqEMA(data, n=22):
	'''00006,2,1'''
	return EMA(data,n)

def lqHHV(data, n=20):
	'''00007,2,1'''
	return HHV(data,n)

def lqHIGH(data):
	'''00008,1,1'''
	return HIGH(data)

def lqKDATA(data):
	'''00009,1,1'''
	return KDATA(data)

def lqLLV(data, n=20):
	'''00010,2,1'''
	return LLV(data,n)

def lqLOW(data):
	'''00011,1,1'''
	return LOW(data)

def lqMA(data, n=22, type="SMA"):
	'''00012,3,1'''
	return MA(data,n,type)

def lqMACD(data, n1=12, n2=26, n3=9):
	'''00013,4,3'''
	return MACD(data,n1,n2,n3)

def lqOPEN(data):
	'''00014,1,1'''
	return OPEN(data)

def lqREF(data, n):
	'''00015,2,1'''
	return REF(data,n)

def lqSAFTYLOSS(data, n1=10, n2=3, p=2.0):
	'''00016,4,1'''
	return SAFTYLOSS(data,n1,n2,p)

def lqSMA(data, n=22):
	'''00017,2,1'''
	return SMA(data,n)

def lqSTDEV(data, n=10):
	'''00018,2,1'''
	return STDEV(data,n)

def lqVIGOR(data, n=2):
	'''00019,2,1'''
	return VIGOR(data,n)

def lqVOL(data):
	'''00020,1,1'''
	return VOL(data)

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


def fa_eps_basic(stock):
    """00156,1,1"""
    return findat.at[stock, 'fa_eps_basic']

def fa_eps_diluted(stock):
    """00157,1,1"""
    return findat.at[stock, 'fa_eps_diluted']

def fa_bps(stock):
    """00158,1,1"""
    return findat.at[stock, 'fa_bps']


def fa_grps(stock):
    """00159,1,1"""
    return findat.at[stock, 'fa_grps']


def fa_orps(stock):
    """00160,1,1"""
    return findat.at[stock, 'fa_orps']


def fa_opps(stock):
    """00161,1,1"""
    return findat.at[stock, 'fa_opps']


def fa_capsurpps(stock):
    """00162,1,1"""
    return findat.at[stock, 'fa_capsurpps']


def fa_spps(stock):
    """00163,1,1"""
    return findat.at[stock, 'fa_spps']


def fa_undistributedps(stock):
    """00164,1,1"""
    return findat.at[stock, 'fa_undistributedps']


def fa_retainedps(stock):
    """00165,1,1"""
    return findat.at[stock, 'fa_retainedps']


def fa_fcffps(stock):
    """00166,1,1"""
    return findat.at[stock, 'fa_fcffps']


def fa_fcfeps(stock):
    """00167,1,1"""
    return findat.at[stock, 'fa_fcfeps']


def fa_cceps(stock):
    """00168,1,1"""
    return findat.at[stock, 'fa_cceps']


def fa_divcover_ttm(stock):
    """00169,1,1"""
    return findat.at[stock, 'fa_divcover_ttm']


def fa_retainedearn_ttm(stock):
    """00170,1,1"""
    return findat.at[stock, 'fa_retainedearn_ttm']


def fa_cfps_ttm(stock):
    """00171,1,1"""
    return findat.at[stock, 'fa_cfps_ttm']


def fa_ocfps_ttm(stock):
    """00172,1,1"""
    return findat.at[stock, 'fa_ocfps_ttm']


def fa_opps_ttm(stock):
    """00173,1,1"""
    return findat.at[stock, 'fa_opps_ttm']


def fa_roe_avg(stock):
    """00174,1,1"""
    return findat.at[stock, 'fa_roe_avg']


def fa_roe_wgt(stock):
    """00175,1,1"""
    return findat.at[stock, 'fa_roe_wgt']


def fa_roe_diluted(stock):
    """00176,1,1"""
    return findat.at[stock, 'fa_roe_diluted']


def fa_roe_exbasic(stock):
    """00177,1,1"""
    return findat.at[stock, 'fa_roe_exbasic']


def fa_roe_exdiluted(stock):
    """00178,1,1"""
    return findat.at[stock, 'fa_roe_exdiluted']


def fa_roenp_ttm(stock):
    """00179,1,1"""
    return findat.at[stock, 'fa_roenp_ttm']


def fa_roaebit_ttm(stock):
    """00180,1,1"""
    return findat.at[stock, 'fa_roaebit_ttm']


def fa_netprofittoassets_ttm(stock):
    """00181,1,1"""
    return findat.at[stock, 'fa_netprofittoassets_ttm']


def fa_roic_ttm(stock):
    """00182,1,1"""
    return findat.at[stock, 'fa_roic_ttm']


def fa_roicebit_ttm(stock):
    """00183,1,1"""
    return findat.at[stock, 'fa_roicebit_ttm']


def fa_roc_ttm(stock):
    """00184,1,1"""
    return findat.at[stock, 'fa_roc_ttm']


def fa_roa_ttm(stock):
    """00185,1,1"""
    return findat.at[stock, 'fa_roa_ttm']


def fa_roaavg5y(stock):
    """00186,1,1"""
    return findat.at[stock, 'fa_roaavg5y']


def fa_roe_ttm(stock):
    """00187,1,1"""
    return findat.at[stock, 'fa_roe_ttm']


def fa_roeavg5y(stock):
    """00188,1,1"""
    return findat.at[stock, 'fa_roeavg5y']


def fa_protocost_ttm(stock):
    """00189,1,1"""
    return findat.at[stock, 'fa_protocost_ttm']


def fa_profittogr_ttm(stock):
    """00190,1,1"""
    return findat.at[stock, 'fa_profittogr_ttm']


def fa_optoor_ttm(stock):
    """00191,1,1"""
    return findat.at[stock, 'fa_optoor_ttm']


def fa_optogr_ttm(stock):
    """00192,1,1"""
    return findat.at[stock, 'fa_optogr_ttm']


def fa_ebittogr_ttm(stock):
    """00193,1,1"""
    return findat.at[stock, 'fa_ebittogr_ttm']


def fa_sellexpensetogr_ttm(stock):
    """00194,1,1"""
    return findat.at[stock, 'fa_sellexpensetogr_ttm']


def fa_adminexpensetogr_ttm(stock):
    """00195,1,1"""
    return findat.at[stock, 'fa_adminexpensetogr_ttm']


def fa_finaexpensetogr_ttm(stock):
    """00196,1,1"""
    return findat.at[stock, 'fa_finaexpensetogr_ttm']


def fa_impairtogr_ttm(stock):
    """00197,1,1"""
    return findat.at[stock, 'fa_impairtogr_ttm']


def fa_octogr_ttm(stock):
    """00198,1,1"""
    return findat.at[stock, 'fa_octogr_ttm']


def fa_netprofittoor_ttm(stock):
    """00199,1,1"""
    return findat.at[stock, 'fa_netprofittoor_ttm']


def fa_taxtoprofitbt_ttm(stock):
    """00200,1,1"""
    return findat.at[stock, 'fa_taxtoprofitbt_ttm']


def fa_netprofitmargin_ttm(stock):
    """00201,1,1"""
    return findat.at[stock, 'fa_netprofitmargin_ttm']


def fa_grossprofitmargin_ttm(stock):
    """00202,1,1"""
    return findat.at[stock, 'fa_grossprofitmargin_ttm']


def fa_expensetosales_ttm(stock):
    """00203,1,1"""
    return findat.at[stock, 'fa_expensetosales_ttm']


def fa_salestocost_ttm(stock):
    """00204,1,1"""
    return findat.at[stock, 'fa_salestocost_ttm']


def fa_taxratio_ttm(stock):
    """00205,1,1"""
    return findat.at[stock, 'fa_taxratio_ttm']


def fa_acca_ttm(stock):
    """00206,1,1"""
    return findat.at[stock, 'fa_acca_ttm']


def fa_berryratio_ttm(stock):
    """00207,1,1"""
    return findat.at[stock, 'fa_berryratio_ttm']


def fa_operincometopbt(stock):
    """00208,1,1"""
    return findat.at[stock, 'fa_operincometopbt']


def fa_operincometopbt_ttm(stock):
    """00209,1,1"""
    return findat.at[stock, 'fa_operincometopbt_ttm']


def fa_chgvaluetopbt_ttm(stock):
    """00210,1,1"""
    return findat.at[stock, 'fa_chgvaluetopbt_ttm']


def fa_nonoperprofittopbt_ttm(stock):
    """00211,1,1"""
    return findat.at[stock, 'fa_nonoperprofittopbt_ttm']


def fa_optopbt_ttm(stock):
    """00212,1,1"""
    return findat.at[stock, 'fa_optopbt_ttm']


def fa_pbttoor_ttm(stock):
    """00213,1,1"""
    return findat.at[stock, 'fa_pbttoor_ttm']


def fa_profittomv_ttm(stock):
    """00214,1,1"""
    return findat.at[stock, 'fa_profittomv_ttm']


def fa_pttomvavg5y(stock):
    """00215,1,1"""
    return findat.at[stock, 'fa_pttomvavg5y']


def fa_salescashtoor(stock):
    """00216,1,1"""
    return findat.at[stock, 'fa_salescashtoor']


def fa_salescashtoor_ttm(stock):
    """00217,1,1"""
    return findat.at[stock, 'fa_salescashtoor_ttm']


def fa_ocftoor(stock):
    """00218,1,1"""
    return findat.at[stock, 'fa_ocftoor']


def fa_ocftoor_ttm(stock):
    """00219,1,1"""
    return findat.at[stock, 'fa_ocftoor_ttm']


def fa_ocftooai_ttm(stock):
    """00220,1,1"""
    return findat.at[stock, 'fa_ocftooai_ttm']


def fa_ocftoop_ttm(stock):
    """00221,1,1"""
    return findat.at[stock, 'fa_ocftoop_ttm']


def fa_cashdivcover_ttm(stock):
    """00222,1,1"""
    return findat.at[stock, 'fa_cashdivcover_ttm']


def fa_cashrecovratio_ttm(stock):
    """00223,1,1"""
    return findat.at[stock, 'fa_cashrecovratio_ttm']


def fa_noncurassetsratio(stock):
    """00224,1,1"""
    return findat.at[stock, 'fa_noncurassetsratio']


def fa_curassetsratio(stock):
    """00225,1,1"""
    return findat.at[stock, 'fa_curassetsratio']


def fa_equitytointerestdebt(stock):
    """00226,1,1"""
    return findat.at[stock, 'fa_equitytointerestdebt']


def fa_equitytocapital(stock):
    """00227,1,1"""
    return findat.at[stock, 'fa_equitytocapital']


def fa_current(stock):
    """00228,1,1"""
    return findat.at[stock, 'fa_current']


def fa_quick(stock):
    """00229,1,1"""
    return findat.at[stock, 'fa_quick']


def fa_superquick(stock):
    """00230,1,1"""
    return findat.at[stock, 'fa_superquick']


def fa_tangibleatointerestdebt(stock):
    """00231,1,1"""
    return findat.at[stock, 'fa_tangibleatointerestdebt']


def fa_tangibleassettonetdebt(stock):
    """00232,1,1"""
    return findat.at[stock, 'fa_tangibleassettonetdebt']


def fa_debttotangibleafybl(stock):
    """00233,1,1"""
    return findat.at[stock, 'fa_debttotangibleafybl']


def fa_ocftodebt(stock):
    """00234,1,1"""
    return findat.at[stock, 'fa_ocftodebt']


def fa_ocftointerestdebt_ttm(stock):
    """00235,1,1"""
    return findat.at[stock, 'fa_ocftointerestdebt_ttm']


def fa_ocftonetdebt_ttm(stock):
    """00236,1,1"""
    return findat.at[stock, 'fa_ocftonetdebt_ttm']


def fa_interestdebttocapital(stock):
    """00237,1,1"""
    return findat.at[stock, 'fa_interestdebttocapital']


def fa_debttoequity(stock):
    """00238,1,1"""
    return findat.at[stock, 'fa_debttoequity']


def fa_ebittointerest(stock):
    """00239,1,1"""
    return findat.at[stock, 'fa_ebittointerest']


def fa_uncurdebttoworkcap(stock):
    """00240,1,1"""
    return findat.at[stock, 'fa_uncurdebttoworkcap']


def fa_blev(stock):
    """00241,1,1"""
    return findat.at[stock, 'fa_blev']


def fa_cfotocurliabs_ttm(stock):
    """00242,1,1"""
    return findat.at[stock, 'fa_cfotocurliabs_ttm']


def fa_cashtocurliabs(stock):
    """00243,1,1"""
    return findat.at[stock, 'fa_cashtocurliabs']


def fa_arturn_ttm(stock):
    """00244,1,1"""
    return findat.at[stock, 'fa_arturn_ttm']


def fa_apturn_ttm(stock):
    """00245,1,1"""
    return findat.at[stock, 'fa_apturn_ttm']


def fa_faturn_ttm(stock):
    """00246,1,1"""
    return findat.at[stock, 'fa_faturn_ttm']


def fa_taturn_ttm(stock):
    """00247,1,1"""
    return findat.at[stock, 'fa_taturn_ttm']


def fa_turndays_ttm(stock):
    """00248,1,1"""
    return findat.at[stock, 'fa_turndays_ttm']


def fa_invturndays_ttm(stock):
    """00249,1,1"""
    return findat.at[stock, 'fa_invturndays_ttm']


def fa_arturndays_ttm(stock):
    """00250,1,1"""
    return findat.at[stock, 'fa_arturndays_ttm']


def fa_apturndays_ttm(stock):
    """00251,1,1"""
    return findat.at[stock, 'fa_apturndays_ttm']


def fa_invturn_ttm(stock):
    """00252,1,1"""
    return findat.at[stock, 'fa_invturn_ttm']


def fa_cashcnvcycle_ttm(stock):
    """00253,1,1"""
    return findat.at[stock, 'fa_cashcnvcycle_ttm']


def fa_currtassetstrate_ttm(stock):
    """00254,1,1"""
    return findat.at[stock, 'fa_currtassetstrate_ttm']


def fa_naturn_ttm(stock):
    """00255,1,1"""
    return findat.at[stock, 'fa_naturn_ttm']


def fa_orgr_ttm(stock):
    """00256,1,1"""
    return findat.at[stock, 'fa_orgr_ttm']


def fa_ncgr_ttm(stock):
    """00257,1,1"""
    return findat.at[stock, 'fa_ncgr_ttm']


def fa_tpgr_ttm(stock):
    """00258,1,1"""
    return findat.at[stock, 'fa_tpgr_ttm']


def fa_oigr_ttm(stock):
    """00259,1,1"""
    return findat.at[stock, 'fa_oigr_ttm']


def fa_npgr_ttm(stock):
    """00260,1,1"""
    return findat.at[stock, 'fa_npgr_ttm']


def fa_nppcgr_ttm(stock):
    """00261,1,1"""
    return findat.at[stock, 'fa_nppcgr_ttm']


def fa_cfogr_ttm(stock):
    """00262,1,1"""
    return findat.at[stock, 'fa_cfogr_ttm']


def fa_cffgr_ttm(stock):
    """00263,1,1"""
    return findat.at[stock, 'fa_cffgr_ttm']


def fa_cfigr_ttm(stock):
    """00264,1,1"""
    return findat.at[stock, 'fa_cfigr_ttm']


def fa_gpmgr_ttm(stock):
    """00265,1,1"""
    return findat.at[stock, 'fa_gpmgr_ttm']


def fa_tagr(stock):
    """00266,1,1"""
    return findat.at[stock, 'fa_tagr']


def fa_nagr(stock):
    """00267,1,1"""
    return findat.at[stock, 'fa_nagr']


def fa_earnmom8qtr(stock):
    """00268,1,1"""
    return findat.at[stock, 'fa_earnmom8qtr']


def fa_fcff(stock):
    """00269,1,1"""
    return findat.at[stock, 'fa_fcff']


def fa_fcfe(stock):
    """00270,1,1"""
    return findat.at[stock, 'fa_fcfe']


def fa_nrgl(stock):
    """00271,1,1"""
    return findat.at[stock, 'fa_nrgl']


def fa_oaincome(stock):
    """00272,1,1"""
    return findat.at[stock, 'fa_oaincome']


def fa_workcapital(stock):
    """00273,1,1"""
    return findat.at[stock, 'fa_workcapital']


def fa_tangibleasset(stock):
    """00274,1,1"""
    return findat.at[stock, 'fa_tangibleasset']


def fa_retainearn(stock):
    """00275,1,1"""
    return findat.at[stock, 'fa_retainearn']


def fa_interestdebt(stock):
    """00276,1,1"""
    return findat.at[stock, 'fa_interestdebt']


def fa_netdebt(stock):
    """00277,1,1"""
    return findat.at[stock, 'fa_netdebt']


def fa_nicurdebt(stock):
    """00278,1,1"""
    return findat.at[stock, 'fa_nicurdebt']


def fa_ninocurdebt(stock):
    """00279,1,1"""
    return findat.at[stock, 'fa_ninocurdebt']


def fa_ebiat(stock):
    """00280,1,1"""
    return findat.at[stock, 'fa_ebiat']


def fa_da(stock):
    """00281,1,1"""
    return findat.at[stock, 'fa_da']


def fa_equity(stock):
    """00282,1,1"""
    return findat.at[stock, 'fa_equity']


def fa_investcapital(stock):
    """00283,1,1"""
    return findat.at[stock, 'fa_investcapital']


def fa_totassets(stock):
    """00284,1,1"""
    return findat.at[stock, 'fa_totassets']


def fa_fixassets(stock):
    """00285,1,1"""
    return findat.at[stock, 'fa_fixassets']


def fa_totliab(stock):
    """00286,1,1"""
    return findat.at[stock, 'fa_totliab']


def fa_totequity(stock):
    """00287,1,1"""
    return findat.at[stock, 'fa_totequity']


def fa_cce(stock):
    """00288,1,1"""
    return findat.at[stock, 'fa_cce']


def fa_gr_ttm(stock):
    """00289,1,1"""
    return findat.at[stock, 'fa_gr_ttm']


def fa_gc_ttm(stock):
    """00290,1,1"""
    return findat.at[stock, 'fa_gc_ttm']


def fa_or_ttm(stock):
    """00291,1,1"""
    return findat.at[stock, 'fa_or_ttm']


def fa_ocnf_ttm(stock):
    """00292,1,1"""
    return findat.at[stock, 'fa_ocnf_ttm']


def fa_oef_ttm(stock):
    """00293,1,1"""
    return findat.at[stock, 'fa_oef_ttm']


def fa_gp_ttm(stock):
    """00294,1,1"""
    return findat.at[stock, 'fa_gp_ttm']


def fa_sellexpense_ttm(stock):
    """00295,1,1"""
    return findat.at[stock, 'fa_sellexpense_ttm']


def fa_adminexpense_ttm(stock):
    """00296,1,1"""
    return findat.at[stock, 'fa_adminexpense_ttm']


def fa_finaexpense_ttm(stock):
    """00297,1,1"""
    return findat.at[stock, 'fa_finaexpense_ttm']


def fa_perexpense_ttm(stock):
    """00298,1,1"""
    return findat.at[stock, 'fa_perexpense_ttm']


def fa_interestexpense_ttm(stock):
    """00299,1,1"""
    return findat.at[stock, 'fa_interestexpense_ttm']


def fa_mininterest_ttm(stock):
    """00300,1,1"""
    return findat.at[stock, 'fa_mininterest_ttm']


def fa_impairloss_ttm(stock):
    """00301,1,1"""
    return findat.at[stock, 'fa_impairloss_ttm']


def fa_operactincome_ttm(stock):
    """00302,1,1"""
    return findat.at[stock, 'fa_operactincome_ttm']


def fa_chavalincome_ttm(stock):
    """00303,1,1"""
    return findat.at[stock, 'fa_chavalincome_ttm']


def fa_op_ttm(stock):
    """00304,1,1"""
    return findat.at[stock, 'fa_op_ttm']


def fa_nooperprofit_ttm(stock):
    """00305,1,1"""
    return findat.at[stock, 'fa_nooperprofit_ttm']


def fa_ebitunver_ttm(stock):
    """00306,1,1"""
    return findat.at[stock, 'fa_ebitunver_ttm']


def fa_tax_ttm(stock):
    """00307,1,1"""
    return findat.at[stock, 'fa_tax_ttm']


def fa_ebt_ttm(stock):
    """00308,1,1"""
    return findat.at[stock, 'fa_ebt_ttm']


def fa_profit_ttm(stock):
    """00309,1,1"""
    return findat.at[stock, 'fa_profit_ttm']


def fa_netprofit_ttm(stock):
    """00310,1,1"""
    return findat.at[stock, 'fa_netprofit_ttm']


def fa_deductprofit_ttm(stock):
    """00311,1,1"""
    return findat.at[stock, 'fa_deductprofit_ttm']


def fa_ebit_ttm(stock):
    """00312,1,1"""
    return findat.at[stock, 'fa_ebit_ttm']


def fa_ebitdainver_ttm(stock):
    """00313,1,1"""
    return findat.at[stock, 'fa_ebitdainver_ttm']


def fa_ebitda_ttm(stock):
    """00314,1,1"""
    return findat.at[stock, 'fa_ebitda_ttm']


def fa_salescash_ttm(stock):
    """00315,1,1"""
    return findat.at[stock, 'fa_salescash_ttm']


def fa_operactcashflow_ttm(stock):
    """00316,1,1"""
    return findat.at[stock, 'fa_operactcashflow_ttm']


def fa_inveactcashflow_ttm(stock):
    """00317,1,1"""
    return findat.at[stock, 'fa_inveactcashflow_ttm']


def fa_finaactcashflow_ttm(stock):
    """00318,1,1"""
    return findat.at[stock, 'fa_finaactcashflow_ttm']

def fa_cashflow_ttm(stock):
    """00319,1,1"""
    return findat.at[stock, 'fa_cashflow_ttm']

def fa_opertax_ttm(stock):
    """00320,1,1"""
    return findat.at[stock, 'fa_opertax_ttm']

def total_shares(stock):
    """00321,1,1"""
    return findat.at[stock, 'total_shares']

def free_float_shares(stock):
    """00322,1,1"""
    return findat.at[stock, 'free_float_shares']
