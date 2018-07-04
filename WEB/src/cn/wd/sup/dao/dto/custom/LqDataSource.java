package cn.wd.sup.dao.dto.custom;

import java.sql.Timestamp;

import com.zxt.framework.mvc.dao.Domain;

/**
 * 数据来源接口
 * @author zhengkai
 *
 */
public class LqDataSource extends Domain{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private Long ds_id;
	
	private String data;
	
	private String author;
	
	private Timestamp create_time;

	public Long getDs_id() {
		return ds_id;
	}

	public void setDs_id(Long ds_id) {
		this.ds_id = ds_id;
	}

	public String getData() {
		return data;
	}

	public void setData(String data) {
		this.data = data;
	}

	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	public Timestamp getCreate_time() {
		return create_time;
	}

	public void setCreate_time(Timestamp create_time) {
		this.create_time = create_time;
	}

	public static long getSerialversionuid() {
		return serialVersionUID;
	}
	
	

}
