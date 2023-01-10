import sys

input = sys.stdin.readline

word1 = 'a'+input().rstrip()    # a로 패딩처리
word2 = 'a'+input().rstrip()    # a로 패딩처리

l1 = len(word1)
l2 = len(word2)

LCS = [[0] * l2 for _ in range(l1)] # LCS 탐색 결과가 들어갈 리스트

for i in range(l1):
    for j in range(l2):
        if i==0 or j==0:        # 패딩처리한 곳 넘기기
            continue
        elif word1[i] == word2[j]:
            LCS[i][j] = LCS[i-1][j-1]+1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])              # LCS