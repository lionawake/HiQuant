package cn.wd.sup.bo.custom.lqS.impl;

import java.util.ArrayList;
import java.util.List;

import com.zxt.framework.exception.DAOException;
import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.bo.custom.lqS.IBoLqS;
import cn.wd.sup.dao.custom.lqS.IDaoLqS;
import cn.wd.sup.dao.dto.custom.LqStrategy;

public class LqSBoImpl implements IBoLqS{
	private IDaoLqS lqSDao;
	
	
	public IDaoLqS getLqSDao() {
		return lqSDao;
	}

	public void setLqSDao(IDaoLqS lqSDao) {
		this.lqSDao = lqSDao;
	}

	/**
	 * 插入信息
	 */
	public Long insert(Domain o) {
		try {
			Long spId = (Long)lqSDao.insert(o);
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
	public ArrayList<LqStrategy> find(Domain o,Integer pageStart , Integer pageSize){
		Object s = lqSDao.find(o, pageStart, pageSize);
		return ( ArrayList<LqStrategy>)s;
	}
	
	/**
	 * 删除多个id
	 * @param os
	 * @return
	 */
	public Integer deleteByIds(List<Domain> os) {
		try {
			return lqSDao.deleteByIDs(os);
		} catch (DAOException e) {
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
			Integer num = lqSDao.countByWhere(o);
			return num;
		} catch (DAOException e) {
			e.printStackTrace();
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
			return lqSDao.update(o);
		} catch (DAOException e) {
			return null;
		}
	}
	
}
