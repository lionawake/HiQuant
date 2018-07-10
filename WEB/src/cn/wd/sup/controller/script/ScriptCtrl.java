package cn.wd.sup.controller.script;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.File;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import org.apache.commons.io.FileUtils;
import org.python.core.PyFunction;
import org.python.core.PyObject;
import org.python.util.PythonInterpreter;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import com.alibaba.fastjson.JSONObject;
import com.zxt.framework.mvc.controller.VOController;
import com.zxt.framework.utils.PropertiesConfigUtils;

import cn.wd.sup.bo.custom.lqS.IBoLqS;
import cn.wd.sup.bo.custom.lqSPt.IBoLqSPt;
import cn.wd.sup.bo.custom.lqSt.IBoLqSt;
import cn.wd.sup.dao.dto.custom.LqStrategyPattern;

@Controller
@RequestMapping("/script")
public class ScriptCtrl extends VOController{
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

	/**
	 * 检查code脚本  TODO
	 * @param jsonString
	 * @return
	 */
	@RequestMapping(value="/codeCheck",method = RequestMethod.POST)
	@ResponseBody
	public JSONObject lqSPtCheck(
			@RequestBody String jsonString) {
		JSONObject json = JSONObject.parseObject(jsonString);
		String code = json.getString("code");
		//TODOO
		Double text = Math.floor(Math.random()*10)%2;
		if(text==0) {
			return getSuccessResult(text);
		}else {
			return getErrorResult(null);
		}
	}
	
	/**
	 * 开始任务
	 * @param spId
	 * @return
	 */
	@RequestMapping(value="/startTest",method = RequestMethod.POST)
	@ResponseBody
	public JSONObject startTest(@RequestBody String jsonString) {
		JSONObject json = JSONObject.parseObject(jsonString);
		Long spId = json.getLong("spId");
		String code = json.getString("code");
		String spName = json.getString("spName");
		String author = json.getString("author");
		//1.生成code文件
		String filePath = PropertiesConfigUtils.getString("file.path")+spId+"/";
		String codeFileName = PropertiesConfigUtils.getString("code.file.name").replaceAll("#spId#", spId.toString());
		String codeFilePath = filePath+"/"+codeFileName;
		try {
			FileUtils.writeStringToFile(new File(codeFilePath), code, "UTF-8");
		} catch (Exception e) {
			e.printStackTrace();
			return getErrorResult("生成code文件失败");
		}
		
		//2.更新状态
		LqStrategyPattern lqSPt = new LqStrategyPattern();
		lqSPt.setSpId(spId);
		lqSPt.setTestStatus(2);
		Integer result = lqSPtBo.update(lqSPt);
		if(result==0 || result==null) {
			return getErrorResult("更新状态失败");
		}
//		//2.调用python脚本
		try {
			//py exe文件路径
			String exe = PropertiesConfigUtils.getString("py.script.exe");
			String command = PropertiesConfigUtils.getString("py.script.path");
			String[] cmdArr = new String[] {exe,command,codeFilePath,spId.toString(), spName, author};
	        Process pr = Runtime.getRuntime().exec(cmdArr);
	        BufferedReader in = new BufferedReader(new InputStreamReader(pr.getInputStream()));
	        List<String> resultData = new ArrayList<String>();
	        resultData.add(exe);
	        resultData.add(command);
	        String line;
	        //Thread.sleep(100);
	        while ((line = in.readLine()) != null) {
	        	System.out.println(line);
	        	resultData.add(line);
	        	//Thread.sleep(100);
	        }
	        in.close();
	        
	        //读取标准错误流
	        BufferedReader brError = new BufferedReader(new InputStreamReader(pr.getErrorStream()));
	        String errline = null;
	        while ((errline = brError.readLine()) != null) {
	        	System.out.println(errline);
	        	resultData.add(errline);
	        }
	        brError.close();
	        pr.waitFor();
	        
	        //成功 保存
	        String resultFileName = PropertiesConfigUtils.getString("result.file.name").replaceAll("#spId#", spId.toString());
	    	String resultFilePAth = filePath+resultFileName;
	    	FileUtils.writeLines(new File(resultFilePAth),"UTF-8", resultData);
	    	return getSuccessResult(resultFilePAth);
	        
		} catch (Exception e) {
			e.printStackTrace();
			return getErrorResult("运行脚本失败");
		}
	}

	public IBoLqSt getLqStBo() {
		return lqStBo;
	}

	public void setLqStBo(IBoLqSt lqStBo) {
		this.lqStBo = lqStBo;
	}
	
	public static void main(String[] args) throws Exception {
		//String exe = "C:/Users/fu/PycharmProjects/Hi/venv/Scripts/python.exe";
		String exe = "python";
		//调用脚本路径
		//String command = "C:/Users/fu/PycharmProjects/Hi/HiQuant/LqPolicyTask.py";
		String command = "C:/Users/fu/PycharmProjects/Hi/HiQuant/LqPolicyTask.py";
        //参数  code路径
        String path = "D:/LqProject/project/result/88/code_88.py";
        String[] cmdArr = new String[] {exe,command,path,"88", "201807022209", "admin"};
        
        Process pr = Runtime.getRuntime().exec(cmdArr);
        BufferedReader in = new BufferedReader(new InputStreamReader(pr.getInputStream()));
        String line;
        while ((line = in.readLine()) != null) {
            System.out.println(line);
        }
        in.close();
        
        //读取标准错误流
        BufferedReader brError = new BufferedReader(new InputStreamReader(pr.getErrorStream()));
        String errline = null;
        while ((errline = brError.readLine()) != null) {
        	System.out.println(errline);
        }
        brError.close();
        pr.waitFor();
        System.out.println("end");
	}
	

}
