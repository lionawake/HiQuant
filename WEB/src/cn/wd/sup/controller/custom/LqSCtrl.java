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

import cn.wd.sup.bo.custom.lqS.IBoLqS;
import cn.wd.sup.dao.dto.custom.LqStrategy;

@Controller
@RequestMapping("/lq/s")
public class LqSCtrl extends CustomBaseController{
	private IBoLqS lqSBo;

	public IBoLqS getlqSBo() {
		return lqSBo;
	}

	public void setlqSBo(IBoLqS lqSBo) {
		this.lqSBo = lqSBo;
	}	
	
	
	/**
	 * 插入模板数据
	 * @param jsonString
	 * @return
	 */
	@RequestMapping(value = "/save",method = RequestMethod.POST)
	@ResponseBody
	public JSONObject lqSPtSave(@RequestBody String jsonString) {
		JSONObject json = JSONObject.parseObject(jsonString);
		LqStrategy lq = JSONObject.toJavaObject(json, LqStrategy.class);
		Long spId = lqSBo.insert(lq);
		if(spId==null) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(spId);
		}
	}
	
	/**
	 * 查找策略数据
	 * @param spName
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	@RequestMapping("/find")
	@ResponseBody
	public JSONObject lqSFind(
			@RequestParam(value="json",required=false) String jsonString,
			@RequestParam(value="pageStart",required=false) Integer pageStart,
			@RequestParam(value="pageSize",required=false) Integer pageSize,
			@RequestParam(value="sortStr",required=false) String sortStr) {
		if(sortStr==null) sortStr = "s_id asc";
		JSONObject json = JSONObject.parseObject(jsonString);
		json.put("sortStr", sortStr);
		LqStrategy lq = JSONObject.toJavaObject(json, LqStrategy.class);
		if(pageStart==null) pageStart = 0;
		if(pageSize==null) pageSize = 1;
		ArrayList<LqStrategy> data = lqSBo.find(lq, pageStart, pageSize);
		if(data.size()==0) {
			return getErrorResult(null);
		}
		Integer num = lqSBo.countByWhere(lq);
		if(num==null) {
			return getErrorResult(null);
		}
		JSONObject result = new JSONObject();
		result.put("data",data);
		result.put("num", num);
		return getSuccessResult(result);
	}
	
	/**
	 * 根据id查找策略数据
	 * @param spName
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	@RequestMapping("/findById/{sId}")
	@ResponseBody
	public JSONObject lqSFindById(
			@PathVariable ("sId") Long sId) {
		LqStrategy lq = new LqStrategy();
		lq.setsId(sId);
		ArrayList<LqStrategy> data = lqSBo.find(lq, 0, 1);
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
	public JSONObject lqSPtDelete(
			@RequestParam(value="ids",required=true) Long[] ids) {
		List<Domain> lqs = new ArrayList<Domain>();
		for(int i=0;i<ids.length;i++) {
			LqStrategy lq = new LqStrategy();
			lq.setSpId(ids[i]);
			lqs.add(lq);
		}
		Integer result = lqSBo.deleteByIds(lqs);
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
	public JSONObject lqSPtUpdate(@RequestBody String jsonString) {
		JSONObject json = JSONObject.parseObject(jsonString);
		LqStrategy lq = JSONObject.toJavaObject(json, LqStrategy.class);
		Integer result = lqSBo.update(lq);
		if(result==null || result==0) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(result);
		}
	}
}
