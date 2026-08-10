class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
             return False

        memo = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True

            if memo[i][j] != -1:
                return memo[i][j]

            ans = False

            if i < len(s1) and s1[i] == s3[i + j]:
                ans = ans or dfs(i + 1, j)

            if j < len(s2) and s2[j] == s3[i + j]:
                ans = ans or dfs(i, j + 1)

            memo[i][j] = ans
            return ans

        return dfs(0, 0)