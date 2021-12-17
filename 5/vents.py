import math

class vent:
    def __init__(self, startx, starty, endx, endy) -> None:
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        self.start = [startx, starty]
        self.end = [endx, endy]

    """
    Calculates which points on the grid the vent covers
    and returns a list of coordinates
    """
    def getCoverage(self):
        coverage = []
        
        if self.startx == self.endx:
            for i in range(abs(self.endy-self.starty)+1):
                if self.endy > self.starty:
                    coverage.append([self.startx, self.starty+i])
                else:
                    coverage.append([self.startx, self.starty-i])
        elif self.starty == self.endy:
            for i in range(abs(self.endx-self.startx)+1):
                if self.endx > self.startx:
                    coverage.append([self.startx+i, self.starty])
                else:
                    coverage.append([self.startx-i, self.starty])
        else:
            for i in range(abs(self.endy-self.starty)+1):
                if self.endx > self.startx and self.endy > self.starty:
                    coverage.append([self.startx+i, self.starty+i])
                elif self.endx < self.startx and self.endy > self.starty:
                    coverage.append([self.startx-i, self.starty+i])
                elif self.endx > self.startx and self.endy < self.starty:
                    coverage.append([self.startx+i, self.starty-i])
                elif self.endx < self.startx and self.endy < self.starty:
                    coverage.append([self.startx-i, self.starty-i])

        return coverage

class mapGrid:
    def __init__(self, maxX, maxY) -> None:
        self.grid = [[0] * int(maxX) for i in range(int(maxY))]
        self.maxX = maxX
        self.maxY = maxY

    def displayGrid(self):
        display = ""
        displayData = []
        for row in range(self.maxY):
            for col in range(self.maxX):
                displayData.append(str(self.grid[row][col]))
            displayData.append('\n')
        display = display.join(displayData)
        print(display)

    def saveGridToFile(self, fileName):
        display = ""
        displayData = []
        for row in range(self.maxY):
            for col in range(self.maxX):
                displayData.append(str(self.grid[row][col]))
            displayData.append('\n')
        display = display.join(displayData)

        gridFile = open(fileName, 'w')
        gridFile.write(display)
        gridFile.close()
    
    def getNumberOfDangerPoints(self):
        dangerPoints = 0
        for row in self.grid:
            for col in row:
                if col > 1:
                    dangerPoints += 1
        
        return dangerPoints