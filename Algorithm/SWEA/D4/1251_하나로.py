def prim(s=0):                                                                          
    MST = [0 for _ in range(N)]                                                                     # MST 생성
    MST[0] = 1                                                                                      # 시작 지점 MST에 포함
    key = [float('inf') for _ in range(N)]                                                          # key 생성
    key[s] = 0                                                                                      # 시작 지점 key 0으로 설정
    for _ in range(N):                                                                              # 정점 수 만큼 반복
        u = 0                                                                                       # 출발 정점이 될 변수
        minV = float('inf')                                                                         # 최소 값
        for i in range(N):                                                                          # 정점 수 만큼 순회
            if MST[i] == 0 and key[i] < minV:                                                       # 정점 i가 MST에 포함되지 않고 해당 i의 key가 minV보다 작을 경우
                u, minV = i, key[i]                                                                 # u, minV 변경
        MST[u] = 1                                                                                  # MST에 포함되지 않고 key가 가장 작은 u 정점 MST에 포함
        for i in range(N):                                                                          # 정점 수 만큼 순회
            if MST[i] == 0:                                                                         # MST에 포함되지 않고
                if islands[u][0] == islands[i][0] or islands[u][1] == islands[i][1]:                # 섬이 같은 X선 또는 Y선에 존재할 경우 
                    dis = abs(islands[u][0] - islands[i][0]) + abs(islands[u][1] - islands[i][1])   # 해저 터널 길이
                else:                                                                               # 두 섬의 대각선 길이가 필요한 경우
                    dis = (abs(islands[u][0] - islands[i][0]) ** 2 + abs(islands[u][1] - islands[i][1]) ** 2) ** (1/2)  # 피타고라스의 정리로 해저 터널 길이 구하기
                key[i] = min(key[i], dis)                                                           # 현재 key에 저장된 값과 dis 값 중 더 작은 값을 key에 저장
    result = 0                                                                                      # 총합
    for i in range(N):                                                                              # 모든 정점을 순회하며
        result += key[i] ** 2 * E                                                                   # 해저 터널 길이의 제곱값 X 세율 값을 result에 더해 지불해야할 환경부담금 계산  
    return round(result)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    islands = []
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    for i in range(N):
        islands.append([X[i], Y[i]])
    E = float(input())
    print(f'#{t} {prim()}')