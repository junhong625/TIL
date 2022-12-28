import sys

input = sys.stdin.readline

nums = list(map(int, input().split()))

def dfs(i=0, total=0, cnt=0):
    global flag
    if i == 3 or flag == True:
        return
    
    if i and total == 0 and cnt:
        flag=True
        return

    dfs(i+1, total+nums[i], cnt+1)
    dfs(i+1, total-nums[i], cnt+1)
    dfs(i+1, total, cnt)

flag = False
dfs()
print('S' if flag else 'N')