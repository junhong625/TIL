from collections import defaultdict

## 최소 이동 거리 탐색 함수
def dijkstra():
    minDIS = [float('inf') for _ in range(N+1)] # 각 노드까지의 최소 이동 거리가 저장될 리스트
    minDIS[0] = 0                               # 시작 지점의 최소 이동거리는 0
    q = [0 for _ in range((N+1)**2)]            # q 생성
    front, rear = -1, -1                        # 포인터 생성
    rear += 1                                   # enque
    q[rear] = 0

    while front != rear:                        # q가 존재하지 않을 때까지 반복
        front += 1                              # deque
        v = q[front]                
        for w, d in adjList[v]:                 # v에서 이동가능한 도로 순회
            if minDIS[w] > minDIS[v] + d:       # 이동 가능한 도로 w에 저장되어 있는 최소 이동거리가 v에서 이동했을 때 보다 크다면
                minDIS[w] = minDIS[v] + d       # v에서 이동한 거리로 최소 이동 거리 변경
                rear += 1                       # enque
                q[rear] = w
    return minDIS[N]                            # 도착 지점의 최소 이동 거리 값 출력

T = int(input())

for t in range(1, T+1):
    N, E = map(int, input().split())
    adjList = defaultdict(list)                 # 도로 생성
    for _ in range(E):                          # 일방통행 도로 생성
        s, e, d = map(int, input().split())
        adjList[s].append([e, d])
    print(f'#{t} {dijkstra()}')
        