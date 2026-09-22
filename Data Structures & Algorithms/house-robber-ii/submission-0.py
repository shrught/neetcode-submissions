class Solution:
    def rob(self, nums: List[int]) -> int:
        #two options 
        #1. start from first house to second last
        #2. start from second to the last
        if len(nums) == 1:
            return nums[0]
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            if i >= len(nums) or (flag == True and i == len(nums) - 1):
                return 0
            
            if memo[i][flag] != -1:
                return memo[i][flag]


            memo[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i 
            + 2, flag or (i == 0)))
            return memo[i][flag]

        return max(dfs(0, True), dfs(1, False))

