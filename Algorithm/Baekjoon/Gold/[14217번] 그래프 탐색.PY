import sys
from collections import defaultdict, deque

def best_load(num):
    if num == 1:
        return
    q = deque([num])
    cnt = 0
    visited = [0 for _ in range(n+1)]
    visited[num] = 1

    while q:
        cnt += 1
        for _ in range(len(q)):
            v = q.popleft()
            minV = 0
            for w in adjLoad[v]:
                if w == 1:
                    dp[num] = cnt
                    return
                elif not visited[w]:
                    q.append(w)
                    visited[w] = 1
    dp[num] = -1


input= sys.stdin.readline

n, m = map(int, input().split())

adjLoad = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    adjLoad[a].append(b)
    adjLoad[b].append(a)

q = int(input())

for _ in range(q):
    v, x, y = map(int, input().split())
    dp = [0 for _ in range(n+1)]
    if v == 1:
        adjLoad[x].append(y)
        adjLoad[y].append(x)
    else:
        adjLoad[x].remove(y)
        adjLoad[y].remove(x)
    for i in range(1, n+1):
        best_load(i)

    print(*dp[1:])
