package cn.wd.sup.constant;


/**
 * 
 * @author WD
 *
 * PulishDate: 2017年9月17日
 * Function:  Contoller层配置参数的常量表
 * ChangeLog:
 */
public class CtrlSettingConst {
	
	public static final int ROLE_ADMIN									=0;
	public static final int ROLE_USER										=1;
	
	//空间目录
//	public static String ROOT_DIR 										=  PropertiesConfigUtils.getString("file.root");  
//	public static String ROOT_DIR_HSARE 								=  PropertiesConfigUtils.getString("file.root.share");  
//	public static String ROOT_PUB_FILE_FOLDER 							=  PropertiesConfigUtils.getString("pub.file.folder");  
//	public static String FILE_NAME_FMA		 							=  PropertiesConfigUtils.getString("file.stat.month.name"); 
	public static final String FILE_SPLIT								="/";

	public static final String 	HTTP_SESSION_ATTR 						= "userwrapper";
	public static final String 	HTTP_SESSION_VC 						= "validateCode";
	
	public static final Integer ACCOUNT_DEFAULT_SEX 					= 0;
	public static final Integer ACCOUNT_DEFAULT_STATUS 					=0;
	public static final Integer ACCOUNT_UNREGISTER_STATUS				=-1;
	
	//文件上传类型
	public static final String FILE_UPLOAD_LIMIT_XLS					="xls";
	public static final String FILE_UPLOAD_LIMIT_XLSX					="xlsx";

	public static final String FILE_UPLOAD_LIMIT_JPEG					="jpg";
	public static final String FILE_UPLOAD_LIMIT_PNG					="png";
	public static final String FILE_UPLOAD_LIMIT_GIF					="gif";

	public static final String[] FILE_UPLOAD_IMG_TYPES				=new String[]{"jpg", "png", "gif","bmp"};
	public static final String[] FILE_UPLOAD_ZIP_TYPES				=new String[]{"zip", "rar", "war","jar"};
	
	public static final int FORLDER_USER									=1;
	public static final int FORLDER_SHARE									=2;
}
