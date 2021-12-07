import re
#puzzle_input = open('AOC5ainput.txt','r')
puzzle_input = open('test.txt','r')
puzlines = puzzle_input.readlines()

points = []

N = 10
line = []
grid = []
for i in range(0,N):
    line = [0]*N
    grid.append(line)

for i in puzlines:
    i = re.split(' |,|\n',i)
    del i[2]
    if len(i)>4:
        del i[4]
    points.append(i)

start = 0
end = 0
for a in points:
    if a[0]==a[2]:
        if a[1]>a[3]:
            start = int(a[3])
            end = int(a[1])
        else:
            start = int(a[1])
            end = int(a[3])
        for i in range(start,end+1):
            grid[i][int(a[0])] = int(grid[i][int(a[0])]) +1
    elif a[1]==a[3]:
        if a[0]>a[2]:
            start = int(a[2])
            end = int(a[0])
        else:
            start = int(a[0])
            end = int(a[2])
        for i in range(start,end+1):
            grid[int(a[1])][i] = int(grid[int(a[1])][i]) +1
    start = 0
    end = 0
overlap = 0

for v in range(0,len(grid)):
    print(grid[v])
    for h in range(0,len(grid)):
        if int(grid[v][h]) >1:
            overlap = overlap+1


print(overlap)
