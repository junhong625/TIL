T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    cnt = 0
    for n in range(N): 
        r1, c1, r2, c2, color = map(int, input().split()) # 좌표와 색 입력
        for i in range(r1, r2+1): # 행 좌표
            for j in range(c1, c2+1): #열 좌표
                if arr[i][j] != 0 and arr[i][j] != color: # 이미 좌표에 색상에 입력되어 있고 내 색상과 다를 경우
                    cnt += 1 # 겹치는 부분 + 1
                arr[i][j] += color # 색상 변경
    print(f'#{t} {cnt}')