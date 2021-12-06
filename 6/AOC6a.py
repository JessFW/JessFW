import re
puzzle_input = open('AOC6ainput.txt','r')
puzlines = puzzle_input.readlines()
fish = []
fishpoints = [0]*9
#clear data
for i in puzlines:
    fish = re.split(',|\n',i)
    del fish[-1]

#work out growth relationship
for l in fish:
    fishpoints[int(l)] = fishpoints[int(l)]+1

fishzero = 0
for d in range(0,256):
    fishzero = fishpoints[0]
    for l in range(0,len(fishpoints)-1):
        fishpoints[l] = fishpoints[l+1]
    fishpoints[-1]= fishzero
    fishpoints[6]= fishpoints[6]+fishzero
    print(d)
#number of fish
print(sum(fishpoints))
