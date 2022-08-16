def len(s):
    cnt = 0
    for _ in s:
        cnt += 1
    return cnt

for _ in range(1, 11):
    T = int(input())
    target = input()
    sentence = input()
    idx = 0
    cnt = 0
    while idx != len(sentence) - len(target) + 1:
        if sentence[idx:idx + len(target)] == target:
            cnt += 1
        idx += 1
    print(f'#{T} {cnt}')