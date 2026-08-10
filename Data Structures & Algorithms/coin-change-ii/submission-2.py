from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dfs(i, target):
            if target==0:
                return 1
            if i==0:
                return 1 if (target%coins[i]==0) else 0

            notTake = dfs(i-1, target)
            take = 0
            if coins[i]<=target:
                take = dfs(i, target-coins[i])
            
            return notTake +  take

        return dfs(len(coins)-1,amount)