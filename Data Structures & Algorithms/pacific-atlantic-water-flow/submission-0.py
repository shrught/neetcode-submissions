class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        ROWS, COLS = len(heights), len(heights[0])


        
        def dfs(r, c, visit, prevHeight):
            #skip conditions: 1. r or c < 0 or r >= ROWS or c >= COLS(out of bounds)
            #2. current height > prevHeight (water can't flow through)
            #3. (r, c) in visit (avoid cycles)
            if ((r, c) in visit or r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prevHeight):
                return

            visit.add((r, c))
            #traverse through 4 separate directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        #
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res 


