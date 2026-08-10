class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        def dfs(i, target):
            if i < 0:
                return 1 if target == 0 else 0

            
            sub = dfs(i-1, target+nums[i])

            add = dfs(i-1, target-nums[i])

            return add+sub

        return dfs(len(nums)-1, target)