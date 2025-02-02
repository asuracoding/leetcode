class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        total = []
        for x in candies:
            if x+extraCandies >= max_c:
                total.append(True)
            else:
                total.append(False)
        return total
        