class Solution:
    def reverseWords(self, s: str) -> str:

        stack = []
        s = s.split(" ")
        s = reversed(s)
        
        return " ".join(x for x in s if x !="")