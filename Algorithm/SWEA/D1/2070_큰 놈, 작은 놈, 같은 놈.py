T = int(input())
for i in range(1, T+1):
    n, m = map(int, input().split())
    if  n > m:
        print(f'#{i} >')
    elif n < m:
        print(f'#{i} <')
    else:
        print(f'#{i} =')