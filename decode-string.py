class Solution:
    def decodeString(self, s: str) -> str:
        N = len(s)
        i = 0
        def helper(n):
            nonlocal i
            ans = []
            while i < N:
                if s[i].isdigit():
                    st = i
                    while s[i].isdigit():
                        i += 1
                    new_n = int(s[st:i])
                    i += 1
                    ans.extend(helper(new_n))
                elif s[i] == "]":
                    temp = ans.copy()
                    for _ in range(n-1):
                        ans.extend(temp)
                    return ans
                else:
                    ans.append(s[i])
                i += 1
            return ans
        return "".join(helper(1))