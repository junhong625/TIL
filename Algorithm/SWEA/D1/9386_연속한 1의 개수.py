T = int(input())
for i in range(1, T+1): # 테스트 케이스 수만큼 반복
    length = int(input()) # 길이
    arr = list(map(int, input())) # 배열
    maxV = 0 # 최대값
    cnt = 0 # 횟수 
    for j in range(length): # 1일 경우에 1을 더하고 0일 경우에 0으로 변경한 이후 최대값과 비교 
        if arr[j] == 1:
            cnt += 1
        else:
            cnt = 0
        maxV = maxV if cnt <= maxV else cnt
    print(f'#{i} {maxV}')