import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())                            # 미로 크기
x, y = map(int, input().split())                            # 시작 좌표
tx, ty = tuple(map(int, input().split()))                   # 도착 좌표
maze = [list(map(int, input().split())) for _ in range(N)]  # 미로 
visited = [[[0]*M for _ in range(N)] for _ in range(2)]     # 방문 기록(visited[0]: 마법 미사용 전용, visited[1]: 마법 사용 전용)
delta = [(0,1),(1,0),(0,-1),(-1,0)]                         # 4방위

def bfs(x, y):
    q = deque([(x, y, 0)])
    cnt = 0

    while q:
        for _ in range(len(q)):
            x, y, broken = q.popleft()
            if (tx, ty) == (x, y):
                return cnt
            for dx, dy in delta:
                dx += x
                dy += y
                if 0 <= dx < N and 0 <= dy < M:
                    if maze[dx][dy] == 0 and visited[broken][dx][dy] == 0: # 이동가능하고 방문하지 않은 곳
                        visited[broken][dx][dy] = 1
                        q.append((dx, dy, broken))
                    elif maze[dx][dy] == 1 and not broken: # 이동할 수 없으나 마법을 쓰지 않은 경우
                        visited[broken][dx][dy] = 1
                        q.append((dx, dy, 1))
        cnt += 1
    return -1

print(bfs(x-1, y-1))