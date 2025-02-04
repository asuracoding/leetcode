class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for x in range(len(s)):
            if s[x] =="*":
                stack.pop()
            else:
                stack.append(s[x])
        return "".join(x for x in stack)