dataFile = open('./input', 'r')
rawData = dataFile.read()

#rawData = """2199943210
#3987894921
#9856789892
#8767896789
#9899965678"""

data = rawData.split('\n')

grid = []
for row in data:
    grid.append(list(row))

#print(grid)

def checkAdjacent(grid, row, col):
    if row-1 >= 0:
        above = int(grid[row-1][col])
    else:
        above = 10
    if col-1 >= 0:
        left = int(grid[row][col-1])
    else:
        left = 10
    if col+1 < len(grid[0]):
        right = int(grid[row][col+1])
    else:
        right = 10
    if row+1 < len(grid):
        below = int(grid[row+1][col])
    else:
        below = 10
    current = int(grid[row][col])

    checks = [above, left, right, below]
    for check in checks:
        if check <= current:
            return False
    
    return True

def recursiveCheck(grid, row, col, calls, direction):
    calls.append([row, col])
    if row-1 >= 0 and direction != 4:
        above = int(grid[row-1][col])
    else:
        above = -1
    if col-1 >= 0 and direction != 3:
        left = int(grid[row][col-1])
    else:
        left = -1
    if col+1 < len(grid[0]) and direction != 2:
        right = int(grid[row][col+1])
    else:
        right = -1
    if row+1 < len(grid) and direction != 1:
        below = int(grid[row+1][col])
    else:
        below = -1
    current = int(grid[row][col])

    checks = [above, left, right, below]
    for check in range(len(checks)):
        if (checks[check]-1 == current or checks[check] == current) and checks[check] != 9 and checks[check] != -1:
            if check == 0:
                recursiveCheck(grid, row-1, col, calls, 1)
            elif check == 1:
                recursiveCheck(grid, row, col-1, calls, 2)
            elif check == 2:
                recursiveCheck(grid, row, col+1, calls, 3)
            elif check == 3:
                recursiveCheck(grid, row+1, col, calls, 4)
    
basins = []
lowPoints = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        #print(f"Row: {row} Col: {col}")
        if checkAdjacent(grid, row, col):
            calls = []
            lowPoints.append(int(grid[row][col]))
            recursiveCheck(grid, row, col, calls, 0)
            for call in calls:
                count = calls.count(call)
                if count > 1:
                    for i in range(count-1):
                        calls.remove(call)
            basins.append(len(calls))

print(f"Low points are {lowPoints}")

riskLevel = 0
for point in lowPoints:
    riskLevel += point+1
print(f"Risk level: {riskLevel}")

basins.sort()
biggestBasins = [basins[len(basins)-1], basins[len(basins)-2], basins[len(basins)-3]]
print(f"Product of three biggest basins = {biggestBasins[0]*biggestBasins[1]*biggestBasins[2]}")