class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = 0
        for ch in s1:
            target += hash(ch)
        N = len(s1)
        check = 0
        if N > len(s2): return False
        for ch in s2[:N]:
            check += hash(ch)
        if check == target: return True
        l = 0
        for ch in s2[N:]:
            check += hash(ch) - hash(s2[l])
            l += 1
            if check == target:
                return True
        return False