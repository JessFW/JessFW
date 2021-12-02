puzzle_input = open('AOC2ainput.txt','r')
puzlines = puzzle_input.readlines()
depth = 0
hori = 0
aim = 0

for i in puzlines:
    move = i.split()
    if move[0] == 'forward':
        hori = hori + int(move[1])
        depth = depth + aim*int(move[1])
    elif move[0]=='up':
        aim = aim - int(move[1])
    elif move[0] == 'down':
        aim = aim + int(move[1])
outcome = hori*depth
print("Depth = " + str(depth) + ". Horizontal movement = " + str(hori)+". Aim = " + str(aim))
print(outcome)

