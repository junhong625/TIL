import sys

def dfs(s):
    print(s, end=' ')
    visited[s] = True
    for i in sorted(arr[s]):
        if not visited[i]:
            dfs(i)
            
def bfs(s):
    visited = [False for _ in range(N+1)]
    q = [s]
    visited[s] = True
    while q:
        s = q.pop(0)
        print(s, end=' ')
        for i in sorted(arr[s]):
            if not visited[i]:
                visited[i] = True
                q.append(i)
    

N, M, V = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [False for _ in range(N+1)]
dfs(V)
print()
bfs(V)