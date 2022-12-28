class Solution:
    def similarPairs(self, words: List[str]) -> int:
        hashs = {}
        ans = 0
        for word in words:
            ch_set = set(word)
            hash_ = 0
            for ch in ch_set:
                hash_ += hash(ch)
            if hash_ in hashs:
                ans += hashs[hash_]
                hashs[hash_] += 1
            else:
                hashs[hash_] = 1
        return ans