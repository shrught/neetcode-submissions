class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        curA = 0

        l, r = 0, len(heights) - 1

        while(l < r):
            width = r - l
            height = min(heights[l], heights[r])
            curA = width * height
            maxA = max(maxA, curA)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        return maxA 

        