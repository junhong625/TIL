import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    if N % H == 0 :
        print(100*H+N//H)
    else:
        print(100*(N % H)+(N//H+1))