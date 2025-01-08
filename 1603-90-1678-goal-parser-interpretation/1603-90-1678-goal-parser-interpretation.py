class Solution:
    def interpret(self, command: str) -> str:
        stk = []
        for i in range(len(command)):
            if command[i] == ')':
                if stk and stk[-1] == '(':
                    stk.pop()
                    stk.append('o')
                else:
                    index = len(stk)-1
                    while stk[index] != '(':
                        index -= 1
                    del stk[index]
            else:
                stk.append(command[i])
        return "".join(stk)