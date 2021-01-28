import sys, timeit
from random import randint

def transposeFull(I, O, x, y, dx, dy):
    if (dx == dy  and dx <= 32):
        for ny in range (y, y+dy):
            for nx in range(x, x+dx):
                O[nx][ny] = I[ny][nx]
    elif (dx >= dy):
        midx = dx // 2
        transposeFull(I, O, x, y, midx, dy)
        transposeFull(I, O, x + midx, y, dx - midx, dy)
    else:
        midy = dy // 2
        transposeFull(I, O, x, y, dx, midy)
        transposeFull(I, O, x, y + midy, dx, dy - midy)

def transpose(I,O):
    transposeFull(I, O, 0, 0, len(I[0]), len(I)) 
    
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