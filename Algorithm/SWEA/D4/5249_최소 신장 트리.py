import collections

## 최소 신장 트리 생성 함수
def prim(s=0):                                  # 시작 지점 임의로 설정                     
    key[s] = 0                                  # 본인의 위치로 이동하는데 드는 가중치는 0
    for _ in range(V+1):                        # 노드 개수만큼 반복
        u  = 0                                   # MST에서 가장 작은 key값을 가진 노드
        minV = float('inf')                     # 현재 노드들의 key값들보다 더 큰 값을 설정
        for i, v in enumerate(MST):             # 노드 개수만큼 반복
            if v == 0 and key[i] < minV:        # 현재 MST에 포함되어 있지 안고 최소값보다 작은 가중치를 가지고 있을 경우
                u, minV = i, key[i]             # 해당 idx를 u로 설정, 최소값도 해당 idx의 가중치로 설정
        MST[u] = 1                              # u를 MST에 포함
        for i, w in adjList[u]:                 # u에서 이동할 수 있는 인접 리스트 순회
            if MST[i] == 0:                     # MST에 포함되어 있지 않고 이동할 때 드는 가중치가 현재 key에 저장된 값보다 낮을 경우
                key[i] = min(key[i], w)         # key의 값을 이동할 때 드는 가중치로 변경

def find_set(x):                                # 대표 원소 탐색
    while rep[x] != x:                          # x와 대표 원소가 같아 질 때 까지 반복
        x = rep[x]
    return x

def union(x, y):                                # y의 대표 원소를 x의 대표 원소로 변경
    rep[find_set(y)] = find_set(x)

def kruskal():                                  
    kruskal_list.sort()                         # 가중치 오름차 순으로 정렬
    cnt = 0                                     # 연결된 간선 개수(즉, 전체 노드 수 - 1)
    total = 0                                   # 가중치 합
    for w, n1, n2 in kruskal_list:              # 정렬된 간선 순회
        if find_set(n1) != find_set(n2):        # n1과 n2의 대표 원소가 다를 경우
            cnt += 1                            # 간선 연결
            union(n1, n2)                       # n2의 대표 원소를 n1으로 변경
            total += w                          # 가중치 합에 더하기
        if cnt == V:                            # 모든 노드가 연결된 경우 
            break                               # 종료
    return total

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    adjList = collections.defaultdict(list)     # 연결 리스트
    kruskal_list, rep = [], [i for i in range(V+1)]
    MST = [0 for _ in range(V+1)]               # 최소 신장 트리
    key = [float('inf') for _ in range(V+1)]    # 최소 가중치가 들어갈 리스트
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        kruskal_list.append([w, n1, n2])
        adjList[n1].append([n2, w])
        adjList[n2].append([n1, w])
    # prim()                                    # prim()으로 탐색 시
    # print(f'#{t} {sum(key)}')
    print(f'#{t} {kruskal()}')