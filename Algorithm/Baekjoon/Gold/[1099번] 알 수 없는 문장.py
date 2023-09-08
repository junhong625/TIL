# 조건: 문장을 해석할 때 최소 비용 계산
# 고려사항: 1) 단어는 중복해서 문장에 포함되어 있을 수 있고 없을 수도 있다.
#         2) 서로 다른 단어끼리는 섞을 수 없다.
#         3) 최소값을 구해야한다.
# 방법: dp를 이용해 각 구간별 최소값을 계산

import sys

# 단어 비용 계산 함수
def check(word1, word2):
    l = len(word1)
    cnt = 0
    for i in range(l):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt

input = sys.stdin.readline

sentence = " " + input().rstrip() # dp 시작점인 0을 넣기 위해 공백으로 패딩
N = int(input()) # 입력 개수
words = [input().rstrip() for _ in range(N)] # 단어들
dp = [float("inf")] * len(sentence) # dp 계산할 리스트
dp[0] = 0 # 시작점

for i in range(len(sentence)-1):
    if dp[i] == float("inf"):
        continue
    for word1 in words:
        l = len(word1)
        word2 = sentence[i+1:i+1+l] # 비교할 단어
        if sorted(word1) == sorted(word2): # 비교할 수 있는 단어
            dp[i+l] = min(dp[i+l], check(word1, word2)+dp[i])

print(dp[-1] if dp[-1] != float("inf") else -1) # 문장 끝까지 비용 계산이 됐을 경우 마지막 값 출력 or 아니라면 -1 출력

