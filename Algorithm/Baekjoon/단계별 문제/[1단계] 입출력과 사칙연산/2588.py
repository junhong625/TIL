a = int(input())
b = input()
total = 0
for num in range(len(b)):
    total += a*int(b[-num-1]) * 10 ** num
    print(a*int(b[-num-1]))
print(total)