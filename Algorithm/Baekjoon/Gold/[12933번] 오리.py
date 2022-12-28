import sys

input = sys.stdin.readline

duckduck = input().rstrip()

target = "quack"
duck_cnt = 0

while duckduck:
    quack = []
    idx = 0
    target_idx = 0
    while idx < len(duckduck):
        if duckduck[idx] == target[target_idx]:
            quack += [idx]
            target_idx = (target_idx + 1) % 5
        idx += 1
    if len(quack) < 5:
        break
    else:
        quack = quack[:len(quack) - len(quack) % 5]
        for i in quack[::-1]:
            duckduck = duckduck[:i] + duckduck[i+1:]
        duck_cnt += 1
print(duck_cnt if not duckduck else -1)
