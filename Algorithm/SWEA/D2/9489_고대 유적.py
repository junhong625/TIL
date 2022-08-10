T = int(input())
for t in range(1, T+1): # 테스트 케이스 수만큼 반복
    N, M = map(int, input().split()) # 행과 열
    arr = [list(map(int, input().split())) for _ in range(N)] # 2차원 배열
     
    maxV = 0 # 최대값
    for i in range(N): # 가로 합에서 나올 수 있는 최대값 구하기
        total_row = 0
        for j in range(M):
            if arr[i][j] == 1:
                total_row += 1
                maxV = total_row if total_row > maxV else maxV
            else:
                total_row = 0
             
    for l in range(M): # 세로 합에서 나올 수 있는 최대값 구하기
        total_col = 0
        for k in range(N):
            if arr[k][l] == 1:
                total_col += 1
                maxV = total_col if total_col > maxV else maxV
            else:
                total_col = 0
             
    print(f'#{t} {maxV}')