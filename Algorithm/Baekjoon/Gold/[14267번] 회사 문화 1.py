import sys

input = sys.stdin.readline

n, m = map(int, input().split())

direct_supervisor = [0] + list(map(int, input().split()))
compliment_score = [0] * (n+1)
direct_supervisor[1] = 1

for _ in range(m):
    i, w = map(int, input().split())
    compliment_score[i] += w

for i in range(len(direct_supervisor)):
    compliment_score[i] += compliment_score[direct_supervisor[i]]

print(*compliment_score[1:])