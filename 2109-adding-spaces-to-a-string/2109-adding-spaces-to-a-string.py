class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        left = 0
        for idx in spaces:
            ans.append(s[left:idx])
            left = idx
        ans.append(s[left:])
        return " ".join(ans)