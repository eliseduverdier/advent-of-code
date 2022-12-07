import numpy as np
from scipy.sparse import csr_matrix

def parseInput(filename):
    with open(filename+'.csv', 'r') as file:
        lines = file.read().split('\n')

    on, off = [], []
    for line in lines:
        line = line.split(' ')
        xyz = line[1].replace('x=', '').replace('y=', '').replace('z=', '').split(',')
        x = xyz[0].split('..')
        y = xyz[1].split('..')
        z = xyz[2].split('..')
        if line[0] == 'on':
            on.append([
                [int(x[0]), int(x[1])],
                [int(y[0]), int(y[1])],
                [int(z[0]), int(z[1])],
            ])
        else: off.append([
                [int(x[0]), int(x[1])],
                [int(y[0]), int(y[1])],
                [int(z[0]), int(z[1])],
            ])

    return on, off

def countLights(cube):
    return np.size(cube[np.where(cube == True)])

on, off = parseInput('sample-part2')
# for i in input:
#     print(i)
# print(np.max(input), np.min(input)) # 120875 -124565

# size = 130000*2 + 1
# cube = np.empty((size, size, size), dtype='bool')
list = {}

print('---')
# 1. should compute the number of cells lit with overlapping (todo)
for instruction in on:
    print(' > ON ', instruction)
    for x in range( instruction[0][0], instruction[0][1]+1  ):
        for y in range( instruction[1][0], instruction[1][1]+1  ):
            for z in range( instruction[2][0], instruction[2][1]+1  ):
                list[f'{x}-{y}-{z}'] = True
                # cube[x + (size//2)][y + (size//2)][z + (size//2)] = True if instruction[0] == 'on' else False

# 2. should compare to the cubes above to turn off cells (todo)
for instruction in off:
    print(' > OFF ', instruction)
    for x in range( instruction[0][0], instruction[0][1]+1  ):
        for y in range( instruction[1][0], instruction[1][1]+1  ):
            for z in range( instruction[2][0], instruction[2][1]+1  ):
                del list[f'{x}-{y}-{z}']

print(len(list), list)