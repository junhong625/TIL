import sys

input = sys.stdin.readline

N, M = map(int, input().split())

name = {}
num = {}

for i in range(1, N+1):
    v = input().rstrip()
    name[v], num[i] = i, v

for _ in range(M):
    a = input().rstrip()
    if a.isdigit():
        print(num[int(a)])
    else:
        print(name[a])

