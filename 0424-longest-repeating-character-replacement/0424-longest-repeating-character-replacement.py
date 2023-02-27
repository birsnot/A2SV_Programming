class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        max_ = 0
        l = 0
        k_ = k
        for ch in s:
            chars[ch] += 1
            if chars[ch] > max_:
                max_ += 1
            else:
                k_ -= 1
            if k_ < 0:
                chars[s[l]] -= 1
                k_ += 1
                l += 1
        return max_ - k_ + k
                