class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for x in prerequisites:
            adj[x[1]].append(x[0])
            indegree[x[0]] += 1

        q = collections.deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for nei in adj[course]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        

        return res if len(res)==numCourses else []