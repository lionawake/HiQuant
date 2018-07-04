package cn.wd.auditor.custom;

import java.text.SimpleDateFormat;
import java.util.Date;

import cn.wd.auditor.DBLoggerBase;


/**
 * 
    * @Package cn.wd.sup.bo.custom.tool
    * @ClassName: woLogger
    * @Description: 工单日志记录接口
    * @author WD created.
    * @date 2018年2月2日
    *
 */
public class WoLogger extends DBLoggerBase{

	private final static String tblName = "t_waudit";

	private final static String[] fields_base = {"account", "wid", "action", "auditTime"};
	private final static String[] fields_modify = {"account", "wid", "action", "actionStatus", "modifyContent", "auditTime"};
	
	/**
	 * 
	    * @Title: log
	    * @Description: 基本日志
	    * @param account
	    * @param wid
	    * @param action
	    * @param actionStatus
	    * @param content
	    * @throws Exception    参数
	    * @return void
	    * @throws
	 */
	public static void log(String account, Integer wid, Integer action) throws Exception{
		SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		String[] logs = {account, ""+wid, ""+action, formatter.format( new Date() ) };
		da( tblName, fields_base, logs);
	}

	/**
	 * 
	    * @Title: logm
	    * @Description: 编辑日志
	    * @param account
	    * @param wid
	    * @param action
	    * @param actionStatus
	    * @param content
	    * @throws Exception    参数
	    * @return void
	    * @throws
	 */
	public static void logm(String account, Integer wid, Integer action, Integer actionStatus, String content) throws Exception{
		SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		String[] logs = {account, ""+wid, ""+action, ""+actionStatus, content, formatter.format( new Date() ) };
		da( tblName, fields_modify, logs);
	}
}
