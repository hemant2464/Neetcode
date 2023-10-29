class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        prev_prev_sell = 0
        prev_sell = 0
        prev_buy = -prices[0]

        for price in prices[1:]:
            temp = prev_sell
            prev_sell = max(prev_sell, prev_buy + price)
            prev_buy = max(prev_buy, prev_prev_sell - price)
            prev_prev_sell = temp

        return prev_sell