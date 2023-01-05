import sys

input = sys.stdin.readline

N = int(input())

while N:
    revenue = [int(input()) for _ in range(N)]

    dp = [revenue[0]] +[-10001] * (N-1)

    for i in range(1, N):
        dp[i] = max(dp[i-1]+revenue[i] , revenue[i]) # 현재 인덱스의 revenue 값과 현재 인덱스의 (revenue + dp) 값 중 더 큰 값이 최대값 
    print(max(dp))
    N = int(input())
