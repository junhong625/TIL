import sys

sys.stdin = open('hws/algorithm/0922/input.txt', 'r')

T = int(input())

## 순열 생성1 - 10개의 숫자: 5.82461sec
# def nPr(n, r, s=[0]): # n = 수의 개수, r = 배열의 목표 길이, s = 배열
#     if len(s) == r: # 목표 길이의 배열이 생성되면 리스트에 저장
#         permutation_list.append(s+[0])
#         return
#     for i in range(1, n):
#         if i not in s: # 중복되지 않는 수일 경우에 배열 생성
#             nPr(n, r, s+[i])

## 순열 생성2 - 10개의 숫자: 2.62838sec
def nPr(i, k):
    if i == k:
        permutation_list.append([0]+nums[:]+[0])
    else:
        for j in range(i, k):
            nums[i], nums[j] = nums[j],  nums[i]
            nPr(i+1, k)
            nums[i], nums[j] = nums[j],  nums[i]

## 최소 배터리 사용량 체크
def useBattery(case): 
    minV = 100 * N
    for c in case:
        s = 0
        for i in range(N):
            s += area[c[i]][c[i+1]]
        if s < minV:
            minV = s
    return minV

for t in range(1,T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    permutation_list = []
    nums = [i for i in range(N) if i != 0]
    nPr(0, N-1)
    print(f'#{t} {useBattery(permutation_list)}')
    
