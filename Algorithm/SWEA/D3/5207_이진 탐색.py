## 이진 탐색
def binary_search(target):                  # target : 목표 값
    l, r = 0, N-1                           # 배열의 시작 idx와 끝 idx를 l과 r로 지정
    m = (l + r) // 2                        # 중간 위치 m으로 지정
    move = [0, 0]                           # 연속 이동 횟수를 확인할 변수
    while l <= r and A[m] != target:        # 둘이 교차되기 전 또는 목표 값을 찾기 전까지 반복
        if A[m] > target:                   # 목표 값보다 중간 값이 클 경우
            r = m - 1                       # r을 m-1로 할당
            move[0] += 1                    # 연속 이동 횟수
            move[1] = 0                     # 반대 방향 이동 횟수 초기화
        elif A[m] < target:                 # 목표 값보다 중간 값이 작을 경우
            l = m + 1                       # l을 m+1로 할당
            move[0] = 0                     # 반대 방향 이동 횟수 초기화
            move[1] += 1                    # 연속 이동 횟수
        if abs(move[0] - move[1]) >= 2:     # 한 쪽의 이동 횟수가 2이상이 될 경우 종료
            return False                    # False를 반환
        m = (l + r) // 2                    # 중간 값 다시 설정

    return True if A[m] == target else False# 반복문이 끝난 후 목표 값을 찾은 경우 True를 반환 아닐 경우 False를 반환

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for b in B:                             # B를 순회하며
        if binary_search(b):                # 각 원소에 대한 이진 탐색 실시하여 True를 반환할 경우
            cnt += 1                        # cnt + 1
    print(f'#{t} {cnt}')
