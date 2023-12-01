import re

digits = {
    'one' : 1,
    'two' : 2,
    'three': 3,
    'four' : 4,
    'five' : 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip().split('\n')

def part1(input):
    nbs = []
    for line in input:
        numbers = re.sub('[a-z]', '', line)
        nbs.append(int(str(numbers)[0]+''+ str(numbers)[-1]))
    return sum(nbs)

def part2(input):
    nbs = []
    for line in input:
        numbers = line
        for s, d in digits.items():
            numbers = re.sub(s, str(d), numbers)
        numbers = re.sub('[a-z]', '', numbers)
        nbs.append(int(str(numbers)[0]+''+ str(numbers)[-1]))
    return sum(nbs)
    return ''


# input = getInput('sample')
input = getInput('input')

# print('>>> part 1:', part1(input))
print('>>> part 2:', part2(input))
