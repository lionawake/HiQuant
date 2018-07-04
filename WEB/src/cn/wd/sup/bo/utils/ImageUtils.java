package cn.wd.sup.bo.utils;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import org.apache.commons.codec.binary.Base64;

public class ImageUtils {

	/**
	 * 
	 * @Title: GetImageStr
	 * @Description:将图片文件转化为字节数组字符串，并对其进行Base64编码处理
	 * @param imgFilePath
	 * @return 参数
	 * @return String
	 * @throws
	 */
	public static String GetImgBase64Str(String imgFilePath) {//
		byte[] data = null;

		// 读取图片字节数组
		try {
			InputStream in = new FileInputStream(imgFilePath);
			data = new byte[in.available()];
			in.read(data);
			in.close();
		} catch (IOException e) {
			e.printStackTrace();
		}

		// 对字节数组Base64编码
//		BASE64Encoder encoder = new BASE64Encoder();
//		return encoder.encode(data);// 返回Base64编码过的字节数组字符串
		return Base64.encodeBase64String( data);
	}

	/**
	 * 
	 * @Title: GetImageStr
	 * @Description: 将图片文件转化为字节数组字符串，并对其进行Base64编码处理
	 * @param in
	 * @return 参数
	 * @return String
	 * @throws
	 */
	public static String GetImgBase64Str(InputStream in) {
		byte[] data = null;

		// 读取图片字节数组
		try {
			data = new byte[in.available()];
			in.read(data);
			in.close();
		} catch (IOException e) {
			e.printStackTrace();
		}

		// 对字节数组Base64编码
//		BASE64Encoder encoder = new BASE64Encoder();
//		return encoder.encode(data);// 返回Base64编码过的字节数组字符串
		return Base64.encodeBase64String( data);
	}
	
	public static String GetImgBase64Str(ByteArrayOutputStream out) {
		InputStream in = new ByteArrayInputStream(out.toByteArray());
		return GetImgBase64Str( in );
	}

	/**
	 * 
	    * @Title: GenerateImage
	    * @Description:  对字节数组字符串进行Base64解码并生成图片
	    * @param imgStr
	    * @param imgFilePath
	    * @return    参数
	    * @return boolean
	    * @throws
	 */
	public static boolean GenerateImageByBase64(String imgStr, String imgFilePath) {//
		if (imgStr == null) // 图像数据为空
			return false;
//		BASE64Decoder decoder = new BASE64Decoder();
		try {
			// Base64解码
//			byte[] bytes = decoder.decodeBuffer(imgStr);
			byte[] bytes = Base64.decodeBase64(imgStr);
			for (int i = 0; i < bytes.length; ++i) {
				if (bytes[i] < 0) {// 调整异常数据
					bytes[i] += 256;
				}
			}
			// 生成jpeg图片
			OutputStream out = new FileOutputStream(imgFilePath);
			out.write(bytes);
			out.flush();
			out.close();
			return true;
		} catch (Exception e) {
			return false;
		}
	}
	
	public static void main(String[] args){
		System.out.println(ImageUtils.GetImgBase64Str("C:/0.D-Work/Tech/projext/p001/webapp/WEB-INF/templates/logo_report.jpg"));
	}
}
