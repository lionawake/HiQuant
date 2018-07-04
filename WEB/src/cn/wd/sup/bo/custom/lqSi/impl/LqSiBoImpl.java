package cn.wd.sup.bo.custom.lqSi.impl;

import java.util.ArrayList;
import java.util.List;

import com.zxt.framework.exception.DAOException;
import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.bo.custom.lqSi.IBoLqSi;
import cn.wd.sup.dao.custom.lqSi.IDaoLqSi;
import cn.wd.sup.dao.dto.custom.LqStrategyInterface;

public class LqSiBoImpl implements IBoLqSi{
	private IDaoLqSi lqSiDao;

	public IDaoLqSi getlqSiDao() {
		return lqSiDao;
	}

	public void setlqSiDao(IDaoLqSi lqSiDao) {
		this.lqSiDao = lqSiDao;
	}

	/**
	 * 插入信息
	 */
	public Long insert(Domain o) {
		try {
			Long spId = (Long)lqSiDao.insert(o);
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
	public ArrayList<LqStrategyInterface> find(Domain o,Integer pageStart , Integer pageSize){
		Object s = lqSiDao.find(o, pageStart, pageSize);
		return ( ArrayList<LqStrategyInterface>)s;
	}
	
	/**
	 * 查找全部
	 * @return
	 */
	@SuppressWarnings("unchecked")
	public ArrayList<LqStrategyInterface> findAll(){
		try {
			Object s = lqSiDao.findAll();
			return ( ArrayList<LqStrategyInterface>)s;
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
			Integer num = lqSiDao.countByWhere(o);
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
			return lqSiDao.deleteByIDs(os);
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
			return lqSiDao.update(o);
		} catch (DAOException e) {
			return null;
		}
	}
	
}
