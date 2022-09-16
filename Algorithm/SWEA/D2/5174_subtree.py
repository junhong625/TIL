def node_count(cur):                        # node의 개수를 count 해주는 함수, cur = 현재 노드
    global cnt                              # cnt 호출
    if adjList[cur][0]:                     # 현재 노드의 왼쪽 자식 노드가 존재할 경우
        cnt += 1                            # 개수 + 1
        node_count(adjList[cur][0])         # 해당 노드로 이동하여 탐색
    if adjList[cur][1]:                     # 현재 노드의 오른쪽 자식 노드가 존재할 경우
        cnt += 1                            # 개수 + 1
        node_count(adjList[cur][1])         # 해당 노드로 이동하여 탐색

T = int(input())

for t in range(1, T+1):
    E, N = map(int, input().split())                # 노드 개수와 시작 노드 번호 입력
    edges = list(map(int, input().split()))         # 간선 입력
    adjList = [[0, 0] for _ in range(E+2)]          # 각 노드의 자식 노드들 생성
    cnt = 1                                         # 루트 노드도 개수에 포함
    for i in range(E):                              # 자식 노드 연결
        if not adjList[edges[i*2]][0]:              # 왼쪽 자식 노드가 존재하지 않을 경우
            adjList[edges[i*2]][0] = edges[i*2+1]   # 왼쪽 자식 노드에 값을 할당
        else:                                       # 왼쪽 자식 노드가 존재할 경우
            adjList[edges[i*2]][1] = edges[i*2+1]   # 오른쪽 자식 노드에 값을 할당
    node_count(N)                                   # node 개수 카운트
    print(f'#{t} {cnt}')                            # 카운트한 노드의 개수를 출력