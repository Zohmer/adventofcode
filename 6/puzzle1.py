import lanternfish

dataFile = open('./input', 'r')
data = dataFile.read().split(',')
dataFile.close()

data = [3,4,3,1,2]

fishSchool = []
for fish in data:
    fishSchool.append(lanternfish.lanternfish(int(fish)))

outputFile = open('./output', 'w')
outputFile.write('')
outputFile.close()
i = 0
for day in range(80):
    for fish in fishSchool:
        newFish = fish.dayChange()
        if newFish:
            fishSchool.append(newFish)
    
    population = []
    for fish in fishSchool:
        population.append(str(fish.cycle))

    report = f"Day {day}: "
    report = report + ",".join(population) + '\n'
    
    outputFile = open('./output', 'a')
    outputFile.write(report)
    outputFile.close()

populationSize = len(fishSchool)
print(f"Population: {populationSize}")