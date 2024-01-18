# 문제: 회의실을 최대한 사용할 수 있는 횟수

# 조건 : 1) 1 <= N <= 100,000
#       2) 0 <= 시작(끝) 시간 <= 2^31-1

# 풀이 : 그리디

# 방법 : 1) 입력값들을 리스트에 모두 넣고 끝나는 시간 기준으로 오름차순 정렬 + 시작 시간 기준으로 오름차순 정렬
#       2) 정렬한 리스트에서 원소를 순차적으로 꺼내면서 시작 시간이 앞선 회의 끝 시간보다 같거나 늦은게 나올 경우 cnt + 1
#       3) 모두 순회 후 최대 개수 출력

import sys

input = sys.stdin.readline

N = int(input())

times = []
for _ in range(N):
    times.append(list(map(int, input().split())))

# 방법 1
times.sort(key=lambda x:(x[1], x[0]))
std, cnt = 0, 0

# 방법 2
for s, e in times:
    if s >= std:
        std = e
        cnt += 1

# 방법 3
print(cnt)