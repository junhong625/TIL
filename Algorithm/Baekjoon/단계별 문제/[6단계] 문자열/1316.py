T = int(input())
cnt = 0
for t in range(1, T+1):
    word = input()
    cur = word[0]
    visited = ""
    for char in word:
        if cur != char:
            if cur in visited:
                break
            visited += cur
            cur = char
    else:
        if cur not in visited:
            cnt += 1
print(cnt)