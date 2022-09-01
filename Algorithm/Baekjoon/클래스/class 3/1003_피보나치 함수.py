import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    result = [0, 1, 1]

    for i in range(3, N+1):
        result.append(result[i-1]+result[i-2])
    print(result[N-1], result[N])