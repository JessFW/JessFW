puzzle_input = open('AOC3ainput.txt','r')
puzlines = puzzle_input.readlines()
mbits = [0]*12
lbits = [0]*12
more = [0]*12
indt = 0
ind = 0
gamma = 0
episilon = 0

for i in puzlines:
    i = i.strip()
    bits = [int(a)for a in str(i)]
    for x in bits:
        if x ==1:
            more[ind] = more[ind]+1
        else:
            more[ind] = more[ind]-1
        ind = ind+1
    ind = 0

for i in more:
    if more[indt] > 0:
         mbits[indt] = 1
         lbits[indt] = 0
    else:
        mbits[indt] = 0
        lbits[indt] = 1
    indt = indt+1

for b in range(0,len(mbits)):
    gamma = gamma + mbits[b]*(2**(12-(b+1)))
    episilon = episilon + lbits[b] * (2 ** (12 - (b + 1)))

power = gamma*episilon
print("the power is = "+ str(power))
