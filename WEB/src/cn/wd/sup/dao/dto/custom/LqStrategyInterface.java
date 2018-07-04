package cn.wd.sup.dao.dto.custom;

import java.sql.Timestamp;

import com.zxt.framework.mvc.dao.Domain;

/**
 * 交易接口
 * @author zhengkai
 *
 */
public class LqStrategyInterface extends Domain{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private Long si_id;
	
	private String data;
	
	private String author;
	
	private Timestamp create_time;

	public Long getSi_id() {
		return si_id;
	}

	public void setSi_id(Long si_id) {
		this.si_id = si_id;
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
