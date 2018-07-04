package cn.wd.sup.dao.custom.lqS.impl;

import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.dao.DaoBaseImpl;
import cn.wd.sup.dao.custom.lqS.IDaoLqS;

public class LqSDaoImpl extends DaoBaseImpl implements IDaoLqS{
	
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
