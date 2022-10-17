class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '(':
                stack.append("")
            elif not stack:
                stack.append(ch)
            elif ch == ')':
                temp = stack.pop()[::-1]
                if not stack:
                    stack.append(temp)
                else:
                    stack[-1] += temp
            else:
                stack[-1] += ch
        
        return stack[0]
