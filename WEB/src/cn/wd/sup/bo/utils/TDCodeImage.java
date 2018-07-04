package cn.wd.sup.bo.utils;

import java.awt.image.BufferedImage;  

import jp.sourceforge.qrcode.data.QRCodeImage;  

/**
 * 
    * @Package com.zxt.framework.export
    * @ClassName: TDCodeImage
    * @Description: 二维码对象
    * @author WD created.
    * @date 2016年12月10日
    *
 */
public class TDCodeImage implements QRCodeImage {

	    BufferedImage bufImg;  
	      
	    public TDCodeImage(BufferedImage bufImg) {  
	        this.bufImg = bufImg;  
	    }  
	      
	    @Override  
	    public int getHeight() {  
	        return bufImg.getHeight();  
	    }  
	  
	    @Override  
	    public int getPixel(int x, int y) {  
	        return bufImg.getRGB(x, y);  
	    }  
	  
	    @Override  
	    public int getWidth() {  
	        return bufImg.getWidth();  
	    }  
	  
}
