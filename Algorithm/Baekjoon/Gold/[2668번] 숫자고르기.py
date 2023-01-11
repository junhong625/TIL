import sys

input = sys.stdin.readline

N = int(input())

num_set = [0] + [int(input()) for _ in range(N)]

# cycle을 찾고 모든 cycle을 더하는 해결 방식
def find_cycle():
    idx = 1
    result = set()

    while idx <= N:
        if idx in result:           # cycle에 포함된 result 건너 뛰기
            idx += 1
            continue
        cycle = []                  # 새로운 cycle 탐색
        num = idx                   # idx를 시작 숫자로 지정
        while True:
            if num not in cycle:    # cycle에 들어있지 않은 num일 경우
                cycle.append(num)   # cycle에 추가
                num = num_set[num]  # 다음 숫자 탐색
            else:                   # cycle에 들어있는 숫자일 경우
                if cycle[0] == num: # cycle의 시작과 num이 같다면 제대로 된 cycle로 인정
                    for n in cycle: # cycle의 숫자들을 result에 추가
                        result.add(n)
                break               # 추가 후 종료
        idx += 1                    # 다음 idx 탐색
    return sorted(list(result))     # 리스트로 변환 후 순서대로 정렬

ans = find_cycle()
print(len(ans))
for n in ans:
    print(n)