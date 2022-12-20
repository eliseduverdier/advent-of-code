######################
#       INPUT !
######################

import os
import time

MAX=167

def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip().split('\n')

def pprint(sandMaze, step = 0):
    os.system('clear')
    map = {' ': '  ', '#': '██', 'o':'▒▒', 'x': '\/', '~': '~~'}
    print('\n┌'+('─'*2000) +'┐')
    for i in sandMaze:
        print('│ ',end='')
        for j in i[250:750]:
            print(map[j] , end='')
        print(' │')
    print('└'+('─'*2000) +'┘')
    print('[STEP '+'% 3d' % step+']')
    time.sleep(.01)
# ==================================================

BOARD = [[' ' for i in range(1000)] for j in range(MAX + 3)]

def drawLines(lines):
    for i in range(0, len(lines)-1):
        START_HOR = int(lines[i][0])
        END_HOR = int(lines[i+1][0])
        START_VER = int(lines[i][1])
        END_VER = int(lines[i+1][1])
        if (START_HOR == END_HOR): # horizontal line
            for j in range(START_VER, (END_VER + (1 if START_VER<END_VER else -1)), (1 if START_VER<END_VER else -1) ):
                BOARD[ j ][ START_HOR ] = '#'

        else: # vertical line
            for j in range(START_HOR, (END_HOR + (1 if START_HOR<END_HOR else -1)), (1 if START_HOR<END_HOR else -1) ):
                BOARD[ START_VER ][ j ] = '#'

def flyLittleSand(height, pos):
    # if height > 168:
    #     BOARD[ height-1 ][ pos ] = '~'
    #     return False # INTO THE ABYSS !
    if height < 0 or BOARD[ 0 ][ 500 ] == 'o': # thats part 2
        return False # SORRY WERE FULL

    if BOARD[ height ][ pos ] == ' ': # don’t stop til we find a path or another grain
        return flyLittleSand(height+1, pos)

    elif BOARD[ height ][ pos ] in ['o', '#']:   # if on top on grain or path
        if BOARD[ height ][ pos-1 ] == ' ': # then try left
            return flyLittleSand(height, pos-1)
        elif BOARD[ height ][ pos+1 ] == ' ': # then try right
            return flyLittleSand(height, pos+1)
        else: # then stay there
            BOARD[ height-1 ][ pos ] = 'o'

    return True

input = getInput('input')
input.append('0,169 -> 999,169')
for i in input:
    drawLines(list(map(
        lambda l: list(map(
            lambda ll: int(ll), l.split(',')
        )), i.split(' -> ')
    )))

grains = 0
while flyLittleSand(0, 500):
    # pprint(BOARD)
    grains += 1
pprint(BOARD)

print('>>> part 1:', grains)