# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        value = []
        def rec(temp):
            if len(temp) == n:
                value.append(''.join(temp))
                return 
            
            if temp and temp[-1] == '0':
                rec(temp + '1')
            else:
                rec(temp + '0')
                rec(temp + '1')

        rec('')
        return value
            
        


