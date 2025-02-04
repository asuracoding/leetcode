class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[k-1]
        elif len(nums) == k:
            return sum(nums[:k]) / k

        max_sum, current_sum = sum(nums[:k]), sum(nums[:k])

        for i in range(len(nums) - k):
            current_sum =  (current_sum - nums[i]) + nums[i+k]
            max_sum = max(current_sum, max_sum)

        return max_sum / k
            