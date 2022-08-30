# def bfs(s):
#     visited = [False] * (V+1)
#     visited[s] = True
#     q = []
#     q.append(s)

#     while q:
#         st = q.pop(0)

#         if visited[st]

for t in range(10):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    adjList = [[] for _ in range(V+1)]
    
    for i in range(E): # 인접노드 생성
        adjList[edges[i*2]].append(edges[i*2+1])

    visited = [False] * (V+1)
    for i in range(1,V+1):
        for w in adjList[i]:
            visited[w] = True

    start = [i for i in range(1,V+1) if not visited[i]] # 시작가능한 위치
    cnt = {i:0 for i in range(1,V+1)} 
    for i in range(E): 
        cnt[edges[i*2+1]] += 1  
    for n in cnt:
        dup = []