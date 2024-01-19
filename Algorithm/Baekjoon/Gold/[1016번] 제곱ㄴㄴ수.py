# 문제: min부터 max 사이에서 정수의 제곱으로 나누어지지 않는 수의 개수 구하기

# 조건 : 1) 1 <= min <= 1,000,000,000,000
#       2) min <= max <= min + 1,000,000

# 풀이 : 에라토스테네스의체 활용

# 방법 : 1) 에라토스테네스의 체 규칙을 활용
#       2) dp에 해당하는 숫자들을 집어넣는다.(set으로 중복 방지)
#       3) max-min+1-len(dp) 식을 통해서 제곱 ㄴㄴ 수의 개수 구하기

import sys, math

input = sys.stdin.readline

min, max = map(int, input().split())

dp = set()

num = 2
square = 4
# 방법 1
while square <= max:
    for i in range(square*math.ceil(min/square), max+1, square):
        # 방법 2 
        dp.add(i)
    num += 1
    square = num*num
#방법 3
print(max-min+1-len(dp))