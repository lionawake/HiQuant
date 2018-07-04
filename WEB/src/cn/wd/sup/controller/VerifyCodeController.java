package cn.wd.sup.controller;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.util.Random;

import javax.imageio.ImageIO;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import cn.wd.sup.constant.CtrlSettingConst;

import com.alibaba.fastjson.JSONObject;
import com.zxt.framework.mvc.controller.VOController;

/**
 * 
 * @author WD
 *
 * PulishDate: 2017年9月1日
 * Function:  构建校验码
 * ChangeLog:
 */
@Controller
@RequestMapping("sup")
public class VerifyCodeController extends VOController {

	// 验证码图片的宽度。配置在VOConf中
	private int width;

	// 验证码图片的高度。配置在VOConf中
	private int height;

	// 验证码字符个数。配置在VOConf中
	private int codeCount;

	private int x = 0;

	// 字体高度
	private int fontHeight;

	private int codeY;

	char[] codeSequence = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q',
			'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2', '3', '4', '5', '6', '7', '8', '9' };
	
	private static final int codeSequence_length = 32;

	/**
	 * 初始化验证图片属性
	 */
	private void initVc() {
		x = width / (codeCount + 1);
		fontHeight = height - 2;
		codeY = height - 4;
	}

	/**
	 * 构建校验码
	 * @param req
	 * @param resp
	 */
	@RequestMapping(value="/vc",method=RequestMethod.GET)
	@ResponseBody
	public void getVerifyCode(HttpServletRequest request, HttpServletResponse resp) {
		initVc();
		// 定义图像buffer
		BufferedImage buffImg = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
		Graphics2D g = buffImg.createGraphics();

		// 创建一个随机数生成器类
		Random random = new Random();

		// 将图像填充为白色
		g.setColor(Color.WHITE);
		g.fillRect(0, 0, width, height);

		// 创建字体，字体的大小应该根据图片的高度来定。
		Font font = new Font("Fixedsys", Font.PLAIN, fontHeight);
		// 设置字体。
		g.setFont(font);

		// 画边框。
		g.setColor(Color.gray);
		g.drawRect(0, 0, width - 1, height - 1);

		// 随机产生160条干扰线，使图象中的认证码不易被其它程序探测到。
		g.setColor(Color.BLACK);
		for (int i = 0; i < 160; i++) {
			int x = random.nextInt(width);
			int y = random.nextInt(height);
			int xl = random.nextInt(12);
			int yl = random.nextInt(12);
			g.drawLine(x, y, x + xl, y + yl);
		}

		// randomCode用于保存随机产生的验证码，以便用户登录后进行验证。
		StringBuffer randomCode = new StringBuffer();
		int red = 0, green = 0, blue = 0;

		// 随机产生codeCount数字的验证码。
		for (int i = 0; i < codeCount; i++) {
			// 得到随机产生的验证码数字。
			String strRand = String.valueOf(codeSequence[random.nextInt( codeSequence_length )]);
			// 产生随机的颜色分量来构造颜色值，这样输出的每位数字的颜色值都将不同。
			red = random.nextInt(255);
			green = random.nextInt(255);
			blue = random.nextInt(255);

			// 用随机产生的颜色将验证码绘制到图像中。
			g.setColor(new Color(red, green, blue));
			g.drawString(strRand, (i + 1) * x, codeY);

			// 将产生的四个随机数组合在一起。
			randomCode.append(strRand);
		}
		// 将四位数字的验证码保存到Session中。
		HttpSession session = request.getSession();
		session.setAttribute( CtrlSettingConst.HTTP_SESSION_VC, randomCode.toString());

		// 禁止图像缓存。
		resp.setHeader("Pragma", "no-cache");
		resp.setHeader("Cache-Control", "no-cache");
		resp.setDateHeader("Expires", 0);

		resp.setContentType("image/jpeg");

		// 将图像输出到Servlet输出流中。
		try{
			ServletOutputStream sos = resp.getOutputStream();
			ImageIO.write(buffImg, "jpeg", sos);
			sos.close();
		}catch( Exception e){
			
		}
	}
	
	/**
	 * 验证用户输入验证码的正确性
	 * @param request
	 * @param cvc 用户输入的验证码
	 * @return 验证结果
	 */
	@RequestMapping(value="/cvc",method=RequestMethod.POST)
	@ResponseBody
	public JSONObject checkVC( HttpServletRequest request ){
		
		String cvc = request.getParameter("cvc");
		logger.debug("THE VC OF USER POSTED IS: " + cvc);
		HttpSession session = request.getSession();
		String vc = (String) session.getAttribute( CtrlSettingConst.HTTP_SESSION_VC);
		if( vc == null || cvc == null){
			logger.debug( "THE VERIFY CODE SESSION IS NULL.");
			return getErrorResult( "");
		}
		if( vc.equalsIgnoreCase( cvc ) ){
			return getSuccessResult( null);
		}else{
			return getErrorResult( "");
		}
	}

	public int getWidth() {
		return width;
	}

	public void setWidth(int width) {
		this.width = width;
	}

	public int getHeight() {
		return height;
	}

	public void setHeight(int height) {
		this.height = height;
	}

	public int getCodeCount() {
		return codeCount;
	}

	public void setCodeCount(int codeCount) {
		this.codeCount = codeCount;
	}
}
