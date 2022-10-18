import sys
from collections import defaultdict

## bfs 탐색으로 본인 제외한 모든 노드들을 몇 번 만에 방문하는지 체크

def bfs(s, visited): # s : 탐색 시작 지점
    q = []
    front = -1
    q.append(s)
    while len(q)-1 != front:
        front += 1
        v = q[front]
        for w in adjList[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v]+1
    return sum(visited)-2 # 본인 노드를 방문하는데 2번이 걸리기에 -2

sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
adjList = defaultdict(list)

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    adjList[s].append(e)
    adjList[e].append(s)

minV = N**2
KB = 0
for i in range(1, N+1):
    v = bfs(i, [0] * (N+1))
    if minV > v:
        minV = v
        KB = i
print(KB)


