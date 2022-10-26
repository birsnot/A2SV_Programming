class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        stack = deque()
        N = len(s)
        j = 0
        while j < N:
            if s[j].isdigit():
                n = s[j]
                j += 1
                while s[j] != '[':
                    n += s[j]
                    j += 1
                j += 1
                stack.append([int(n), ""])
            if j < N and s[j].islower():
                ss = s[j]
                j += 1
                while j < N and s[j].islower():
                    ss += s[j]
                    j += 1
                if stack:
                    stack[-1][1] += ss
                else:
                    ans += ss
            if j < N and s[j] == ']':
                last = stack.pop()
                if stack:
                    stack[-1][1] += last[0]*last[1]
                else:
                    ans += last[0]*last[1]
                j += 1
        return ans
