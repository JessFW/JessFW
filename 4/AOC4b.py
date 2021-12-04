#get input from the text files
puzzle_input = open('AOC4ainputlist.txt','r')
board_input = open('AOC4ainputboard.txt','r')
#board_input = open('test.txt','r')
puzlines = puzzle_input.readlines()
boards = board_input.readlines()
puzlines = puzlines[0].split(',') #get the list of number called and into a list
#puzlines = [1,2,3,4,5]

#store the information
currentboard = []
allboard = []

#split the board data into a list of lists of lists [][][]
for i in boards:
    line = i.split()
    if i !='\n':
        currentboard.append(line)
    else:
        allboard.append(currentboard)
        currentboard = []

#allboard.append(currentboard)
winnum = 0
winboard = []
sumhori = 0
sumvert = 0
alreadywin = []
newwin= True
points = 0

#find and mark a match of the board
for c in puzlines:
    for t in range(0,len(allboard)):
        for m in range(0,5):
            for b in range(0,5):
                if int(allboard[t][m][b]) == int(c):
                    allboard[t][m][b] = -1 #mark found values as negative 1
                for y in range(0, 5):
                    sumvert = sumvert + int(allboard[t][y][b])
                    sumhori = sumhori + int(allboard[t][m][y])

                if sumvert == -5 or sumhori ==-5:  # found vertical
                    if bool(alreadywin)==True:
                        for w in alreadywin:
                            if w == int(t):
                                newwin = False
                                break
                    if newwin: #if it is a new win work out the points  - stop all found
                        for v in allboard[int(t)]: #find the sum of the non found values
                            for l in v:
                                if int(l) >= 0:
                                    points = points + int(l)
                        points = points * int(c)
                        print("the winning points are = " + str(points))
                        points = 0
                        alreadywin.append(int(t))
                    newwin = True
                sumvert = 0
                sumhori = 0
