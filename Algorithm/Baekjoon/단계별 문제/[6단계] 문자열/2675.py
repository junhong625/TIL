T = int(input())
for t in range(1, T+1):
    R, S = map(str, input().split())
    result = ''
    for char in S:
        result += char*int(R)
    print(result)