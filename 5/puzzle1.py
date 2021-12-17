import vents

dataFile = open('./input', 'r')
rawData = dataFile.read()

testData = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
data = rawData.split('\n')

def parseVent(data):
    ventData = data.split('->')
    start = ventData[0].split(',')
    end = ventData[1].split(',')

    vent = vents.vent(int(start[0]), int(start[1]), int(end[0]), int(end[1]))
    return vent

ventList = []
for vent in range(len(data)):
    ventList.append(parseVent(data[vent]))

maxX = 0
maxY = 0

for i in range(len(ventList)):
    if ventList[i].startx > maxX:
        maxX = ventList[i].startx
    if ventList[i].endx > maxX:
        maxX = ventList[i].endx

for i in range(len(ventList)):
    if ventList[i].starty > maxY:
        maxY = ventList[i].starty
    if ventList[i].endy > maxY:
        maxY = ventList[i].endy

grid = vents.mapGrid(maxX+10, maxY+10)

for vent in ventList:
    #if vent.startx != vent.endx and vent.starty != vent.endy:
       # continue
    coverage = vent.getCoverage()
    for i in coverage:
        grid.grid[i[0]][i[1]] += 1

grid.saveGridToFile('./output')
print(grid.getNumberOfDangerPoints())