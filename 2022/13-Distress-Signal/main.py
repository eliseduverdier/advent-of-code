def getInput(name, asPairs):
    with open(name+'.txt', 'r') as file:
        sets = file.read().strip().split('\n\n')
        l = []
        for set in sets:
            setAsLines = set.split('\n')
            if asPairs:
                l.append( [ eval(setAsLines[0]), eval(setAsLines[1]) ] )
            else:
                l.append( eval(setAsLines[0]))
                l.append( eval(setAsLines[1]) )
        return l

def compare(item1, item2):
    # print('--------- comparing',item1,'and', item2)
    if isinstance(item1, int) and isinstance(item2, int):
        if item1 == item2:
            return None
        return item1 < item2

    if isinstance(item1, list) and isinstance(item2, list):
        for e1, e2 in zip(item1, item2):
            res = compare(e1, e2)
            if res is not None:
                return res
        return compare(len(item1), len(item2))

    if isinstance(item1, int):
        return compare([item1], item2)
    return compare(item1, [item2])

def getFirstInt(l):
    if isinstance(l, int): return l
    if len(l) == 0: return 0
    else: return getFirstInt(l[0])

def part1(input):
    SUM = 0
    for idx, lists in enumerate(input):
        res = compare(lists[0], lists[1])
        if res: SUM += idx+1
    return SUM

def part2(input):
    TWO, SIX = 0, 0
    firstItems = []
    for l in input:
        firstItems.append( getFirstInt(l) )
    firstItems.sort()
    TWO = firstItems.index(2) - 1
    SIX = firstItems.index(6)
    return TWO * SIX

# input = getInput('sample', False)
input = getInput('input', False)

print('>>> part 1:', part1(input))
print('>>> part 2:', part2(input))
#     (2) 118×  (6) 200   = 23600