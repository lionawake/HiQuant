package cn.wd.auditor;

import org.apache.tomcat.jdbc.pool.PoolProperties;

/**
 * 
    * @Package com.zxt.framework.db
    * @ClassName: DBPro
    * @Description: 数据库连接属性对象
    * @author Andrew
    * @date 2016年5月24日
    *
 */
public class DBProExt extends DBPro {
	
	/**
	 * 长整型值。为避免过度验证而设定的频率时间值（以秒计）。
	 * 最多以这种频率运行验证。如果连接应该进行验证，
	 * 但却没能在此间隔时间内得到验证，则会重新对其进行验证。默认为 30000（30 秒）。
	 */
	private Integer validationInterval = 30000;
	
	private String validationQuery = "SELECT 1";
	
	/**
	 * 是否测试有效后，才将连接返回。
	 */
	private Boolean testOnReturn = false;
	
	private Integer timeBetweenEvictionRunsMillis = 30000;
	
	/**
	 * 表示如果连接时间超出了removeAbandonedTimeout，则将清除废弃连接
	 */
	private Integer removeAbandonedTimeout = 60;
	
	private Integer minEvictableIdleTimeMillis = 30000;

	public Integer getValidationInterval() {
		return validationInterval;
	}

	public void setValidationInterval(Integer validationInterval) {
		this.validationInterval = validationInterval;
	}

	public String getValidationQuery() {
		return validationQuery;
	}

	public void setValidationQuery(String validationQuery) {
		this.validationQuery = validationQuery;
	}

	public Boolean getTestOnReturn() {
		return testOnReturn;
	}

	public void setTestOnReturn(Boolean testOnReturn) {
		this.testOnReturn = testOnReturn;
	}

	public Integer getTimeBetweenEvictionRunsMillis() {
		return timeBetweenEvictionRunsMillis;
	}

	public void setTimeBetweenEvictionRunsMillis(Integer timeBetweenEvictionRunsMillis) {
		this.timeBetweenEvictionRunsMillis = timeBetweenEvictionRunsMillis;
	}

	public Integer getRemoveAbandonedTimeout() {
		return removeAbandonedTimeout;
	}

	public void setRemoveAbandonedTimeout(Integer removeAbandonedTimeout) {
		this.removeAbandonedTimeout = removeAbandonedTimeout;
	}

	public Integer getMinEvictableIdleTimeMillis() {
		return minEvictableIdleTimeMillis;
	}

	public void setMinEvictableIdleTimeMillis(Integer minEvictableIdleTimeMillis) {
		this.minEvictableIdleTimeMillis = minEvictableIdleTimeMillis;
	}
	
	/**
	 * 
	    * @Title: setPros
	    * @Description: 构建数据库配置对象
	    * @param pros
	    * @return    参数
	    * @return PoolProperties
	    * @throws
	 */
	public static PoolProperties setPros( DBProExt pros ){
		
		PoolProperties poolProperties = new PoolProperties();
		
		// 设置URL
		poolProperties.setUrl( pros.getUrl() );
		// 设置驱动名
		poolProperties.setDriverClassName( pros.getDriver());
		// 设置数据库用户名
		poolProperties.setUsername( pros.getUserName());
		// 设置数据库密码
		poolProperties.setPassword( pros.getPassword());
		// 设置初始化连接数
		poolProperties.setInitialSize( pros.getBaseConns() );
		// 长整型值。为避免过度验证而设定的频率时间值（以秒计）。
		// 最多以这种频率运行验证。如果连接应该进行验证，
		// 但却没能在此间隔时间内得到验证，则会重新对其进行验证。默认为 30000（30 秒）。
		poolProperties.setValidationInterval( pros.getValidationInterval());
		// 它配置之后，才能配置testOnBorrow，testOnRetur
		poolProperties.setValidationQuery( pros.getValidationQuery());
		// 默认值为 false。
		//从池中借出对象之前，是否对其进行验证。如果对象验证失败，将其从池中清除，再接着去借下一个
		poolProperties.setTestOnBorrow( pros.getTestOnBorrow());
		// 是否测试有效后，才将连接返回。
		poolProperties.setTestOnReturn( pros.getTestOnReturn());

		poolProperties.setTimeBetweenEvictionRunsMillis( pros.getTimeBetweenEvictionRunsMillis() );
		// 表示如果连接时间超出了removeAbandonedTimeout，则将清除废弃连接
		poolProperties.setRemoveAbandonedTimeout( pros.getRemoveAbandonedTimeout());
								
		poolProperties.setMinEvictableIdleTimeMillis( pros.getMinEvictableIdleTimeMillis());
		
		return poolProperties;
	}
}
