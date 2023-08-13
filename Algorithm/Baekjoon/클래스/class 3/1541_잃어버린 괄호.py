# 조건 : 괄호 쳐서 최소값 찾기
# 방법 : + 인것들끼리 먼저 계산하게 되면 최소값 계산 가능

import sys

input = sys.stdin.readline

ex = input().rstrip().split("-")

for i in range(len(ex)):
    ex[i] = sum([int(a) for a in ex[i].split("+")])

res = ex[0]

if len(ex) > 1:
    for i in range(1, len(ex)):
        res -= ex[i]

print(res)

