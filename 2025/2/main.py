def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip().split(',')

def isInvalidIdPartOne(id):
    if len(id) % 2 == 1:
        return False
    else:
        mid = int(len(id) / 2)
        if id[:mid] == id[mid:]:
            return True
        else:
            return False

def isInvalidIdPartTwo(id):
    for i in range(1, int(len(id) / 2)+1):
        if isRepeatedNDigits(id, i):
#             print('is repeated!', id, 'with', i)
            return True
    return False

def isRepeatedNDigits(num, N):
    num = str(num)
    start = num[0:N]
    for i in range(N, len(num), N):
        if start != num[i:(i+N)]: return False
    return True

def getResult(input):
    invalidIds = []
    for rr in input:
        r = rr.split('-')
        start = int(r[0])
        end = int(r[1])
        # print(' > ',start, ' -> ', end)
        for i in range(start, end, 1):
            if isInvalidIdPartTwo(str(i)):
                invalidIds.append(i)
    return sum(invalidIds)

# -------------------------------------------------
# input = getInput('sample')
input = getInput('input')

print(' >>> ', getResult(input))
