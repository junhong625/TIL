T = int(input())

for t in range(1, T+1):                                  
    N = int(input())                                    # 삼각형 길이
    tri = [[0]*(n+1) for n in range(N)]                 # 각 위치에 대한 값
    tri[0][0] = 1                                       # 시작점
    print(f'#{t}')                                  
    for i in range(N):                                  
        for j in range(i+1):
            if j-1 < 0 or j+1 > i:                      # 윗줄의 값을 가져오는데 범위를 벗어날 경우 1로 지정
                tri[i][j] = 1
            else:                                       # 윗줄의 값과 윗줄 왼쪽의 값을 더한 값 할당
                tri[i][j] = tri[i-1][j] + tri[i-1][j-1]
            print(tri[i][j], end=' ')                   # 해당 위치의 값 출력
        print()