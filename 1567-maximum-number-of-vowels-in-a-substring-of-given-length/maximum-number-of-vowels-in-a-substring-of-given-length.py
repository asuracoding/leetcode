class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'i', 'u','e','o'}
        total = max_windows = sum([1 if x in vowels else 0 for x in s[:k]])
        for x in range(len(s) - k):
            max_windows = max_windows -(1 if s[x] in vowels else 0) + (1 if s[x + k] in vowels else 0)
            
            total = max(total, max_windows)
        return total