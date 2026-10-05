class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        steps = 0


        while r < len(nums) - 1:
            curMax = 0
            
            for i in range(l, r + 1):
                curMax = max(curMax, i + nums[i])
            
            l = r + 1
            r = curMax
            steps += 1
        
        return steps