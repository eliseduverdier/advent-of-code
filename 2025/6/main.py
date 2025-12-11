def getInput(name):
    all = []
    with open(name+'.txt', 'r') as file:
        lines = file.read().strip().split('\n')
        for line in lines:
            all.append(filterEmpty(line.split(' ')))
    return all

def filterEmpty(input):
    newArray = []
    for i in input:
        if i != '':
            newArray.append(i)
    return newArray

def product(numbers):
    prod = 1
    for n in numbers:
        prod = prod * int(n)
    return prod
# --------------------------------------- PART 1

def getResult(input):
    operations = []
    for i in range(0, len(input[0])):
        numbers = []
        for j in range (0, len(input) - 1):
            numbers.append(input[j][i])
        operations.append([
            input[len(input)-1][i],
            numbers
        ])

    operationResults = []

    for op in operations:
        if op[0] == '+':
            operationResults.append( sum(    list(map(lambda x: int(x), op[1])) ))
        if op[0] == '*':
            operationResults.append( product(op[1]) )

    return sum(operationResults)
# -------------------------------------------------
# input = getInput('sample')
input = getInput('input')

print(' >>> ',getResult(input))
