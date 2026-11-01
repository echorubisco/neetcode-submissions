class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        p1,p2 = 0,1
        rev = 0
        while p2 < len(prices):
            if prices[p2] >= prices[p1]:
                rev = max(rev, prices[p2]-prices[p1])
            else:
                p1 = prices.index(min(prices[:p2+1]))
                rev = max(rev, prices[p2]-prices[p1])
            p2 += 1
        return rev
        