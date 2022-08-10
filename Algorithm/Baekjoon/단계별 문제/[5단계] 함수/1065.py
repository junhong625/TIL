X = int(input())
if X < 100:
    print(X)
else:
    total = 99
    for i in range(111, X+1):
        if int(str(i)[2])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[0]):
            total += 1
    print(total)