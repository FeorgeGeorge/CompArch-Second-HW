import matplotlib.pyplot as plt
import numpy as np
import os
print("Start\n Collecting configuration...")
configFile = open("Project/Data/config.txt")


configList = []
for line in configFile:
    configList.append(int(line))

configFile.close()
print("Configuration collected!")

START = 1
LIMIT = configList[1]*10**3
STEP = 100

AMOUNT = LIMIT//STEP
NUM = configList[0]

print("Collectiong Data...")
fullData = [[], []] # naive[], oblivious[]

directory = ["naive", "oblivious"]
for i in range(2):
    counter = 0
    directoryString = "Project/Data/{}Data/".format(directory[i])
    findir = os.fsdecode(directoryString)
    for fileName in os.listdir(findir):
        newData = []
        if (not fileName.endswith(".csv")):
            continue
        counter +=1
        if counter > NUM: 
            break
        my_file = open(directoryString + fileName, "r")
        
        for num in my_file:
            newData.append(float(num))
        my_file.close()
        
        fullData[i].append(newData)

print("Data collected!")

print("Drawing the Graph...")
times = [[], []]
for j in range(2):
    for i in range(AMOUNT):
        smol_list = []    
        for x in range(NUM):
            smol_list.append(fullData[j][x][i])
        times[j].append(np.average(np.array(smol_list)))
     
times = [np.array(times[0]), np.array(times[1])]

[plt.plot([i for i in range(START, LIMIT, STEP)], times[j]) for j in range(2)]
plt.legend(["oblivious", "naive"])
plt.savefig("Project/evm_{0}_{1}.png".format(configList[0], configList[1]))

print("Graph drawn! \n Finish.")