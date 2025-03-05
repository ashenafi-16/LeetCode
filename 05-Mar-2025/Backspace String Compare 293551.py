# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk = []
        stk2 = []
        for char in s:
            if char == '#':
                if stk:
                    stk.pop()
            else:
                stk.append(char)
        for char in t:
            if char == '#':
                if stk2:
                    stk2.pop()
            else:
                stk2.append(char)
        return "".join(stk) == "".join(stk2)