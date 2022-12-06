def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip().split('\n')

def fullyContains(arr1, arr2):
    if int(arr1[0]) >= int(arr2[0]) and int(arr1[1]) <= int(arr2[1]):
        print (arr1, 'fully contains', arr2)
        return True
    return False

def overlap(arr1, arr2):
    #   1  ends   before   2 starts
    if int(arr1[1]) >= int(arr2[0]) and int(arr2[1]) >= int(arr1[0]):
        print (arr1, arr2, 'overlap because',arr1[1],' >= ',arr2[0] )
        return True
    return False

def part1(input):
    count = 0
    for line in input:
        l = line.split(',')
        a = [ l[0].split('-'), l[1].split('-') ]
        if fullyContains(a[0], a[1]) or fullyContains(a[1], a[0]):
            count += 1
    return count

def part2(input):
    count = 0
    for line in input:
        l = line.split(',')
        a = [ l[0].split('-'), l[1].split('-') ]
        if overlap(a[0], a[1]):
            count += 1
    return count


# input = getInput('sample')
input = getInput('input')

# print('>>> part 1:', part1(input))
print('>>> part 2:', part2(input))