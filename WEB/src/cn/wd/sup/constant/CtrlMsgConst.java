package cn.wd.sup.constant;

/**
 * 
 * @author WD
 *
 * PulishDate: 2017年9月17日
 * Function: Controller层的提示信息常量 
 * ChangeLog:
 */
public class CtrlMsgConst {

	//for login controller

	public static final String MSG_ERROR									= "出错了，请重试";
	
	//for login/logout
	public static final String MSG_LOGIN_FAILED_ACCOUNT			= "帐户或者密码错误.";
	public static final String MSG_LOGIN_FAILED_SYSTEM				= "系统错误，请稍后重试.";
	public static final String MSG_LOGOUT_FAILED_SYSTEM			= "系统错误.";
	public static final String MSG_REGISTER_FAILED_ACCOUNT		= "帐户已经存在，请重新注册.";
	public static final String MSG_REVER_FAILED_ACCOUNT			= "帐户不存在，请注册.";
	
	
	public static final String MSG_SESSION_TIMEOUT					= "#999";//"操作超时，请重新登录.";
	public static final String MSG_PRO_NO								= "#403";//"您无权限操作.";
	
}
