class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        p1,p2 = 0,1
        rev = 0
        min_idx = (p1 if prices[p1] < prices[p2] else p2)
        while p2 < len(prices):
            if prices[p2] < prices[min_idx]:
                min_idx = p2
            if prices[p2] >= prices[p1]:
                rev = max(rev, prices[p2]-prices[p1])
            else:
                p1 = min_idx
                rev = max(rev, prices[p2]-prices[p1])

            p2 += 1
        return rev
        