# -
import os 

import Basics_identical_exe 
import LoRa_time_Power_TDMA
import LoRa_time_power_Aloha

distant_from_real_utilizaion = 0.03

os.chdir("./sampleTasks")
# utilizations =[0.072, 0.15, 0.28, 0.41, 0.53, 0.67, 0.8, 0.94, 1.08, 1.23] # [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
utilizations =[0.072, 0.15, 0.28, 0.41, 0.67, 0.94, 1.23] # [0.05, 0.1, 0.2, 0.3, 0.5, 0.7,0.9]
# because of our type of making period (just using first 8 prime number to limit the hyper period) to get considered utilization
# we assign a number bigger than real utilization to achive that , e.g we use 0.94 to get 0.7 utilization  
util_dict = {0.072:0.05 , 0.15:0.1 , 0.28:0.2 , 0.41:0.3 , 0.53:0.4 , 0.67:0.5 , 0.8:0.6 , 0.94:0.7 , 1.08:0.8, 1.23:0.9}
# no_tasks_list = [5, 10, 15, 20, 30, 40, 50]
no_tasks_list = [5, 10, 20, 40]
counter = 0
for i in utilizations:
    for j in no_tasks_list:
        # for p in range(1,11,1):
        for p in range(1,6,1):
            counter +=1
            name_of_file = "{:03d}".format(counter) + "-" + str(j) + "_tasks_util_" + str(util_dict[i]) + "_" + str(p) + ".csv" 
            (guard, period_list, utils) = \
            Basics_identical_exe.select_period(i, j,LoRa_time_Power_TDMA.exe_time, util_dict[i], distant_from_real_utilizaion)
            if len(period_list) == 0:
                of = open(name_of_file, 'w')
                of.writelines(" operation was unsuccessful !!! ")
                of.close()
            else:
                Basics_identical_exe.make_task_list_same_exe (j, LoRa_time_Power_TDMA.exe_time, LoRa_time_power_Aloha.exe_time, period_list, name_of_file)







# utilization = 0.94
# expected_utilization = 0.7
# No_tasks = 5
# print("number of tasks is ", No_tasks)
# (guard, period_list, utils) = Basics_identical_exe.select_period(utilization, No_tasks, expected_utilization)
# if len(period_list) == 0:
#     print("Unsuccessful operation")
# else:
#     print(period_list)
#     set_periods = set(period_list)
#     print(" unique periods are : ", set_periods)
#     non_duplicate_periods = len(period_list) - len(set_periods)
#     (HP, mult, calculated_utilization ) = Basics_identical_exe.total_hyper_period(period_list)
#     print("while guard is ", guard, "No of duplicate periods", non_duplicate_periods,
#           "\n hyper period is : ", HP, "and mult is : ", mult, " and calculated utilization is : " , calculated_utilization)
#     Basics_identical_exe.make_task_list_same_exe (No_tasks, LoRa_time_Power_TDMA.exe_time, period_list, "test.csv")
    # print ("exe time on air is : ", LoRa_time_Power_TDMA.time_on_air, " and  rec is : ", LoRa_time_Power_TDMA.ack_time_on_air)

# guard = 100
# hp = 1


