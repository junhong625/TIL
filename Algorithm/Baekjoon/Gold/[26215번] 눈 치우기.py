import sys
import heapq

input = sys.stdin.readline

N = int(input())

home = list(map(int, input().split()))
cnt = 0

for i in range(len(home)):              # heapq를 최대힙으로 사용하기 위해 리스트의 원소들을 -로 변경 
    home[i] = -home[i]

heapq.heapify(home)                     # list를 heap으로 변경

while N:
    snow1 = heapq.heappop(home)+1   
    if N > 1:                           # 눈이 남은 집의 수가 2개 이상일 경우
        snow2 = heapq.heappop(home)+1
        if snow2 != 0:                  # 현재 if문을 이전 if문 밖에서 실행 시 NameError 발생 
            heapq.heappush(home, snow2) # home에 추가
        else:                           # 집 앞에 눈이 0이 되면 눈 제거가 필요한 집의 수 -1
            N -= 1 

    if snow1 != 0:                      # 집 앞에 눈이 남은 경우
        heapq.heappush(home, snow1)     # home에 추가
    else:                               # 집 앞에 눈이 없는 경우
        N -= 1                      

    cnt += 1                            # 1분 추가

print(cnt if cnt <= 1440 else -1)