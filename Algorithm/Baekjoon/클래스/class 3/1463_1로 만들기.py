import sys

input = sys.stdin.readline

# sys.stdin = open('input.txt', 'r')

N = int(input())

dp = [0 for _ in range(N+1)]

ans = 0

q = [[N, 0]]
while q:
    x, cnt = q.pop(0)
    if x == 1:
        ans = cnt
        break
    if x % 3 == 0:
        if not dp[x//3] or dp[x//3] > cnt+1:
            dp[x//3] = cnt+1
            q.append((x//3, cnt+1))
    if x % 2 == 0:
        if not dp[x//2] or dp[x//2] > cnt+1:
            dp[x//2] = cnt+1
            q.append((x//2, cnt+1))
    if not dp[x-1] or dp[x-1] > cnt+1:
        dp[x-1] = cnt+1
        q.append((x-1, cnt+1))

print(ans)