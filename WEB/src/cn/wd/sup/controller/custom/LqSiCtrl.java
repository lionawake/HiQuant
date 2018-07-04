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

import cn.wd.sup.bo.custom.lqSi.IBoLqSi;
import cn.wd.sup.dao.dto.custom.LqStrategyInterface;

@Controller
@RequestMapping("/lq/si")
public class LqSiCtrl extends CustomBaseController{
	private IBoLqSi lqSiBo;

	public IBoLqSi getlqSiBo() {
		return lqSiBo;
	}

	public void setlqSiBo(IBoLqSi lqSiBo) {
		this.lqSiBo = lqSiBo;
	}	
	
	
	/**
	 * 插入数据来源数据
	 * @param jsonString
	 * @return
	 */
	@RequestMapping(value = "/save",method = RequestMethod.POST)
	@ResponseBody
	public JSONObject lqDsSave(@RequestBody String jsonString) {
		JSONObject json = JSONObject.parseObject(jsonString);
		LqStrategyInterface lqDs = JSONObject.toJavaObject(json, LqStrategyInterface.class);
		Long Si_id = lqSiBo.insert(lqDs);
		if(Si_id==null) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(Si_id);
		}
	}
	
	/**
	 * 查找数据来源数据
	 * @param spName
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	@RequestMapping("/find")
	@ResponseBody
	public JSONObject lqDsFind(
			@RequestParam(value="json",required=false) String jsonString,
			@RequestParam(value="pageStart",required=false) Integer pageStart,
			@RequestParam(value="pageSize",required=false) Integer pageSize) {
		JSONObject json = JSONObject.parseObject(jsonString);
		LqStrategyInterface lqDs = JSONObject.toJavaObject(json, LqStrategyInterface.class);
		if(pageStart==null) pageStart = 0;
		if(pageSize==null) pageSize = 1;
		ArrayList<LqStrategyInterface> data = lqSiBo.find(lqDs, pageStart, pageSize);
		if(data.size()==0) {
			return getErrorResult(null);
		}
		Integer num = lqSiBo.countByWhere(lqDs);
		if(num==null) {
			return getErrorResult(null);
		}
		JSONObject result = new JSONObject();
		result.put("data",data);
		result.put("num", num);
		return getSuccessResult(result);
	}
	
	/**
	 * 根据id查找数据来源
	 * @param spName
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	@RequestMapping("/findById/{Si_id}")
	@ResponseBody
	public JSONObject lqDsFindById(
			@PathVariable ("Si_id") Long Si_id) {
		LqStrategyInterface lqDs = new LqStrategyInterface();
		lqDs.setSi_id(Si_id);
		ArrayList<LqStrategyInterface> data = lqSiBo.find(lqDs, 0, 1);
		if(data.size()==0) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(data.get(0));
		}
	}
	
	/**
	 * 查找全部数据
	 * @return
	 */
	@RequestMapping("/findAll")
	@ResponseBody
	public JSONObject lqDsFindAll() {
		ArrayList<LqStrategyInterface> data = lqSiBo.findAll();
		if(data.size()==0) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(data);
		} 
	}
	
	/**
	 * 删除
	 * @param ids
	 * @return
	 */
	@RequestMapping("/deletes")
	@ResponseBody
	public JSONObject lqDsDelete(
			@RequestParam(value="ids",required=true) Long[] ids) {
		List<Domain> lqs = new ArrayList<Domain>();
		for(int i=0;i<ids.length;i++) {
			LqStrategyInterface lq = new LqStrategyInterface();
			lq.setSi_id(ids[i]);
			lqs.add(lq);
		}
		Integer result = lqSiBo.deleteByIds(lqs);
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
	public JSONObject lqDsUpdate(@RequestBody String jsonString) {
		JSONObject json = JSONObject.parseObject(jsonString);
		LqStrategyInterface lq = JSONObject.toJavaObject(json, LqStrategyInterface.class);
		Integer result = lqSiBo.update(lq);
		if(result==null || result==0) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(result);
		}
	}

}
