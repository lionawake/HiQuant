package cn.wd.sup.dao.dto;

import com.zxt.framework.mvc.dao.Domain;

/**
 * 
    * @Package cn.wd.sup.dao.dto
    * @ClassName: SysAccount
    * @Description: 账户对象
    * @author WD created.
    * @date 2017年9月29日
    *
 */
public class SysAccount extends Domain{
	    
	private static final long serialVersionUID = 1L;

	private String personName;

	private String userName;
	
	private String password;
	
	private String email;
	
	private String phone;
	
	private Integer role;
	
	private Integer status;
	
	public Integer getStatus() {
		return status;
	}

	public void setStatus(Integer status) {
		this.status = status;
	}

	public Integer getRole() {
		return role;
	}

	public void setRole(Integer role) {
		this.role = role;
	}

	public String getPersonName() {
		return personName;
	}

	public void setPersonName(String personName) {
		this.personName = personName;
	}

	public String getUserName() {
		return userName;
	}

	public void setUserName(String userName) {
		this.userName = userName;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}
}
