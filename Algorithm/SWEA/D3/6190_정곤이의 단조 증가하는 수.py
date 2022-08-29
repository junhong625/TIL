T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    maxV = 0
    for i in range(N-1):
        for j in range(i+1, N):
            Sum = str(nums[i] * nums[j])
            for n in range(len(Sum)-1):
                if Sum[n] > Sum[n+1]:
                    break
            else:
                maxV = maxV if maxV > int(Sum) else int(Sum)
    print(f'#{t} {maxV}' if maxV else f'#{t} -1')