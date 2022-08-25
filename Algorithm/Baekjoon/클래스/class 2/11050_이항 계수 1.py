import sys

def f(a): # factorial 함수
    t = 1
    for i in range(1, a+1):
        t *= i
    return t

A ,B = map(int, sys.stdin.readline().split())
total = 1 

for i in range(B):
    total *= (A-i)

print(total // f(B))