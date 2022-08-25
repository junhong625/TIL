def bfs(x, y, cnt): # x, y : 현재 탐색 좌표, cnt : 현재 탐색 횟수 
    global min_V
    if arr[x][y] == 3: # 현재 좌표가 3일 경우 종료
        min_V = min_V if min_V < cnt-1 else cnt-1
        return
    for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]: # 4방향 체크
        if 0<=x+dx<N and 0<=y+dy<N and arr[x+dx][y+dy] != 1: # 범위 안이고 다음 방향이 0일 경우
            arr[x][y] = 1 # 현재 좌표를 벽으로 막고 
            bfs(x+dx, y+dy, cnt+1) # 다음 좌표로 이동
            arr[x][y] = 0 # 다음 경우의 수를 위해 원상복귀  

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    min_V = N*N # 최소 방문 횟수
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2: # 시작점을 찾을 경우
                bfs(i, j, 0)   # bfs 탐색 시작
            
    print(f'#{t} {min_V if min_V != N*N else 0}') # min_V가 변동 없을 경우 0을 출력, 변동이 있을 경우 min_V를 그대로 출력
    