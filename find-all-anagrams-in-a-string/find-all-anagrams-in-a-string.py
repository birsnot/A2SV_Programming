class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        p_count = {}
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1
        N = len(p)
        n = 0
        ch_count = {}
        for key in p_count:
            ch_count[key] = 0
        ans = []
        i = 0
        for j, ch in enumerate(s):
            if ch not in ch_count:
                i = j+1
                for key in ch_count:
                    ch_count[key] = 0
                    n = 0
            else:
                if ch_count[ch] == p_count[ch]:
                    while s[i] != ch:
                        ch_count[s[i]] -= 1
                        i += 1
                        n -= 1
                    i += 1
                else:
                    ch_count[ch] += 1
                    n += 1
                if n == N:
                    ans.append(i)
        return ans
