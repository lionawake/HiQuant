package cn.wd.sup.dao.dto.custom;

import com.zxt.framework.mvc.dao.Domain;
/**
 * 操作日志表 lq_task_stat
 * @author zhengkai
 *
 */
public class LqTaskStat extends Domain{

	/**
	 * 序列化id
	 */
	private static final long serialVersionUID = 1L;

	private Long taskWait;
	
	private Long taskRun;
	
	private Long taskOver;

	public Long getTaskWait() {
		return taskWait;
	}

	public void setTaskWait(Long taskWait) {
		this.taskWait = taskWait;
	}

	public Long getTaskRun() {
		return taskRun;
	}

	public void setTaskRun(Long taskRun) {
		this.taskRun = taskRun;
	}

	public Long getTaskOver() {
		return taskOver;
	}

	public void setTaskOver(Long taskOver) {
		this.taskOver = taskOver;
	}

	public static long getSerialversionuid() {
		return serialVersionUID;
	}
	
	
}
