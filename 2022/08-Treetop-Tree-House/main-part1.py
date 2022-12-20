def getInput(name):
    with open(name+'.txt', 'r') as file:
        lines = file.read().strip().split('\n')
        for i in range (len(lines)):
            lines[i] = list(map(lambda i: int(i), (list(lines[i]))))
    return lines

def isLittleTreeVisible(input, i, j) -> bool:
    invisibleFrom = 0
    # from the NORTH ?
    for a in range(0, i):
        if input[a][j] >= input[i][j]:
            invisibleFrom+=1;break
    # and the WEST ?
    for a in range(0, j):
        if input[i][a] >= input[i][j]:
            invisibleFrom+=1;break
    # or the EAST ?
    for a in range(len(input[0])-1, j, -1):
        if input[i][a] >= input[i][j]:
            invisibleFrom+=1;break
    # the from the SOUTH
    for a in range(len(input)-1, i, -1):
        if input[a][j] >= input[i][j]:
            invisibleFrom+=1;break
    return invisibleFrom < 4


def part1(input):
    columns = len(input)
    rows = len(input[0])
    count = 0
    for i in range(1, columns-1):
        for j in range(1, rows-1):
            if isLittleTreeVisible(input, i, j): count += 1

    return count + len(input) * 2 + (len(input[0])-2) * 2

# input = getInput('sample')
input = getInput('input')

print('>>> part 1:', part1(input))