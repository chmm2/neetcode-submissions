class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxList = []
        n = len(nums)
        for i in range(n-k+1):
            maxList.append(max(nums[i:i+k]))
        return maxList