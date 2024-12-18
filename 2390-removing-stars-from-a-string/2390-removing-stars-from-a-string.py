class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for char in s:
            if char == '*':
                if stk:
                    stk.pop()
            else:
                stk.append(char)
        return "".join(stk)