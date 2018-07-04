package cn.wd.sup.bo.impl;

import java.util.List;

import cn.wd.sup.bo.IBoAccount;
import cn.wd.sup.constant.BoConst;
import cn.wd.sup.dao.act.IDaoJsonSysAccount;
import cn.wd.sup.dao.dto.SysAccount;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.zxt.framework.exception.BOException;
import com.zxt.framework.exception.BOMsgException;
import com.zxt.framework.exception.DAOException;
import com.zxt.framework.mvc.bo.BaseBOImpl;
import com.zxt.framework.utils.code.MD5;

/**
 * 
 * @author WD
 *
 * PulishDate: 2017年9月5日
 * Function: 系统配置>>帐户信息管理的业务实现 
 * ChangeLog:
 */
public class BoAccount extends BaseBOImpl implements IBoAccount{

	private IDaoJsonSysAccount daoAccount;
	
//	private static final int ACT_STATUS_DEFALT = 0;
	
	@Override
	public SysAccount  login(String userName, String passwd) throws BOException {
		try{
			SysAccount account = (SysAccount)daoAccount.getObjectByIndex( userName);
			//逻辑判断
			if( account == null ){
				logger.debug( "[LOGIN] THE ACCOUNT IS NULL");
				throw new BOException("[LOGIN] THE ACCOUNT IS NULL");
			}else{
				String pwd = account.getPassword();
				if( passwd.trim().equals( pwd.trim())){
					logger.info( "[LOGIN] LOGIN SUCCESS");
				}else{
					logger.debug( "[LOGIN] THE ACCOUNT'S PWD IS WRONG");
					throw new BOException("[LOGIN] THE ACCOUNT'S PWD IS WRONG");
				}
			}
			return account;
		}catch( DAOException de){
			logger.warn( "[LOGIN]LOGIN FAILED IN DAO, BEACAUSE:" + de.getExceptionInfo());
			throw new BOException( de.getExceptionInfo());
		}
	}

	@Override
	public List<SysAccount> getAllAccount() throws BOException {
		try{
			List<SysAccount> result = daoAccount.getAll();
			if( result == null) throw new BOException("THE ACCOUNT DATA IS NULL.");
			return result;
		}catch( DAOException de){
			logger.warn( "GET ALL ACCOUNTS FAILED IN DAO, BEACAUSE:" + de.getExceptionInfo());
			throw new BOException( de.getExceptionInfo());
		}
	}

	@Override
	public void addAccount( JSONObject account) throws BOException, BOMsgException {
		
		SysAccount o = JSON.toJavaObject( account, SysAccount.class);
		String userName = o.getUserName();
		
		try{
			//查找同名用户名的存在性
			if( userName == null || userName.trim().length() <= 0){
				logger.debug( "[SYSTEM][ACCOUNT]THE ACCOUNT'S USERNAME IS NULL" );
				throw new DAOException("THE ACCOUNT'S USERNAME IS NULL");
			}
			//用户名限制32位
			if( userName.length() > BoConst.SYS_ACCOUNT_PWD_DEFAULT_LENGTH ){
				logger.debug( "[SYSTEM][ACCOUNT]THE ACCOUNT'S USERNAME IS longer(32)" );
				throw new BOMsgException( "用户名不能超过32个字符.");
			}
			if( o.getRole() == null || o.getRole().intValue() < 0){
				logger.debug( "[SYSTEM][ACCOUNT]THE ACCOUNT'S ROLE IS VALIABLE" );
				throw new BOMsgException("角色不对,又捣蛋.");
			}
			//found the account exsit.
			List<SysAccount> lst = getAllAccount();
			for( SysAccount a : lst){
				if( a.getUserName().equals( account.get( "userName"))){
					throw new BOMsgException( "账户已经存在，请重试.");
				}
			}
			//set account's default password.
			o.setPassword( MD5.MD5Encode( BoConst.SYS_ACCOUNT_PWD_DEFAULT));
			
			daoAccount.addObject( o);
		}catch( Exception de){
			de.printStackTrace();
			logger.warn( "GET ALL ACCOUNTS FAILED IN DAO, BEACAUSE:" + de.getMessage());
			throw new BOException( de.getMessage());
		}
	}

	@Override
	public void deleteAccount( String userName, Boolean isDelFolder) throws BOException {
		try{
			daoAccount.deleteObjectByIndex( userName);
		}catch( Exception de){
			logger.warn( "DELETE ACCOUNT FAILED IN DAO, BEACAUSE:" + de.getMessage());
			throw new BOException( de.getMessage());
		}
	}

	/**
	 * 帐户更新密码
	 * @param userName 帐户名
	 * @param passwd  原密码
	 * @param newPasswd  新密码
	 * @throws BOException
	 */
	public void changePasswd( String userName, String passwd, String newPasswd) throws BOException{
		
		SysAccount account = new SysAccount();
		account.setUserName( userName);
		try{
			account.setPassword( MD5.MD5Encode(passwd) );
			List<SysAccount> _account = daoAccount.getObjectsByWhere( account);
			
			if( _account == null || _account.isEmpty()){
				throw new BOException("CHANGE PASSWORD FAILED IN DAO, BEACAUSE: THE PASSWORD IS ERROR.");
			}

			account.setPassword( MD5.MD5Encode( newPasswd) );
			daoAccount.updateObject( account);
		}catch(DAOException de){
			de.printStackTrace();
			logger.warn( "CHANGE PASSWORD FAILED IN DAO, BEACAUSE:" + de.getExceptionInfo());
			throw new BOException( de.getExceptionInfo());
		}
	}

	/**
	 * 
	    * @Title: resetPasswd
	    * @Description: 重置密码
	    * @param userName
	    * @throws BOException    参数
	    * @return void
	    * @throws
	 */
	public void resetPasswd( String userName ) throws BOException{
		
		SysAccount account = new SysAccount();
		account.setUserName( userName);
		try{
			List<SysAccount> _account = daoAccount.getObjectsByWhere( account);
			
			if( _account == null || _account.isEmpty()){
				throw new BOException("CHANGE PASSWORD FAILED IN DAO, BEACAUSE: THE PASSWORD IS ERROR.");
			}

			account.setPassword( MD5.MD5Encode( BoConst.SYS_ACCOUNT_PWD_DEFAULT) );
			daoAccount.updateObject( account);
		}catch(DAOException de){
			de.printStackTrace();
			logger.warn( "CHANGE PASSWORD FAILED IN DAO, BEACAUSE:" + de.getExceptionInfo());
			throw new BOException( de.getExceptionInfo());
		}
	}
	public IDaoJsonSysAccount getDaoAccount() {
		return daoAccount;
	}

	public void setDaoAccount(IDaoJsonSysAccount daoAccount) {
		this.daoAccount = daoAccount;
	}
}
