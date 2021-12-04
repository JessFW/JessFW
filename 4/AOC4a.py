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
winboard = 0
sumhori = 0
sumvert = 0
end = False
#find and mark a match of the board
for c in puzlines:
    for t in range(0,len(allboard)):
        for m in range(0,5):
            for b in range(0,5):
                if end :
                    break

                if int(allboard[t][m][b]) == int(c):
                    allboard[t][m][b] = -1
                for y in range(0, 5):
                    sumvert = sumvert + int(allboard[t][y][b])
                    sumhori = sumhori + int(allboard[t][m][y])
                if sumvert == -5 or sumhori ==-5:  # found vertical
                    winnum = int(c)
                    winboard = int(t)
                    end = True
                    break
                sumvert = 0
                sumhori = 0
            if end :
                break
        if end:
            break
    if end:
        break

points = 0
#work out points
for v in allboard[winboard]:
    for l in v:
        if int(l)>=0:
            points = points+int(l)
points = points*winnum
print("the winning points are = " + str(points))