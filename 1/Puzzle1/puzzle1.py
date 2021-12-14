dataFile = open('./input', 'r');

data = dataFile.read()
dataArray = data.split('\n')
result = 0
for i in range(len(dataArray)):
    if i == 0:
        pass
    elif int(dataArray[i])>int(dataArray[i-1]):
        result += 1

print("Result puzzle 1: " + str(result))

pastSegmentSum = 0
result = 0

for i in range(len(dataArray)):
    if i >= len(dataArray)-2:
        break
    if i == 0:
        pastSegmentSum = int(dataArray[i]) + int(dataArray[i+1]) + int(dataArray[i+2])
    else:
        segmentSum = int(dataArray[i]) + int(dataArray[i+1]) + int(dataArray[i+2])

        if segmentSum > pastSegmentSum:
            result += 1

        pastSegmentSum = segmentSum

print("Result puzzle 2: " + str(result))