package cn.wd.sup.dao;

import java.util.List;

import com.zxt.framework.exception.DAOException;
import com.zxt.framework.mvc.dao.Domain;

/**
 * 
 * @author WD
 *
 * PulishDate: 2017年9月16日
 * Function: 文件数据存储的基础操作接口 
 * ChangeLog:
 */
public interface IDaoJsonBase {

	/**
	 * 新增单个对象
	 * @param o 新增对象
	 * @throws DAOException
	 */
	public void addObject( Domain o) throws DAOException;
	
	/**
	 * 批量添加对象
	 * @param lst 对象集合
	 * @throws DAOException
	 */
	public void addObjects( List<Domain> lst) throws DAOException;
	
	/**
	 * 获取指定唯一性关键字的对象
	 * @param index 唯一性关键字
	 * @return  查询结果
	 * @throws DAOException
	 */
	public Domain getObjectByIndex( String index) throws DAOException;
	
	/**
	 * 获取指定条件的对象
	 * @param filter 指定条件
	 * @return 查询结果
	 * @throws DAOException
	 */
//	public Domain getObjectsByWhere( Map<Object, Object> filter) throws DAOException;
	
	/**
	 * 根据参数对象，更新数据
	 * @param object 需要更新的对象，包含对象唯一性关键字。
	 * @throws DAOException
	 */
//	public void updateObject( Domain o) throws DAOException;
	
	/**
	 * 删除指定对象唯一关键字的数据
	 * @param index  唯一关键字
	 * @throws DAOException
	 */
	public void deleteObjectByIndex( String index) throws DAOException;
	
	/**
	 * 删除指定对象属性的数据
	 * @param object 对象实例
	 * @throws DAOException
	 */
	public void deleteObject( Domain object) throws DAOException;
}
