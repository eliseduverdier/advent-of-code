def getInput(name):
    with open(name+'.txt', 'r') as file:
        parts = (file.read().strip().split('\n\n'))
        return [
            parts[0].split('\n'),
            parts[1].split('\n')
        ]

# --------------------------------------- PART 1
def isInRange(ingredientId, r):
#     print('    ',ingredientId,'in', r, '?')
    rr = r.split('-')
    return (ingredientId) >= int(rr[0]) and ingredientId <= int(rr[1])

def isFresh(ingredientId, ranges):
    for r in ranges:
        if isInRange(int(ingredientId),r):
            return True
    return False

def getResult(ranges, ingredientsIds):
    countFresh = 0
    for ingredientId in ingredientsIds:
        if isFresh(ingredientId, ranges):
#             print(ingredientId,'is fresh')
            countFresh += 1
    return countFresh

# --------------------------------------- PART 2
def getUnique(listOfIngredients):
    uniqList=[]
    for item in listOfIngredients:
        if item not in uniqList:
            uniqList.append(item)
    return uniqList

def getResult2(ranges):
    countFresh = 0

    # get numbers from range
    numbers = []
    for r in ranges:
        rr = r.split('-')
        numbers.append(int(rr[0]))
        numbers.append(int(rr[1]))

    print('checking from', min(numbers), 'to', max(numbers)+1)
    # check all numbers
    for ingredientId in range(min(numbers), max(numbers)+1):
        if isFresh(ingredientId, ranges):
            # print(ingredientId,'is fresh')
            countFresh += 1
    return countFresh

# -------------------------------------------------
# input = getInput('sample')
input = getInput('input')

# print(' >>> ',getResult(input[0], input[1]))
print(' >>> ',getResult2(input[0]))
