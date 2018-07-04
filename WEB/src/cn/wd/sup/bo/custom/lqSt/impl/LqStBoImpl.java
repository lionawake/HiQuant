package cn.wd.sup.bo.custom.lqSt.impl;

import java.util.ArrayList;
import java.util.List;

import com.zxt.framework.exception.DAOException;
import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.bo.custom.lqSt.IBoLqSt;
import cn.wd.sup.dao.custom.lqSt.IDaoLqSt;
import cn.wd.sup.dao.dto.custom.LqStrategyTest;

public class LqStBoImpl implements IBoLqSt{
	private IDaoLqSt lqStDao;

	
	public IDaoLqSt getLqStDao() {
		return lqStDao;
	}

	public void setLqStDao(IDaoLqSt lqStDao) {
		this.lqStDao = lqStDao;
	}

	/**
	 * 插入信息
	 */
	public Long insert(Domain o) {
		try {
			Long tId = (Long)lqStDao.insert(o);
			return tId;
		} catch (DAOException e) {
			e.printStackTrace();
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
	public ArrayList<LqStrategyTest> find(Domain o,Integer pageStart , Integer pageSize){
		Object s = lqStDao.find(o, pageStart, pageSize);
		return ( ArrayList<LqStrategyTest>)s;
	}
	
	/**
	 * 删除多个id
	 * @param os
	 * @return
	 */
	public Integer deleteByIds(List<Domain> os) {
		try {
			return lqStDao.deleteByIDs(os);
		} catch (DAOException e) {
			return null;
		}
	}
}
