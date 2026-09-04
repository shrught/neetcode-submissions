class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
    
        res = nums[0]
        while(l <= r):
            #if in the sub array, return the min
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break
            
            #if not nums[l] > nums[r], means the array has been rotated and needs to perform a Binary Search
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res

            

