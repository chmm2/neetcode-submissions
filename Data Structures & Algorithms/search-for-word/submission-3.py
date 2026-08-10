class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        present = False
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, w, i):
            if (i not in range(len(word)) or r not in range(ROWS) or c not in range(COLS) or board[r][c]!=word[i] or (r,c) in visited):
                return

            w+=board[r][c]
            visited.add((r,c))
            
            dfs(r+1, c, w, i+1)
            dfs(r, c+1, w, i+1)
            dfs(r-1, c, w, i+1)
            dfs(r, c-1, w, i+1)

            visited.remove((r,c))
            
            if (w==word):
                nonlocal present
                present = True
                return

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,"",0)
        
        return present