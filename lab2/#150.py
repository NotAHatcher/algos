class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+-*/':
                r = stack.pop()
                l = stack.pop()
                if i == '+':
                    stack.append(l+r)
                elif i == '-':
                    stack.append(l-r)
                elif i == '*':
                    stack.append(l*r)
                else:
                    stack.append(int(l/r))
            else:
                stack.append(int(i))

        return stack[-1]