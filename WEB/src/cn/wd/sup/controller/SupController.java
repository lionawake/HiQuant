package cn.wd.sup.controller;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import cn.wd.sup.constant.CtrlSettingConst;
import cn.wd.sup.controller.act.ActWrapper;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.zxt.framework.mvc.controller.VOController;
import org.apache.commons.lang.StringUtils;

/**
 * 
    * @Package cn.doofen.sup.controller
    * @ClassName: SupController
    * @Description: Controller根类
    * @author WD
    * @date 2017年9月14日
    *
 */
public class SupController extends VOController{	
	
	/**
	 * 获取用户的Session信息
	 * @param request HttpRequest
	 * @param response HttpResponse
	 * @return 用户Session信息的JSON或者错误信息
	 */
	protected ActWrapper getSession( HttpServletRequest request){
		try{
			HttpSession session = request.getSession();
			JSONObject sJson = (JSONObject)session.getAttribute( CtrlSettingConst.HTTP_SESSION_ATTR );
			
			ActWrapper userWrap = JSON.toJavaObject( sJson, ActWrapper.class);
			
			return userWrap;
		}catch( Exception e){
			return null;
		}
	}

	/**
	 * 获取文件名称
	 * 
	 * @param data
	 * @return
	 * @throws UnsupportedEncodingException
	 */
	protected String getFileName(HttpServletRequest request, String fileName) throws UnsupportedEncodingException {

		if (fileName != null) {
			fileName = fileName.trim();
		} else {
			fileName = "简历_" + new SimpleDateFormat("yyyy-MM-dd").format(new Date());
		}
		final String userAgent = request.getHeader("USER-AGENT");
		logger.debug("UA:" + userAgent);
		if (StringUtils.contains(userAgent, "Trident")) {// IE浏览器
			fileName = URLEncoder.encode(fileName, "UTF-8");
			return fileName;
		} else if (StringUtils.contains(userAgent, "Firefox")) {// google,火狐浏览器
			fileName = new String(fileName.getBytes(), "ISO8859-1");
			return fileName;
		} else {
			fileName = URLEncoder.encode(fileName, "UTF-8");// 其他浏览器
			return fileName;
		}

	}
}
