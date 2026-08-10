class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subs = []
        
        def backtrack(subs):
            if len(subs) == len(nums):
                res.append(subs.copy())
            
            for num in nums:

                if num in subs:
                    continue
                
                subs.append(num)
                backtrack(subs)
                subs.pop()
        
        backtrack(subs)
        return res