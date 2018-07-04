package cn.wd.auditor.custom;

import java.util.Date;

import com.zxt.framework.mvc.dao.Domain;

/**
 * 
    * @Package cn.wd.auditor.custom
    * @ClassName: WoLog
    * @Description: 工单审计日志对象
    * @author WD created.
    * @date 2018年2月2日
    *
 */
public class WoLog extends Domain{

	private static final long serialVersionUID = 1L;

	private String account;
	
	private Long wid;
	
	private Integer action;
	
	private Integer actionStatus;
	
	private String modifyContent;
	
	private Date auditTime;

	public String getAccount() {
		return account;
	}

	public void setAccount(String account) {
		this.account = account;
	}

	public Long getWid() {
		return wid;
	}

	public void setWid(Long wid) {
		this.wid = wid;
	}

	public Integer getAction() {
		return action;
	}

	public void setAction(Integer action) {
		this.action = action;
	}

	public Integer getActionStatus() {
		return actionStatus;
	}

	public void setActionStatus(Integer actionStatus) {
		this.actionStatus = actionStatus;
	}

	public String getModifyContent() {
		return modifyContent;
	}

	public void setModifyContent(String modifyContent) {
		this.modifyContent = modifyContent;
	}

	public Date getAuditTime() {
		return auditTime;
	}

	public void setAuditTime(Date auditTime) {
		this.auditTime = auditTime;
	}
}
