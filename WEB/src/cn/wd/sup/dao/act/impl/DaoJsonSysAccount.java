package cn.wd.sup.dao.act.impl;

import java.util.ArrayList;
import java.util.List;

import cn.wd.sup.dao.DaoJsonBase;
import cn.wd.sup.dao.act.IDaoJsonSysAccount;
import cn.wd.sup.dao.dto.SysAccount;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.zxt.framework.exception.DAOException;
import com.zxt.framework.mvc.dao.Domain;

/**
 * 
 * @author WD
 * 
 *         PulishDate: 2017年9月16日 
 *         Function: 系统管理>>帐户管理的数据操作实现类 
 *         ChangeLog:
 */
public class DaoJsonSysAccount extends DaoJsonBase implements IDaoJsonSysAccount {

	private String dbName;//数据文件名称
	/**
	 * 新增单个对象
	 * 
	 * @param o
	 *                新增对象
	 * @throws DAOException
	 */
	public void addObject(Domain account) throws DAOException {
		try{
			List<SysAccount> lst = getAll();
			JSONArray jArr = (JSONArray)JSON.toJSON( lst);
			jArr.add( account);
			writeJSON2File( jArr, dbName);
		}catch( Exception e){
			e.printStackTrace();
			throw new DAOException( e.getMessage());
		}
	}

	/**
	 * 批量添加对象
	 * 
	 * @param lst
	 *                对象集合
	 * @throws DAOException
	 */
	public void addObjects(List<Domain> accounts) throws DAOException {
		try{
			//TODO
		}catch( Exception e){
			throw new DAOException( e.getMessage());
		}
	}

	/**
	 * 获取所有的数据
	 * @return 全部对象列表
	 * @throws DAOException
	 */
	public List<SysAccount>getAll() throws DAOException{
		try {
			String jsonStr = readJSONFile( dbName);
			List<SysAccount> lst = JSONObject.parseArray( jsonStr, SysAccount.class );
			for( SysAccount sa : lst){
				logger.debug( sa.toString());
			}
			return lst;
		} catch (Exception e) {
			e.printStackTrace();
			logger.warn( "GET ALL ACCOUNTS FAILED IN BO, BEACAUSE:" + e.getCause());
			throw new DAOException(e.getMessage());
		}
	}
	/**
	 * 获取指定唯一性关键字的对象
	 * 
	 * @param userName
	 *                用户名
	 * @return 查询结果
	 * @throws DAOException
	 */
	public SysAccount getObjectByIndex(String userName) throws DAOException {
		try {
			String jsonStr = readJSONFile( dbName);
			List<SysAccount> lst = JSONObject.parseArray( jsonStr, SysAccount.class );
			for( SysAccount account : lst){
				if( account.getUserName().equals( userName)){
					return account;
				}
			}
			return null;
		} catch (Exception e) {
			throw new DAOException(e.getMessage());
		}
	}

	/**
	 * 获取指定对象属性条件的对象
	 * 
	 * @param filter
	 *                指定条件，对应一个对象实例
	 * @return 查询结果
	 * @throws DAOException
	 */
	public List<SysAccount> getObjectsByWhere( SysAccount account) throws DAOException {
		
		String userName = account.getUserName() ;
		String pwd = account.getPassword();
		
		List<SysAccount> result = new ArrayList<SysAccount>();
		try{
			List<SysAccount> results = getAll();
			for( SysAccount a : results){
				if( a.getUserName().equals( userName) &&
								a.getPassword().equals( pwd) ){
					result.add( a);
				}
			}
			return result;
		}catch( Exception e){
			throw new DAOException( e.getMessage());
		}
	}

	/**
	 * 根据参数对象，更新数据
	 * 
	 * @param object
	 *                需要更新的对象，包含对象唯一性关键字。
	 * @throws DAOException
	 */
	public void updateObject(SysAccount account) throws DAOException {
		try{
			List<SysAccount> lst = getAll();
			
			for( SysAccount a : lst){
				if( a.getUserName().equals( account.getUserName())){
					if( account.getPassword() != null)
						a.setPassword( account.getPassword());
					break;
				}
			}
			
			JSONArray jArr = (JSONArray)JSON.toJSON( lst);
			writeJSON2File( jArr, dbName);
		}catch( Exception e){
			e.printStackTrace();
			throw new DAOException( e.getMessage());
		}
	}

	/**
	 * 删除指定对象唯一关键字的数据
	 * 
	 * @param index
	 *                唯一关键字
	 * @throws DAOException
	 */
	public void deleteObjectByIndex(String userName) throws DAOException {
		try{
			List<SysAccount> lst = getAll();
			JSONArray jArr = (JSONArray)JSON.toJSON( lst);
			for( int i = 0; i < jArr.size(); i++){
				JSONObject account = jArr.getJSONObject( i);
				if( account.getString( "userName").equals( userName)){
					jArr.remove( i);
					break;
				}
			}
			writeJSON2File( jArr, dbName);
		}catch( Exception e){
			throw new DAOException( e.getMessage());
		}
	}

	/**
	 * 删除指定对象属性的数据
	 * 
	 * @param object
	 *                对象实例
	 * @throws DAOException
	 */
	public void deleteObject(Domain account) throws DAOException {

	}

	public String getDbName() {
		return dbName;
	}

	public void setDbName(String dbName) {
		this.dbName = dbName;
	}
	
	public static void main( String[] args){
		DaoJsonSysAccount opr = new DaoJsonSysAccount();
		opr.setDbName( "C:/0.D-Work/Teach/cube/trunk/src/webapp/WEB-INF/db/account.cdb");
		try{
			List<SysAccount> a = opr.getAll();
			for( SysAccount sa : a){
				System.out.println( sa.toString());
			}
		}catch(Exception e){
			e.printStackTrace();
		}
	}
}
