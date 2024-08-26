
while True:
    string = input()
    # string = string.split()
    countA = 0
    countB = 0

    for i in string:
        if i not in ['a', 'b']:
            print('String inválida')
            exit()
        if i == 'a':
            countA = countA + 1
        elif i== 'b':
            countB = countB + 1
        
    if countA % 2 == 0 and countB % 2 == 0:
        print('string válida')
    else:
        print('String inválida')
    

