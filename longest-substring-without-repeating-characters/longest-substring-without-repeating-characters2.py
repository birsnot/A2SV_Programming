class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = -1
        chars = {}
        ans = 0
        for i,ch in enumerate(s):
            if ch in chars and chars[ch] > j:
                j = chars[ch]
            elif ans < i-j:
                    ans = i-j
            chars[ch] = i
        return ans
