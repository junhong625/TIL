# 조건: 최대 동전을 움직일 수 있는 횟수 계산
# 고려사항: 1) 동전이 있는 위치에 쓰여진 X만큼 이동
#         2) 이동하는 방향은 4방향(위, 아래, 왼쪽, 오른쪽) 중에 자유롭게 선택
#         3) 이동 중에는 구멍에 빠지지 않음
#         4) 구멍에 빠지거나 보드의 바깥으로 빠진다면 게임 종료
# 방법: 1) bfs를 통해 최대 개수 구하기(X) -> bfs가 아닌 dfs와 dp를 활용해 최대 개수 구하기
#      2) visited를 구현하고 내가 밟았던 곳을 다시 밟는 다면 무한히 움직일 수 있다고 판단
#      3) H나 밖으로 나가는 횟수를 계산하지 않았기에 최종 maxCnt값에서 +1 한 값이 정답
#      4) recursion error를 해결하기 위해 recursionlimit값 조정

import sys
from collections import deque

sys.setrecursionlimit(10**6) # 조건4
input = sys.stdin.readline

def dfs(x, y): # 조건 1

    global maxCnt

    d = int(grid[x][y])
    adjList = [[x+d, y], [x-d, y], [x, y+d], [x,y-d]]
    for dx, dy in adjList:
        if 0 <= dx < N and 0 <= dy < M and grid[dx][dy] != "H" and dp[x][y] + 1 > dp[dx][dy] :
            if visited[dx][dy]: # 조건 2
                print(-1)
                exit()
            visited[dx][dy] = 1
            dp[dx][dy] = dp[x][y] + 1
            maxCnt = max(dp[dx][dy], maxCnt)
            dfs(dx, dy)
            visited[dx][dy] = 0

N, M = map(int, input().split())
grid = [input().rstrip() for _ in range(N)]

visited = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]
visited[0][0] = 1
maxCnt = 0

dfs(0, 0)
print(maxCnt+1) # 조건 3