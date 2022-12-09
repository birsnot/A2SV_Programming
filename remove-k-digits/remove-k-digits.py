class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        dgts = {}
        i = count = j = 0
        mn = "a"
        for dgt in num:
            if dgt == '0':
                k -= count
                count = 0
                dgts = {}
                mn = "a"
                j = i+1
            elif count == k: break
            else:
                dgts[dgt] = dgts.get(dgt,0)+1
                count += 1
                if dgt < mn:
                    mn = dgt
            i += 1
        ans = ""
        for k,dgt in enumerate(num[i:]):
            if dgt < mn:
                ans += num[i+k:]
                break
            dgts[dgt] = dgts.get(dgt,0)+1
            ans += mn
            if dgts[mn] == 1: del dgts[mn]
            else: dgts[mn] -= 1
            while num[j] != mn:
                if dgts[num[j]] == 1: del dgts[num[j]]
                else: dgts[num[j]] -= 1
                j += 1
            j += 1
            mn = min(dgts)
        if not ans: return "0"
        return ans
