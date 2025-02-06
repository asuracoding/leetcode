class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','i','u','e','o','A','I','U','E','O'}
        left, right = 0,len(s) -1
        s_list = list(s)
        while left < right:
            if s_list[left] in vowels:
                if s_list[right] in vowels:
                    print(f"found {s_list[left]} and {s_list[right]}")
                    s_list[left], s_list[right] = s_list[right], s_list[left]
                    left +=1
                    right -=1
                else:
                    right -= 1
            else:
                left +=1
        return "".join(x for x in s_list)

