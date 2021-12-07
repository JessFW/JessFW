import re
import math
puzzle_input = open('AOC7ainput.txt','r')
#puzzle_input = open('test.txt','r')
puzlines = puzzle_input.readlines()

crab = []
for i in puzlines:
    crab = re.split(',',i)

fuel = 0
move = [0]*int(max(crab))
for p in range(0,int(max(crab))):
    for s in range(0,len(crab)):
        fuel=fuel+((abs(int(crab[s])-p))**2+abs(int(crab[s])-p))/2
    move[p] = fuel
    fuel = 0
best = min(move)
print(best)
