def getInput(name):
    with open(name+'.txt', 'r') as file:
        lines = (file.read().strip().split('\n'))
        return list(map(lambda l: list(l), lines))

def prettyPrint(matrix):
    for i in matrix:
        for j in i:
            print(j, end='')
        print('')
    print('---')

def countNeighbours(matrix, a, b):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (a+i >= 0
                and a+i < len(matrix[0])
                and b+j >= 0
                and b+j < len(matrix)
                and not(i==0 and j==0)
            ):
                if matrix[a+i][b+j] == '@' or matrix[a+i][b+j] == 'x':
                    neighbours += 1
    #print(matrix[a][b], '[',a,',',b,']', 'has count', neighbours,)
    return neighbours

def getResult(input):
    count = 0
    mapOfRollsToBeReplaced = [ [0]*len(input) for i in range(len(input))]
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if input[i][j] == '@' and countNeighbours(input, i, j) < 4:
                count += 1
                mapOfRollsToBeReplaced[i][j] = 1
    return [count, mapOfRollsToBeReplaced]

def replacePaperRolls(input, mapOfRollsToBeReplaced):
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if (mapOfRollsToBeReplaced[i][j] == 1):
                input[i][j] = '.'
    return input

def countRolls(input):
    countRolls = 0
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if (input[i][j] == '@'):
                countRolls += 1
    return countRolls

def getResult2(input):
    rollsAtBeginning = countRolls(input)
    res = getResult(input)
    count = res[0]
    newInput = replacePaperRolls(input, res[1])
    while count > 0:
        res = getResult(newInput)
        count = res[0]
        newInput = replacePaperRolls(newInput, res[1])
    prettyPrint(newInput)

    return rollsAtBeginning - countRolls(newInput)


# -------------------------------------------------
# input = getInput('sample')
input = getInput('input')

print(' >>> ',getResult2(input))
# 1991 too high
