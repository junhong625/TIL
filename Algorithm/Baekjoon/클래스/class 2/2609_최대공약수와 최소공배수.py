import sys

a, b = map(int, sys.stdin.readline().split())

mx, mn = max(a, b), min(a, b)

while mx % mn != 0:         # 최소 공배수 구하는 식(유클리드 호제법)
    mx, mn = mn, mx % mn    # 두 수들 중 작은 값이 큰 수르 나머지 없이 나눌 때 작은 수를 최소 공약수로 판단
print(mn)                   # 만약 위 식이 성립되지 않을 시 큰 수를 작은 수로 변경, 작은 수는 큰 수를 작은 수로 나눈 나머지로 변경하여 위 조건이 성립될 때까지 반복

print(a*b // mn)            # 최대 공약수 구하는 식
                            # 두 수를 곱한 값에서 최대공약수를 나눈 값