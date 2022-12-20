import itertools

def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip().split('\n')

def sumSizes(lines):
    sumSizes = [] # part 1
    accumulateSizes = [] # part 2
    for line in lines:
        command = line.split(' ')

        if command[0] == '$':
            if command[1] == 'cd':
                if command[2] == '..':
                    sumSizes.append(accumulateSizes.pop())
                    accumulateSizes[-1] += sumSizes[-1]
                else: # $cd newDir
                    accumulateSizes.append(0)
            else: pass # $ ls
        elif command[0] != 'dir': # output of LS for files
            accumulateSizes[-1] += int(command[0])

    return sumSizes + list(itertools.accumulate(accumulateSizes[::-1]))

def part1(lines):
    lowestDirSizes = filter(lambda x: x <= 100_000, sumSizes(lines))
    return sum(lowestDirSizes)

def part2(lines):
    sumDirSizes = sumSizes(lines)
    available = 70_000_000 - sumDirSizes[-1]
    return min(filter(lambda x: x + available >= 30_000_000, sumDirSizes))

input = getInput('sample')
# input = getInput('input')

print('>>> part 1:', part1(input)) # sample: 95437
print('>>> part 2:', part2(input)) # sample: 24933642