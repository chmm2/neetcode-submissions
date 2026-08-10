class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for x in prerequisites:
            adj[x[1]].append(x[0])
            indegree[x[0]] += 1

        q = collections.deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        courseCount = 0
        while q:
            course = q.popleft()
            courseCount+=1
            for nei in adj[course]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        

        return courseCount==numCourses
                
        
