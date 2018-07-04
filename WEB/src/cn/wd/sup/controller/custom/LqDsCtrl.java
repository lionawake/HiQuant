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

import cn.wd.sup.bo.custom.lqDs.IBoLqDs;
import cn.wd.sup.dao.dto.custom.LqDataSource;

@Controller
@RequestMapping("/lq/ds")
public class LqDsCtrl extends CustomBaseController{
	private IBoLqDs lqDsBo;

	public IBoLqDs getlqDsBo() {
		return lqDsBo;
	}

	public void setlqDsBo(IBoLqDs lqDsBo) {
		this.lqDsBo = lqDsBo;
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
		LqDataSource lqDs = JSONObject.toJavaObject(json, LqDataSource.class);
		Long ds_id = lqDsBo.insert(lqDs);
		if(ds_id==null) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(ds_id);
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
		LqDataSource lqDs = JSONObject.toJavaObject(json, LqDataSource.class);
		if(pageStart==null) pageStart = 0;
		if(pageSize==null) pageSize = 1;
		ArrayList<LqDataSource> data = lqDsBo.find(lqDs, pageStart, pageSize);
		if(data.size()==0) {
			return getErrorResult(null);
		}
		Integer num = lqDsBo.countByWhere(lqDs);
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
	@RequestMapping("/findById/{ds_id}")
	@ResponseBody
	public JSONObject lqDsFindById(
			@PathVariable ("ds_id") Long ds_id) {
		LqDataSource lqDs = new LqDataSource();
		lqDs.setDs_id(ds_id);
		ArrayList<LqDataSource> data = lqDsBo.find(lqDs, 0, 1);
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
		ArrayList<LqDataSource> data = lqDsBo.findAll();
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
			LqDataSource lq = new LqDataSource();
			lq.setDs_id(ids[i]);
			lqs.add(lq);
		}
		Integer result = lqDsBo.deleteByIds(lqs);
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
		LqDataSource lq = JSONObject.toJavaObject(json, LqDataSource.class);
		Integer result = lqDsBo.update(lq);
		if(result==null || result==0) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(result);
		}
	}

}
