import sys

M, N = map(int, sys.stdin.readline().split())

if M % 2 == 0:
    M += 1

for i in range(M, N+1, 2):
    for num in range(2, i):
        if i % num == 0:
            break
    else:
        print(i)
