def bfs(idx, cnt=0):                                    # bfs탐색 함수
    global result                                       # 정답을 호출
    visited = [False for _ in range(len(adjNode))]      # 연락 기록
    q = [[idx, 0]]                                      # q 생성 q[0] = 현재 노드 위치, q[1] = 연락 횟수
    visited[idx] = True                                 # 시작점 연락 체크
    while q:                                            # q가 존재할 경우에 계속 반복
        s, cnt = q.pop(0)                               # s = 현재 노드위치, cnt = 연락 횟수
        for w in adjNode[s]:                            # s가 연락 가능한 번호(w) 확인 
            if not visited[w]:                          # w에 연락한 적이 없다면
                q.append([w, cnt+1])                    # q에 [w, 연락 횟수 + 1]을 추가
                visited[w] = True                       # 연락 기록에 w 연락한 것으로 변경
                result = result if result[1] >= cnt+1 and result[0] >= w else [w, cnt+1] # 현재 정답과 비교하여 연락 횟수가 정답 이상이고 번호가 기존 번호 이상일 경우 변경
        

for t in range(1, 11):
    N, S = map(int, input().split())
    adjNode = [set() for _ in range(101)]               # 인접 연락망 생성 -> set을 활용하여 중복 연락망 제거
    edges = list(map(int, input().split()))             # 연락망 입력
    result = [0,0]                                      # 정답
    for i in range(N//2):                               # 연락망 수 만큼 반복
        adjNode[edges[i*2]].add(edges[i*2+1])           # 인접 연락망에 추가
    bfs(S)                                              # bfs로 확인
    print(f'#{t} {result[0]}')                          # 정답 출력
    
    