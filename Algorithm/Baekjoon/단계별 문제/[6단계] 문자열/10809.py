S = input()
alpha = [-1] * 26 # 알파벳 개수

for char in S:
    alpha[ord(char)-97] = S.index(char)
print(*alpha)