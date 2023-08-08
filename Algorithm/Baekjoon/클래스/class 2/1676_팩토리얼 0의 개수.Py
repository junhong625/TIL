import sys

input = sys.stdin.readline

# factorial 계산 함수
def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

# 0의 개수 계산 함수
def zero_cnt(n):
    if n == 0:
        return 0
    cnt = 0
    for i in list(str(n))[::-1]:
        if i == "0": cnt += 1
        else: break
    return cnt

N = int(input())

f = factorial(N)

print(zero_cnt(f))