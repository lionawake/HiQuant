package cn.wd.sup.dao.custom.lqSt.impl;

import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.dao.DaoBaseImpl;
import cn.wd.sup.dao.custom.lqSt.IDaoLqSt;

public class LqStDaoImpl extends DaoBaseImpl implements IDaoLqSt{
	
	/**
	 * 重写分页查找
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	public Object find(Domain o,Integer pageStart , Integer pageSize){
		Object s = this.slaveSqlMapClientTemplate.queryForList(modelName+".find", o ,pageStart , pageSize);
		return s;
	}
}
