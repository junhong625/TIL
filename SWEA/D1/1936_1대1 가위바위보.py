while True:
    A, B = map(int, input().split())
    if A == 1:
        if B == 1:
            continue
        elif B == 2:
            print('B')
            break
        else :
            print('A')
            break
    elif A == 2:
        if B == 1:
            print('A')
            break
        elif B == 2:
            continue
        else :
            print('B')
            break
 
    else:
        if B == 1:
            print('B')
            break
        elif B == 2:
            print('A')
            break
        else :
            continue