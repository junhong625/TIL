## bfs로 최소 연산 횟수 탐색
def bfs(num, target):                   # num : 시작 숫자, target : 목표 숫자
    visited = [0] * (10**6+1)           # 방문 횟수
    visited[num] = 1                    # 시작 지점 방문 처리
    q = [0] * (10**6+1)                 # q 생성
    front, rear = -1, -1                # deque와 enque의 기준이 될 변수
    rear += 1                           # enque
    q[rear] = num

    while front != rear:                # front와 rear의 값이 같아지기 전까지 반복
        front += 1                      # deque
        v = q[front]
        if v == target:                 # v가 목표 값과 같을 경우
            return visited[v]-1         # v값의 최소 방문 횟수를 반환
        elif v > target+10:             # 목표 값의 10보다 클 경우에는 다음 수로 이동
            continue
        for w in [v+1, v-1, v*2, v-10]: # 연산 결과를 w에 할당
            if 0 <= w <= 1000000 and not visited[w]: # w가 0이상이고 1000000이하이며 방문시 더 적은 방문횟수로 방문이 가능하다면
                rear += 1               # enque
                q[rear] = w
                visited[w] = visited[v] + 1 # 방문횟수 업데이트

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{t} {bfs(N, M)}')