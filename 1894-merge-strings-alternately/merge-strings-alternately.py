class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combi_str = ''
        len_1 = len(word1)
        len_2 = len(word2)

        for x in range(max(len_1,len_2)):
            if x < len_1:
                combi_str +=word1[x]
            if x < len_2:
                combi_str +=word2[x]

        return combi_str
