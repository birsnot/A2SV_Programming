class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = 0
        for letter in uppers:
            l = 0
            count = 0
            for i, ch in enumerate(s):
                if ch != letter:
                    count += 1
                if count > k:
                    count -= (s[l] != letter)
                    l += 1
            ans = max(ans, len(s) - l)
        return ans