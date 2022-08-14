T = int(input())
 
for t in range(1, T+1):
    nums = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    test_case, case_len = map(str, input().split())
    nums_list = list(map(str, input().split()))
    for num in nums_list:
        nums[num] += 1
 
    print(test_case)
    for n in nums:
        for i in range(nums[n]):
            print(n, end=' ')