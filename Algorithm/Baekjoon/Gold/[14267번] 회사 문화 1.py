import sys

input = sys.stdin.readline

n, m = map(int, input().split())

direct_supervisor = list(map(int, input().split()))
compliment_score = [0] * (n + 1)

for _ in range(m):
    i, w = map(int, input().split())
    compliment_score[i] += w

for i in range(1, n):
    compliment_score[i+1] += compliment_score[direct_supervisor[i]]

print(*compliment_score[1:])