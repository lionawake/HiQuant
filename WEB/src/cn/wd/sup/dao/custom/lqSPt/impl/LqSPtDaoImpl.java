package cn.wd.sup.dao.custom.lqSPt.impl;

import java.util.HashMap;

import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.dao.DaoBaseImpl;
import cn.wd.sup.dao.custom.lqSPt.IDaoLqSPt;

public class LqSPtDaoImpl extends DaoBaseImpl implements IDaoLqSPt{
	
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
	
	/**
	 * 查找模板状态
	 * @return
	 */
	@SuppressWarnings("rawtypes")
	public HashMap findStatus() {
		Object map = this.slaveSqlMapClientTemplate.queryForObject(modelName+".findStatus");
		return (HashMap)map;
	}
}
