def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip().split('\n')

def getMaxTwoDigitNumber(line):
    maxFirstNum = getMaxWithIndex(list(line), True)
    maxIndex = maxFirstNum[1]
    maxSecondNum = getMaxWithIndex(list(line)[(maxIndex+1):], False)
    return str(maxFirstNum[0]) +  str(maxSecondNum[0])

def getMaxTwelveDigitNumber(line):
    maxFirstNum = getMaxWithIndex(list(line), True)
    maxIndex = maxFirstNum[1]
    maxSecondNum = getMaxWithIndex(list(line)[(maxIndex+1):], False)
    return str(maxFirstNum[0]) +  str(maxSecondNum[0])

def getMaxWithIndex(line, cantBeLast):
    max = [0, 0]
    secondMax = [0, 0]
    for i in range(len(line)):
        if int(line[i]) > max[0]:
            secondMax = max
            max = [int(line[i]), i]
    if max[1] == len(line)-1 and cantBeLast:
        return secondMax
    else:
        return max

def getResult(input):
    maxNumbers = []
    for line in input:
        # maxNumbers.append(getMaxTwoDigitNumber(line)) # part 1
        maxNumbers.append(getMaxTwelveDigitNumber(line)) # part 2
    # print(maxNumbers)
    return sum(map(int, maxNumbers))
# -------------------------------------------------
# input = getInput('sample')
input = getInput('input')

print(' >>> ',getResult(input))
