import sys

N = int(sys.stdin.readline())
people = []
result = [1 for _ in range(N)]

for _ in range(N):
    people.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                result[i] += 1

print(*result)