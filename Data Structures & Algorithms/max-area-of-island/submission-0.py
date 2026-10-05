class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()


        def dfs(r, c):
            if (r >= ROWS or r < 0 or c >= COLS or grid[r][c] == 0 or c < 0 or (r, c) in visit):
                return 0
            
            visit.add((r, c))
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))

        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r, c))

        return maxArea
            
        