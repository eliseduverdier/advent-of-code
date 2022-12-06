def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip().split('\n')

def part1(input):
    return ''

def part2(input):
    return ''


input = getInput('sample')
# input = getInput('input')

print('>>> part 1:', part1(input))
print('>>> part 2:', part2(input))