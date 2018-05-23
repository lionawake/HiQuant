#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================
import threading
import queue

class PolicyTask:
    def __init__(self, id, name, policyTemplate, que):
        self.policyID = id
        self.policyName = name
        self.template = policyTemplate
        self.que = que

    def policyGen(self):
        policyStr = ""
        self.que.put(policyStr)
        return True

    def __del__(self):
        pass

class TaskThread(threading.Thread):
    def __init__(self, tid, tname, que, queLock):
        threading.Thread.__init__(self)
        self.id = tid
        self.name = tname
        self.taskQue = que
        self.finish = False
        self.lock = queLock

    def run(self):
        self.lock.acquire()
        if not self.taskQue.empty():
            task = self.taskQue.get_nowait()
            self.lock.release()
            policy_task_proc(task)
        else:
            self.finish = True
            self.lock.release()

def policy_task_proc(task):
    pass

def LOG(level, str):
    print(level + ': ' + str)

