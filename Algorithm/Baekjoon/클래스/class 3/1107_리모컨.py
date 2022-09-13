# 발생한 반례
# 1. dfs 함수에서 가고 싶은 채널의 자리수보다 작은 값을 numbers에 추가할 때 빈 값을 int로 형 변환시에 value error 발생
# 2. 모든 버튼이 고장나 buttons에 값이 없을 경우 dfs를 돌면 value error 발생
# 3. 10만대의 채널이 주어질 때 가능한 버튼이 많으면 경우의 수가 너무 많아 시간초과 발생

import sys

def dfs(l, num=''): # dfs 재귀 함수
    if len(num) == l+1:
        if int(num) > 1000000:
            return
        numbers.append(len(num)+abs(N-int(num)))
        return 
    elif len(num) == l or (num and len(num) == l-1):
        numbers.append(len(num)+abs(N-int(num)))

    for i in buttons:
        dfs(l, num+str(i))

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

if M: # 고장난 버튼이 있을 경우
    broken_buttons = list(map(int, sys.stdin.readline().split()))
    buttons = [i for i in range(10) if i not in broken_buttons]
else: # 고장난 버튼이 없을 경우
    buttons = [i for i in range(10)]

numbers = []
min_cnt = abs(N-100)

if buttons:
    dfs(len(str(N))) # 재귀 함수 후
    min_cnt = min_cnt if min_cnt < min(numbers) else min(numbers) # numbers에 추가된 리모컨 버튼 클릭 수들 중 가장 작은 값을 min_cnt와 비교
print(min_cnt)