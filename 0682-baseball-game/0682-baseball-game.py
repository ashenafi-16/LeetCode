class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for val in operations:
            if val == '+':
                op1 = stk[-1]
                op2 = stk[-2]
                stk.append(op1 + op2)
            elif val == 'C':
                stk.pop()
            elif val == 'D':
                stk.append(stk[-1]*2)
            else:
                stk.append(int(val))
        return sum(stk)
