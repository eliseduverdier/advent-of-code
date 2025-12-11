def getInput(name):
    columns = []
    with open(name+'.txt', 'r') as file:
        lines = file.read().strip().split('\n')
        for i in range(len(lines[0])):
            col = []
            for j in range(len(lines)):
                col.append(
                    '' if lines[j][i] == '.' or lines[j][i] == ' ' else lines[j][i]
                )
            columns.append(col)
    # columns ok, concat numbers
    okCols = []
    for c in columns:
        if '*' in c:
            okCols.append('*')
            okCols.append(''.join(c).replace('*', ''))
        elif '+' in c:
            okCols.append('+')
            okCols.append(''.join(c).replace('+', ''))
        else:
            okCols.append(''.join(c))

    return okCols

def product(numbers):
    prod = 1
    for n in numbers:
        prod = prod * int(n)
    return prod

# --------------------------------------- PART 2
def getResult(input):
    #print(input)
    operationResults = []
    numbers = []
    input.append('')
    for i in input:
        if i == '*': currentOp = '*'
        elif i == '+': currentOp = '+'
        elif i == '' :
            #print('finished op', currentOp, numbers)
            if currentOp == '*':
                operationResults.append( product(numbers) )
            if currentOp == '+':
                operationResults.append( sum(list(map(lambda x: int(x), numbers))) )
            numbers = []
        else:
            #print('is',i)
            numbers.append(i)

    return sum(operationResults)



# -------------------------------------------------
# input = getInput('sample')
input = getInput('input')
# print(input)

print(' >>> ',getResult(input))
