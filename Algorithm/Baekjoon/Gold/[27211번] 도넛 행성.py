import sys
from collections import deque

## 풀이 방식
# - 전체 맵을 순회하며 탐색하다가 해당 좌표가 비어있는 곳이라면 bfs탐색을 진행해 해당 구역을 확인
# - (해당 좌표는 확인했기에 다른 구역들과 겹치지 않거나 중복으로 구역 체크하지 않도록 숲으로 변경)

## 중요 포인트
# - 한 바퀴를 돌면 원래 자리로 돌아오게 됨
#   -  x, y 좌표의 값들을 각 row와 column의 길이로 나눈 나머지 값들을 활용하면 해결 가능 (ex : x = x % row 길이)

input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            dx = (x + dx) % N       # 한 바퀴 돌았는지 체크
            dy = (y + dy) % M       # 한 바퀴 돌았는지 체크
            if not grid[dx][dy]:
                q.append((dx,dy))
                grid[dx][dy] = 1

N, M = map(int, input().split())

delta = [(0,1),(0,-1),(1,0),(-1,0)]
grid = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if not grid[i][j]:
            cnt += 1
            bfs(i, j)

print(cnt)