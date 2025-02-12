class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_max = current_sum = 0
        for x in gain:
            current_sum += x
            prefix_max = max(prefix_max, current_sum)

        return prefix_max