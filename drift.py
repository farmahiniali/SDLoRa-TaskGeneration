
import math

max_drift_per_crystal = 2  # the unit is PPM
crystal_freq = 1  # unit is MHz
ppm_in_crystal_rate = max_drift_per_crystal * crystal_freq
time_of_err_per_second_by_ppm_in_crystal_rate = ppm_in_crystal_rate / 1000000  # unit is second
time_of_err_per_second_by_ppm_in_crystal_rate_change_unit_to_ms = time_of_err_per_second_by_ppm_in_crystal_rate * 1000  # unit is milli second
amount_of_error_in_a_milli_second_by_drift_unit_ms = time_of_err_per_second_by_ppm_in_crystal_rate_change_unit_to_ms / 1000  # unit is milli second
center_freq_of_transmit = 433  # the unit is MHz
drift_per_center_freq = math.ceil(center_freq_of_transmit * max_drift_per_crystal)

def modify_drift_by_temperature(temperature):
    if temperature < -20 or temperature > 60:
        return -1000
    else:
        normal_temperature = 25
        diff_temperature_to_normal = temperature - normal_temperature
        return diff_temperature_to_normal * 10 / 25

def needed_num_sync_periods_for_drift_2_time_to_get_err(node_period, node_exe, safety_guard_of_exe):
    acceptable_err_drift = (node_exe * safety_guard_of_exe) / 2 # this value present amount of error that is accptable,
    # we divide it by 2 because we must consider plus/minus of this error and unit is ms
    
    #time_to_get_err_by_drift = math.floor(acceptable_err_drift / amount_of_error_in_a_milli_second_by_drift_unit_ms) - 1  # multiply in 1000 is
    time_to_get_err_by_drift = math.floor(acceptable_err_drift / time_of_err_per_second_by_ppm_in_crystal_rate_change_unit_to_ms) - 1  # multiply in 1000 is
    
    
    #  for converting to ms because 'acceptable_err_drift' unit is ms and 'time_of_err_per_milli_second_by_drift' unit
    # is ns and result of division is micro second  and -1 for ensuring that we surely befor node become un-synced
    # we synchronize it in this example result for 121 ms exe is : (6ms(err_drift) / 150ns (err_of_drift)* 1000 = 40000ms
    if time_to_get_err_by_drift > node_period:
        return 0  # , 0  # means to need to sync before next period, and there is not time to get error
    else:
        return math.floor(node_period / time_to_get_err_by_drift) 

x = needed_num_sync_periods_for_drift_2_time_to_get_err (10000,205.055999999999,0.5)
print(x)