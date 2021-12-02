puzzle_input = open('AOC2ainput.txt','r')
puzlines = puzzle_input.readlines()
depth = 0
hori = 0

for i in puzlines:
    move = i.split()
    if move[0] == 'forward':
        hori = hori + int(move[1])
    elif move[0]=='up':
        depth = depth - int(move[1])
        if depth <0:
            depth = 0
    elif move[0] == 'down':
        depth = depth + int(move[1])
outcome = hori*depth
print("Depth = " + str(depth) + ". Horizontal movement = " + str(hori))
print(outcome)

