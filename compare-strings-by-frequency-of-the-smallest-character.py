class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(word):
            ch = min(word)
            return word.count(ch)
        fs = [0]*len(words)
        for i, word in enumerate(words):
            fs[i] = -f(word)
        fs.sort()
        ans = [0]*len(queries)
        for i, q in enumerate(queries):
            ans[i] = bisect_left(fs, -f(q))
        return ans