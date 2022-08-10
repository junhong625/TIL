T = int(input())

delta= [[0,1],[1,0],[0,-1],[-1,0]]

for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    
    cnt = 1 # 현재 칸에 들어갈 숫자
    idx = 0 # delta의 index
    x, y = 0, 0 # 2차원 리스트 좌표
    while cnt <= N**2: # cnt가 박스 개수보다 커지면 종료
        arr[x][y] = cnt # 좌표에 현재 값 추가
        cnt += 1 
        if 0 <= x + delta[idx][0] < N and 0 <= y + delta[idx][1] < N and arr[x+ delta[idx][0]][y + delta[idx][1]] == 0: # x나 y의 다음 값이 범위를 벗어나지 않고 다음 좌표의 값이 0일 경우 통과
            pass
        else: #x나 y의 다음 값이 범위를 벗어나거나 다음 좌표의 값이 0이 아닐 경우 방향전환
            #print('방향전환')
            idx = (idx + 1) % 4 # 방향 전환을 위해 delta의 index를 변경
        x += delta[idx][0] # x를 다음 좌표로 이동
        y += delta[idx][1] # y를 다음 좌표로 이동
        
    print(f'#{t}')
    for row in arr:
        print(*row)
        
            