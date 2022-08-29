import sys

sys.stdin = open('TIL/Algorithm/SWEA/D4/input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [] # 정답
    dup_xy = [] # 중복 체크
    
    for i in range(N):
        subarr = [] # 가로 범위
        for j in range(N):
            if arr[i][j] == 0: # 0일 경우 
                col = i
                if subarr:
                    while subarr and col < N and arr[col][subarr[0]] != 0: # 세로 길이 체크
                        col += 1
                    result.append([col-i, subarr[-1] - subarr[0] + 1]) # 세로 길이와 가로 길이 추가
                    for x in range(i, col):
                        for y in range(subarr[0], subarr[-1]+1):
                            dup_xy.append([x,y])
                    subarr = []
            elif arr[i][j] != 0: # 0이 아닐 경우
                # print(i,j)
                if [i,j] not in dup_xy: # 이미 체크 했던 범위가 아닐 경우
                    subarr.append(j)

            if j == N-1: # 끝라인일 경우
                col = i
                if subarr:
                    # print(subarr)
                    while subarr and col < N and arr[col][subarr[0]] != 0: # 세로 길이 체크
                        col += 1
                    result.append([col-i, subarr[-1] - subarr[0] + 1]) # 세로 길이와 가로 길이 추가
                    for x in range(i, col):
                        for y in range(subarr[0], subarr[-1]+1):
                            dup_xy.append([x,y])
                    subarr = []
        
    print(f'#{t} {len(result)}', end=' ')

    for i in range(len(result)-1): # 선택 정렬 후......
        minV, minI = result[i][0] * result[i][1], i
        for j in range(i+1, len(result)):
            if result[j][0] * result[j][1] < minV:
                minV, minI = result[j][0] * result[j][1], j
        result[i], result[minI] = result[minI], result[i]
    for i in result:
        print(*i, end=' ')
    print()