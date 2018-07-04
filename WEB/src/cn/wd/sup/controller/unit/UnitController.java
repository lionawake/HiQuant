package cn.wd.sup.controller.unit;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import cn.wd.sup.constant.CtrlMsgConst;
import cn.wd.sup.controller.SupController;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;


@Controller
@RequestMapping("sup/unit")
public class UnitController extends SupController {
	
	@RequestMapping(value="/json",method=RequestMethod.GET)
	@ResponseBody
	public JSONObject getUnitData(  
			HttpServletRequest request,
			HttpServletResponse response,
			@RequestParam(value="code",required=true) String code){
		try{	
			JSONArray rjarr = new JSONArray();
			JSONReader reader = new JSONReader();
//			if( code.equalsIgnoreCase("pt")){
				reader.setForld("unit");
				String str = reader.readJSONFile( code+".json");
				rjarr = JSONArray.parseArray( str);
//			}
			return getSuccessResult( rjarr);
		}catch( Exception e){
			e.printStackTrace();
			return getErrorResult( CtrlMsgConst.MSG_LOGOUT_FAILED_SYSTEM);
		}
	}
}
