# 문제: 한수가 이동거리 K만큼 이동하여 목적지에 도착하는 경우의 수 구하기

# 조건: 1) 1 <= R, C <= 5
#      2) 1 <= K <= R * C
#      3) 이동 못하는 좌표 = T

# 풀이: dfs를 활용

# 방법: 1) 4방위로 탐색하는 dfs 구현
#      2) visited에서 방문여부만 확인하는 것이 아닌 몇번째 이동에 방문했는지 기록
#      3) 현재 이동거리가 K일때 위치가 우측 상단의 목적지가 아닐 경우엔 탐색 종료(K이상 탐색은 무의미하기 때문)
#      4) 목적지에 도달하여 탐색이 끝냈을 경우 visited 초기화 후 이전 함수 실행


import sys

input = sys.stdin.readline

R, C, K = map(int, input().split())

# 방법 1
def dfs(x, y):
    # 방법 3
    if visited[x][y] == K:
        if (x, y) == (0, C-1):
            global cnt
            cnt += 1
        return
    for dx, dy in [(0,1), (-1,0), (0,-1), (1,0)]:
        dx += x
        dy += y
        if 0 <= dx < R and 0 <= dy < C and not visited[dx][dy] and grid[dx][dy] != "T":
            # 방법 2
            visited[dx][dy] = visited[x][y] + 1
            dfs(dx, dy)
            # 방법 4
            visited[dx][dy] = 0
    
grid = []
visited = [[0 for _ in range(C)] for _ in range(R)]
cnt = 0
for _ in range(R):
    grid.append(input().rstrip())

visited[R-1][0] = 1
dfs(R-1, 0)
print(cnt)