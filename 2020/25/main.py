# # sample
# card = 5764801
# door = 17807724
# input
card = 10604480
door = 4126658

subject = 7

divider = 20201227

def getLoopNumberFor(n, subject):
    loop = 0
    value = 1
    while value != n:
        # print(value, end=', ')
        value = (value * subject) % divider
        loop += 1
    return loop

def transform(n, loop):
    value = 1
    for i in range(loop):
        value = (value * n) % divider
    return value


loopCard = getLoopNumberFor(card, subject)
loopDoor = getLoopNumberFor(door, subject)
print(loopCard, loopDoor)

print(transform(card,loopDoor))
print(transform(door,loopCard))