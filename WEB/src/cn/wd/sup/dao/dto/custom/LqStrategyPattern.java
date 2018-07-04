package cn.wd.sup.dao.dto.custom;


import java.sql.Timestamp;

import com.zxt.framework.mvc.dao.Domain;
/**
 * 策略模板表（保存用于通过因子代换生成策略的模板） lq_strategy_pattern
 * @author zhengkai
 *
 */
public class LqStrategyPattern extends Domain{

	/**
	 * 序列化id
	 */
	private static final long serialVersionUID = 1L;
	
	/**
	 * spId
	 */
	private Long spId;
	
	/**
	 * sp名称
	 */
	private String spName;
	
	/**
	 * 作者
	 */
	private String author;
	
	/**
	 * 创建时间
	 */
	private Timestamp createTime;
	
	/**
	 * 状态
	 */
	private Integer testStatus;
	
	/**
	 * 分解出的任务总数
	 */
	private Long taskTotal;
	
	/**
	 * 已执行的任务数
	 */
	private Long taskFinished;
	
	/**
	 * 代码
	 */
	private String code;
	
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

	public String getSpName() {
		return spName;
	}

	public void setSpName(String spName) {
		this.spName = spName;
	}

	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	public Timestamp getCreateTime() {
		return createTime;
	}

	public void setCreateTime(Timestamp createTime) {
		this.createTime = createTime;
	}

	public Integer getTestStatus() {
		return testStatus;
	}

	public void setTestStatus(Integer testStatus) {
		this.testStatus = testStatus;
	}

	public Long getTaskTotal() {
		return taskTotal;
	}

	public void setTaskTotal(Long taskTotal) {
		this.taskTotal = taskTotal;
	}

	public Long getTaskFinished() {
		return taskFinished;
	}

	public void setTaskFinished(Long taskFinished) {
		this.taskFinished = taskFinished;
	}

	public String getCode() {
		return code;
	}

	public void setCode(String code) {
		this.code = code;
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
