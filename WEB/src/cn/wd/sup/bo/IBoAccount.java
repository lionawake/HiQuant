package cn.wd.sup.bo;

import java.util.List;

import cn.wd.sup.dao.dto.SysAccount;

import com.alibaba.fastjson.JSONObject;
import com.zxt.framework.exception.BOException;
import com.zxt.framework.exception.BOMsgException;
import com.zxt.framework.mvc.bo.BaseBO;

/**
 * 
 * @author WD
 *
 * PulishDate: 2017年9月17日
 * Function: 系统配置>>帐户管理业务逻辑接口 
 * ChangeLog:
 */
public interface IBoAccount extends BaseBO{

	/**
	 * 帐户登录业务逻辑
	 * @param userName 用户名
	 * @param passwd  密码,MD5的hash
	 * @throws BOException
	 */
	public SysAccount login( String userName, String passwd) throws BOException;
	
	/**
	 * 获取所有的帐户数据对象
	 * @return 帐户数据集合
	 * @throws BOException
	 */
	public List<SysAccount> getAllAccount() throws BOException;
	
	/**
	 * 添加新的账号
	 * @param account 账号信息
	 * @throws BOException 
	 */
	public void addAccount( JSONObject account) throws BOException,BOMsgException;
	
	/**
	 * 删除账号
	 * @param account 账号信息
	 * @param isDelFolder 是否删除空间目录
	 * @throws BOException
	 */
	public void deleteAccount( String userName, Boolean isDelFolder) throws BOException;

	/**
	 * 帐户更新密码
	 * @param userName 帐户名
	 * @param passwd  原密码
	 * @param newPasswd  新密码
	 * @throws BOException
	 */
	public void changePasswd( String userName, String passwd, String newPasswd) throws BOException;

	/**
	 * 
	    * @Title: resetPasswd
	    * @Description: 重置密码
	    * @param userName
	    * @throws BOException    参数
	    * @return void
	    * @throws
	 */
	public void resetPasswd( String userName ) throws BOException;
}
