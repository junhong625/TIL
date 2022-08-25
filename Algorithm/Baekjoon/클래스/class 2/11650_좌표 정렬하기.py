import sys

N = int(sys.stdin.readline())

points = {}

for _ in range(N):
    x, y = map(int, input().split())
    if x in points:
        points[x].append(y)
    else:
        points[x] = [y]
for key in sorted(points):
    for value in sorted(points[key]):
        print(key, value)
