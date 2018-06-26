#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================
import threading
import queue
import time
from datetime import datetime
import os
import sys
import LqCommon as lqc

taskThreadNum = 4
taskQueueSize = 1000000
threadList = []
taskQueueLock = threading.Lock()
taskQueue = queue.Queue(taskQueueSize)
policyFileDefault = 'Template2.py'
policyFile = ''

def show_process_bar(end=False):
    queSzCur = taskQueue.qsize()
    percent = (queSz - queSzCur) * 100 / queSz
    nArrow = int(percent)
    nLine = 100 - nArrow
    showPercent = "\r" + "[" + ">" * nArrow + "-" * nLine + "] |%.1f" % percent + "%|"
    sys.stdout.write(showPercent)
    sys.stdout.flush()
    if end:
        print('\r\n')
    pass

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        policyFile = sys.argv[1]
    if policyFile == '':
        policyFile = policyFileDefault
    startTime = datetime.now()
    # 读取策略模板文件内容
    if not os.path.exists(policyFile):
        lqc.ERR('Template file does not exist.')
        sys.exit(-1)
    tfd = open(policyFile, 'r', encoding='UTF-8')
    policyTemplate = tfd.read()
    tfd.close()
    # 创建策略文件目录
    if not os.path.exists('./tmp'):
        os.mkdir('./tmp')
    # 通过策略模板生成策略任务队列
    ret = lqc.PolicyTask("LQPolicy", policyTemplate, taskQueue, taskQueueSize).generate()
    if ret != True:
        lqc.ERR('Policy task generate failed')
    queSz = taskQueue.qsize()
    lqc.gDBProc.save_strategy_pattern("abc", "xxx", 0, queSz, 0, policyTemplate)

    # 创建多线程列表
    i = 0
    while (i < taskThreadNum):
        thd = lqc.TaskThread(i, "TaskThread_%02d"%i, taskQueue, taskQueueLock)
        thd.start()
        threadList.append(thd)
        i += 1

    # 等待任务队列执行完毕
    while not taskQueue.empty():
        show_process_bar()
        time.sleep(1)
        pass
    show_process_bar(end=True)

    # 线程退出
    for t in threadList:
        if t.finish == True:
            t.join()

    lqc.INF("Task queue size: %d" % taskQueue.qsize())
    del taskQueueLock
    del taskQueue
    endTime = datetime.now()
    useTime = (endTime - startTime).total_seconds()
    lqc.INF('Use %d second(s)' % useTime)
    lqc.INF('OK')
lqc.INF('Policy Task Exit')
