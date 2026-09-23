class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = float("-inf")
        maxSum = float("-inf")

        for i in range(len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            maxSum = max(curSum, maxSum)

        return maxSum
