class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {i: -1 for i in range(len(nums))}

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if memo[i] != -1:
                return memo[i]

            lis = 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    lis = max(lis, 1 + dfs(j))
                
            memo[i] = lis
            return memo[i]

        curmax = 0
        maxLis = 0
        for i in range(len(nums)):
            curmax = max(curmax, dfs(i))
            maxLis = max(curmax, maxLis)

        return maxLis