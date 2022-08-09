T = int(input())

def min(args):
    min_num = args[0]
    for arg in args:
        min_num = arg if arg < min_num else min_num
    return min_num

def max(args):
    max_num = args[0]
    for arg in args:
        max_num = arg if arg > max_num else max_num
    return max_num
for i in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    print(f'#{i} {max(nums) - min(nums)}')
