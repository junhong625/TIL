# 최소 신장 트리(MST)

> 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리
> 

### 그래프에서 최소 비용 문제

1. 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
2. 두 정점 사이의 최소 비용의 경로 찾기

### 신장 트리

- n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리

## Prim 알고리즘

### 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식

1. 임의 정점을 하나 선택해서 시작
2. 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
3. 모든 정점이 선택될 때 까지 1, 2 과정을 반복

### 서로소인 2개의 집합 정보를 유지

- 트리 정점들(tree vertices) - MST를 만들기 위해 선택된 정점들
- 비트리 정점들(nontree vertices) - 선택 되지 않은 정점들

### 코드

```python
def prim1(r, V):
    MST = [0] * (V+1)                           # MST 포함 여부
    key = [10000] * (V+1)                       # 가중치의 최대값 이상으로 초기화. key[v]는 v가 MST에 속한 정점과 연결될 값
    key[r] = 0                                  # 시작정점의 key
    for _ in range(V):                          # 시작 정점을 제외한 나머지 정점들 최소값 설정
        # MST에 포함되지 않은 정점 중 (MST[u] == 0), key가 최소인 u찾기
        u = 0
        minV = 10000
        for i in range(V+1):                    # MST에 포함되어 있지 않으면서 가중치가 최소인 i를 u로 설정
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        MST[u] = 1                              # 해당 정점 MST에 포함된 것으로 처리
        for v in range(V+1):                    # 모든 정점을 순회하며
            if MST[v] == 0 and adjM[u][v] > 0:  # MST에 포함되지 않았으며 u와 연결된 가중치가 0보다 클 경우
                key[v] = min(key[v], adjM[u][v])# 해당 정점에 저장된 가중치를 연결 가중치와 비교하여 더욱 작은 값으로 변경
    return sum(key)                             # 모든 가중치의 합을 반환

V, E = map(int, input().split())
adjM = [[0]*(V+1) for _ in range(V+1)] # 인접 행렬

for _ in range(E):
	u, v, w = map(int, input().split())
	adjM[u][v] = w
	adjM[v][u] = w                       # 가중치가 있는 무방향 그래프

prim(0, 6)
``` 