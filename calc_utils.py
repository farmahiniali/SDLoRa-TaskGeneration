# -
import os 
import re 
import math
import LoRa_time_Power_TDMA  

safety_guard = 0.5

time_to_get_err_by_sg = {0.1:3758, 0.2:8201, 0.3:13327, 0.4:19137, 0.5:25630}

def util_sync_in_per(period,sg):
    num_needed_sync = math.ceil(float(period)/time_to_get_err_by_sg[sg])
    time_of_sync_in_per = num_needed_sync * LoRa_time_Power_TDMA.sync_tx_rx_time
    return time_of_sync_in_per

# --------------  when we want to seperate utilization content in on field of csv  ----------------

# dir = r'D:\Course\PHD\UT\Papers\LoRa\Tool\Python\TimeCompTDMA_Aloha\TaskGenerator\TaskGenerator_same_exeTime\sampleTasks'
# files = os.listdir(dir)
# os.chdir(dir)
# for file in files:
#     with open(file, 'r') as f:
#         lines = f.readlines()
#     with open (file, 'w') as f:
#         pat = r".*:\s\d\.\d*"
#         for line in lines: 
#             utils = re.findall(pat,line)
#             if len(utils) > 0:
#                 tmp =line.split(':')
#                 tmp[1] = tmp[1].strip()
#                 row = tmp[0] + ',' + tmp[1] + '\n'
#                 f.writelines(row)
#             else:
#                 f.writelines(line)

#  ---------------------------------------------------------------------------------------------------------

dir = r'D:\Course\PHD\UT\Papers\LoRa\Tool\Python\TimeCompTDMA_Aloha\TaskGenerator\TaskGenerator_same_exeTime\sampleTasks'
files = os.listdir(dir)
os.chdir(dir)
for file in files:
    with open(file, 'r') as f:
        lines = f.readlines()
    with open (file, 'w') as f:
        td_util = 0 
        al_util = 0 
        as_util = 0
        if len(lines) > 0:
            for line in lines: 
                elements =line.split(',')
                td_util += float(elements[1]) / float(elements[2])
                al_util += float(elements[5]) / float(elements[6])
                as_util += util_sync_in_per(elements[2], safety_guard) / float(elements[2])
                # row = line + '\n'
                f.writelines(line)
        as_util += td_util
        new_rows = "\n\n\n utilization without safty guard is : ," + str(al_util) + \
            "\n utilization after adding safety guard is : ," + str(td_util) + \
                " \n new utilization after sysnchronization is : ," + str(as_util)
        f.writelines(new_rows)



