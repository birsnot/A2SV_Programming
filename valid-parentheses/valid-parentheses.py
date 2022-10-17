class Solution:
    def isValid(self, s: str) -> bool:
        buffer = []
        for ch in s:
            if ch in '[{(':
                buffer.append(ch)
            elif len(buffer) == 0:
                return False
            else:
                if ch == ']':
                    if buffer.pop() != '[':
                        return False
                elif ch == ')':
                    if buffer.pop() != '(':
                        return False
                elif ch == '}':
                    if buffer.pop() != '{':
                        return False
        if len(buffer) == 0:
            return True
        else:
            return False
