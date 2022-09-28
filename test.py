def prim1(r, V):
    MST = [0] * (V+1)                           # MST 포함 여부
    key = [10000] * (V+1)                       # 가중치의 최대값 이상으로 초기화. key[v]는 v가 MST에 속한 정점과 연결될 값
    key[r] = 0                                  # 시작정점의 key
    for _ in range(V):                          # 시작 정점을 제외한 나머지 정점들 최소값 설정
        # MST에 포함되지 않은 정점 중 (MST[u] == 0), key가 최소인 u찾기
        u = 0
        minV = 10000
        for i in range(V+1):                    # 가중치가 최소인 i를 u로 설정
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