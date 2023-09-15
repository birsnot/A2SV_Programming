class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda e: e[1], reverse=True)
        envelopes.sort(key=lambda e: e[0])
        sub = [0]
        for _, n in envelopes:
            if sub[-1] < n:
                sub.append(n)
            else:
                sub[bisect_left(sub, n)] = n
        return len(sub) - 1