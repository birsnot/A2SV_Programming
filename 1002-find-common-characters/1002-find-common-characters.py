class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        chars = [100]*26
        for word in words:
            temp = [0]*26
            for ch in word:
                temp[ord(ch)-97] += 1
            for i, count in enumerate(zip(chars, temp)):
                chars[i] = min(count)
        ans = []
        for i in range(26):
            ch = chr(97+i)
            for count in range(chars[i]):
                ans.append(ch)
        return ans