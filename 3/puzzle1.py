dataFile = open('./input', 'r')
data = dataFile.read()
data = data.split('\n')

binaryGrid = [[0] * len(data[0])] * len(data)
for i in range(len(data)):
    for j in range(len(data[i])):
        binaryNum = data[i]
        binaryGrid[i][j] = (binaryNum[j:j+1])

gammaRate = []
epsilonRate = []

for i in range(len(data[i])):
    count0 = 0
    count1 = 0
    for j in range(len(data)):
        if data[j][i] == "1":
            count1 += 1
        elif data[j][i] == "0":
            count0 += 1
    if count0 > count1:
        gammaRate.append(0)
        epsilonRate.append(1)
    else:
        gammaRate.append(1)
        epsilonRate.append(0)

gammaRateDec = int("".join(str(i) for i in gammaRate), 2)
epsilonRateDec = int("".join(str(i) for i in epsilonRate), 2)

print("Gamma rate: " + str(gammaRate))
print("Epsilon rate: " + str(epsilonRate))
print("Energy consumption: " + str(gammaRateDec*epsilonRateDec))
