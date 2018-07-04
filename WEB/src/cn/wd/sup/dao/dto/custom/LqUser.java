package cn.wd.sup.dao.dto.custom;

import java.sql.Timestamp;

import com.zxt.framework.mvc.dao.Domain;
/**
 * 用户表 lq_user
 * @author zhengkai
 *
 */
public class LqUser extends Domain{

	/**
	 * 序列化id
	 */
	private static final long serialVersionUID = 1L;

	private Integer userId;
	
	private String username;
	
	private String password;
	
	private Integer type;
	
	private Timestamp lastLogin;

	public Integer getUserId() {
		return userId;
	}

	public void setUserId(Integer userId) {
		this.userId = userId;
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public Integer getType() {
		return type;
	}

	public void setType(Integer type) {
		this.type = type;
	}

	public Timestamp getLastLogin() {
		return lastLogin;
	}

	public void setLastLogin(Timestamp lastLogin) {
		this.lastLogin = lastLogin;
	}

	public static long getSerialversionuid() {
		return serialVersionUID;
	}
	
	
}
