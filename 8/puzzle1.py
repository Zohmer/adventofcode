import sevenSegment

dataFile = open('./input', 'r')
rawData = dataFile.read()
dataFile.close()

data = rawData.split('\n')

displays = []
for i in data:
    displays.append(sevenSegment.SevenSegment(i))

uniques = 0
for display in displays:
    uniques += display.getNumberOfUniqueSegments('output')

print(f"1, 4, 7 and 8 appears: {uniques} times")

testData = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

testObject = sevenSegment.SevenSegment(testData)

decodedPattern = testObject.decodeSignalPattern()

print(decodedPattern)