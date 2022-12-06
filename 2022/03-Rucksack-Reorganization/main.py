def getInput(name):
    with open(name+'.txt', 'r') as file:
        return file.read().strip().split('\n')

prios = { # lol, might be a better way with ascii codes
'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,
'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52,
}

def findCommonLetterIn2(arr1, arr2):
    for a in arr1:
        for b in arr2:
            if a == b: return a

def findCommonLetterIn3(str1, str2, str3):
    for a in str1:
        for b in str2:
            if a == b:
                print('common! '+a)
                for c in str3:
                    if c == a: return a

def findCommonLetterIn2(arr1, arr2):
    for a in arr1:
        for b in arr2:
            if a == b: return a

def part1(input):
    sum = 0
    for line in input:
        chars = list(line)
        half1 = chars[0 : (len(chars)//2)]
        half2 = chars[(len(chars)//2) :  ]
        sum +=prios[ findCommonLetterIn2(half1,half2)  ]
    return sum

def part2(input):
    sum = 0
    for i in range(0, len(input)-1, 3):
        print( findCommonLetterIn3(
            input[i],
            input[i+1],
            input[i+2]
        ) )
        sum +=prios[ findCommonLetterIn3(input[i],
            input[i+1],
            input[i+2])  ]
    return sum


# input = getInput('sample')
input = getInput('input')

# print('>>> part 1:', part1(input))
print('>>> part 2:', part2(input))
