class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        res = -1
        for station in range(n):
            fuel = 0
            for i in range(station, n+station):
                if i >= n:
                    fuel+=gas[i%n]-cost[i%n]
                else:
                    fuel+=gas[i]-cost[i]
                if fuel<0:
                    break
            if fuel>=0:
                res = station
                break
                

        return res