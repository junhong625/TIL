dial = [[], [], 'ABC', 'DEF','GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input()
result = 0
for char in word:
    for i in range(2, len(dial)):
        if char in dial[i]:
            result += i + 1
print(result)
