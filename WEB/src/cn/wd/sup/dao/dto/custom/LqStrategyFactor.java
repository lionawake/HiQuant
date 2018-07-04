package cn.wd.sup.dao.dto.custom;

import java.sql.Timestamp;

import com.zxt.framework.mvc.dao.Domain;

/**
 * 策略因子表（存储用于构建策略的指标因子） lq_strategy_factor
 * @author zhengkai
 *
 */
public class LqStrategyFactor extends Domain{

	/**
	 * 序列化id
	 */
	private static final long serialVersionUID = 1L;
	
	/**
	 * 因子id
	 */
	private Long factor_id;
	
	/**
	 * 因子描述
	 */
	private String factor_desc;
	
	/**
	 * 类型
	 */
	private Integer type;
	
	/**
	 * 代码
	 */
	private String code;
	
	/**
	 * 函数名
	 */
	private String func_name;
	
	/**
	 * 参数个数
	 */
	private Integer param_num;
	
	/**
	 * 参数名
	 */
	private String param1_name;
	
	/**
	 * 参数范围起始
	 */
	private Double param1_start;
	
	/**
	 * 参数范围结束
	 */
	private Double param1_end;
	
	/**
	 * 参数变化步长
	 */
	private Double param1_step;
	
	/**
	 * 参数默认值
	 */
	private Double param1_default;

	/**
	 * 参数名
	 */
	private String param2_name;
	
	/**
	 * 参数范围起始
	 */
	private Double param2_start;
	
	/**
	 * 参数范围结束
	 */
	private Double param2_end;
	
	/**
	 * 参数变化步长
	 */
	private Double param2_step;
	
	/**
	 * 参数默认值
	 */
	private Double param2_default;

	/**
	 * 参数名
	 */
	private String param3_name;
	
	/**
	 * 参数范围起始
	 */
	private Double param3_start;
	
	/**
	 * 参数范围结束
	 */
	private Double param3_end;
	
	/**
	 * 参数变化步长
	 */
	private Double param3_step;
	
	/**
	 * 参数默认值
	 */
	private Double param3_default;

	/**
	 * 参数名
	 */
	private String param4_name;
	
	/**
	 * 参数范围起始
	 */
	private Double param4_start;
	
	/**
	 * 参数范围结束
	 */
	private Double param4_end;
	
	/**
	 * 参数变化步长
	 */
	private Double param4_step;
	
	/**
	 * 参数默认值
	 */
	private Double param4_default;

	/**
	 * 参数名
	 */
	private String param5_name;
	
	/**
	 * 参数范围起始
	 */
	private Double param5_start;
	
	/**
	 * 参数范围结束
	 */
	private Double param5_end;
	
	/**
	 * 参数变化步长
	 */
	private Double param5_step;
	
	/**
	 * 参数默认值
	 */
	private Double param5_default;

	/**
	 * 参数名
	 */
	private String param6_name;
	
	/**
	 * 参数范围起始
	 */
	private Double param6_start;
	
	/**
	 * 参数范围结束
	 */
	private Double param6_end;
	
	/**
	 * 参数变化步长
	 */
	private Double param6_step;
	
	/**
	 * 参数默认值
	 */
	private Double param6_default;

	/**
	 * 参数名
	 */
	private String param7_name;
	
	/**
	 * 参数范围起始
	 */
	private Double param7_start;
	
	/**
	 * 参数范围结束
	 */
	private Double param7_end;
	
	/**
	 * 参数变化步长
	 */
	private Double param7_step;
	
	/**
	 * 参数默认值
	 */
	private Double param7_default;

	/**
	 * 参数名
	 */
	private String param8_name;
	
	/**
	 * 参数范围起始
	 */
	private Double param8_start;
	
	/**
	 * 参数范围结束
	 */
	private Double param8_end;
	
	/**
	 * 参数变化步长
	 */
	private Double param8_step;
	
	/**
	 * 参数默认值
	 */
	private Double param8_default;
	
	/**
	 * 创建时间
	 */
	private Timestamp create_time;
	
	/**
	 * 作者
	 */
	private String author;
	

	public Long getFactor_id() {
		return factor_id;
	}

	public void setFactor_id(Long factor_id) {
		this.factor_id = factor_id;
	}

	public String getFactor_desc() {
		return factor_desc;
	}

	public void setFactor_desc(String factor_desc) {
		this.factor_desc = factor_desc;
	}

	public String getFunc_name() {
		return func_name;
	}

	public void setFunc_name(String func_name) {
		this.func_name = func_name;
	}

	public Integer getParam_num() {
		return param_num;
	}

	public void setParam_num(Integer param_num) {
		this.param_num = param_num;
	}

	public String getParam1_name() {
		return param1_name;
	}

	public void setParam1_name(String param1_name) {
		this.param1_name = param1_name;
	}

	public Double getParam1_start() {
		return param1_start;
	}

	public void setParam1_start(Double param1_start) {
		this.param1_start = param1_start;
	}

	public Double getParam1_end() {
		return param1_end;
	}

	public void setParam1_end(Double param1_end) {
		this.param1_end = param1_end;
	}

	public Double getParam1_step() {
		return param1_step;
	}

	public void setParam1_step(Double param1_step) {
		this.param1_step = param1_step;
	}

	public Double getParam1_default() {
		return param1_default;
	}

	public void setParam1_default(Double param1_default) {
		this.param1_default = param1_default;
	}

	public String getParam2_name() {
		return param2_name;
	}

	public void setParam2_name(String param2_name) {
		this.param2_name = param2_name;
	}

	public Double getParam2_start() {
		return param2_start;
	}

	public void setParam2_start(Double param2_start) {
		this.param2_start = param2_start;
	}

	public Double getParam2_end() {
		return param2_end;
	}

	public void setParam2_end(Double param2_end) {
		this.param2_end = param2_end;
	}

	public Double getParam2_step() {
		return param2_step;
	}

	public void setParam2_step(Double param2_step) {
		this.param2_step = param2_step;
	}

	public Double getParam2_default() {
		return param2_default;
	}

	public void setParam2_default(Double param2_default) {
		this.param2_default = param2_default;
	}

	public String getParam3_name() {
		return param3_name;
	}

	public void setParam3_name(String param3_name) {
		this.param3_name = param3_name;
	}

	public Double getParam3_start() {
		return param3_start;
	}

	public void setParam3_start(Double param3_start) {
		this.param3_start = param3_start;
	}

	public Double getParam3_end() {
		return param3_end;
	}

	public void setParam3_end(Double param3_end) {
		this.param3_end = param3_end;
	}

	public Double getParam3_step() {
		return param3_step;
	}

	public void setParam3_step(Double param3_step) {
		this.param3_step = param3_step;
	}

	public Double getParam3_default() {
		return param3_default;
	}

	public void setParam3_default(Double param3_default) {
		this.param3_default = param3_default;
	}

	public String getParam4_name() {
		return param4_name;
	}

	public void setParam4_name(String param4_name) {
		this.param4_name = param4_name;
	}

	public Double getParam4_start() {
		return param4_start;
	}

	public void setParam4_start(Double param4_start) {
		this.param4_start = param4_start;
	}

	public Double getParam4_end() {
		return param4_end;
	}

	public void setParam4_end(Double param4_end) {
		this.param4_end = param4_end;
	}

	public Double getParam4_step() {
		return param4_step;
	}

	public void setParam4_step(Double param4_step) {
		this.param4_step = param4_step;
	}

	public Double getParam4_default() {
		return param4_default;
	}

	public void setParam4_default(Double param4_default) {
		this.param4_default = param4_default;
	}

	public String getParam5_name() {
		return param5_name;
	}

	public void setParam5_name(String param5_name) {
		this.param5_name = param5_name;
	}

	public Double getParam5_start() {
		return param5_start;
	}

	public void setParam5_start(Double param5_start) {
		this.param5_start = param5_start;
	}

	public Double getParam5_end() {
		return param5_end;
	}

	public void setParam5_end(Double param5_end) {
		this.param5_end = param5_end;
	}

	public Double getParam5_step() {
		return param5_step;
	}

	public void setParam5_step(Double param5_step) {
		this.param5_step = param5_step;
	}

	public Double getParam5_default() {
		return param5_default;
	}

	public void setParam5_default(Double param5_default) {
		this.param5_default = param5_default;
	}

	public String getParam6_name() {
		return param6_name;
	}

	public void setParam6_name(String param6_name) {
		this.param6_name = param6_name;
	}

	public Double getParam6_start() {
		return param6_start;
	}

	public void setParam6_start(Double param6_start) {
		this.param6_start = param6_start;
	}

	public Double getParam6_end() {
		return param6_end;
	}

	public void setParam6_end(Double param6_end) {
		this.param6_end = param6_end;
	}

	public Double getParam6_step() {
		return param6_step;
	}

	public void setParam6_step(Double param6_step) {
		this.param6_step = param6_step;
	}

	public Double getParam6_default() {
		return param6_default;
	}

	public void setParam6_default(Double param6_default) {
		this.param6_default = param6_default;
	}

	public String getParam7_name() {
		return param7_name;
	}

	public void setParam7_name(String param7_name) {
		this.param7_name = param7_name;
	}

	public Double getParam7_start() {
		return param7_start;
	}

	public void setParam7_start(Double param7_start) {
		this.param7_start = param7_start;
	}

	public Double getParam7_end() {
		return param7_end;
	}

	public void setParam7_end(Double param7_end) {
		this.param7_end = param7_end;
	}

	public Double getParam7_step() {
		return param7_step;
	}

	public void setParam7_step(Double param7_step) {
		this.param7_step = param7_step;
	}

	public Double getParam7_default() {
		return param7_default;
	}

	public void setParam7_default(Double param7_default) {
		this.param7_default = param7_default;
	}

	public String getParam8_name() {
		return param8_name;
	}

	public void setParam8_name(String param8_name) {
		this.param8_name = param8_name;
	}

	public Double getParam8_start() {
		return param8_start;
	}

	public void setParam8_start(Double param8_start) {
		this.param8_start = param8_start;
	}

	public Double getParam8_end() {
		return param8_end;
	}

	public void setParam8_end(Double param8_end) {
		this.param8_end = param8_end;
	}

	public Double getParam8_step() {
		return param8_step;
	}

	public void setParam8_step(Double param8_step) {
		this.param8_step = param8_step;
	}

	public Double getParam8_default() {
		return param8_default;
	}

	public void setParam8_default(Double param8_default) {
		this.param8_default = param8_default;
	}

	public static long getSerialversionuid() {
		return serialVersionUID;
	}

	public Integer getType() {
		return type;
	}

	public void setType(Integer type) {
		this.type = type;
	}

	public String getCode() {
		return code;
	}

	public void setCode(String code) {
		this.code = code;
	}

	public Timestamp getCreate_time() {
		return create_time;
	}

	public void setCreate_time(Timestamp create_time) {
		this.create_time = create_time;
	}

	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}
	
}
