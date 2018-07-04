package cn.wd.sup.bo.custom.lqDs;

import java.util.ArrayList;
import java.util.List;

import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.bo.custom.IBoLqBase;
import cn.wd.sup.dao.dto.custom.LqDataSource;

public interface IBoLqDs extends IBoLqBase{
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
	public ArrayList<LqDataSource> find(Domain o,Integer pageStart , Integer pageSize);
	
	/**
	 * 查找全部
	 * @return
	 */
	public ArrayList<LqDataSource> findAll();
	
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
	
}
