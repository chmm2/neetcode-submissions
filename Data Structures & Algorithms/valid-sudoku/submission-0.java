class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<String, Set<Character>> square = new HashMap<>();

        for(int r=0; r<9; r++)
        {
            for(int c=0; c<9; c++)
            {
                if(board[r][c] == '.') continue;

                String key = (r/3) + "," + (c/3);

                if(rows.computeIfAbsent(r,k-> new HashSet<>()).contains(board[r][c]) ||
                cols.computeIfAbsent(c,k-> new HashSet<>()).contains(board[r][c]) ||
                square.computeIfAbsent(key,k-> new HashSet<>()).contains(board[r][c])) return false;

                rows.get(r).add(board[r][c]);
                cols.get(c).add(board[r][c]);
                square.get(key).add(board[r][c]);
            }
        }
        return true;
    }
}
