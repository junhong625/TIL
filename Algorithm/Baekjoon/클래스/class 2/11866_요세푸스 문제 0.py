import sys

N, K = map(int, sys.stdin.readline().split())

arr = [i for i in range(1, N+1)]
idx = K-1

out = []

while arr:
    print(idx)
    out.append(arr.pop(idx))
    if arr:
        idx = (idx + K-1) % len(arr)
print('<', end='')
for i in range(len(out)):
    if i == len(out)-1:
        print(f'{out[i]}>')
    else:
        print(out[i], end=', ')
