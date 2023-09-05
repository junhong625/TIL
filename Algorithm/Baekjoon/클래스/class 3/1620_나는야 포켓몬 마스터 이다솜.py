# 조건 : 문자일 때 숫자 숫자일 때 문자로 답변하기
# 방법 : key(문자):value(숫자) 와 key(숫자):value(문자)인 두 개의 Dictionary를 만들기

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

name = {}
num = {}

for i in range(1, N+1):
    v = input().rstrip()
    name[v], num[i] = i, v

for _ in range(M):
    a = input().rstrip()
    if a.isdigit():
        print(num[int(a)])
    else:
        print(name[a])

