def bfs(x, y): # bfs 탐색 함수
    global result
    if result == 1: # 도착 지점을 찾은 경우 다른 재귀 함수들 종료
        return
    if (x, y) == (13, 13): # 도착 지점에 도착했을 경우 종료
        result = 1
        return
    for dx, dy in [[0, 1],[1, 0],[0, -1],[-1, 0]]: # 델타로 방향 체크
        if arr[dx+x][dy+y] != 1: # 벽이 아닌 곳이 있다면 
            arr[x][y] = 1  # 현재 위치 벽으로 변경
            bfs(dx+x, dy+y) # 이동 가능한 위치로 이동
            arr[x][y] = 0  # 다른 경우의 수를 위하여 다시 원상복구
    else: return # 더 이상 갈 길이 없다면 종료

for _ in range(10):
    t = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    result = 0
    bfs(1, 1)
    print(f'#{t} {result}')
