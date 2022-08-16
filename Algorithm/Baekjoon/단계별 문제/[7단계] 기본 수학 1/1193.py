target = int(input())

n, m = 1, 1
while target >  n:
    m += 1
    n += m

if m % 2 == 0:
    a, b = target-(n-m), m + 1 - (target-(n-m))
else:
    a, b = m + 1 - (target-(n-m)), target-(n-m)

print(f'{a}/{b}')