import sys
from collections import Counter

def check_floor(h):
    time = 0
    for s in counter.keys():
        if h < s:
            time += (s-h) * 2 * counter[s]
        elif h > s:
            time += (h-s) * counter[s]
        else:
            continue
    times.append(time)
    heights.append(h)

N, M, B = map(int, sys.stdin.readline().split())
arr, times, heights = [], [], []
for _ in range(N):
    arr.extend(list(map(int, sys.stdin.readline().split())))
counter = Counter(arr)
result, max_h, min_h = sum(arr), max(counter.keys()), min(counter.keys())

for s in range(min_h, max_h+1):
    if B + result < s * N * M:
        break
    check_floor(s)
    
times, heights = times[::-1], heights[::-1]
idx = times.index(min(times))
print(times[idx], heights[idx])