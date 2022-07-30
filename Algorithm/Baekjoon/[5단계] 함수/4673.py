def d(n):
    n = n + sum(list(map(int, str(n))))
    return n

not_self_number = set()
for i in range(1, 10001):
    not_self_number.add(d(i))

for i in range(1, 10001):
    if i not in not_self_number:
        print(i)