import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
x, y = map(int, input().split())                                                 # 시작 좌표
delta = [(-2,-1), (-2,+1), (-1,-2), (-1,+2), (+1,-2), (+1,+2), (+2,-1), (+2,+1)] # 나이트의 이동 경로
visited = [[-1 for _ in range(N)] for _ in range(N)]                             # 방문 기록
target = [tuple(map(int, input().split())) for _ in range(M)]                    # 목표의 좌표

## bfs 탐색
# 시작 좌표에서 모든 좌표에 대한 이동 횟수를 계산한 후에 target 좌표의 이동 횟수 출력
def bfs(x, y):                                                                   # x: 시작 좌표 x, y: 시작 좌표 y
    q = deque([(x, y)])
    visited[x][y] = 0
    
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in delta:
                dx += x
                dy += y
                if 0 <= dx < N and 0 <= dy < N and visited[dx][dy] == -1:
                    q.append((dx,dy))
                    visited[dx][dy] = visited[x][y]+1


bfs(x-1, y-1)

for i in range(M):
    a, b = target[i]
    print(visited[a-1][b-1], end=" ")