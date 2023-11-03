import sys

input = sys.stdin.readline

N = int(input())

word_list = [input().rstrip() for _ in range(N)]

cnt = N
while word_list:
    flag = False
    for i in range(len(word_list)):
        if flag:
            break
        for j in range(len(word_list)):
            if i == j:continue
            if word_list[i] == word_list[j][:len(word_list[i])]:
                word_list.pop(i)
                cnt -= 1
                flag = True
                break
    else:
        break
print(cnt)