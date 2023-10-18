# 문제: L과 R 사이 중에 8이 제일 적게 들어있는 자연수의 8의 개수

# 조건: 1) 1 <= L <= 2000000000
#      2) L <= R <= 2000000000

# 방법: 1) L과 R의 길이가 같을 때
#      2) 앞에서부터 자리수가 같은 범위를 찾고
#      3) 그 범위 내에서 같은 자리수에 존재하는 8의 개수가 정답이라는 규칙 발견


import sys

input = sys.stdin.readline

L, R = map(str, input().split())

res = 0

# 방법 1
if len(L) == len(R):
    # 방법 2
    for i in range(len(L)):
        if L[i] == R[i]:
            # 방법 3
            if L[i]  == '8':
                res += 1
        else: break

print(res)