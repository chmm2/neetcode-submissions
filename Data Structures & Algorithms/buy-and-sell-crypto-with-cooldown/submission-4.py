class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, buy):
            if i >= len(prices):
                return 0

            if (i, buy) in memo:
                return memo[(i, buy)]

            if buy:
                memo[(i, buy)] = max(
                    -prices[i] + dfs(i+1, 0),
                    dfs(i+1, 1)
                )
            else:
                memo[(i, buy)] = max(
                    prices[i] + dfs(i+2, 1),
                    dfs(i+1, 0)
                )

            return memo[(i, buy)]
        return dfs(0,1)