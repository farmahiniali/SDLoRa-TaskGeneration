# - 
import os 
import re 


SG = 0.5
dir = r'D:\Course\PHD\UT\Papers\LoRa\Tool\Python\TimeCompTDMA_Aloha\TaskGenerator\TaskGenerator_same_exeTime\sampleTasks_few\SG_0.5'
files = os.listdir(dir)
files = files[:len(files) - 2]
os.chdir(dir)

pat1 = 'without'
pat2 = 'safety'
pat3 = 'sysnc'

with open ("utilization.csv", 'a') as out:
    header = "num of tasks, task id, nominal util, util w/o SG, util w SG, util after sync, schedulable, life time, total cor msg\n"
    out.writelines(header)
for file in files:
    tasks_att = file.split('-')[1].split('_')
    num_task = tasks_att[0]
    nominal_util = tasks_att[3]
    task_id = tasks_att[4].split('.')[0]
    with open(file, 'r') as f:
        lines = f.readlines()
    for line in lines: 
        tmp1 = re.findall(pat1,line)
        tmp2 = re.findall(pat2,line)
        tmp3 = re.findall(pat3,line)
        if len(tmp1) > 0: 
            util_wo ="{:.2f}".format(float(line.split(',')[1].strip('\n')))
        if len(tmp2) > 0: 
            util_wsg = "{:.2f}".format(float(line.split(',')[1].strip('\n')))
        if len(tmp3) > 0: 
            util_sync = "{:.2f}".format(float(line.split(',')[1].strip('\n')))
            if float(util_sync) > 1.0:
                schedulability = False     
            else:
                schedulability = True               
    with open ("utilization.csv", 'a') as out:
        row = str(num_task) + ',' + str(task_id) + ',' + str(nominal_util) + ',' + \
            str(util_wo) + ',' + str(util_wsg) + ',' + str(util_sync) + ',' + str(schedulability) + '\n'
        out.writelines(row)
td_path = dir + "\\TDMA"
os.chdir(td_path)
files = os.listdir(td_path)
lf = []
cm = []
for file in files:
    with open (file, 'r') as f:
        lines = f.readlines()
    cor_msg = 0
    life_time = '1000000.0' # this number for life time is too much 
    for line in lines: 
        cor_msg += int(line.split(',')[1])
        life_time_tmp = "{:.2f}".format(float(line.split(',')[2]))
        if float(life_time_tmp) < float(life_time):
            life_time = life_time_tmp
    cm.append(str(cor_msg))
    lf.append(life_time)
out_file_path = dir + "\\utilization.csv"
with open (out_file_path, 'r') as f_out: 
    lines = f_out.readlines()
with open (out_file_path, 'w') as f_out:
    f_out.writelines(lines[0])
    lines = lines[1:]
    line_counter = 0
    for line in lines: 
        row = line.strip('\n') + ',' + lf[line_counter] + ',' + cm[line_counter] + '\n'
        f_out.writelines(row)
        line_counter +=1 
