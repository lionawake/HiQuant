package cn.wd.sup.controller.custom;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.alibaba.fastjson.JSONObject;
import com.zxt.framework.mvc.dao.Domain;

import cn.wd.sup.bo.custom.lqSFt.IBoLqSFt;
import cn.wd.sup.dao.dto.custom.LqStrategyFactor;

@Controller
@RequestMapping("/lq/sft")
public class LqSFtCtrl extends CustomBaseController{
	private IBoLqSFt lqSFtBo;

	public IBoLqSFt getlqSFtBo() {
		return lqSFtBo;
	}

	public void setlqSFtBo(IBoLqSFt lqSFtBo) {
		this.lqSFtBo = lqSFtBo;
	}	
	
	
	/**
	 * 插入因子数据
	 * @param jsonString
	 * @return
	 */
	@RequestMapping(value = "/save",method = RequestMethod.POST)
	@ResponseBody
	public JSONObject lqSFtSave(@RequestBody String jsonString) {
		JSONObject json = JSONObject.parseObject(jsonString);
		LqStrategyFactor lqSFt = JSONObject.toJavaObject(json, LqStrategyFactor.class);
		Long factor_id = lqSFtBo.insert(lqSFt);
		if(factor_id==null) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(factor_id);
		}
	}
	
	/**
	 * 查找因子数据
	 * @param spName
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	@RequestMapping("/find")
	@ResponseBody
	public JSONObject lqSFtFind(
			@RequestParam(value="json",required=false) String jsonString,
			@RequestParam(value="pageStart",required=false) Integer pageStart,
			@RequestParam(value="pageSize",required=false) Integer pageSize) {
		JSONObject json = JSONObject.parseObject(jsonString);
		LqStrategyFactor lqSFt = JSONObject.toJavaObject(json, LqStrategyFactor.class);
		if(pageStart==null) pageStart = 0;
		if(pageSize==null) pageSize = 1;
		ArrayList<LqStrategyFactor> data = lqSFtBo.find(lqSFt, pageStart, pageSize);
		if(data.size()==0) {
			return getErrorResult(null);
		}
		Integer num = lqSFtBo.countByWhere(lqSFt);
		if(num==null) {
			return getErrorResult(null);
		}
		JSONObject result = new JSONObject();
		result.put("data",data);
		result.put("num", num);
		return getSuccessResult(result);
	}
	
	/**
	 * 根据id查找因子数据
	 * @param spName
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	@RequestMapping("/findById/{factor_id}")
	@ResponseBody
	public JSONObject lqSFtFindById(
			@PathVariable ("factor_id") Long factor_id) {
		LqStrategyFactor lqSFt = new LqStrategyFactor();
		lqSFt.setFactor_id(factor_id);
		ArrayList<LqStrategyFactor> data = lqSFtBo.find(lqSFt, 0, 1);
		if(data.size()==0) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(data.get(0));
		}
	}
	
	/**
	 * 删除
	 * @param ids
	 * @return
	 */
	@RequestMapping("/deletes")
	@ResponseBody
	public JSONObject lqSFtDelete(
			@RequestParam(value="ids",required=true) Long[] ids) {
		List<Domain> lqs = new ArrayList<Domain>();
		for(int i=0;i<ids.length;i++) {
			LqStrategyFactor lq = new LqStrategyFactor();
			lq.setFactor_id(ids[i]);
			lqs.add(lq);
		}
		Integer result = lqSFtBo.deleteByIds(lqs);
		if(result==null || result==0) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(result);
		}
	}
	
	/**
	 * 更新操作
	 * @param jsonString
	 * @return
	 */
	@RequestMapping(value = "/update",method = RequestMethod.POST)
	@ResponseBody
	public JSONObject lqSFtUpdate(@RequestBody String jsonString) {
		JSONObject json = JSONObject.parseObject(jsonString);
		LqStrategyFactor lq = JSONObject.toJavaObject(json, LqStrategyFactor.class);
		Integer result = lqSFtBo.update(lq);
		if(result==null || result==0) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(result);
		}
	}

}
