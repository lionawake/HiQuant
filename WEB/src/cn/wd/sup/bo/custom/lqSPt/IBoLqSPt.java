package cn.wd.sup.bo.custom.lqSPt;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.bo.custom.IBoLqBase;
import cn.wd.sup.dao.dto.custom.LqStrategyPattern;

public interface IBoLqSPt extends IBoLqBase{
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
	public ArrayList<LqStrategyPattern> find(Domain o,Integer pageStart , Integer pageSize);
	
	/**
	 * 查找总数
	 * @param o
	 * @return
	 */
	public Integer countByWhere(Domain o);
	
	/**
	 * 删除多个id
	 * @param os
	 * @return
	 */
	public Integer deleteByIds(List<Domain> os);
	
	/**
	 * 更新操作
	 * @param o
	 * @return
	 */
	public Integer update(Domain o);
	
	/**
	 * 查找模板任务状态
	 * @return
	 */
	@SuppressWarnings("rawtypes")
	public HashMap findStatus();
}