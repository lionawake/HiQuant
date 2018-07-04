package cn.wd;

import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;

import com.zxt.framework.utils.PropertiesConfigUtils;

/**
 * 工程启动加载类<br/>
 *  用于初始化系统字典  bso对象信息
 * @author WD
 *
 * PulishDate: 2017年9月20日
 * Function: 
 * ChangeLog:
 */
public class Startup implements ServletContextListener {
	
	public void contextDestroyed(ServletContextEvent sce) {
	}

	public void contextInitialized(ServletContextEvent sce) {

		try{
			initPro();
		}catch(Exception e){
			System.err.println("doofen: load System Properties failed.");
		}
		System.out.println("");
	}
	
	protected void initPro() throws Exception{
		System.out.println("doofen:  load system properties...");
		String[] pros = new String[]{"../config/conf.properties","../config/db/jdbc.properties"};
		PropertiesConfigUtils.loadFiles( pros );

		for( int i = 0; i < pros.length; i++){
			System.out.println("doofen:  load property file: " + pros[i]);
		}
		System.out.println("doofen:  load system properties success!");
	}
}
