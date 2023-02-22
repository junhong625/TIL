import sys

input = sys.stdin.readline

N = int(input())
r = list(map(int, input().split()))
line = [i for i in range(N)]
result = 0

def check():
    # print(line)
    for i in range(N):
        cnt = 0
        for j in range(i, -1, -1):
            if line[i] < line[j]:
                cnt += 1
        if cnt != r[line[i]]:
            return False
    return True

def perm(i, N):
    global result
    if result:
        return

    if i == N:
        if check():
            result = line[::]
        return
    else:
        for j in range(i, N):
            line[i], line[j] = line[j], line[i]
            perm(i+1, N)
            line[i], line[j] = line[j], line[i]

perm(0, N)
print(" ".join(str(i+1) for i in result))