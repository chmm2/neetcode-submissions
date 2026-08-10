class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x) 
        
        visit = [False]*n
        def dfs(x):
            for nei in adj[x]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                res+=1
        
        return res