class Solution(object):
    def productExceptSelf(self, nums):
        result = [1] * len(nums)
        
        # 왼쪽 계산
        left_mul = 1
        for i in range(1, len(nums)):
            left_mul *= nums[i-1]
            result[i] *= left_mul
        
        # 오른쪽 계산
        right_mul = 1
        for i in range(-2, -(len(nums))-1, -1):
            right_mul *= nums[i+1]
            result[i] *= right_mul

        return result