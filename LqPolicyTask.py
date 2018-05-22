import threading

taskThreadNum = 8

class TaskThread(threading.Thread):
    def __init__(self, tid, tname, taskList):
        threading.Thread.__init__(self)
        self.id = tid
        self.name = tname
        self.taskList = taskList

    def run(self):
        pass


threadList = []
taskListList = []
if __name__ == '__main__':
    #创建多线程列表
    i = 0
    while (i < taskThreadNum):
        if len(taskListList) <= i:
            break
        thd = TaskThread(i, "TaskThread_%02d"%i, taskListList[i])
        threadList.append(thd)
        i += 1

print('OK')
