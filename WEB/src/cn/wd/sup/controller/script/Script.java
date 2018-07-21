package cn.wd.sup.controller.script;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

import javax.websocket.Session;

import org.apache.commons.io.FileUtils;
import org.springframework.context.support.FileSystemXmlApplicationContext;

import com.alibaba.fastjson.JSONObject;
import com.zxt.framework.utils.PropertiesConfigUtils;

import cn.wd.sup.bo.custom.lqSPt.IBoLqSPt;
import cn.wd.sup.dao.dto.custom.LqStrategyPattern;
import cn.wd.ws.WsBase;

public class Script {
	private IBoLqSPt lqSPtBo = (IBoLqSPt)new FileSystemXmlApplicationContext(new String[]{
			"classpath:../config/app/DAOConfiguration.xml",
			"classpath:../config/app/applicationContext.xml",
			"classpath:../config/app/BOConfiguration.xml"}).getBean("lqSPtBo");
	
	
	private Session session;
	
	public Script(Session session){
		this.session = session ; 
	}
	
	public void script(JSONObject json) throws Exception{
		Long spId = json.getLong("spId");
		//String code = json.getString("code");
		String spName = json.getString("spName");
		String author = json.getString("author");
		
		WsBase.wInfo(session, "查找模板信息中...");
		LqStrategyPattern lq = new LqStrategyPattern();
		lq.setSpId(spId);
		ArrayList<LqStrategyPattern> list = lqSPtBo.find(lq, 0, 1);
		if(list==null || list.size()==0){
			WsBase.wError(session, "查找信息失败！");
			throw new Exception("查找信息失败！");
		}
		String code = list.get(0).getCode();
		WsBase.wInfo(session, "查找信息成功");
		//1.生成code文件
		WsBase.wInfo(session, "生成code文件中");
		String filePath = PropertiesConfigUtils.getString("file.path")+spId+"/";
		String codeFileName = PropertiesConfigUtils.getString("code.file.name").replaceAll("#spId#", spId.toString());
		String codeFilePath = filePath+"/"+codeFileName;
		try {
			FileUtils.writeStringToFile(new File(codeFilePath), code, "UTF-8");
		} catch (Exception e) {
			e.printStackTrace();
			WsBase.wError(session, "生成code文件失败");
			throw new Exception("生成code文件失败");
		}
		WsBase.wInfo(session, "生成code成功");
		
		//2.更新状态
		WsBase.wInfo(session, "更新任务状态");
		LqStrategyPattern lqSPt = new LqStrategyPattern();
		lqSPt.setSpId(spId);
		lqSPt.setTestStatus(2);
		
		//修改模板状态
		Integer result = lqSPtBo.update(lqSPt);
		if(result==0 || result==null) {
			WsBase.wError(session, "更新状态失败");
			throw new Exception("更新状态失败");
		}
		WsBase.wInfo(session, "更新任务状态成功");
		
		//2.调用python脚本
		WsBase.wInfo(session, "数据分析中... ...");
		BufferedReader br = null;
		Process process = null;
		try {
			int rs = 0;
			String output = null;
			String exe = PropertiesConfigUtils.getString("py.script.exe");
			String command = PropertiesConfigUtils.getString("py.script.path");
	        String[] cmds = new String[] {exe,command,codeFilePath,spId.toString(), spName, author};
	        List<String> resultData = new ArrayList<String>();
	        resultData.add(exe);
	        resultData.add(command);
	        String resultFileName = PropertiesConfigUtils.getString("result.file.name").replaceAll("#spId#", spId.toString());
	        String resultFilePAth = filePath+resultFileName;
	        
	        ProcessBuilder builder = new ProcessBuilder(cmds);
	        builder.redirectErrorStream(true);
	        process = builder.start();
	        br = new BufferedReader(new InputStreamReader(process.getInputStream()));
	        
	        while (null != (output = br.readLine()))
	        {
//	        	System.out.println(output);
	        	resultData.add(output);
	        }
	        rs = process.waitFor();
	        if(rs != 0) {
	        	System.out.printf("Python failed: %d\n", rs);
	        	WsBase.wError(session, "执行Python任务失败");
	        }else {
	        	System.out.println("Python Successful");
	        	WsBase.wInfo(session, "执行Python任务成功");
	        }
//	        process.destroy();
//	        br.close();
	        System.out.println("结束");
	        //成功 保存
	    	FileUtils.writeLines(new File(resultFilePAth),"UTF-8", resultData);
	    	WsBase.wInfo(session, "分析结束，结果保存在 "+resultFilePAth);
		} catch (Exception e) {
			e.printStackTrace();
			WsBase.wError(session, "分析失败");
		}finally{
			if(br != null) {
				br.close();
			}
			if(process != null) {
				process.destroy();
			}
		}
	}
}
