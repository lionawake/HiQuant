package cn.wd.sup.dao.custom.lqSFt.impl;

import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.dao.DaoBaseImpl;
import cn.wd.sup.dao.custom.lqSFt.IDaoLqSFt;

public class LqSFtDaoImpl extends DaoBaseImpl implements IDaoLqSFt{
	
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
