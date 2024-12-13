class Solution:
    def reverseVowels(self, s: str) -> str:
       vowels={'a','e','i','o','u','A','E','I','O','U'}
       st_list = list(s)
       left ,right = 0,len(st_list)-1
       while left < right:
        if st_list[left] not in vowels:
            left += 1
        elif st_list[right] not in vowels:
            right -= 1
        else:
            st_list[right],st_list[left] = st_list[left],st_list[right]
            right -= 1
            left += 1
       return "".join(st_list)