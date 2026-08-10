class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = [[-1]*(amount+1) for _ in range(len(coins)+1)]

        def dfs(i, target):
            if target==0:
                return 1
            if i<0:
                return 0
            
            if memo[i][target] != -1:
                return memo[i][target]

            notTake = dfs(i-1, target)
            take = 0
            if coins[i]<=target:
                take = dfs(i, target-coins[i])
            
            memo[i][target] = notTake +  take
            return notTake +  take

        return dfs(len(coins)-1,amount)