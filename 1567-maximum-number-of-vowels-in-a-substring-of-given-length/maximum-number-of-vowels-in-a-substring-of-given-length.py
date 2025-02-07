class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','i','u','e','o'}

        window = s[:k]
        current_vowels = max_vowels = len([x for x in window if x in vowels])
        for x in range(len(s) - k):
            print(f"removing {s[x]} and got {s[x+k]}")
            if s[x] in vowels:
                current_vowels -=1
            
            if s[x + k] in vowels:
                current_vowels +=1
                max_vowels = max(current_vowels, max_vowels)
            print(f"total are {max_vowels}")
        return max_vowels