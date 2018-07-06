package cn.wd.sup.bo.custom.lqSPt.impl;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import com.zxt.framework.exception.DAOException;
import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.bo.custom.lqSPt.IBoLqSPt;
import cn.wd.sup.dao.custom.lqSPt.IDaoLqSPt;
import cn.wd.sup.dao.dto.custom.LqStrategyPattern;

public class LqSPtBoImpl implements IBoLqSPt{
	private IDaoLqSPt lqSPtDao;

	public IDaoLqSPt getLqSPtDao() {
		return lqSPtDao;
	}

	public void setLqSPtDao(IDaoLqSPt lqSPtDao) {
		this.lqSPtDao = lqSPtDao;
	}

	/**
	 * 插入信息
	 */
	public Long insert(Domain o) {
		try {
			Long spId = (Long)lqSPtDao.insert(o);
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
	public ArrayList<LqStrategyPattern> find(Domain o,Integer pageStart , Integer pageSize){
		Object s = lqSPtDao.find(o, pageStart, pageSize);
		return ( ArrayList<LqStrategyPattern>)s;
	}
	
	/**
	 * 查找总数
	 * @param o
	 * @return
	 */
	public Integer countByWhere(Domain o){
		try {
			Integer num = lqSPtDao.countByWhere(o);
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
			return lqSPtDao.deleteByIDs(os);
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
			return lqSPtDao.update(o);
		} catch (DAOException e) {
			return null;
		}
	}
	
	/**
	 * 查找模板任务状态
	 * @return
	 */
	@SuppressWarnings("rawtypes")
	public HashMap findStatus() {
		return lqSPtDao.findStatus();
	}
	
}