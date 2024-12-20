class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {')': '(', '}': '{', ']': '['}
        stk = []
        for val in s:
            if val in parenthesis.values():
                stk.append(val)
            elif val in parenthesis:
                if stk and parenthesis[val] == stk[-1]:
                    stk.pop()
                else:
                    return False
        return True if not stk else False

