class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = prefix = suffix = 0
        while pivot <len(nums):
            prefix = sum(nums[:pivot])
            suffix = sum(nums[pivot+1:])
            print(f"prefix is {prefix} suffix is {suffix}")
            if  prefix == suffix:
                return pivot
            pivot +=1
        return -1