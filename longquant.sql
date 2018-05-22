
-- 策略因子表（存储用于构建策略的指标因子）
DROP TABLE IF EXISTS lq_strategy_factor;
CREATE TABLE lq_strategy_factor (
  factor_id bigint NOT NULL AUTO_INCREMENT,
  factor_name varchar(40) NOT NULL,
  func_name varchar(40), -- 函数名
  param_num int, -- 参数个数
  param1_name varchar(20), -- 参数名
  param1_start double , -- 参数范围起始
  param1_end double, -- 参数范围结束
  param1_step double, -- 参数变化步长
  param1_default double, -- 参数默认值
  param2_name varchar(20), -- 参数名
  param2_start double , -- 参数范围起始
  param2_end double, -- 参数范围结束
  param2_step double, -- 参数变化步长
  param2_default double, -- 参数默认值
  param3_name varchar(20), -- 参数名
  param3_start double , -- 参数范围起始
  param3_end double, -- 参数范围结束
  param3_step double, -- 参数变化步长
  param3_default double, -- 参数默认值
  param4_name varchar(20), -- 参数名
  param4_start double , -- 参数范围起始
  param4_end double, -- 参数范围结束
  param4_step double, -- 参数变化步长
  param4_default double, -- 参数默认值
  param5_name varchar(20), -- 参数名
  param5_start double , -- 参数范围起始
  param5_end double, -- 参数范围结束
  param5_step double, -- 参数变化步长
  param5_default double, -- 参数默认值
  param6_name varchar(20), -- 参数名
  param6_start double , -- 参数范围起始
  param6_end double, -- 参数范围结束
  param6_step double, -- 参数变化步长
  param6_default double, -- 参数默认值
  param7_name varchar(20), -- 参数名
  param7_start double , -- 参数范围起始
  param7_end double, -- 参数范围结束
  param7_step double, -- 参数变化步长
  param7_default double, -- 参数默认值
  param8_name varchar(20), -- 参数名
  param8_start double , -- 参数范围起始
  param8_end double, -- 参数范围结束
  param8_step double, -- 参数变化步长
  param8_default double, -- 参数默认值
  PRIMARY KEY (factor_id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- 策略模板表（保存用于通过因子代换生成策略的模板）
DROP TABLE IF EXISTS lq_strategy_pattern;
CREATE TABLE lq_strategy_pattern (
  sp_id bigint NOT NULL AUTO_INCREMENT,
  sp_name varchar(32) NOT NULL,
  author varchar(32) NOT NULL,
  create_time time,
  test_status int,
  task_total bigint, -- 分解出的任务总数
  task_finished bigint, -- 已执行的任务数
  code varchar(30000),
  PRIMARY KEY (sp_id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- 策略表（保存从模板产生的具体策略）
DROP TABLE IF EXISTS lq_strategy;
CREATE TABLE lq_strategy (
  sp_id bigint NOT NULL,
  s_id bigint NOT NULL AUTO_INCREMENT,
  code varchar(30000) NOT NULL,
  data_path varchar(255) NOT NULL,
  net_profit double , -- 净利润
  total_profit double, -- 总盈利
  total_loss double, -- 总亏损
  total_profit_loss double, -- 总盈利/总亏损
  trade_lot int, -- 交易手数
  profit_ratio double, -- 盈利比率
  average_profit double, -- 平均利润
  average_loss double, -- 平均亏损
  average_profit_loss double, -- 平均盈利/平均亏损
  max_profit double, -- 最大盈利
  max_loss double, -- 最大亏损
  max_total_profit double, -- 最大盈利/总盈利
  max_total_loss double, -- 最大亏损/总亏损
  average_hold_period int, -- 平均持仓周期
  max_fund_use double, -- 最大使用资金
  yield_rate double, -- 收益率
  annual_return double, -- 年化收益率
  effect_yield double, -- 有效收益率
  benefit_risk_ratio double, -- 收益风险比
  adj_benefit_risk_ratio double, -- 调整收益风险比
  r_square_yield_curve double, -- 收益曲线R平方值
  sharpe_ratio double, -- 夏普比率
  total_trans_time int, -- 总交易时间
  hold_period_ratio double, -- 持仓时间比率
  max_retrace_value double, -- 最大资产回撤值
  max_retrace_ratio double，-- 最大资产回撤值比率
  PRIMARY KEY (sp_id,s_id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- 策略回测表（保存一条策略针对一个标的执行回测的结果，回测过程中的交易指令保存在文件中，文件路径存在data_path中）
DROP TABLE IF EXISTS lq_strategy_test;
CREATE TABLE lq_strategy_test (
  sp_id bigint NOT NULL,
  s_id bigint NOT NULL,
  stock varchar(16) NOT NULL,
  data_path varchar(255) NOT NULL,
  test_time time, -- 回测完成的时间
  net_profit double , -- 净利润
  total_profit double, -- 总盈利
  total_loss double, -- 总亏损
  total_profit_loss double, -- 总盈利/总亏损
  trade_lot int, -- 交易手数
  profit_ratio double, -- 盈利比率
  average_profit double, -- 平均利润
  average_loss double, -- 平均亏损
  average_profit_loss double, -- 平均盈利/平均亏损
  max_profit double, -- 最大盈利
  max_loss double, -- 最大亏损
  max_total_profit double, -- 最大盈利/总盈利
  max_total_loss double, -- 最大亏损/总亏损
  average_hold_period int, -- 平均持仓周期
  max_fund_use double, -- 最大使用资金
  yield_rate double, -- 收益率
  annual_return double, -- 年化收益率
  effect_yield double, -- 有效收益率
  benefit_risk_ratio double, -- 收益风险比
  adj_benefit_risk_ratio double, -- 调整收益风险比
  r_square_yield_curve double, -- 收益曲线R平方值
  sharpe_ratio double, -- 夏普比率
  total_trans_time int, -- 总交易时间
  hold_period_ratio double, -- 持仓时间比率
  max_retrace_value double, -- 最大资产回撤值
  max_retrace_ratio double，-- 最大资产回撤值比率
  PRIMARY KEY (sp_id,s_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 策略留存表（存储回测效果好的策略备用）
DROP TABLE IF EXISTS lq_strategy_saved;
CREATE TABLE lq_strategy_saved (
  sp_id bigint NOT NULL,
  s_id bigint NOT NULL,
  code varchar(30000) NOT NULL,
  data_path varchar(255) NOT NULL,
  test_time time, -- 回测完成的时间
  net_profit double , -- 净利润
  total_profit double, -- 总盈利
  total_loss double, -- 总亏损
  total_profit_loss double, -- 总盈利/总亏损
  trade_lot int, -- 交易手数
  profit_ratio double, -- 盈利比率
  average_profit double, -- 平均利润
  average_loss double, -- 平均亏损
  average_profit_loss double, -- 平均盈利/平均亏损
  max_profit double, -- 最大盈利
  max_loss double, -- 最大亏损
  max_total_profit double, -- 最大盈利/总盈利
  max_total_loss double, -- 最大亏损/总亏损
  average_hold_period int, -- 平均持仓周期
  max_fund_use double, -- 最大使用资金
  yield_rate double, -- 收益率
  annual_return double, -- 年化收益率
  effect_yield double, -- 有效收益率
  benefit_risk_ratio double, -- 收益风险比
  adj_benefit_risk_ratio double, -- 调整收益风险比
  r_square_yield_curve double, -- 收益曲线R平方值
  sharpe_ratio double, -- 夏普比率
  total_trans_time int, -- 总交易时间
  hold_period_ratio double, -- 持仓时间比率
  max_retrace_value double, -- 最大资产回撤值
  max_retrace_ratio double，-- 最大资产回撤值比率
  PRIMARY KEY (sp_id,s_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 策略交易表（存储用于实盘交易的策略）
DROP TABLE IF EXISTS lq_strategy_trade;
CREATE TABLE lq_strategy_trade (
  sp_id bigint NOT NULL,
  s_id bigint NOT NULL,
  code varchar(30000) NOT NULL,
  data_path varchar(255) NOT NULL,
  start_time time, -- 启用交易的时间
  block varchar(255), -- 股票池
  funds double, -- 投入资金
  net_profit double , -- 净利润
  total_profit double, -- 总盈利
  total_loss double, -- 总亏损
  total_profit_loss double, -- 总盈利/总亏损
  trade_lot int, -- 交易手数
  profit_ratio double, -- 盈利比率
  average_profit double, -- 平均利润
  average_loss double, -- 平均亏损
  average_profit_loss double, -- 平均盈利/平均亏损
  max_profit double, -- 最大盈利
  max_loss double, -- 最大亏损
  max_total_profit double, -- 最大盈利/总盈利
  max_total_loss double, -- 最大亏损/总亏损
  average_hold_period int, -- 平均持仓周期
  max_fund_use double, -- 最大使用资金
  yield_rate double, -- 收益率
  annual_return double, -- 年化收益率
  effect_yield double, -- 有效收益率
  benefit_risk_ratio double, -- 收益风险比
  adj_benefit_risk_ratio double, -- 调整收益风险比
  r_square_yield_curve double, -- 收益曲线R平方值
  sharpe_ratio double, -- 夏普比率
  total_trans_time int, -- 总交易时间
  hold_period_ratio double, -- 持仓时间比率
  max_retrace_value double, -- 最大资产回撤值
  max_retrace_ratio double，-- 最大资产回撤值比率
  PRIMARY KEY (sp_id,s_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 任务状态表
DROP TABLE IF EXISTS lq_task_stat;
CREATE TABLE lq_task_stat (
  task_wait bigint NOT NULL,
  task_run bigint NOT NULL,
  task_over bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 系统负载表
DROP TABLE IF EXISTS lq_sysload;
CREATE TABLE lq_sysload (
  sample_time time NOT NULL,
  cpu_ratio int NOT NULL,
  mem_ratio int NOT NULL,
  mem_cost int NOT NULL,
  disk_ratio int NOT NULL,
  disk_read_bytes bigint NOT NULL,
  disk_write_bytes bigint NOT NULL,
  net_up_bytes bigint NOT NULL,
  net_dw_bytes bigint NOT NULL,
  PRIMARY KEY (sample_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 用户表
DROP TABLE IF EXISTS lq_user;
CREATE TABLE lq_user (
  userid int NOT NULL AUTO_INCREMENT,
  username varchar(32) NOT NULL,
  password varchar(40) NOT NULL,
  type int NOT NULL, -- 0=管理员，1=普通用户
  last_login time, -- 最后登录时间
  PRIMARY KEY (userid)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- 操作日志表
DROP TABLE IF EXISTS lq_task_stat;
CREATE TABLE lq_task_stat (
  act_time time NOT NULL,
  username varchar(32) NOT NULL,
  oper_log varchar(40) NOT NULL,
  PRIMARY KEY (act_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
