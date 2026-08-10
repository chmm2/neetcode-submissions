class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = []
        res = [-1]*len(queries)
        i = 0
        for idx, q in sorted(enumerate(queries), key=lambda x: x[1]):
            while i<len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(heap, (r-l+1, r))
                i+=1
            
            while heap and heap[0][1]<q: #Already ended before the "q"
                heapq.heappop(heap)
            
            if heap:
                res[idx] = heap[0][0]
        return res