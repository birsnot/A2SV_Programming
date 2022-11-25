class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        N = len(pushed)
        i = 0
        stack = []
        for n in popped:
            if stack and stack[-1] == n: stack.pop()
            else:
                while i < N and pushed[i] != n:
                    stack.append(pushed[i])
                    i += 1
                if i == N: return False
                i += 1
        return True
