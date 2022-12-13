import sys
from collections import deque

delta = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)] # 8방위 델타 설정

def bfs(x, y):
    q = deque([(x, y)])
    std = True                  # 봉우리 판단 기준
    while q:            
        x, y = q.popleft()
        visited[x][y] = 1       # 시작 좌표 방문처리
        for dx, dy in delta:    # 8방위 탐색
            dx += x
            dy += y
            if 0 <= dx < N and 0 <= dy < M: # 범위 안이고
                if mountain[dx][dy] > mountain[x][y]:   # 방위 중 더 높은 곳이 있다면 봉우리가 아님
                    std = False
                if not visited[dx][dy] and mountain[dx][dy] == mountain[x][y]:  # 방문한 적이 없고 높이가 같다면 큐에 추가
                    q.append((dx,dy))
    
    return std                  # 봉우리 판단 기준 반환

input = sys.stdin.readline

N, M = map(int, input().split())

mountain = []
visited = []
cnt = 0

for _ in range(N):  # 농장의 높이와 방문기록을 저장 
    mountain.append(list(map(int, input().split())))
    visited.append([0] * M)

for i in range(N):  # 농장을 순회
    for j in range(M):
        if not visited[i][j] and bfs(i, j): # 방문하지 않았거나 bfs결과가 True인 경우에만 봉우리 개수 + 1
            cnt += 1

print(cnt)

