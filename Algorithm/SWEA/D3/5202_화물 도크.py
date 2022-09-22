import sys

sys.stdin = open('hws/algorithm/0922/input.txt', 'r')

## greedy 재귀 탐색으로 최대 화물 적재 횟수 구하는 함수
def greedy(s): # s : 시작 시간
    for i in sorted(schedule, key=lambda x:schedule[x]): # i : 끝나는 시간이 가장 빠른 시작 시간
        if i >= s: # 시작 시간(i)이 s 이상일 경우
            global cnt
            cnt += 1 # 횟수 + 1
            greedy(schedule[i]) # 다음 가장 빠른 시간 탐색
            return

T = int(input())

for t in range(1, T+1):
    N = int(input())
    schedule = {}
    cnt = 0
    for _ in range(N):
        s, e = map(int, input().split())
        if s not in schedule or schedule[s] > e: # 시작시간이 스케줄에 없거나 끝나는 시간이 시간이 스케줄에 담겨 있는 시간보다 작을 경우
            schedule[s] = e # 스케줄에 시작시간과 끝나는 시간 기록
    cnt = 0
    greedy(0)
    print(f'#{t} {cnt}')

