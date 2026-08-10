class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        highMax = r
        while(l<=r):
            midHour = (l+r)//2
            till_max = 0
            for x in piles:
                till_max += math.ceil(x/midHour)

            if till_max > h :
                l = midHour + 1
            else:
                highMax = midHour
                r = midHour - 1
            
        
        return highMax 