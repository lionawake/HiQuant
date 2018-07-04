package cn.wd.sup.dao.custom.lqSPt;

import java.util.HashMap;

import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.dao.custom.IDaoLqBase;

public interface IDaoLqSPt extends IDaoLqBase{
	/**
	 * 重写分页查找
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	public Object find(Domain o,Integer pageStart , Integer pageSize);
	
	/**
	 * 查找模板状态
	 * @return
	 */
	@SuppressWarnings("rawtypes")
	public HashMap findStatus();
}
