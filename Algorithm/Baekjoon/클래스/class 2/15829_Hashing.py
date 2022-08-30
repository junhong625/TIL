import sys

N = int(sys.stdin.readline())
word = sys.stdin.readline()
result = 0
for i in range(N):
    result += ((ord(word[i])-96) * (31 ** (i))) 
print(result % 1234567891) 