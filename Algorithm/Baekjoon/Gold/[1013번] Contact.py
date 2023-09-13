# 문제: 규칙에 맞는 전파 찾기
# 조건: 1) 1 <= N <= 200
#         2) 시작이 0일 경우 반드시 01이어야함
#         3) 시작이 1일 경우 100+1+ 조건에 성립해야함
# 방법: 조건 3번에 맞는 함수 생성 

import sys
from collections import deque

def con(s): # 조건 3
    global q
    idx = 3
    while idx < len(s) and s[idx] == "0":
        idx += 1
    while idx < len(s) and s[idx] == "1":
        q.append(s[idx+1:])
        idx += 1
    
input = sys.stdin.readline

for _ in range(int(input())):
    spread = input().rstrip()
    q = deque([spread])
    while q:
        spread = q.popleft()
        if len(spread) < 2:
            break
        elif spread[:2] == "01": # 조건 2
            q.append(spread[2:])
        elif spread[:3] == "100": # 조건 3
            con(spread)

    if not spread:
        print("YES")
        continue
    for s in q:
        if len(s) == 0:
            print("YES")
            break
    else:
        print("NO")