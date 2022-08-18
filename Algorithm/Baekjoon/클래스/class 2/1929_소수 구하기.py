# 에라토스테네스의 체
# 0과 1을 False 그 이후의 수들을 모두 True로 두고
# 가장 작은 수인 2를 소수로 판단하고 2의 배수를 모두 False로 변환
# 다음 True인 수들 중 가장 작은 수인 3을 소수로 판단하고 3의 배수를 모두 False로 변환
# 위와 같은 작업을 계속하여 소수를 골라낸다면 시간 복잡도를 O(N log N)으로 해결이 가능
import sys

M, N = map(int, sys.stdin.readline().split())

prime = []
nums = [False, False] + [True] * N

for i in range(2, N+1):
    if nums[i]:
        if i >= M:
            prime.append(i)
        for j in range(i*2, N+1, i):
            nums[j] = False
for prime_num in prime:
    print(prime_num)