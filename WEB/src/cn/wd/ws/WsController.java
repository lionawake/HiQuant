package cn.wd.ws;

import java.io.IOException;

import javax.websocket.CloseReason;
import javax.websocket.OnClose;
import javax.websocket.OnMessage;
import javax.websocket.OnOpen;
import javax.websocket.Session;
import javax.websocket.server.ServerEndpoint;

import com.alibaba.fastjson.JSONException;
import com.alibaba.fastjson.JSONObject;

import cn.wd.sup.controller.script.Script;

@ServerEndpoint("/ws/lq")
public class WsController {
	@OnOpen
	public void onOpen(Session session) throws IOException {
	
	}
	
	@OnMessage
	public void onMessage(Session session , String message) throws Exception{
		try {
			WsBase.wInfo(session, "开始执行脚本中 >>>>>>>>>>>>>>>>>");
			JSONObject json = JSONObject.parseObject(message);
			Long spId = json.getLong("spId");
			String spName = json.getString("spName");
			String author = json.getString("author");
			if(spId==null || spName==null || author==null){
				throw new JSONException("参数信息错误!");
			}
			WsBase.wInfo(session, "策略模板编号："+spId+"，策略名称："+spName+"，策略作者："+author);
			Script script = new Script(session);
			script.script(json);
		} catch(JSONException e){
			e.printStackTrace();
			WsBase.wError(session, "参数有误！");
		} catch(Exception e) {
			e.printStackTrace();
			WsBase.wError(session, "不明真相的错误！");
		} finally {
			WsBase.wInfo(session, "执行结束 >>>>>>>>>>>>>>>>>");
			WsBase.wInfo(session,"end");
		}
	}
	
	@OnClose
	public void onClose(Session session, CloseReason reason) {

	} 
}
