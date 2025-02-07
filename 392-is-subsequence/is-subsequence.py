class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = []
        left, right = 0, len(t)
        for x in s:
            while left < right and x in list(t):
                if x == t[left]:
                    res.append(t[left])
                    left +=1
                    break
                else: 
                    left+=1
        if len(res) == len(s):
            return True
        else:
            return False

        
