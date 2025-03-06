# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        file = path.split('/')
        for i in range(len(file)):
        
            if stk and file[i] == '..':
                stk.pop()
            elif file[i] and file[i] != '..' and file[i] != '.':
                stk.append('/'+file[i])
        return ''.join(stk) if stk else '/'
       