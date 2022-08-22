import sys

N = int(sys.stdin.readline())

for i in range(10 ** (len(str(N))-1), N):
    sum_nums = sum(list(map(int, str(i))))
    if i + sum_nums == N:
        print(i)
        break
else:
    print(0)