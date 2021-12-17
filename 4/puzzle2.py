import bingo

dataFile = open('./input')
rawData = dataFile.read()
data = rawData.split('\n\n')

drawNums = data[0].split(',')

boardCols = 5
boardRows = 5

"""
Parses given data using the standard of white space separation.
Returns a 2d list with the parsed board
"""
def parseBoard(boardData, boardRows, boardCols):
    rows = boardData.split('\n')

    board = [[0] * boardCols for i in range(boardRows)]
    for row in range(len(rows)):
        cols = rows[row].split(' ')
        index = 0
        for i in range(len(cols)):
            if cols[i].isnumeric():
                board[row][index] = int(cols[i])
                index += 1

    return board

#Creates an array with the bingo boards
boards = [[[0] * boardCols for i in range(boardRows)] for j in range(len(data)-1)]
boards = []
for i in range(1, len(data)):
    newBingoBoard = bingo.BingoBoard(boardRows, boardCols)
    newBingoBoard.setBoard(parseBoard(data[i], boardRows, boardCols))
    boards.append(newBingoBoard)

numberSequence = bingo.BingoNumberSecuence(drawNums)

boardsLeft = len(boards)
lastBoard = bingo.BingoBoard(boardRows, boardCols)
lastBoardFound = False

for draw in range(numberSequence.length):
    number = numberSequence.drawNumber()
    
    for board in boards:
        board.checkNumber(number)

        if board.checkForWin():
            boardsLeft -= 1
            if boardsLeft <= 1:
                lastBoard = board
                lastBoardFound = True
    if lastBoardFound:
        break

lastBoardReadable = f"""
{lastBoard.board[0]}
{lastBoard.board[1]}
{lastBoard.board[2]}
{lastBoard.board[3]}
{lastBoard.board[4]}
"""
lastBoardChecksReadable = f"""
{lastBoard.checks[0]}
{lastBoard.checks[1]}
{lastBoard.checks[2]}
{lastBoard.checks[3]}
{lastBoard.checks[4]}
"""

print(lastBoardReadable)
print(lastBoardChecksReadable)

for draw in range(numberSequence.length - numberSequence.index):
    lastBoard.checkNumber(number)
    if lastBoard.checkForWin():
        score = lastBoard.calcFinalScore(number)
        print(f"Final score for last winning board is: {score}")
        break
    number = numberSequence.drawNumber()