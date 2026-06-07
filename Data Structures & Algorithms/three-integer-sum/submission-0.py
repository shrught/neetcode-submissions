class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):

            #all the rest of the arrays sum can't be smaller than 0
            if nums[i] > 0:
                break

            #skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = 0 - nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    #skip duplicate
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                if nums[l] + nums[r] > target:
                    r -= 1
                if nums[l] + nums[r] < target:
                    l += 1
                
        return res

        