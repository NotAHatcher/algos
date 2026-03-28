class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if len(stack) > 0 and ((stack[-1] == '(' and i == ')') or (stack[-1] == '[' and i == ']')  or (stack[-1] == '{' and i == '}')):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False