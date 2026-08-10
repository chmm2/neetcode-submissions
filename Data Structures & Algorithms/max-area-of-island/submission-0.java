class Solution {
    public static final int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
    public int count = 0;
    public int maxAreaOfIsland(int[][] grid) {
        int ROWS = grid.length;
        int COLS = grid[0].length;
        int area = 0;
        for(int r=0; r<ROWS; r++)
        {
            for(int c=0; c<COLS; c++)
            {
                if(grid[r][c]==1)
                {
                    count = 0;
                    count = dfs(grid, r, c);
                     area = Math.max(count, area);
                }
            }
        }
        return area;
    }

    public int dfs(int[][] grid, int r, int c)
    {
        if(r<0||c<0||r>=grid.length||c>=grid[0].length||grid[r][c]==0)
        {
            return 0;
        }

        count++;
        grid[r][c] = 0;
        for(int[] dir:directions)
        {
            dfs(grid, r+dir[0], c+dir[1]);
        }
        return count;
    }
}
