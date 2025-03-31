# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        arr = ['(',')']
        def generate_paren(idx,temp):
            open = temp.count('(')
            close = temp.count(')')
            if close == open and n*2 == len(temp):
                res.append(''.join(temp))
                return
            if close > open or open > n:
                return 
            for i in range(len(arr)):
                temp.append(arr[i])
                generate_paren(i,temp)
                temp.pop()     
            
        generate_paren(0,[])
        return res
