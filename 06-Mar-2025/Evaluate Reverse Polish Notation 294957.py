# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}  # Set of valid operators

        for c in tokens:
            if c not in operators:  
                stack.append(int(c))
            else:
                op1 = stack.pop()
                op2 = stack.pop()

                if c == "+":
                    stack.append(op2 + op1)
                elif c == "-":
                    stack.append(op2 - op1)
                elif c == "*":
                    stack.append(op2 * op1)
                elif c == "/":
                    stack.append(int(op2 / op1))

        return stack[0]