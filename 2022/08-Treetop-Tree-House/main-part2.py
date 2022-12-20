def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return min(rightMax, int(rightMin + (valueScaled * rightSpan)))

def prettyPrint(matrix):
    heights = [' ','⋅','░','▒','▓','█','🌲']
    for i in matrix:
        for j in i:
            print(heights[translate(j,0, 100,0,6)], end=' ')
        print('')
    print('---')

def getInput(name):
    with open(name+'.txt', 'r') as file:
        lines = file.read().strip().split('\n')
        for i in range (len(lines)):
            lines[i] = list(map(lambda i: int(i), (list(lines[i]))))
    return lines

def getTreeViewCount(input, i, j) -> bool:
    viewCountTop = 0
    viewCountLeft = 0
    viewCountRight = 0
    viewCountBot = 0
    # from the NORTH
    for a in range(i-1, -1, -1):
        if input[a][j] >= input[i][j]: viewCountTop += 1; break
        else: viewCountTop += 1
    # EAST
    for a in range(j+1, len(input[0])):
        if input[i][a] >= input[i][j]: viewCountRight += 1; break
        else: viewCountRight += 1
    # SOUTH
    for a in range(i+1, len(input)):
        if input[a][j] >= input[i][j]: viewCountBot += 1; break
        else: viewCountBot += 1
    # WEST
    for a in range(j-1, -1, -1):
        if input[i][a] >= input[i][j]: viewCountLeft += 1; break
        else: viewCountLeft += 1

    return viewCountTop*viewCountRight*viewCountBot*viewCountLeft


def part2(input):
    scenicScores = []
    columns = len(input)
    rows = len(input[0])
    count = 0
    for i in range(0, columns):
        scenicScores.append([])
        for j in range(0, rows):
            TreeViewCount = getTreeViewCount(input, i, j)
            scenicScores[i].append(TreeViewCount)

    prettyPrint(scenicScores)

    maxes = list(map(lambda i: max(i), scenicScores))
    return max(maxes)

# input = getInput('sample')
input = getInput('input')

print('>>> part 2:', part2(input))