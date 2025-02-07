class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        #prefix
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *=nums[i]
        
        #suffix
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        print(f"suffix {prefix}\n prefix {suffix}")
        return output