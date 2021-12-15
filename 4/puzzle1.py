dataFile = open('./input')
rawData = dataFile.read()
data = rawData.split('\n\n')

drawNums = data[0].split(',')

boardCol = 5
boardRow = 5
boards = [[[0] * boardCol for i in range(boardRow)] for j in range(len(data)-1)]
boardsChecked = [[[False] * boardCol for i in range(boardRow)] for j in range(len(data)-1)]

def parseBoards(boardData, boards):
    for i in range(1, len(boardData)):
        boardRow = boardData[i].split('\n')
        for j in range(len(boardRow)):
            boardNum = boardRow[j].split(' ')
            #print(boardNum)
            index = 0
            for n in range(len(boardNum)):
                #print(f"i: {i} j: {j} n: {n} index: {index}")
                if not boardNum[n].isdigit():
                    continue
                boards[i-1][j][index] = boardNum[n]
                index += 1

def checkBoardForWin(boardChecked):
    #Check rows for win
    for row in boardChecked:
        for col in range(len(row)):
            if not row[col]:
                break
            elif col >= len(row)-1:
                return True
    
    #Check columns for win
    for col in range(len(boardChecked[0])):
        for row in range(len(boardChecked)):
            if not boardChecked[row][col]:
                break
            elif row >= len(boardChecked)-1:
                return True
    
    return False

def putCheckOnBoardsWithNumber(boards, boardsChecked, num):
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            for col in range(len(boards[board][row])):
                #print(f"Number is: {num}")
                #print(boards[board][row][col])
                if int(boards[board][row][col]) == int(num):
                    #print("Board got checked")
                    boardsChecked[board][row][col] = True

def drawNumber(numbers, index):
    return numbers[index]

def calcFinalScore(board, boardChecked, num):
    score = 0
    #print(boardChecked)
    for row in range(len(boardChecked)):
        for col in range(len(boardChecked[row])):
            #print(boardChecked[row][col])
            if not boardChecked[row][col]:
                #print(board[row][col])
                score += int(board[row][col])
    
    return score*int(num)

parseBoards(data, boards)
winningBoard = 0
winningNum = 0

for draw in range(len(boards)):
    number = drawNumber(drawNums, draw)
    putCheckOnBoardsWithNumber(boards, boardsChecked, number)
    print(f"Draw nr: {draw}")
    
    for board in range(len(boards)):
        if checkBoardForWin(boardsChecked[board]):
            print(f"Board: {board} won at draw: {draw}")
            winningBoard = board
            winningNum = number
            break
    if winningNum and winningBoard:
        break

#print(boardsChecked)

print(f"The final score is: {calcFinalScore(boards[winningBoard], boardsChecked[winningBoard], winningNum)}")

lastBoard = 0
lastBoardHasWon = False
lastWinningNum = 0
boardHasWon = []
winningBoards = 0
for i in range(len(boards)):
    boardHasWon.append(False)

for draw in range(len(boards)):
    number = drawNumber(drawNums, draw)
    putCheckOnBoardsWithNumber(boards, boardsChecked, number)
    print(f"Draw nr: {draw}")
    
    for board in range(len(boards)):
        if checkBoardForWin(boardsChecked[board]):
            boardHasWon[board] = True
            winningBoards += 1

            if lastBoard == board:
                lastBoardHasWon = True
                break

            if winningBoards >= len(boardHasWon)-1:
                for i in range(len(boardHasWon)):
                    if not boardHasWon[i]:
                        lastBoard = i
                        print(f"Last board is {lastBoard}")
                        lastWinningNum = number
                        break
    
    if lastBoard and lastBoardHasWon:
        break

print(f"The final score for the last board is {calcFinalScore(boards[lastBoard], boardsChecked[lastBoard], lastWinningNum)}")