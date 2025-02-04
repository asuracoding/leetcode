class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = 1
        total = sum(nums)
        for x in range(len(nums)):
            if left == total - left - nums[x]:
                return  x
            left +=nums[x]
        return -1
        # while left <= len(nums)-1:
        #     prefix = sum(nums[:left])
        #     suffix = sum(nums[right:])
        #     if prefix == suffix:
        #         return right-1
        #     left+=1
        #     right+=1
        return -1
