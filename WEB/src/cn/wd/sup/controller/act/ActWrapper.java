package cn.wd.sup.controller.act;

import com.zxt.framework.mvc.controller.bean.UserWrapper;

/**
 * 
 * @author WD
 *
 * PulishDate: 2017年9月5日
 * Function: 存储用户session信息的对象 
 * ChangeLog:
 */
public class ActWrapper extends UserWrapper {

	private Integer roleId;
	
	private String usrPath;
	
	private String sharePath;

	public String getSharePath() {
		return sharePath;
	}

	public void setSharePath(String sharePath) {
		this.sharePath = sharePath;
	}

	public String getUsrPath() {
		return usrPath;
	}

	public void setUsrPath(String usrPath) {
		this.usrPath = usrPath;
	}

	public Integer getRoleId() {
		return roleId;
	}

	public void setRoleId(Integer roleId) {
		this.roleId = roleId;
	}
}
