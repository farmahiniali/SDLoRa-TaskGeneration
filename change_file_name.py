import os 

dir = r'D:\Course\PHD\UT\Papers\LoRa\Tool\Python\TimeCompTDMA_Aloha\TaskGenerator\TaskGenerator_same_exeTime\sampleTasks-SG0.3'
files = os.listdir(dir)
os.chdir(dir)
for file in files:
    name = file.split('-')
    if len(name[0]) == 1:
        name[0] = "00" + name[0]
        new_name = name[0] + "-" + name[1]
        os.rename(file, new_name)
    elif len(name[0]) == 2:
        name[0] = "0" + name[0]
        new_name = name[0] + "-" + name[1]
        os.rename(file, new_name)
    
