# 문제: 주어지는 N번째 감소하는 수 찾기

# 조건: 1) 0 < N, M <= 1000000
#      2) 큰 자릿수부터 작은 자릿수까지 계속 감소해야한다.
#      3) 최대 감소수는 9876543210
#      4) 최대 개수는 1023개(2^10의 - 1)

# 방법: 1) 10자리로 가능한 모든 조합을 구한다.
#      2) 모든 조합들을 리스트 안에서 넣고 정렬한다.
#      3) 리스트에서 해당하는 N번째 수를 인덱스로 찾는다

import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

if N > 1022:
    print(-1)
    exit()

comb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(2, 11): # 방법 1
    for case in list(combinations(range(10), i)):
        case = sorted(case, reverse=True) # 방법 2
        num = ""
        for n in case:
            num += str(n)
        comb.append(int(num))

comb.sort()

print(comb[N]) # 방법 3