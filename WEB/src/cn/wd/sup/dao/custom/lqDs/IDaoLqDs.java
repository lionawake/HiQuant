package cn.wd.sup.dao.custom.lqDs;


import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.dao.custom.IDaoLqBase;

public interface IDaoLqDs extends IDaoLqBase{
	/**
	 * 重写分页查找
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	public Object find(Domain o,Integer pageStart , Integer pageSize);
	
}
