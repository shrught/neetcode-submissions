class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[ROWS - 1][COLS - 1]:
            return False

        srow, erow = 0, ROWS - 1
        scol, ecol = 0, COLS - 1

        while srow <= erow:
            midrow = (srow + erow) // 2
            if target < matrix[midrow][0]:
                erow = midrow - 1
            elif target > matrix[midrow][COLS - 1]:
                srow = midrow + 1
            else:
                break

        while scol <= ecol:
            midcol = (scol + ecol) // 2
            if target == matrix[midrow][midcol]:
                return True
            if target < matrix[midrow][midcol]:
                ecol = midcol - 1
            if target > matrix[midrow][midcol]:
                scol = midcol + 1

        return False
        

            