from collections import deque

def bfs(n, adjList):
    q = deque([1])
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    ans = 0
    while q:
        ans = len(q)
        for _ in range(ans):
            v = q.popleft()
            for w in adjList[v]:
                if not visited[w]:
                    q.append(w)
                    visited[w] = 1
    return ans

def solution(n, edge):
    adjList = {}
    for a, b in edge:
        if adjList.get(a):
            adjList[a].append(b)
        else: adjList[a] = [b]
        if adjList.get(b):
            adjList[b].append(a)
        else: adjList[b] = [a]
    
    return bfs(n, adjList)