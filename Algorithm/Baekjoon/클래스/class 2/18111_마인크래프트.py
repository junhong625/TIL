import sys

N, M, B = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
total, result = 0, 0
for r in arr:
    total += sum(r)

avg = round(total / (N*M))
for i in range(N):
    for j in range(M):
        if avg - arr[i][j] > 0:
            result += 1 * abs(avg - arr[i][j])
        else:
            result += 2 * abs(avg-arr[i][j])
print(result, avg)