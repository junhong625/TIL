## bfs 순회 탐색
def bfs(operator):
    q = []                                                                      # q 생성
    front = -1                                                                  # 속도를 높이기 위해서 rear를 제외한 front만 포인터로 사용
    q.append([nums[0], 1, operator])                                            # enque
    while front != len(q)-1:                                                    # q가 없어질 때 까지 반복
        front += 1                                                              # deque
        total, cnt, op = q[front]                                               # total : 숫자의 합, cnt : 연산에 포함한 카드의 개수, op : 연산자 개수
        if cnt == N:                                                            # 모든 카드를 연산 했을 경우
            global minV, maxV                                                   # 최대값, 최소값 호출
            minV = min(minV, total)                                             # 최소값 비교 및 변경
            maxV = max(maxV, total)                                             # 최대값 비교 및 변경
        else:                                                                   # 연산해야 할 카드가 남았을 경우
            if op[0]:                                                           # + 연산자가 남아 있을 경우
                q.append([total + nums[cnt], cnt+1, [op[0]-1]+op[1:]])          
            if op[1]:                                                           # - 연산자가 남아 있을 경우
                q.append([total - nums[cnt], cnt+1, op[:1]+[op[1]-1]+op[2:]])   
            if op[2]:                                                           # * 연산자가 남아 있을 경우
                q.append([total * nums[cnt], cnt+1, op[:2]+[op[2]-1]+op[3:]])   
            if op[3]:                                                           # / 연산자가 남아 있을 경우
                q.append([int(total / nums[cnt]), cnt+1, op[:3]+[op[3]-1]])     



T = int(input())

for t in range(1, T+1):
    N = int(input())
    operator_cnt = list(map(int, input().split()))                              # 연산자 개수가 담긴 리스트
    nums = list(map(int, input().split()))                                      # 숫자 카드 리스트
    maxV, minV = -1000000000, 1000000000                                        # 최소값, 최대값
    bfs(operator_cnt)                                                           # bfs로 가능한 모든 경우의 수 확인
    print(f'#{t} {maxV - minV}')