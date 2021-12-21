class SevenSegment:
    def __init__(self, data) -> None:
        self.signalPattern = self.parseSignalPattern(data)
        self.output = self.parseOutput(data)

    def parseSignalPattern(self, data):
        signalPattern = data.split('|')
        signalPattern = signalPattern[0].strip()
        signalPattern = signalPattern.split(' ')
        return signalPattern

    def parseOutput(self, data):
        output = data.split('|')
        output = output[1].strip()
        output = output.split(' ')
        return output

    def getNumberOfUniqueSegments(self, part):
        if part == 'signal pattern':
            segments = self.signalPattern
        elif part == 'output':
            segments = self.output
        else:
            return 0
        
        uniqueSegments = 0
        for digit in segments:
            if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
                uniqueSegments += 1
        
        return uniqueSegments

    def decodeSignalPattern(self):
        """
        Segments are based on this code:
             aaaa
            b    c
            b    c
             dddd
            e    f
            e    f
             gggg
        """

        """
        Known digits: 0, 1, 4, 6, 7, 8, 9
        Known segments: a, b, c, d, e, f
        """

        decodedSegments = {
            "a":'',
            "b":'',
            "c":'',
            "d":'',
            "e":'',
            "f":'',
            "g":''
        }

        signalPattern = self.signalPattern

        #Decodes pattern for the digit one
        onePattern = []
        for pattern in signalPattern:
            if len(pattern) == 2:
                onePattern = list(pattern)
                signalPattern.remove(pattern)
                break

        #Decodes pattern for the digit four
        fourPattern = []
        for pattern in signalPattern:
            if len(pattern) == 4:
                fourPattern = list(pattern)
                signalPattern.remove(pattern)
                break

        #Decodes pattern for the digit seven
        sevenPattern = []
        for pattern in signalPattern:
            if len(pattern) == 3:
                sevenPattern = list(pattern)
                signalPattern.remove(pattern)
                break
        
        #Decodes pattern for the digit eight
        eightPattern = []
        for pattern in signalPattern:
            if len(pattern) == 7:
                eightPattern = list(pattern)
                signalPattern.remove(pattern)
                break

        #Decodes the segment for the a position
        for pattern in sevenPattern:
            if onePattern.count(pattern) == 0:
                decodedSegments['a'] = pattern

        #Decodes pattern for the digit six
        sixPattern = []
        for pattern in signalPattern:
            partFound = 0
            for i in range(len(pattern)):
                if pattern[i] == onePattern[0]:
                    partFound += 1
                if pattern[i] == onePattern[1]:
                    partFound += 1
            if partFound != 2 and len(pattern) == 6:
                sixPattern = pattern
                signalPattern.remove(pattern)

        #Decodes pattern for the digits nine and zero
        ninePattern = []
        zeroPattern = []
        partialFourPattern = []
        for segment in fourPattern:
            if onePattern.count(segment) == 0:
                partialFourPattern.append(segment)
        for pattern in signalPattern:
            if len(pattern) == 6:
                partFound = 0
                for segment in pattern:
                    if partialFourPattern.count(segment) != 0:
                        partFound += 1
                if partFound == 2:
                    ninePattern = pattern
                    signalPattern.remove(pattern)

        for pattern in signalPattern:
            if len(pattern) == 6:
                zeroPattern = pattern
                signalPattern.remove(pattern)

        #Decodes the segment for the d position
        if zeroPattern.count('a') == 0:
            decodedSegments['d'] = 'a'
        elif zeroPattern.count('b') == 0:
            decodedSegments['d'] = 'b'
        elif zeroPattern.count('c') == 0:
            decodedSegments['d'] = 'c'
        elif zeroPattern.count('d') == 0:
            decodedSegments['d'] = 'd'
        elif zeroPattern.count('e') == 0:
            decodedSegments['d'] = 'e'
        elif zeroPattern.count('f') == 0:
            decodedSegments['d'] = 'f'
        elif zeroPattern.count('g') == 0:
            decodedSegments['d'] = 'g'

        #Decodes the segment for the e position
        if ninePattern.count('a') == 0:
            decodedSegments['e'] = 'a'
        elif ninePattern.count('b') == 0:
            decodedSegments['e'] = 'b'
        elif ninePattern.count('c') == 0:
            decodedSegments['e'] = 'c'
        elif ninePattern.count('d') == 0:
            decodedSegments['e'] = 'd'
        elif ninePattern.count('e') == 0:
            decodedSegments['e'] = 'e'
        elif ninePattern.count('f') == 0:
            decodedSegments['e'] = 'f'
        elif ninePattern.count('g') == 0:
            decodedSegments['e'] = 'g'

        #Decodes the segment for the c position
        if sixPattern.count('a') == 0:
            decodedSegments['c'] = 'a'
        elif sixPattern.count('b') == 0:
            decodedSegments['c'] = 'b'
        elif sixPattern.count('c') == 0:
            decodedSegments['c'] = 'c'
        elif sixPattern.count('d') == 0:
            decodedSegments['c'] = 'd'
        elif sixPattern.count('e') == 0:
            decodedSegments['c'] = 'e'
        elif sixPattern.count('f') == 0:
            decodedSegments['c'] = 'f'
        elif sixPattern.count('g') == 0:
            decodedSegments['c'] = 'g'

        #Decodes the segment for the f position
        for segment in onePattern:
            if segment != decodedSegments['c']:
                decodedSegments['f'] = segment
                break

        #Decodes the segment for the b position
        tempPattern = [
            decodedSegments['c'],
            decodedSegments['d'],
            decodedSegments['f']
        ]
        for pattern in fourPattern:
            if tempPattern.count(pattern) == 0:
                decodedSegments['b'] = pattern

        #Decodes the segment for the g position
        allSegments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        valueFound = [False, False, False, False, False, False, False]
        for segment in allSegments:
            print(f"""

                Segment: {segment}

            """)
            if segment == decodedSegments['a']:
                print(decodedSegments['a'])
                valueFound[0] = True
            elif segment == decodedSegments['b']:
                print(decodedSegments['b'])
                valueFound[1] = True
            elif segment == decodedSegments['c']:
                print(decodedSegments['c'])
                valueFound[2] = True
            elif segment == decodedSegments['d']:
                print(decodedSegments['d'])
                valueFound[3] = True
            elif segment == decodedSegments['e']:
                print(decodedSegments['e'])
                valueFound[4] = True
            elif segment == decodedSegments['f']:
                print(decodedSegments['f'])
                valueFound[5] = True
            elif segment == decodedSegments['g']:
                print(decodedSegments['g'])
                valueFound[6] = True
        
        print(valueFound)
        for segment in range(len(allSegments)):
            if not valueFound[segment]:
                decodedSegments['g'] = allSegments[segment]
                break


        return decodedSegments