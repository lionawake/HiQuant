
////////////////// Hikyuu 实现的 ///////////////////////////////

/**
 * 佩里.J 考夫曼（Perry J.Kaufman）自适应移动平均，参见《精明交易者》（2006年 广东经济出版社）
 * @param n 计算均值的周期窗口，必须为大于2的整数，默认为10天
 * @param fast_n 对应快速周期N，默认为2
 * @param slow_n 对应慢速EMA线的N值，默认为30，不过当超过60左右该指标会收敛不会有太大的影响
 * @ingroup Indicator 具有2个结果集，result(0)为AMA，result(1)为ER
 */
Indicator HKU_API AMA(int n = 10, int fast_n = 2, int slow_n = 30);

/**
 * 平均真实波幅(Average True Range)
 * @param n 计算均值的周期窗口，必须为大于1的整数
 * @ingroup Indicator
 */
Indicator HKU_API ATR(int n = 14);

/**
 * 创建一个指定长度的常数指标
 * @param value 常量
 * @param len 长度
 * @param discard 抛弃数量，默认0
 * @ingroup Indicator
 */
Indicator HKU_API CVAL(double value=0.0, size_t len=0, size_t discard=0);

/**
 * 差分指标，即data[i] - data[i-1]
 * @ingroup Indicator
 */
Indicator HKU_API DIFF();

/**
 * 指数移动平均线(Exponential Moving Average)
 * @param n 计算均值的周期窗口，必须为大于0的整数
 * @ingroup Indicator
 */
Indicator HKU_API EMA(int n = 22);

/**
 * N日内最高价
 * @param n N日时间窗口
 */
Indicator HKU_API HHV(int n = 20);

/**
 * N日内最低价
 * @param n N日时间窗口
 */
Indicator HKU_API LLV(int n = 20);

OPEN()
HIGH()
LOW()
CLOSE()
AMO() //成交金额
VOL() //成交量

/**
 * 移动平均
 * @param data 待计算的数据
 * @param n 计算均值的周期窗口，必须为大于0的整数
 * @param type "EMA"|"SMA"|"AMA", 默认"SMA"
 * @ingroup Indicator
 */
Indicator HKU_API MA(const Indicator& data, int n = 22, const string& type = "SMA");

/**
 * MACD平滑异同移动平均线
 * @param n1 短期EMA时间窗，默认12
 * @param n2 长期EMA时间窗，默认26
 * @param n3 （短期EMA-长期EMA）EMA平滑时间窗，默认9
 * @return
 * <pre>
 * MACD BAR： MACD直柱，即MACD快线－MACD慢线
 * DIFF: 快线,即（短期EMA-长期EMA）
 * DEA: 慢线，即快线的n3周期EMA平滑
 * </pre>
 * @ingroup Indicator
 */
Indicator HKU_API MACD(int n1 = 12, int n2 = 26, int n3 = 9);

/**
 * REF 向前引用 （即右移）
 * 引用若干周期前的数据。
 * 用法：　REF(X，A)　引用A周期前的X值。
 * @param n 引用n周期前的值，即右移n位
 * @ingroup Indicator
 */
Indicator HKU_API REF(int n);

/**
 * 亚历山大 艾尔德安全地带止损
 * @details
 * <pre>
 * 参见《走进我的交易室》（2007年 地震出版社） 亚历山大.艾尔德(Alexander Elder) P202
 * 计算说明：在回溯周期内（一般为10到20天），将所有向下穿越的长度相加除以向下穿越的次数，
 *         得到噪音均值（即回溯期内所有最低价低于前一日最低价的长度除以次数），并用今日
 *         最低价减去（前日噪音均值乘以一个倍数）得到该止损线。为了抵消波动并且保证止损线的
 *         上移，在上述结果的基础上再取起N日（一般为3天）内的最高值
 * </pre>
 * @note：返回结果中前（回溯周期宽度＋去最高值的宽度）个点是无效的
 * @param n1 计算平均噪音的回溯时间窗口，默认为10天
 * @param n2 对初步止损线去n2日内的最高值，默认为3
 * @param p 噪音系数，默认为2
 * @ingroup Indicator
 */
Indicator HKU_API SAFTYLOSS(int n1 = 10, int n2 = 3, double p = 2.0);

/**
 * 简单移动平均
 * @param data 待计算的数据
 * @param n 计算均值的周期窗口，必须为大于0的整数
 * @ingroup Indicator
 */
Indicator HKU_API SMA(int n = 22);

/**
 * 计算N周期内样本标准差
 * @param n N日时间窗口
 * @ingroup Indicator
 */
Indicator HKU_API STDEV(int n = 10);

/**
 * 亚历山大 艾尔德力度指数
 * @details
 * <pre>
 * 参见《走进我的交易室》（2007年 地震出版社） (Alexander Elder) P131
 * 计算公式：（收盘价今－收盘价昨）＊成交量今
 * 一般可以再使用EMA或MA进行平滑
 * </pre>
 * @param n EMA平滑窗口，必须大于等于1
 * @ingroup Indicator
 */
Indicator HKU_API VIGOR(int n = 2);



///////////////////////////// TA-Lib 引入的 ////////////////////////////////////
/*
列表如下：
AD                  Chaikin A/D Line
ADOSC               Chaikin A/D Oscillator
ADX                 Average Directional Movement Index
ADXR                Average Directional Movement Index Rating
APO                 Absolute Price Oscillator
AROON               Aroon
AROONOSC            Aroon Oscillator
ATR                 Average True Range
AVGPRICE            Average Price
BBANDS              Bollinger Bands
BETA                Beta
BOP                 Balance Of Power
CCI                 Commodity Channel Index
CDL2CROWS           Two Crows
CDL3BLACKCROWS      Three Black Crows
CDL3INSIDE          Three Inside Up/Down
CDL3LINESTRIKE      Three-Line Strike 
CDL3OUTSIDE         Three Outside Up/Down
CDL3STARSINSOUTH    Three Stars In The South
CDL3WHITESOLDIERS   Three Advancing White Soldiers
CDLABANDONEDBABY    Abandoned Baby
CDLADVANCEBLOCK     Advance Block
CDLBELTHOLD         Belt-hold
CDLBREAKAWAY        Breakaway
CDLCLOSINGMARUBOZU  Closing Marubozu
CDLCONCEALBABYSWALL Concealing Baby Swallow
CDLCOUNTERATTACK    Counterattack
CDLDARKCLOUDCOVER   Dark Cloud Cover
CDLDOJI             Doji
CDLDOJISTAR         Doji Star
CDLDRAGONFLYDOJI    Dragonfly Doji
CDLENGULFING        Engulfing Pattern
CDLEVENINGDOJISTAR  Evening Doji Star
CDLEVENINGSTAR      Evening Star
CDLGAPSIDESIDEWHITE Up/Down-gap side-by-side white lines
CDLGRAVESTONEDOJI   Gravestone Doji
CDLHAMMER           Hammer
CDLHANGINGMAN       Hanging Man
CDLHARAMI           Harami Pattern
CDLHARAMICROSS      Harami Cross Pattern
CDLHIGHWAVE         High-Wave Candle
CDLHIKKAKE          Hikkake Pattern
CDLHIKKAKEMOD       Modified Hikkake Pattern
CDLHOMINGPIGEON     Homing Pigeon
CDLIDENTICAL3CROWS  Identical Three Crows
CDLINNECK           In-Neck Pattern
CDLINVERTEDHAMMER   Inverted Hammer
CDLKICKING          Kicking
CDLKICKINGBYLENGTH  Kicking - bull/bear determined by the longer marubozu
CDLLADDERBOTTOM     Ladder Bottom
CDLLONGLEGGEDDOJI   Long Legged Doji
CDLLONGLINE         Long Line Candle
CDLMARUBOZU         Marubozu
CDLMATCHINGLOW      Matching Low
CDLMATHOLD          Mat Hold
CDLMORNINGDOJISTAR  Morning Doji Star
CDLMORNINGSTAR      Morning Star
CDLONNECK           On-Neck Pattern
CDLPIERCING         Piercing Pattern
CDLRICKSHAWMAN      Rickshaw Man
CDLRISEFALL3METHODS Rising/Falling Three Methods
CDLSEPARATINGLINES  Separating Lines
CDLSHOOTINGSTAR     Shooting Star
CDLSHORTLINE        Short Line Candle
CDLSPINNINGTOP      Spinning Top
CDLSTALLEDPATTERN   Stalled Pattern
CDLSTICKSANDWICH    Stick Sandwich
CDLTAKURI           Takuri (Dragonfly Doji with very long lower shadow)
CDLTASUKIGAP        Tasuki Gap
CDLTHRUSTING        Thrusting Pattern
CDLTRISTAR          Tristar Pattern
CDLUNIQUE3RIVER     Unique 3 River
CDLUPSIDEGAP2CROWS  Upside Gap Two Crows
CDLXSIDEGAP3METHODS Upside/Downside Gap Three Methods
CMO                 Chande Momentum Oscillator
CORREL              Pearson's Correlation Coefficient (r)
DEMA                Double Exponential Moving Average
DX                  Directional Movement Index
EMA                 Exponential Moving Average
HT_DCPERIOD         Hilbert Transform - Dominant Cycle Period
HT_DCPHASE          Hilbert Transform - Dominant Cycle Phase
HT_PHASOR           Hilbert Transform - Phasor Components
HT_SINE             Hilbert Transform - SineWave
HT_TRENDLINE        Hilbert Transform - Instantaneous Trendline
HT_TRENDMODE        Hilbert Transform - Trend vs Cycle Mode
KAMA                Kaufman Adaptive Moving Average
LINEARREG           Linear Regression
LINEARREG_ANGLE     Linear Regression Angle
LINEARREG_INTERCEPT Linear Regression Intercept
LINEARREG_SLOPE     Linear Regression Slope
MA                  All Moving Average
MACD                Moving Average Convergence/Divergence
MACDEXT             MACD with controllable MA type
MACDFIX             Moving Average Convergence/Divergence Fix 12/26
MAMA                MESA Adaptive Moving Average
MAX                 Highest value over a specified period
MAXINDEX            Index of highest value over a specified period
MEDPRICE            Median Price
MFI                 Money Flow Index
MIDPOINT            MidPoint over period
MIDPRICE            Midpoint Price over period
MIN                 Lowest value over a specified period
MININDEX            Index of lowest value over a specified period
MINMAX              Lowest and highest values over a specified period
MINMAXINDEX         Indexes of lowest and highest values over a specified period
MINUS_DI            Minus Directional Indicator
MINUS_DM            Minus Directional Movement
MOM                 Momentum
NATR                Normalized Average True Range
OBV                 On Balance Volume
PLUS_DI             Plus Directional Indicator
PLUS_DM             Plus Directional Movement
PPO                 Percentage Price Oscillator
ROC                 Rate of change : ((price/prevPrice)-1)*100
ROCP                Rate of change Percentage: (price-prevPrice)/prevPrice
ROCR                Rate of change ratio: (price/prevPrice)
ROCR100             Rate of change ratio 100 scale: (price/prevPrice)*100
RSI                 Relative Strength Index
SAR                 Parabolic SAR
SAREXT              Parabolic SAR - Extended
SMA                 Simple Moving Average
STDDEV              Standard Deviation
STOCH               Stochastic
STOCHF              Stochastic Fast
STOCHRSI            Stochastic Relative Strength Index
SUM                 Summation
T3                  Triple Exponential Moving Average (T3)
TEMA                Triple Exponential Moving Average
TRANGE              True Range
TRIMA               Triangular Moving Average
TRIX                1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
TSF                 Time Series Forecast
TYPPRICE            Typical Price
ULTOSC              Ultimate Oscillator
VAR                 Variance
WCLPRICE            Weighted Close Price
WILLR               Williams' %R
WMA                 Weighted Moving Average

具体函数定义如下：
*/

/*
 * TA_ACOS - Vector Trigonometric ACos
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_ACOS( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_AD - Chaikin A/D Line
 * 
 * Input  = High, Low, Close, Volume
 * Output = double
 * 
 */
TA_RetCode TA_AD( int    startIdx,
                  int    endIdx,
                  const double inHigh[],
                  const double inLow[],
                  const double inClose[],
                  const double inVolume[],
                  int          *outBegIdx,
                  int          *outNBElement,
                  double        outReal[] );

/*
 * TA_ADD - Vector Arithmetic Add
 * 
 * Input  = double, double
 * Output = double
 * 
 */
TA_RetCode TA_ADD( int    startIdx,
                   int    endIdx,
                   const double inReal0[],
                   const double inReal1[],
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_ADOSC - Chaikin A/D Oscillator
 * 
 * Input  = High, Low, Close, Volume
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInFastPeriod:(From 2 to 100000)
 *    Number of period for the fast MA
 * 
 * optInSlowPeriod:(From 2 to 100000)
 *    Number of period for the slow MA
 * 
 * 
 */
TA_RetCode TA_ADOSC( int    startIdx,
                     int    endIdx,
                     const double inHigh[],
                     const double inLow[],
                     const double inClose[],
                     const double inVolume[],
                     int           optInFastPeriod, /* From 2 to 100000 */
                     int           optInSlowPeriod, /* From 2 to 100000 */
                     int          *outBegIdx,
                     int          *outNBElement,
                     double        outReal[] );

/*
 * TA_ADX - Average Directional Movement Index
 * 
 * Input  = High, Low, Close
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_ADX( int    startIdx,
                   int    endIdx,
                   const double inHigh[],
                   const double inLow[],
                   const double inClose[],
                   int           optInTimePeriod, /* From 2 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_ADXR - Average Directional Movement Index Rating
 * 
 * Input  = High, Low, Close
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_ADXR( int    startIdx,
                    int    endIdx,
                    const double inHigh[],
                    const double inLow[],
                    const double inClose[],
                    int           optInTimePeriod, /* From 2 to 100000 */
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_APO - Absolute Price Oscillator
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInFastPeriod:(From 2 to 100000)
 *    Number of period for the fast MA
 * 
 * optInSlowPeriod:(From 2 to 100000)
 *    Number of period for the slow MA
 * 
 * optInMAType:
 *    Type of Moving Average
 * 
 * 
 */
TA_RetCode TA_APO( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInFastPeriod, /* From 2 to 100000 */
                   int           optInSlowPeriod, /* From 2 to 100000 */
                   TA_MAType     optInMAType,
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_AROON - Aroon
 * 
 * Input  = High, Low
 * Output = double, double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_AROON( int    startIdx,
                     int    endIdx,
                     const double inHigh[],
                     const double inLow[],
                     int           optInTimePeriod, /* From 2 to 100000 */
                     int          *outBegIdx,
                     int          *outNBElement,
                     double        outAroonDown[],
                     double        outAroonUp[] );

/*
 * TA_AROONOSC - Aroon Oscillator
 * 
 * Input  = High, Low
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_AROONOSC( int    startIdx,
                        int    endIdx,
                        const double inHigh[],
                        const double inLow[],
                        int           optInTimePeriod, /* From 2 to 100000 */
                        int          *outBegIdx,
                        int          *outNBElement,
                        double        outReal[] );

/*
 * TA_ASIN - Vector Trigonometric ASin
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_ASIN( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_ATAN - Vector Trigonometric ATan
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_ATAN( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_ATR - Average True Range
 * 
 * Input  = High, Low, Close
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_ATR( int    startIdx,
                   int    endIdx,
                   const double inHigh[],
                   const double inLow[],
                   const double inClose[],
                   int           optInTimePeriod, /* From 1 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_AVGPRICE - Average Price
 * 
 * Input  = Open, High, Low, Close
 * Output = double
 * 
 */
TA_RetCode TA_AVGPRICE( int    startIdx,
                        int    endIdx,
                        const double inOpen[],
                        const double inHigh[],
                        const double inLow[],
                        const double inClose[],
                        int          *outBegIdx,
                        int          *outNBElement,
                        double        outReal[] );

/*
 * TA_BBANDS - Bollinger Bands
 * 
 * Input  = double
 * Output = double, double, double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * optInNbDevUp:(From TA_REAL_MIN to TA_REAL_MAX)
 *    Deviation multiplier for upper band
 * 
 * optInNbDevDn:(From TA_REAL_MIN to TA_REAL_MAX)
 *    Deviation multiplier for lower band
 * 
 * optInMAType:
 *    Type of Moving Average
 * 
 * 
 */
TA_RetCode TA_BBANDS( int    startIdx,
                      int    endIdx,
                      const double inReal[],
                      int           optInTimePeriod, /* From 2 to 100000 */
                      double        optInNbDevUp, /* From TA_REAL_MIN to TA_REAL_MAX */
                      double        optInNbDevDn, /* From TA_REAL_MIN to TA_REAL_MAX */
                      TA_MAType     optInMAType,
                      int          *outBegIdx,
                      int          *outNBElement,
                      double        outRealUpperBand[],
                      double        outRealMiddleBand[],
                      double        outRealLowerBand[] );

/*
 * TA_BETA - Beta
 * 
 * Input  = double, double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_BETA( int    startIdx,
                    int    endIdx,
                    const double inReal0[],
                    const double inReal1[],
                    int           optInTimePeriod, /* From 1 to 100000 */
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_BOP - Balance Of Power
 * 
 * Input  = Open, High, Low, Close
 * Output = double
 * 
 */
TA_RetCode TA_BOP( int    startIdx,
                   int    endIdx,
                   const double inOpen[],
                   const double inHigh[],
                   const double inLow[],
                   const double inClose[],
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_CCI - Commodity Channel Index
 * 
 * Input  = High, Low, Close
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_CCI( int    startIdx,
                   int    endIdx,
                   const double inHigh[],
                   const double inLow[],
                   const double inClose[],
                   int           optInTimePeriod, /* From 2 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_CDL2CROWS - Two Crows
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDL2CROWS( int    startIdx,
                         int    endIdx,
                         const double inOpen[],
                         const double inHigh[],
                         const double inLow[],
                         const double inClose[],
                         int          *outBegIdx,
                         int          *outNBElement,
                         int           outInteger[] );

/*
 * TA_CDL3BLACKCROWS - Three Black Crows
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDL3BLACKCROWS( int    startIdx,
                              int    endIdx,
                              const double inOpen[],
                              const double inHigh[],
                              const double inLow[],
                              const double inClose[],
                              int          *outBegIdx,
                              int          *outNBElement,
                              int           outInteger[] );

/*
 * TA_CDL3INSIDE - Three Inside Up/Down
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDL3INSIDE( int    startIdx,
                          int    endIdx,
                          const double inOpen[],
                          const double inHigh[],
                          const double inLow[],
                          const double inClose[],
                          int          *outBegIdx,
                          int          *outNBElement,
                          int           outInteger[] );

/*
 * TA_CDL3LINESTRIKE - Three-Line Strike 
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDL3LINESTRIKE( int    startIdx,
                              int    endIdx,
                              const double inOpen[],
                              const double inHigh[],
                              const double inLow[],
                              const double inClose[],
                              int          *outBegIdx,
                              int          *outNBElement,
                              int           outInteger[] );

/*
 * TA_CDL3OUTSIDE - Three Outside Up/Down
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDL3OUTSIDE( int    startIdx,
                           int    endIdx,
                           const double inOpen[],
                           const double inHigh[],
                           const double inLow[],
                           const double inClose[],
                           int          *outBegIdx,
                           int          *outNBElement,
                           int           outInteger[] );

/*
 * TA_CDL3STARSINSOUTH - Three Stars In The South
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDL3STARSINSOUTH( int    startIdx,
                                int    endIdx,
                                const double inOpen[],
                                const double inHigh[],
                                const double inLow[],
                                const double inClose[],
                                int          *outBegIdx,
                                int          *outNBElement,
                                int           outInteger[] );

/*
 * TA_CDL3WHITESOLDIERS - Three Advancing White Soldiers
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDL3WHITESOLDIERS( int    startIdx,
                                 int    endIdx,
                                 const double inOpen[],
                                 const double inHigh[],
                                 const double inLow[],
                                 const double inClose[],
                                 int          *outBegIdx,
                                 int          *outNBElement,
                                 int           outInteger[] );

/*
 * TA_CDLABANDONEDBABY - Abandoned Baby
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 * Optional Parameters
 * -------------------
 * optInPenetration:(From 0 to TA_REAL_MAX)
 *    Percentage of penetration of a candle within another candle
 * 
 * 
 */
TA_RetCode TA_CDLABANDONEDBABY( int    startIdx,
                                int    endIdx,
                                const double inOpen[],
                                const double inHigh[],
                                const double inLow[],
                                const double inClose[],
                                double        optInPenetration, /* From 0 to TA_REAL_MAX */
                                int          *outBegIdx,
                                int          *outNBElement,
                                int           outInteger[] );

/*
 * TA_CDLADVANCEBLOCK - Advance Block
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLADVANCEBLOCK( int    startIdx,
                               int    endIdx,
                               const double inOpen[],
                               const double inHigh[],
                               const double inLow[],
                               const double inClose[],
                               int          *outBegIdx,
                               int          *outNBElement,
                               int           outInteger[] );

/*
 * TA_CDLBELTHOLD - Belt-hold
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLBELTHOLD( int    startIdx,
                           int    endIdx,
                           const double inOpen[],
                           const double inHigh[],
                           const double inLow[],
                           const double inClose[],
                           int          *outBegIdx,
                           int          *outNBElement,
                           int           outInteger[] );

/*
 * TA_CDLBREAKAWAY - Breakaway
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLBREAKAWAY( int    startIdx,
                            int    endIdx,
                            const double inOpen[],
                            const double inHigh[],
                            const double inLow[],
                            const double inClose[],
                            int          *outBegIdx,
                            int          *outNBElement,
                            int           outInteger[] );

/*
 * TA_CDLCLOSINGMARUBOZU - Closing Marubozu
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLCLOSINGMARUBOZU( int    startIdx,
                                  int    endIdx,
                                  const double inOpen[],
                                  const double inHigh[],
                                  const double inLow[],
                                  const double inClose[],
                                  int          *outBegIdx,
                                  int          *outNBElement,
                                  int           outInteger[] );

/*
 * TA_CDLCONCEALBABYSWALL - Concealing Baby Swallow
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLCONCEALBABYSWALL( int    startIdx,
                                   int    endIdx,
                                   const double inOpen[],
                                   const double inHigh[],
                                   const double inLow[],
                                   const double inClose[],
                                   int          *outBegIdx,
                                   int          *outNBElement,
                                   int           outInteger[] );

/*
 * TA_CDLCOUNTERATTACK - Counterattack
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLCOUNTERATTACK( int    startIdx,
                                int    endIdx,
                                const double inOpen[],
                                const double inHigh[],
                                const double inLow[],
                                const double inClose[],
                                int          *outBegIdx,
                                int          *outNBElement,
                                int           outInteger[] );

/*
 * TA_CDLDARKCLOUDCOVER - Dark Cloud Cover
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 * Optional Parameters
 * -------------------
 * optInPenetration:(From 0 to TA_REAL_MAX)
 *    Percentage of penetration of a candle within another candle
 * 
 * 
 */
TA_RetCode TA_CDLDARKCLOUDCOVER( int    startIdx,
                                 int    endIdx,
                                 const double inOpen[],
                                 const double inHigh[],
                                 const double inLow[],
                                 const double inClose[],
                                 double        optInPenetration, /* From 0 to TA_REAL_MAX */
                                 int          *outBegIdx,
                                 int          *outNBElement,
                                 int           outInteger[] );

/*
 * TA_CDLDOJI - Doji
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLDOJI( int    startIdx,
                       int    endIdx,
                       const double inOpen[],
                       const double inHigh[],
                       const double inLow[],
                       const double inClose[],
                       int          *outBegIdx,
                       int          *outNBElement,
                       int           outInteger[] );

/*
 * TA_CDLDOJISTAR - Doji Star
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLDOJISTAR( int    startIdx,
                           int    endIdx,
                           const double inOpen[],
                           const double inHigh[],
                           const double inLow[],
                           const double inClose[],
                           int          *outBegIdx,
                           int          *outNBElement,
                           int           outInteger[] );

/*
 * TA_CDLDRAGONFLYDOJI - Dragonfly Doji
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLDRAGONFLYDOJI( int    startIdx,
                                int    endIdx,
                                const double inOpen[],
                                const double inHigh[],
                                const double inLow[],
                                const double inClose[],
                                int          *outBegIdx,
                                int          *outNBElement,
                                int           outInteger[] );

/*
 * TA_CDLENGULFING - Engulfing Pattern
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLENGULFING( int    startIdx,
                            int    endIdx,
                            const double inOpen[],
                            const double inHigh[],
                            const double inLow[],
                            const double inClose[],
                            int          *outBegIdx,
                            int          *outNBElement,
                            int           outInteger[] );

/*
 * TA_CDLEVENINGDOJISTAR - Evening Doji Star
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 * Optional Parameters
 * -------------------
 * optInPenetration:(From 0 to TA_REAL_MAX)
 *    Percentage of penetration of a candle within another candle
 * 
 * 
 */
TA_RetCode TA_CDLEVENINGDOJISTAR( int    startIdx,
                                  int    endIdx,
                                  const double inOpen[],
                                  const double inHigh[],
                                  const double inLow[],
                                  const double inClose[],
                                  double        optInPenetration, /* From 0 to TA_REAL_MAX */
                                  int          *outBegIdx,
                                  int          *outNBElement,
                                  int           outInteger[] );

/*
 * TA_CDLEVENINGSTAR - Evening Star
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 * Optional Parameters
 * -------------------
 * optInPenetration:(From 0 to TA_REAL_MAX)
 *    Percentage of penetration of a candle within another candle
 * 
 * 
 */
TA_RetCode TA_CDLEVENINGSTAR( int    startIdx,
                              int    endIdx,
                              const double inOpen[],
                              const double inHigh[],
                              const double inLow[],
                              const double inClose[],
                              double        optInPenetration, /* From 0 to TA_REAL_MAX */
                              int          *outBegIdx,
                              int          *outNBElement,
                              int           outInteger[] );

/*
 * TA_CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLGAPSIDESIDEWHITE( int    startIdx,
                                   int    endIdx,
                                   const double inOpen[],
                                   const double inHigh[],
                                   const double inLow[],
                                   const double inClose[],
                                   int          *outBegIdx,
                                   int          *outNBElement,
                                   int           outInteger[] );

/*
 * TA_CDLGRAVESTONEDOJI - Gravestone Doji
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLGRAVESTONEDOJI( int    startIdx,
                                 int    endIdx,
                                 const double inOpen[],
                                 const double inHigh[],
                                 const double inLow[],
                                 const double inClose[],
                                 int          *outBegIdx,
                                 int          *outNBElement,
                                 int           outInteger[] );

/*
 * TA_CDLHAMMER - Hammer
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLHAMMER( int    startIdx,
                         int    endIdx,
                         const double inOpen[],
                         const double inHigh[],
                         const double inLow[],
                         const double inClose[],
                         int          *outBegIdx,
                         int          *outNBElement,
                         int           outInteger[] );

/*
 * TA_CDLHANGINGMAN - Hanging Man
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLHANGINGMAN( int    startIdx,
                             int    endIdx,
                             const double inOpen[],
                             const double inHigh[],
                             const double inLow[],
                             const double inClose[],
                             int          *outBegIdx,
                             int          *outNBElement,
                             int           outInteger[] );

/*
 * TA_CDLHARAMI - Harami Pattern
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLHARAMI( int    startIdx,
                         int    endIdx,
                         const double inOpen[],
                         const double inHigh[],
                         const double inLow[],
                         const double inClose[],
                         int          *outBegIdx,
                         int          *outNBElement,
                         int           outInteger[] );

/*
 * TA_CDLHARAMICROSS - Harami Cross Pattern
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLHARAMICROSS( int    startIdx,
                              int    endIdx,
                              const double inOpen[],
                              const double inHigh[],
                              const double inLow[],
                              const double inClose[],
                              int          *outBegIdx,
                              int          *outNBElement,
                              int           outInteger[] );

/*
 * TA_CDLHIGHWAVE - High-Wave Candle
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLHIGHWAVE( int    startIdx,
                           int    endIdx,
                           const double inOpen[],
                           const double inHigh[],
                           const double inLow[],
                           const double inClose[],
                           int          *outBegIdx,
                           int          *outNBElement,
                           int           outInteger[] );

/*
 * TA_CDLHIKKAKE - Hikkake Pattern
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLHIKKAKE( int    startIdx,
                          int    endIdx,
                          const double inOpen[],
                          const double inHigh[],
                          const double inLow[],
                          const double inClose[],
                          int          *outBegIdx,
                          int          *outNBElement,
                          int           outInteger[] );

/*
 * TA_CDLHIKKAKEMOD - Modified Hikkake Pattern
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLHIKKAKEMOD( int    startIdx,
                             int    endIdx,
                             const double inOpen[],
                             const double inHigh[],
                             const double inLow[],
                             const double inClose[],
                             int          *outBegIdx,
                             int          *outNBElement,
                             int           outInteger[] );

/*
 * TA_CDLHOMINGPIGEON - Homing Pigeon
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLHOMINGPIGEON( int    startIdx,
                               int    endIdx,
                               const double inOpen[],
                               const double inHigh[],
                               const double inLow[],
                               const double inClose[],
                               int          *outBegIdx,
                               int          *outNBElement,
                               int           outInteger[] );

/*
 * TA_CDLIDENTICAL3CROWS - Identical Three Crows
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLIDENTICAL3CROWS( int    startIdx,
                                  int    endIdx,
                                  const double inOpen[],
                                  const double inHigh[],
                                  const double inLow[],
                                  const double inClose[],
                                  int          *outBegIdx,
                                  int          *outNBElement,
                                  int           outInteger[] );

/*
 * TA_CDLINNECK - In-Neck Pattern
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLINNECK( int    startIdx,
                         int    endIdx,
                         const double inOpen[],
                         const double inHigh[],
                         const double inLow[],
                         const double inClose[],
                         int          *outBegIdx,
                         int          *outNBElement,
                         int           outInteger[] );

/*
 * TA_CDLINVERTEDHAMMER - Inverted Hammer
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLINVERTEDHAMMER( int    startIdx,
                                 int    endIdx,
                                 const double inOpen[],
                                 const double inHigh[],
                                 const double inLow[],
                                 const double inClose[],
                                 int          *outBegIdx,
                                 int          *outNBElement,
                                 int           outInteger[] );

/*
 * TA_CDLKICKING - Kicking
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLKICKING( int    startIdx,
                          int    endIdx,
                          const double inOpen[],
                          const double inHigh[],
                          const double inLow[],
                          const double inClose[],
                          int          *outBegIdx,
                          int          *outNBElement,
                          int           outInteger[] );

/*
 * TA_CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLKICKINGBYLENGTH( int    startIdx,
                                  int    endIdx,
                                  const double inOpen[],
                                  const double inHigh[],
                                  const double inLow[],
                                  const double inClose[],
                                  int          *outBegIdx,
                                  int          *outNBElement,
                                  int           outInteger[] );

/*
 * TA_CDLLADDERBOTTOM - Ladder Bottom
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLLADDERBOTTOM( int    startIdx,
                               int    endIdx,
                               const double inOpen[],
                               const double inHigh[],
                               const double inLow[],
                               const double inClose[],
                               int          *outBegIdx,
                               int          *outNBElement,
                               int           outInteger[] );

/*
 * TA_CDLLONGLEGGEDDOJI - Long Legged Doji
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLLONGLEGGEDDOJI( int    startIdx,
                                 int    endIdx,
                                 const double inOpen[],
                                 const double inHigh[],
                                 const double inLow[],
                                 const double inClose[],
                                 int          *outBegIdx,
                                 int          *outNBElement,
                                 int           outInteger[] );

/*
 * TA_CDLLONGLINE - Long Line Candle
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLLONGLINE( int    startIdx,
                           int    endIdx,
                           const double inOpen[],
                           const double inHigh[],
                           const double inLow[],
                           const double inClose[],
                           int          *outBegIdx,
                           int          *outNBElement,
                           int           outInteger[] );

/*
 * TA_CDLMARUBOZU - Marubozu
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLMARUBOZU( int    startIdx,
                           int    endIdx,
                           const double inOpen[],
                           const double inHigh[],
                           const double inLow[],
                           const double inClose[],
                           int          *outBegIdx,
                           int          *outNBElement,
                           int           outInteger[] );

/*
 * TA_CDLMATCHINGLOW - Matching Low
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLMATCHINGLOW( int    startIdx,
                              int    endIdx,
                              const double inOpen[],
                              const double inHigh[],
                              const double inLow[],
                              const double inClose[],
                              int          *outBegIdx,
                              int          *outNBElement,
                              int           outInteger[] );

/*
 * TA_CDLMATHOLD - Mat Hold
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 * Optional Parameters
 * -------------------
 * optInPenetration:(From 0 to TA_REAL_MAX)
 *    Percentage of penetration of a candle within another candle
 * 
 * 
 */
TA_RetCode TA_CDLMATHOLD( int    startIdx,
                          int    endIdx,
                          const double inOpen[],
                          const double inHigh[],
                          const double inLow[],
                          const double inClose[],
                          double        optInPenetration, /* From 0 to TA_REAL_MAX */
                          int          *outBegIdx,
                          int          *outNBElement,
                          int           outInteger[] );

/*
 * TA_CDLMORNINGDOJISTAR - Morning Doji Star
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 * Optional Parameters
 * -------------------
 * optInPenetration:(From 0 to TA_REAL_MAX)
 *    Percentage of penetration of a candle within another candle
 * 
 * 
 */
TA_RetCode TA_CDLMORNINGDOJISTAR( int    startIdx,
                                  int    endIdx,
                                  const double inOpen[],
                                  const double inHigh[],
                                  const double inLow[],
                                  const double inClose[],
                                  double        optInPenetration, /* From 0 to TA_REAL_MAX */
                                  int          *outBegIdx,
                                  int          *outNBElement,
                                  int           outInteger[] );

/*
 * TA_CDLMORNINGSTAR - Morning Star
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 * Optional Parameters
 * -------------------
 * optInPenetration:(From 0 to TA_REAL_MAX)
 *    Percentage of penetration of a candle within another candle
 * 
 * 
 */
TA_RetCode TA_CDLMORNINGSTAR( int    startIdx,
                              int    endIdx,
                              const double inOpen[],
                              const double inHigh[],
                              const double inLow[],
                              const double inClose[],
                              double        optInPenetration, /* From 0 to TA_REAL_MAX */
                              int          *outBegIdx,
                              int          *outNBElement,
                              int           outInteger[] );

/*
 * TA_CDLONNECK - On-Neck Pattern
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLONNECK( int    startIdx,
                         int    endIdx,
                         const double inOpen[],
                         const double inHigh[],
                         const double inLow[],
                         const double inClose[],
                         int          *outBegIdx,
                         int          *outNBElement,
                         int           outInteger[] );

/*
 * TA_CDLPIERCING - Piercing Pattern
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLPIERCING( int    startIdx,
                           int    endIdx,
                           const double inOpen[],
                           const double inHigh[],
                           const double inLow[],
                           const double inClose[],
                           int          *outBegIdx,
                           int          *outNBElement,
                           int           outInteger[] );

/*
 * TA_CDLRICKSHAWMAN - Rickshaw Man
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLRICKSHAWMAN( int    startIdx,
                              int    endIdx,
                              const double inOpen[],
                              const double inHigh[],
                              const double inLow[],
                              const double inClose[],
                              int          *outBegIdx,
                              int          *outNBElement,
                              int           outInteger[] );

/*
 * TA_CDLRISEFALL3METHODS - Rising/Falling Three Methods
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLRISEFALL3METHODS( int    startIdx,
                                   int    endIdx,
                                   const double inOpen[],
                                   const double inHigh[],
                                   const double inLow[],
                                   const double inClose[],
                                   int          *outBegIdx,
                                   int          *outNBElement,
                                   int           outInteger[] );

/*
 * TA_CDLSEPARATINGLINES - Separating Lines
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLSEPARATINGLINES( int    startIdx,
                                  int    endIdx,
                                  const double inOpen[],
                                  const double inHigh[],
                                  const double inLow[],
                                  const double inClose[],
                                  int          *outBegIdx,
                                  int          *outNBElement,
                                  int           outInteger[] );

/*
 * TA_CDLSHOOTINGSTAR - Shooting Star
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLSHOOTINGSTAR( int    startIdx,
                               int    endIdx,
                               const double inOpen[],
                               const double inHigh[],
                               const double inLow[],
                               const double inClose[],
                               int          *outBegIdx,
                               int          *outNBElement,
                               int           outInteger[] );

/*
 * TA_CDLSHORTLINE - Short Line Candle
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLSHORTLINE( int    startIdx,
                            int    endIdx,
                            const double inOpen[],
                            const double inHigh[],
                            const double inLow[],
                            const double inClose[],
                            int          *outBegIdx,
                            int          *outNBElement,
                            int           outInteger[] );

/*
 * TA_CDLSPINNINGTOP - Spinning Top
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLSPINNINGTOP( int    startIdx,
                              int    endIdx,
                              const double inOpen[],
                              const double inHigh[],
                              const double inLow[],
                              const double inClose[],
                              int          *outBegIdx,
                              int          *outNBElement,
                              int           outInteger[] );

/*
 * TA_CDLSTALLEDPATTERN - Stalled Pattern
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLSTALLEDPATTERN( int    startIdx,
                                 int    endIdx,
                                 const double inOpen[],
                                 const double inHigh[],
                                 const double inLow[],
                                 const double inClose[],
                                 int          *outBegIdx,
                                 int          *outNBElement,
                                 int           outInteger[] );

/*
 * TA_CDLSTICKSANDWICH - Stick Sandwich
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLSTICKSANDWICH( int    startIdx,
                                int    endIdx,
                                const double inOpen[],
                                const double inHigh[],
                                const double inLow[],
                                const double inClose[],
                                int          *outBegIdx,
                                int          *outNBElement,
                                int           outInteger[] );

/*
 * TA_CDLTAKURI - Takuri (Dragonfly Doji with very long lower shadow)
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLTAKURI( int    startIdx,
                         int    endIdx,
                         const double inOpen[],
                         const double inHigh[],
                         const double inLow[],
                         const double inClose[],
                         int          *outBegIdx,
                         int          *outNBElement,
                         int           outInteger[] );

/*
 * TA_CDLTASUKIGAP - Tasuki Gap
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLTASUKIGAP( int    startIdx,
                            int    endIdx,
                            const double inOpen[],
                            const double inHigh[],
                            const double inLow[],
                            const double inClose[],
                            int          *outBegIdx,
                            int          *outNBElement,
                            int           outInteger[] );

/*
 * TA_CDLTHRUSTING - Thrusting Pattern
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLTHRUSTING( int    startIdx,
                            int    endIdx,
                            const double inOpen[],
                            const double inHigh[],
                            const double inLow[],
                            const double inClose[],
                            int          *outBegIdx,
                            int          *outNBElement,
                            int           outInteger[] );

/*
 * TA_CDLTRISTAR - Tristar Pattern
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLTRISTAR( int    startIdx,
                          int    endIdx,
                          const double inOpen[],
                          const double inHigh[],
                          const double inLow[],
                          const double inClose[],
                          int          *outBegIdx,
                          int          *outNBElement,
                          int           outInteger[] );

/*
 * TA_CDLUNIQUE3RIVER - Unique 3 River
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLUNIQUE3RIVER( int    startIdx,
                               int    endIdx,
                               const double inOpen[],
                               const double inHigh[],
                               const double inLow[],
                               const double inClose[],
                               int          *outBegIdx,
                               int          *outNBElement,
                               int           outInteger[] );

/*
 * TA_CDLUPSIDEGAP2CROWS - Upside Gap Two Crows
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLUPSIDEGAP2CROWS( int    startIdx,
                                  int    endIdx,
                                  const double inOpen[],
                                  const double inHigh[],
                                  const double inLow[],
                                  const double inClose[],
                                  int          *outBegIdx,
                                  int          *outNBElement,
                                  int           outInteger[] );

/*
 * TA_CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods
 * 
 * Input  = Open, High, Low, Close
 * Output = int
 * 
 */
TA_RetCode TA_CDLXSIDEGAP3METHODS( int    startIdx,
                                   int    endIdx,
                                   const double inOpen[],
                                   const double inHigh[],
                                   const double inLow[],
                                   const double inClose[],
                                   int          *outBegIdx,
                                   int          *outNBElement,
                                   int           outInteger[] );

/*
 * TA_CEIL - Vector Ceil
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_CEIL( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_CMO - Chande Momentum Oscillator
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_CMO( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInTimePeriod, /* From 2 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_CORREL - Pearson's Correlation Coefficient (r)
 * 
 * Input  = double, double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_CORREL( int    startIdx,
                      int    endIdx,
                      const double inReal0[],
                      const double inReal1[],
                      int           optInTimePeriod, /* From 1 to 100000 */
                      int          *outBegIdx,
                      int          *outNBElement,
                      double        outReal[] );

/*
 * TA_COS - Vector Trigonometric Cos
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_COS( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_COSH - Vector Trigonometric Cosh
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_COSH( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_DEMA - Double Exponential Moving Average
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_DEMA( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int           optInTimePeriod, /* From 2 to 100000 */
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_DIV - Vector Arithmetic Div
 * 
 * Input  = double, double
 * Output = double
 * 
 */
TA_RetCode TA_DIV( int    startIdx,
                   int    endIdx,
                   const double inReal0[],
                   const double inReal1[],
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_DX - Directional Movement Index
 * 
 * Input  = High, Low, Close
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_DX( int    startIdx,
                  int    endIdx,
                  const double inHigh[],
                  const double inLow[],
                  const double inClose[],
                  int           optInTimePeriod, /* From 2 to 100000 */
                  int          *outBegIdx,
                  int          *outNBElement,
                  double        outReal[] );

/*
 * TA_EMA - Exponential Moving Average
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_EMA( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInTimePeriod, /* From 2 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_EXP - Vector Arithmetic Exp
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_EXP( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_FLOOR - Vector Floor
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_FLOOR( int    startIdx,
                     int    endIdx,
                     const double inReal[],
                     int          *outBegIdx,
                     int          *outNBElement,
                     double        outReal[] );

/*
 * TA_HT_DCPERIOD - Hilbert Transform - Dominant Cycle Period
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_HT_DCPERIOD( int    startIdx,
                           int    endIdx,
                           const double inReal[],
                           int          *outBegIdx,
                           int          *outNBElement,
                           double        outReal[] );

/*
 * TA_HT_DCPHASE - Hilbert Transform - Dominant Cycle Phase
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_HT_DCPHASE( int    startIdx,
                          int    endIdx,
                          const double inReal[],
                          int          *outBegIdx,
                          int          *outNBElement,
                          double        outReal[] );

/*
 * TA_HT_PHASOR - Hilbert Transform - Phasor Components
 * 
 * Input  = double
 * Output = double, double
 * 
 */
TA_RetCode TA_HT_PHASOR( int    startIdx,
                         int    endIdx,
                         const double inReal[],
                         int          *outBegIdx,
                         int          *outNBElement,
                         double        outInPhase[],
                         double        outQuadrature[] );

/*
 * TA_HT_SINE - Hilbert Transform - SineWave
 * 
 * Input  = double
 * Output = double, double
 * 
 */
TA_RetCode TA_HT_SINE( int    startIdx,
                       int    endIdx,
                       const double inReal[],
                       int          *outBegIdx,
                       int          *outNBElement,
                       double        outSine[],
                       double        outLeadSine[] );

/*
 * TA_HT_TRENDLINE - Hilbert Transform - Instantaneous Trendline
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_HT_TRENDLINE( int    startIdx,
                            int    endIdx,
                            const double inReal[],
                            int          *outBegIdx,
                            int          *outNBElement,
                            double        outReal[] );

/*
 * TA_HT_TRENDMODE - Hilbert Transform - Trend vs Cycle Mode
 * 
 * Input  = double
 * Output = int
 * 
 */
TA_RetCode TA_HT_TRENDMODE( int    startIdx,
                            int    endIdx,
                            const double inReal[],
                            int          *outBegIdx,
                            int          *outNBElement,
                            int           outInteger[] );

/*
 * TA_KAMA - Kaufman Adaptive Moving Average
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_KAMA( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int           optInTimePeriod, /* From 2 to 100000 */
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_LINEARREG - Linear Regression
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_LINEARREG( int    startIdx,
                         int    endIdx,
                         const double inReal[],
                         int           optInTimePeriod, /* From 2 to 100000 */
                         int          *outBegIdx,
                         int          *outNBElement,
                         double        outReal[] );

/*
 * TA_LINEARREG_ANGLE - Linear Regression Angle
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_LINEARREG_ANGLE( int    startIdx,
                               int    endIdx,
                               const double inReal[],
                               int           optInTimePeriod, /* From 2 to 100000 */
                               int          *outBegIdx,
                               int          *outNBElement,
                               double        outReal[] );

/*
 * TA_LINEARREG_INTERCEPT - Linear Regression Intercept
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_LINEARREG_INTERCEPT( int    startIdx,
                                   int    endIdx,
                                   const double inReal[],
                                   int           optInTimePeriod, /* From 2 to 100000 */
                                   int          *outBegIdx,
                                   int          *outNBElement,
                                   double        outReal[] );

/*
 * TA_LINEARREG_SLOPE - Linear Regression Slope
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_LINEARREG_SLOPE( int    startIdx,
                               int    endIdx,
                               const double inReal[],
                               int           optInTimePeriod, /* From 2 to 100000 */
                               int          *outBegIdx,
                               int          *outNBElement,
                               double        outReal[] );

/*
 * TA_LN - Vector Log Natural
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_LN( int    startIdx,
                  int    endIdx,
                  const double inReal[],
                  int          *outBegIdx,
                  int          *outNBElement,
                  double        outReal[] );

/*
 * TA_LOG10 - Vector Log10
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_LOG10( int    startIdx,
                     int    endIdx,
                     const double inReal[],
                     int          *outBegIdx,
                     int          *outNBElement,
                     double        outReal[] );

/*
 * TA_MA - Moving average
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * optInMAType:
 *    Type of Moving Average
 * 
 * 
 */
TA_RetCode TA_MA( int    startIdx,
                  int    endIdx,
                  const double inReal[],
                  int           optInTimePeriod, /* From 1 to 100000 */
                  TA_MAType     optInMAType,
                  int          *outBegIdx,
                  int          *outNBElement,
                  double        outReal[] );

/*
 * TA_MACD - Moving Average Convergence/Divergence
 * 
 * Input  = double
 * Output = double, double, double
 * 
 * Optional Parameters
 * -------------------
 * optInFastPeriod:(From 2 to 100000)
 *    Number of period for the fast MA
 * 
 * optInSlowPeriod:(From 2 to 100000)
 *    Number of period for the slow MA
 * 
 * optInSignalPeriod:(From 1 to 100000)
 *    Smoothing for the signal line (nb of period)
 * 
 * 
 */
TA_RetCode TA_MACD( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int           optInFastPeriod, /* From 2 to 100000 */
                    int           optInSlowPeriod, /* From 2 to 100000 */
                    int           optInSignalPeriod, /* From 1 to 100000 */
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outMACD[],
                    double        outMACDSignal[],
                    double        outMACDHist[] );

/*
 * TA_MACDEXT - MACD with controllable MA type
 * 
 * Input  = double
 * Output = double, double, double
 * 
 * Optional Parameters
 * -------------------
 * optInFastPeriod:(From 2 to 100000)
 *    Number of period for the fast MA
 * 
 * optInFastMAType:
 *    Type of Moving Average for fast MA
 * 
 * optInSlowPeriod:(From 2 to 100000)
 *    Number of period for the slow MA
 * 
 * optInSlowMAType:
 *    Type of Moving Average for slow MA
 * 
 * optInSignalPeriod:(From 1 to 100000)
 *    Smoothing for the signal line (nb of period)
 * 
 * optInSignalMAType:
 *    Type of Moving Average for signal line
 * 
 * 
 */
TA_RetCode TA_MACDEXT( int    startIdx,
                       int    endIdx,
                       const double inReal[],
                       int           optInFastPeriod, /* From 2 to 100000 */
                       TA_MAType     optInFastMAType,
                       int           optInSlowPeriod, /* From 2 to 100000 */
                       TA_MAType     optInSlowMAType,
                       int           optInSignalPeriod, /* From 1 to 100000 */
                       TA_MAType     optInSignalMAType,
                       int          *outBegIdx,
                       int          *outNBElement,
                       double        outMACD[],
                       double        outMACDSignal[],
                       double        outMACDHist[] );

/*
 * TA_MACDFIX - Moving Average Convergence/Divergence Fix 12/26
 * 
 * Input  = double
 * Output = double, double, double
 * 
 * Optional Parameters
 * -------------------
 * optInSignalPeriod:(From 1 to 100000)
 *    Smoothing for the signal line (nb of period)
 * 
 * 
 */
TA_RetCode TA_MACDFIX( int    startIdx,
                       int    endIdx,
                       const double inReal[],
                       int           optInSignalPeriod, /* From 1 to 100000 */
                       int          *outBegIdx,
                       int          *outNBElement,
                       double        outMACD[],
                       double        outMACDSignal[],
                       double        outMACDHist[] );

/*
 * TA_MAMA - MESA Adaptive Moving Average
 * 
 * Input  = double
 * Output = double, double
 * 
 * Optional Parameters
 * -------------------
 * optInFastLimit:(From 0.01 to 0.99)
 *    Upper limit use in the adaptive algorithm
 * 
 * optInSlowLimit:(From 0.01 to 0.99)
 *    Lower limit use in the adaptive algorithm
 * 
 * 
 */
TA_RetCode TA_MAMA( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    double        optInFastLimit, /* From 0.01 to 0.99 */
                    double        optInSlowLimit, /* From 0.01 to 0.99 */
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outMAMA[],
                    double        outFAMA[] );

/*
 * TA_MAVP - Moving average with variable period
 * 
 * Input  = double, double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInMinPeriod:(From 2 to 100000)
 *    Value less than minimum will be changed to Minimum period
 * 
 * optInMaxPeriod:(From 2 to 100000)
 *    Value higher than maximum will be changed to Maximum period
 * 
 * optInMAType:
 *    Type of Moving Average
 * 
 * 
 */
TA_RetCode TA_MAVP( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    const double inPeriods[],
                    int           optInMinPeriod, /* From 2 to 100000 */
                    int           optInMaxPeriod, /* From 2 to 100000 */
                    TA_MAType     optInMAType,
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_MAX - Highest value over a specified period
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_MAX( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInTimePeriod, /* From 2 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_MAXINDEX - Index of highest value over a specified period
 * 
 * Input  = double
 * Output = int
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_MAXINDEX( int    startIdx,
                        int    endIdx,
                        const double inReal[],
                        int           optInTimePeriod, /* From 2 to 100000 */
                        int          *outBegIdx,
                        int          *outNBElement,
                        int           outInteger[] );

/*
 * TA_MEDPRICE - Median Price
 * 
 * Input  = High, Low
 * Output = double
 * 
 */
TA_RetCode TA_MEDPRICE( int    startIdx,
                        int    endIdx,
                        const double inHigh[],
                        const double inLow[],
                        int          *outBegIdx,
                        int          *outNBElement,
                        double        outReal[] );

/*
 * TA_MFI - Money Flow Index
 * 
 * Input  = High, Low, Close, Volume
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_MFI( int    startIdx,
                   int    endIdx,
                   const double inHigh[],
                   const double inLow[],
                   const double inClose[],
                   const double inVolume[],
                   int           optInTimePeriod, /* From 2 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_MIDPOINT - MidPoint over period
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_MIDPOINT( int    startIdx,
                        int    endIdx,
                        const double inReal[],
                        int           optInTimePeriod, /* From 2 to 100000 */
                        int          *outBegIdx,
                        int          *outNBElement,
                        double        outReal[] );

/*
 * TA_MIDPRICE - Midpoint Price over period
 * 
 * Input  = High, Low
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_MIDPRICE( int    startIdx,
                        int    endIdx,
                        const double inHigh[],
                        const double inLow[],
                        int           optInTimePeriod, /* From 2 to 100000 */
                        int          *outBegIdx,
                        int          *outNBElement,
                        double        outReal[] );

/*
 * TA_MIN - Lowest value over a specified period
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_MIN( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInTimePeriod, /* From 2 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_MININDEX - Index of lowest value over a specified period
 * 
 * Input  = double
 * Output = int
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_MININDEX( int    startIdx,
                        int    endIdx,
                        const double inReal[],
                        int           optInTimePeriod, /* From 2 to 100000 */
                        int          *outBegIdx,
                        int          *outNBElement,
                        int           outInteger[] );

/*
 * TA_MINMAX - Lowest and highest values over a specified period
 * 
 * Input  = double
 * Output = double, double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_MINMAX( int    startIdx,
                      int    endIdx,
                      const double inReal[],
                      int           optInTimePeriod, /* From 2 to 100000 */
                      int          *outBegIdx,
                      int          *outNBElement,
                      double        outMin[],
                      double        outMax[] );

/*
 * TA_MINMAXINDEX - Indexes of lowest and highest values over a specified period
 * 
 * Input  = double
 * Output = int, int
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_MINMAXINDEX( int    startIdx,
                           int    endIdx,
                           const double inReal[],
                           int           optInTimePeriod, /* From 2 to 100000 */
                           int          *outBegIdx,
                           int          *outNBElement,
                           int           outMinIdx[],
                           int           outMaxIdx[] );

/*
 * TA_MINUS_DI - Minus Directional Indicator
 * 
 * Input  = High, Low, Close
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_MINUS_DI( int    startIdx,
                        int    endIdx,
                        const double inHigh[],
                        const double inLow[],
                        const double inClose[],
                        int           optInTimePeriod, /* From 1 to 100000 */
                        int          *outBegIdx,
                        int          *outNBElement,
                        double        outReal[] );

/*
 * TA_MINUS_DM - Minus Directional Movement
 * 
 * Input  = High, Low
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_MINUS_DM( int    startIdx,
                        int    endIdx,
                        const double inHigh[],
                        const double inLow[],
                        int           optInTimePeriod, /* From 1 to 100000 */
                        int          *outBegIdx,
                        int          *outNBElement,
                        double        outReal[] );

/*
 * TA_MOM - Momentum
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_MOM( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInTimePeriod, /* From 1 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_MULT - Vector Arithmetic Mult
 * 
 * Input  = double, double
 * Output = double
 * 
 */
TA_RetCode TA_MULT( int    startIdx,
                    int    endIdx,
                    const double inReal0[],
                    const double inReal1[],
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_NATR - Normalized Average True Range
 * 
 * Input  = High, Low, Close
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_NATR( int    startIdx,
                    int    endIdx,
                    const double inHigh[],
                    const double inLow[],
                    const double inClose[],
                    int           optInTimePeriod, /* From 1 to 100000 */
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_OBV - On Balance Volume
 * 
 * Input  = double, Volume
 * Output = double
 * 
 */
TA_RetCode TA_OBV( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   const double inVolume[],
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_PLUS_DI - Plus Directional Indicator
 * 
 * Input  = High, Low, Close
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_PLUS_DI( int    startIdx,
                       int    endIdx,
                       const double inHigh[],
                       const double inLow[],
                       const double inClose[],
                       int           optInTimePeriod, /* From 1 to 100000 */
                       int          *outBegIdx,
                       int          *outNBElement,
                       double        outReal[] );

/*
 * TA_PLUS_DM - Plus Directional Movement
 * 
 * Input  = High, Low
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_PLUS_DM( int    startIdx,
                       int    endIdx,
                       const double inHigh[],
                       const double inLow[],
                       int           optInTimePeriod, /* From 1 to 100000 */
                       int          *outBegIdx,
                       int          *outNBElement,
                       double        outReal[] );

/*
 * TA_PPO - Percentage Price Oscillator
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInFastPeriod:(From 2 to 100000)
 *    Number of period for the fast MA
 * 
 * optInSlowPeriod:(From 2 to 100000)
 *    Number of period for the slow MA
 * 
 * optInMAType:
 *    Type of Moving Average
 * 
 * 
 */
TA_RetCode TA_PPO( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInFastPeriod, /* From 2 to 100000 */
                   int           optInSlowPeriod, /* From 2 to 100000 */
                   TA_MAType     optInMAType,
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_ROC - Rate of change : ((price/prevPrice)-1)*100
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_ROC( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInTimePeriod, /* From 1 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_ROCP - Rate of change Percentage: (price-prevPrice)/prevPrice
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_ROCP( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int           optInTimePeriod, /* From 1 to 100000 */
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_ROCR - Rate of change ratio: (price/prevPrice)
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_ROCR( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int           optInTimePeriod, /* From 1 to 100000 */
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_ROCR100 - Rate of change ratio 100 scale: (price/prevPrice)*100
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_ROCR100( int    startIdx,
                       int    endIdx,
                       const double inReal[],
                       int           optInTimePeriod, /* From 1 to 100000 */
                       int          *outBegIdx,
                       int          *outNBElement,
                       double        outReal[] );

/*
 * TA_RSI - Relative Strength Index
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_RSI( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInTimePeriod, /* From 2 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_SAR - Parabolic SAR
 * 
 * Input  = High, Low
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInAcceleration:(From 0 to TA_REAL_MAX)
 *    Acceleration Factor used up to the Maximum value
 * 
 * optInMaximum:(From 0 to TA_REAL_MAX)
 *    Acceleration Factor Maximum value
 * 
 * 
 */
TA_RetCode TA_SAR( int    startIdx,
                   int    endIdx,
                   const double inHigh[],
                   const double inLow[],
                   double        optInAcceleration, /* From 0 to TA_REAL_MAX */
                   double        optInMaximum, /* From 0 to TA_REAL_MAX */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_SAREXT - Parabolic SAR - Extended
 * 
 * Input  = High, Low
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInStartValue:(From TA_REAL_MIN to TA_REAL_MAX)
 *    Start value and direction. 0 for Auto, >0 for Long, <0 for Short
 * 
 * optInOffsetOnReverse:(From 0 to TA_REAL_MAX)
 *    Percent offset added/removed to initial stop on short/long reversal
 * 
 * optInAccelerationInitLong:(From 0 to TA_REAL_MAX)
 *    Acceleration Factor initial value for the Long direction
 * 
 * optInAccelerationLong:(From 0 to TA_REAL_MAX)
 *    Acceleration Factor for the Long direction
 * 
 * optInAccelerationMaxLong:(From 0 to TA_REAL_MAX)
 *    Acceleration Factor maximum value for the Long direction
 * 
 * optInAccelerationInitShort:(From 0 to TA_REAL_MAX)
 *    Acceleration Factor initial value for the Short direction
 * 
 * optInAccelerationShort:(From 0 to TA_REAL_MAX)
 *    Acceleration Factor for the Short direction
 * 
 * optInAccelerationMaxShort:(From 0 to TA_REAL_MAX)
 *    Acceleration Factor maximum value for the Short direction
 * 
 * 
 */
TA_RetCode TA_SAREXT( int    startIdx,
                      int    endIdx,
                      const double inHigh[],
                      const double inLow[],
                      double        optInStartValue, /* From TA_REAL_MIN to TA_REAL_MAX */
                      double        optInOffsetOnReverse, /* From 0 to TA_REAL_MAX */
                      double        optInAccelerationInitLong, /* From 0 to TA_REAL_MAX */
                      double        optInAccelerationLong, /* From 0 to TA_REAL_MAX */
                      double        optInAccelerationMaxLong, /* From 0 to TA_REAL_MAX */
                      double        optInAccelerationInitShort, /* From 0 to TA_REAL_MAX */
                      double        optInAccelerationShort, /* From 0 to TA_REAL_MAX */
                      double        optInAccelerationMaxShort, /* From 0 to TA_REAL_MAX */
                      int          *outBegIdx,
                      int          *outNBElement,
                      double        outReal[] );

/*
 * TA_SIN - Vector Trigonometric Sin
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_SIN( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_SINH - Vector Trigonometric Sinh
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_SINH( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_SMA - Simple Moving Average
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_SMA( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInTimePeriod, /* From 2 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_SQRT - Vector Square Root
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_SQRT( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_STDDEV - Standard Deviation
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * optInNbDev:(From TA_REAL_MIN to TA_REAL_MAX)
 *    Nb of deviations
 * 
 * 
 */
TA_RetCode TA_STDDEV( int    startIdx,
                      int    endIdx,
                      const double inReal[],
                      int           optInTimePeriod, /* From 2 to 100000 */
                      double        optInNbDev, /* From TA_REAL_MIN to TA_REAL_MAX */
                      int          *outBegIdx,
                      int          *outNBElement,
                      double        outReal[] );

/*
 * TA_STOCH - Stochastic
 * 
 * Input  = High, Low, Close
 * Output = double, double
 * 
 * Optional Parameters
 * -------------------
 * optInFastK_Period:(From 1 to 100000)
 *    Time period for building the Fast-K line
 * 
 * optInSlowK_Period:(From 1 to 100000)
 *    Smoothing for making the Slow-K line. Usually set to 3
 * 
 * optInSlowK_MAType:
 *    Type of Moving Average for Slow-K
 * 
 * optInSlowD_Period:(From 1 to 100000)
 *    Smoothing for making the Slow-D line
 * 
 * optInSlowD_MAType:
 *    Type of Moving Average for Slow-D
 * 
 * 
 */
TA_RetCode TA_STOCH( int    startIdx,
                     int    endIdx,
                     const double inHigh[],
                     const double inLow[],
                     const double inClose[],
                     int           optInFastK_Period, /* From 1 to 100000 */
                     int           optInSlowK_Period, /* From 1 to 100000 */
                     TA_MAType     optInSlowK_MAType,
                     int           optInSlowD_Period, /* From 1 to 100000 */
                     TA_MAType     optInSlowD_MAType,
                     int          *outBegIdx,
                     int          *outNBElement,
                     double        outSlowK[],
                     double        outSlowD[] );

/*
 * TA_STOCHF - Stochastic Fast
 * 
 * Input  = High, Low, Close
 * Output = double, double
 * 
 * Optional Parameters
 * -------------------
 * optInFastK_Period:(From 1 to 100000)
 *    Time period for building the Fast-K line
 * 
 * optInFastD_Period:(From 1 to 100000)
 *    Smoothing for making the Fast-D line. Usually set to 3
 * 
 * optInFastD_MAType:
 *    Type of Moving Average for Fast-D
 * 
 * 
 */
TA_RetCode TA_STOCHF( int    startIdx,
                      int    endIdx,
                      const double inHigh[],
                      const double inLow[],
                      const double inClose[],
                      int           optInFastK_Period, /* From 1 to 100000 */
                      int           optInFastD_Period, /* From 1 to 100000 */
                      TA_MAType     optInFastD_MAType,
                      int          *outBegIdx,
                      int          *outNBElement,
                      double        outFastK[],
                      double        outFastD[] );

/*
 * TA_STOCHRSI - Stochastic Relative Strength Index
 * 
 * Input  = double
 * Output = double, double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * optInFastK_Period:(From 1 to 100000)
 *    Time period for building the Fast-K line
 * 
 * optInFastD_Period:(From 1 to 100000)
 *    Smoothing for making the Fast-D line. Usually set to 3
 * 
 * optInFastD_MAType:
 *    Type of Moving Average for Fast-D
 * 
 * 
 */
TA_RetCode TA_STOCHRSI( int    startIdx,
                        int    endIdx,
                        const double inReal[],
                        int           optInTimePeriod, /* From 2 to 100000 */
                        int           optInFastK_Period, /* From 1 to 100000 */
                        int           optInFastD_Period, /* From 1 to 100000 */
                        TA_MAType     optInFastD_MAType,
                        int          *outBegIdx,
                        int          *outNBElement,
                        double        outFastK[],
                        double        outFastD[] );

/*
 * TA_SUB - Vector Arithmetic Substraction
 * 
 * Input  = double, double
 * Output = double
 * 
 */
TA_RetCode TA_SUB( int    startIdx,
                   int    endIdx,
                   const double inReal0[],
                   const double inReal1[],
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_SUM - Summation
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_SUM( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInTimePeriod, /* From 2 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_T3 - Triple Exponential Moving Average (T3)
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * optInVFactor:(From 0 to 1)
 *    Volume Factor
 * 
 * 
 */
TA_RetCode TA_T3( int    startIdx,
                  int    endIdx,
                  const double inReal[],
                  int           optInTimePeriod, /* From 2 to 100000 */
                  double        optInVFactor, /* From 0 to 1 */
                  int          *outBegIdx,
                  int          *outNBElement,
                  double        outReal[] );

/*
 * TA_TAN - Vector Trigonometric Tan
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_TAN( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_TANH - Vector Trigonometric Tanh
 * 
 * Input  = double
 * Output = double
 * 
 */
TA_RetCode TA_TANH( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_TEMA - Triple Exponential Moving Average
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_TEMA( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int           optInTimePeriod, /* From 2 to 100000 */
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_TRANGE - True Range
 * 
 * Input  = High, Low, Close
 * Output = double
 * 
 */
TA_RetCode TA_TRANGE( int    startIdx,
                      int    endIdx,
                      const double inHigh[],
                      const double inLow[],
                      const double inClose[],
                      int          *outBegIdx,
                      int          *outNBElement,
                      double        outReal[] );

/*
 * TA_TRIMA - Triangular Moving Average
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_TRIMA( int    startIdx,
                     int    endIdx,
                     const double inReal[],
                     int           optInTimePeriod, /* From 2 to 100000 */
                     int          *outBegIdx,
                     int          *outNBElement,
                     double        outReal[] );

/*
 * TA_TRIX - 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_TRIX( int    startIdx,
                    int    endIdx,
                    const double inReal[],
                    int           optInTimePeriod, /* From 1 to 100000 */
                    int          *outBegIdx,
                    int          *outNBElement,
                    double        outReal[] );

/*
 * TA_TSF - Time Series Forecast
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_TSF( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInTimePeriod, /* From 2 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_TYPPRICE - Typical Price
 * 
 * Input  = High, Low, Close
 * Output = double
 * 
 */
TA_RetCode TA_TYPPRICE( int    startIdx,
                        int    endIdx,
                        const double inHigh[],
                        const double inLow[],
                        const double inClose[],
                        int          *outBegIdx,
                        int          *outNBElement,
                        double        outReal[] );

/*
 * TA_ULTOSC - Ultimate Oscillator
 * 
 * Input  = High, Low, Close
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod1:(From 1 to 100000)
 *    Number of bars for 1st period.
 * 
 * optInTimePeriod2:(From 1 to 100000)
 *    Number of bars fro 2nd period
 * 
 * optInTimePeriod3:(From 1 to 100000)
 *    Number of bars for 3rd period
 * 
 * 
 */
TA_RetCode TA_ULTOSC( int    startIdx,
                      int    endIdx,
                      const double inHigh[],
                      const double inLow[],
                      const double inClose[],
                      int           optInTimePeriod1, /* From 1 to 100000 */
                      int           optInTimePeriod2, /* From 1 to 100000 */
                      int           optInTimePeriod3, /* From 1 to 100000 */
                      int          *outBegIdx,
                      int          *outNBElement,
                      double        outReal[] );

/*
 * TA_VAR - Variance
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 1 to 100000)
 *    Number of period
 * 
 * optInNbDev:(From TA_REAL_MIN to TA_REAL_MAX)
 *    Nb of deviations
 * 
 * 
 */
TA_RetCode TA_VAR( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInTimePeriod, /* From 1 to 100000 */
                   double        optInNbDev, /* From TA_REAL_MIN to TA_REAL_MAX */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );

/*
 * TA_WCLPRICE - Weighted Close Price
 * 
 * Input  = High, Low, Close
 * Output = double
 * 
 */
TA_RetCode TA_WCLPRICE( int    startIdx,
                        int    endIdx,
                        const double inHigh[],
                        const double inLow[],
                        const double inClose[],
                        int          *outBegIdx,
                        int          *outNBElement,
                        double        outReal[] );

/*
 * TA_WILLR - Williams' %R
 * 
 * Input  = High, Low, Close
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_WILLR( int    startIdx,
                     int    endIdx,
                     const double inHigh[],
                     const double inLow[],
                     const double inClose[],
                     int           optInTimePeriod, /* From 2 to 100000 */
                     int          *outBegIdx,
                     int          *outNBElement,
                     double        outReal[] );

/*
 * TA_WMA - Weighted Moving Average
 * 
 * Input  = double
 * Output = double
 * 
 * Optional Parameters
 * -------------------
 * optInTimePeriod:(From 2 to 100000)
 *    Number of period
 * 
 * 
 */
TA_RetCode TA_WMA( int    startIdx,
                   int    endIdx,
                   const double inReal[],
                   int           optInTimePeriod, /* From 2 to 100000 */
                   int          *outBegIdx,
                   int          *outNBElement,
                   double        outReal[] );
