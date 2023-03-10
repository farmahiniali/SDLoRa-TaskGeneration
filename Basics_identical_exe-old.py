import os 

import random
import math
from re import T
import drift
import prime_multipliers 
import LoRa_time_Power_TDMA  

# ----- global variables -------------
while_guard = 100
hyper_period_limit = 4000000
max_period_limit = 450000
# min_period_limit = 100
fix_exe_time = 1  # unit is milli second and in real scenario we know that fix_exe_time is at least 40ms
# since the utilization = e/p1 + e/p2 + ... + e/pn and in this problem exe time is same for all utilization fraction,
# so we can factorize exe from numerator of fraction => utilization = e (1/p1 + 1/p2 + ... + 1/pn) and for
# simplification we can assume exe time is equal to 1 so we have utilization = 1/p1 + 1/p2 + ... + 1/pn so that this
# simplification lead to decrease hyper period (LCM of periods)

file_prime_mat = "prime_mat_450-000.txt"
# mat = prime_multipliers.make_prime_matrix(max_period_limit) # making once prime matrix and use it many
of = open(file_prime_mat, "r")
mat = str(of.readlines()).strip("[").strip("]").strip("\'")
mat = mat.split(",")
mat = [int(x) for x in mat] 

# ------------ numbers under 1000 which  

# ------------ UUnifast functions ---------------
# to make sure that numerator of fractions do not get too small, at first I share 10 percent of utilization among all
def utilization_func(u, No_tasks):
    u_set = []
    sum_u = u - (u * 0.4)
    for i in range(No_tasks - 1):
        next_sum_u = sum_u * pow(random.uniform(0, 1), 1.0/(No_tasks - i))
        util_nominate = sum_u - next_sum_u + ((u * 0.1) / No_tasks)# in this statement i add (u * 0.1)/No_task to each fraction
        u_set.append(float("{:.6f}".format(util_nominate)))
        sum_u = next_sum_u
    u_set.append(sum_u + ((u * 0.1) / No_tasks))
    return u_set


# ---------- compute LCM -----------
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


# ------------ make periods ------------------------------------
def select_period(utilization_value, No_tasks, TDMA_exe_time, expected_util, dist_of_real_util):  # input parameter is overall utilization
    # prime matrix is made at the first of this module as 'mat'    
    while_guard = 100
    util_interval_ok = False
    util_over = True 
    while while_guard > 0 and (not util_interval_ok or util_over):
        util_over = False
        periods = []
        period_divide_exe = []
        utilization_arr = utilization_func(utilization_value, No_tasks)
        calc_util = 0 
        for i in range(len(utilization_arr)):
            temp_period = int(1.0 / utilization_arr[i]) # at now we assume exe-time is unit (1.0) to obtain nearest number in next step 
            temp_period = prime_multipliers.nearest_num(temp_period, mat)
            period_divide_exe.append(temp_period)
            correct_period_with_exe_TDMA = int(temp_period * TDMA_exe_time)
            periods.append(correct_period_with_exe_TDMA) 
            calc_util += float( 1.0 / temp_period) # even though the correct period is in correct_period_with_exe_TDMA but for util 
            # we can still use temp_period 
        while_guard -= 1
        if calc_util > 1 : # it means utilization is more than 1 that is unacceptable 
            util_over = True
        if abs(calc_util - expected_util) < dist_of_real_util:
            util_interval_ok = True
        # util_interval_ok = calc_util_ok(period_divide_exe, expected_util, 0.03)
    if while_guard > 0: 
        return while_guard, periods, utilization_arr
    else: 
        return (-1,[],[])
    # if length of list is 0 it means the function could not find some valid values for periods


# ---------  check real and final utilization ------------------------
def calc_util_ok(periods, expected_util, acceptable_interval):
    fin_period = 0
    for i in range(len(periods)):
        fin_period += float(1.0 / periods[i])
    if abs(fin_period - expected_util) <= acceptable_interval:
        return True
    else:
        False

# --------- calculate Total hyper Period -------------------
def total_hyper_period(period_list):
    hp = 1
    mult = 1
    calculated_util = 0
    for i in range(len(period_list)):
        mult *= int(period_list[i])
        calculated_util += float(float(1)/period_list[i])
        gcd_res = math.gcd(hp, int(period_list[i]))
        hp = int((hp * int(period_list[i])) / gcd_res)
    return hp, mult, calculated_util


# --------------- make tasks  ------------------------

def make_task_list_same_exe (No_tasks, TDMA_exe_time, Aloha_exe_time, period_list, output_file):
    f = open(output_file,'w')
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
    f.close()
                
















