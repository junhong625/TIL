import sys

input = sys.stdin.readline

# python의 round의 버그를 해결한 4사5입에 해당하는 함수
def round(n):
    return int(n)+1 if n - int(n) >= 0.5 else int(n)

# 절사평균 30%를 적용한 함수
def avg(D):
    if not D:
        return 0
    std = round(n * 0.15)
    new_D = D[std:n-std]
    return round(sum(new_D) / len(new_D))

n = int(input())
d = [int(input()) for _ in range(n)]
d.sort()
print(avg(d))