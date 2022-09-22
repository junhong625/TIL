import sys

sys.stdin = open('hws/algorithm/0922/input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    containers = sorted(list(map(int, input().split())), reverse=True)  # 오름차순 정렬
    trucks = sorted(list(map(int, input().split())))                    # 내림차순 정렬
    total = 0
    while trucks and containers:# 트럭과 적재 가능한 화물이 존재할 때만 반복
        truck = trucks.pop()    # 적재용량이 가장 큰 트럭 선택
        for c in range(len(containers)):    # 남은 containers 중 탐색
            if containers[c] <= truck:      # 현재 트럭의 최대 적재 용량 이하의 화물일 경우
                total += containers[c]      # 트럭에 화물 적재 
                containers.pop(c)           # 해당 화물 제거
                break
    print(f'#{t} {total}')


    