import sys
from itertools import permutations as p

input = sys.stdin.readline

N = int(input())

# 가능한 경우의 수가 9 * 8 * 7 이므로 브루트 포스 탐색
case = list(p(range(1,10), 3)) # 모든 경우의 수 case에 저장

for _ in range(N):
    num, s, b = map(int, input().split())
    num = list(map(int, list(str(num)))) # 한 자리씩 변환
    cur = 0 # 현재 인덱스
    while cur < len(case): # 현재 인덱스가 case의 길이보다 작을경우
        c = case[cur]
        strike, ball = 0, 0
        for i in range(3): # 순회하며 스트라이크, 볼의 개수 계산
            if c[i] == num[i]:
                strike += 1
            elif c[i] in num:
                ball += 1
        if s != strike or b != ball: # 스트라이크, 볼의 개수가 같을 경우에만 제거
            case.pop(cur)
            continue # 현재 인덱스의 케이스를 제거해줬기에 인덱스를 증가 하지 않고 while문 시작 지점으로 이동
        cur += 1

print(len(case)) # 남은 경우의 수 개수 출력