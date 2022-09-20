import sys

sys.stdin = open('SSAFY/hws/algorithm/0920/extra/input.txt', 'r')

T = int(input())

def case2(num): # 2진수의 모든 경우의 수를 계산하여 10진수로 바꾼 값을 dup_nums에 추가
    global dup_nums
    for i in range(len(num)):
        if num[i] == '1':
            copy_num = num[:i] + '0' + num[i+1:]
            dup_nums[int(copy_num, 2)] = True
        else:
            copy_num = num[:i] + '1' + num[i+1:]
            dup_nums[int(copy_num, 2)] = True

def case3(num): # 3진수의 모든 경우의 수를 계산하며 10진수로 바꾼 값이 dup_nums에 존재할 경우 해당 값을 반환
    for i in range(len(num)):
        memo = ['0', '1', '2']
        memo.remove(num[i])
        for j in memo:
            copy_num = num[:i] + j + num[i+1:]
            if int(copy_num, 3) in dup_nums:
                return int(copy_num, 3)

for t in range(1,T+1):
    num2 = input()
    num3 = input()
    dup_nums = {}
    case2(num2)
    print(f'#{t} {case3(num3)}')