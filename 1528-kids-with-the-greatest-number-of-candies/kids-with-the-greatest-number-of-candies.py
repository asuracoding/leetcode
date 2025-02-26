class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)

        return [True if x + extraCandies >= max_c else False for x in candies]
        