# -
import os 

sys.path.append('D:/Course/PHD/UT/Papers/LoRa/Tool/Python/TimeCompTDMA_Aloha/System/TDMA')
import drift
import Node
node = Node.NodeTDMA(-1,70000,125,Basics_identical_exe.No_exe_slot)

import Basics_identical_exe 

# distant_from_real_utilizaion = 0.03

# --------------- make tasks  ------------------------

def make_task_list_same_exe (No_tasks, TDMA_exe_time, Aloha_exe_time, period_list, output_file):
    with open (output_file,'w') as f:
    #f = open(output_file,'w')
        calculated_util_default_period = 0
        calculated_util_new_period = 0
        needed_num_period = 0 
        Aloha_util = 0
        amount_add_time_for_sync = LoRa_time_Power_TDMA.sync_ready_time_on_air + LoRa_time_Power_TDMA.sync_rec_time_on_air
        for i in range(No_tasks):
            needed_num_period = drift.needed_num_sync_periods_for_drift_2_time_to_get_err(period_list[i], TDMA_exe_time, LoRa_time_Power_TDMA.safety_guard)
            accumulate_period = float(TDMA_exe_time / period_list[i])
            Aloha_util +=  float(Aloha_exe_time / period_list[i])
            if needed_num_period > 0:
                new_needed_period = needed_num_period * amount_add_time_for_sync
                accumulate_period += float(new_needed_period / period_list[i]) 
            # task = [id, exe, period]
            task = "{},{},{},{},{},{},{}\n".format(i, TDMA_exe_time, period_list[i], "", "", Aloha_exe_time, period_list[i])
            f.writelines(task)
            calculated_util_default_period += float(TDMA_exe_time / period_list[i])
            calculated_util_new_period += accumulate_period
        print_calculated_util = "\n\n\n utilization without safty guard is : " + str(Aloha_util) + \
            " \n utilization after adding safety guard is : " + str(calculated_util_default_period) +\
            " \n new utilization after sysnchronization is : " + str(calculated_util_new_period) 
        f.writelines(print_calculated_util)
    #f.close()
                

# -------------------------------------------------------


os.chdir("./sampleTasks")
utilizations = [0.05]#, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
no_task_list = 2#10 # for each pair (util,no_node) we choose 10 different task list for (0.05, 5) 1-[0.01, 0.01, 0.01, 0.01, 0.01] 2-[0.005, 0.005,0. 005, 0.005, 0.03] 
no_nodes = [5]#, 10, 20, 40]
counter = 0
for i in utilizations:
    for j in range(no_task_list):
        # for p in range(1,11,1):
        for p in no_nodes:
            counter +=1
            name_of_file = "{:03d}".format(counter) + "-" + str(j) + "_tasks_util_" + str(i) + "_" + str(p) + ".csv" 
            (guard, period_list,period_by_timeSlot, utils) = \
            Basics_identical_exe.select_period(i, p,Basics_identical_exe.No_exe_slot, Basics_identical_exe.time_slot)#, utilizations[i](1.1), utilizations[i](0.1))
            if len(period_list) == 0:
                of = open(name_of_file, 'w')
                of.writelines(" operation was unsuccessful !!! ")
                of.close()
            else:
                Basics_identical_exe.make_task_list_same_exe (j, node.effExe, node.exe_wo_ack, period_list, name_of_file)







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


