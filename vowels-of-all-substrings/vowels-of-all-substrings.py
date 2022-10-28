class Solution:
    def countVowels(self, word: str) -> int:
        ans = incr = 0
        v = {'a','e','i','o','u'}
        for i,ch in enumerate(word,1):
            if ch in v:
                incr += i
            ans += incr
        return ans
