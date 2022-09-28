# 최단 경로

> 간선의 가중치가 있는 그래프에서 두 정점 상의 경로들 중에 간선의 가중치의 합이 최소인 경로
> 

## 하나의 시작 정점에서 끝 정점까지의 최단 경로

### 다익스트라(dijkstra) 알고리즘

- 음의 가중치 허용 X

### 벨만-포드(Bellman-Ford) 알고리즘

- 음의 가중치 허용 O

## 모든 정점들에 대한 최단 경로

### 플로이드 워샬(Floayd Warshall) 알고리즘

# Dijkstra 알고리즘

> 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식이다.
> 
- 시작 정점(s)에서 끝 정점(t)까지의 최단 경로에 정점 x가 존재한다.
- 이때, 최단 경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단 경로 구성된다.
- 탐욕 기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사

### 코드 - 예시 문제(swea1795)

```python
def dijkstra(s, adjList):                           # s : 시작 지점, adjList : 함수 내에서 사용할 인접리스트
    min_DIS = [float('inf') for _ in range(N+1)]    # 각 노드까지의 최단 경로가 저장될 리스트
    min_DIS[s] = 0                                  # 시작 지점은 0으로 설정
    q = [0] * 10**6                                 # q 생성
    front, rear = -1, -1                            # 포인터 설정
    rear += 1                                       # enque
    q[rear] = s
    
    while front != rear:                            # q가 없을 때 까지 반복
        front += 1                                  # deque
        v = q[front]
        for y, c in adjList[v]:                     # v의 인접리스트 순회 
            if min_DIS[v] + c < min_DIS[y]:         # 지금의 경로가 이전 경로보다 짧을 경우
                min_DIS[y] = min_DIS[v] + c         # 최소 경로 변경
                rear += 1                           # enque
                q[rear] = y
    return min_DIS[1:]                              # 최단 경로 값 반환

T = int(input())

for t in range(1, T+1):
    N, M, X = map(int, input().split())
    adjList = [[] for _ in range(N+1)]
    adjList_R = [[] for _ in range(N+1)]
    result = []

    for _ in range(M):                      # 인접 행렬 삽입
        x, y, c = map(int, input().split())
        adjList[x].append((y, c))           # 인수의 집까지의 최단 경로를 탐색하는 인접 리스트 
        adjList_R[y].append((x, c))         # 인수의 집에서 친구들의 집까지 최단 경로를 탐색하는 인접 리스트

    result = dijkstra(X, adjList)           # 친구의 집 -> 인수의 집에 해당하는 최단 경로
    result2 = dijkstra(X, adjList_R)        # 인수의 집 -> 친구의 집에 해당하는 최단 경로

    maxV = 0                                # 가장 오래 걸리는 시간
    for i in range(N):                      # 가장 오래 걸리는 시간 탐색
        maxV = max(maxV, result[i] + result2[i])
    print(f'#{t} {maxV}')
``` 