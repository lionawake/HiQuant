#!/usr/bin/python
# -*- coding: utf8 -*-
#==============================================================================
# written by fuxuanhuang
#==============================================================================
import os
import threading
import queue
import time
import random
import itertools as its

class StockFilter:
    '筛选公共类'
    def __init__(self, stock):
        #print(self.__doc__)
        pass
    def __del__(self):
        pass

    def stock_filter000(self):
        return 1000

    def stock_filter001(self):
        return 1000

    def stock_filter002(self):
        return 100

    def stock_filter003(self):
        return 1

    def stock_filter004(self):
        return 1

    def stock_filter005(self):
        return 1

    def stock_filter006(self):
        return 1

    def stock_filter007(self):
        return 1

    def stock_filter008(self):
        return 1

    def stock_filter009(self):
        return 1

    def stock_filter010(self):
        return 1

    def stock_filter011(self):
        return 1

    def stock_filter012(self):
        return 1

class PolicyTask:
    def __init__(self, name, policyTemplate, que, sz):
        self.policyName = name
        self.template = policyTemplate
        self.que = que
        self.sz = sz

    def generate(self):
        remain_str = self.template
        str_len = len(self.template)
        remain_len = str_len
        pos_s = 0
        pos_e = 0
        while (remain_len > 0):
            cut_res = str_cut('$$F:', '$', remain_str)
            if cut_res == -1:
                break
            pos_s = cut_res[0]
            pos_e = cut_res[1]
            func_list = get_func_name_list(remain_str[pos_s:pos_e])
            pos_s -= 4
            pos_e += 1
            func_key = remain_str[pos_s:pos_e]
            gFuncNameDict[func_key] = func_list
            remain_len -= pos_e
            remain_str = remain_str[pos_e:]

            para_list_list = []
            while (remain_len > 0):
                pos_f = remain_str.find('$$F:')
                pos_p = remain_str.find('$$P:')
                if pos_p < 0:
                    break
                if pos_f > 0 and pos_p > 0 and pos_f <= pos_p:
                    break
                cut_res = str_cut('$$P:', '$', remain_str)
                if cut_res == -1:
                    break
                pos_s = cut_res[0]
                pos_e = cut_res[1]
                para_list = get_func_para_list(remain_str[pos_s:pos_e])
                pos_s -= 4
                pos_e += 1
                para_key = remain_str[pos_s:pos_e]
                gRightValuieDict[para_key] = para_list
                gRightValueKeyDict[func_key] = para_key
                remain_len -= pos_e
                remain_str = remain_str[pos_e:]
                pass
            pass

        f_ll = []
        for f_key in gFuncNameDict:
            f_list = gFuncNameDict[f_key]
            f_ll.append(f_list)
            pass

        p_ll = []
        for p_key in gRightValuieDict:
            p_list = gRightValuieDict[p_key]
            p_ll.append(p_list)
            pass

        i = 0
        j = 0
        policy_count = 0
        replace_str = self.template
        for l in its.product(*f_ll):
            i = 0
            policy_count += 1
            replace_str = self.template
            for f_key in gFuncNameDict:
                replace_str = replace_str.replace(f_key, l[i])
                i += 1
                pass
            for p in its.product(*p_ll):
                j = 0
                replace_str_2 = replace_str
                for f_key in gFuncNameDict:
                    if gRightValueKeyDict.__contains__(f_key) == False:
                        continue
                    p_key = gRightValueKeyDict[f_key]
                    replace_str_2 = replace_str_2.replace(p_key, str(p[j]))
                    j += 1
                    pass
                task = [self.policyName, replace_str_2]
                self.que.put(task)
                if policy_count >= self.sz:
                    ALM("Tasks overrun: %d"%policy_count)
                    return True
                pass
            pass
        INF("Task queue size: %d"%self.que.qsize())
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
        while True:
            self.lock.acquire()
            if not self.taskQue.empty():
                task = self.taskQue.get_nowait()
                self.lock.release()
                policy_task_proc(task)
                #print('.', end='')
            else:
                self.lock.release()
                self.finish = True
                break
            pass

def str_cut(start, end, src):
    s = src.find(start)
    if s >= 0:
        s += len(start)
        e = src.find(end, s)
        if e >= 0:
            return [s, e]
    return -1

def get_func_name_list(src):
    s = src.strip('[')
    s = s.strip(']')
    res = []
    l = s.split(',')
    for x in l:
        t = x.split('-')
        if len(t) == 1:
            n = int(t[0])
            res.append(gStockFuncList[n])
        else:
            min = int(t[0])
            max = int(t[1]) + 1
            r = range(min, max)
            for y in r:
                n = int(y)
                res.append(gStockFuncList[n])
    return res

def get_func_para_list(src):
    s = src.strip('[')
    s = s.strip(']')
    res = []
    l = s.split(',')
    for x in l:
        t = x.split('-')
        if len(t) == 1:
            if t[0].isdigit():
                n = int(t[0])
                res.append(n)
            else:
                res.append(x.strip())
        else:
            if t[0].isdigit() and t[1].isdigit():
                min = int(t[0])
                max = int(t[1]) + 1
                r = range(min, max)
                for y in r:
                    n = int(y)
                    res.append(n)
            else:
                res.append(x.strip())
    return res

def policy_task_proc(task):
    taskName = task[0]
    taskCode = task[1]
    x = random.randint(0, 999)
    curTime = int(round(time.time() * 1000))
    policy_desc = taskName + "_%d_" % curTime + "%03d"%x
    py_file = "./tmp/%s.py" % policy_desc
    # 生成py代码文件
    py_fd = open(py_file, "w+")
    py_fd.write(taskCode)
    py_fd.close()
    # 执行通过替换指标函数后的py代码文件
    os.system(gPyExe + " " + py_file)
    if gTaskFileReserve == False:
        os.remove(py_file)
    pass

def LOG(level, str):
    if level == 0:
        h = '[ERR]'
    elif level == 1:
        h = '[ALM]'
    elif level == 2:
        h = '[INF]'
    else:
        h = '[LOG]'
    print(h + str)
    pass

def ERR(str):
    LOG(0, str)
    pass

def ALM(str):
    LOG(1, str)
    pass

def INF(str):
    LOG(2, str)
    pass

# 是否保留新生成的策略模板代码文件
gTaskFileReserve = False
# 获取StockFilter全部筛选函数
gStockFuncList = list(filter(lambda x: x.startswith('stock_filter') and callable(getattr(StockFilter, x)), dir(StockFilter)))
gFuncNameDict = {}
gRightValuieDict = {}
gRightValueKeyDict = {}
gPyExe = os.getcwd() + "\\venv\Scripts\python.exe"
