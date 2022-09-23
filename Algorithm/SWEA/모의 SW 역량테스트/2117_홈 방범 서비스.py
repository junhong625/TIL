## 손해 없이 가장 많은 집에 서비스를 제공해주는 함수
def security_area(x, y):                
    max_house = 0                                                           # 한 번에 방범 서비스를 가장 많이 받을 수 있는 집의 수  
    for n in range(N+1):                                                    # 서비스의 최대 길이는 배열의 길이
        service_house = 0                                                   # 서비스 받는 집의 수
        area = 0                                                            # 서비스 영역 크기
        for i in range(-(n), n+1):                                          # 마름모를 구하는 2중 for문
            for j in range(-(n), n+1):          
                if abs(i) + abs(j) <= n:                                    # 각 좌표의 절대값 합이 n이하일 경우
                    area += 1                                               # 서비스 영역
                    if 0 <= i+x < N and 0 <= j+y < N and arr[i+x][j+y] == 1:# 서비스 영역이 범위에서 벗어나지 않고 해당 집의 1
                        service_house += 1                                  # 서비스 받는 집의 수 + 1
        if area <= service_house * M:                                       # 서비스 영역의 크기가 서비스 받는 집들이 지불하는 비용보다 작거나 같을 경우
            max_house = max(max_house, service_house)                       # 한 번에 방범 서비스를 가장 많이 받을 수 있는 집의 수 업데이트
    return max_house                                                        # 가능한 마름모의 크기만큼 순회 후 max_house 반환
        
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_service_houses = 0
    for i in range(N):                                                      # 모든 좌표마다 security_area함수를 통해 가장 많이 서비스를 받을 수 있는 집들의 수 계산
        for j in range(N):
            service_houses = security_area(i, j)
            max_service_houses = max(max_service_houses, service_houses)    # 가장 많이 서비스를 받을 수 있는 집들의 수 max_service_houses에 저장
    print(f'#{t} {max_service_houses}')