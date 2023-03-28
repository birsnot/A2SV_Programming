class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []
        cur = []
        ans = []
        N = len(s)
        def helper(i):
            if len(cur) == 3:
                num = s[i:]
                n = int(num)
                if (num[0] != "0" or num == "0") and n < 256:
                        ans.append(".".join(cur + [num]))
                return
            for j in range(i + 1, N):
                num = s[i:j]
                n = int(num)
                if (num[0] != "0" or num == "0") and n < 256:
                    cur.append(num)
                    helper(j)
                    cur.pop()
                else:
                    break
            return
        helper(0)
        return ans