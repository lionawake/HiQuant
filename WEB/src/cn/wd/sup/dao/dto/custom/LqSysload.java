package cn.wd.sup.dao.dto.custom;

import java.sql.Timestamp;

import com.zxt.framework.mvc.dao.Domain;

/**
 * 系统负载表 lq_sysload
 * @author zhengkai
 *
 */
public class LqSysload extends Domain{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	private Timestamp sampleTime;
	
	private Integer cupRadio;
	
	private Integer memRatio;
	
	private Integer memCost;
	
	private Integer diskRatio;
	
	private Long diskReadBytes;
	
	private Long diskWriteBytes;
	
	private Long netUpBytes;
	
	private Long netDwBytes;

	public Timestamp getSampleTime() {
		return sampleTime;
	}

	public void setSampleTime(Timestamp sampleTime) {
		this.sampleTime = sampleTime;
	}

	public Integer getCupRadio() {
		return cupRadio;
	}

	public void setCupRadio(Integer cupRadio) {
		this.cupRadio = cupRadio;
	}

	public Integer getMemRatio() {
		return memRatio;
	}

	public void setMemRatio(Integer memRatio) {
		this.memRatio = memRatio;
	}

	public Integer getMemCost() {
		return memCost;
	}

	public void setMemCost(Integer memCost) {
		this.memCost = memCost;
	}

	public Integer getDiskRatio() {
		return diskRatio;
	}

	public void setDiskRatio(Integer diskRatio) {
		this.diskRatio = diskRatio;
	}

	public Long getDiskReadBytes() {
		return diskReadBytes;
	}

	public void setDiskReadBytes(Long diskReadBytes) {
		this.diskReadBytes = diskReadBytes;
	}

	public Long getDiskWriteBytes() {
		return diskWriteBytes;
	}

	public void setDiskWriteBytes(Long diskWriteBytes) {
		this.diskWriteBytes = diskWriteBytes;
	}

	public Long getNetUpBytes() {
		return netUpBytes;
	}

	public void setNetUpBytes(Long netUpBytes) {
		this.netUpBytes = netUpBytes;
	}

	public Long getNetDwBytes() {
		return netDwBytes;
	}

	public void setNetDwBytes(Long netDwBytes) {
		this.netDwBytes = netDwBytes;
	}

	public static long getSerialversionuid() {
		return serialVersionUID;
	}
	
	
}
