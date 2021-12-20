dataFile = open('./input', 'r')
rawData = dataFile.read()
data = rawData.split(',')

#data = [16,1,2,0,4,7,1,2,14]

crabSubsPos = []
for i in data:
    crabSubsPos.append(int(i))

crabSubsFuelCost = []

for pos in range(len(crabSubsPos)):
    fuelCostSum = 0
    for crabSub in crabSubsPos:
        distanceMoved = abs(int(crabSub)-pos)
        fuelCost = 0
        for i in range(distanceMoved):
            fuelCost += i+1

        fuelCostSum += fuelCost
    
    crabSubsFuelCost.append(fuelCostSum)

cheapestPos = 0
cheapestCost = crabSubsFuelCost[0]
for pos in range(len(crabSubsFuelCost)):
    if crabSubsFuelCost[pos] < cheapestCost:
        cheapestPos = pos
        cheapestCost = crabSubsFuelCost[pos]

print(f"Position: {cheapestPos} is cheapest with a cost of: {cheapestCost}")