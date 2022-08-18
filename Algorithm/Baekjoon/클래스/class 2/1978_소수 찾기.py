# 에르토스테네스의 체 사용

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# 주어진 숫자들 중 가장 큰 숫자까지 에르토스테네스의 체를 사용하여 소수 판별
prime = []
find_prime = [False, False] + [True] * (max(nums))
for i in range(2, max(nums)+1):
    if find_prime[i]:
        prime.append(i)
        for j in range(i*2, max(nums)+1, i):
            find_prime[j] = False

# 주어진 숫자를 하나씩 꺼내서 소수인지 확인하여 카운트
cnt = 0
for num in nums:
    if num in prime:
        cnt += 1

print(cnt)