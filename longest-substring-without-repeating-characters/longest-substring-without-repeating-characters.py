class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        i = j = 0
        count = ans = 0
        while j < len(s):
            if s[j] in chars:
                while True:
                    chars.remove(s[i])
                    i += 1
                    count -= 1
                    if s[i-1] == s[j]:
                        break
            count += 1
            chars.add(s[j])
            ans = max(ans, count)
            j += 1
        return ans
