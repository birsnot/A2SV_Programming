class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        pow_2s = []
        temp = 1
        for p in range(22):
            pow_2s.append(temp)
            temp *= 2
        ans = 0
        for pow_2 in pow_2s:
            pairs = {}
            for n in deliciousness:
                if n <= pow_2:
                    pair = pow_2-n
                    if pair in pairs:
                        ans += pairs[pair]
                    if n in pairs:
                        pairs[n] += 1
                    else:
                        pairs[n] = 1
        return ans%(1000000007)