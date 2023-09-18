# 문제: 특정건물을 가장 빨리 지을 때까지 걸리는 최소시간
# 시간 제한 1초 / 메모리 제한 512MB

# 조건: 1) 2 <= N <= 1000 | 건물의 개수
#      2) 1 <= K <= 100000 | 건설순서 규칙
#      3) 1 <= X, Y, W <= N | 
#      4) 0 <= Di <= 100000

# 방법: 1) bfs와 dp를 통해 모든 건물을 다 짓는데 걸리는 시간 구하기

import sys
from collections import deque

sys.setrecursionlimit(2000)

input = sys.stdin.readline

def min_time(W): # 방법 1
    dp = [0 for _ in range(N+1)]
    dp[W] = bt[W]

    q = deque([W])
    while q:
        v = q.popleft()
        for w in adjList[v]:
            if dp[w] < dp[v] + bt[w]:
                dp[w] = dp[v] + bt[w]
                q.append(w)
    return max(dp)

for _ in range(int(input())):
    N, K = map(int, input().split())
    bt = [0] + list(map(int, input().split()))
    adjList = [[] for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        adjList[Y].append(X)

    W = int(input())
    
    print(min_time(W))
