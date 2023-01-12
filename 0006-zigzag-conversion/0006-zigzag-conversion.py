class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        jump1 = numRows*2 - 2
        jump2 = 0
        ans = ""
        str_len = len(s)
        for r in range(numRows):
            i = r
            if jump1 and jump2:
                while i < str_len:
                    ans += s[i]
                    i += jump1
                    if i < str_len:
                        ans += s[i]
                        i += jump2
            elif jump1:
                while i < str_len:
                    ans += s[i]
                    i += jump1
            else:
                while i < str_len:
                    ans += s[i]
                    i += jump2
            jump1 -= 2
            jump2 += 2
        return ans