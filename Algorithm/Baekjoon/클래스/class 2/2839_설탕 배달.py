import sys
N = int(sys.stdin.readline())

cnt = [N // 5, N % 5 // 3]

while cnt[0] * 5 + cnt[1] * 3 != N and cnt[0] != -1:
    cnt[0] -= 1
    cnt[1] = (N - cnt[0] * 5) // 3

if cnt[0] == -1:
    print(-1)
else:
    print(sum(cnt))