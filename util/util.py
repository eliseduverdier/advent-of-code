def prettyPrint(matrix):
    # os.system('clear')
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print('')
    print('---')
    # time.sleep(.5)