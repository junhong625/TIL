# 문제: 최대 S번의 교환으로 나오는 사전순 가장 뒷자리

# 조건 : 1) 1 <= N <= 50
#       2) 1 <= 원소값 범위 <= 1,000,000
#       3) 1 <= S <= 1,000,000

# 풀이 : 그리디 or 규칙

# 방법 : 1) 주어진 최대 교환 횟수인 A[:S+1] 범위 안에서의 가장 큰 값을 제일 앞자리로 이동(해당 원소의 인덱스가 이동 횟수)
#       2) 맨 앞자리는 바뀌지 않을테니 A에서 빼고 result에 집어넣기
#       3) S(교환 횟수) 인덱스 값만큼 줄이기
#       4) 반복하다 A에 비었는데 S가 남아있다면 모든 정렬이 끝난것이니 반복문 종료

import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

S = int(input())

result = []
while S:
    if not A:
        break
    maxV = max(A[:S+1])
    idx = A.index(maxV)
    S -= idx
    result.append(A.pop(idx))

print(*result + A)