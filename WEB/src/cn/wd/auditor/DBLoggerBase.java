package cn.wd.auditor;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DBLoggerBase {

	
	/**
	 * 
	    * @Title: da
	    * @Description: 基于数据库的审计
	    * @throws Exception    参数
	    * @return void
	    * @throws
	 */
	protected static void da( String tblName, String[] fields, String[] values) throws Exception{

		Connection conn = DBUtil.getConnection();
		PreparedStatement ps = null;
		try {
			
			String p = "";
			for( int i = 0; i < values.length; i++){
				p = p+ "?,";
			}
			p = p.substring( 0, p.length()-1);
			String fs = "";
			for( int i = 0; i < fields.length; i++){
				fs = fs+ fields[i] + ",";
			}
			fs = fs.substring( 0, fs.length()-1);

//			System.out.println("insert into "+tblName+" ("+fs+") values ("+p+")");
			ps = conn.prepareStatement("insert into "+tblName+" ("+fs+") values ("+p+")");
			for( int i = 0; i < values.length; i++){
				ps.setString( i+1, values[i]);
			}
			ps.execute();
		} catch (SQLException e) {
			throw new Exception("Audit failed, beacause: " + e.getMessage());
		} finally {
			try {
				ps.close();
				conn.close();
			} catch (SQLException e) {
//				e.printStackTrace();
				throw new Exception("Close conn failed after audit, beacause: " + e.getMessage());
			}

		}
	}
	
	/**
	 * 
	    * @Title: dda
	    * @Description: 删除审计数据
	    * @param tblName 表名
	    * @param cond 条件
	    * @throws Exception    参数
	    * @return void
	    * @throws
	 */
	public static void dda( String tblName, String cond) throws Exception{

		Connection conn = DBUtil.getConnection();
		PreparedStatement ps = null;
		try {

			ps = conn.prepareStatement("delete from "+tblName +" where " + cond);
			ps.execute();
		} catch (SQLException e) {
			throw new Exception("Delete audit failed, beacause: " + e.getMessage());
		} finally {
			try {
				ps.close();
				conn.close();
			} catch (SQLException e) {
//				e.printStackTrace();
				throw new Exception("Close conn failed after audit, beacause: " + e.getMessage());
			}

		}		
	}
}
