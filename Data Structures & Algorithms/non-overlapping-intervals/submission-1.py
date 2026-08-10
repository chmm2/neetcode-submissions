class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prevNum = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            if start>=prevNum:
                prevNum = end
            else:
                res+=1
                prevNum = min(prevNum, end)
        return res