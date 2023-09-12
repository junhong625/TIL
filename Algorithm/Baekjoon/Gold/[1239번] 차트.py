# 조건: 원의 중심을 지나는 선의 최대 개수 구하기
# 고려사항: 1) 1 <= N <= 8 | 최대값 <= 100
#         2) 값이 50일 때는 무조건 1개
#         3) 모든 값들이 2번씩 중복될 때 중복되는 갯수만큼 
# 방법: 순열 값을 순차적으로 더한 sub list에서 a+50 == b인 개수 구해서 최대값으로 변경

import sys
from collections import Counter
from itertools import permutations

input = sys.stdin.readline

N = int(input())

N_list = sorted(list(map(int, input().split())))

std = N

N_cnt = Counter(N_list)
cnt = 0

for n in N_cnt:
    if N_cnt[n] % 2 == 1:
        break
    if n >= 50: 
        if n > 50:
            print(0)
        print(1) # 조건 1
        exit()
    cnt += int(N_cnt[n] / 2) # 조건 2
else:
    print(cnt)
    exit()

def check_ans(L): # 방법
    max_cnt = 0
    N_com = list(permutations(L))
    for com in N_com:
        cnt = 0
        sub = []
        c = 0
        for n in com:
            c += n
            sub.append(c)
        for n1 in sub[:-1]:
            for n2 in sub[1:]:
                if n1 + 50 == n2:
                    cnt += 1
        max_cnt = max(cnt, max_cnt)
    return max_cnt
    
print(check_ans(N_list))
