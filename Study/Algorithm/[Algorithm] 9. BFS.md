# Algorithm_9💡

# 너비 우선 탐색/BFS (Breadth First Search)

> 탐색 시작점의 인접한 정점들은 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
> 
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비 우선 탐색을 진행해야 하므로, FIFO 형태의 자료구조인 큐를 활용
- 미로 그래프 문제
    - A→B 경로가 있는가? : DFS, BFS
    - A→B 경로의 개수는? : DFS
    - A→B 최단 경로의 길이는? : BFS
- DFS → 반복(stack), 재귀로 풀이
- BFS → 반복(que) 풀이
- 알고리즘 구현
    
    ```python
    def bfs(v, N): # v 시작 정점, N 마지막 정점 번호
        visited = [0] * (N+1)   # visited 생성
        q = []								  # Queue 생성
        q.append(v)						  # 시작점 enQueue
        visited[v] = 1          # 시작점 처리 표시
        while q:                # 큐가 차 있다면
            v = q.pop(0)        # deQueue
            print(v)            # 출력 
            for w in adjList[v]:    # 인접 노드 확인
                if visited[w] == 0: # 방문하지 않았다면
                    q.append(w)     # enQueue
                    visited[w] = 1  # 방문 처리
    
    V, E = map(int, input().split())
    N = V + 1
    adjList = [[] for _ in range(N)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjList[a].append(b)
        adjList[b].append(a)
    bfs(0, 6)
    ```
- 재귀로 구현
    ```python
    min_v = 999999999
    input_list = [1, 2, 3]
    visited = [0] * len(input_list)

    def BFS(i, g, c): # i: 방문하는 노드, g: 도착지, c: 지나온 정점 갯수
        global min_v
        if i == g:  # 목적지에 도착한 경우
            if min_v > c:
                min_v = c
            else:
                visited[i] = 1  # 방문 체크
                for j in input_list[:]:
                    BFS(j, g, c+1)
                visited[i] = 0
