import sys

input = sys.stdin.readline

N = int(input())

stepping_stone = [0] + list(map(int, input().split()))

s, e = map(int ,input().split())

def bfs(s=s):
    q = [s]                         # q
    cnt = 0                         # 점프횟수
    while q:                        # q가 존재할 경우
        cnt += 1                    
        for _ in range(len(q)):     # q개수 만큼 반복
            cur = q.pop(0)          # 현재 징검다리 위치
            j = stepping_stone[cur] # 가중치
            jump = j                # 현재 점프 길이
            if j == 1:              # j가 1일 경우 무조건 가능하기에 바로 종료
                return cnt
            while jump+cur <= N:    # +jump에 대한 경우 모두 q에 추가
                if cur+jump == e:
                    return cnt
                q.append(cur+jump)
                jump += j

            jump = -j
            while cur+jump >= 1:    # -jump에 대한 경우 모두 q에 추가
                if cur+jump == e:
                    return cnt
                q.append(cur+jump)
                jump -= j
    return -1

print(bfs())

    
