class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best, cur = nums[0],0
        for num in nums:
            if cur<0:
                cur = 0
            cur += num
            best = max(best,cur)
            
        return best