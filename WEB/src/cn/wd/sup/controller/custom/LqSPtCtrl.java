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
import cn.wd.sup.bo.custom.lqSPt.IBoLqSPt;
import cn.wd.sup.bo.custom.lqSt.IBoLqSt;
import cn.wd.sup.dao.dto.custom.LqStrategy;
import cn.wd.sup.dao.dto.custom.LqStrategyPattern;
import cn.wd.sup.dao.dto.custom.LqStrategyTest;

@Controller
@RequestMapping("/lq/spt")
public class LqSPtCtrl extends CustomBaseController{
	private IBoLqSPt lqSPtBo;
	
	private IBoLqS lqSBo;
	
	private IBoLqSt lqStBo;
	
	public IBoLqSPt getLqSPtBo() {
		return lqSPtBo;
	}

	public void setLqSPtBo(IBoLqSPt lqSPtBo) {
		this.lqSPtBo = lqSPtBo;
	}

	public IBoLqS getLqSBo() {
		return lqSBo;
	}

	public void setLqSBo(IBoLqS lqSBo) {
		this.lqSBo = lqSBo;
	}

	public IBoLqSt getLqStBo() {
		return lqStBo;
	}

	public void setLqStBo(IBoLqSt lqStBo) {
		this.lqStBo = lqStBo;
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
		LqStrategyPattern lqSPt = JSONObject.toJavaObject(json, LqStrategyPattern.class);
		if(lqSPt.getTestStatus()==null) lqSPt.setTestStatus(0);
		if(lqSPt.getTaskTotal()==null) lqSPt.setTaskTotal(0l);
		if(lqSPt.getTaskFinished()==null) lqSPt.setTaskFinished(0l);
		Long spId = lqSPtBo.insert(lqSPt);
		if(spId==null) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(spId);
		}
	}
	
	/**
	 * 查找模板数据
	 * @param spName
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	@RequestMapping("/find")
	@ResponseBody
	public JSONObject lqSPtFind(
			@RequestParam(value="json",required=false) String jsonString,
			@RequestParam(value="pageStart",required=false) Integer pageStart,
			@RequestParam(value="pageSize",required=false) Integer pageSize,
			@RequestParam(value="sortStr",required=false) String sortStr) {
		if(sortStr==null) sortStr = "sp_id desc";
		JSONObject json = JSONObject.parseObject(jsonString);
		json.put("sortStr", sortStr);
		LqStrategyPattern lqSPt = JSONObject.toJavaObject(json, LqStrategyPattern.class);
		System.out.println(lqSPt);
		if(pageStart==null) pageStart = 0;
		if(pageSize==null) pageSize = 1;
		ArrayList<LqStrategyPattern> data = lqSPtBo.find(lqSPt, pageStart, pageSize);
		if(data.size()==0) {
			return getErrorResult(null);
		}
		Integer num = lqSPtBo.countByWhere(lqSPt);
		if(num==null) {
			return getErrorResult(null);
		}
		JSONObject result = new JSONObject();
		result.put("data",data);
		result.put("num", num);
		return getSuccessResult(result);
	}
	
	/**
	 * 根据id查找模板
	 * @param spName
	 * @param pageStart
	 * @param pageSize
	 * @return
	 */
	@RequestMapping("/findById/{spId}")
	@ResponseBody
	public JSONObject lqSPtFindById(
			@PathVariable ("spId") Long spId) {
		LqStrategyPattern lqSPt = new LqStrategyPattern();
		lqSPt.setSpId(spId);
		ArrayList<LqStrategyPattern> data = lqSPtBo.find(lqSPt, 0, 1);
		if(data.size()==0) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(data.get(0));
		}
	}
	
	
	@RequestMapping("/findStatus")
	@ResponseBody
	public JSONObject findStatus() {
		return getSuccessResult(lqSPtBo.findStatus());
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
		//删除模板
		List<Domain> lqSpt = new ArrayList<Domain>();
		for(int i=0;i<ids.length;i++) {
			LqStrategyPattern lq = new LqStrategyPattern();
			lq.setSpId(ids[i]);
			lqSpt.add(lq);
		}
		Integer result = lqSPtBo.deleteByIds(lqSpt);
		//删除策略
		List<Domain> lqs = new ArrayList<Domain>();
		for(int i=0;i<ids.length;i++) {
			LqStrategy lq = new LqStrategy();
			lq.setSpId(ids[i]);
			lqs.add(lq);
		}
		lqSBo.deleteByIds(lqs);
		//删除报告
		List<Domain> lqsts = new ArrayList<Domain>();
		for(int i=0;i<ids.length;i++) {
			LqStrategyTest lqSt = new LqStrategyTest();
			lqSt.setSpId(ids[i]);
			lqsts.add(lqSt);
		}
		lqStBo.deleteByIds(lqsts);
		
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
		LqStrategyPattern lq = JSONObject.toJavaObject(json, LqStrategyPattern.class);
		Integer result = lqSPtBo.update(lq);
		if(result==null || result==0) {
			return getErrorResult(null);
		}else {
			return getSuccessResult(result);
		}
	}
}
