class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left,right = 0,len(s)-1
        l_c,r_c =0,0
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        while left < right:
            if s[left] in vowels:
                l_c += 1
            if s[right] in vowels:
                r_c += 1
            left += 1
            right -= 1
        if l_c == r_c:
            return True
        return False

