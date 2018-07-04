package cn.wd.sup.bo.custom.lqSt;

import java.util.ArrayList;
import java.util.List;

import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.bo.custom.IBoLqBase;
import cn.wd.sup.dao.dto.custom.LqStrategyTest;

public interface IBoLqSt extends IBoLqBase{
	/**
	 * 插入信息
	 */
	public Long insert(Domain o);
	
	/**
	 * 重写分页查找
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	public ArrayList<LqStrategyTest> find(Domain o,Integer pageStart , Integer pageSize);
	
	/**
	 * 删除多个id
	 * @param os
	 * @return
	 */
	public Integer deleteByIds(List<Domain> os);
}
