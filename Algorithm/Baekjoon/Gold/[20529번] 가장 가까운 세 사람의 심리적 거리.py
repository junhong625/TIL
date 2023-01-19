import sys
from itertools import combinations

sys.stdin = open('TIL\Algorithm\Baekjoon\Gold\input.txt', 'r')

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    mbti_list = list(map(str, input().split()))
    minV = float('inf')                         # 최소값
    if N > 32:                                  # mbti의 개수가 32개가 넘어갈 경우 3개가 중복이 되는 경우가 최소 하나 발생
        print(0)
        continue
    comb_mbti = list(combinations(mbti_list, 3))# mbti 3개를 조합하는 모든 경우의 수
    for idx in range(len(comb_mbti)):           # 각 경우의 수를 모두 계산
        tot = 0
        a, b, c = comb_mbti[idx]
        for i in range(4):                       
            tot += 1 if a[i] != b[i] else 0
            tot += 1 if a[i] != c[i] else 0
            tot += 1 if c[i] != b[i] else 0
        minV = min(minV, tot)
    print(minV)