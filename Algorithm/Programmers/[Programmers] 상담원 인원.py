# 문제: 상담원 인원을 잘 분배해 최소 대기시간을 구하기

# 조건: 1) 1 <= k <= 5
#      2) k <= n <= 20
#      3) 3 <= reqs.lenth <= 300
#      4) 1 <= a <= 1000, 1 <= b <= 100, 1 <= c <= k
#      5) reqs는 a를 기준으로 오름차순 정렬, a는 중복되지 않음

# 방법: 1) 각 요청들을 상담 유형에 따라 분류, 분류하면서 [상담 시작 시간, 종료 시간, 최종 종료 시간] 형태로 저장
#      2) dfs를 통해 가능한 상담원 분배 경우의 수 계산 -> 계산 시 대기 시간 연산 돌입
#      3) 각 요청들을 분배 가능한 상담원 인원에 따라 상담원 인원이 남아 있을 경우와 상담원들 모두 상담 중인 경우에 따라 처리


from collections import deque
import copy

answer = 10000000 # 최대값 설정

def solution(k, n, reqs):
    reqs_kind = [[] for _ in range(k)]
    # 방법 1
    for a, b, c in reqs:
        reqs_kind[c-1].append([a,b,a+b])
    
    working_mento = [0 for _ in range(k)]
    
    def mento(idx, cnt):
        # 방법 2
        if idx == k:
            if sum(working_mento) != n:
                return
            total = 0
            for i in range(k):
                req_list = copy.deepcopy(reqs_kind[i])
                q = deque()
                max_size = working_mento[i]
                end_time = 0
                while req_list:
                    q = deque(sorted(q, key=lambda x:x[2]))
                    # 방법 3
                    if len(q) < max_size:
                        q.append(req_list.pop(0))
                    else:
                        end_time = q.popleft()[2]
                        req = req_list.pop(0)
                        if end_time > req[0]:
                            total += end_time - req[0]
                            req[2] = req[1] + end_time
                        q.append(req)
            global answer
            answer = min(answer, total)
            return
        
        # 방법 2
        for i in range(1, cnt-(k-idx-1)+1):
            working_mento[idx] = i 
            mento(idx+1, cnt-i)
    mento(0, n)
    
    return answer