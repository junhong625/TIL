# 문제: 다솜이가 목걸이를 만들 수 있는 방법의 경우의 수
# 시간 제한 2초 / 메모리 제한 128MB

# 조건: 1) 연속된 3개의 구슬 중 같은 색상이 있으면 안된다.
#      2) 처음 구슬과 마지막 구슬은 이어져있지 않다.
#      3) 3 <= N <= 5
#      4) 0 <= 각 구슬의 개수 <= 10
#      5) 구슬의 총 개수의 합 <= 35

# 방법: 1) 7차원으로 dp를 구현 = 5종류의 구슬의 개수를 나타내는 5차원 + 1개전, 2개전의 구슬 색을 나타내는 2차원
#      2) dp를 통해 각 구슬의 개수와 1개 전, 2개 전 구슬의 색에 따른 값 계산

import sys

input = sys.stdin.readline

N = int(input())
beads = [0 for _ in range(5)]

maxB = 0
for n in range(N):
    beads[n] = int(input())
    maxB = max(beads[n], maxB)
total = sum(beads)
maxB += 1
# 방법 1
dp = [[[[[[[-1 for _ in range(5)] for _ in range(5)] for _ in range(maxB)] for _ in range(maxB)] for _ in range(maxB)] for _ in range(maxB)] for _ in range(maxB)]

# 방법 2
def memo(size, p, pp): # size: 사용한 구슬의 개수, p: 이전 구슬의 색, pp: 2개 전 구슬의 색
    if size == total:
        return 1
    
    if dp[beads[0]][beads[1]][beads[2]][beads[3]][beads[4]][p][pp] != -1:
        return dp[beads[0]][beads[1]][beads[2]][beads[3]][beads[4]][p][pp]
    
    result = 0

    for i, b in enumerate(beads):
        if p == i or pp == i or b == 0: # 조건 1
            continue
        beads[i] -= 1
        result += memo(size+1, i, p)
        beads[i] += 1
    
    dp[beads[0]][beads[1]][beads[2]][beads[3]][beads[4]][p][pp] = result
    return result

print(memo(0, -1, -1))