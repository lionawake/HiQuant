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
import LqCommon as lqc

taskThreadNum = 4
taskQueueSize = 1000000
threadList = []
taskQueueLock = threading.Lock()
taskQueue = queue.Queue(taskQueueSize)

policyTemplate = "# -*- coding: utf8 -*-\n" \
                 "from LqCommon import StockFilter\n" \
                 "#from hikyuu.interactive.interactive import *\n" \
                 "#FPDF:  function parameters default value\n" \
                 "#FPDFL: function parameters default value list\n" \
                 "sf = StockFilter('') \n" \
                 "if sf.$$F:[1-3,8]$() > $$P:[10-12,15]$ and" \
                 " sf.$$F:[9,10]$() <= 3000:\n" \
                 "    if sf.$$F:[3-6,12]$() == $$P:[888,999]$:\n" \
                 "        pass\n" \
                 "    else:\n" \
                 "        pass\n" \
                 "else:\n" \
                 "    pass\n" \
                 "pass\n"

if __name__ == '__main__':
    startTime = datetime.now()
    # 创建策略文件目录
    if not os.path.exists('./tmp'):
        os.mkdir('./tmp')
    # 通过策略模板生成策略任务队列
    ret = lqc.PolicyTask("LQPolicy", policyTemplate, taskQueue, taskQueueSize).generate()
    if ret != True:
        lqc.ERR('Policy task generate failed')

    # 创建多线程列表
    i = 0
    while (i < taskThreadNum):
        thd = lqc.TaskThread(i, "TaskThread_%02d"%i, taskQueue, taskQueueLock)
        thd.start()
        threadList.append(thd)
        i += 1

    # 等待任务队列执行完毕
    print('[', end='')
    while not taskQueue.empty():
        print('>', end='')
        time.sleep(1)
        pass
    print(']')
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
