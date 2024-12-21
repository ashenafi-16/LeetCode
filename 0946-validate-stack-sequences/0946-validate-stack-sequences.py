class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l=r=0
        stk = []
        while l < len(pushed):
            stk.append(pushed[l])
            l += 1
            while stk and stk[-1] == popped[r]:
                stk.pop()
                r += 1
        return True if not stk else False