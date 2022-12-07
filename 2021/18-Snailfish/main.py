def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().split('\n')

def part1():
    return

def part2():
    return


input = getInput('sample')
# input = getInput('input')

print('part 1:', part1())
print('part 2:', part2())

'''
For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].


    If any pair is nested inside four pairs, the leftmost such pair explodes.
    If any regular number is 10 or greater, the leftmost such regular number splits.


Here are some examples of a single explode action:

    [[[[[9,8],1],2],3],4] becomes
        [[[[0,9],2],3],4] (the 9 has no regular number to its left, so it is not added to any regular number).

    [7,[6,[5,[4,[3,2]]]]] becomes
    [7,[6,[5,[7,0]]]] (the 2 has no regular number to its right, and so it is not added to any regular number).

    [[6,[5,[4,[3,2]]]],1] becomes
    [[6,[5,[7,0]]],3].

    [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] becomes
    [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] (the pair [3,2] is unaffected because the pair [7,3] is further
     to the left; [3,2] would explode on the next action).

    [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] becomes
    [[3,[2,[8,0]]],[9,[5,[7,0]]]].

'''