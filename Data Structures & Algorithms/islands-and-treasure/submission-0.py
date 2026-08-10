class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647 
        dirs = [0,1,0,-1,0]
        if grid is None or len(grid)==0:
            return 
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr = r+dirs[i]
                nc = c+dirs[i+1]    

                if nr>=0 and nc>=0 and nr<ROWS and nc<COLS and grid[nr][nc] == INF:
                    grid[nr][nc] = min(grid[nr][nc], grid[r][c]+1)
                    q.append((nr,nc))