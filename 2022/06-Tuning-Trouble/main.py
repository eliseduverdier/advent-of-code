def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip()


def parts(input, LEN):
    index = LEN
    lastFourChars = []
    for i in range(LEN, len(input)):
        lastFourChars = set(input[i-LEN:i])
        if (len(lastFourChars)) == LEN: return index
        index += 1
    print (lastFourChars)
    return index


# input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb' # 7
# input = 'bvwbjplbgvbhsrlpgdmjqwftvncz' # 5
# input = 'nppdvjthqldpwncqszvftbrmjlhg' # 6
# input = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' # 10
# input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' # 11
input = getInput('input')

# print('>>> part 1:', parts(input, 4))
print('>>> part 2:', parts(input, 14))