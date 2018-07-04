package cn.wd.sup.dao;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

import org.apache.log4j.Logger;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.zxt.framework.utils.ClassPathFounder;

/**
 * 
 * @author WD
 * 
 *         PulishDate: 2017年9月16日 
 *         Function: JSON文件数据库操作的基础类 
 *         ChangeLog:
 */
public class DaoJsonBase {

	private String forld;
	
	protected final Logger logger = Logger.getLogger(getClass());
	
	/**
	 * 读取文件中的JSON字符串
	 * @param fileName 文件名称
	 * @return 查询的json结果
	 * @throws IOException 文件操作异常
	 */
	protected String readJSONFile(String fileName) throws IOException{
		String jsonStr = "";
		// 将输入流转移到内存输出流中
		 BufferedReader bufReader = null;
		 InputStreamReader insReader = null;
		try {
			File file = new File( ClassPathFounder.getClassPathFolder() + this.getForld() +"/"+ fileName);
			logger.debug("THE JSON FILE PATH IS: "+file.getAbsolutePath());
			if( file.exists()){
				insReader = new InputStreamReader(  
					                        new FileInputStream(file), "UTF-8");  
					  
		                bufReader = new BufferedReader(insReader);  
		  
		                String line = new String();  
		                while ( ( line = bufReader.readLine() ) != null) {  
		                	jsonStr += line; 
		                } 
			}else{
				logger.error("CAN NOT FOUND THE .cdb FILE");
			}
			logger.debug("THE JSON READ FROM FILE IS: " + jsonStr);
		} finally {
			try {
				if ( insReader != null) {
					insReader.close();
				}
				if ( bufReader != null) {
					bufReader.close();
				}
			} catch (IOException ie) {
				logger.warn("CLOSE INPUTSTREAM FAILED, ON READING JSON FILE, BECAUSE: "+ie.getMessage());
			}
		}
		return jsonStr;
	}
	
	/**
	 * 将json数据写入相关文件
	 * @param jObject 需要写入的json内容
	 * @throws IOException 文件操作异常
	 */
	protected void writeJSON2File( JSONObject jObject, String fileName) throws IOException{
		//TODO 此处还需要进一步考虑同步操作的问题
		String filePath = ClassPathFounder.getClassPathFolder() + this.getForld() +"/"+ fileName;
		logger.debug("THE JSON FILE PATH IS: "+filePath);
		OutputStreamWriter out = new OutputStreamWriter( new FileOutputStream( filePath),"UTF-8");
		try{
			out.write( jObject.toJSONString());
		}finally{
			out.flush();
			out.close();
		}
	}
	
	/**
	 * 将json数组写入文件
	 * @param jObject json数组
	 * @throws IOException 文件操作异常
	 */
	protected void writeJSON2File( JSONArray jObject, String fileName) throws IOException{
		//TODO 此处还需要进一步考虑同步操作的问题
		String filePath = ClassPathFounder.getClassPathFolder() + this.getForld() +"/"+ fileName;
		logger.debug("THE JSON FILE PATH IS: "+filePath);
		OutputStreamWriter out = new OutputStreamWriter( new FileOutputStream( filePath),"UTF-8");
		try{
			out.write( jObject.toJSONString());
		}finally{
			out.flush();
			out.close();
		}
	}
	
	public String getForld() {
		return forld;
	}
	public void setForld(String forld) {
		this.forld = forld;
	}
}
