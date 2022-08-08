def max(nums): # 내장 함수 max의 역할을 하는 함수
    max_num = nums[0]
    for num in nums:
        max_num = num if max_num < num else max_num
    return max_num

# 케이스가 10개 이므로 1부터 10까지 반복
for i in range(1, 11):
    # 빌딩 숲 길이
    length = int(input())
    # 빌딩 숲
    buildingForest = list(map(int, input().split()))
    # 조망권 세대 수
    total = 0

    # 현재 idx 위치의 빌딩 높이와 좌우 2칸씩 비교하여 모두 현재 idx 위치의 빌딩 높이보다 낮을 경우, 
    # 현재 idx 위치의 빌딩 높이에서 양옆의 두칸씩 (총 4칸)에서 가장 높은 높이를 빼준 값을 total에 더해주어 조망권이 확보된 세대 수를 반환
    for idx in range(2, length-2):
        # 좌측 2칸의 빌딩 높이가 현재 idx 위치의 빌딩 높이보다 낮을 경우
        if buildingForest[idx-1] < buildingForest[idx] and buildingForest[idx-2] < buildingForest[idx]: 
            # 우측 2칸의 빌딩 높이가  현재 idx 위치의 빌딩 높이보다 낮을 경우
            if buildingForest[idx+1] < buildingForest[idx] and buildingForest[idx+2] < buildingForest[idx]: 
                # 현재 idx 위치의 빌딩 높이에서 양옆의 두칸씩 (총 4칸)에서 가장 높은 높이를 빼준 값을 total에 더해주기
                total += (buildingForest[idx] - max([buildingForest[idx+1], buildingForest[idx+2], buildingForest[idx-1], buildingForest[idx-2]]))
    print(f'#{i} {total}')