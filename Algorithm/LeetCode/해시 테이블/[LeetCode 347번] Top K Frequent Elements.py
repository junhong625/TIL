## 72ms(99.48%) 16.6bm(86.89%)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        
        count = Counter(nums)
        count = sorted(count, key=lambda x:count[x], reverse=True)
        return count[:k]