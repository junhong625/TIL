import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]  # 비행 점수 표시 그리드
up_best_root = [[float("-inf")]*M for _ in range(N)]        # 상승 비행 때 각 좌표마다의 가장 높은 점수를 기록할 판
down_best_root = [[float("-inf")]*M for _ in range(N)]      # 하강 비행 때 각 좌표마다의 가장 높은 점수를 기록할 판
up_best_root[N-1][0] = grid[N-1][0]                         # 시작 좌표 값 할당
down_best_root[N-1][M-1] = grid[N-1][M-1]                   # 시작 좌표 값 할당
up = [(0,1), (-1,0)]                                        # 상승 비행 시의 탐색 좌표
down = [(-1,0), (0,-1)]                                     # 하강 비행 시의 탐색 좌표

## dp탐색
def dp(direction):                                          # direction = "up" : 상승 비행, "down" : 하강 비행
    if direction == "up":                                   # 상승 비행 시 세팅
        q = deque([(N-1, 0)]) 
        delta = up
        best_root = up_best_root
    else:                                                   # 하강 비행 시 세팅
        q = deque([(N-1, M-1)]) 
        delta = down
        best_root = down_best_root
    while q:                                                # dajkstra 방식
        x, y = q.popleft()
        for dx, dy in delta:
            dx += x
            dy += y
            if 0 <= dx < N and 0 <= dy < M:
                value = grid[dx][dy] + best_root[x][y]
                if best_root[dx][dy] < value:               # 현재 좌표의 value와 grid 좌표에서의 value과 탐색하는 좌표의 value보다 높을 경우에만 value 적용 후 q에 추가
                    best_root[dx][dy] = value
                    q.append((dx, dy))

## 최대 값 탐색 함수
def maxV(N, M):                                             
    maxValue = float("-inf")
    for i in range(N):
        for j in range(M):
            value = up_best_root[i][j] + down_best_root[i][j]
            maxValue = max(maxValue, value)
    return maxValue

dp("up")
dp("down")
print(maxV(N,M))