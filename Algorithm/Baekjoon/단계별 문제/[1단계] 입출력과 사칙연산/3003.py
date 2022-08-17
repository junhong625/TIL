result = [1, 1, 2, 2, 2, 8]

find = list(map(int, input().split()))

for i in range(len(result)):
    print(result[i]-find[i], end=' ')