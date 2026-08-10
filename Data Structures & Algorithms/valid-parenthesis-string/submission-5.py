from functools import cache

class Solution:
    def checkValidString(self, s: str) -> bool:

        @cache
        def dfs(ind, count):
            if count < 0:
                return False

            if ind == len(s):
                return count == 0

            if s[ind] == "(":
                return dfs(ind + 1, count + 1)

            if s[ind] == ")":
                return dfs(ind + 1, count - 1)

            return (
                dfs(ind + 1, count + 1) or
                dfs(ind + 1, count - 1) or
                dfs(ind + 1, count)
            )

        return dfs(0, 0)