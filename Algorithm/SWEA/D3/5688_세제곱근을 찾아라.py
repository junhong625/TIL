### 1번째 풀이
T = int(input())
# 0부터 9까지 제곱을 했을 때 나올 수 있는 일의 자리 수를 dict형으로 저장
nums = {0:[0], 1:[1], 2:[2,4,8,6], 3:[3,9,7,1], 4:[4,6], 5:[5], 6:[6], 7:[7,9,3,1], 8:[8,4,2,6], 9:[9,1]}

for t in range(1, T+1):
    possibleN = []
    N = int(input())

    ## 0부터 9까지 순회하며 N의 일의 자리 수가 nums[i]에 들어있는 i를 possibleN에 추가
    for i in range(10):
        if int(str(N)[-1]) in nums[i]:
            possibleN.append(i)

    result = 0  # 세제곱의 결과 값이 들어갈 변수
    add = 0     # 일의 자리는 변화 없이 10의 자리만 변화해주기 위해 따로 설정한 변수

    ## 오름차순으로 계산을 해볼 것이기에 i를 세제곱한 결과 값이 N이상이 될 경우 정지 
    while result < N:
        for i in possibleN:
            result = (i+add)**3
            if result >= N:
                break
        else:       # 위의 반복문에서 탈출 하지 않았다면 add에 + 10 
            add += 10
 
    if result == N: # 위의 반복문이 끝난 후 result가 N과 같을 경우
        print(f'#{t} {i+add}') # i와add를 더한 값을 반환
    else:           # result가 N과 다를 경우
        print(f'#{t} -1')      # -1을 반환

### 2번째 풀이
T = int(input())
## N의 세제곱근을 구하여 반올림 후 계산하는 방식
for t in range(1, T+1): 
    N = int(input())
    n = round(N ** (1/3))

    if n**3 == N:
        print(f'#{t} {n}')
    else:
        print(f'#{t} -1')