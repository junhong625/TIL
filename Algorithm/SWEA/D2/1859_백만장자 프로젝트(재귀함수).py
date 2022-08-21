def maxidx(arr): # 최대값의 인덱스
    maxI, maxV = 0, 0
    idx = 0
    for n in arr:
        if n > maxV:
            maxV, maxI = n, idx
        idx += 1
    return maxI

def milliondollar(arr, N, result): # 사재기 재귀함수
    if N == 0:
        return result
    maxI = maxidx(arr)
    for i in range(maxI):
        if arr[i] < arr[maxI]:
            result += arr[maxI] - arr[i]
    return milliondollar(arr[maxI+1:], N-maxI-1, result)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    print(f'#{t} {milliondollar(arr, N, result)}')