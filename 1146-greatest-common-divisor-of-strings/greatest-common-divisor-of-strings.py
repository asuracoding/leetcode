class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for x in range(len(str2),0,-1):
            splitter = str2[:x]
            res = str1.split(splitter)
            res_2 = str2.split(splitter)
            if all(x == '' for x in res) and all(y =='' for y in res_2):
                return str2[:x]
        return ""
        