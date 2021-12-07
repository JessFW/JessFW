import re
puzzle_input = open('AOC5ainput.txt','r')
#puzzle_input = open('test.txt','r')
puzlines = puzzle_input.readlines()

N = 1000
grid = []
start = 0
end= 0
ydir = 0
xdir = 0

for i in range (0,N):
    grid.append([0]*N)

for i in puzlines:
    i = re.split(',| -> |\n',i)
    if int(i[0]) == int(i[2]):
        if int(i[1])>int(i[3]):
            start = int(i[3])
            end = int(i[1])
        else:
            start = int(i[1])
            end = int(i[3])
        for v in range(start,end+1):
            grid[v][int(i[0])] = grid[v][int(i[0])]+1
    elif int(i[1]) == int(i[3]):
        if int(i[0]) > int(i[2]):
            start = int(i[2])
            end = int(i[0])
        else:
            start = int(i[0])
            end = int(i[2])
        for h in range(start, end + 1):
            grid[int(i[1])][h] = grid[int(i[1])][h] + 1
    #adding diagonals from part 2
    elif abs(int(i[0])-int(i[2]))== abs(int(i[1])-int(i[3])):
        if int(i[1]) > int(i[3]):
            ydir = -1
        else:
            ydir = 1
        if int(i[0]) > int(i[2]):
           xdir = -1
        else:
            xdir = 1
        #start at one, move down and across for each till reaches other
        for b in range(0,abs(int(i[0])-int(i[2]))+1):
            grid[int(i[1])+b*ydir][int(i[0])+b*xdir] = grid[int(i[1])+b*ydir][int(i[0])+b*xdir]+1



overlap = 0
for v in range(0,N):
    print(grid[v])
    for h in range(0,N):
        if grid[v][h]>=2:
            overlap = overlap+1
print(overlap)