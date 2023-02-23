class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        chars = defaultdict(int)
        max_key = s[0]
        for i, ch in enumerate(s):
            chars[ch] += 1
            max_key = max(chars, key=chars.get)
            if i - l + 1 - chars[max_key] > k:
                chars[s[l]] -= 1
                l += 1
        return len(s) - l