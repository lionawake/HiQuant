from hikyuu.interactive.interactive import *
from datetime import datetime
from HiCommon import *

print('Start')
arg_list = []

arg_list.append(HikyuuArgs(80000000, blocka, ['-50,-100,-5'], 'SG_Flex', ['1,5,2', '10,20,3'], 'MM_FixedCount', ['1000,1000,1'], ['001','tactics001']))
#arg_list.append(HikyuuArgs(90000000, 'SG_Flex', [5, 10], 'MM_FixedCount', [2000], blockg, -60, '002', 'tactics002'))
#arg_list.append(HikyuuArgs(20000000, 'SG_Flex', [1, 20], 'MM_FixedCount', [3000], blocksh, -90, '003', 'tactics003'))
#arg_list.append(HikyuuArgs(30000000, 'SG_Flex', [5, 10], 'MM_FixedCount', [1000], blocksz, -100, '004', 'tactics004'))
#arg_list.append(HikyuuArgs(50000000, 'SG_Flex', [5, 60], 'MM_FixedCount', [2000], sm, -200, '005', 'tactics005'))
#arg_list.append(HikyuuArgs(60000000, 'SG_Flex', [5, 30], 'MM_FixedCount', [500],  sm, -600, '006', 'tactics006'))

start_t = datetime.now()
#a = HikyuuCommon_old(80000000, 'SG_Flex', 5, 10, 'MM_FixedCount', 10000).cycle(sm, Query(-60))
for arg in arg_list:
    a = HikyuuCommon(arg).running()

end_t = datetime.now()
t = (end_t - start_t).total_seconds()

print('Use %d second(s)'%t)
print('OK')
