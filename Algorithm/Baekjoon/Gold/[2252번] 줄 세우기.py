import sys

input = sys.stdin.readline

N, M = map(int, input().split())

caseList = sorted([list(map(int, input().split())) for _ in range(M)])
union = [[]] * (N+1)

def make_union(u, idx):
    if idx in u:
        return
    u.append(idx)
    for i in union[idx]:
        sub = (make_union(u, i))
        if sub:
            u.append(sub)
    return u

for p, c in caseList:
    union[p].append(c)

for idx, childs in enumerate(union):
    if idx:
        print(make_union([], idx))
