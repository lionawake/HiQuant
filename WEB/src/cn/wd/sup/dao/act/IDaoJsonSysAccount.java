package cn.wd.sup.dao.act;

import java.util.List;

import cn.wd.sup.dao.IDaoJsonBase;
import cn.wd.sup.dao.dto.SysAccount;

import com.zxt.framework.exception.DAOException;


/**
 * 
 * @author WD
 *
 * PulishDate: 2017年9月16日
 * Function:  系统管理>>帐户管理的数据操作接口
 * ChangeLog:
 */
public interface IDaoJsonSysAccount  extends IDaoJsonBase{
	
	/**
	 * 获取所有的数据
	 * @return 全部对象列表
	 * @throws DAOException
	 */
	public List<SysAccount>getAll() throws DAOException;
	
	/**
	 * 获取指定对象属性条件的对象
	 * @param filter 指定条件，对应一个对象实例
	 * @return 查询结果
	 * @throws DAOException
	 */
	public List<SysAccount> getObjectsByWhere( SysAccount filter ) throws DAOException;
	
	/**
	 * 根据参数对象，更新数据
	 * @param object 需要更新的对象，包含对象唯一性关键字。
	 * @throws DAOException
	 */
	public void updateObject( SysAccount o) throws DAOException;
	
}
