package cn.wd.sup.bo.custom.lqDs.impl;

import java.util.ArrayList;
import java.util.List;

import com.zxt.framework.exception.DAOException;
import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.bo.custom.lqDs.IBoLqDs;
import cn.wd.sup.dao.custom.lqDs.IDaoLqDs;
import cn.wd.sup.dao.dto.custom.LqDataSource;

public class LqDsBoImpl implements IBoLqDs{
	private IDaoLqDs lqDsDao;

	public IDaoLqDs getlqDsDao() {
		return lqDsDao;
	}

	public void setlqDsDao(IDaoLqDs lqDsDao) {
		this.lqDsDao = lqDsDao;
	}

	/**
	 * 插入信息
	 */
	public Long insert(Domain o) {
		try {
			Long spId = (Long)lqDsDao.insert(o);
			return spId;
		} catch (DAOException e) {
			return null;
		}
	}
	
	/**
	 * 重写分页查找
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	@SuppressWarnings("unchecked")
	public ArrayList<LqDataSource> find(Domain o,Integer pageStart , Integer pageSize){
		Object s = lqDsDao.find(o, pageStart, pageSize);
		return ( ArrayList<LqDataSource>)s;
	}
	
	/**
	 * 查找全部
	 * @return
	 */
	@SuppressWarnings("unchecked")
	public ArrayList<LqDataSource> findAll(){
		try {
			Object s = lqDsDao.findAll();
			return ( ArrayList<LqDataSource>)s;
		} catch (DAOException e) {
			e.printStackTrace();
			return null;
		}
		
	}
	
	/**
	 * 查找总数
	 * @param o
	 * @return
	 */
	public Integer countByWhere(Domain o){
		try {
			Integer num = lqDsDao.countByWhere(o);
			return num;
		} catch (DAOException e) {
			e.printStackTrace();
			return null;
		}
	}
	
	/**
	 * 删除多个id
	 * @param os
	 * @return
	 */
	public Integer deleteByIds(List<Domain> os) {
		try {
			return lqDsDao.deleteByIDs(os);
		} catch (DAOException e) {
			return null;
		}
	}
	
	/**
	 * 更新操作
	 * @param o
	 * @return
	 */
	public Integer update(Domain o) {
		try {
			return lqDsDao.update(o);
		} catch (DAOException e) {
			return null;
		}
	}
	
}
