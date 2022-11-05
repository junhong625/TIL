import sys

input = sys.stdin.readline

def dfs(idx, total):
    if idx == len(nums):
        # print(total)
        sit.append(total)
        return

    for i in range(4):
        if operators[i]:
            if i == 0:
                operators[i] -= 1
                dfs(idx+1, total+nums[idx])
                operators[i] += 1
            elif i == 1:
                operators[i] -= 1
                dfs(idx+1, total-nums[idx])
                operators[i] += 1
            elif i == 2:
                operators[i] -= 1
                dfs(idx+1, total*nums[idx])
                operators[i] += 1
            else:
                operators[i] -= 1
                dfs(idx+1, int(total/nums[idx]))
                operators[i] += 1

N = int(input())

nums = list(map(int, input().split()))
operators = list(map(int,input().split()))
sit = []

dfs(1, nums[0])

print(max(sit))
print(min(sit))
