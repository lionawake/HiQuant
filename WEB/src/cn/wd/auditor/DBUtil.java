package cn.wd.auditor;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.Properties;
import java.util.concurrent.Future;

import org.apache.tomcat.jdbc.pool.DataSource;
import org.apache.tomcat.jdbc.pool.PoolProperties;

/**
 * 
    * @Package cn.wd.auditor
    * @ClassName: DBUtil
    * @Description: 数据库操作基类
    * @author WD created.
    * @date 2018年2月2日
    *
 */
public class DBUtil {
	
	static DataSource dataSource = new DataSource();
	
	private static String PRO_DB_SETTING = "../config/db/jdbc.properties";

	private String proSource;
	
	/**
	 * 
	    * @Title: init
	    * @Description: 基础初始化
	    * @param pros    参数
	    * @return void
	    * @throws
	 */
	public static void init( DBPro pros ){

		DBProExt pro = new DBProExt();
		try {			
			// 设置URL
			pro.setUrl( pros.getUrl());
			// 设置驱动名
			pro.setDriver( pros.getDriver());
			// 设置数据库用户名
			pro.setUserName( pros.getUserName());
			// 设置数据库密码
			pro.setPassword( pros.getPassword());
			// 设置初始化连接数
			pro.setBaseConns( pros.getBaseConns());
			
			pro.setTestOnBorrow(true);
			
			PoolProperties poolProperties = DBProExt.setPros( pro);
			
			dataSource.setPoolProperties(poolProperties);
		} catch (Exception e) {
			throw new RuntimeException("初始化数据库连接池失败");
		}
	}
	
	/**
	 * 
	    * @Title: initByProperies
	    * @Description: 基于配置文件的数据库初始化，仅需url\driver\ username\password\initialSize
	    * @return void
	    * @throws
	 */
	public static void initByProperies() {

		DBProExt pros = new DBProExt();
		Properties dbProperties = new Properties();
		try {
			
			dbProperties.load( DBUtil.class.getClassLoader().getResourceAsStream( PRO_DB_SETTING ) );
			// 设置URL
			pros.setUrl(dbProperties.getProperty("url"));
			// 设置驱动名
			pros.setDriver(dbProperties.getProperty("driver"));
			// 设置数据库用户名
			pros.setUserName(dbProperties.getProperty("username"));
			// 设置数据库密码
			pros.setPassword(dbProperties.getProperty("password"));
			// 设置初始化连接数
			pros.setBaseConns(Integer.valueOf(dbProperties.getProperty("initialSize")));
			pros.setTestOnBorrow(true);
			
			PoolProperties poolProperties = DBProExt.setPros( pros);
			
			dataSource.setPoolProperties(poolProperties);
		} catch (Exception e) {
			throw new RuntimeException("初始化数据库连接池失败");
		}
	}
	
	/**
	 * 
	    * @Title: initByProperies
	    * @Description: 自定义db配置属性
	    * @param proResources    参数
	    * @return void
	    * @throws
	 */
	public static void initByProperies( String proResources) {

		DBProExt pros = new DBProExt();
		Properties dbProperties = new Properties();
		try {
			if( proResources == null || proResources.isEmpty())
				throw new Exception("DB properties can not found.");
			dbProperties.load(  DBUtil.class.getClassLoader().getResourceAsStream( proResources ) );
			// 设置URL
			pros.setUrl(dbProperties.getProperty("url"));
			// 设置驱动名
			pros.setDriver(dbProperties.getProperty("driver"));
			// 设置数据库用户名
			pros.setUserName(dbProperties.getProperty("username"));
			// 设置数据库密码
			pros.setPassword(dbProperties.getProperty("password"));
			// 设置初始化连接数
			pros.setBaseConns(Integer.valueOf(dbProperties.getProperty("initialSize")));
			pros.setTestOnBorrow(true);
			
			PoolProperties poolProperties = DBProExt.setPros( pros);
			
			dataSource.setPoolProperties(poolProperties);
		} catch (Exception e) {
			throw new RuntimeException("初始化数据库连接池失败");
		}
	}
	
	/**
	 * 
	    * @Title: init
	    * @Description: 基于用户自定义的初始化
	    * @param pros    参数
	    * @return void
	    * @throws
	 */
	public static void initBySelf( DBProExt pros){

		try {			
			PoolProperties poolProperties = DBProExt.setPros( pros);
			
			dataSource.setPoolProperties(poolProperties);
		} catch (Exception e) {
			throw new RuntimeException("初始化数据库连接池失败");
		}
	}

	/**
	 * 获取数据库连接
	 * 
	 * @return 数据库连接
	 */
	public static final Connection getConnection() {
		Connection conn = null;
		try {
			// 连接池同步
			Future<Connection> future = dataSource.getConnectionAsync();
			while (!future.isDone()) {
				// 等待连接池同步
				Thread.sleep(100);
			}

			// 获取连接池
			conn = future.get();

		} catch ( Exception e) {
			throw new RuntimeException("获取数据库连接失败");
		} 
		return conn;

	}

	/**
	 * 关闭连接
	 * 
	 * @param conn
	 *                需要关闭的连接
	 */
	public static void closeConnection(Connection conn) {
		try {
			if (conn != null && !conn.isClosed()) {
				conn.close();
			}
		} catch (SQLException e) {
			throw new RuntimeException("关闭数据库连接失败");
		}
	}

	public String getProSource() {
		return proSource;
	}

	public void setProSource(String proSource) {
		this.proSource = proSource;
	}
}
