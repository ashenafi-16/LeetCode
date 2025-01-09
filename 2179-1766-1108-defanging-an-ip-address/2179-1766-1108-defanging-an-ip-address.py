class Solution:
    def defangIPaddr(self, address: str) -> str:
        stk = []
        for i in range(len(address)):
            if address[i] == '.':
                stk.append('[.]')
            else:
                stk.append(address[i])
        return "".join(stk)