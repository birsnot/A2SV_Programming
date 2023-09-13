class Solution:
    def reorganizeString(self, s: str) -> str:
        cnts = Counter(s)
        N = len(s)
        max_ch = max(cnts, key=lambda ch: cnts[ch])
        max_cnt = cnts[max_ch]
        if N < 2*max_cnt - 1: return ""
        ans = [[max_ch] for _ in range(max_cnt)]
        del cnts[max_ch]
        i = 0
        for ch in cnts:
            for _ in range(cnts[ch]):
                ans[i%max_cnt].append(ch)
                i += 1
        return "".join("".join(ans[i]) for i in range(max_cnt))