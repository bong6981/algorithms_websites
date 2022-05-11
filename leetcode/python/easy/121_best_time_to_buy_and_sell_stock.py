class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        ans = 0
        max_v = prices[-1]
        prices = prices[:-1]
        prices.reverse()
        for p in prices:
            ans = max(ans, max_v-p)
            max_v = max(max_v, p)
        return ans
