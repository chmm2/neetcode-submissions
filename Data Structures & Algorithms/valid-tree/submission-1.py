class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        q = deque([(0,-1)])
        visit = set()
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))

        return len(visit) == n