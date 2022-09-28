import sys

sys.stdin = open('Algorithm/SWEA/D6/input.txt', 'r')
 
## 최단 경로 탐색 함수
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