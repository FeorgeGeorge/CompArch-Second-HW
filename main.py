import sys, os

num = int(sys.argv[1])
up_bound = int(sys.argv[2])

classes = ['naive', 'oblivious']

configFile = open("Project/Data/config.txt", "w")
configFile.write(str(num))

configFile.write("\n")
configFile.write(str(up_bound)) 

configFile.close()

for my_class in classes:
    for i in range(num):
        os.system("pypy3 Project/{0}.py Project/Data/{0}Data/{0}{1}.csv {2}".format(my_class, i, up_bound))

