def bfs(s, e):
    global minV # 최소값 
    if visited[s] > minV: # 가지치기
        return
    if s == e:  # 도착 지점에 도착했을 경우
        minV = minV if minV < visited[s] else visited[s] # 최소값 비교
        return
    for w in adjList[s]: # 인접 노드 확인
        if visited[w] == 0: # 방문하지 않았을 경우
            visited[w] = visited[s] + 1
            bfs(w, e)
            visited[w] = 0  # 원상 복귀
    else:
        return 


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    adjList = [[] for _ in range(V+1)]
    
    for _ in range(E): # 노드 연결
        a, b = map(int, input().split())
        adjList[a].append(b)
        adjList[b].append(a)

    visited = [0]*(V+1)
    minV = V
    S, G = map(int, input().split())
    bfs(S, G)
    if minV == V: # 변동이 없을 경우
        print(f'#{t} 0') # 0을 출력
    else:         # 변동이 있을 경우 해당 값으로 출력
        print(f'#{t} {minV}')