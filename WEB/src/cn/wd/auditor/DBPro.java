package cn.wd.auditor;

/**
 * 
    * @Package com.zxt.framework.db
    * @ClassName: DBPro
    * @Description: 数据库连接属性对象根类
    * @author Andrew
    * @date 2016年5月24日
    *
 */
public class DBPro {
	
	/**
	 * 设置URL
	 */
	private String url;
	
	/**
	 * 设置驱动名
	 */
	private String driver;
	
	/**
	 * 设置数据库用户名
	 */
	private String userName;
	
	/**
	 * 设置数据库密码
	 */
	private String password;
	
	/**
	 * 设置初始化连接数
	 */
	private Integer baseConns;
	
	/**
	 * 默认值为 false。
	 * 从池中借出对象之前，是否对其进行验证。如果对象验证失败，将其从池中清除，再接着去借下一个
	 */
	private Boolean testOnBorrow = false;

	public Integer getBaseConns() {
		return baseConns;
	}

	public void setBaseConns(Integer baseConns) {
		this.baseConns = baseConns;
	}

	public String getUrl() {
		return url;
	}

	public void setUrl(String url) {
		this.url = url;
	}

	public String getDriver() {
		return driver;
	}

	public void setDriver(String driver) {
		this.driver = driver;
	}

	public String getUserName() {
		return userName;
	}

	public void setUserName(String userName) {
		this.userName = userName;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public Boolean getTestOnBorrow() {
		return testOnBorrow;
	}

	public void setTestOnBorrow(Boolean testOnBorrow) {
		this.testOnBorrow = testOnBorrow;
	}
}
