class BingoBoard:
    def __init__(self, gridRows, gridCols) -> None:
        self.board = [[0] * gridCols for i in range(gridRows)]
        self.checks = [[False] * gridCols for i in range(gridRows)]
        self.rows = gridRows
        self.cols = gridCols

    """
    Sets the board to the inputted numbergrid
    """
    def setBoard(self, grid):
        for row in range(self.rows):
            for col in range(self.cols):
                self.board[row][col] = int(grid[row][col])

    """
    Sets a specific number on the given index of the board
    """
    def setBoardNumber(self, number, indexRow, indexCol):
        if indexRow > self.rows or indexCol > self.cols or indexRow < 0 or indexCol < 0:
            raise IndexError(f"Index needs to be positive and not bigger than [{self.rows}][{self.cols}]")
        self.board[indexRow][indexCol] = number

    """
    Resets all checks on the board
    """
    def resetChecks(self):
        self.checks = [[False] * self.cols for i in range(self.rows)]

    """
    Checks inputted number on the board if it exists and
    returns True if number is checked otherwise returns False.
    Also returns False if the number has been checked before.
    """
    def checkNumber(self, number):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == int(number) and not self.checks[row][col]:
                    self.checks[row][col] = True
                    return True
        return False
    
    """
    Checks if the board has won by covering an entire row/col.
    Returns True if win and False otherwise.
    """
    def checkForWin(self):
        #Checks for winning row
        for row in range(self.rows):
            streak = 0
            for col in range(self.cols):
                if self.checks[row][col]:
                    streak += 1
                    if streak >= self.cols:
                        return True
        
        #Checks for winning column
        for col in range(self.cols):
            streak = 0
            for row in range(self.rows):
                if self.checks[row][col]:
                    streak += 1
                    if streak >= self.rows:
                        return True
        return False

    """
    Calcultates the final score for the board according to the rules of
    score = (sum of unchecked numbers) * (winning number)
    Returns the result.
    """
    def calcFinalScore(self, number):
        #Sums all the unchecked numbers
        sumOfNumbers = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.checks[row][col]:
                    sumOfNumbers += self.board[row][col]

        #print(f"sum: {sumOfNumbers}, number: {number}")
        return sumOfNumbers*int(number)

class BingoNumberSecuence:
    def __init__(self, secuence) -> None:
        self.secuence = secuence
        self.index = 0
        self.length = len(secuence)

    """
    Resets the secuence so it starts over
    """
    def resetSecuence(self):
        self.index = 0

    """
    Draws a number from the sequence and returns drawn number
    """
    def drawNumber(self):
        number = self.secuence[self.index]
        self.index += 1
        return number