__author__ = 'karthikb'
class Solution:
    # @return a boolean
    def isValid(self, s):
        forward_braces = ['{','[','(']
        back_braces = ['}',']',')']
        stack = []
        top = -1
        N = len(s)
        if s == '' or N <= 1:
            return 0
        for brack in s:
            if brack in forward_braces or top == -1:
                stack.append(brack)
                top += 1
            elif brack == ')' and stack[top] == '(':
                stack.pop()
                top -= 1
            elif brack == ']' and stack[top] == '[':
                stack.pop()
                top -= 1
            elif brack == '}' and stack[top] == '{':
                stack.pop()
                top -= 1
            else:
                return False
        if len(stack) == 0:
            return True
        return False

s = Solution()
print s.isValid("[])")



