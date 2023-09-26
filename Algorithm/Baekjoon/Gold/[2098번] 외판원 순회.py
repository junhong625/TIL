# 문제: 가장 적은 비용 순회 찾기
# 시간 제한 1초 / 메모리 제한 128MB

# 조건: 1) 2 <= N <= 16 | 도시의 수
#      2) 1 <= W[i][j] <= 1000000 | 비용의 최대 값
#      3) 갈 수 없는 경우 비용 0

# 방법: 비트마스킹 + DP + DFS

import sys

input = sys.stdin.readline

N = int(input())

adjList = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e9)
dp = {}

def dfs(x, visited):
    if visited == (1 << N) - 1:
        if adjList[x][0]:
            return adjList[x][0]
        else:
            return INF
    
    if (x, visited) in dp:
        return dp[(x, visited)]
    
    min_cost = INF
    for i in range(1, N):
        if adjList[x][i] == 0 or visited & (1 << i):
            continue
        cost = dfs(i, visited | (1 << i)) + adjList[x][i]
        min_cost = min(cost, min_cost)

    dp[(x, visited)] = min_cost
    return min_cost

print(dfs(0, 1))