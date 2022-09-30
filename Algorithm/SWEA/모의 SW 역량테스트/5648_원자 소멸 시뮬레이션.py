from collections import defaultdict

T = int(input())

for t in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    case = defaultdict(list)
    for x, y, d, k in atoms:
        for X, Y, D, K in atoms:            
            if x == X and d+D == 1:       # 세로 충돌 확인
                if (d == 0 and y < Y) or (d == 1 and y > Y): 
                    case[abs(Y-y)].append([[x,y,k], [X,Y,K]])
            elif y == Y and d+D == 5:     # 가로 충돌 확인
                if (d == 2 and x > X) or (d == 3 and x < X):
                    case[abs(X-x)].append([[x,y,k], [X,Y,K]])
            elif abs(y-Y) == abs(x-X):                      # 다른 방향 충돌 확인
                if x < X and y < Y and [d, D] in [[3, 1], [0, 2]]:
                    pass
                elif x < X and y > Y and [d, D] in [[3,0], [1, 2]]:
                    pass
                elif x > X and y > Y and [d, D] in [[1,3], [2, 0]]:
                    pass
                elif x > X and y < Y and [d, D] in [[0,3], [2, 1]]:
                    pass
                else:
                    continue
                case[abs(x-X)*2].append([[x,y,k], [X,Y,K]])
                
    sort_case = sorted(case)
    bigbang = {}
    cur_time = 0
    total = 0
    for time in sort_case:
        for [x,y,k], [X,Y,K] in case[time]:
            if (x,y) not in bigbang and (X,Y) not in bigbang:
                total += k+K
                bigbang[(x,y)] = time
                bigbang[(X,Y)] = time
                cur_time = time
            elif (x,y) in bigbang and (X,Y) not in bigbang and time == bigbang[(x,y)]:
                total += K
                bigbang[(X,Y)] = time
            elif (x,y) not in bigbang and (X,Y) in bigbang and time == bigbang[(X,Y)]:
                total += k
                bigbang[(x,y)] = time
        # print(total)
        # print(time, bigbang)
    print(f'#{t} {total}')