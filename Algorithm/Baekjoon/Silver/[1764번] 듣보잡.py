# 문제: 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하기

# 조건: 1) 입력줄 <= 20
#      2) 입력문자는 모두 소문자
#      3) N, M < 500,000
#      4) 중복 X
#      5) 듣보잡 사전순으로 출력

# 풀이: dictionary를 이용해 이름별 카운팅 2가 되면 듣보잡

# 방법: 1) 듣도 못한 사람과 보도 못한 사람의 명단 순회하면서 이름 횟수 카운트
#      2) 카운트 하면서 숫자가 2가 되는 경우 dbj 명단에 추가
#      3) dbj 명단 정렬 순서대로 출력

import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
name_count = defaultdict(int)
dbj = []

for _ in range(N):
    name_count[input().rstrip()] += 1

for _ in range(M):
    name = input().rstrip()
    if name_count[name]:
        dbj.append(name)
    name_count[name] += 1

print(len(dbj))
for name in sorted(dbj):
    print(name)