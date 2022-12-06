import numpy as np

def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip().split('\n\n')

def part1(input):
    sums = []
    for i in input:
        sums.append ( sum(list(map(lambda i: int(i), i.split('\n')))) )
    print( max (sums))
    return sums

def part2(sums):
    sorted = np.sort(sums)
    return sum(sorted[:-2])


# input = getInput('sample')
input = getInput('input')
result1 = part1(input)
print('part 1:', )
print('part 2:', part2(result1))