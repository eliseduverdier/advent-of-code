import time
import os

def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip().split('\n')

def prettyPrint(matrix):
    os.system('clear')

    for i in matrix:
        for j in i:
            print(j, end=' ')
        print('')
    print('---')
    # time.sleep(.5)

stackSample = [
['.', '.', '.'],
['.', '.', '.'],
['.', '.', '.'],
['.', '.', '.'],
['.', '.', '.'],
['.', '.', '.'],
['.', '.', '.'],
['.', 'D', '.'],
['N', 'C', '.'],
['Z', 'M', 'P']
]

stackInput = [
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', 'C', '.', '.', 'N', 'R', '.'],
['J', 'T', '.', 'H', '.', '.', 'P', 'L', '.'],
['F', 'S', 'T', 'B', '.', '.', 'M', 'D', '.'],
['C', 'L', 'J', 'Z', 'S', '.', 'L', 'B', '.'],
['N', 'Q', 'G', 'J', 'J', '.', 'F', 'F', 'R'],
['D', 'V', 'B', 'L', 'B', 'Q', 'D', 'M', 'T'],
['B', 'Z', 'Z', 'T', 'V', 'S', 'V', 'S', 'D'],
['W', 'P', 'P', 'D', 'G', 'P', 'B', 'P', 'V'],
]

def getTopOfCol(col):
    i = 0
    while stack[i][col] == '.':
        i += 1
    item = stack[i][col]
    stack[i][col] = '.'
    return item

def getMultiTopOfCol(qty, col):
    i = 0
    while stack[i][col] == '.':
        i += 1
    l = []
    for j in range(i,i+qty):
        l.append( stack[j][col] )
        stack[j][col] = '.'
    return l

def setMultiTopOfCol(qty, col, items):
    i = 0
    if stack[len(stack)-1][col] == '.':  # if column is empty, set the bottom case
        bottomstart = len(stack)-1
    else:
        while stack[i][col] == '.' :
            i += 1
            bottomstart = i-1
    j=len(items)-1
    for item in items:
        stack[i-1-j][col] = item
        j-=1

def setTopOfCol(col, item):
    i = 0
    if stack[len(stack)-1][col] == '.':  # if column is empty, set the bottom case
        stack[len(stack)-1][col] = item
    else:
        while stack[i][col] == '.' :
            i += 1
        stack[i-1][col] = item

def part1(input):
    for line in input:
        print('================', line)
        instruction = line.split(' from ')
        moves = int(instruction[0].split(' ')[1])
        fromCol, toCol = list(map(lambda i: int(i), instruction[1].split(' to ')))
        prettyPrint(stack)
        for i in range(moves):
            itemToMove = getTopOfCol(fromCol-1)
            setTopOfCol(toCol-1, itemToMove)

    print('#######################"')
    prettyPrint(stack)
    for i in range(len(stack[0])):
        print(getTopOfCol(i),end='')
    return

def part2(input):
    for line in input:
        prettyPrint(stack)
        print('================', line)

        instruction = line.split(' from ')
        moves = int(instruction[0].split(' ')[1])
        fromCol, toCol = list(map(lambda i: int(i), instruction[1].split(' to ')))

        itemsToMove = getMultiTopOfCol(moves, fromCol-1)
        setMultiTopOfCol(moves, toCol-1, itemsToMove)

    print('####################### end:')
    prettyPrint(stack)
    for i in range(len(stack[0])):
        print(getTopOfCol(i),end='')
    return


# input = getInput('sample')
# stack = stackSample

input = getInput('input')
stack = stackInput

# print('>>> part 1:', part1(input))
print('>>> part 2:', part2(input))