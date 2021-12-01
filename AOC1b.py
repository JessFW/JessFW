# Code for advent of code problem 1a
puzzle_input = open('AOC1ainput.txt','r')
puzlines = puzzle_input.readlines()
prevval = 0
lmeasure = 0

for i in range(0,len(puzlines)-2):
    numtop = int(puzlines[i].strip())
    nummid = int(puzlines[i+1].strip())
    numbot = int(puzlines[i+2].strip())
    swindow3sum = numtop+nummid+numbot
    if prevval == 0:
        print(str(swindow3sum) + ': no previous measurement')
    elif prevval < swindow3sum:
        print(str(swindow3sum) + ': increased')
        lmeasure = lmeasure+1
    else:
        print(str(swindow3sum) + ': decreased')
    prevval = swindow3sum

print("total increased = " + str(lmeasure))