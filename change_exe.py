# - 
import LoRa_time_Power_TDMA
import os 

dir = r'D:\Course\PHD\UT\Papers\LoRa\Tool\Python\TimeCompTDMA_Aloha\TaskGenerator\TaskGenerator_same_exeTime\sampleTasks_few\SG_0.5'
files = os.listdir(dir)
os.chdir(dir)
for file in files:
    with open(file, 'r') as f:
        lines = f.readlines()
    with open (file, 'w') as f:
        for line in lines: 
            if line == '\n':
                break
            elements = line.split(',')
            elements[1] = str(LoRa_time_Power_TDMA.exe_time)
            tmp = ""
            for j in elements:
                tmp += j  + ','
            tmp = tmp[:len(tmp) -1 ] 
            f.writelines(tmp)
