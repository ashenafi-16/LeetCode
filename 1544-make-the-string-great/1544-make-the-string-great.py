class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for ch in s:
            if ch.isupper() and stk:
                if ch.lower() == stk[-1]:
                    stk.pop()
                else:
                    stk.append(ch)
            elif ch.islower() and stk:
                if ch.upper() == stk[-1]:
                    stk.pop()
                else:
                    stk.append(ch)
            else:
                stk.append(ch)
                
        return "".join(stk)
