import sys

input = sys.stdin.readline

N, K = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]
items.sort()

dp = [[0]*(K+1) for _ in range(N)]

for i in range(N):
    for j in range(1, K+1):
        if items[i][0] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i][0]] + items[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N-1][K])