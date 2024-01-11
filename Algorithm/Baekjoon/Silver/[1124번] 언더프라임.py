# 문제: 언더프라임인 것의 개수 구하기

# 조건: 1) 2 <= A <= B <= 100,000
#      2) 자연수 X를 소인수분해 했을 때 나오는 소수의 개수가 소수면 언더프라임

# 풀이: 에라토스테네스의 체를 활용하여 소수를 구하는데 소수가 아닌 수들을 계산할 때 해당 숫자에 들어가는 소수 개수를 구하기

# 방법: 1) 에라토스테네스의 체 공식을 활용해 B까지의 소수들을 구한다.
#      2) 소수에 해당하는 숫자 a를 최대값인 B까지 제곱하며 에라토스테네스의 체를 돌린다.
#      3) 에라토스테네스의 체 공식을 활용할 때 소수로 표시하는게 아니라 해당 숫자의 인덱스의 값에 +1을 함으로써 해당 숫자를 소인수분해 했을때의 소수 개수를 저장할 수 있다.

def find_decimal(n):
    # 방법 1
    for i in range(2, n+1):
        if not nums[i]:
            std = i
            # 방법 2
            while std <= n:
                for j in range(std, n+1, std):
                    # 방법 3
                    nums[j] += 1
                std *= i

import sys

input = sys.stdin.readline

A, B = map(int, input().split())
nums = [0 for _ in range(B+1)]
find_decimal(B)

cnt = 0
for n in range(A, B+1):
    if nums[nums[n]] == 1:
        cnt += 1

print(cnt)