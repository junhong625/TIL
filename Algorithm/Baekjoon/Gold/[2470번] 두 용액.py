import sys

input = sys.stdin.readline

N = int(input())

solution = sorted(list(map(int, input().split())))
minV = float('inf')
st, ed = 0, N-1

while st < ed:         
    s1, s2 = solution[st], solution[ed]
    v = s1 + s2
    if abs(v) < minV:
        minV = abs(v)
        minN = s1, s2
        if minV == 0:
            break
    if v < 0:
        st += 1
    elif v > 0:
        ed -= 1
print(*minN)
            