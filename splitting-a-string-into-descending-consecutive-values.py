class Solution:
    def splitString(self, s: str) -> bool:
        sofar = []

        def backtrack(i):
            if i == len(s):
                return len(sofar) > 1
            for j in range(i + 1, len(s) + 1):
                n = int(s[i:j])
                if not sofar or sofar[-1] == n + 1:
                    sofar.append(n)
                    if backtrack(j):
                        return True
                    sofar.pop()
                elif sofar[-1] <= n:
                    break
        return backtrack(0)