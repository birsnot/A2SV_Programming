class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = 0
        for ch in p:
            target += hash(ch)
        check = 0
        N = len(p)
        for ch in s[:N]:
            check += hash(ch)
        ans = []
        if check == target: ans.append(0)
        for i, ch in enumerate(s[N:]):
            check += hash(ch) - hash(s[i])
            if check == target:
                ans.append(i+1)
        return ans