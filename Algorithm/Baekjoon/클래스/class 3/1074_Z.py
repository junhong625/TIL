import sys

N, r, c = map(int, sys.stdin.readline().split())

total = (2**N)**2
start, end = 0, (2**N)**2
while total != 0:
    if r < total**(1/2)//2 and c < total**(1/2)//2:
        end -= (end-start)//4*3
    elif r < total**(1/2)//2 and c >= total**(1/2)//2:
        end, start = end-(end-start)//4*2, start+(end-start)//4
        c -= total**(1/2)//2
    elif r >= total**(1/2)//2 and c < total**(1/2)//2:
        end, start = end-(end-start)//4, start+(end-start)//4*2
        r -= total**(1/2)//2
    else:
        start += (end-start)//4*3
        r -= total**(1/2)//2
        c -= total**(1/2)//2
    total //= 4
print(start)
