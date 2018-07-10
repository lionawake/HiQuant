package cn.wd.ws;


import javax.websocket.Session;


public class WsBase{
	private static String msgFormat(String logLevel , String msg) {
		return msg;
	}

	/**
	 * 
	 * @Title: info
	 * @Description: html日志输出 info级别
	 * @param msg
	 * @return 参数
	 * @return String
	 * @throws
	 */
//	public static String common(String msg) {
//		return WsConst.MSG_COMMON.replaceAll("\\{msg\\}", msgFormat(msg));
//	}
	
	/**
	 * 
	 * @Title: error
	 * @Description: html日志输出info级别
	 * @param msg
	 * @return 参数
	 * @return String
	 * @throws
	 */
	public static String info(String msg) {
		return WsConst.MSG_INFO.replaceAll("\\{msg\\}", msgFormat("信息",msg));
	}

	/**
	 * 
	 * @Title: warn
	 * @Description: html日志输出 warn级别
	 * @param msg
	 * @return 参数
	 * @return String
	 * @throws
	 */
	public static String warn(String msg) {
		return WsConst.MSG_WARN.replaceAll("\\{msg\\}", msgFormat("警告",msg));
	}

	/**
	 * 
	 * @Title: error
	 * @Description: html日志输出 error级别
	 * @param msg
	 * @return 参数
	 * @return String
	 * @throws
	 */
	public static String error(String msg) {
		return WsConst.MSG_ERROR.replaceAll("\\{msg\\}", msgFormat("错误",msg));
	}

	/**
	 * 
	 * @Title: wWarn
	 * @Description: html日志输出info级别
	 * @param session
	 * @param msg
	 * @param fileName    参数
	 * @return void
	 * @throws
	 */
	public static void wInfo(Session session, String msg ) {
		try {
			session.getBasicRemote().sendText(info(msg));
		} catch (Exception e) {
			//
		}
	}
	
	
	/**
	 * 
	 * @Title: wWarn
	 * @Description: html日志输出warn级别
	 * @param session
	 * @param msg
	 * @param fileName    参数
	 * @return void
	 * @throws
	 */
	public static void wWarn(Session session, String msg) {
		try {
			session.getBasicRemote().sendText(warn(msg));
		} catch (Exception e) {
			//
		}
	}

	/**
	 * 
	 * @Title: wWarn
	 * @Description: html日志输出error级别
	 * @param session
	 * @param msg
	 * @param fileName    参数
	 * @return void
	 * @throws
	 */
	public static void wError(Session session, String msg) {
		try {
			session.getBasicRemote().sendText(error(msg));
		} catch (Exception e) {
			//
		}
	}
	
}
