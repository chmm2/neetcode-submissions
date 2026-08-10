
from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0:
            return False
        
        k = total//2
        
        @cache
        def dfs(i, target):
            if target == 0:
                return True
            if i == 0:
                return nums[i] == target
            
            noTake = dfs(i-1, target)
            take = False
            if target > nums[i]:
                take = dfs(i-1, target-nums[i])

            return take|noTake
    
        return dfs(len(nums)-1, k)