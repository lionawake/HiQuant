package cn.wd.sup.constant;

import com.zxt.framework.utils.PropertiesConfigUtils;


/**
 * 
    * @Package cn.wd.sup.constant
    * @ClassName: CustomConst
    * @Description: 工单系统常量表
    * @author WD created.
    * @date 2017年12月9日
    *
 */
public class CustomConst {


	public static String resumesPath = PropertiesConfigUtils.getString("file.path.resume");
	
	/**
	 *   `orderType` int(4) NOT NULL DEFAULT '0' COMMENT '类型 0：bug 1：story',
		  `orderFactor` varchar(128) NOT NULL COMMENT '工单提出厂家',
		  `orderTitle` text NOT NULL COMMENT '工单标题',
		  `orderVersion` varchar(256) DEFAULT NULL COMMENT '工单版本',
		  `orderModule` text COMMENT '工单对应模块',
		  `orderCharger` varchar(256) NOT NULL COMMENT '工单责任人',
		  `orderPriority` int(4) NOT NULL DEFAULT '1' COMMENT '工单优先级 0：低 1：中 2：高',
		  `orderImportance` int(4) NOT NULL DEFAULT '1' COMMENT '工单重要性 0：提示 1：一般 2：重要 3：关键',
		  `orderResult` int(4) DEFAULT NULL COMMENT '工单结果 0：新建 1： 处理中 2：已解决 3： 未复现 4：不是问题 5：挂起 6：已拒绝 7：已关闭',
		  `orderDes` text COMMENT '工单描述',
		  `orderTag` text COMMENT '工单标签',
		  `orderField` int(4) DEFAULT NULL COMMENT '工单领域 0：功能 1：性能 2：可用性 3：可靠性 4：网络安全 5：可维护性 6：其他',
		  `orderCreator` varchar(128) NOT NULL COMMENT '工单创建人账户',
		  `orderTime` datetime NOT NULL COMMENT '工单创建时间',
		  `orderMark` text COMMENT '工单备注',
		  `orderWHP` int(4) DEFAULT NULL COMMENT '工单预计工时',
		  `orderWHA` int(4) DEFAULT NULL COMMENT '工单实际工时',
	 */
	public final static Integer ORDER_ID_FIELD_FA 		= 0;
	public final static Integer ORDER_ID_FIELD_PA 		= 1;
	public final static Integer ORDER_ID_FIELD_UA		= 2;
	public final static Integer ORDER_ID_FIELD_RA		= 3;
	public final static Integer ORDER_ID_FIELD_NSA 		= 4;
	public final static Integer ORDER_ID_FIELD_MA		= 5;
	public final static Integer ORDER_ID_FIELD_OTHER	= 6;
	public final static String  ORDER_NAME_FIELD_FA 	= "功能";
	public final static String  ORDER_NAME_FIELD_PA		= "性能";
	public final static String  ORDER_NAME_FIELD_UA		= "可用性";
	public final static String  ORDER_NAME_FIELD_RA		= "可靠性";
	public final static String  ORDER_NAME_FIELD_NSA	= "网络安全";
	public final static String  ORDER_NAME_FIELD_MA		= "可维护性 ";
	public final static String  ORDER_NAME_FIELD_OTHER	= "其他";
	
	public static String getOrderFieldNameBYId( Integer id){
		switch( id ){
		case 0:
			return ORDER_NAME_FIELD_FA;
		case 1: 
			return ORDER_NAME_FIELD_PA;
		case 2: 
			return ORDER_NAME_FIELD_UA;
		case 3: 
			return ORDER_NAME_FIELD_RA;
		case 4: 
			return ORDER_NAME_FIELD_NSA;
		case 5: 
			return ORDER_NAME_FIELD_MA;
		case 6: 
			return ORDER_NAME_FIELD_OTHER;
		default:
			return null;
		}
	}
	public static Integer getOrderFieldIdByName( String name){
		switch( name ){
		case ORDER_NAME_FIELD_FA:
			return ORDER_ID_FIELD_FA;
		case ORDER_NAME_FIELD_PA: 
			return ORDER_ID_FIELD_PA;
		case ORDER_NAME_FIELD_UA: 
			return ORDER_ID_FIELD_UA;
		case ORDER_NAME_FIELD_RA: 
			return ORDER_ID_FIELD_RA;
		case ORDER_NAME_FIELD_NSA: 
			return ORDER_ID_FIELD_NSA;
		case ORDER_NAME_FIELD_MA: 
			return ORDER_ID_FIELD_MA;
		case ORDER_NAME_FIELD_OTHER: 
			return ORDER_ID_FIELD_OTHER;
		default:
			return null;
		}
	}
	
	//正常 1：发布 2：作废
	public final static Integer ORDER_ID_RESULT_NEW 		= 0;
	public final static Integer ORDER_ID_RESULT_PROCESS 	= 1;
	public final static Integer ORDER_ID_RESULT_SOLVED		= 2;
	public final static String  ORDER_NAME_RESULT_NEW 		= "内部";
	public final static String  ORDER_NAME_RESULT_PROCESS	= "发布";
	public final static String  ORDER_NAME_RESULT_SOLVED	= "作废";

	public static String getOrderResultNameBYId( Integer id){
		switch( id ){
		case 0:
			return ORDER_NAME_RESULT_NEW;
		case 1: 
			return ORDER_NAME_RESULT_PROCESS;
		case 2: 
			return ORDER_NAME_RESULT_SOLVED;
		default:
			return null;
		}
	}
	public static Integer getOrderResultIdByName( String name){
		switch( name ){
		case ORDER_NAME_RESULT_NEW:
			return ORDER_ID_RESULT_NEW;
		case ORDER_NAME_RESULT_PROCESS: 
			return ORDER_ID_RESULT_PROCESS;
		case ORDER_NAME_RESULT_SOLVED: 
			return ORDER_ID_RESULT_SOLVED;
		default:
			return null;
		}
	}
	
	public final static Integer ORDER_ID_IMPORT_INFO 		= 0;
	public final static Integer ORDER_ID_IMPORT_NORMAL 		= 1;
	public final static Integer ORDER_ID_IMPORT_IMPORTANT	= 2;
	public final static Integer ORDER_ID_IMPORT_CRUX 		= 3;
	public final static String  ORDER_NAME_IMPORT_INFO 		= "提示";
	public final static String  ORDER_NAME_IMPORT_NORMAL 	= "一般";
	public final static String  ORDER_NAME_IMPORT_IMPORTANT	= "重要";
	public final static String  ORDER_NAME_IMPORT_CRUX 		= "关键";
	
	public static String getOrderImportNameBYId( Integer id){
		switch( id ){
		case 0:
			return ORDER_NAME_IMPORT_INFO;
		case 1: 
			return ORDER_NAME_IMPORT_NORMAL;
		case 2: 
			return ORDER_NAME_IMPORT_IMPORTANT;
		case 3: 
			return ORDER_NAME_IMPORT_CRUX;
		default:
			return null;
		}
	}
	public static Integer getOrderImportIdByName( String name){
		switch( name ){
		case ORDER_NAME_IMPORT_INFO:
			return ORDER_ID_IMPORT_INFO;
		case ORDER_NAME_IMPORT_NORMAL: 
			return ORDER_ID_IMPORT_NORMAL;
		case ORDER_NAME_IMPORT_IMPORTANT: 
			return ORDER_ID_IMPORT_IMPORTANT;
		case ORDER_NAME_IMPORT_CRUX: 
			return ORDER_ID_IMPORT_CRUX;
		default:
			return null;
		}
	}
	
	public final static Integer ORDER_ID_TYPE_BUG 			= 0;
	public final static Integer ORDER_ID_TYPE_STORY 		= 1;
	public final static String  ORDER_NAME_TYPE_BUG 		= "Bug";
	public final static String  ORDER_NAME_TYPE_STORY 		= "Story";
	
	/**
	 * 
	    * @Title: getOrderTypeNameBYId
	    * @Description: 根据ID获取类型名称
	    * @param id
	    * @return    参数
	    * @return String
	    * @throws
	 */
	public static String getOrderTypeNameBYId( Integer id){
		switch( id ){
		case 0:
			return ORDER_NAME_TYPE_BUG;
		case 1: 
			return ORDER_NAME_TYPE_STORY;
		default:
			return null;
		}
	}
	/**
	 * 
	    * @Title: getOrderIdByName
	    * @Description: 根据名称获取类型ID
	    * @param name
	    * @return    参数
	    * @return Integer
	    * @throws
	 */
	public static Integer getOrderTypeIdByName( String name){
			switch( name ){
			case ORDER_NAME_TYPE_BUG:
				return ORDER_ID_TYPE_BUG;
			case ORDER_NAME_TYPE_STORY: 
				return ORDER_ID_TYPE_STORY;
			default:
				return null;
			}
	}


	public final static Integer ORDER_ID_PRIORITY_LOW 			= 0;
	public final static Integer ORDER_ID_PRIORITY_MIDDLE 		= 1;
	public final static Integer ORDER_ID_PRIORITY_HIGH	 		= 2;
	public final static String  ORDER_NAME_PRIORITY_LOW 		= "低";
	public final static String  ORDER_NAME_PRIORITY_MIDDLE 		= "中";
	public final static String  ORDER_NAME_PRIORITY_HIGH 		= "高";

	/**
	 * 
	    * @Title: getOrderPriorityNameBYId
	    * @Description: 基于ID获取优先级名称
	    * @param id
	    * @return    参数
	    * @return String
	    * @throws
	 */
	public static String getOrderPriorityNameBYId( Integer id){
		switch( id ){
		case 0:
			return ORDER_NAME_PRIORITY_LOW;
		case 1: 
			return ORDER_NAME_PRIORITY_MIDDLE;
		case 2: 
			return ORDER_NAME_PRIORITY_HIGH;
		default:
			return null;
		}
	}
	/**
	 * 
	    * @Title: getOrderPriorityIdByName
	    * @Description: 基于名字获取优先级ID
	    * @param name
	    * @return    参数
	    * @return Integer
	    * @throws
	 */
	public static Integer getOrderPriorityIdByName( String name){
			switch( name ){
			case ORDER_NAME_PRIORITY_LOW:
				return ORDER_ID_PRIORITY_LOW;
			case ORDER_NAME_PRIORITY_MIDDLE: 
				return ORDER_ID_PRIORITY_MIDDLE;
			case ORDER_NAME_PRIORITY_HIGH: 
				return ORDER_ID_PRIORITY_HIGH;
			default:
				return null;
			}
	}


}
