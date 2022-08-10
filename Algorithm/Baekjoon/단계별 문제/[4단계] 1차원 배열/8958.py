T = int(input())
for i in range(1, T+1):
    quiz = input()
    total = 0
    add = 0
    for ox in quiz:
        if ox == 'X':
            add = 0
        else:
            add += 1
            total += add
    print(total)