package cn.wd.sup.dao.custom.lqS;

import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.dao.custom.IDaoLqBase;

public interface IDaoLqS extends IDaoLqBase{
	/**
	 * 重写分页查找
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	public Object find(Domain o,Integer pageStart , Integer pageSize);
}
