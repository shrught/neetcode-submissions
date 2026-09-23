class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # a cell c[m][n]'s all unique paths is the sum of all unique paths from c[m][n-1] and c[m-1][n]

        memo = {}

        def dp(r, c):
            if r >= m or c >= n:
                return 0
            
            if r == m - 1 and c == n - 1:
                return 1

            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = dp(r, c + 1) + dp(r + 1, c)
            return memo[(r, c)]

        return dp(0, 0)