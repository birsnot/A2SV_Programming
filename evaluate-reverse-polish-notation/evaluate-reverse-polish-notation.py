class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(n, m):
            return n+m

        def mul(n, m):
            return n*m

        def div(n, m):
            return int(n/m)

        def sub(n, m):
            return n-m

        funcs = {'+': add, '*': mul, '/': div, '-': sub}

        stack = []

        for p in tokens:
            if p not in funcs:
                stack.append(int(p))
            else:
                m = stack.pop()
                n = stack.pop()
                stack.append(funcs[p](n, m))
        return stack[0]
