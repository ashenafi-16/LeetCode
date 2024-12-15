class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0 
        s_list = list(s)
        right = len(s_list)-1
        while left < right:
            if not s_list[left].isalpha():
                left += 1
            if not s_list[right].isalpha():
                right -= 1
            if s_list[right].isalpha() and s_list[left].isalpha():
                temp = s_list[right]
                s_list[right],s_list[left] = s_list[left],s_list[right]
                right -= 1
                left += 1
        return "".join(s_list)