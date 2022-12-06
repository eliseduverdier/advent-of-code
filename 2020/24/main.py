import os
import time

def getInput(name):
    with open(name+'.txt', 'r') as file:
        return list(map(
            lambda l: parseDirections(l), file.read().split('\n')
        ))
def prettyPrint(tiles, step):
    map = {0:' ⋅ ',1:'⬤  ','F':' ↺ '}
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n┌'+'─'*len(tiles[0]) * 3+'┐')
    for i in tiles:
        print('│',end='')
        for j in i:
            print(map[j], end='')
            # print(j if j != 0 else ' ', end=' ')
        print('│')
    print('└'+'─'*len(tiles[0]) * 3+'┘')
    print('[STEP '+'% 3d' % step+']')
# ============================================================

def parseDirections(directionString): # line
    dir = []
    i = 0
    while i < len(directionString):
        if directionString[i] == 'e' or directionString[i] == 'w':
            dir += [ directionString[:i+1] ]
            directionString = directionString[i+1:]
            i = -1
        i += 1
    return dir

directions = {
    #     X(ew) Y(sn)                >   v
     'e' : [ 2,  0 ],  # i -> j -> [ 2,  0 ]
    'se' : [ 1,  1 ],  # i -> o -> [ 1,  1 ]
    'ne' : [ 1, -1 ],  # i -> d -> [ 1, -1 ]
     'w' : [-2,  0 ],  # i -> h -> [-2,  0 ]
    'sw' : [-1,  1 ],  # i -> n -> [-1,  1 ]
    'nw' : [-1, -1 ],  # i -> c -> [-1, -1 ]
}

# big matrix and count move only by twoes
# .c.d.
# h.i.j
# .n.o.

# ============================================================
def decideWhichTileToReturn(tiles):
    tilesCopy = [[0 for i in range(len(tiles[0]))] for i in range(len(tiles))]
    for i in range(len(tiles)):
        for j in range(len(tiles[0])):
            if shouldBeFlipped(tiles, i, j):
                tilesCopy[i][j] = 'F'
    return tilesCopy

def getNeighboursCountForEach(tiles):
    tilesCopy = [[0 for i in range(len(tiles[0]))] for i in range(len(tiles))]
    for i in range(len(tiles)):
        for j in range(len(tiles[0])):
            tilesCopy[i][j] = countBlackNeighbours(tiles, i, j)
    return tilesCopy

def returnTiles(original, flipping):
    for i in range(len(original)):
        for j in range(len(original[0])):
            if flipping[i][j] == 'F':
                original[i][j] = 1 if original[i][j] == 0 else 0
    return original

'''
- Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
- Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
'''
def shouldBeFlipped(tiles, i, j):
    n = countBlackNeighbours(tiles, i, j)
    #print(n,end=' ')
    return (tiles[i][j] == 1 and (n == 0 or n > 3)) \
        or (tiles[i][j] == 0 and n > 0 and n <= 3)

def countBlackNeighbours(tiles, i, j):
    count = 0
    for dir in directions.values():
        try:
            if tiles[ i + dir[0] ][ j + dir[1] ] == 1:
                count += 1
        except:
            pass
    return count
# ============================================================

# STEP 1: count flipped tiles

movments = getInput('input')

size = 120
tiles = [[0 for i in range(size)] for i in range(size)]
x, y = int(size/2), int(size/2)
for mov in movments:
    for step in mov:
        x += directions[step][0]
        y += directions[step][1]
    tiles[x][y] = 1 if tiles[x][y] == 0 else 0
    x, y = int(size/2), int(size/2) # reset starting tile

steps = 0
for i in range(1000):
    flip = decideWhichTileToReturn(tiles)
    tiles = returnTiles(tiles, flip)
    prettyPrint(tiles, steps)
    steps += 1
    time.sleep(.1)

count = 0
for i in tiles:
    for j in i:
        if j == 1: count += 1
print(count)
