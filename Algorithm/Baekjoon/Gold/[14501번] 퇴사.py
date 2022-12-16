import sys

input = sys.stdin.readline

def dfs(day=0, total=0, ing=0, done=[]):
    if day == N:
        if not ing:
            global maxV
            maxV = max(maxV, total)
        return 
    
    if not ing:
        dfs(day+1, total + cal[1][day], cal[0][day]-1, done+[day])
    dfs(day+1, total, ing if not ing else ing-1, done)

N = int(input())

cal = [[0] * N for _ in range(2)]
maxV = 0

for i in range(N):
    cal[0][i], cal[1][i] = map(int,input().split())
    
dfs()
print(maxV)

