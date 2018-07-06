package cn.wd.sup.dao.dto.custom;

import com.zxt.framework.mvc.dao.Domain;

/**
 * 策略表（保存从模板产生的具体策略） lq_strategy
 * @author zhengkai
 *
 */
public class LqStrategy extends Domain{

	/**
	 * 序列化id
	 */
	private static final long serialVersionUID = 1L;
	
	/**
	 * sp id
	 */
	private Long spId;
	
	/**
	 * s id
	 */
	private Long sId;
	
	/**
	 * 代码
	 */
	private String code;
	
	/**
	 * 
	 */
	private String dataPath;
	
	/**
	 * 净利润
	 */
	private Double netProfit;
	
	/**
	 * 总盈利
	 */
	private Double totalProfit;
	
	/**
	 * 总亏损
	 */
	private Double totalLoss;
	
	/**
	 * 总盈利/总亏损
	 */
	private Double totalProfitLoss;
	
	/**
	 * 交易手数
	 */
	private Integer tradeLot;
	
	/**
	 * 盈利比率
	 */
	private Double profitRatio;
	
	/**
	 * 平均利润
	 */
	private Double averageProfit;
	
	/**
	 * 平均亏损
	 */
	private Double averageLoss;
	
	/**
	 * 平均盈利/平均亏损
	 */
	private Double averageProfitLoss;
	
	/**
	 * 最大盈利
	 */
	private Double maxProfit;
	
	/**
	 * 最大亏损
	 */
	private Double maxLoss;
	
	/**
	 * 最大盈利/总盈利
	 */
	private Double maxTotalProfit;
	
	/**
	 * 最大亏损/总亏损
	 */
	private Double maxTotalLoss;
	
	/**
	 * 平均持仓周期
	 */
	private Integer averageHoldPeriod;
	
	/**
	 * 最大使用资金
	 */
	private Double maxFundUse;
	
	/**
	 * 收益率
	 */
	private Double yieldRate;
	
	/**
	 * 年化收益率
	 */
	private Double annualReturn;
	
	/**
	 * 有效收益率
	 */
	private Double effectYield;
	
	/**
	 * 收益风险比
	 */
	private Double benefitRiskRatio;
	
	/**
	 * 调整收益风险比
	 */
	private Double adjBenefitRiskRatio;
	
	/**
	 * 收益曲线R平方值
	 */
	private Double rSquareYieldCurve;
	
	/**
	 * 夏普比率
	 */
	private Double sharpeRatio;
	
	/**
	 * 总交易时间
	 */
	private Integer totalTransTime;
	
	/**
	 * 持仓时间比率
	 */
	private Double holdPeriodRatio;
	
	/**
	 * 最大资产回撤值
	 */
	private Double maxRetraceValue;
	
	/**
	 * 最大资产回撤值比率
	 */
	private Double maxRetraceRatio;
	
	
	private String profit_daily;
	
	private String profit_monthly;
	
	
	public String getProfit_daily() {
		return profit_daily;
	}

	public void setProfit_daily(String profit_daily) {
		this.profit_daily = profit_daily;
	}

	public String getProfit_monthly() {
		return profit_monthly;
	}

	public void setProfit_monthly(String profit_monthly) {
		this.profit_monthly = profit_monthly;
	}

	/**
	 * 排序方式
	 */
	private String sortStr;

	public Long getSpId() {
		return spId;
	}

	public void setSpId(Long spId) {
		this.spId = spId;
	}

	public Long getsId() {
		return sId;
	}

	public void setsId(Long sId) {
		this.sId = sId;
	}

	public String getCode() {
		return code;
	}

	public void setCode(String code) {
		this.code = code;
	}

	public String getDataPath() {
		return dataPath;
	}

	public void setDataPath(String dataPath) {
		this.dataPath = dataPath;
	}

	public Double getNetProfit() {
		return netProfit;
	}

	public void setNetProfit(Double netProfit) {
		this.netProfit = netProfit;
	}

	public Double getTotalProfit() {
		return totalProfit;
	}

	public void setTotalProfit(Double totalProfit) {
		this.totalProfit = totalProfit;
	}

	public Double getTotalLoss() {
		return totalLoss;
	}

	public void setTotalLoss(Double totalLoss) {
		this.totalLoss = totalLoss;
	}

	public Double getTotalProfitLoss() {
		return totalProfitLoss;
	}

	public void setTotalProfitLoss(Double totalProfitLoss) {
		this.totalProfitLoss = totalProfitLoss;
	}

	public Integer getTradeLot() {
		return tradeLot;
	}

	public void setTradeLot(Integer tradeLot) {
		this.tradeLot = tradeLot;
	}

	public Double getProfitRatio() {
		return profitRatio;
	}

	public void setProfitRatio(Double profitRatio) {
		this.profitRatio = profitRatio;
	}

	public Double getAverageProfit() {
		return averageProfit;
	}

	public void setAverageProfit(Double averageProfit) {
		this.averageProfit = averageProfit;
	}

	public Double getAverageLoss() {
		return averageLoss;
	}

	public void setAverageLoss(Double averageLoss) {
		this.averageLoss = averageLoss;
	}

	public Double getAverageProfitLoss() {
		return averageProfitLoss;
	}

	public void setAverageProfitLoss(Double averageProfitLoss) {
		this.averageProfitLoss = averageProfitLoss;
	}

	public Double getMaxProfit() {
		return maxProfit;
	}

	public void setMaxProfit(Double maxProfit) {
		this.maxProfit = maxProfit;
	}

	public Double getMaxLoss() {
		return maxLoss;
	}

	public void setMaxLoss(Double maxLoss) {
		this.maxLoss = maxLoss;
	}

	public Double getMaxTotalProfit() {
		return maxTotalProfit;
	}

	public void setMaxTotalProfit(Double maxTotalProfit) {
		this.maxTotalProfit = maxTotalProfit;
	}

	public Double getMaxTotalLoss() {
		return maxTotalLoss;
	}

	public void setMaxTotalLoss(Double maxTotalLoss) {
		this.maxTotalLoss = maxTotalLoss;
	}

	public Integer getAverageHoldPeriod() {
		return averageHoldPeriod;
	}

	public void setAverageHoldPeriod(Integer averageHoldPeriod) {
		this.averageHoldPeriod = averageHoldPeriod;
	}

	public Double getMaxFundUse() {
		return maxFundUse;
	}

	public void setMaxFundUse(Double maxFundUse) {
		this.maxFundUse = maxFundUse;
	}

	public Double getYieldRate() {
		return yieldRate;
	}

	public void setYieldRate(Double yieldRate) {
		this.yieldRate = yieldRate;
	}

	public Double getAnnualReturn() {
		return annualReturn;
	}

	public void setAnnualReturn(Double annualReturn) {
		this.annualReturn = annualReturn;
	}

	public Double getEffectYield() {
		return effectYield;
	}

	public void setEffectYield(Double effectYield) {
		this.effectYield = effectYield;
	}

	public Double getBenefitRiskRatio() {
		return benefitRiskRatio;
	}

	public void setBenefitRiskRatio(Double benefitRiskRatio) {
		this.benefitRiskRatio = benefitRiskRatio;
	}

	public Double getAdjBenefitRiskRatio() {
		return adjBenefitRiskRatio;
	}

	public void setAdjBenefitRiskRatio(Double adjBenefitRiskRatio) {
		this.adjBenefitRiskRatio = adjBenefitRiskRatio;
	}

	public Double getrSquareYieldCurve() {
		return rSquareYieldCurve;
	}

	public void setrSquareYieldCurve(Double rSquareYieldCurve) {
		this.rSquareYieldCurve = rSquareYieldCurve;
	}

	public Double getSharpeRatio() {
		return sharpeRatio;
	}

	public void setSharpeRatio(Double sharpeRatio) {
		this.sharpeRatio = sharpeRatio;
	}

	public Integer getTotalTransTime() {
		return totalTransTime;
	}

	public void setTotalTransTime(Integer totalTransTime) {
		this.totalTransTime = totalTransTime;
	}

	public Double getHoldPeriodRatio() {
		return holdPeriodRatio;
	}

	public void setHoldPeriodRatio(Double holdPeriodRatio) {
		this.holdPeriodRatio = holdPeriodRatio;
	}

	public Double getMaxRetraceValue() {
		return maxRetraceValue;
	}

	public void setMaxRetraceValue(Double maxRetraceValue) {
		this.maxRetraceValue = maxRetraceValue;
	}

	public Double getMaxRetraceRatio() {
		return maxRetraceRatio;
	}

	public void setMaxRetraceRatio(Double maxRetraceRatio) {
		this.maxRetraceRatio = maxRetraceRatio;
	}

	public static long getSerialversionuid() {
		return serialVersionUID;
	}

	public String getSortStr() {
		return sortStr;
	}

	public void setSortStr(String sortStr) {
		this.sortStr = sortStr;
	}
	
	
}