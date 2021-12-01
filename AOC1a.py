# Code for advent of code problem 1a
puzzle_input = open('AOC1ainput.txt','r')
puzlines = puzzle_input.readlines()
prevval = 0
lmeasure = 0

for i in puzlines:
    i.strip()
    num = int(i)
    if prevval == 0:
        print(str(num) + ': no previous measurement')
    elif prevval < num:
        print(str(num) + ': increased')
        lmeasure = lmeasure+1
    else:
        print(str(num) + ': decreased')
    prevval = num

print("total increased = " + str(lmeasure))