total = int(input())

N = int(input())
for n in range(N):
    a, b = map(int, input().split())
    total -= a*b
if total == 0:
    print('Yes')
else:
    print('No')