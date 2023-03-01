class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        for ch in s:
            if ch == "(":
                stk.append("(")
            elif stk[-1] != "(":
                n = stk.pop()*2
                stk.pop()
                if stk and stk[-1] != "(":
                    stk[-1] += n
                else:
                    stk.append(n)
            else:
                if len(stk) > 1 and stk[-2] != "(":
                    stk.pop()
                    stk[-1] += 1
                else:
                    stk[-1] = 1
        return stk[0]