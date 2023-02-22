class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = defaultdict(int)
        count = i = 0
        for ch in s:
            chars[ch] += 1
            count += 1
            if len(chars) < count:
                count -= 1
                chars[s[i]] -= 1
                if chars[s[i]] == 0:
                    del chars[s[i]]
                i += 1
        return len(s) - i