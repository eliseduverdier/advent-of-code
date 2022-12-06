def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip().split('\n')

scores = {
    'A':1, 'X':1, # rock
    'B':2, 'Y':2, # papers
    'C':3, 'Z':3, # scissors
}

def part1(input):
    totalscore = 0
    for i in input:
        draw = i.split(' ')
        totalscore += scores[draw[1]]
        if (draw[0]=='A' and draw[1]=='Y') or  (draw[0]=='B' and draw[1]=='Z') or  (draw[0]=='C' and draw[1]=='X'): # won
            totalscore += 6
        elif (draw[0]=='A' and draw[1]=='Z') or  (draw[0]=='B' and draw[1]=='X') or  (draw[0]=='C' and draw[1]=='Y'): # loose
            totalscore += 0
        elif scores[draw[0]] == scores[draw[1]]: # draw
            totalscore += 3
    return totalscore;

def part2(input):
    totalscore = 0
    for i in input:
        draw = i.split(' ')
        # print(draw[0] , scores[draw[0]] , draw[1],  scores[draw[1]], end='')
        if draw[1] == 'X': # needs to loose
            totalscore += 0
            if draw[0]=='A': totalscore += 3
            if draw[0]=='B': totalscore += 1
            if draw[0]=='C': totalscore += 2

        elif draw[1] == 'Y': # needs to draw
            totalscore += scores[draw[0]]+3

        elif draw[1] == 'Z': # needs to win
            totalscore += 6
            if draw[0]=='A': totalscore += 2
            if draw[0]=='B': totalscore += 3
            if draw[0]=='C': totalscore += 1
    return totalscore;


# input = getInput('sample')
input = getInput('input')

print('part 1:', part1(input))
print('part 2:', part2(input))