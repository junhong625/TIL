import sys
from collections import deque

T = int(sys.stdin.readline())

for t in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    nums = deque(map(int, sys.stdin.readline().split())) # deque이용
    
    idx = deque([n for n in range(N)])  # 각각의 숫자들 인덱스 위치
    cnt = 1                             # 출력 횟수
    while nums:
        front = nums.popleft()          # 제일 앞 숫자 꺼내서 확인
        if nums and max(nums) > front:  # front보다 큰 값이 있다면
            nums.append(front)          # 뒤에 추가
            idx.append(idx.popleft())   # idx의 위치도 이동
        else:                           # front보다 큰 값이 없다면
            i = idx.popleft()           # 해당 숫자의 인덱스를 꺼내서 확인
            if i == M:                  # 목표로 하는 인덱스가 맞다면
                print(cnt)              # 현재 출력 횟수 출력
            cnt += 1                    # 아닐 경우 출력 횟수만 + 1
        # print(f'nums : {nums}')
        # print(f'idx : {idx}')
    