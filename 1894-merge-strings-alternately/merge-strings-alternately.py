class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combi_str = ''
        left, right = 0, 0
        while left < len(word1) or right < len(word2):
            
            if left < len(word1):
                combi_str += word1[left]
                left+=1

            if right < len(word2):
                combi_str += word2[right]
                right+=1
            print(combi_str)
        return combi_str