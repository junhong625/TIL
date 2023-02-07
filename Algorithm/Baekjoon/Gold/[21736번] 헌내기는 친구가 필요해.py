import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

delta = [(0,1), (1,0), (0,-1), (-1,0)]
visited = [[0] * M for _ in range(N)]
school = [list(input().rstrip()) for _ in range(N)]

x, y = 0, 0
total = 0

for i in range(N):
    for j in range(M):
        if school[i][j] == 'I':
            x, y = i, j
            visited[i][j] = 1
            break
## dfs로 시도 시 RecursionError 발생
# def dfs(x, y):
#     for dx, dy in delta:
#         dx += x
#         dy += y
#         if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy] and school[dx][dy] != 'X':
#             visited[dx][dy] = 1
#             if school[dx][dy] == 'P':
#                 global total
#                 total += 1
#             dfs(dx, dy)
# dfs(x, y)


## que를 사용
# deque를 사용하지 않으니까 2배 정도 느림
q = deque([(x, y)])

while q:
    x, y = q.pop()
    for dx, dy in delta:
        dx += x
        dy += y
        if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy] and school[dx][dy] != 'X':
            visited[dx][dy] = 1
            if school[dx][dy] == 'P':
                total += 1
            q.append((dx,dy))

print(total if total else 'TT')