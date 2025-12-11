def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip().split('\n')

def moveOne(position, direction):
    if direction == 'L':
        if position == 0: return 99
        else: return position - 1
    if direction == 'R':
        if position == 99: return 0
        else: return position + 1

def getResult(input):
    counterZero = 0
    position = 50
    for move in input:
        distance = int(move[1:])
        for i in range(distance):
            position = moveOne(position, move[0])
            if position == 0: counterZero += 1
    return counterZero

# -------------------------------------------------
# input = getInput('sample')
input = getInput('input')

print(getResult(input))
