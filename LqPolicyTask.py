#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================
import threading
import queue
import LqCommon as lqc

taskThreadNum = 8
threadList = []
taskQueueLock = threading.Lock()
taskQueue = queue.Queue(100000)

if __name__ == '__main__':
    #通过策略模板生成策略任务队列
    ret = lqc.PolicyTask(1, "LQPolicy", "", taskQueue).policyGen()
    if ret != True:
        lqc.LOG('ERR', 'Policy task generate failed')

    #创建多线程列表
    i = 0
    while (i < taskThreadNum):
        thd = lqc.TaskThread(i, "TaskThread_%02d"%i, taskQueue, taskQueueLock)
        thd.start()
        threadList.append(thd)
        i += 1

    #等待任务队列执行完毕
    while not taskQueue.empty():
        pass

    #线程退出
    for t in threadList:
        if t.finish == True:
            t.join()

    print('OK')
print('Policy Task Exit')
