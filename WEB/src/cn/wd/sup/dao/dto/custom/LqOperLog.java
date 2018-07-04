package cn.wd.sup.dao.dto.custom;

import java.sql.Timestamp;

import com.zxt.framework.mvc.dao.Domain;
/**
 * 
 * @author zhengkai
 *
 */
public class LqOperLog extends Domain{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private Timestamp actTime;
	
	private String username;
	
	private String operLog;

	public Timestamp getActTime() {
		return actTime;
	}

	public void setActTime(Timestamp actTime) {
		this.actTime = actTime;
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getOperLog() {
		return operLog;
	}

	public void setOperLog(String operLog) {
		this.operLog = operLog;
	}

	public static long getSerialversionuid() {
		return serialVersionUID;
	}
	
	
	
}
