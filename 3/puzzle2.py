dataFile = open('./input', 'r')
data = dataFile.read()

sampleData = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

data = data.split('\n')

binaryGrid = [[0] * len(data[0]) for i in range(len(data))]
for i in range(len(data)):
    for j in range(len(data[i])):
        binaryNum = data[i]
        binaryGrid[i][j] = (binaryNum[j:j+1])

#print(binaryGrid)

generatorRating = []
scrubberRating = []

def gridFlip(grid):
    flippedGrid = [[0] * len(grid) for i in range(len(grid[0]))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            flippedGrid[j][i]
    return flippedGrid

flippedGrid = gridFlip(binaryGrid)

#Takes a binaryGrid and adds the most common bit to the given binaryArray while eliminating the least common rows from the grid.
def recursivePriority(grid, binaryNum):
    if len(grid[0]) <= 0:
        return

    mostCommon = 0
    newGridRows = 0
    count0 = 0
    count1 = 0
    for i in range(len(grid)):
        if int(grid[i][0]) == 0:
            count0 += 1
        else:
            count1 += 1
    
    #print("count0: " + str(count0) + " count1: " + str(count1))
    if count0 > count1:
        mostCommon = 0
        newGridRows = count0
    else:
        mostCommon = 1
        newGridRows = count1

    newGridCounter = 0
    newGrid = [[0] * (len(grid[0])-1) for i in range(newGridRows)]
    for i in range(len(grid)):
        if int(grid[i][0]) == mostCommon:
            #print("newGrid got a value")
            for j in range(len(grid[i])-1):
                newGrid[newGridCounter][j] = int(grid[i][j+1])
            newGridCounter += 1
    
    #print(str(newGrid) + " : " + str(mostCommon))
    binaryNum.append(mostCommon)
    recursivePriority(newGrid, binaryNum)

def recursiveMinority(grid, binaryNum):
    if len(grid[0]) <= 0:
        return
    if len(grid) <= 1:
        for i in range(len(grid[0])):
            binaryNum.append(grid[0][i])
        return

    leastCommon = 0
    newGridRows = 0
    count0 = 0
    count1 = 0
    for i in range(len(grid)):
        if int(grid[i][0]) == 0:
            count0 += 1
        else:
            count1 += 1
    
    #print("count0: " + str(count0) + " count1: " + str(count1))
    if count0 <= count1:
        leastCommon = 0
        newGridRows = count0
    else:
        leastCommon = 1
        newGridRows = count1

    newGridCounter = 0
    newGrid = [[0] * (len(grid[0])-1) for i in range(newGridRows)]
    for i in range(len(grid)):
        if int(grid[i][0]) == leastCommon:
            #print("newGrid got a value")
            for j in range(len(grid[i])-1):
                newGrid[newGridCounter][j] = int(grid[i][j+1])
            newGridCounter += 1
    
    #print(str(newGrid) + " : " + str(leastCommon))
    binaryNum.append(leastCommon)
    recursiveMinority(newGrid, binaryNum)

generatorRating = []
recursivePriority(binaryGrid, generatorRating)

scrubberRating = []
recursiveMinority(binaryGrid, scrubberRating)

print(generatorRating)
print(scrubberRating)

generatorRatingDec = int("".join(str(i) for i in generatorRating), 2)
scrubberRatingDec = int("".join(str(i) for i in scrubberRating), 2)

print("Generator Rating: " + str(generatorRatingDec) + " Scrubber Rating: " + str(scrubberRatingDec) + " Life Support Rating: " + str(generatorRatingDec*scrubberRatingDec))