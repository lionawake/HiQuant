package cn.wd.sup.bo.custom.lqSFt.impl;

import java.util.ArrayList;
import java.util.List;

import com.zxt.framework.exception.DAOException;
import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.bo.custom.lqSFt.IBoLqSFt;
import cn.wd.sup.dao.custom.lqSFt.IDaoLqSFt;
import cn.wd.sup.dao.dto.custom.LqStrategyFactor;

public class LqSFtBoImpl implements IBoLqSFt{
	private IDaoLqSFt lqSFtDao;

	public IDaoLqSFt getLqSFtDao() {
		return lqSFtDao;
	}

	public void setLqSFtDao(IDaoLqSFt lqSFtDao) {
		this.lqSFtDao = lqSFtDao;
	}

	/**
	 * 插入信息
	 */
	public Long insert(Domain o) {
		try {
			System.out.println(o);
			Long factor_id = (Long)lqSFtDao.insert(o);
			return factor_id;
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
	public ArrayList<LqStrategyFactor> find(Domain o,Integer pageStart , Integer pageSize){
		Object s = lqSFtDao.find(o, pageStart, pageSize);
		return ( ArrayList<LqStrategyFactor>)s;
	}
	
	/**
	 * 查找总数
	 * @param o
	 * @return
	 */
	public Integer countByWhere(Domain o){
		try {
			Integer num = lqSFtDao.countByWhere(o);
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
			System.out.println(os);
			return lqSFtDao.deleteByIDs(os);
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
			return lqSFtDao.update(o);
		} catch (DAOException e) {
			return null;
		}
	}
	
}
