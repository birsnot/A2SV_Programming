class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        st_ch = needle[0]
        end_ch = needle[-1]
        l = 0
        r = len(needle) - 1
        N = len(haystack)
        while r < N:
            if haystack[l] == st_ch and haystack[r] == end_ch:
                i = l + 1
                j = 1
                while i < r and needle[j] == haystack[i]:
                    i += 1
                    j += 1
                if i >= r: return l
            l += 1
            r += 1
        return -1