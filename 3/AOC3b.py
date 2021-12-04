puzzle_input = open('AOC3ainput.txt','r')
puzlines = puzzle_input.readlines()

opuz = puzlines
cpuz = puzlines

more = 0
ind = 0


while len(opuz)>1:
    for i in opuz:
        i = i.strip()
        bits = [int(a)for a in str(i)]
        if bits[ind] ==1:
            more = more+1
        else:
            more = more-1
    pastopus = opuz
    opuz = []
    for x in pastopus:
        x = x.strip()
        bits = [int(a) for a in str(x)]
        if more >= 0 and bits[ind]==1:
            opuz.append(x)
        elif more < 0 and bits[ind]==0:
            opuz.append(x)
    ind = ind+1
    more = 0

ind = 0
while len(cpuz)>1:
    for i in cpuz:
        i = i.strip()
        bits = [int(a)for a in str(i)]
        if bits[ind] ==1:
            more = more+1
        else:
            more = more-1
    pastcpus = cpuz
    cpuz = []
    for x in pastcpus:
        x = x.strip()
        bits = [int(a) for a in str(x)]
        if more >= 0 and bits[ind]==0:
            cpuz.append(x)
        elif more < 0 and bits[ind]==1:
            cpuz.append(x)
    ind = ind+1
    more = 0

oxy = 0
co=0
oxybits = [int(a) for a in str(opuz[0])]
cobits = [int(a) for a in str(cpuz[0])]
for b in range(0,len(oxybits)):
    oxy = oxy + oxybits[b]*(2**(12-(b+1)))

for b in range(0,len(cobits)):
    co = co + cobits[b]*(2**(12-(b+1)))

lifesupport = oxy*co
print("The life support value = "+str(lifesupport))
