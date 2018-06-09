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
import re
import itertools as its
import LqIndicator

class PolicyTask:
    def __init__(self, name, policyTemplate, que, sz):
        self.policyName = name
        self.template = policyTemplate
        self.que = que
        self.sz = sz

    def put_queue(self):
        c = 0
        for t in gTaskList:
            s = t[1]
            tuple_ll = []
            for f_key in gFuncTupleDict:
                if s.find(f_key) != -1:
                    tuple_ll.append(gFuncTupleDict[f_key])
                pass
            if len(tuple_ll) == 0:
                c += 1
                self.que.put(t)
                if c >= self.sz:
                    ALM("Tasks overrun: %d" % c)
                    return True
                continue
            for f in its.product(*tuple_ll):
                f_len = len(f)
                i = 0
                c += 1
                has_replace = False
                replace_str_3 = s
                while (i < f_len):
                    l = f[i].split(',')
                    if replace_str_3.find(l[0]) == -1:
                        continue
                    pat = l[0] + '\((.*?)\)'
                    global gFuncTupleStr
                    gFuncTupleStr = l[1]
                    replace_str_3 = re.sub(pat, re_replace, replace_str_3)
                    has_replace = True
                    i += 1
                if has_replace == False:
                    continue
                task = [t[0], replace_str_3]
                self.que.put(task)
                if c >= self.sz:
                    ALM("Tasks overrun: %d" % c)
                    return True
                pass
        INF("Task queue size: %d" % self.que.qsize())

    def generate(self):
        para_count = 0
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

            para_key_list = []
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
                f_p_key = para_key + func_key + '%06d'%para_count
                para_count += 1
                gFuncParaRightValueDict[f_p_key] = para_list
                #gRightValueKeyDict[func_key] = para_key
                para_key_list.append(para_key)
                remain_len -= pos_e
                remain_str = remain_str[pos_e:]
                pass
            gRightValueKeyDict[func_key] = para_key_list
            pass

        f_ll = []
        for f_key in gFuncNameDict:
            f_list = gFuncNameDict[f_key]
            f_ll.append(f_list)
            pass

        p_ll = []
        for p_key_list in gFuncParaRightValueDict:
            p_list = gFuncParaRightValueDict[p_key_list]
            p_ll.append(p_list)
            pass
        i = 0
        j = 0
        policy_count = 0
        replace_str = self.template
        for f in its.product(*f_ll):
            i = 0
            replace_str = self.template
            for f_key in gFuncNameDict:
                replace_str = replace_str.replace(f_key, f[i])
                i += 1
                pass
            for p in its.product(*p_ll):
                j = 0
                replace_str_2 = replace_str
                for f_key in gFuncNameDict:
                    if gRightValueKeyDict.__contains__(f_key) == False:
                        continue
                    p_key_list = gRightValueKeyDict[f_key]
                    for p_key in p_key_list:
                        replace_str_2 = replace_str_2.replace(p_key, str(p[j]))
                        j += 1
                    pass
                policy_count += 1
                task = [self.policyName, replace_str_2]
                gTaskList.append(task)
            pass
        #INF("Task queue size: %d"%self.que.qsize())
        self.put_queue()
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
        id = 0
        while True:
            self.lock.acquire()
            if not self.taskQue.empty():
                task = self.taskQue.get_nowait()
                id = self.taskQue.qsize()
                self.lock.release()
                policy_task_proc(task, id)
            else:
                self.lock.release()
                self.finish = True
                break
            pass

def re_replace(matched):
    return matched.group(0) + gFuncTupleStr

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
            res.append(gFuncList[n])
        else:
            min = int(t[0])
            max = int(t[1]) + 1
            r = range(min, max)
            for y in r:
                n = int(y)
                res.append(gFuncList[n])
    return res

def get_func_para_list(src):
    res = []
    if src[0] == '[':
        s = src.strip('[')
        s = s.strip(']')
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
    else:
        l = src.split(',')
        min = float(l[0])
        max = float(l[1])
        step = float(l[2])
        while (min <= max):
            res.append(round(min,3))
            min = min + step
            pass
        pass
    return res

def policy_task_proc(task, id):
    taskName = task[0]
    taskCode = task[1]
    #x = random.randint(0, 999)
    curTime = int(round(time.time() * 1000))
    policy_desc = taskName + "_%d"%curTime + "_%06d"%id
    py_file = "./tmp/%s.py" % policy_desc
    # 生成py代码文件
    py_fd = open(py_file, "w+", encoding='UTF-8')
    py_fd.write(taskCode)
    py_fd.close()
    # 执行通过替换指标函数后的py代码文件
    os.system(gPyExe + " " + py_file)
    if gTaskFileReserve == False:
        os.remove(py_file)
    pass

def get_func_doc_dict():
    for x in dir(LqIndicator):
        if callable(getattr(LqIndicator, x)) == True:
            tuple_list = []
            ret_num = 0
            gFuncDocDict[x] = getattr(LqIndicator, x).__doc__.split(',')
            func_id = int(gFuncDocDict[x][0])
            para_num = int(gFuncDocDict[x][1])
            ret_num = int(gFuncDocDict[x][2])
            if ret_num > 1:
                n = 0
                while (ret_num > 0):
                    s = '%s,'%x + '[%d]' % n
                    ret_num -= 1
                    n += 1
                    tuple_list.append(s)
                gFuncTupleDict[x] = tuple_list
        pass

def get_func_list():
    f_l = list(filter(lambda x: callable(getattr(LqIndicator, x)), dir(LqIndicator)))
    f_num = len(f_l)
    i = 0
    while (i <= f_num):
        for f in f_l:
            l = getattr(LqIndicator, f).__doc__.split(',')
            f_id = int(l[0])
            if f_id == i:
                gFuncList.append(f)
                break
        pass
        if f_id != i:
            gFuncList.append('NULL')
        i += 1
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
gTaskFileReserve = True
#gTaskFileReserve = False
# 获取StockFilter全部筛选函数
gTaskList = []
gFuncList = []
gFuncDocDict = {}
gFuncTupleDict = {}
gFuncNameDict = {}
gFuncParaRightValueDict = {}
gRightValueKeyDict = {}
#gPyExe = os.getcwd() + "\..\\venv\Scripts\python.exe"
gPyExe = "python"
gFuncTupleStr = ''
#按序号生成指标函数列表
get_func_list()
#生成多返回值指标函数字典
get_func_doc_dict()
