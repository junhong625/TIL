class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        money = 0
        for i in range(len(prices)-1):              # 순회
            if prices[i] < prices[i+1]:             # 다음 값이 현재 값보다 클 경우에만
                money += prices[i+1] - prices[i]    # 이익 발생
        return money