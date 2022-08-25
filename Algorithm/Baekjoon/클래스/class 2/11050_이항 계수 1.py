i

def bino_coef(n, k):
    if k == 0 or n == k:
        return 1
    t = 1
    for i in range(k):
        t *= (n-i)
    return t // 2

A, B = map(int, input().split())
print(bino_coef(A, B))