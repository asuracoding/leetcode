class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = nums[:k]
        window_sum = max_res = sum(window)
        for x in range(len(nums)-k):
            window_sum = window_sum - nums[x] + nums[x+k]
            max_res = max(max_res, window_sum)
        return max_res / k