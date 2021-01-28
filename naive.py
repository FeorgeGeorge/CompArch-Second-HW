import sys, timeit
from random import randint

def transpose(I,O):
    for y in range(len(I)):
        for x in range(len(I[0])): 
            O[y][x] = I[x][y]    

if __name__ == '__main__':
   
    fileName = sys.argv[1]
    upper = int(sys.argv[2])*10**3 # 12*10**3
    step = 100
    count = 0
    myFile = open(fileName, 'w')
    for i in range(1, upper, step):
        a = [[randint(0,2) for x in range(i)] for y in range(i)]
        b = [[0 for x in range(i)] for y in range(i)]
        before = timeit.default_timer()
        transpose(a, b)
        myFile.write(str(timeit.default_timer() - before))
        myFile.write("\n")
        count += 1
        print(count)

        
