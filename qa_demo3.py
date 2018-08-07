import os
import sys

cwd = os.getcwd()
sys.path.append(cwd)

print("Demo:".ljust(15), cwd)
#sys.path.append(cwd)
import LqDB_QA as lqdb

db = lqdb.SqlDB('192.168.54.11', 3306, 'root', 'lq2018', 'lq')
db.save_strategy_test(10000, 1, 0, "000001", cwd, 0)
