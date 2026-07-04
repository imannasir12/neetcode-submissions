class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = prices[0]

        for i in range(1, len(prices)):
            curr_profit = prices[i]  - min
            if curr_profit > profit:
                profit = curr_profit
            if prices[i] < min:
                min = prices[i]
        
        return profit