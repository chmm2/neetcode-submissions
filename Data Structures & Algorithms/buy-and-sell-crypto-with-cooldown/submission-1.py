from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dfs(i, buy):
            if i>=len(prices):
                return 0
            
            if buy:
                return max(-prices[i] + dfs(i+1,0), 0 + dfs(i+1,1))
            return max(prices[i]+dfs(i+2, 1), 0+dfs(i+1,0))
        
        return dfs(0,1)