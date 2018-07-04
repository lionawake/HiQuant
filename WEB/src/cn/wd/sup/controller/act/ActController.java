package cn.wd.sup.controller.act;

import java.util.List;

import javax.crypto.SecretKey;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import javax.ws.rs.core.Context;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import cn.wd.sup.bo.IBoAccount;
import cn.wd.sup.constant.CtrlMsgConst;
import cn.wd.sup.constant.CtrlSettingConst;
import cn.wd.sup.controller.SupController;
import cn.wd.sup.dao.dto.SysAccount;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.zxt.framework.exception.BOException;
import com.zxt.framework.exception.BOMsgException;
import com.zxt.framework.utils.Base64Utils;
import com.zxt.framework.utils.code.DesEncrypterUtil;

/**
 * 
 * @author WD
 *
 * PulishDate: 2017年9月17日
 * Function: 系统配置>>帐户管理的表现层控制类
 * ChangeLog:
 */
@Controller
@RequestMapping("sup/account")
public class ActController  extends SupController{

	private IBoAccount boAccount;
	//激活重定向页面
	private static final String VERIFY_REDIR_PATH = "login.html";
	//加密密钥
	private static final String VERIFY_KEY = "AFF55F179F88419BABB78B0B79FB4705";

	//加密密钥
	private static final String ACCOUNT_DEFAULT = "admin";	
	
	/**
	 * 帐户登录验证接口
	 * @param request HttpRequest
	 * @param response HttpResponse
	 * @param userName 帐户名
	 * @param passwd 帐户密码
	 * @return 操作结果
	 */
	@RequestMapping(value="/login",method=RequestMethod.POST)
	@ResponseBody
	public JSONObject Login( HttpServletRequest request,HttpServletResponse response, @RequestBody String jsonString ){
		
		logger.debug( "THE ACCOUNT INFO IS: " + jsonString);
		if( jsonString.isEmpty()){
			return getErrorResult( null);
		}
		try{
			JSONObject loginJo = JSONObject.parseObject( jsonString);
			if( loginJo.getString("username")==null || loginJo.getString("password") == null ){
				return getErrorResult( null);
			}
			String userName = loginJo.getString("username");
			String passwd = loginJo.getString("password");
			// password md5.
			String _pwd = Base64Utils.decode4String(passwd.getBytes());

			SysAccount account = boAccount.login( userName, _pwd);
			if( account == null )
				return getErrorResult( CtrlMsgConst.MSG_LOGIN_FAILED_ACCOUNT);
			
			//set ActWrapperper to session 
			ActWrapper wrap = new ActWrapper();
			wrap.setUserName( userName);
			wrap.setRoleId(account.getRole()+99 );
			
			HttpSession session = request.getSession();
			session.setAttribute( CtrlSettingConst.HTTP_SESSION_ATTR,  JSONObject.toJSON( wrap));
			logger.debug( "LOGIN SUCCESS, AND THE SESSION IS:"+JSON.toJSONString( JSONObject.toJSON( wrap) ) );
			return getSuccessResult( null);
		}catch( BOException be){
//			be.printStackTrace();
			return getErrorResult( CtrlMsgConst.MSG_LOGIN_FAILED_ACCOUNT);
		}catch( Exception e){
//			e.printStackTrace();
			return getErrorResult( CtrlMsgConst.MSG_LOGIN_FAILED_SYSTEM);
		}
	}

	/**
	 * 帐户登出接口
	 * @param request HttpRequest
	 * @param response HttpResponse
	 * @return login成功或者失败的信息
	 */
	@RequestMapping(value="/logout",method=RequestMethod.GET)
	@ResponseBody
	public JSONObject Logout(  HttpServletRequest request,HttpServletResponse response){
		try{			
			HttpSession session = request.getSession();
			session.removeAttribute(  CtrlSettingConst.HTTP_SESSION_ATTR );
			return getSuccessResult( null);
		}catch( Exception e){
			return getErrorResult( CtrlMsgConst.MSG_LOGOUT_FAILED_SYSTEM);
		}
	}

	/**
	 * 添加新的用户
	 * @param request HttpRequest
	 * @param jsonString 用户信息的JSON结构数据
	 * @return 操作结果
	 */
	@RequestMapping(value="/reg",method=RequestMethod.POST)
	@ResponseBody
	public JSONObject regAccount(@Context HttpServletRequest request, @RequestBody String jsonString ){
		try{
			logger.debug( "THE ACCOUNT INFO IS: " + jsonString);
			if( jsonString.isEmpty()){
				return getErrorResult( null);
			}
			JSONObject account = JSONObject.parseObject( jsonString);
			boAccount.addAccount( account);
			
			return getSuccessResult( null);
		}catch( BOMsgException be ){
			logger.warn( "ADD ACCOUNT FAILED IN BO, BEACAUSE:" + be.getExceptionInfo());
			return getErrorResult( be.exceptionInfo);
		}catch( BOException be ){
			logger.warn( "ADD ACCOUNT FAILED IN BO, BEACAUSE:" + be.getExceptionInfo());
			return getErrorResult( null);
		}catch( Exception e){
			e.printStackTrace();
			logger.warn( "ADD ACCOUNT FAILED IN CONTROLLER, BEACAUSE:" + e.getCause());
			return getErrorResult( CtrlMsgConst.MSG_LOGIN_FAILED_SYSTEM);
		}
	}
	
	/**
	 * 认证邮件的认证接口
	 * @param code 认证号
	 * @return
	 */
	@RequestMapping(value="/verify/{code}",method=RequestMethod.GET)
	@ResponseBody
	public void regVerify(
					@Context HttpServletRequest request,
					@Context HttpServletResponse response,
					@PathVariable(value = "code" )  String code){
		try {
			code = Base64Utils.decode4String( code.getBytes());
			logger.debug( "THE REGISTER AUTH CODE IS: "+code );
			
			//解密
			SecretKey key = DesEncrypterUtil.getDESKey(VERIFY_KEY.getBytes());
			DesEncrypterUtil.init(key, DesEncrypterUtil.TEXT);
			String orgStr = DesEncrypterUtil.decryptText( code ) ;
			logger.debug( "THE AUTH USER IS: " + orgStr.split("\\|")[0] );
			
//			JSONObject jo = JSONObject.parseObject( orgStr.split("\\|")[0]);
			
//			boAccount.setStatus( jo.getString( "email"), CtrlSettingConst.ACCOUNT_DEFAULT_STATUS);
			
			String scheme = request.getScheme();
			String serverName = request.getServerName();
			String port = ""+request.getServerPort();
			String path = request.getContextPath();  
			if( port.equals( "80")){
				port="";
			}else{
				port=":"+port;
			}
			String basePath = scheme+"://"+
							      serverName+
							      port+
							      path+"/";  
			String redir = basePath + VERIFY_REDIR_PATH;
			response.sendRedirect( redir );
		} catch (Exception e) {
			e.printStackTrace();
			logger.warn( "REDIR VERIFY PATH FAILED, BEACAUSE: " + e.getMessage());
			//TODO
			//重定向错误页面
		}
	}

	/**
	 * 更新密码
	 * @param request
	 * @param jsonString
	 * @return
	 */
	@RequestMapping(value="/changepwd",method=RequestMethod.POST)
	@ResponseBody
	public JSONObject changepwd(  HttpServletRequest request,  @RequestBody String jsonString ){
		
		logger.debug( "THE CHANGE PASSWORD INFO IS: " + jsonString);
		if( jsonString.isEmpty()){
			return getErrorResult( null);
		}
		JSONObject o = JSONObject.parseObject( jsonString);
		String password = o.getString( "password");
		String newPassword = o.getString( "password_new");
		try{
			HttpSession session = request.getSession();
			JSONObject sJson = (JSONObject)session.getAttribute( CtrlSettingConst.HTTP_SESSION_ATTR );
			
			ActWrapper ActWrapper = JSON.toJavaObject( sJson, ActWrapper.class);
			String userName = ActWrapper.getUserName();
			if( userName == null || userName.isEmpty())
				return getErrorResult( CtrlMsgConst.MSG_SESSION_TIMEOUT);
			logger.debug( "THE ACCOUNT USERNAME IS: " + userName);
			boAccount.changePasswd( userName, password, newPassword);
			
			return getSuccessResult( null);
		}catch( BOException be ){
			logger.warn( "CHANGE PASSWORD FAILED IN BO, BEACAUSE:" + be.getExceptionInfo());
			be.printStackTrace();
			return getErrorResult( null);
		}catch( Exception e){
			e.printStackTrace();
			logger.warn( "CHANGE PASSWORD FAILED IN CONTROLLER, BEACAUSE:" + e.getCause());
			return getErrorResult( null);
		}		
	}
	
	/**
	 * 获取用户的Session信息
	 * @param request HttpRequest
	 * @param response HttpResponse
	 * @return 用户Session信息的JSON或者错误信息
	 */
	@RequestMapping(value="/session",method=RequestMethod.GET)
	@ResponseBody
	public JSONObject getSession( HttpServletRequest request,HttpServletResponse response){
		try{
			ActWrapper ActWrapper = getSession(request);
			if( ActWrapper == null){
				return getErrorResult( CtrlMsgConst.MSG_SESSION_TIMEOUT);
			}
			return getSuccessResult( JSONObject.toJSON( ActWrapper));
		}catch( Exception e){
			return getErrorResult( CtrlMsgConst.MSG_ERROR);
		}
	}
	
	/**
	 * 获取所有帐户信息的集合并转换为JSON数组对象返回
	 * @return JSON对象数组
	 */
	@RequestMapping(value="/list",method=RequestMethod.GET)
	@ResponseBody
	public JSONObject getAllAccount(){
		try{
			List<SysAccount> data = boAccount.getAllAccount();
			if( data == null) return new JSONObject();

			String jStr = JSON.toJSONString( data, true);
			JSONArray jarr = JSONArray.parseArray( jStr);

			int index = -1;
			for( int i = 0; i < jarr.size(); i++){
				if( jarr.getJSONObject(i).getString("userName").equalsIgnoreCase(ACCOUNT_DEFAULT)){
					index = i;
					break;
				}
			}
			if( index != -1 ) jarr.remove( index);
			
			return getSuccessResult( jarr);
		}catch( BOException be ){
			logger.warn( "GET ALL ACCOUNTS FAILED IN BO, BEACAUSE:" + be.getExceptionInfo());
			return new JSONObject();
		}catch( Exception e){
//			e.printStackTrace();
			logger.warn( "GET ALL ACCOUNTS FAILED IN CONTROLLER, BEACAUSE:" + e.getCause());
			return new JSONObject();
		}
	}

	@RequestMapping(value="/delete",method=RequestMethod.GET)
	@ResponseBody
	public JSONObject delAccount( 
					HttpServletRequest request, 
					@RequestParam(value="username",required=true) String userName, 
					@RequestParam(value="df",required=false) Boolean isDelFolder){
		try{
			logger.debug( "THE ACCOUNT USERNAME IS: " + userName);
			boAccount.deleteAccount( userName, isDelFolder);
			return getSuccessResult( null);
		}catch( BOException be ){
			logger.warn( "DELETE ACCOUNT FAILED IN BO, BEACAUSE:" + be.getExceptionInfo());
			return getErrorResult( null);
		}catch( Exception e){
//			e.printStackTrace();
			logger.warn( "DELETE ACCOUNT FAILED IN CONTROLLER, BEACAUSE:" + e.getCause());
			return getErrorResult( CtrlMsgConst.MSG_LOGIN_FAILED_SYSTEM);
		}		
	}


	/**
	 * 
	    * @Title: resetPwd
	    * @Description: 批量重置密码
	    * @param request
	    * @param response
	    * @param userName
	    * @return    参数
	    * @return JSONObject
	    * @throws
	 */
	@RequestMapping(value="/reset",method=RequestMethod.GET)
	@ResponseBody
	public JSONObject resetPwd(
					@Context HttpServletRequest request,
					@Context HttpServletResponse response,
					@RequestParam(value="username",required=true) String userName ){
		try{
			logger.debug( "THE ACCOUNT USERNAME IS: " + userName);
			String[] us = userName.split(",");
			for( int i = 0; i<us.length; i++){
				boAccount.resetPasswd( us[i] );
			}
			return getSuccessResult( null);
		}catch( BOException be ){
			logger.warn( "DELETE ACCOUNT FAILED IN BO, BEACAUSE:" + be.getExceptionInfo());
			return getErrorResult( null);
		}catch( Exception e){
//			e.printStackTrace();
			logger.warn( "DELETE ACCOUNT FAILED IN CONTROLLER, BEACAUSE:" + e.getCause());
			return getErrorResult( CtrlMsgConst.MSG_LOGIN_FAILED_SYSTEM);
		}
		
	}
	
	public IBoAccount getBoAccount() {
		return boAccount;
	}

	public void setBoAccount(IBoAccount boAccount) {
		this.boAccount = boAccount;
	}
}
