class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arrx = [0]
        for x in range(len(gain)):
            arrx.append(arrx[x] + gain[x])
        return max(arrx)
        