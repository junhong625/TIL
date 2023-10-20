from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    limit = len(q1) * 3
    if (s1 + s2) % 2:
        return -1
    
    while s1 != s2:
        if answer > limit: # 탐색횟수가 최대 횟수를 넘을 경우 탐색 불가한 케이스로 판단
            return -1
        if s1 > s2:
            temp = q1.popleft()
            q2.append(temp)
            s1 -= temp
            s2 += temp
        else:
            temp = q2.popleft()
            q1.append(temp)
            s1 += temp
            s2 -= temp
        answer += 1
    return answer